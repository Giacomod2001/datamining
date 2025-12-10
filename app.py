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
import io              # Input/Output per gestione file in memoria
try:
    from PyPDF2 import PdfReader  # Lettura e estrazione testo da PDF
except ImportError:
    PdfReader = None  # Fallback se PyPDF2 non è installato

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
# SOFT SKILLS - ESCLUSE DAL CALCOLO DEL MATCH
# ============================================================================
# Le soft skills non vengono conteggiate nella percentuale di compatibilità
# perché sono soggettive e difficili da quantificare
# ============================================================================

SOFT_SKILLS = {
    "Teamwork",
    "Communication", 
    "Problem Solving",
    "Leadership",
    "Agile",
    "Project Management"
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
    "Python": ["Pandas"],  # Se usi Python, sai usare Pandas
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
    "Machine Learning": ["Python", "Data Science", "Pandas"],
    "Deep Learning": ["Python", "Machine Learning", "Data Science", "Pandas"],
    "TensorFlow": ["Python", "Machine Learning", "Pandas"],
    "PyTorch": ["Python", "Machine Learning", "Pandas"],
    "Data Science": ["Python", "SQL", "Pandas"],
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
    # BUSINESS INTELLIGENCE - TOOL EQUIVALENTI
    # ------------------------------------------------------------------------
    # Power BI, Tableau, Looker sono concettualmente simili:
    # Se sai usarne uno, sai usare anche gli altri (stessi principi di BI)
    "Power BI": ["Excel", "Data Science", "Tableau", "Looker"],
    "Tableau": ["Data Science", "SQL", "Power BI", "Looker"],
    "Looker": ["SQL", "Data Science", "Power BI", "Tableau"],
    
    # ------------------------------------------------------------------------
    # METODOLOGIE → SOFT SKILLS
    # ------------------------------------------------------------------------
    "Agile": ["Teamwork", "Communication", "Project Management"],
    "Scrum": ["Agile", "Teamwork", "Project Management"],
    "Project Management": ["Leadership", "Communication"],
    "Team Leading": ["Leadership", "Communication", "Teamwork"],
}


# ============================================================================
# DATABASE RISORSE DI APPRENDIMENTO
# ============================================================================
# Per ogni skill, fornisce risorse concrete per acquisirla
# ============================================================================

LEARNING_RESOURCES = {
    # ------------------------------------------------------------------------
    # LINGUAGGI DI PROGRAMMAZIONE
    # ------------------------------------------------------------------------
    "Python": {
        "difficoltà": "Media",
        "tempo": "2-3 mesi",
        "corsi": [
            "Python for Everybody (Coursera - Gratis)",
            "Complete Python Bootcamp (Udemy)",
            "Python Documentation ufficiale"
        ],
        "pratica": "Progetti su Kaggle, LeetCode, progetto personale",
        "certificazioni": "PCAP (Python Institute)"
    },
    "Java": {
        "difficoltà": "Media-Alta",
        "tempo": "3-4 mesi",
        "corsi": ["Java Programming MOOC (University of Helsinki)", "Oracle Java Tutorials"],
        "pratica": "Build una Spring Boot REST API",
        "certificazioni": "Oracle Certified Associate"
    },
    "JavaScript": {
        "difficoltà": "Media",
        "tempo": "2-3 mesi",
        "corsi": ["freeCodeCamp JavaScript", "JavaScript.info (gratis)"],
        "pratica": "Build portfolio website interattivo",
        "certificazioni": "Focus su portfolio, non certificazioni"
    },
    
    # ------------------------------------------------------------------------
    # DATA SCIENCE & AI
    # ------------------------------------------------------------------------
    "Machine Learning": {
        "difficoltà": "Alta",
        "tempo": "4-6 mesi",
        "corsi": [
            "Machine Learning by Andrew Ng (Coursera)",
            "Fast.ai Practical Deep Learning"
        ],
        "pratica": "Kaggle competitions, progetti ML su dataset reali",
        "certificazioni": "Google ML Engineer"
    },
    "Data Science": {
        "difficoltà": "Media-Alta",
        "tempo": "3-5 mesi",
        "corsi": ["Data Science Specialization (Coursera)", "DataCamp Career Track"],
        "pratica": "Analisi dati pubblici, portfolio GitHub",
        "certificazioni": "IBM Data Science Professional"
    },
    "Pandas": {
        "difficoltà": "Bassa-Media",
        "tempo": "2-4 settimane",
        "corsi": ["Pandas Documentation", "DataCamp Pandas Course"],
        "pratica": "Kaggle datasets exploration",
        "certificazioni": "Non necessarie"
    },
    "NLP": {
        "difficoltà": "Alta",
        "tempo": "3-4 mesi",
        "corsi": ["NLP Specialization (deeplearning.ai)", "Hugging Face Course"],
        "pratica": "Build chatbot, sentiment analysis projects",
        "certificazioni": "Dimostra con progetti pratici"
    },
    
    # ------------------------------------------------------------------------
    # DATABASE & SQL
    # ------------------------------------------------------------------------
    "SQL": {
        "difficoltà": "Bassa-Media",
        "tempo": "3-6 settimane",
        "corsi": ["Mode SQL Tutorial", "SQLBolt (interattivo)", "Codecademy SQL"],
        "pratica": "LeetCode SQL problems, progetti con DB reali",
        "certificazioni": "Pratica è più importante"
    },
    
    # ------------------------------------------------------------------------
    # CLOUD & DEVOPS
    # ------------------------------------------------------------------------
    "AWS": {
        "difficoltà": "Media-Alta",
        "tempo": "2-3 mesi",
        "corsi": ["AWS Cloud Practitioner", "A Cloud Guru"],
        "pratica": "Deploy app su EC2, S3, Lambda (free tier)",
        "certificazioni": "AWS Certified Cloud Practitioner"
    },
    "Docker": {
        "difficoltà": "Media",
        "tempo": "2-3 settimane",
        "corsi": ["Docker Documentation", "Docker Mastery (Udemy)"],
        "pratica": "Containerizza i tuoi progetti",
        "certificazioni": "Skill pratica, non certificazioni"
    },
    "Kubernetes": {
        "difficoltà": "Alta",
        "tempo": "2-3 mesi",
        "corsi": ["Kubernetes Basics", "K8s Documentation"],
        "pratica": "Minikube local, deploy apps su cluster",
        "certificazioni": "CKA (Certified Kubernetes Admin)"
    },
    
    # ------------------------------------------------------------------------
    # FRONTEND
    # ------------------------------------------------------------------------
    "React": {
        "difficoltà": "Media",
        "tempo": "1-2 mesi",
        "corsi": ["React Documentation", "Scrimba React Course"],
        "pratica": "Build 5+ progetti personali",
        "certificazioni": "Portfolio > Certificazioni"
    },
    "HTML/CSS": {
        "difficoltà": "Bassa",
        "tempo": "2-4 settimane",
        "corsi": ["freeCodeCamp Responsive Design", "MDN Web Docs"],
        "pratica": "Build 10 landing pages",
        "certificazioni": "Non necessarie"
    },
    
    # ------------------------------------------------------------------------
    # BUSINESS INTELLIGENCE
    # ------------------------------------------------------------------------
    "Excel": {
        "difficoltà": "Bassa-Media",
        "tempo": "2-3 settimane",
        "corsi": ["Excel Essential Training (LinkedIn)", "Chandoo.org"],
        "pratica": "Pivot tables, dashboard, macros con dati reali",
        "certificazioni": "Microsoft Office Specialist Excel"
    },
    "Power BI": {
        "difficoltà": "Media",
        "tempo": "1-2 mesi",
        "corsi": ["Microsoft Power BI Training", "Enterprise DNA"],
        "pratica": "Build dashboard con dati pubblici",
        "certificazioni": "Microsoft Data Analyst Associate"
    },
    "Tableau": {
        "difficoltà": "Media",
        "tempo": "1-2 mesi",
        "corsi": ["Tableau Desktop Specialist", "Tableau Public"],
        "pratica": "Visualizzazioni su Tableau Public",
        "certificazioni": "Tableau Desktop Specialist"
    },
    "Looker": {
        "difficoltà": "Media",
        "tempo": "1-2 mesi",
        "corsi": ["Google Cloud Skills Boost", "Looker docs"],
        "pratica": "Build dashboards con Google Cloud",
        "certificazioni": "Google Cloud Certified Pro"
    },
    
    # ------------------------------------------------------------------------
    # SOFT SKILLS
    # ------------------------------------------------------------------------
    "Teamwork": {
        "difficoltà": "Bassa-Media",
        "tempo": "Ongoing",
        "corsi": ["Skill pratica, non corsi teorici"],
        "pratica": "Open Source collaboration, hackathon, team projects",
        "certificazioni": "Non applicabile"
    },
    "Communication": {
        "difficoltà": "Media",
        "tempo": "Ongoing",
        "corsi": ["Public Speaking, Writing courses"],
        "pratica": "Blog tecnico, presentazioni, networking",
        "certificazioni": "Non applicabile"
    },
    "Leadership": {
        "difficoltà": "Media-Alta",
        "tempo": "Ongoing",
        "corsi": ["Leadership courses (Coursera, LinkedIn)"],
        "pratica": "Lead projects, mentoring",
        "certificazioni": "PMP (Project Management Pro)"
    },
    "Agile": {
        "difficoltà": "Bassa-Media",
        "tempo": "2-4 settimane",
        "corsi": ["Scrum.org Learning Path", "Agile Foundations"],
        "pratica": "Apply Agile in progetti reali",
        "certificazioni": "PSM I (Professional Scrum Master)"
    },
    
    # ------------------------------------------------------------------------
    # TESTING & VERSION CONTROL
    # ------------------------------------------------------------------------
    "Testing": {
        "difficoltà": "Bassa-Media",
        "tempo": "1-2 mesi",
        "corsi": ["Test Automation University", "Software Testing courses"],
        "pratica": "Write tests per tutti i progetti, TDD",
        "certificazioni": "ISTQB Foundation Level"
    },
    "Git": {
        "difficoltà": "Bassa",
        "tempo": "1-2 settimane",
        "corsi": ["Git Documentation", "Learn Git Branching (interattivo)"],
        "pratica": "Usa Git daily, contribute to Open Source",
        "certificazioni": "Non necessarie"
    },
}

# Risorsa di default per skill non mappate
DEFAULT_LEARNING_RESOURCE = {
    "difficoltà": "Varia",
    "tempo": "1-3 mesi",
    "corsi": ["Cerca corsi su Coursera, Udemy, YouTube"],
    "pratica": "Progetti pratici, tutorial, documentazione ufficiale",
    "certificazioni": "Verifica certificazioni disponibili online"
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
# FUNZIONE: ESTRAZIONE TESTO DA PDF
# ============================================================================
# PILASTRO TEXT MINING: Estensione per gestire documenti PDF
# ============================================================================

def extract_text_from_pdf(pdf_file) -> str:
    """
    Estrae il testo da un file PDF caricato dall'utente.
    
    ALGORITMO:
    1. Legge il file PDF usando PyPDF2
    2. Itera su tutte le pagine
    3. Estrae il testo da ogni pagina
    4. Concatena tutto in un'unica stringa
    
    Args:
        pdf_file: File PDF caricato tramite st.file_uploader
    
    Returns:
        str: Testo estratto dal PDF
    
    Raises:
        Exception: Se PyPDF2 non è installato o il PDF è corrotto
    """
    if PdfReader is None:
        raise ImportError(
            "PyPDF2 non è installato. "
            "Installa con: pip install PyPDF2"
        )
    
    try:
        # Crea un oggetto PdfReader dal file caricato
        pdf_reader = PdfReader(pdf_file)
        
        # Lista per accumulare il testo di tutte le pagine
        text_parts = []
        
        # Itera su tutte le pagine del PDF
        for page_num, page in enumerate(pdf_reader.pages):
            # Estrai il testo dalla pagina
            page_text = page.extract_text()
            
            if page_text:
                text_parts.append(page_text)
        
        # Unisci tutto il testo con spazi
        full_text = " ".join(text_parts)
        
        return full_text
    
    except Exception as e:
        raise Exception(f"Errore nella lettura del PDF: {str(e)}")


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
    IMPORTANTE: Le soft skills sono ESCLUSE dal calcolo della percentuale.
    
    ALGORITMO:
    1. Filtra soft skills da entrambi i set
    2. Intersezione: Trova skill comuni (job_skills ∩ cv_skills)
    3. Differenza: Trova skill mancanti (job_skills - cv_skills)
    4. Scoring: Percentuale = (skill_comuni / skill_richieste) * 100
    
    Args:
        job_skills (Set[str]): Competenze richieste dall'annuncio
        cv_skills (Set[str]): Competenze possedute dal candidato
    
    Returns:
        Tuple[float, Set[str], Set[str]]: 
            - Percentuale di match (0-100) basata su HARD SKILLS
            - Set di skill possedute
            - Set di skill mancanti
    """
    # STEP 1: Filtra soft skills (non contano per la percentuale)
    hard_job_skills = job_skills - SOFT_SKILLS
    hard_cv_skills = cv_skills - SOFT_SKILLS
    
    # Caso edge: nessuna hard skill richiesta
    if not hard_job_skills:
        return 0.0, set(), set()
    
    # STEP 2: OPERAZIONI INSIEMISTICHE (Set Theory) - solo hard skills
    matched_skills = hard_job_skills.intersection(hard_cv_skills)  # A ∩ B
    missing_skills = hard_job_skills.difference(hard_cv_skills)    # A - B
    
    # STEP 3: CALCOLO PERCENTUALE DI MATCH (solo hard skills)
    # Formula: (hard_skill_match / hard_skill_totali_richieste) * 100
    match_percentage = (len(matched_skills) / len(hard_job_skills)) * 100
    
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
    
    # Tab per scegliere tra testo o PDF
    input_method = st.radio(
        "Modalità di input:",
        ["📝 Testo", "📎 Upload PDF"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    cv_text = ""
    
    if input_method == "📝 Testo":
        # Text area per input CV manuale
        cv_text = st.text_area(
            "Incolla qui il tuo CV o lista di competenze",
            height=300,
            placeholder="Esperienza con Python, JavaScript, React, PostgreSQL...",
            key="cv_text_input"
        )
    else:
        # File uploader per PDF
        uploaded_file = st.file_uploader(
            "Carica il tuo CV in formato PDF",
            type=["pdf"],
            help="Carica un file PDF del tuo curriculum vitae"
        )
        
        if uploaded_file is not None:
            try:
                # Estrai testo dal PDF
                with st.spinner("📖 Lettura del PDF in corso..."):
                    cv_text = extract_text_from_pdf(uploaded_file)
                
                # Mostra preview del testo estratto
                with st.expander("👁️ Anteprima testo estratto"):
                    st.text(cv_text[:500] + "..." if len(cv_text) > 500 else cv_text)
                
                st.success(f"✅ PDF caricato! Estratte {len(cv_text)} caratteri.")
            
            except ImportError as e:
                st.error(
                    "❌ PyPDF2 non installato. "
                    "Esegui: `pip install PyPDF2`"
                )
            except Exception as e:
                st.error(f"❌ Errore nella lettura del PDF: {str(e)}")
        else:
            st.info("👆 Carica un file PDF per iniziare l'analisi")

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
        
        # COLONNA DESTRA: Skill mancanti con GUIDA COMPATTA
        with col_missing:
            st.subheader("❌ Skill Mancanti")
            
            if missing_skills:
                missing_list = sorted(missing_skills)
                st.markdown(f"**{len(missing_list)} competenze** da sviluppare")
                
                # Mostra solo TOP 3 skill con raccomandazioni
                st.markdown("---")
                st.markdown("**🎯 Priorità (Top 3):**")
                
                for skill in missing_list[:3]:  # Solo prime 3
                    st.error(f"✗ {skill}")
                    resource = LEARNING_RESOURCES.get(skill, DEFAULT_LEARNING_RESOURCE)
                    
                    # Info compatta in una riga
                    st.caption(
                        f"⏱️ {resource['tempo']} | "
                        f"📊 {resource['difficoltà']} | "
                        f"📖 {resource['corsi'][0]}"
                    )
                
                # Altre skill (se ci sono) in expander compatto
                if len(missing_list) > 3:
                    with st.expander(f"➕ Altre {len(missing_list) - 3} skill da sviluppare"):
                        for skill in missing_list[3:]:
                            resource = LEARNING_RESOURCES.get(skill, DEFAULT_LEARNING_RESOURCE)
                            st.write(f"• **{skill}** - {resource['tempo']}, {resource['difficoltà']}")
                
                # Consiglio finale compatto
                st.info("💡 Inizia dalla prima skill in lista (più rilevante)")
            
            else:
                st.success("🎉 Hai tutte le skill richieste!")
                st.balloons()
        
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
