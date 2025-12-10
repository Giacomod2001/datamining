"""
===================================================================================
JOB SEEKER HELPER - Analizzatore di Compatibilità CV/Annunci di Lavoro
===================================================================================
Progetto: Text Mining e NLP per Job Matching

PILASTRI DEL PROGETTO:
1. TEXT MINING & NLP: Estrazione automatica di keyword da testi non strutturati
2. PATTERN MATCHING: Utilizzo di regex per riconoscimento intelligente
3. ENVIRONMENT MANAGEMENT: Gestione dipendenze Python (requirements.txt)
4. DATA ANALYSIS: Calcolo metriche e scoring di compatibilità

Autori: Luca Tallarico, Ruben Scoletta, Giacomo Dellacqua
Licenza: MIT
===================================================================================
"""

# ============================================================================
# IMPORT DELLE LIBRERIE
# ============================================================================
import streamlit as st  # Framework per interfaccia web interattiva
import re              # Regex per pattern matching e text mining
from typing import Set, Tuple, List  # Type hints per code clarity

# ============================================================================
# CONFIGURAZIONE APPLICAZIONE WEB
# ============================================================================
st.set_page_config(
    page_title="Job Seeker Helper",  # Titolo che appare nel tab del browser
    page_icon="🎯",                  # Emoji come favicon
    layout="wide"                     # Layout espanso per sfruttare lo schermo
)

# ============================================================================
# DATABASE KNOWLEDGE BASE - GRUPPI DI COMPETENZE CORRELATE
# ============================================================================
# PILASTRO NLP: Normalizzazione semantica delle competenze
# Ogni gruppo rappresenta un CONCETTO (chiave) con le sue VARIAZIONI (valori)
# Questo permette di riconoscere sinonimi e varianti ortografiche
# Esempio: "Machine Learning", "ML", "Deep Learning" → tutti riconosciuti come "Machine Learning"
# ============================================================================

SKILL_GROUPS = {
    # ------------------------------------------------------------------------
    # LINGUAGGI DI PROGRAMMAZIONE
    # ------------------------------------------------------------------------
    "Python": [
        "Python", "Python3", "PyPy", 
        "Sviluppo Python", "Python Developer", "Python dev"
    ],
    "Java": [
        "Java", "JDK", "JRE", 
        "Java Developer", "Java dev", "JavaEE", "J2EE"
    ],
    "JavaScript": [
        "JavaScript", "JS", "ECMAScript", "ES6", "ES2015", 
        "Node", "Node.js", "NodeJS"
    ],
    "TypeScript": ["TypeScript", "TS"],
    "C++": ["C++", "CPP", "C Plus Plus"],
    "C#": ["C#", "CSharp", "C Sharp", ".NET", "dotnet"],
    "PHP": ["PHP", "PHP7", "PHP8"],
    "Ruby": ["Ruby", "RoR", "Ruby on Rails", "Rails"],
    "Go": ["Go", "Golang"],
    "Rust": ["Rust", "Cargo"],
    "Kotlin": ["Kotlin", "Kotlin dev"],
    "Swift": ["Swift", "SwiftUI"],
    "R": ["R", "R Programming", "R Studio"],
    
    # ------------------------------------------------------------------------
    # FRONTEND FRAMEWORKS & TOOLS
    # ------------------------------------------------------------------------
    "React": [
        "React", "ReactJS", "React.js", 
        "React Native", "Next.js", "NextJS"
    ],
    "Angular": [
        "Angular", "AngularJS", "Angular2+", "Angular dev"
    ],
    "Vue": [
        "Vue", "Vue.js", "VueJS", "Nuxt", "Nuxt.js"
    ],
    "HTML/CSS": [
        "HTML", "CSS", "HTML5", "CSS3", 
        "SASS", "SCSS", "LESS", "Tailwind", "Bootstrap"
    ],
    "Frontend": [
        "Frontend", "Front-end", "Front end", 
        "UI Development", "Web Development"
    ],
    
    # ------------------------------------------------------------------------
    # BACKEND FRAMEWORKS
    # ------------------------------------------------------------------------
    "Django": ["Django", "Django REST", "DRF"],
    "Flask": ["Flask", "Flask-RESTful"],
    "FastAPI": ["FastAPI", "Fast API"],
    "Spring": [
        "Spring", "Spring Boot", "SpringBoot", "Spring Framework"
    ],
    "Express": ["Express", "ExpressJS", "Express.js"],
    "Backend": [
        "Backend", "Back-end", "Back end", "Server-side"
    ],
    
    # ------------------------------------------------------------------------
    # DATABASE & DATA STORAGE
    # ------------------------------------------------------------------------
    "SQL": [
        "SQL", "MySQL", "PostgreSQL", "MS SQL", "SQL Server", 
        "MariaDB", "Database", "DB", "Relational Database"
    ],
    "NoSQL": [
        "NoSQL", "MongoDB", "Cassandra", "CouchDB", "Document DB"
    ],
    "Database Management": [
        "Database", "DB", "Database Management", "DBMS", "Data Storage"
    ],
    
    # ------------------------------------------------------------------------
    # CLOUD PLATFORMS
    # ------------------------------------------------------------------------
    "AWS": [
        "AWS", "Amazon Web Services", "EC2", "S3", "Lambda", "Cloud AWS"
    ],
    "Azure": ["Azure", "Microsoft Azure", "Azure Cloud"],
    "GCP": ["GCP", "Google Cloud", "Google Cloud Platform"],
    "Cloud": [
        "Cloud", "Cloud Computing", "Cloud Infrastructure", "Cloud Services"
    ],
    
    # ------------------------------------------------------------------------
    # DEVOPS & CONTAINERIZATION
    # ------------------------------------------------------------------------
    "Docker": ["Docker", "Containerization", "Container", "Dockerfile"],
    "Kubernetes": ["Kubernetes", "K8s", "Container Orchestration"],
    "CI/CD": [
        "CI/CD", "Continuous Integration", "Continuous Deployment", 
        "Jenkins", "GitLab CI", "GitHub Actions", "CI CD"
    ],
    "DevOps": ["DevOps", "Dev Ops", "Site Reliability", "SRE"],
    
    # ------------------------------------------------------------------------
    # DATA SCIENCE & ARTIFICIAL INTELLIGENCE
    # ------------------------------------------------------------------------
    "Machine Learning": [
        "Machine Learning", "ML", "Deep Learning", "AI", 
        "Artificial Intelligence", "Neural Networks", "Deep Neural Networks"
    ],
    "Data Science": [
        "Data Science", "Data Scientist", "Data Analysis", 
        "Data Analytics", "Big Data", "Data Mining"
    ],
    "TensorFlow": ["TensorFlow", "Tensorflow", "TF", "Keras"],
    "PyTorch": ["PyTorch", "Torch"],
    "Pandas": ["Pandas", "Data Manipulation", "Data Processing"],
    "NLP": [
        "NLP", "Natural Language Processing", 
        "Text Mining", "Text Analysis", "Linguistics"
    ],
    "Computer Vision": [
        "Computer Vision", "CV", "Image Processing", 
        "Image Recognition", "Object Detection"
    ],
    
    # ------------------------------------------------------------------------
    # VERSION CONTROL
    # ------------------------------------------------------------------------
    "Git": [
        "Git", "GitHub", "GitLab", "Bitbucket", 
        "Version Control", "Source Control", "VCS"
    ],
    
    # ------------------------------------------------------------------------
    # TESTING & QA
    # ------------------------------------------------------------------------
    "Testing": [
        "Testing", "Test", "QA", "Quality Assurance", 
        "Unit Test", "Integration Test", "Test Automation"
    ],
    "Selenium": ["Selenium", "Test Automation", "Web Testing"],
    
    # ------------------------------------------------------------------------
    # AGILE & PROJECT MANAGEMENT
    # ------------------------------------------------------------------------
    "Agile": [
        "Agile", "Scrum", "Kanban", "Sprint", 
        "Agile Methodology", "Agile Development"
    ],
    "Project Management": [
        "Project Management", "PM", "Product Management", 
        "Gestione Progetti", "PMP"
    ],
    
    # ------------------------------------------------------------------------
    # SOFT SKILLS
    # ------------------------------------------------------------------------
    "Teamwork": [
        "Team Working", "Teamwork", "Team work", 
        "Lavoro di squadra", "Collaborazione", "Collaboration"
    ],
    "Communication": [
        "Communication", "Comunicazione", "Presentation", "Public Speaking"
    ],
    "Problem Solving": [
        "Problem Solving", "Critical Thinking", "Analytical", "Analytical Skills"
    ],
    "Leadership": [
        "Leadership", "Team Leading", "Mentoring", "Management", "Lead"
    ],
    
    # ------------------------------------------------------------------------
    # LINGUE
    # ------------------------------------------------------------------------
    "English": [
        "English", "Inglese", "Lingua Inglese", "English Language"
    ],
    "Italian": ["Italian", "Italiano", "Lingua Italiana"],
    
    # ------------------------------------------------------------------------
    # MOBILE DEVELOPMENT
    # ------------------------------------------------------------------------
    "Mobile Development": [
        "Mobile", "Mobile Development", "iOS", "Android", 
        "React Native", "Flutter", "Mobile dev"
    ],
    
    # ------------------------------------------------------------------------
    # SECURITY
    # ------------------------------------------------------------------------
    "Security": [
        "Security", "Cybersecurity", "Cyber Security", 
        "Information Security", "Sicurezza", "Penetration Testing"
    ],
    
    # ------------------------------------------------------------------------
    # DESIGN
    # ------------------------------------------------------------------------
    "UI/UX": [
        "UI", "UX", "User Experience", "User Interface", 
        "Design", "UI Design", "UX Design", "Product Design"
    ],
    
    # ------------------------------------------------------------------------
    # BUSINESS INTELLIGENCE TOOLS
    # ------------------------------------------------------------------------
    "Excel": ["Excel", "Microsoft Excel", "Spreadsheet", "Fogli di calcolo"],
    "Word": ["Word", "Microsoft Word", "Word Processing"],
    "PowerPoint": ["PowerPoint", "Microsoft PowerPoint", "PPT", "Presentation"],
    "Power BI": ["Power BI", "PowerBI", "Business Intelligence", "BI"],
    "Looker": ["Looker", "Looker Studio", "Google Looker", "Data Studio"],
    "Tableau": ["Tableau", "Tableau Desktop", "Data Visualization"],
    
    # ------------------------------------------------------------------------
    # API & WEB SERVICES
    # ------------------------------------------------------------------------
    "API": ["API", "REST", "RESTful", "REST API", "Web API", "Web Services"],
}


# ============================================================================
# SISTEMA DI INFERENZA SKILL IMPLICITE
# ============================================================================
# PILASTRO NLP AVANZATO: Deduzione intelligente di competenze correlate
# Se un CV menziona una skill "macro", il sistema inferisce automaticamente
# le competenze "micro" che essa implica
# Esempio: "Microsoft Office" → Excel, Word, PowerPoint
# ============================================================================

SKILL_IMPLICATIONS = {
    # ------------------------------------------------------------------------
    # SUITE SOFTWARE E PACCHETTI
    # ------------------------------------------------------------------------
    "Microsoft Office": ["Excel", "Word", "PowerPoint"],
    "Office": ["Excel", "Word", "PowerPoint"],
    "Google Workspace": ["Excel", "Looker"],
    "G Suite": ["Excel", "Looker"],
    
    # ------------------------------------------------------------------------
    # RUOLI PROFESSIONALI → SKILL TECNICHE
    # ------------------------------------------------------------------------
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Pandas", "Data Science"],
    "Data Analyst": ["SQL", "Excel", "Python", "Data Science"],
    "Full Stack Developer": ["JavaScript", "HTML/CSS", "Backend", "Frontend", "SQL"],
    "Frontend Developer": ["JavaScript", "HTML/CSS", "React", "Frontend"],
    "Backend Developer": ["Backend", "SQL", "API"],
    "DevOps Engineer": ["Docker", "CI/CD", "Cloud", "Git", "DevOps"],
    "Software Engineer": ["Git", "Testing", "Agile"],
    "Web Developer": ["HTML/CSS", "JavaScript", "Frontend"],
    "Mobile Developer": ["Mobile Development", "Git"],
    
    # ------------------------------------------------------------------------
    # FRAMEWORK → LINGUAGGI BASE
    # ------------------------------------------------------------------------
    "React": ["JavaScript", "HTML/CSS", "Frontend"],
    "Angular": ["JavaScript", "HTML/CSS", "Frontend"],
    "Vue": ["JavaScript", "HTML/CSS", "Frontend"],
    "Django": ["Python", "Backend", "SQL"],
    "Flask": ["Python", "Backend"],
    "FastAPI": ["Python", "Backend"],
    "Spring": ["Java", "Backend", "SQL"],
    "Express": ["JavaScript", "Backend"],
    
    # ------------------------------------------------------------------------
    # DATA SCIENCE → TOOL ECOSISTEMA
    # ------------------------------------------------------------------------
    "Machine Learning": ["Python", "Data Science"],
    "Deep Learning": ["Python", "Machine Learning", "Data Science"],
    "TensorFlow": ["Python", "Machine Learning"],
    "PyTorch": ["Python", "Machine Learning"],
    "Data Science": ["Python", "SQL"],
    "Big Data": ["Data Science", "SQL"],
    
    # ------------------------------------------------------------------------
    # CLOUD → COMPETENZE CORRELATE
    # ------------------------------------------------------------------------
    "AWS": ["Cloud", "DevOps"],
    "Azure": ["Cloud", "DevOps"],
    "GCP": ["Cloud", "DevOps"],
    "Docker": ["DevOps", "Cloud"],
    "Kubernetes": ["Docker", "DevOps", "Cloud"],
    
    # ------------------------------------------------------------------------
    # DATABASE → SQL GENERAL
    # ------------------------------------------------------------------------
    "PostgreSQL": ["SQL", "Database Management"],
    "MySQL": ["SQL", "Database Management"],
    "MongoDB": ["NoSQL", "Database Management"],
    "Oracle": ["SQL", "Database Management"],
    
    # ------------------------------------------------------------------------
    # BUSINESS INTELLIGENCE
    # ------------------------------------------------------------------------
    "Power BI": ["Excel", "Data Science"],
    "Tableau": ["Data Science", "SQL"],
    "Looker": ["SQL", "Data Science"],
    
    # ------------------------------------------------------------------------
    # METODOLOGIE → SOFT SKILLS
    # ------------------------------------------------------------------------
    "Agile": ["Teamwork", "Communication", "Project Management"],
    "Scrum": ["Agile", "Teamwork", "Project Management"],
    "Project Management": ["Leadership", "Communication"],
    "Team Leading": ["Leadership", "Communication", "Teamwork"],
}


# ============================================================================
# FUNZIONE: INFERENZA SKILL IMPLICITE
# ============================================================================

def infer_implied_skills(detected_skills: Set[str]) -> Set[str]:
    """
    Deduce automaticamente skill implicite basate su quelle rilevate.
    
    ALGORITMO:
    1. Per ogni skill rilevata, controlla se ha implicazioni
    2. Se sì, aggiunge le skill implicate al set
    3. Ripete finché non ci sono più nuove skill da inferire
    
    Args:
        detected_skills (Set[str]): Skill rilevate direttamente dal testo
    
    Returns:
        Set[str]: Skill originali + skill inferite
    
    Esempio:
        Input: {"Microsoft Office", "Data Scientist"}
        Output: {"Microsoft Office", "Excel", "Word", "PowerPoint", 
                 "Data Scientist", "Python", "SQL", "Machine Learning", "Pandas"}
    """
    # Inizia con le skill già rilevate
    all_skills = detected_skills.copy()
    
    # CICLO DI INFERENZA: continua finché trova nuove skill
    newly_added = True
    while newly_added:
        newly_added = False
        current_skills = all_skills.copy()
        
        # Per ogni skill attualmente nel set
        for skill in current_skills:
            # Controlla se questa skill implica altre competenze
            if skill in SKILL_IMPLICATIONS:
                implied = SKILL_IMPLICATIONS[skill]
                
                # Aggiungi le skill implicate
                for implied_skill in implied:
                    if implied_skill not in all_skills:
                        all_skills.add(implied_skill)
                        newly_added = True  # Nuova skill trovata, ripeti il ciclo
    
    return all_skills



# ============================================================================
# FUNZIONE CORE: TEXT MINING E KEYWORD EXTRACTION
# ============================================================================
# PILASTRO NLP: Questa funzione implementa l'estrazione intelligente di keyword
# Simile al task NLP del laboratorio (rake_nltk), ma con approccio custom
# ============================================================================

def normalize_and_extract(text: str) -> Set[str]:
    """
    Estrae le competenze dal testo usando Text Mining e Pattern Matching,
    poi applica inferenza intelligente per dedurre skill implicite.
    
    ALGORITMO:
    1. Normalizzazione: Converte il testo in lowercase per case-insensitive matching
    2. Pattern Matching: Usa regex per trovare keyword esatte (con word boundaries)
    3. Normalizzazione Semantica: Mappa variazioni diverse allo stesso concetto
    4. INFERENZA INTELLIGENTE: Deduce skill implicite (NOVITÀ!)
    
    Args:
        text (str): Testo da analizzare (annuncio di lavoro o CV)
    
    Returns:
        Set[str]: Set di skill normalizzate + skill inferite
    
    Esempio:
        Input: "Data Scientist con Microsoft Office"
        Step 1-3: {"Data Scientist", "Microsoft Office"}
        Step 4 (inferenza): {"Data Scientist", "Python", "SQL", "Machine Learning",
                             "Microsoft Office", "Excel", "Word", "PowerPoint"}
    """
    # Set per memorizzare le skill trovate (usa Set per evitare duplicati)
    found_skills = set()
    
    # STEP 1: Normalizzazione testo - converte tutto in minuscolo
    text_lower = text.lower()
    
    # STEP 2: Iterazione su tutti i gruppi di competenze
    for main_skill, variations in SKILL_GROUPS.items():
        # Per ogni variazione di questa skill
        for variation in variations:
            # STEP 3: Pattern Matching con Regex
            # \b = word boundary (evita match parziali: "python" in "pythonic")
            # re.escape() = escape caratteri speciali (es. C++, C#, .NET)
            pattern = r'\b' + re.escape(variation.lower()) + r'\b'
            
            # STEP 4: Ricerca pattern nel testo
            if re.search(pattern, text_lower):
                # Skill trovata! Aggiungi al set usando il nome normalizzato
                found_skills.add(main_skill)
                # Break: una sola variazione basta per riconoscere la skill
                break
    
    # STEP 5 (NUOVO): INFERENZA SKILL IMPLICITE
    # Espande il set con competenze deducibili logicamente
    all_skills = infer_implied_skills(found_skills)
    
    return all_skills


# ============================================================================
# FUNZIONE: CALCOLO METRICHE DI COMPATIBILITÀ
# ============================================================================
# PILASTRO DATA ANALYSIS: Calcola scoring e metriche quantitative
# ============================================================================

def calculate_match(job_skills: Set[str], cv_skills: Set[str]) -> Tuple[float, Set[str], Set[str]]:
    """
    Calcola la percentuale di match e identifica skill possedute vs mancanti.
    
    ALGORITMO:
    1. Intersezione: Trova skill comuni (job_skills ∩ cv_skills)
    2. Differenza: Trova skill mancanti (job_skills - cv_skills)
    3. Scoring: Percentuale = (skill_comuni / skill_richieste) * 100
    
    Args:
        job_skills (Set[str]): Competenze richieste dall'annuncio
        cv_skills (Set[str]): Competenze possedute dal candidato
    
    Returns:
        Tuple[float, Set[str], Set[str]]: 
            - Percentuale di match (0-100)
            - Set di skill possedute
            - Set di skill mancanti
    """
    # Caso edge: nessuna skill richiesta nell'annuncio
    if not job_skills:
        return 0.0, set(), set()
    
    # OPERAZIONI INSIEMISTICHE (Set Theory)
    matched_skills = job_skills.intersection(cv_skills)  # A ∩ B
    missing_skills = job_skills.difference(cv_skills)    # A - B
    
    # CALCOLO PERCENTUALE DI MATCH
    # Formula: (skill_match / skill_totali_richieste) * 100
    match_percentage = (len(matched_skills) / len(job_skills)) * 100
    
    return match_percentage, matched_skills, missing_skills


# ============================================================================
# FUNZIONE: GENERAZIONE FEEDBACK QUALITATIVO
# ============================================================================

def get_match_message(percentage: float) -> str:
    """
    Converte il punteggio numerico in feedback testuale per l'utente.
    
    THRESHOLDS:
    - < 40%: Match Basso (profilo junior o requisiti eccessivi)
    - 40-75%: Match Medio (buona base, serve integrazione)
    - > 75%: Match Alto (profilo ideale)
    
    Args:
        percentage (float): Percentuale di compatibilità (0-100)
    
    Returns:
        str: Messaggio formattato con emoji e descrizione
    """
    if percentage < 40:
        return "🔴 Match Basso - Richieste forse irrealistiche o profilo junior"
    elif percentage <= 75:
        return "🟡 Match Medio - Buona base"
    else:
        return "🟢 Match Alto - Profilo ideale"


# ============================================================================
# INTERFACCIA UTENTE STREAMLIT
# ============================================================================
# PILASTRO VIBE CODING: UI generata con approccio dichiarativo e intuitivo
# ============================================================================

# Header principale
st.title("🎯 Job Seeker Helper")
st.markdown("### Analizza la compatibilità tra annuncio di lavoro e il tuo CV")
st.markdown("---")  # Separatore visuale

# ============================================================================
# SEZIONE INPUT: Due colonne per annuncio e CV
# ============================================================================
col1, col2 = st.columns(2)  # Layout a 2 colonne

with col1:
    st.subheader("📋 Annuncio di Lavoro")
    # Text area per input annuncio
    job_text = st.text_area(
        "Incolla qui il testo dell'annuncio",
        height=300,
        placeholder="Cerca Software Engineer con esperienza in Python, SQL, Docker..."
    )

with col2:
    st.subheader("📄 Il tuo CV / Lista Skill")
    # Text area per input CV
    cv_text = st.text_area(
        "Incolla qui il tuo CV o lista di competenze",
        height=300,
        placeholder="Esperienza con Python, JavaScript, React, PostgreSQL..."
    )

st.markdown("---")  # Separatore

# ============================================================================
# SEZIONE PROCESSING: Logica di analisi al click del bottone
# ============================================================================

# Bottone di analisi (type="primary" → colore acceso, use_container_width → full width)
if st.button("🔍 Analizza Match", type="primary", use_container_width=True):
    
    # VALIDAZIONE INPUT: Verifica che entrambi i campi siano compilati
    if not job_text or not cv_text:
        st.warning("⚠️ Compila entrambi i campi per procedere con l'analisi!")
    
    else:
        # ====================================================================
        # PIPELINE DI ANALISI
        # ====================================================================
        
        # STEP 1: TEXT MINING - Estrazione keyword da entrambi i testi
        job_skills = normalize_and_extract(job_text)   # Skill richieste
        cv_skills = normalize_and_extract(cv_text)     # Skill possedute
        
        # STEP 2: SCORING - Calcolo compatibilità
        match_percentage, matched_skills, missing_skills = calculate_match(
            job_skills, cv_skills
        )
        
        # ====================================================================
        # VISUALIZZAZIONE RISULTATI
        # ====================================================================
        
        st.markdown("---")
        st.subheader("📊 Risultato dell'Analisi")
        
        # METRICA PRINCIPALE: Percentuale di match
        st.metric("Percentuale di Match", f"{match_percentage:.1f}%")
        
        # PROGRESS BAR: Visualizzazione grafica (0.0 - 1.0)
        st.progress(match_percentage / 100)
        
        # MESSAGGIO QUALITATIVO: Feedback basato su threshold
        st.info(get_match_message(match_percentage))
        
        st.markdown("---")
        
        # ====================================================================
        # DETTAGLIO SKILL: Layout a due colonne
        # ====================================================================
        col_matched, col_missing = st.columns(2)
        
        # COLONNA SINISTRA: Skill possedute (verde ✓)
        with col_matched:
            st.subheader("✅ Skill Possedute")
            if matched_skills:
                # Ordina alfabeticamente e mostra con success badge
                for skill in sorted(matched_skills):
                    st.success(f"✓ {skill}")
            else:
                st.write("Nessuna skill in comune trovata.")
        
        # COLONNA DESTRA: Skill mancanti (rosso ✗)
        with col_missing:
            st.subheader("❌ Skill Mancanti")
            if missing_skills:
                # Ordina alfabeticamente e mostra con error badge
                for skill in sorted(missing_skills):
                    st.error(f"✗ {skill}")
            else:
                st.write("Hai tutte le skill richieste! 🎉")
        
        # ====================================================================
        # STATISTICHE AGGIUNTIVE
        # ====================================================================
        st.markdown("---")
        st.caption(
            f"📈 Skill rilevate nell'annuncio: {len(job_skills)} | "
            f"Skill rilevate nel CV: {len(cv_skills)}"
        )

# ============================================================================
# FINE CODICE
# ============================================================================
# Per eseguire: streamlit run app.py
# ============================================================================
