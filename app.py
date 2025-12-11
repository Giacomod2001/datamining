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
from typing import Set, Tuple, List, Optional  # Type hints per code clarity
import io              # Input/Output per gestione file in memoria
import plotly.graph_objects as go  # Grafici interattivi
import plotly.express as px  # Charts veloci

# PDF Processing
try:
    from PyPDF2 import PdfReader  # Lettura e estrazione testo da PDF
except ImportError:
    PdfReader = None  # Fallback se PyPDF2 non è installato

# NLP Avanzato con spaCy
try:
    import spacy
    from spacy.matcher import PhraseMatcher
    # Lazy loading del modello (caricato solo quando necessario)
    @st.cache_resource
    def load_nlp_model():
        """Carica modello spaCy con caching per performance"""
        try:
            return spacy.load("en_core_web_md")  # Medium model con word vectors
        except OSError:
            st.warning("⚠️ Modello spaCy non trovato. Esegui: python -m spacy download en_core_web_md")
            return None
except ImportError:
    spacy = None
    PhraseMatcher = None
    def load_nlp_model():
        return None

# Fuzzy matching per typos
try:
    import Levenshtein
except ImportError:
    Levenshtein = None

# ============================================================================
# CONFIGURAZIONE APPLICAZIONE WEB
# ============================================================================
st.set_page_config(
    page_title="Job Seeker Helper - AI Powered",
    page_icon="🎯",
    layout="wide",  # Layout espanso
    initial_sidebar_state="collapsed"  # Sidebar nascosta di default
)

# ============================================================================
# CUSTOM CSS - LINKEDIN-INSPIRED DESIGN
# ============================================================================
st.markdown("""
<style>
    /* LinkedIn Color Palette */
    :root {
        --linkedin-blue: #0077B5;
        --linkedin-dark: #004182;
        --white: #FFFFFF;
        --gray-50: #F8F9FA;
        --gray-100: #E9ECEF;
        --gray-200: #DEE2E6;
        --gray-700: #495057;
        --gray-900: #212529;
        --success: #057642;
        --danger: #CC1016;
    }
    
    /* Global Styles */
    .main {
        background-color: var(--gray-50);
    }
    
    /* Professional Header */
    .linkedin-header {
        background: linear-gradient(135deg, var(--linkedin-blue) 0%, var(--linkedin-dark) 100%);
        padding: 2.5rem 2rem;
        border-radius: 8px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0, 119, 181, 0.15);
    }
    
    .linkedin-header h1 {
        color: var(--white);
        font-size: 2.5rem;
        font-weight: 600;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .linkedin-header p {
        color: rgba(255,255,255,0.95);
        font-size: 1.1rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Card Containers */
    .results-card {
        background: var(--white);
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        border: 1px solid var(--gray-200);
    }
    
    /* Skill Badges - LinkedIn Style */
    .skill-badge {
        display: inline-block;
        background: var(--linkedin-blue);
        color: var(--white);
        padding: 0.4rem 0.9rem;
        border-radius: 16px;
        margin: 0.25rem;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .skill-badge-missing {
        background: var(--gray-200);
        color: var(--gray-700);
    }
    
    /* Clean Streamlit Elements */
    .stButton > button {
        background-color: var(--linkedin-blue);
        color: var(--white);
        border: none;
        border-radius: 24px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background-color: var(--linkedin-dark);
        box-shadow: 0 4px 12px rgba(0, 119, 181, 0.2);
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background-color: var(--linkedin-blue);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: var(--linkedin-blue);
        font-size: 2rem;
    }
    
    /* Remove Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: var(--gray-100);
    }
    ::-webkit-scrollbar-thumb {
        background: var(--linkedin-blue);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--linkedin-dark);
    }
    
    /* Input Fields */
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid var(--gray-200);
    }
    
    .stTextArea textarea:focus {
        border-color: var(--linkedin-blue);
        box-shadow: 0 0 0 1px var(--linkedin-blue);
    }
</style>
""", unsafe_allow_html=True)


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
# FUNZIONE: SIMILARITÀ SEMANTICA CON spaCy (NLP AVANZATO)
# ============================================================================
# PILASTRO NLP AVANZATO: Matching intelligente oltre le keyword esatte
# ============================================================================

@st.cache_data
def semantic_skill_match(text: str, skill_variations: List[str], _nlp_model=None, threshold: float = 0.75) -> bool:
    """
    Usa spaCy word vectors per matching semantico.
    
    Riconosce skill anche se non sono keyword esatte ma semanticamente simili.
    Esempio: "Python programmer" matcha con "Python developer"
    
    Args:
        text: Testo dove cercare
        skill_variations: Lista di variazioni della skill
        _nlp_model: Modello spaCy (prefix _ per evitare hashing in cache)
        threshold: Soglia di similarity (0-1), default 0.75
    
    Returns:
        bool: True se trova match semantico
    """
    if not _nlp_model or not hasattr(_nlp_model, 'vocab'):
        # Fallback a regex se spaCy non disponibile
        text_lower = text.lower()
        for variation in skill_variations:
            pattern = r'\b' + re.escape(variation.lower()) + r'\b'
            if re.search(pattern, text_lower):
                return True
        return False
    
    # Processa il testo con spaCy
    doc = _nlp_model(text.lower())
    
    # Per ogni variazione della skill
    for variation in skill_variations:
        variation_doc = _nlp_model(variation.lower())
        
        # Calcola similarità usando word vectors
        if variation_doc.has_vector and doc.has_vector:
            similarity = variation_doc.similarity(doc)
            if similarity >= threshold:
                return True
        
        # Fallback: regex se no word vectors
        pattern = r'\b' + re.escape(variation.lower()) + r'\b'
        if re.search(pattern, text.lower()):
            return True
    
    return False




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


# ==============================================================================
# INTERFACCIA UTENTE - LINKEDIN PROFESSIONAL DESIGN
# ============================================================================

# Professional Header
st.markdown("""
<div class="linkedin-header">
    <h1>🎯 Job Seeker Helper</h1>
    <p>AI-Powered CV-Job Matching Platform</p>
</div>
""", unsafe_allow_html=True)

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
                
                st.success(f"✅ PDF caricato! Estratti {len(cv_text)} caratteri.")
            
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
        # VISUALIZZAZIONE RISULTATI - DESIGN PROFESSIONALE
        # ====================================================================
        
        st.markdown("---")
        
        # CARD RISULTATI con chart interattivo
        col_chart, col_metrics = st.columns([1, 1])
        
        with col_chart:
            st.subheader("📊 Match Analysis")
            
            # Donut Chart - LinkedIn Style
            fig = go.Figure(data=[go.Pie(
                labels=['Matched Skills', 'Skills Gap'],
                values=[len(matched_skills), len(missing_skills)],
                hole=0.65,
                marker=dict(colors=['#0077B5', '#E9ECEF']),
                textinfo='label+percent',
                textfont_size=13,
                textfont_color='#212529'
            )])
            
            fig.update_layout(
                showlegend=False,
                height=280,
                margin=dict(t=0, b=0, l=0, r=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                annotations=[dict(
                    text=f'{match_percentage:.0f}%',
                    x=0.5, y=0.5,
                    font_size=36,
                    showarrow=False,
                    font=dict(color='#0077B5', family='Arial', weight='bold')
                )]
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col_metrics:
            st.subheader("📈 Key Metrics")
            
            # Clean metrics display
            m1, m2 = st.columns (2)
            with m1:
                st.metric("Match Score", f"{match_percentage:.0f}%")
            with m2:
                st.metric("Total Skills", len(job_skills))
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Status indicator - clean design
            if match_percentage >= 75:
                st.success("✅ **Strong Match** - Excellent fit for this role")
            elif match_percentage >= 50:
                st.info("ℹ️ **Good Match** - Solid foundation, worth applying")
            else:
                st.warning("⚠️ **Developing Match** - Consider upskilling first")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ====================================================================
        # SKILL DETAILS - CATEGORIZED DRILL-DOWN
        # ====================================================================
        
        # Funzione helper per categorizzare skill
        def categorize_skills(skills_set):
            categories = {
                "Programming": [],
                "Data & Analytics": [],
                "Cloud & DevOps": [],
                "Business Intelligence": [],
                "Soft Skills": []
            }
            
            for skill in skills_set:
                if skill in ["Python", "Java", "JavaScript", "C++", "C#", "R", "Go"]:
                    categories["Programming"].append(skill)
                elif skill in ["Data Science", "Machine Learning", "NLP", "Deep Learning", "AI", "Pandas", "SQL", "PostgreSQL", "MySQL", "MongoDB"]:
                    categories["Data & Analytics"].append(skill)
                elif skill in ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "DevOps"]:
                    categories["Cloud & DevOps"].append(skill)
                elif skill in ["Power BI", "Tableau", "Looker", "Excel"]:
                    categories["Business Intelligence"].append(skill)
                elif skill in ["Leadership", "Communication", "Teamwork", "Agile", "Project Management"]:
                    categories["Soft Skills"].append(skill)
                else:
                    # Default alla categoria più probabile
                    if "data" in skill.lower() or "sql" in skill.lower():
                        categories["Data & Analytics"].append(skill)
                    else:
                        categories["Programming"].append(skill)
            
            # Rimuovi categorie vuote
            return {k: v for k, v in categories.items() if v}
        
        col_matched, col_missing = st.columns(2)
        
        # === MATCHED SKILLS - COMPACT ===
        with col_matched:
            st.subheader("✅ Matched Skills")
            
            if matched_skills:
                categorized_matched = categorize_skills(matched_skills)
                
                # Mostra count compatto
                st.metric("Total Matched", len(matched_skills))
                
                # Drill-down per categoria
                for category, skills in categorized_matched.items():
                    with st.expander(f"📁 {category} ({len(skills)})"):
                        for skill in sorted(skills):
                            st.success(f"✓ {skill}", icon="✅")
            else:
                st.info("No skills matched")
        
        # === MISSING SKILLS - DETAILED LEARNING RESOURCES ===
        with col_missing:
            st.subheader("❌ Skills Gap")
            
            if missing_skills:
                categorized_missing = categorize_skills(missing_skills)
                
                # Mostra count
                st.metric("Skills to Develop", len(missing_skills))
                
                # Drill-down per ogni skill con risorse COMPLETE
                for category, skills in categorized_missing.items():
                    with st.expander(f"📁 {category} ({len(skills)})", expanded=(category == list(categorized_missing.keys())[0])):
                        for skill in sorted(skills):
                            st.error(f"**{skill}**", icon="❌")
                            
                            # Ottieni risorse complete
                            resource = LEARNING_RESOURCES.get(skill, DEFAULT_LEARNING_RESOURCE)
                            
                            # Box con dettagli completi
                            with st.container():
                                # Metrics row
                                c1, c2 = st.columns(2)
                                with c1:
                                    st.caption(f"⏱️ **Time:** {resource['tempo']}")
                                with c2:
                                    st.caption(f"📊 **Level:** {resource['difficoltà']}")
                                
                                # Learning path completo
                                st.markdown("**📚 Learning Path:**")
                                for i, corso in enumerate(resource['corsi'], 1):
                                    st.markdown(f"{i}. {corso}")
                                
                                st.markdown(f"**🛠️ Practice:** {resource['pratica']}")
                                st.markdown(f"**🏆 Certification:** {resource['certificazioni']}")
                                
                                st.markdown("---")
                
                # Suggerimento strategico
                st.info("💡 **Strategy:** Focus on one category at a time. Start with highest priority skills for this role.")
            
            else:
                st.success("🎉 Perfect match! You have all required skills!")
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
