import streamlit as st
import re
from typing import Set, Tuple, List

# Configurazione pagina
st.set_page_config(
    page_title="Job Seeker Helper",
    page_icon="🎯",
    layout="wide"
)

# Gruppi di competenze correlate - ogni gruppo rappresenta skill simili/correlate
SKILL_GROUPS = {
    # Linguaggi di programmazione
    "Python": ["Python", "Python3", "PyPy", "Sviluppo Python", "Python Developer", "Python dev"],
    "Java": ["Java", "JDK", "JRE", "Java Developer", "Java dev", "JavaEE", "J2EE"],
    "JavaScript": ["JavaScript", "JS", "ECMAScript", "ES6", "ES2015", "Node", "Node.js", "NodeJS"],
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
    
    # Frontend
    "React": ["React", "ReactJS", "React.js", "React Native", "Next.js", "NextJS"],
    "Angular": ["Angular", "AngularJS", "Angular2+", "Angular dev"],
    "Vue": ["Vue", "Vue.js", "VueJS", "Nuxt", "Nuxt.js"],
    "HTML/CSS": ["HTML", "CSS", "HTML5", "CSS3", "SASS", "SCSS", "LESS", "Tailwind", "Bootstrap"],
    "Frontend": ["Frontend", "Front-end", "Front end", "UI Development", "Web Development"],
    
    # Backend
    "Django": ["Django", "Django REST", "DRF"],
    "Flask": ["Flask", "Flask-RESTful"],
    "FastAPI": ["FastAPI", "Fast API"],
    "Spring": ["Spring", "Spring Boot", "SpringBoot", "Spring Framework"],
    "Express": ["Express", "ExpressJS", "Express.js"],
    "Backend": ["Backend", "Back-end", "Back end", "Server-side"],
    
    # Database
    "SQL": ["SQL", "MySQL", "PostgreSQL", "MS SQL", "SQL Server", "MariaDB", "Database", "DB", "Relational Database"],
    "NoSQL": ["NoSQL", "MongoDB", "Cassandra", "CouchDB", "Document DB"],
    "Database Management": ["Database", "DB", "Database Management", "DBMS", "Data Storage"],
    
    # Cloud
    "AWS": ["AWS", "Amazon Web Services", "EC2", "S3", "Lambda", "Cloud AWS"],
    "Azure": ["Azure", "Microsoft Azure", "Azure Cloud"],
    "GCP": ["GCP", "Google Cloud", "Google Cloud Platform"],
    "Cloud": ["Cloud", "Cloud Computing", "Cloud Infrastructure", "Cloud Services"],
    
    # DevOps
    "Docker": ["Docker", "Containerization", "Container", "Dockerfile"],
    "Kubernetes": ["Kubernetes", "K8s", "Container Orchestration"],
    "CI/CD": ["CI/CD", "Continuous Integration", "Continuous Deployment", "Jenkins", "GitLab CI", "GitHub Actions", "CI CD"],
    "DevOps": ["DevOps", "Dev Ops", "Site Reliability", "SRE"],
    
    # Data Science & AI
    "Machine Learning": ["Machine Learning", "ML", "Deep Learning", "AI", "Artificial Intelligence", "Neural Networks", "Deep Neural Networks"],
    "Data Science": ["Data Science", "Data Scientist", "Data Analysis", "Data Analytics", "Big Data", "Data Mining"],
    "TensorFlow": ["TensorFlow", "Tensorflow", "TF", "Keras"],
    "PyTorch": ["PyTorch", "Torch"],
    "Pandas": ["Pandas", "Data Manipulation", "Data Processing"],
    "NLP": ["NLP", "Natural Language Processing", "Text Mining", "Text Analysis", "Linguistics"],
    "Computer Vision": ["Computer Vision", "CV", "Image Processing", "Image Recognition", "Object Detection"],
    
    # Version Control
    "Git": ["Git", "GitHub", "GitLab", "Bitbucket", "Version Control", "Source Control", "VCS"],
    
    # Testing
    "Testing": ["Testing", "Test", "QA", "Quality Assurance", "Unit Test", "Integration Test", "Test Automation"],
    "Selenium": ["Selenium", "Test Automation", "Web Testing"],
    
    # Agile & Project Management
    "Agile": ["Agile", "Scrum", "Kanban", "Sprint", "Agile Methodology", "Agile Development"],
    "Project Management": ["Project Management", "PM", "Product Management", "Gestione Progetti", "PMP"],
    
    # Soft Skills
    "Teamwork": ["Team Working", "Teamwork", "Team work", "Lavoro di squadra", "Collaborazione", "Collaboration"],
    "Communication": ["Communication", "Comunicazione", "Presentation", "Public Speaking"],
    "Problem Solving": ["Problem Solving", "Critical Thinking", "Analytical", "Analytical Skills"],
    "Leadership": ["Leadership", "Team Leading", "Mentoring", "Management", "Lead"],
    
    # Lingue
    "English": ["English", "Inglese", "Lingua Inglese", "English Language"],
    "Italian": ["Italian", "Italiano", "Lingua Italiana"],
    
    # Mobile
    "Mobile Development": ["Mobile", "Mobile Development", "iOS", "Android", "React Native", "Flutter", "Mobile dev"],
    
    # Security
    "Security": ["Security", "Cybersecurity", "Cyber Security", "Information Security", "Sicurezza", "Penetration Testing"],
    
    # Design
    "UI/UX": ["UI", "UX", "User Experience", "User Interface", "Design", "UI Design", "UX Design", "Product Design"],
    
    # Altri tools
    "Excel": ["Excel", "Microsoft Excel", "Spreadsheet", "Fogli di calcolo"],
    "Power BI": ["Power BI", "PowerBI", "Business Intelligence", "BI"],
}


def normalize_and_extract(text: str) -> Set[str]:
    """
    Estrae le skill dal testo in modo più intelligente, riconoscendo variazioni e concetti correlati.
    Restituisce un set di skill normalizzate (le chiavi dei gruppi).
    """
    found_skills = set()
    text_lower = text.lower()
    
    # Per ogni gruppo di skill
    for main_skill, variations in SKILL_GROUPS.items():
        # Controlla se almeno una variazione è presente nel testo
        for variation in variations:
            # Pattern più flessibile che cattura anche variazioni
            # Es: "Python developer", "sviluppo in Python", etc.
            pattern = r'\b' + re.escape(variation.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.add(main_skill)
                break  # Trovata una variazione, passa al prossimo gruppo
    
    return found_skills


def calculate_match(job_skills: Set[str], cv_skills: Set[str]) -> Tuple[float, Set[str], Set[str]]:
    """
    Calcola la percentuale di match tra skill richieste e possedute.
    Restituisce: (percentuale, skill_possedute, skill_mancanti)
    """
    if not job_skills:
        return 0.0, set(), set()
    
    matched_skills = job_skills.intersection(cv_skills)
    missing_skills = job_skills.difference(cv_skills)
    
    match_percentage = (len(matched_skills) / len(job_skills)) * 100
    
    return match_percentage, matched_skills, missing_skills


def get_match_message(percentage: float) -> str:
    """
    Restituisce un messaggio dinamico basato sulla percentuale di match.
    """
    if percentage < 40:
        return "🔴 Match Basso - Richieste forse irrealistiche o profilo junior"
    elif percentage <= 75:
        return "🟡 Match Medio - Buona base"
    else:
        return "🟢 Match Alto - Profilo ideale"


# UI
st.title("🎯 Job Seeker Helper")
st.markdown("### Analizza la compatibilità tra annuncio di lavoro e il tuo CV")
st.markdown("---")

# Input areas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Annuncio di Lavoro")
    job_text = st.text_area(
        "Incolla qui il testo dell'annuncio",
        height=300,
        placeholder="Cerca Software Engineer con esperienza in Python, SQL, Docker..."
    )

with col2:
    st.subheader("📄 Il tuo CV / Lista Skill")
    cv_text = st.text_area(
        "Incolla qui il tuo CV o lista di competenze",
        height=300,
        placeholder="Esperienza con Python, JavaScript, React, PostgreSQL..."
    )

st.markdown("---")

# Bottone analisi
if st.button("🔍 Analizza Match", type="primary", use_container_width=True):
    if not job_text or not cv_text:
        st.warning("⚠️ Compila entrambi i campi per procedere con l'analisi!")
    else:
        # Estrazione skill con riconoscimento intelligente
        job_skills = normalize_and_extract(job_text)
        cv_skills = normalize_and_extract(cv_text)
        
        # Calcolo match
        match_percentage, matched_skills, missing_skills = calculate_match(job_skills, cv_skills)
        
        # Output
        st.markdown("---")
        st.subheader("📊 Risultato dell'Analisi")
        
        # Progress bar
        st.metric("Percentuale di Match", f"{match_percentage:.1f}%")
        st.progress(match_percentage / 100)
        
        # Messaggio dinamico
        st.info(get_match_message(match_percentage))
        
        st.markdown("---")
        
        # Colonne con dettagli
        col_matched, col_missing = st.columns(2)
        
        with col_matched:
            st.subheader("✅ Skill Possedute")
            if matched_skills:
                for skill in sorted(matched_skills):
                    st.success(f"✓ {skill}")
            else:
                st.write("Nessuna skill in comune trovata.")
        
        with col_missing:
            st.subheader("❌ Skill Mancanti")
            if missing_skills:
                for skill in sorted(missing_skills):
                    st.error(f"✗ {skill}")
            else:
                st.write("Hai tutte le skill richieste! 🎉")
        
        # Info aggiuntive
        st.markdown("---")
        st.caption(f"📈 Skill rilevate nell'annuncio: {len(job_skills)} | Skill rilevate nel CV: {len(cv_skills)}")
