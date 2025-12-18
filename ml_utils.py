import re
# Force Streamlit Cloud Update
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List
import urllib.parse

# Optional Imports with robust handling
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.cluster import KMeans, AgglomerativeClustering
    from sklearn.decomposition import PCA
    import scipy.cluster.hierarchy as sch
    import matplotlib.pyplot as plt
except ImportError:
    RandomForestClassifier = None
    TfidfVectorizer = None
    Pipeline = None
    KMeans = None
    AgglomerativeClustering = None
    PCA = None
    sch = None
    plt = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from fpdf import FPDF
except ImportError:
    FPDF = None

import constants

# =============================================================================
# TRAINING (Used for Debugger & Future ML features)
# =============================================================================
@st.cache_resource
def train_rf_model():
    """
    Trains a Random Forest model on Hard Skills from constants.py.
    Returns (pipeline, dataframe).
    """
    # Prepare Data
    data = []
    
    # Check if HARD_SKILLS exists in constants (Backward compatibility)
    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})
    
    for skill_name, keywords in hard_skills.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})
            data.append({"text": f"used {kw}", "label": skill_name})
            
    for skill_name, keywords in soft_skills.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})

    df = pd.DataFrame(data)
    
    if df.empty:
        return None, df

    # If sklearn is missing or failed to import
    if not RandomForestClassifier or not TfidfVectorizer or not Pipeline:
        return None, df
        
    try:
        pipe = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=1000)),
            ('rf', RandomForestClassifier(n_estimators=50, random_state=42))
        ])
        pipe.fit(df['text'], df['label'])
        return pipe, df
    except Exception as e:
        print(f"Training Error: {e}")
        return None, df

# =============================================================================
# CLUSTERING (Unsupervised Learning for Skills)
# =============================================================================
def perform_skill_clustering(skills: List[str]):
    """
    Performs K-Means and Hierarchical Clustering on a list of skills.
    Returns:
    - kmeans_fig: Plotly figure for K-Means (PCA 2D)
    - dendrogram_img_path: Path to saved dendrogram image
    - clusters: Dict of {skill: cluster_id}
    """
    if not skills or len(skills) < 3:
        return None, None, {}

    if not TfidfVectorizer or not KMeans or not sch:
        return None, None, {}

    try:
        # 1. Vectorize Skills
        vectorizer = TfidfVectorizer(stop_words='english', min_df=1)
        X = vectorizer.fit_transform(skills).toarray()
        
        # 2. Hierarchical Clustering (Dendrogram)
        # Using Ward's linkage as per Lecture 02
        linkage_matrix = sch.linkage(X, method='ward')
        
        plt.figure(figsize=(10, 5))
        dendro = sch.dendrogram(linkage_matrix, labels=skills, leaf_rotation=90)
        plt.title("Skill Dendrogram (Hierarchical Clustering)")
        plt.tight_layout()
        dendro_path = "dendrogram.png"
        plt.savefig(dendro_path)
        plt.close()

        # 3. K-Means Clustering
        # Determine K (simple heuristic: sqrt(N/2) or max 3-5 for small skill sets)
        n_clusters = max(2, min(len(skills) // 3, 5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        
        skill_clusters = {skill: int(label) for skill, label in zip(skills, labels)}

        # 4. Visualization (PCA to 2D)
        pca = PCA(n_components=2)
        coords = pca.fit_transform(X)
        
        df_viz = pd.DataFrame({
            'x': coords[:, 0],
            'y': coords[:, 1],
            'skill': skills,
            'cluster': [f"Cluster {l}" for l in labels]
        })
        
        return df_viz, dendro_path, skill_clusters

    except Exception as e:
        print(f"Clustering Error: {e}")
        return None, None, {}

# --- NEW: TOPIC MODELING (LDA) ---
try:
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.feature_extraction.text import CountVectorizer
    from wordcloud import WordCloud
except ImportError:
    LatentDirichletAllocation = None
    CountVectorizer = None
    WordCloud = None

def perform_topic_modeling(text_corpus: List[str], n_topics=3, n_words=5):
    """
    Performs Latent Dirichlet Allocation (LDA) to extract topics from text.
    Returns a list of topics (each topic is a string of keywords) and a WordCloud image path.
    """
    if not LatentDirichletAllocation or not CountVectorizer or not WordCloud:
        return [], None

    try:
        # Custom Stop Words for HR/Recruiting Context (Aggressive)
        hr_stop_words = [
            # Structural / Sections
            'requirements', 'qualifications', 'responsibilities', 'duties', 'summary', 
            'overview', 'description', 'profile', 'benefits', 'education', 'experience', 
            'skills', 'background', 'about', 'us', 'team', 'company', 'role', 'job', 
            'position', 'candidate', 'opportunity', 'location', 'category', 'status',
            'salary', 'compensation', 'employment', 'type', 'industry', 'department',
            
            # Common Adjectives / Qualifiers
            'strong', 'excellent', 'good', 'great', 'proven', 'demonstrated', 'successful',
            'ideal', 'passionate', 'motivated', 'proactive', 'hands-on', 'detail-oriented',
            'dynamic', 'collaborative', 'fast-paced', 'global', 'international', 'leading',
            'preferred', 'plus', 'advantage', 'bonus', 'desirable', 'essential', 'key',
            'core', 'primary', 'required', 'proficient', 'proficiency', 'fluent',
            'knowledge', 'understanding', 'familiarity', 'ability', 'capability', 
            
            # Common Verbs / Actions
            'work', 'working', 'join', 'apply', 'seeking', 'looking', 'ensure', 'provide',
            'assist', 'support', 'help', 'manage', 'lead', 'coordinate', 'communicate',
            'collaborate', 'participate', 'contribute', 'develop', 'create', 'maintain',
            'deliver', 'drive', 'execute', 'perform', 'build', 'using', 'based',
            
            # Time / Measure / Misc
            'years', 'year', 'level', 'senior', 'junior', 'mid', 'associate', # debatable, but often generic in topic
            'full-time', 'part-time', 'contract', 'permanent', 'temporary', 'remote', 'hybrid',
            'degree', 'bachelor', 'master', 'phd', 'equivalent', 'related', 'relevant',
            'including', 'include', 'includes', 'various', 'similar', 'etc', 'suite',
            'must', 'will', 'can', 'may', 'should', 'would', 'tools', 'environment'
        ]
        
        # Italian Stop Words (Manual List to avoid dependency issues)
        it_stop_words = [
            'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra',
            'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una',
            'e', 'ed', 'o', 'ma', 'se', 'che', 'non', 'si', 'chi',
            'mi', 'ti', 'ci', 'vi', 'li', 'ne', 'lei', 'lui', 'noi', 'voi', 'loro',
            'mio', 'tuo', 'suo', 'nostro', 'vostro', 'loro',
            'mia', 'tua', 'sua', 'nostra', 'vostra',
            'questo', 'quello', 'quella', 'questi', 'quelle',
            'cui', 'c', 'è', 'sono', 'siete', 'siamo', 'hanno', 'ha', 'ho', 'hai', 'hanno',
            'avuto', 'fatto', 'fare', 'essere', 'avere', 'stato', 'stata', 'stati', 'state',
            'presso', 'durante', 'tramite', 'verso', 'contro', 'sulla', 'dello', 'degli', 'della', 'dei', 'dal', 'dalla',
            'ai', 'agli', 'alla', 'alle', 'negli', 'nelle', 'nella', 'del', 'al', 
            'come', 'dove', 'quando', 'perché', 'anche', 'più', 'meno',
            'tutto', 'tutti', 'tutta', 'tut te', 'ogni', 'altro', 'altra', 'altri', 'altre',
            'molto', 'poco', 'abbastanza', 'proprio', 'già', 'ancora', 
            'ecc', 'eccetera', 'via', 'poi', 'solo', 'soltanto',
            # Apostrophe handling (tokenizers often split 'dell', 'all')
            'dell', 'all', 'sull', 'dall', 'nell', 'quest', 'quant', 'tant'
        ]
        
        # Manually filter stop words from vocabulary if CountVectorizer didn't catch them
        # (Alternatively, pass list to stop_words, but 'english' + list is tricky in sklearn < 0.24)
        # Better approach: extend the built-in english list
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
        all_stop_words = list(ENGLISH_STOP_WORDS) + hr_stop_words + it_stop_words
        
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=all_stop_words)
        tf = tf_vectorizer.fit_transform(text_corpus)

        lda = LatentDirichletAllocation(n_components=n_topics, max_iter=10, learning_method='online', random_state=42)
        lda.fit(tf)
        
        feature_names = tf_vectorizer.get_feature_names_out()
        topics = []
        
        # Extract top words for each topic
        for topic_idx, topic in enumerate(lda.components_):
            top_features_ind = topic.argsort()[:-n_words - 1:-1]
            top_features = [feature_names[i] for i in top_features_ind]
            topics.append(f"Topic {topic_idx+1}: {', '.join(top_features)}")
            
        # Generate Word Cloud for the first topic (or combined)
        # Flattening simple corpus for cloud
        # Flattening simple corpus for cloud
        combined_text = " ".join(text_corpus)
        wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=set(all_stop_words)).generate(combined_text)
        
        wc_path = "topic_wordcloud.png"
        wordcloud.to_file(wc_path)
        
        return topics, wc_path

    except Exception as e:
        print(f"LDA Error: {e}")
        return [], None

# --- NEW: NAMED ENTITY RECOGNITION (NER) ---
try:
    import nltk
    import ssl

    # Bypass SSL check for NLTK download (common issue on macOS)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # Download necessary NLTK data (cached)
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('chunkers/maxent_ne_chunker_tab')
        nltk.data.find('taggers/averaged_perceptron_tagger_eng')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('maxent_ne_chunker_tab')
        nltk.download('words')
        nltk.download('averaged_perceptron_tagger_eng')
except ImportError:
    nltk = None

def extract_entities_ner(text: str) -> Dict[str, List[str]]:
    """
    Extracts named entities (Organizations, GPE, Date) using NLTK with advanced filtering.
    """
    if not nltk:
        return {}
        
    entities = {"Organizations": [], "Locations": [], "Persons": []}
    
    # 1. Build Exclusion Set (Skills + Headers + Common Noise)
    exclusion_set = set()
    
    # Add Hard/Soft Skills to exclusion
    all_skills = getattr(constants, "ALL_SKILLS", {})
    for skill_cat, skill_vars in all_skills.items():
        exclusion_set.add(skill_cat.lower())
        for var in skill_vars:
            exclusion_set.add(var.lower())

    # Add Common CV Headers & Noise
    noise_words = {
        "curriculum", "vitae", "resume", "cv", "profile", "summary", 
        "experience", "education", "skills", "projects", "languages",
        "certifications", "interests", "references", "contacts",
        "email", "phone", "address", "date", "present", "current",
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
        "january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december",
        "page", "of", "senior", "junior", "mid", "level", "lead", "manager", "support",
        "competenze", "esperienze", "formazione", "istruzione", "lingue", "progetti",
        "certificazioni", "interessi", "contatti", "profilo", "sommario",
        "milano", "roma", "torino", "napoli", "italia", "italy", "remote", "smart working", # Locations to keep in Loc but not Org/Person
        "laurea", "triennale", "magistrale", "diploma", "corso", "master", "phd", "studio", "studi", "università",
        "competenza", "capacità", "conoscenza", "personale", "autorizzazione", "dati", "privacy", "buono", "ottimo", "discreto", 
        "madrelingua", "scolastico", "hobby", "sport", "patente", "automunito", "disponibilità", "immediata", "livello",
        "apprendimento", "curiosità", "economia", "finanza", "gestione", "giudizio", "impresa", "business", "analisi",
        "generative", "afm", "supporto", "aperto", "istituto", "metodi", "lettura",
        "chatgpt", "claude", "gemini", "canva", "perplexity", "orange", "jmp", "jupyterlab",
        "naive", "bayes", "random", "forest", "modello", "sistema", "pratico", "società", "relazioni", "pubbliche",
        "automazione", "chatbot", "ai", "digital", "technology", "intelligenza", "artificiale",
        "lavorativo", "buonoprofilo", "usa"
    }
    exclusion_set.update(noise_words)

    try:
        for sent in nltk.sent_tokenize(text):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    entity_name = ' '.join(c[0] for c in chunk)
                    label = chunk.label()
                    
                    # --- FILTERS ---
                    name_lower = entity_name.lower()
                    
                    entity_tokens = name_lower.split()
                    
                    # 1. Partial Match Filtering (Stronger)
                    # If ANY word in the entity name is in our exclusion set, drop it.
                    if any(t in exclusion_set for t in entity_tokens):
                        continue
                        
                    # 2. Skip single characters or very short abbreviations (unless specific)
                    if len(entity_name) < 3 and label != 'GPE': 
                        continue

                    # 3. Skip pure numbers or mixed noise (e.g. "2023-2024")
                    if any(char.isdigit() for char in entity_name):
                        continue
                        
                    if any(char.isdigit() for char in entity_name):
                        continue
                        
                    # 4. Length Check (Long phrases are usually garbage)
                    if len(entity_tokens) > 4:
                        continue

                    # 5. Filter Specific Categories
                    if label == 'ORGANIZATION':
                        # Exclude all-caps typically headers (unless specific known orgs)
                        # Rule: Allow short acronyms (IULM, IBM) < 5 chars.
                        # Drop headers like "LAVORATIVO" (10), "ISTITUTO" (8), "PROFILO" (7)
                        if entity_name.isupper() and len(entity_name) > 4 and len(entity_name) < 20: 
                             pass 
                        else:
                             entities["Organizations"].append(entity_name)
                        
                    elif label == 'GPE': # Geo-Political Entity
                        entities["Locations"].append(entity_name)
                        
                    elif label == 'PERSON':
                        # Person names rarely appear as specific skills
                        if name_lower not in exclusion_set:
                            entities["Persons"].append(entity_name)
                        
        # Deduplicate and Clean
        for k in entities:
             # Final pass: Remove items that exact match exclusion set again (safety)
             clean_list = sorted(list(set(entities[k])))
             entities[k] = [e for e in clean_list if e.lower() not in exclusion_set]
            
        return entities
    except Exception as e:
        print(f"NER Error: {e}")
        return {}

def generate_cluster_insight(clusters: Dict[str, int], matching_skills: Set[str], missing_skills: Set[str]) -> str:
    """
    Generates a text summary of the clustering results.
    """
    if not clusters:
        return "Not enough data to generate insights."
    
    # Invert dictionary: Cluster ID -> List of Skills
    cluster_groups = {}
    for skill, cid in clusters.items():
        if cid not in cluster_groups: cluster_groups[cid] = []
        cluster_groups[cid].append(skill)
        
    insight = "### 💡 AI Analysis of your Profile Structure\n\n"
    
    # Identify strongest and weakest clusters
    for cid, skills in cluster_groups.items():
        # Calculate coverage
        n_total = len(skills)
        n_matched = sum(1 for s in skills if s in matching_skills)
        coverage = (n_matched / n_total) * 100
        
        # Taking top 3 representative skills for the name
        preview = ", ".join(skills[:3])
        
        insight += f"**Group {cid} ({preview}...)**\n"
        insight += f"- **Coverage**: {coverage:.0f}% of these skills are in your CV.\n"
        
        if coverage > 75:
            insight += "- 🚀 **Assessment**: You are very strong in this area.\n"
        elif coverage < 30:
            insight += "- ⚠️ **Assessment**: This seems to be a significant gap area for you.\n"
        else:
            insight += "- ℹ️ **Assessment**: You have some foundation here, but room to improve.\n"
        
        insight += "\n"
        
    return insight


# =============================================================================
# GENERIC FALLBACK (TF-IDF)
# =============================================================================
def extract_generic_keywords(text: str, top_n=5) -> Set[str]:
    """
    Extracts top keywords from text using TF-IDF when no known skills are found.
    """
    if not TfidfVectorizer or not text or len(text.split()) < 10:
        return set()
        
    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
        vectorizer.fit_transform([text])
        return set(vectorizer.get_feature_names_out())
    except:
        return set()

# =============================================================================
# SKILL EXTRACTION CORE
# =============================================================================
# =============================================================================
# OPTIONAL IMPORTS
# =============================================================================
try:
    from thefuzz import fuzz
except ImportError:
    fuzz = None

# =============================================================================
# SKILL EXTRACTION CORE
# =============================================================================
def extract_skills_from_text(text: str) -> Tuple[Set[str], Set[str]]:
    hard_found = set()
    soft_found = set()
    text_lower = text.lower()
    
    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})
    inference_rules = getattr(constants, "INFERENCE_RULES", {})
    
    # Pre-process text for fuzzy matching (split into words)
    text_words = set(text_lower.split())

    # 1. Regex Match Hard Skills (Exact + Fuzzy)
    for skill, variations in hard_skills.items():
        matched = False
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                hard_found.add(skill)
                matched = True
                break
        
        # FUZZY FALLBACK (Robustness)
        if not matched and fuzz:
            # Check if any word in text is > 90% similar to the skill name
            for word in text_words:
                if fuzz.ratio(word, skill.lower()) > 90:
                    hard_found.add(skill)
                    break
                
    # 2. Regex Match Soft Skills (Exact + Fuzzy)
    for skill, variations in soft_skills.items():
        matched = False
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                soft_found.add(skill)
                matched = True
                break
        
        # FUZZY FALLBACK
        if not matched and fuzz:
             for word in text_words:
                if fuzz.ratio(word, skill.lower()) > 90:
                    soft_found.add(skill)
                    break

    # 3. Hierarchical Inference
    inferred_skills = set()
    for child_skill in hard_found:
        if child_skill in inference_rules:
            parents = inference_rules[child_skill]
            inferred_skills.update(parents)
    hard_found.update(inferred_skills)
    
    # 4. Generic Fallback
    if len(hard_found) < 2:
        generic_keywords = extract_generic_keywords(text, top_n=5)
        for kw in generic_keywords:
            hard_found.add(kw.capitalize())
    
    return hard_found, soft_found

# =============================================================================
# PDF EXTRACTION
# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    if PdfReader is None: 
        raise ImportError("PyPDF2 missing")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF Error: {str(e)}")

# =============================================================================
# REPORT UTILS
# =============================================================================
def generate_pdf_report(res: Dict, jd_text: str = "") -> bytes:
    """
    Generates a professional PDF report with advanced styling.
    """
    if not FPDF:
        return b"FPDF library missed."
        
    class PDF(FPDF):
        def header(self):
            # Banner Navy Blue
            self.set_fill_color(20, 29, 44)  # #141d2c
            self.rect(0, 0, 210, 40, 'F')
            
            # Title
            self.set_font('Arial', 'B', 24)
            self.set_text_color(255, 255, 255)
            self.set_xy(10, 10)
            self.cell(0, 15, 'JOB SEEKER ANALYTICS', 0, 1, 'L')
            
            # Subtitle
            self.set_font('Arial', 'I', 10)
            self.set_text_color(200, 200, 200)
            self.cell(0, 5, 'Automated Gap Analysis & Learning Roadmap', 0, 1, 'L')
            self.ln(20)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f'Job Seeker Helper | Generated with AI | Page {self.page_no()}', 0, 0, 'C')

        def section_title(self, label):
            self.set_font('Arial', 'B', 14)
            self.set_text_color(33, 33, 33)
            self.set_fill_color(240, 240, 240)
            self.cell(0, 10, f"  {label}", 0, 1, 'L', fill=True)
            self.ln(4)

        def card(self, title, content, link=None):
            self.set_fill_color(250, 250, 250)
            self.set_draw_color(220, 220, 220)
            self.set_font('Arial', 'B', 11)
            self.set_text_color(0, 0, 0)
            
            x = self.get_x()
            y = self.get_y()
            
            self.rect(x, y, 190, 25, 'FD')
            
            self.set_xy(x + 5, y + 5)
            self.cell(0, 5, title, 0, 1)
            
            self.set_font('Arial', '', 10)
            self.set_text_color(80, 80, 80)
            self.set_xy(x + 5, y + 12)
            self.cell(0, 5, content, 0, 1)
            
            if link:
                self.set_font('Arial', 'U', 9)
                self.set_text_color(0, 102, 204)
                self.set_xy(x + 150, y + 12)
                self.cell(30, 5, "Open Resource ->", 0, 0, link=link)

            self.ln(20)

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    def clean(text):
        """Sanitize text for FPDF (Latin-1)"""
        if not text: return ""
        # Replace common unicode chars
        replacements = {
            "’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
            "…": "...", "✅": "[V]", "❌": "[X]", "⚠️": "[!]", "➕": "[+]",
            "🚀": "", "📂": "", "☁️": "", "🛠️": "", "🎯": ""
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        
        # Force encode to latin-1, replacing unknown with ?
        return text.encode('latin-1', 'replace').decode('latin-1')

    # 1. EXECUTIVE SCORECARD
    pct = res["match_percentage"]
    
    # Logic for colors
    if pct >= 80:
        bg_r, bg_g, bg_b = 209, 231, 221 # Green-ish
        txt_color = "Excellent Match"
    elif pct >= 60:
        bg_r, bg_g, bg_b = 255, 243, 205 # Yellow-ish
        txt_color = "Good Potential"
    else:
        bg_r, bg_g, bg_b = 248, 215, 218 # Red-ish
        txt_color = "High Gap"

    pdf.set_fill_color(bg_r, bg_g, bg_b)
    pdf.rect(10, 50, 190, 30, 'F')
    
    pdf.set_y(55)
    pdf.set_x(15)
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(40, 10, f"{pct:.0f}%", 0, 0)
    
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, f"Match Score: {txt_color}", 0, 1)
    
    pdf.set_y(65)
    pdf.set_x(15)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, "Based on comprehensive analysis of Hard Skills, Soft Skills, and Portfolio triggers.", 0, 1)
    
    pdf.ln(20)

    # 2. SKILL MATRIX
    pdf.section_title("SKILL BREAKDOWN")
    
    # Matched
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(0, 100, 0) # Dark Green
    pdf.cell(95, 10, clean("MATCHED SKILLS"), 0, 0)
    
    # Missing
    pdf.set_text_color(150, 0, 0) # Dark Red
    pdf.cell(95, 10, clean("MISSING SKILLS"), 0, 1)
    
    # Reset text
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(50, 50, 50)
    
    matched_str = "\n".join([f"- {clean(s)}" for s in res["matching_hard"]])
    missing_str = "\n".join([f"- {clean(s)}" for s in res["missing_hard"]])
    
    y_start = pdf.get_y()
    pdf.multi_cell(95, 6, matched_str if matched_str else "None", border=1)
    y_end1 = pdf.get_y()
    
    pdf.set_xy(105, y_start)
    pdf.multi_cell(95, 6, missing_str if missing_str else "None", border=1)
    y_end2 = pdf.get_y()
    
    pdf.set_y(max(y_end1, y_end2) + 10)

    # Transferable
    if res.get("transferable"):
        pdf.set_font('Arial', 'B', 11)
        pdf.set_text_color(204, 153, 0) # Dark Yellow/Orange
        pdf.cell(0, 10, clean("TRANSFERABLE SKILLS (Equivalents Found)"), 0, 1)
        
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(50, 50, 50)
        for missing, present in res["transferable"].items():
             pdf.cell(0, 7, clean(f"• Required: {missing}  ->  You have: {present}"), 0, 1)
        pdf.ln(10)

    # 3. LEARNING ROADMAP
    if res["missing_hard"]:
        pdf.add_page()
        pdf.section_title("LEARNING ROADMAP")
        pdf.ln(5)
        
        for skill in res["missing_hard"]:
            r = constants.LEARNING_RESOURCES.get(skill, None)
            
            content = "Use general search engines to find tutorials."
            link_url = f"https://www.google.com/search?q=learn+{urllib.parse.quote(skill)}"
            
            if r:
                course_str = ", ".join(r['courses'][:1]) # Take first course
                content = f"Recommended: {course_str}. Project Layout: {r['project']}"
                # We assume a generic search link if no direct URL in DB (DB currently has strings titles)
            
            pdf.card(clean(f"Skill Gap: {skill}"), clean(content), link=link_url)

    # Output with correct encoding handling
    return pdf.output(dest='S').encode('latin-1', 'ignore')

def detect_language(text: str) -> str:
    """
    Simple heuristic to detect non-explicit native language.
    """
    text = text.lower()
    it_markers = {" il ", " lo ", " la ", " i ", " gli ", " le ", " di ", " è ", " e ", " per ", " delle ", " nella "}
    en_markers = {" the ", " a ", " an ", " and ", " is ", " of ", " for ", " to ", " in ", " with ", " that ", " this "}
    
    it_score = sum(1 for w in it_markers if w in text)
    en_score = sum(1 for w in en_markers if w in text)
    
    if it_score > en_score: return "Italian"
    if en_score > it_score: return "English"
    return None

# =============================================================================
# GAP ANALYSIS
# =============================================================================
def analyze_gap(cv_text: str, job_text: str) -> Dict:
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text)
    
    # 0. Native Language Inference
    # If CV is detected as Italian, we assume candidate speaks Italian (Native)
    detected_lang = detect_language(cv_text)
    if detected_lang:
        cv_hard.add(detected_lang)
    
    matching_hard = cv_hard & job_hard
    initial_missing_hard = job_hard - cv_hard
    extra_hard = cv_hard - job_hard
    
    # Stats
    skill_clusters = getattr(constants, "SKILL_CLUSTERS", {})
    project_skills = getattr(constants, "PROJECT_BASED_SKILLS", set())
    
    # Logic 1: Transferable
    transferable = {} 
    remaining_missing = set()
    for missing in initial_missing_hard:
        found_transferable = False
        for cluster_name, members in skill_clusters.items():
            if missing in members:
                user_has = members.intersection(cv_hard)
                if user_has:
                    transferable[missing] = list(user_has)[0] 
                    found_transferable = True
                    break
        if not found_transferable:
            remaining_missing.add(missing)
            
    # Logic 2: Project-Based
    project_review = set()
    final_strict_missing = set()
    for skill in remaining_missing:
        if skill in project_skills:
            project_review.add(skill)
        else:
            final_strict_missing.add(skill)
            
    matching_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft
    
    score_points = len(matching_hard) + (len(transferable) * 0.5) + (len(project_review) * 0.3)
    match_pct = score_points / len(job_hard) * 100 if job_hard else 0
    
    return {
        "match_percentage": match_pct,
        "matching_hard": matching_hard,
        "missing_hard": final_strict_missing,
        "project_review": project_review, 
        "transferable": transferable,
        "extra_hard": extra_hard,
        "matching_soft": matching_soft,
        "missing_soft": missing_soft
    }

# =============================================================================
def analyze_gap_with_project(cv_text: str, job_text: str, project_text: str) -> Dict:
    """
    Analyzes CV + Project vs Job Description.
    Returns standard gap analysis plus 'project_verified' skills.
    """
    # 1. Standard CV Analysis
    res = analyze_gap(cv_text, job_text)
    
    # 2. Project Analysis
    proj_hard, _ = extract_skills_from_text(project_text)
    
    # 3. Identify Verified Skills (Requested by JD AND found in Projects)
    # These are skills that might be in 'matching_hard' (CV+JD) or 'missing_hard' (JD only)
    # If they are in Projects, we upgrade/verify them.
    
    job_hard, _ = extract_skills_from_text(job_text) # Re-extract to be sure or pass it if possible, but cheap enough
    
    project_verified = job_hard.intersection(proj_hard)
    
    # Update Result
    res["project_verified"] = project_verified
    
    # Boost Score? Optional. Let's keep it simple: just identifying them for now.
    # We could recalculate match_percentage if we wanted project skills to fill gaps.
    
    # If a skill was missing in CV but found in Project, move it from missing to matching?
    # Strategy: "Project skills count as skills"
    
    newly_found_in_project = res["missing_hard"].intersection(proj_hard)
    if newly_found_in_project:
        res["matching_hard"].update(newly_found_in_project)
        res["missing_hard"] = res["missing_hard"] - newly_found_in_project
        
        # Recalculate Score
        # (Simplified recalc based on previous formula in analyze_gap)
        # score_points = len(matching_hard) + (len(transferable) * 0.5) + (len(project_review) * 0.3)
        
        score_points = len(res["matching_hard"]) + (len(res["transferable"]) * 0.5) + (len(res["project_review"]) * 0.3)
        res["match_percentage"] = score_points / len(job_hard) * 100 if job_hard else 0

    return res
