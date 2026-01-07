"""
================================================================================
CareerMatch AI - Semi-Supervised Learning Module
================================================================================

Questo modulo implementa un layer di apprendimento SEMI-SUPERVISIONATO che:
1. PARTE dalle costanti (HARD_SKILLS, SOFT_SKILLS) come "seed knowledge"
2. USA i modelli ML esistenti (Random Forest, Clustering) come base
3. IMPARA AUTOMATICAMENTE nuove skill e pattern dai dati analizzati

================================================================================
RIFERIMENTI AL CORSO:
================================================================================
- "Semi-Supervised Learning": Combina labeled e unlabeled data
- "Label Propagation": Propaga etichette da dati labeled a unlabeled simili
- "Self-Training": Usa predizioni ad alta confidenza come nuove etichette

================================================================================
ALGORITMO PRINCIPALE:
================================================================================
1. Estrai skill con il modello Random Forest supervisionato
2. Per predizioni ad ALTA CONFIDENZA (>85%):
   - Cerca frasi simili nel testo (TF-IDF similarity)
   - Propaga l'etichetta alle frasi simili (Label Propagation)
   - Salva i nuovi pattern appresi (Persistenza JSON)
3. Nelle analisi successive, usa anche i pattern appresi

================================================================================
"""

import json
import os
from datetime import datetime
from typing import Dict, Set, List, Tuple, Optional
from collections import defaultdict

# Sklearn imports per similarity
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None
    np = None

import constants

# =============================================================================
# CONFIGURAZIONE
# =============================================================================
# Parametri del Semi-Supervised Learning

CONFIG = {
    # Soglia minima di confidenza per considerare una predizione "affidabile"
    # e usarla per espandere il knowledge base
    "HIGH_CONFIDENCE_THRESHOLD": 0.85,
    
    # Soglia di similarità coseno per propagare etichette
    # Un chunk di testo deve essere almeno 70% simile per ereditare l'etichetta
    "SIMILARITY_THRESHOLD": 0.70,
    
    # Numero massimo di pattern da apprendere per skill
    # Evita di accumulare troppi sinonimi rumorosi
    "MAX_PATTERNS_PER_SKILL": 20,
    
    # File di persistenza per i pattern appresi
    "PATTERNS_FILE": "learned_patterns.json",
    
    # Abilita/Disabilita il self-learning
    "LEARNING_ENABLED": True
}


# =============================================================================
# CLASSE PRINCIPALE: SemiSupervisedSkillLearner
# =============================================================================
class SemiSupervisedSkillLearner:
    """
    SEMI-SUPERVISED SKILL LEARNER
    ==============================
    Riferimento corso: "Semi-Supervised Learning", "Label Propagation"
    
    Questa classe implementa un sistema di apprendimento semi-supervisionato
    che combina:
    - SEED KNOWLEDGE: Le costanti definite (HARD_SKILLS, SOFT_SKILLS)
    - SUPERVISED PREDICTIONS: Output del Random Forest classifier
    - SELF-LEARNING: Pattern appresi automaticamente dai dati
    
    CICLO DI APPRENDIMENTO:
    -----------------------
    1. INPUT: Testo (CV o Job Description)
    2. ESTRAZIONE: Random Forest estrae skill con confidenza
    3. PROPAGAZIONE: Skill ad alta confidenza → cerca frasi simili
    4. APPRENDIMENTO: Salva nuovi pattern nel JSON
    5. OUTPUT: Skill estratte + skill inferite dai pattern appresi
    
    PERSISTENZA:
    ------------
    I pattern appresi sono salvati in `learned_patterns.json` e caricati
    all'avvio. Questo permette al modello di migliorare nel tempo.
    """
    
    def __init__(self, patterns_file: str = None):
        """
        Inizializza il learner con:
        - Seed knowledge dalle costanti
        - Pattern appresi da file JSON (se esiste)
        """
        self.patterns_file = patterns_file or CONFIG["PATTERNS_FILE"]
        
        # Determina il path assoluto del file patterns
        self.patterns_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            self.patterns_file
        )
        
        # Strutture dati per i pattern appresi
        # skill_synonyms: {"Python": ["ho usato python", "python developer"]}
        self.skill_synonyms: Dict[str, Set[str]] = defaultdict(set)
        
        # context_patterns: frasi di contesto associate a skill
        # {"Machine Learning": ["modelli predittivi", "training models"]}
        self.context_patterns: Dict[str, Set[str]] = defaultdict(set)
        
        # learned_associations: skill inferite da altre skill
        # [{"skill": "TensorFlow", "inferred_skills": ["Deep Learning", "Python"]}]
        self.learned_associations: List[Dict] = []
        
        # Statistiche di apprendimento
        self.stats = {
            "total_learned": 0,
            "last_updated": None,
            "learning_sessions": 0,
            "skills_enhanced": set()
        }
        
        # Carica pattern esistenti dal file
        self._load_patterns()
        
        # Inizializza TF-IDF vectorizer per similarity
        if TfidfVectorizer:
            self.vectorizer = TfidfVectorizer(
                ngram_range=(1, 3),
                max_features=1000,
                stop_words='english'
            )
        else:
            self.vectorizer = None
    
    # =========================================================================
    # PERSISTENZA: LOAD/SAVE
    # =========================================================================
    
    def _load_patterns(self):
        """
        CARICAMENTO PATTERN PERSISTENTI
        ================================
        Carica i pattern appresi dal file JSON.
        
        Questo permette al sistema di:
        - Ricordare ciò che ha imparato tra sessioni
        - Accumulare conoscenza nel tempo
        - Non ripartire da zero ad ogni avvio
        """
        if os.path.exists(self.patterns_path):
            try:
                with open(self.patterns_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Carica skill_synonyms (converti liste in set)
                for skill, synonyms in data.get("skill_synonyms", {}).items():
                    self.skill_synonyms[skill] = set(synonyms)
                
                # Carica context_patterns
                for skill, patterns in data.get("context_patterns", {}).items():
                    self.context_patterns[skill] = set(patterns)
                
                # Carica associazioni
                self.learned_associations = data.get("learned_associations", [])
                
                # Carica statistiche
                saved_stats = data.get("statistics", {})
                self.stats["total_learned"] = saved_stats.get("total_learned", 0)
                self.stats["last_updated"] = saved_stats.get("last_updated")
                self.stats["learning_sessions"] = saved_stats.get("learning_sessions", 0)
                self.stats["skills_enhanced"] = set(saved_stats.get("skills_enhanced", []))
                
                print(f"[Semi-Supervised] Caricati {self.stats['total_learned']} pattern appresi")
                
            except Exception as e:
                print(f"[Semi-Supervised] Errore caricamento pattern: {e}")
    
    def _save_patterns(self):
        """
        SALVATAGGIO PATTERN PERSISTENTI
        =================================
        Salva i pattern appresi nel file JSON.
        
        Struttura del file:
        {
            "skill_synonyms": {"Python": ["ho usato python", ...]},
            "context_patterns": {"ML": ["training models", ...]},
            "learned_associations": [...],
            "statistics": {...}
        }
        """
        try:
            data = {
                "skill_synonyms": {
                    skill: list(synonyms) 
                    for skill, synonyms in self.skill_synonyms.items()
                },
                "context_patterns": {
                    skill: list(patterns)
                    for skill, patterns in self.context_patterns.items()
                },
                "learned_associations": self.learned_associations,
                "statistics": {
                    "total_learned": self.stats["total_learned"],
                    "last_updated": datetime.now().isoformat(),
                    "learning_sessions": self.stats["learning_sessions"],
                    "skills_enhanced": list(self.stats["skills_enhanced"])
                }
            }
            
            with open(self.patterns_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            self.stats["last_updated"] = datetime.now().isoformat()
            
        except Exception as e:
            print(f"[Semi-Supervised] Errore salvataggio pattern: {e}")
    
    # =========================================================================
    # CORE: LABEL PROPAGATION
    # =========================================================================
    
    def propagate_labels(self, text: str, predictions: List[Tuple[str, float]]) -> Set[str]:
        """
        LABEL PROPAGATION
        ==================
        Riferimento corso: "Semi-Supervised Learning", "Label Propagation"
        
        Questo è il cuore dell'apprendimento semi-supervisionato.
        
        ALGORITMO:
        ----------
        1. Prendi le predizioni ad alta confidenza (>85%)
        2. Per ogni predizione affidabile:
           a. Dividi il testo in chunk (frasi)
           b. Calcola similarità TF-IDF tra chunk e skill
           c. Se similarità > 70%, propaga l'etichetta
           d. Salva il nuovo pattern
        
        Args:
            text: Testo originale (CV/Job Description)
            predictions: Lista di (skill, confidence) dal Random Forest
        
        Returns:
            Set di skill aggiuntive inferite dalla propagazione
        """
        if not CONFIG["LEARNING_ENABLED"]:
            return set()
        
        if not self.vectorizer or not cosine_similarity:
            return set()
        
        inferred_skills = set()
        
        # Filtra solo predizioni ad alta confidenza
        high_confidence = [
            (skill, conf) for skill, conf in predictions 
            if conf >= CONFIG["HIGH_CONFIDENCE_THRESHOLD"]
        ]
        
        if not high_confidence:
            return inferred_skills
        
        # Dividi il testo in chunk (frasi/righe)
        chunks = self._split_into_chunks(text)
        
        if len(chunks) < 2:
            return inferred_skills
        
        try:
            # Vectorizza tutti i chunk
            chunk_vectors = self.vectorizer.fit_transform(chunks)
            
            for skill, confidence in high_confidence:
                # Crea un vettore per la skill (usando le keyword note)
                skill_keywords = self._get_skill_keywords(skill)
                skill_text = " ".join(skill_keywords)
                
                if not skill_text.strip():
                    continue
                
                # Vectorizza la skill
                skill_vector = self.vectorizer.transform([skill_text])
                
                # Calcola similarità con tutti i chunk
                similarities = cosine_similarity(skill_vector, chunk_vectors)[0]
                
                # Propaga etichetta a chunk simili
                for i, sim in enumerate(similarities):
                    if sim >= CONFIG["SIMILARITY_THRESHOLD"]:
                        chunk = chunks[i].strip().lower()
                        
                        # Evita chunk troppo corti o già noti
                        if len(chunk) > 10 and chunk not in skill_keywords:
                            self._learn_pattern(skill, chunk, sim)
                            inferred_skills.add(skill)
            
            # Salva i pattern aggiornati
            if inferred_skills:
                self._save_patterns()
        
        except Exception as e:
            print(f"[Semi-Supervised] Errore propagazione: {e}")
        
        return inferred_skills
    
    def _split_into_chunks(self, text: str) -> List[str]:
        """
        Divide il testo in chunk per l'analisi.
        Usa una combinazione di righe e frasi.
        """
        import re
        
        # Split per righe e frasi
        chunks = []
        
        # Prima split per righe
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) > 5:
                # Poi split per frasi (., ;, -)
                sentences = re.split(r'[.;•\-]', line)
                for sent in sentences:
                    sent = sent.strip()
                    if len(sent) > 10:
                        chunks.append(sent)
        
        return chunks
    
    def _get_skill_keywords(self, skill: str) -> List[str]:
        """
        Recupera le keyword associate a una skill dal knowledge base.
        Combina costanti + pattern appresi.
        """
        keywords = []
        
        # Keyword dalle costanti
        hard_skills = getattr(constants, "HARD_SKILLS", {})
        soft_skills = getattr(constants, "SOFT_SKILLS", {})
        
        if skill in hard_skills:
            keywords.extend(hard_skills[skill])
        if skill in soft_skills:
            keywords.extend(soft_skills[skill])
        
        # Aggiungi pattern appresi
        if skill in self.skill_synonyms:
            keywords.extend(list(self.skill_synonyms[skill]))
        
        return keywords
    
    def _learn_pattern(self, skill: str, pattern: str, confidence: float):
        """
        APPRENDIMENTO DI UN NUOVO PATTERN
        ===================================
        Aggiunge un nuovo pattern al knowledge base.
        
        Controlli:
        - Non superare MAX_PATTERNS_PER_SKILL
        - Evita duplicati
        - Normalizza il pattern
        """
        # Normalizza
        pattern = pattern.lower().strip()
        
        # Evita pattern troppo corti o troppo lunghi
        if len(pattern) < 5 or len(pattern) > 100:
            return
        
        # Controlla limite
        if len(self.skill_synonyms[skill]) >= CONFIG["MAX_PATTERNS_PER_SKILL"]:
            return
        
        # Evita duplicati
        if pattern in self.skill_synonyms[skill]:
            return
        
        # Aggiungi pattern
        self.skill_synonyms[skill].add(pattern)
        self.stats["total_learned"] += 1
        self.stats["skills_enhanced"].add(skill)
        
        print(f"[Semi-Supervised] Learned: '{pattern}' → {skill} (conf: {confidence:.2f})")
    
    # =========================================================================
    # ENHANCEMENT: MIGLIORA ESTRAZIONE SKILL
    # =========================================================================
    
    def enhance_extraction(self, text: str, base_skills: Set[str]) -> Set[str]:
        """
        ENHANCE EXTRACTION CON PATTERN APPRESI
        ========================================
        Migliora l'estrazione di skill usando i pattern appresi.
        
        Questo metodo viene chiamato DOPO l'estrazione base del Random Forest.
        Cerca nel testo i pattern appresi precedentemente.
        
        Args:
            text: Testo da analizzare
            base_skills: Skill già estratte dal Random Forest
        
        Returns:
            Set combinato di skill (base + inferite dai pattern)
        """
        enhanced_skills = set(base_skills)
        text_lower = text.lower()
        
        # Cerca pattern appresi nel testo
        for skill, patterns in self.skill_synonyms.items():
            if skill not in enhanced_skills:
                for pattern in patterns:
                    if pattern in text_lower:
                        enhanced_skills.add(skill)
                        break
        
        # Cerca context patterns
        for skill, contexts in self.context_patterns.items():
            if skill not in enhanced_skills:
                for context in contexts:
                    if context in text_lower:
                        enhanced_skills.add(skill)
                        break
        
        return enhanced_skills
    
    def learn_from_context(self, text: str, confirmed_skills: Set[str]):
        """
        APPRENDIMENTO DAL CONTESTO
        ===========================
        Analizza il contesto delle skill confermate per imparare
        nuove frasi associative.
        
        Es: Se "Python" è confermato e vicino c'è "linguaggio di scripting",
        impara l'associazione.
        """
        if not CONFIG["LEARNING_ENABLED"]:
            return
        
        chunks = self._split_into_chunks(text)
        
        for skill in confirmed_skills:
            skill_keywords = self._get_skill_keywords(skill)
            
            for i, chunk in enumerate(chunks):
                chunk_lower = chunk.lower()
                
                # Verifica se il chunk contiene la skill
                if any(kw.lower() in chunk_lower for kw in skill_keywords):
                    # Salva anche chunk vicini come contesto
                    for j in range(max(0, i-1), min(len(chunks), i+2)):
                        if j != i:
                            context = chunks[j].strip().lower()
                            if len(context) > 10 and len(context) < 100:
                                if len(self.context_patterns[skill]) < CONFIG["MAX_PATTERNS_PER_SKILL"]:
                                    self.context_patterns[skill].add(context)
        
        self._save_patterns()
    
    # =========================================================================
    # STATISTICHE E REPORTING
    # =========================================================================
    
    def get_learning_stats(self) -> Dict:
        """
        Restituisce statistiche sull'apprendimento.
        Usato dal debugger nell'app.
        """
        return {
            "total_patterns_learned": self.stats["total_learned"],
            "skills_enhanced": len(self.stats["skills_enhanced"]),
            "last_updated": self.stats["last_updated"],
            "learning_sessions": self.stats["learning_sessions"],
            "skill_synonyms_count": sum(len(v) for v in self.skill_synonyms.values()),
            "context_patterns_count": sum(len(v) for v in self.context_patterns.values()),
            "top_enhanced_skills": list(self.stats["skills_enhanced"])[:10],
            "learning_enabled": CONFIG["LEARNING_ENABLED"]
        }
    
    def get_learned_patterns_for_skill(self, skill: str) -> Dict:
        """
        Restituisce tutti i pattern appresi per una specifica skill.
        """
        return {
            "synonyms": list(self.skill_synonyms.get(skill, set())),
            "context": list(self.context_patterns.get(skill, set()))
        }
    
    def start_learning_session(self):
        """
        Inizia una nuova sessione di apprendimento.
        Chiamato all'inizio di ogni analisi.
        """
        self.stats["learning_sessions"] += 1
    
    def reset_learned_patterns(self):
        """
        Resetta tutti i pattern appresi.
        Utile per testing o reset completo.
        """
        self.skill_synonyms = defaultdict(set)
        self.context_patterns = defaultdict(set)
        self.learned_associations = []
        self.stats = {
            "total_learned": 0,
            "last_updated": None,
            "learning_sessions": 0,
            "skills_enhanced": set()
        }
        self._save_patterns()
        print("[Semi-Supervised] Pattern resettati")


# =============================================================================
# ISTANZA GLOBALE (Singleton Pattern)
# =============================================================================
# Mantiene un'unica istanza del learner per tutta l'applicazione

_learner_instance: Optional[SemiSupervisedSkillLearner] = None

def get_learner() -> SemiSupervisedSkillLearner:
    """
    Restituisce l'istanza singleton del SemiSupervisedSkillLearner.
    Crea l'istanza al primo accesso.
    """
    global _learner_instance
    if _learner_instance is None:
        _learner_instance = SemiSupervisedSkillLearner()
    return _learner_instance


def enable_learning(enabled: bool = True):
    """Abilita o disabilita il self-learning."""
    CONFIG["LEARNING_ENABLED"] = enabled
    

def is_learning_enabled() -> bool:
    """Verifica se il self-learning è abilitato."""
    return CONFIG["LEARNING_ENABLED"]
