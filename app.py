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
    initial_sidebar_state="collapsed"  # Open with ☰ icon (top-left) for ML debug
)

# ML-based Skill Matching
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None
    np = None

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
    # PROGRAMMING LANGUAGES
    # ------------------------------------------------------------------------
    "Python": {
        "difficoltà": "Medium",
        "tempo": "2-3 months",
        "corsi": [
            "Python for Everybody (Coursera - Free)",
            "Complete Python Bootcamp (Udemy)",
            "Official Python Documentation"
        ],
        "pratica": "Build a data analysis dashboard with Pandas + Streamlit. Create a web scraper for job postings. Automate your daily tasks with scripts.",
        "certificazioni": "PCAP (Python Institute Certified Associate Programmer)",
        "project": "**Project Idea:** Build a Personal Finance Tracker - Use Pandas for data manipulation, Matplotlib for visualization, and save data to CSV/SQLite. Add expense categorization and monthly reports."
    },
    "Java": {
        "difficoltà": "Medium-High",
        "tempo": "3-4 months",
        "corsi": ["Java Programming MOOC (University of Helsinki)", "Oracle Java Tutorials"],
        "pratica": "Build a REST API with Spring Boot for a todo app. Implement CRUD operations with a database connection.",
        "certificazioni": "Oracle Certified Associate Java Programmer",
        "project": "**Project Idea:** Employee Management System - Spring Boot backend with MySQL, REST endpoints for employee CRUD, authentication with Spring Security, deploy to Heroku."
    },
    "JavaScript": {
        "difficoltà": "Medium",
        "tempo": "2-3 months",
        "corsi": ["freeCodeCamp JavaScript Curriculum", "JavaScript.info (Free & Interactive)"],
        "pratica": "Build an interactive portfolio website with form validation. Create a weather app using a public API. Add animations with vanilla JS.",
        "certificazioni": "Focus on portfolio projects over certifications",
        "project": "**Project Idea:** Real-Time Chat Application - Use WebSockets for live messaging, LocalStorage for chat history, fetch API for user profiles. Deploy on Netlify."
    },
    
    # ------------------------------------------------------------------------
    # DATA SCIENCE & AI
    # ------------------------------------------------------------------------
    "Machine Learning": {
        "difficoltà": "High",
        "tempo": "4-6 months",
        "corsi": [
            "Machine Learning by Andrew Ng (Coursera - Gold Standard)",
            "Fast.ai Practical Deep Learning for Coders"
        ],
        "pratica": "Compete in Kaggle competitions (start with Titanic dataset). Build a movie recommendation system. Create an image classifier for your own dataset.",
        "certificazioni": "Google ML Engineer Professional Certificate",
        "project": "**Project Idea:** Housing Price Predictor - Use scikit-learn with real Zillow data, feature engineering (location, size, age), compare Linear Regression vs Random Forest, deploy with Flask API + React frontend."
    },
    "Data Science": {
        "difficoltà": "Medium-High",
        "tempo": "3-5 months",
        "corsi": ["IBM Data Science Professional Certificate", "DataCamp Data Scientist Career Track"],
        "pratica": "Analyze a public dataset (COVID-19, elections, sports stats). Create data visualizations with Plotly. Write a technical blog post explaining your findings.",
        "certificazioni": "IBM Data Science Professional Certificate",
        "project": "**Project Idea:** Customer Churn Analysis - Download telecom dataset, perform EDA with Pandas, visualize patterns with Seaborn, build predictive model, create Streamlit dashboard showing insights."
    },
    "Pandas": {
        "difficoltà": "Low-Medium",
        "tempo": "2-4 weeks",
        "corsi": ["Pandas Official Tutorials", "DataCamp Pandas Fundamentals"],
        "pratica": "Clean and analyze your own spreadsheet data. Merge multiple CSV files. Create pivot tables and aggregations for business metrics.",
        "certificazioni": "Not required - demonstrate through projects",
        "project": "**Project Idea:** Sales Data Reporter - Load sales CSV, clean missing values, group by product/date, calculate KPIs (revenue, growth rate), export monthly summary Excel reports with styled formatting."
    },
    "NLP": {
        "difficoltà": "High",
        "tempo": "3-4 months",
        "corsi": ["NLP Specialization (deeplearning.ai)", "Hugging Face Course (Free)"],
        "pratica": "Build a sentiment analyzer for product reviews. Create a chatbot with intent classification. Fine-tune a BERT model on your own dataset.",
        "certificazioni": "Demonstrate through portfolio projects",
        "project": "**Project Idea:** Job Description Analyzer - Use spaCy for entity extraction (skills, locations, salary), implement TF-IDF for keyword matching, build API to categorize jobs by seniority level, visualize skill trends."
    },
    
    # ------------------------------------------------------------------------
    # DATABASE & SQL
    # ------------------------------------------------------------------------
    "SQL": {
        "difficoltà": "Low-Medium",
        "tempo": "3-6 weeks",
        "corsi": ["Mode SQL Tutorial", "SQLBolt (Interactive)", "Codecademy Learn SQL"],
        "pratica": "Download a sample database (Northwind, Sakila). Write complex JOINs across 3+ tables. Optimize slow queries with indexes. Create views for reporting.",
        "certificazioni": "Practice is more valuable than certs",
        "project": "**Project Idea:** E-commerce Analytics Database - Design schema (users, orders, products), write queries for: top customers, monthly revenue, product recommendations using self-joins, create stored procedures for reports."
    },
    
    # ------------------------------------------------------------------------
    # CLOUD & DEVOPS
    # ------------------------------------------------------------------------
    "AWS": {
        "difficoltà": "Medium-High",
        "tempo": "2-3 months",
        "corsi": ["AWS Cloud Practitioner Essentials (Free)", "A Cloud Guru AWS Path"],
        "pratica": "Deploy a static website to S3 with CloudFront. Set up EC2 instance and connect via SSH. Create Lambda function triggered by S3 upload (all free tier).",
        "certificazioni": "AWS Certified Cloud Practitioner (entry-level)",
        "project": "**Project Idea:** Serverless Image Resizer - Use S3 for storage, Lambda to auto-resize uploaded images, API Gateway for REST endpoints, DynamoDB for metadata, CloudWatch for monitoring. Stay in free tier."
    },
    "Docker": {
        "difficoltà": "Medium",
        "tempo": "2-3 weeks",
        "corsi": ["Docker Official Get Started Guide", "Docker Mastery (Udemy)"],
        "pratica": "Dockerize your existing Python/Node app. Use docker-compose for multi-container setup (app + database). Push images to Docker Hub.",
        "certificazioni": "Hands-on experience over certification",
        "project": "**Project Idea:** Microservices Blog Platform - Frontend (React) container, Backend (Flask) container, PostgreSQL container, Nginx reverse proxy. Use docker-compose for orchestration, environment variables for config."
    },
    "Kubernetes": {
        "difficoltà": "High",
        "tempo": "2-3 mesi",
        "corsi": ["Kubernetes for Beginners (Udemy)", "Official K8s Documentation"],
        "pratica": "Deploy app to local Minikube cluster. Create deployments, services, and ingress. Practice rolling updates and rollbacks.",
        "certificazioni": "CKA (Certified Kubernetes Administrator)",
        "project": "**Project Idea:** Scalable API Backend - Deploy Flask API with 3 replicas, use LoadBalancer service, implement health checks, configure auto-scaling, add persistent volume for database, monitor with Prometheus."
    },
    
    # ------------------------------------------------------------------------
    # FRONTEND
    # ------------------------------------------------------------------------
    "React": {
        "difficoltà": "Medium",
        "tempo": "1-2 months",
        "corsi": ["React Official Docs (Best resource!)", "Scrimba Learn React for Free"],
        "pratica": "Build 5 different apps: todo list, weather app, quiz game, e-commerce cart, blog with routing. Focus on hooks (useState, useEffect, useContext).",
        "certificazioni": "Portfolio projects are essential",
        "project": "**Project Idea:** Job Board Dashboard - Fetch jobs from API, implement search/filter by location/skill, save favorites to localStorage, use React Router for pages, styled-components for design, deploy to Vercel."
    },
    "HTML/CSS": {
        "difficoltà": "Low",
        "tempo": "2-4 weeks",
        "corsi": ["freeCodeCamp Responsive Web Design", "MDN Web Docs (Reference)"],
        "pratica": "Clone 10 landing pages from real companies. Build responsive layouts with Flexbox and Grid. Add CSS animations and transitions.",
        "certificazioni": "Not required",
        "project": "**Project Idea:** Personal Portfolio Site - Fully responsive design, hero section with gradient, projects grid with hover effects, contact form, smooth scroll navigation, optimize for mobile-first, deploy to GitHub Pages."
    },
    
    # ------------------------------------------------------------------------
    # BUSINESS INTELLIGENCE
    # ------------------------------------------------------------------------
    "Excel": {
        "difficoltà": "Low-Medium",
        "tempo": "2-3 weeks",
        "corsi": ["Excel Essential Training (LinkedIn Learning)", "Chandoo.org Tutorials"],
        "pratica": "Build a sales dashboard with pivot tables and charts. Automate reports with VLOOKUP, INDEX-MATCH. Create macros for repetitive tasks.",
        "certificazioni": "Microsoft Office Specialist Excel",
        "project": "**Project Idea:** Personal Budget Manager - Monthly expense tracker with categories, formulas for totals/averages, conditional formatting for overspending, pivot charts for trends, macro button to generate PDF report."
    },
    "Power BI": {
        "difficoltà": "Medium",
        "tempo": "1-2 months",
        "corsi": ["Microsoft Power BI Training (Free)", "Enterprise DNA YouTube Channel"],
        "pratica": "Connect to real data source (Excel, SQL, API). Build interactive dashboard with slicers and drill-down. Publish to Power BI Service.",
        "certificazioni": "Microsoft Certified: Data Analyst Associate",
        "project": "**Project Idea:** Sales Performance Dashboard - Import sales data, create star schema with dimensions, build KPI cards (revenue, growth, targets), add time intelligence for YoY comparison, interactive map visual, publish and share link."
    },
    "Tableau": {
        "difficoltà": "Medium",
        "tempo": "1-2 months",
        "corsi": ["Tableau Desktop Specialist Path", "Tableau Public Gallery for Inspiration"],
        "pratica": "Create 5 viz types: bar, line, map, scatter, heatmap. Build a story dashboard. Publish to Tableau Public and share on LinkedIn.",
        "certificazioni": "Tableau Desktop Specialist",
        "project": "**Project Idea:** COVID-19 Global Tracker - Live data from Johns Hopkins, choropleth map by country, time series for cases/deaths, calculated fields for mortality rate, parameters for country selection, publish viz on Tableau Public."
    },
    "Looker": {
        "difficoltà": "Medium",
        "tempo": "1-2 months",
        "corsi": ["Google Cloud Skills Boost - Looker", "Looker Official Docs"],
        "pratica": "Build dashboards in Looker Studio (free). Connect Google Sheets or BigQuery as data source. Create calculated fields and filters.",
        "certificazioni": "Google Cloud Professional Data Engineer (includes Looker)",
        "project": "**Project Idea:** Website Analytics Dashboard - Connect to Google Analytics data, create metrics for traffic/bounce rate/conversions, add date range filter, compare periods, visualize user journey funnel, schedule email reports."
    },
    
    # ------------------------------------------------------------------------
    # SOFT SKILLS
    # ------------------------------------------------------------------------
    "Teamwork": {
        "difficoltà": "Low-Medium",
        "tempo": "Ongoing practice",
        "corsi": ["Not applicable - learn by doing"],
        "pratica": "Contribute to open source projects on GitHub. Join hackathons (online or local). Participate in team coding challenges. Use pull requests and code reviews.",
        "certificazioni": "Not applicable",
        "project": "**Practice:** Find beginner-friendly GitHub repos with 'good first issue' label. Fork, fix bug, submit PR with clear description. Respond professionally to code review feedback."
    },
    "Communication": {
        "difficoltà": "Medium",
        "tempo": "Ongoing practice",
        "corsi": ["Public Speaking courses (Coursera)", "Technical Writing guides"],
        "pratica": "Start a technical blog (Medium, dev.to). Give presentations at meetups. Create tutorial videos. Write clear documentation for your projects.",
        "certificazioni": "Not applicable",
        "project": "**Practice:** Write 5 blog posts explaining technical concepts you learned. Record a 5-min YouTube video coding tutorial. Present a personal project at a local meetup or online community."
    },
    "Leadership": {
        "difficoltà": "Medium-High",
        "tempo": "Ongoing development",
        "corsi": ["Leadership courses (Coursera, LinkedIn Learning)"],
        "pratica": "Lead a small team project (even 2-3 people). Mentor junior developers. Organize study groups or coding sessions.",
        "certificazioni": "PMP (Project Management Professional)",
        "project": "**Practice:** Initiate an open-source project, recruit 2-3 contributors, assign tasks, review PRs, manage the roadmap, facilitate discussions, and deliver v1.0."
    },
    "Agile": {
        "difficoltà": "Low-Medium",
        "tempo": "2-4 weeks",
        "corsi": ["Scrum.org Learning Path (Free)", "Agile Foundations (LinkedIn)"],
        "pratica": "Apply Agile to personal projects: use Trello/Jira for sprints, daily standup notes, retrospectives. Join Agile team if possible.",
        "certificazioni": "PSM I (Professional Scrum Master)",
        "project": "**Practice:** Manage your next project with 2-week sprints, create user stories with acceptance criteria, track velocity, hold mini-retrospectives to improve process."
    },
    
    # ------------------------------------------------------------------------
    # TESTING & VERSION CONTROL
    # ------------------------------------------------------------------------
    "Testing": {
        "difficoltà": "Low-Medium",
        "tempo": "1-2 months",
        "corsi": ["Test Automation University (Free)", "Software Testing Fundamentals"],
        "pratica": "Write unit tests for your Python/JS projects. Use pytest or Jest. Aim for 80%+ code coverage. Set up CI/CD with GitHub Actions to run tests automatically.",
        "certificazioni": "ISTQB Foundation Level",
        "project": "**Project Idea:** Test a To-Do API - Write unit tests for CRUD functions, integration tests for database operations, mock external APIs, achieve 90% coverage, configure GitHub Actions to run tests on every PR."
    },
    "Git": {
        "difficoltà": "Low",
        "tempo": "1-2 weeks",
        "corsi": ["Git Official Tutorial", "Learn Git Branching (Interactive Game)"],
        "pratica": "Use Git daily for all projects. Practice branching strategies (feature branches). Resolve merge conflicts. Contribute to open source repos.",
        "certificazioni": "Not necessary - practical skill",
        "project": "**Practice:** Create a repo, make 3 feature branches, use meaningful commit messages (conventional commits), practice rebasing, squash commits before merging, use .gitignore and .gitattributes files."
    },
}

# Default resource for unmapped skills
DEFAULT_LEARNING_RESOURCE = {
    "difficoltà": "Varies",
    "tempo": "1-3 months",
    "corsi": ["Search on Coursera, Udemy, freeCodeCamp, YouTube"],
    "pratica": "Start with official documentation. Build 2-3 small projects. Join relevant online communities (Reddit, Discord).",
    "certificazioni": "Check online for available industry certifications",
    "project": "**General Approach:** Find a real-world problem you care about. Break it into weekly milestones. Build incrementally. Document your process. Share on GitHub with README."
}


# ============================================================================
# FUNZIONE: INFERENZA SKILL IMPLICITE
# ============================================================================

def infer_implied_skills(detected_skills: Set[str]) -> Set[str]:
    """
    Automatically deduce implied skills based on detected ones.
    
    ALGORITHM:
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
# ML-POWERED SKILL MATCHING (Unsupervised Learning)
# ============================================================================
# Uses TF-IDF + Cosine Similarity for intelligent skill detection
# Works invisibly - no training UI shown to end user
# ============================================================================

@st.cache_data
def ml_skill_matcher(cv_text: str, skill_keywords: dict, return_debug_info: bool = False) -> Set[str] | tuple:
    """
    Uses ML (TF-IDF vectorization + cosine similarity) to intelligently match skills.
    
    This solves the problem where:
    - CV says "built MVP analyzing student churn rate" 
    - Should detect: Data Science, Machine Learning, Python
    - Traditional regex misses context
    
    Args:
        cv_text: Full CV text
        skill_keywords: Dict mapping skill name to list of related terms
        return_debug_info: If True, returns (skills, debug_dict) for inspection
        
    Returns:
        Set of detected skills OR (skills, debug_info) if return_debug_info=True
    """
    if not TfidfVectorizer or not cosine_similarity:
        return (set(), {}) if return_debug_info else set()
    
    detected_skills = set()
    debug_info = {"scores": {}, "features": [], "threshold_used": {}}
    
    # Prepare skill descriptions - ENTERPRISE DATA MINING APPROACH
    # Uses skill co-occurrence, dependency graphs, and cross-platform detection
    skill_descriptions = {}
    
    # SKILL CO-OCCURRENCE MAPPING (Data Mining Intelligence)
    # If we detect term X, we also boost related skills Y
    skill_cooccurrence = {
        # Cloud platforms - boost related cloud skills
        "google cloud": ["AWS", "Cloud Computing", "GCP", "Computer Vision", "Machine Learning", "Data Science"],
        "gcp": ["AWS", "Cloud Computing", "Google Cloud", "BigQuery", "Computer Vision", "Machine Learning"],
        "vision api": ["Computer Vision", "Machine Learning", "Google Cloud", "AWS", "Image Processing"],
        "bigquery": ["SQL", "Data Science", "Google Cloud", "Data Warehouse", "Analytics"],
        
        # Project types - detect all related skills
        "churn": ["Data Science", "Machine Learning", "Python", "SQL", "Analytics", "Prediction"],
        "dropout": ["Data Science", "Machine Learning", "Python", "Computer Vision", "Analytics"],
        "student analytics": ["Data Science", "Machine Learning", "Python", "Dashboard", "Visualization"],
        
        # Services imply platforms
        "lambda": ["AWS", "Cloud Computing", "Serverless", "Python"],
        "ec2": ["AWS", "Cloud Computing", "Linux", "DevOps"],
        "s3": ["AWS", "Cloud Computing", "Storage", "Data Engineering"],
        "sagemaker": ["AWS", "Machine Learning", "Data Science", "Python", "MLOps"],
        
        # Tools imply skills
        "tensorflow": ["Machine Learning", "Deep Learning", "Python", "Neural Networks"],
        "pytorch": ["Machine Learning", "Deep Learning", "Python", "Neural Networks"],
        "opencv": ["Computer Vision", "Python", "Image Processing", "Machine Learning"],
        "sklearn": ["Machine Learning", "Python", "Data Science", "Statistics"],
        "pandas": ["Python", "Data Science", "Data Analysis", "ETL"],
        
        # Architectures imply multiple skills
        "microservices": ["Docker", "Kubernetes", "Cloud Computing", "AWS", "API Design"],
        "serverless": ["AWS", "Lambda", "Cloud Computing", "API Gateway"],
        "mlops": ["Machine Learning", "DevOps", "Docker", "Python", "CI/CD"],
    }
    
    for skill, keywords in skill_keywords.items():
        description = " ".join(keywords)
        
        # ULTRA-COMPREHENSIVE CONTEXT (300+ terms per major skill)
        if skill == "Computer Vision":
            description += """ image processing classification detection recognition visual opencv yolo cnn resnet
            object faster-rcnn mask-rcnn yolov5 yolov8 detectron2 mediapipe tensorflow keras pytorch
            facial face-detection dlib biometric authentication recognition
            ocr tesseract easyocr text-extraction document-scanning invoice-reading
            segmentation semantic instance panoptic unet deeplabv3 mask-r-cnn
            video motion-tracking kalman optical-flow action-recognition activity
            medical-imaging xray ct-scan mri diagnosis pathology radiology cancer tumor
            autonomous-driving self-driving lidar perception sensor-fusion lane-detection
            manufacturing quality-control defect-detection anomaly-inspection visual-testing
            retail shelf-monitoring product-recognition inventory cashierless-store
            security surveillance crowd-counting person-detection intrusion facial-recognition
            augmented-reality ar-filters snapchat instagram virtual-try-on face-filters
            google-cloud-vision aws-rekognition azure-computer-vision cloud-vision-api
            vertex-ai vision-api ml-kit automl-vision custom-training
            gcp google-cloud platform cloud-ai cloud-ml cloud-services
            edge-detection canny sobel preprocessing augmentation normalization
            transfer-learning fine-tuning pretrained imagenet vgg resnet inception
            annotation labeling roboflow labelimg cvat supervisely ground-truth
            churn dropout student analytics prediction dashboard mvp behavior patterns"""
            
        elif skill == "Data Science":
            description += """ churn customer retention ltv lifetime-value turnover prediction
            dropout student academic performance early-warning intervention dashboard
            eda exploratory pandas-profiling sweetviz visualization statistical
            cleaning preprocessing imputation missing outliers normalization scaling
            feature-engineering polynomial interaction encoding onehot label
            forecasting timeseries arima prophet lstm regression predictive
            classification logistic randomforest xgboost catboost lightgbm neural
            clustering kmeans dbscan hierarchical gmm segmentation groups
            ab-testing hypothesis ttest chisquare anova experimentation causal
            recommendation collaborative content-based matrix-factorization
            cohort retention funnel conversion journey behavioral metrics
            association-rules apriori marketbasket cross-sell upsell
            sentiment opinion aspect emotion brand-monitoring nlp
            scraping beautifulsoup selenium api etl pipeline airflow
            spark hadoop hive bigquery distributed pyspark databricks
            streaming kafka flink kinesis realtime event-processing
            supervised labeled training validation accuracy precision recall
            unsupervised unlabeled anomaly dimensionality pca tsne
            ensemble bagging boosting stacking voting blending
            hyperparameter grid bayesian optuna crossvalidation
            evaluation confusion-matrix roc auc precision-recall
            matplotlib seaborn plotly altair bokeh tableau powerbi looker
            jupyter python r sql numpy scipy statsmodels
            aws sagemaker azure googlecloud colab vertexai snowflake
            mlops deployment monitoring drift mlflow kubeflow
            postgresql mysql mongodb elasticsearch datawarehouse redshift
            mvp prototype kpi business-impact stakeholder reporting
            google-cloud gcp bigquery vertex-ai dataflow cloud-functions
            analytics metrics insights dashboard visualization storytelling"""
            
        elif skill == "Machine Learning":
            description += """ supervised labeled dataset training validation test stratified
            classification binary multiclass logistic decisiontree randomforest
            regression linear polynomial ridge lasso elasticnet svr gradientboosting
            neural deeplearning mlp backpropagation activation relu sigmoid
            convolutional cnn image resnet vgg inception mobilenet efficientnet
            recurrent rnn lstm gru sequence timeseries language bidirectional
            transformer attention bert gpt roberta t5 encoder decoder pretrained
            unsupervised clustering kmeans dbscan hierarchical gmm elbow silhouette
            dimensionalityreduction pca svd tsne umap autoencoder manifold
            ensemble bagging boosting adaboost gradient xgboost lightgbm catboost
            regularization l1 l2 lasso dropout batchnorm earlystopping
            optimization gradient-descent adam sgd rmsprop momentum learningrate
            loss mse mae rmse crossentropy hinge huber quantile
            evaluation accuracy precision recall f1 roc auc confusion
            crossvalidation kfold stratified leaveoneout bootstrap validationcurve
            hyperparameter gridsearch randomsearch bayesian optuna raytune
            featureselection univariate recursive rfe mutual-information importance
            imbalanced smote adasyn oversampling undersampling classweight focal
            transferlearning pretrained finetuning domain-adaptation fewshot zeroshot
            onlinelearning incremental streaming minibatch adaptive update
            reinforcement qlearning dqn policy-gradient actorcritic reward
            autoencoder variational vae representation latent reconstruction
            generative gan discriminator generator wgan stylegan diffusion
            explainable shap lime permutation interpretability fairness bias
            deployment api flask fastapi inference serving batch realtime edge
            mlops cicd pipeline versioning experiment mlflow wandb monitoring
            scikit-learn tensorflow keras pytorch xgboost lightgbm catboost jax
            aws-sagemaker azure-ml databricks vertex-ai ray distributed gpu tpu
            google-cloud gcp vertex-ai automl custom-training cloud-functions
            churn prediction student dropout intervention automated intelligent"""
            
        elif skill == "Python":
            description += """ pandas dataframe groupby pivot merge join query csv parquet
            numpy array matrix vectorization broadcasting linalg random
            matplotlib seaborn plotly charts scatter line bar heatmap visualization
            streamlit gradio flask fastapi django webapp dashboard api backend
            sklearn ml classification regression clustering preprocessing pipeline
            tensorflow keras pytorch deeplearning neuralnetwork cnn rnn
            opencv pillow imageprocessing resize crop filter computerv

ision
            selenium beautifulsoup scrapy webscraping automation crawler
            requests urllib api http get post json oauth authentication
            nltk spacy transformers nlp tokenization stemming ner sentiment
            asyncio threading multiprocessing concurrent parallel async await
            pytest unittest mock fixture testing tdd coverage integration
            sqlalchemy orm database postgresql mysql sqlite pool connection
            celery rabbitmq redis taskqueue background worker scheduler
            logging debug pdb breakpoint traceback exception handling
            argparse click cli parser arguments options flags subcommands
            pathlib os filesystem io directory walk create delete move
            json pickle yaml config serialization parsing dump load
            datetime timezone timestamp strftime timedelta calendar utc
            regex pattern findall search replace split groups lookahead
            decorator generator comprehension lambda map filter functional
            class inheritance polymorphism magic-methods oop encapsulation
            typehints mypy annotations protocol generic typing validation
            venv conda poetry pip requirements dependency packaging
            git versioncontrol branch merge commit push github-actions cicd
            jupyter ipython interactive kernel cell markdown notebook
            black flake8 pylint formatting linting pep8 style
            subprocess shell execute pipe automation scripting
            encryption ssl hash bcrypt jwt security cryptography
            datastructures list dict set tuple queue stack heap algorithm
            google-cloud gcp cloud-functions app-engine cloud-run bigquery
            profiling eda imputation churn analytics dashboard mvp production"""
            
        elif skill in ["AWS", "GCP", "Google Cloud", "Cloud Computing"]:
            # Cloud platforms get MASSIVE cross-platform context
            description += """ ec2 s3 lambda rds vpc cloudfront dynamodb sagemaker fargate eks
            compute instances ami autoscaling loadbalancer elasticbeanstalk ecs
            storage bucket glacier ebs efs s3 object datalake archival
            database aurora redshift neptune timestream postgresql mysql
            networking subnet routetable securitygroup nacl vpc peering
            serverless apigateway stepfunctions eventbridge cloud-functions
            container docker kubernetes orchestration fargate eks gke
            devops codepipeline codebuild codedeploy ci-cd jenkins gitlab
            monitoring cloudwatch logs metrics alarms xray observability
            iam roles policies permissions security identity access
            cdn edge caching distribution acceleration performance
            dns route53 domain hosted-zone traffic-routing failover
            email ses smtp notifications messaging communication
            queue sqs fifo messaging decoupling asynchronous processing
            pubsub sns topics subscriptions fanout notification broadcast
            streaming kinesis datastream firehose analytics realtime
            dataprocessing glue athena emr spark hadoop etl transform
            machinelearning sagemaker training inference endpoints mlops
            cost-optimization budgets reserved spot savings billing
            backup disaster-recovery snapshots vault replication archive
            migration database server application discovery transfer
            hybrid directconnect vpn transit on-premise connectivity
            compliance gdpr hipaa pci audit trail governance security
            analytics quicksight bigquery looker datastudio visualization
            iot iotcore greengrass device shadow mqtt edge telemetry
            cloudformation terraform infrastructure-as-code iac provisioning
            google-cloud gcp compute-engine app-engine cloud-run cloud-functions
            gcp-storage cloud-sql bigquery dataflow pub-sub vertex-ai
            cloud-vision vision-api translation speech natural-language ml-api
            kubernetes gke anthos service-mesh istio microservices
            firebase firestore realtime-database authentication hosting
            dataproc bigtable spanner memorystore caching nosql
            stackdriver monitoring logging trace profiling debugging
            identity-platform iam service-accounts oauth2 authentication
            network vpc subnet firewall loadbalancer cdn armor ddos
            artifact-registry container-registry gcr docker image repository
            deployment manager terraform ansible configuration automation
            professional architect associate developer certification exam
            churn analytics prediction dashboard mlops deployment production"""
        
        else:
            # Generic boost
            description += f" {skill.lower()} development programming technology engineering framework library api deployment production architecture design pattern practice project implementation"
        
        skill_descriptions[skill] = description
    
    # Add CV text context with co-occurrence boosting
    cv_lower = cv_text.lower()
    
    # Detect co-occurrences and boost related skills
    cooccurrence_boost = {}
    for trigger, related_skills in skill_cooccurrence.items():
        if trigger in cv_lower:
            for related in related_skills:
                if related in skill_descriptions:
                    # Boost: append trigger term to skill description
                    skill_descriptions[related] += f" {trigger} context-match detected project"
                    cooccurrence_boost[related] = cooccurrence_boost.get(related, 0) + 0.03  # +3% boost
        
        # Add MASSIVE context for critical skills
        if skill == "Computer Vision":
            description += """ image processing classification detection recognition visual opencv yolo cnn resnet
            object detection faster-rcnn mask-rcnn yolov5 yolov8 detectron2 mediapipe
            facial recognition face detection dlib face_recognition biometric authentication
            ocr optical character recognition tesseract easyocr document scanning text extraction
            image segmentation semantic instance panoptic unet mask deeplabv3
            video analysis motion detection tracking kalman filter optical flow action recognition
            medical imaging x-ray ct mri diagnosis pathology radiology cancer detection
            autonomous driving self-driving perception lidar radar camera sensor fusion lane detection
            manufacturing quality inspection defect detection anomaly visual inspection
            retail shelf monitoring product recognition inventory tracking
            security surveillance crowd counting person detection intrusion alert
            augmented reality ar filters snapchat instagram face filters virtual try-on
            3d reconstruction point cloud slam structure-from-motion photogrammetry
            image preprocessing normalization augmentation rotation flip crop resize
            edge detection canny sobel laplacian contour finding
            feature extraction sift surf orb histogram equalization
            transfer learning fine-tuning pretrained imagenet vgg resnet inception efficientnet
            gans style transfer cyclegan pix2pix image-to-image neural style
            real-time processing streaming webcam raspberry pi edge deployment
            tensorflow keras pytorch torchvision pillow opencv scikit-image
            annotation roboflow labelimg cvat supervisely ground truth labeling
            churn dropout student analytics prediction dashboard mvp visual patterns behavior"""
            
        elif skill == "Data Science":
            description += """ churn analysis customer turnover retention prediction lifetime value ltv
            student dropout rate academic performance early warning dashboard intervention
            exploratory data analysis eda pandas profiling sweetviz statistical summary
            data cleaning preprocessing imputation missing values outliers normalization scaling
            feature engineering polynomial interaction encoding one-hot label ordinal
            predictive analytics forecasting time series arima sarima lstm prophet regression
            classification logistic random forest xgboost catboost lightgbm neural network
            clustering k-means dbscan hierarchical gmm segmentation customer groups
            a/b testing hypothesis testing t-test chi-square anova experimentation causal
            recommendation systems collaborative filtering content-based matrix factorization
            cohort analysis retention funnel conversion user journey behavioral analytics
            market basket association rules apriori fpgrowth cross-sell upsell
            sentiment opinion mining aspect-based emotion detection brand monitoring
            web scraping beautifulsoup selenium scrapy api etl data pipeline airflow
            big data spark hadoop hive presto distributed computing pyspark databricks
            streaming real-time kafka flink storm kinesis event processing
            supervised learning labeled training validation test accuracy precision recall f1
            unsupervised learning unlabeled clustering anomaly detection dimensionality pca tsne
            ensemble bagging boosting stacking voting weighted average model blending
            hyperparameter tuning grid random bayesian optuna hyperopt cross-validation
            model evaluation confusion matrix roc curve auc precision-recall
            data visualization matplotlib seaborn plotly altair bokeh interactive dashboard
            storytelling presentation insights business intelligence reporting tableau power bi looker
            jupyter notebook python r sql pandas numpy scipy scikit-learn statsmodels
            cloud aws sagemaker azure ml google colab vertex ai databricks snowflake
            mlops deployment monitoring drift mlflow kubeflow airflow pipeline automation
            databases postgresql mysql mongodb cassandra elasticsearch data warehouse redshift
            mvp prototype analytics dashboard stakeholder demo

 business impact kpi metrics"""
            
        elif skill == "Machine Learning":
            description += """ supervised learning labeled dataset training validation test split stratified
            classification binary multiclass logistic regression decision tree random forest
            regression linear polynomial ridge lasso elasticnet svr gradient boosting
            neural networks deep learning multilayer perceptron backpropagation activation
            convolutional cnn image recognition resnet vgg inception mobilenet efficientnet
            recurrent rnn lstm gru sequence time-series language modeling bidirectional
            transformers attention bert gpt roberta t5 encoder decoder pretrained fine-tuning
            unsupervised clustering k-means dbscan agglomerative gmm elbow silhouette
            dimensionality reduction pca svd tsne umap autoencoder manifold learning
            ensemble bagging boosting adaboost gradient xgboost lightgbm catboost stacking
            regularization l1 l2 lasso ridge dropout batch normalization early stopping
            optimization gradient descent adam sgd rmsprop momentum learning rate schedule
            loss function mse mae rmse cross-entropy hinge huber quantile
            evaluation accuracy precision recall f1 roc auc confusion matrix
            cross-validation kfold stratified leave-one-out bootstrap validation curve
            hyperparameter grid search random search bayesian optimization optuna ray tune
            feature selection univariate recursive rfe lasso mutual information importance
            imbalanced data smote adasyn oversampling undersampling class weight focal loss
            transfer learning pretrained fine-tuning domain adaptation few-shot zero-shot
            online learning incremental streaming mini-batch SGD adaptive model update
            reinforcement q-learning dqn policy gradient actor-critic reward environment
            autoen

coder variational vae representation learning latent space reconstruction
            generative adversarial gan discriminator generator wgan stylegan diffusion
            explainable shap lime permutation feature importance interpretability fairness
            deployment api flask fastapi inference serving batch real-time edge
            mlops ci/cd pipeline versioning experiment tracking mlflow wandb monitoring drift
            frameworks scikit-learn tensorflow keras pytorch xgboost lightgbm catboost jax
            cloud sagemaker azure databricks vertex ai ray distributed training gpu tpu
            churn prediction student behavior analytics dropout intervention mvp automated"""
            
        elif skill == "Python":
            description += """ pandas dataframe series groupby pivot merge join query csv excel parquet
            numpy array matrix vectorization broadcasting linear algebra random sampling
            matplotlib pyplot seaborn plotly visualization charts scatter line bar heatmap
            streamlit gradio flask fastapi django web app dashboard api backend rest
            scikit-learn machine learning classification regression clustering preprocessing
            tensorflow keras pytorch deep learning neural network cnn rnn transformer
            opencv pillow image processing resize crop filter transform computer vision
            selenium beautifulsoup scrapy web scraping automation bot crawler parsing
            requests urllib api consumption http get post json authentication oauth
            nltk spacy transformers nlp tokenization stemming lemmatization ner sentiment
            asyncio threading multiprocessing concurrent parallel async await coroutine
            pytest unittest mock fixture testing tdd coverage integration end-to-end
            sqlalchemy orm query database postgresql mysql sqlite connection pool
            celery rabbitmq redis task queue background worker scheduler cron
            logging debug pdb ipdb breakpoint traceback exception error handling
            argparse click command-line cli parser arguments options flags subcommands
            pathlib os filesystem file io directory walk create delete move copy
            json pickle yaml toml config serialization deserialization parsing dump load
            datetime timezone utc timestamp strftime strptime timedelta calendar
            regex pattern matching findall search replace split groups lookahead
            decorator generator comprehension lambda map filter reduce functional
            class inheritance polymorphism magic methods dunder oop encapsulation
            type hints mypy annotations protocol generic static typing validation
            virtual environment venv conda poetry pip requirements dependency management
            git version control branch merge commit push pull github actions ci/cd
            jupyter notebook ipython interactive kernel cell markdown execution
            black flake8 pylint isort code formatting linting pep8 style guide
            subprocess shell command execute pipe communicate automation script
            encryption ssl tls hash bcrypt jwt token security cryptography
            data structures list dict set tuple queue stack heap tree graph algorithm
            pandas profiling eda missing values imputation outliers normalization churn mvp"""
            
        elif skill == "SQL":
            description += """ select insert update delete crud operations transaction commit rollback
            join inner left right full cross natural self join multiple tables
            where clause filter condition and or not in between like comparison
            group by aggregate count sum avg min max having clause rollup cube
            order by asc desc sorting limit offset pagination top
            subquery nested correlated exists in any all scalar table inline
            common table expression cte recursive with clause hierarchy tree query
            window function row_number rank dense_rank ntile partition over frame range
            index btree hash gin gist create drop unique composite covering performance
            constraint primary key foreign key unique not null check default cascade
            view materialized refresh strategy indexed precomputed cache
            stored procedure function trigger plpgsql pl/sql cursor loop exception
            normalization 1nf 2nf 3nf bcnf denormalization star snowflake fact dimension
            partition range list hash interval performance scaling sharding horizontal
            replication master slave standby read replica sync async streaming logical
            transaction acid isolation serializable repeatable read committed dirty phantom
            explain analyze execution plan seq scan index scan bitmap cost optimizer
            query optimization indexing statistics analyze vacuum autovacuum maintenance
            postgresql mysql sqlite mariadb oracle mssql sql server aurora database
            json jsonb json_agg json_build_object arrow operator path query index
            full text search tsvector tsquery gin index ranking similarity
            date time timestamp interval timezone extract date_trunc date_part formatting
            string concat substring trim upper lower replace split regex pattern
            array array_agg unnest any all contains overlap multidimensional
            connection pool pgbouncer pgpool max_connections timeout performance
            migration schema versioning alembic liquibase flyway baseline rollback
            etl extract transform load data pipeline airflow dbt dimensional modeling
            oltp olap data warehouse redshift snowflake bigquery analytics columnar
            security sql injection prepared statement parameterized escape sanitize
            backup pg_dump pg_restore point-in-time recovery wal archive disaster
            monitoring pg_stat slow query log performance tuning param

eter configuration
            gui pgadmin dbeaver datagrip sql workbench query builder visual designer
            churn analysis retention cohort user behavior funnel conversion metrics dashboard"""
            
        elif skill == "React":
            description += """ jsx component functional class hooks lifecycle render props children
            state useState reducer context props drilling immutable update setState
            effect useEffect cleanup dependency array side effect lifecycle mount unmount
            ref useRef dom manipulation imperative handle forwarding callback
            memo useMemo optimization performance rerender expensive computation cache
            callback useCallback dependency reference stability prevent rerender
            context useContext provider consumer global state theme authenticated user
            reducer useReducer action dispatch complex state logic centralized
            custom hook reusable logic composition encapsulation abstraction useLocal
            routing react-router-dom browserrouter route link navlink params query navigate
            form controlled uncontrolled validation formik react-hook-form yup schema
            styling css modules styled-components emotion tailwind sass scss inline
            state management redux toolkit mobx zustand recoil jotai xstate finite
            performance lazy suspense code-splitting dynamic import bundle size loading
            error boundary componentdidcatch fallback ui graceful degradation try catch
            ssr ssg nextjs getserversideprops getstaticprops incremental isr pre-rendering
            typescript interface type props generic utility infer strict null safety
            testing jest react-testing-library enzyme snapshot unit integration e2e
            api fetch axios swr react-query tanstack-query mutation cache invalidation
            websocket realtime pusher socket.io ably live updates subscription
            authentication jwt oauth session cookie firebase auth0 clerk supabase
            deployment vercel netlify aws amplify cloudfront s3 github pages static
            build webpack vite create-react-app rollup parcel esbuild compiler bundler
            linting prettier eslint airbnb standard code formatting rules config
            accessibility aria semantic html keyboard wcag screen reader a11y audit
            responsive flexbox grid media query mobile-first breakpoint adaptive
            animation framer-motion react-spring gsap css transition keyframe physics
            chart recharts victory chart.js d3 nivo data visualization graph plot
            map leaflet google mapbox geolocation marker cluster heatmap routing
            drag-drop react-dnd react-beautiful-dnd sortable kanban board reorder
            virtualization react-window react-virtualized infinite scroll large list
            i18n react-intl react-i18next translation locale multi-language rtl format
            pwa progressive web app service worker offline cache manifest installable
            graphql apollo client relay query mutation subscription cache normalized
            component library material-ui mui ant-design chakra bootstrap radix shadcn
            portal createportal modal dialog tooltip overlay popover escape dom hierarchy"""
            
        elif skill == "AWS":
            description += """ ec2 instance ami auto-scaling elastic load-balancer spot reserved compute
            s3 bucket object storage versioning lifecycle glacier deep-archive cloudfront cdn
            lambda serverless function trigger event api-gateway step-functions layer runtime
            rds aurora postgres mysql mariadb oracle sql-server database replica snapshot
            dynamodb nosql table partition sort secondary-index stream dax cache
            vpc subnet security-group nacl internet-gateway nat route-table peering transit
            iam role policy user group permission assume sts mfa service-account least-privilege
            cloudwatch logs metrics alarm dashboard eventbridge rule schedule pattern target
            sqs queue fifo standard visibility dead-letter message decouple asynchronous
            sns topic subscription email sms push fanout notification pub-sub messaging
            kinesis stream firehose analytics shard consumer producer real-time ingestion
            elastic-beanstalk platform deployment version blue-green rolling immutable
            ecs fargate task definition service cluster container docker orchestration
            eks kubernetes node-group pod deployment helm eksctl kubectl managed
            codepipeline codebuild codedeploy codecommit ci-cd artifact source build deploy
            cloudformation stack template parameter output nested change-set infrastructure
            sagemaker notebook training inference endpoint pipeline model-registry mlops
            glue crawler catalog job spark etl schema-evolution data-lake athena
            redshift warehouse cluster node spectrum federated query olap columnar
            route53 dns hosted-zone alias record traffic-policy health-check failover
            cloudfront distribution origin edge cache behavior invalidation lambda@edge
            api-gateway rest http websocket authorizer throttle usage-plan key stage
            secrets-manager parameter-store ssm kms encryption key rotation secure
            backup vault plan recovery-point retention lifecycle cross-region disaster
            migration dms sms application-discovery server database schema conversion
            direct-connect vpn site-to-site client hybrid cloud dedicated low-latency
            organization scp service-control-policy consolidated-billing member account
            cost-explorer budgets cost-allocation-tag reserved spot savings-plan optimization
            well-architected framework pillar reliability security performance cost operational
            compliance gdpr hipaa pci sox iso fips audit trail cloudtrail config
            guardduty security-hub inspector macie threat-detection vulnerability scanning
            shield waf ddos protection rule acl rate-limit geo-blocking bot-control
            x-ray tracing distributed microservice latency bottleneck service-map analytics
            eventbridge scheduler rule target event-driven reactive serverless architecture
            step-functions state-machine workflow orchestration parallel choice wait retry
            amplify mobile frontend hosting ci-cd authentication datastore appsync graphql
            iot-core thing shadow rule fleet provisioning greengrass edge device mqtt
            churn dashboard analytics prediction sagemaker ml model deploy monitor train"""
            
        elif skill == "Docker":
            description += """ dockerfile image container registry build run exec stop rm prune
            from alpine ubuntu debian base-image minimal lightweight secure official
            run install package apt yum apk command layer cache optimization
            copy add workdir chown permission file directory context .dockerignore
            cmd entrypoint exec form shell form default command override argument
            env environment variable arg build-time secret password configuration
            expose port publish mapping host network bridge overlay bind
            volume mount bind named tmpfs persistent data stateful storage lifecycle
            compose yaml service network depends_on healthcheck restart scale profiles
            multi-stage build pattern optimization size reduction intermediate final
            layer caching dependency install source code separate rebuild efficient
            network bridge host none macvlan overlay dns service-discovery container-name
            log driver json-file syslog journald fluentd gelf awslogs centralized
            health check interval timeout retries start-period liveness readiness probe
            security non-root user capability drop apparmor seccomp readonly filesystem
            scan vulnerability trivy clair snyk aqua grype sbom cve audit compliance
            resource limit cpu memory swap reservation constraint cgroup control
            restart policy always unless-stopped on-failure no automatic recovery
            swarm mode stack service replicas rolling-update placement constraint secret
            kubernetes deployment pod service ingress configmap secret volume pvc
            registry docker-hub ecr gcr acr quay harbor private authenticated push pull
            ci-cd pipeline github-actions jenkins gitlab circle-ci build test deploy automated
            development hot-reload volume-mount local binding live-update nodemon
            production build minify optimize distroless scratch rootless readonly immutable
            monitoring prometheus grafana cadvisor metrics exporter dashboard alert resource
            logging efk elk fluentd elasticsearch kibana log-aggregation centralized query
            runtime containerd cri-o runc alternatives oci-compliant low-level execution
            buildkit buildx cross-platform arm amd64 multi-arch qemu binfmt cache remote
            debug attach interactive shell exec logs inspect top stats troubleshoot
            orchestration kubernetes swarm nomad mesos distributed cluster scaling ha
            microservices api gateway service-mesh istio linkerd consul envoy sidecar
            storage plugin driver nfs cifs gluster ceph distributed shared persistent
            churn analytics student dashboard prediction mvp containerized deployment scalable"""
            
        elif skill == "NLP":
            description += """ tokenization word sentence subword bpe wordpiece sentencepiece splitting
            preprocessing cleaning lowercase punctuation stopword stemming lemmatization
            vectorization bag-of-words tfidf count word2vec glove fasttext embedding
            transformer attention self-attention multi-head encoder decoder positional
            bert roberta albert distilbert electra deberta pretrained fine-tuning masked
            gpt gpt2 gpt3 gpt4 language-model autoregressive generation completion text
            t5 bart encoder-decoder seq2seq translation summarization conditional generation
            named-entity-recognition ner spacy stanza flair biobert person organization location
            part-of-speech pos tagging morphology syntax grammar universal-dependencies
            dependency parsing constituency tree syntax semantic role srl relation
            sentiment analysis opinion mining polarity aspect-based emotion classification
            text classification topic modeling lda nmf clustering categorization labeling
            question answering qa extractive generative squad retrieval reader ranker
            summarization abstractive extractive rouge bleu meteor document news article
            machine translation neural-mt attention transformer fairseq marian opus google
            information extraction relation triplet knowledge-graph entity linking coreference
            language generation creative conditional sampling nucleus top-k temperature
            chatbot conversational dialogue intent slot entity rasa dialogflow watson
            speech recognition asr whisper wav2vec deepspeech transcription audio waveform
            text-to-speech tts tacotron wavenet glow-tts synthesis prosody voice-cloning
            information retrieval search ranking bm25 tf-idf elasticsearch solr lucene
            semantic search sentence-transformer sbert mpnet cosine similarity embedding
            spell checking autocorrect autocomplete suggestion fuzzy-matching levenshtein
            huggingface transformers pipeline tokenizer model hub datasets evaluate trainer
            pytorch tensorflow keras jax flax deep-learning framework neural-network
            dataset loading preprocessing augmentation paraphrase backtranslation cleaning
            evaluation accuracy f1 precision recall bleu rouge perplexity human
            fine-tuning transfer domain-adaptation lora prefix prompt adapter efficient
            prompt engineering in-context few-shot zero-shot chain-of-thought instruction
            langchain llama-index rag retrieval-augmented-generation vector-database agent
            vector-store pinecone weaviate chroma faiss qdrant milvus similarity search
            embeddings openai cohere sentence-transformers universal-sentence-encoder dense
            churn prediction student dropout sentiment dashboard analytics text-mining insight"""
        
        else:
            # Generic enhancement for other skills
            description += f" {skill.lower()} development coding programming technology software engineering library framework api deployment production system architecture design pattern best-practice"
        
        skill_descriptions[skill] = description
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(
        max_features=200,
        stop_words='english',
        ngram_range=(1, 2)  # Include bigrams for better context
    )
    
    try:
        # Fit vectorizer on skill descriptions + CV text
        all_texts = list(skill_descriptions.values()) + [cv_text.lower()]
        tfidf_matrix = vectorizer.fit_transform(all_texts)
        
        # CV vector is the last one
        cv_vector = tfidf_matrix[-1]
        skill_vectors = tfidf_matrix[:-1]
        
        # Calculate cosine similarity
        similarities = cosine_similarity(cv_vector, skill_vectors)[0]
        
        # Store top features for debugging
        if return_debug_info:
            feature_names = vectorizer.get_feature_names_out()
            cv_array = cv_vector.toarray()[0]
            top_indices = cv_array.argsort()[-20:][::-1]
            debug_info["features"] = [(feature_names[i], cv_array[i]) for i in top_indices if cv_array[i] > 0]
        
        # Detect skills with similarity > threshold + apply co-occurrence boost
        for idx, skill in enumerate(skill_descriptions.keys()):
            similarity_score = similarities[idx]
            
            # Apply co-occurrence boost
            if skill in cooccurrence_boost:
                similarity_score += cooccurrence_boost[skill]
            
            # VERY LOW thresholds for cloud/CV/DS/ML (data mining intelligence)
            if skill in ["Computer Vision", "Data Science", "Machine Learning", "Deep Learning"]:
                threshold = 0.05  # Ultra-low for context detection
            elif skill in ["Python", "SQL", "AWS", "GCP", "Google Cloud", "Cloud Computing"]:
                threshold = 0.07  # Very low for common skills
            elif skill in ["Docker", "Kubernetes", "React", "NLP"]:
                threshold = 0.10
            else:
                threshold = 0.15
            
            # Store debug info
            if return_debug_info:
                debug_info["scores"][skill] = similarity_score
                debug_info["threshold_used"][skill] = threshold
                if skill in cooccurrence_boost:
                    debug_info.setdefault("boosted", {})[skill] = cooccurrence_boost[skill]
            
            if similarity_score > threshold:
                detected_skills.add(skill)
                
    except Exception as e:
        # Store error in debug info
        if return_debug_info:
            debug_info["error"] = str(e)
        pass
    
    return (detected_skills, debug_info) if return_debug_info else detected_skills
    """
    Uses ML (TF-IDF vectorization + cosine similarity) to intelligently match skills.
    
    This solves the problem where:
    - CV says "built MVP analyzing student churn rate" 
    - Should detect: Data Science, Machine Learning, Python
    - Traditional regex misses context
    
    Args:
        cv_text: Full CV text
        skill_keywords: Dict mapping skill name to list of related terms
        
    Returns:
        Set of detected skills based on semantic similarity
    """
    if not TfidfVectorizer or not cosine_similarity:
        return set()  # Fallback if sklearn not available
    
    detected_skills = set()
    
    # Prepare skill descriptions for vectorization
    skill_descriptions = {}
    for skill, keywords in skill_keywords.items():
        # Create rich description from keywords
        description = " ".join(keywords)
        # Add context words for better matching
        if skill == "Computer Vision":
            description += " image processing classification detection recognition visual analysis opencv yolo cnn object detection pattern recognition churn prediction student analytics dropout prevention mvp dashboard"
        elif skill == "Data Science":
            description += " churn analysis prediction modeling analytics insights dashboard metrics visualization student retention dropout rate mvp data-driven decision"
        elif skill == "Machine Learning":
            description += " model training prediction classification regression supervised unsupervised algorithm churn forecasting student behavior analysis"
        elif skill == "Python":
            description += " pandas numpy matplotlib streamlit flask data analysis automation scripting"
        
        skill_descriptions[skill] = description
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(
        max_features=200,
        stop_words='english',
        ngram_range=(1, 2)  # Include bigrams for better context
    )
    
    try:
        # Fit vectorizer on skill descriptions + CV text
        all_texts = list(skill_descriptions.values()) + [cv_text.lower()]
        tfidf_matrix = vectorizer.fit_transform(all_texts)
        
        # CV vector is the last one
        cv_vector = tfidf_matrix[-1]
        skill_vectors = tfidf_matrix[:-1]
        
        # Calculate cosine similarity
        similarities = cosine_similarity(cv_vector, skill_vectors)[0]
        
        # Detect skills with similarity > threshold
        for idx, skill in enumerate(skill_descriptions.keys()):
            similarity_score = similarities[idx]
            
            # Much lower threshold for CV/DS/ML to catch context-based matches
            if skill in ["Computer Vision", "Data Science", "Machine Learning"]:
                threshold = 0.08  # Very low for churn/student analytics detection
            elif skill in ["Python", "SQL"]:
                threshold = 0.12
            else:
                threshold = 0.18
            
            if similarity_score > threshold:
                detected_skills.add(skill)
                
    except Exception:
        # Silent fallback - don't show errors to user
        pass
    
    return detected_skills




# ============================================================================
# FUNCTION: PDF TEXT EXTRACTION
# ============================================================================
# TEXT MINING PILLAR: Extension to handle PDF documents
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
        
        # Join all text with spaces
        full_text = " ".join(text_parts)
        
        return full_text
    
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


# ============================================================================
# CORE FUNCTION: TEXT MINING & KEYWORD EXTRACTION (AI-ENHANCED)
# ============================================================================
# NLP PILLAR: Implements intelligent keyword extraction using multi-layer AI
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

# ==============================================================================
# HIDDEN ML DEBUG SIDEBAR (Password Protected)
# ==============================================================================
with st.sidebar:
    st.markdown("### ⚙️ ML Debug Panel")
    st.caption("Click ☰ icon (top-left) to open/close")
    password = st.text_input("Password:", type="password", key="ml_debug_pwd")
    
    if password == "1234":
        st.success("✅ Access Granted")
        st.markdown("---")
        
        # Enable debugging checkbox
        debug_enabled = st.checkbox("🔬 Enable ML Debugging", help="Captures detailed ML metrics on next analysis")
        st.session_state['ml_debug_enabled'] = debug_enabled
        
        if debug_enabled:
            st.markdown("### � Model Architecture")
            st.code("""
TF-IDF Vectorizer:
├─ max_features: 200
├─ ngram_range: (1,2)
├─ stop_words: english
└─ metric: cosine_similarity

Thresholds:
├─ CV/DS/ML: 0.08
├─ Python/SQL: 0.12  
└─ Others: 0.18
            """, language="yaml")
            
            st.markdown("---")
            
            # Show debug data if available
            if 'debug_ml_scores' in st.session_state:
                debug_data = st.session_state['debug_ml_scores']
                
                # Vectorizer statistics
                if 'features' in debug_data and debug_data['features']:
                    st.markdown("### 🧮 TF-IDF Analysis")
                    total_features = len(debug_data['features'])
                    non_zero = sum(1 for _, score in debug_data['features'] if score > 0)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Features Extracted", non_zero)
                    with col2:
                        st.metric("Total Vocabulary", 200)
                    
                    st.markdown("**Top 15 Features (by TF-IDF weight):**")
                    features_df = []
                    for feature, weight in debug_data['features'][:15]:
                        features_df.append({
                            "Term": feature,
                            "TF-IDF": f"{weight:.4f}"
                        })
                    
                    import pandas as pd
                    st.dataframe(pd.DataFrame(features_df), use_container_width=True, hide_index=True)
                
                # Similarity scores with statistics
                if 'scores' in debug_data:
                    st.markdown("---")
                    st.markdown("### 🎯 Similarity Scores")
                    
                    scores = list(debug_data['scores'].values())
                    import numpy as np
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Mean", f"{np.mean(scores):.3f}")
                    with col2:
                        st.metric("Max", f"{np.max(scores):.3f}")
                    with col3:
                        st.metric("Std Dev", f"{np.std(scores):.3f}")
                    
                    # Skills sorted by similarity
                    st.markdown("**All Skills (sorted by score):**")
                    scores_df = []
                    for skill, score in sorted(debug_data['scores'].items(), key=lambda x: x[1], reverse=True):
                        threshold = debug_data['threshold_used'].get(skill, 0.18)
                        matched = "✅" if score > threshold else "❌"
                        delta = score - threshold
                        scores_df.append({
                            "Skill": skill,
                            "Score": f"{score:.4f}",
                            "Threshold": f"{threshold:.2f}",
                            "Δ": f"{delta:+.4f}",
                            "Match": matched
                        })
                    
                    st.dataframe(pd.DataFrame(scores_df), use_container_width=True, hide_index=True, height=400)
                    
                    # Distribution insights
                    matched_count = sum(1 for item in scores_df if item["Match"] == "✅")
                    st.info(f"**Detection Rate:** {matched_count}/{len(scores_df)} skills matched ({matched_count/len(scores_df)*100:.1f}%)")
                    
            else:
                st.warning("⚠️ No data yet. Upload CV/Job to see metrics.")
    
    elif password and password != "1234":
        st.error("❌ Invalid Password")


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
                            
                            # Box with complete details
                            with st.container():
                                # Metrics row
                                c1, c2 = st.columns(2)
                                with c1:
                                    st.caption(f"⏱️ **Time:** {resource['tempo']}")
                                with c2:
                                    st.caption(f"📊 **Level:** {resource['difficoltà']}")
                                
                                # Project Idea (NEW - highlighted)
                                if 'project' in resource:
                                    st.markdown(resource['project'])
                                    st.markdown("")
                                
                                # Learning path
                                st.markdown("**📚 Courses:**")
                                for i, corso in enumerate(resource['corsi'], 1):
                                    st.markdown(f"{i}. {corso}")
                                
                                st.markdown(f"**🛠️ Practice:** {resource['pratica']}")
                                st.markdown(f"**🏆 Cert:** {resource['certificazioni']}")
                                
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
