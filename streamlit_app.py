import streamlit as st
import re
from typing import Set, Tuple, List

# Configurazione pagina
st.set_page_config(
    page_title="Job Seeker Helper",
    page_icon="🎯",
    layout="wide"
)

# Lista completa di keyword hardcoded
KEYWORDS = [
    # Linguaggi di programmazione
    "Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "PHP", "Ruby", "Go", "Golang",
    "Rust", "Kotlin", "Swift", "R", "Scala", "Perl", "Shell", "Bash", "PowerShell",
    
    # Frontend
    "HTML", "CSS", "React", "Angular", "Vue", "Vue.js", "Svelte", "Next.js", "Nuxt.js",
    "jQuery", "Bootstrap", "Tailwind", "SASS", "SCSS", "Webpack", "Vite",
    
    # Backend
    "Node.js", "Express", "Django", "Flask", "FastAPI", "Spring", "Spring Boot",
    ".NET", "ASP.NET", "Laravel", "Rails", "Symfony",
    
    # Database
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle", "SQLite", "Redis", "Cassandra",
    "DynamoDB", "MariaDB", "MSSQL", "SQL Server", "NoSQL", "Firebase",
    
    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Google Cloud", "Docker", "Kubernetes", "K8s", "Jenkins",
    "GitLab", "GitHub Actions", "CI/CD", "Terraform", "Ansible", "Chef", "Puppet",
    
    # Data Science & ML
    "Machine Learning", "Deep Learning", "AI", "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Jupyter", "NLP", "Computer Vision",
    "Data Analysis", "Data Science", "Big Data", "Spark", "Hadoop", "Kafka",
    
    # Tools & Software
    "Git", "GitHub", "GitLab", "Bitbucket", "Jira", "Confluence", "Trello", "Slack",
    "Excel", "Power BI", "Tableau", "Looker", "QlikView", "SAP", "Salesforce",
    
    # Metodologie & Pratiche
    "Agile", "Scrum", "Kanban", "DevOps", "TDD", "BDD", "Microservices", "REST", "RESTful",
    "API", "GraphQL", "SOAP", "Waterfall", "Lean", "Six Sigma",
    
    # Project Management
    "Project Management", "Product Management", "Team Leading", "Leadership", "Mentoring",
    "Stakeholder Management", "Budget Management", "Risk Management",
    
    # Soft Skills
    "Team Working", "Teamwork", "Communication", "Problem Solving", "Critical Thinking",
    "Time Management", "Adaptability", "Creativity", "Analytical Skills", "Attention to Detail",
    
    # Lingue
    "Inglese", "English", "Francese", "French", "Tedesco", "German", "Spagnolo", "Spanish",
    "Italiano", "Italian", "Cinese", "Chinese", "Giapponese", "Japanese",
    
    # Testing
    "Testing", "Unit Testing", "Integration Testing", "Test Automation", "Selenium",
    "Jest", "Mocha", "Pytest", "JUnit", "Cypress", "QA",
    
    # Security
    "Cybersecurity", "Security", "Penetration Testing", "OWASP", "Encryption",
    "Authentication", "Authorization", "OAuth", "JWT", "SSL", "TLS",
    
    # Mobile
    "iOS", "Android", "React Native", "Flutter", "Xamarin", "Mobile Development",
    
    # Altri
    "Blockchain", "Solidity", "Ethereum", "Web3", "IoT", "Arduino", "Raspberry Pi",
    "Linux", "Unix", "Windows Server", "Networking", "TCP/IP", "VPN", "DNS",
    "UX", "UI", "User Experience", "User Interface", "Design Thinking", "Figma",
    "Adobe XD", "Sketch", "Photoshop", "Illustrator"
]


def extract_keywords(text: str, keywords: List[str]) -> Set[str]:
    """
    Estrae le keyword presenti nel testo usando regex case-insensitive.
    """
    found = set()
    text_lower = text.lower()
    
    for keyword in keywords:
        # Usa word boundary per evitare match parziali
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.add(keyword)
    
    return found


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
        # Estrazione skill
        job_skills = extract_keywords(job_text, KEYWORDS)
        cv_skills = extract_keywords(cv_text, KEYWORDS)
        
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
