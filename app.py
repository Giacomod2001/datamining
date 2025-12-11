"""
Job Seeker Helper - CV vs Job Description Skill Gap Analyzer
Uses ML (TF-IDF + Cosine Similarity) for intelligent skill detection.
"""

import streamlit as st
import re
from typing import Set, Dict, List

# ML imports
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None
    np = None

# PDF extraction
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Job Seeker Helper",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# SKILL GROUPS DATABASE
# =============================================================================
SKILL_GROUPS = {
    # Programming Languages
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6"],
    "C++": ["c++", "cpp", "c plus plus"],
    "C#": ["c#", "csharp", "c sharp", ".net", "dotnet", "asp.net"],
    "Go": ["go", "golang"],
    "Rust": ["rust", "rustlang"],
    "R": ["r language", "r programming", "rstudio", "tidyverse"],
    
    # Data Science & ML
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural network", "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn"],
    "Data Science": ["data science", "data scientist", "data analysis", "analytics", "statistical analysis"],
    "Computer Vision": ["computer vision", "cv", "image processing", "opencv", "yolo", "object detection", "image recognition"],
    "NLP": ["nlp", "natural language processing", "text mining", "sentiment analysis", "transformers", "bert", "gpt"],
    "Deep Learning": ["deep learning", "neural network", "cnn", "rnn", "lstm", "transformer"],
    
    # Databases
    "SQL": ["sql", "mysql", "postgresql", "postgres", "sqlite", "oracle", "sql server", "tsql", "plsql"],
    "MongoDB": ["mongodb", "mongo", "nosql"],
    "Redis": ["redis", "caching"],
    "BigQuery": ["bigquery", "big query", "bq"],
    
    # Cloud
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda", "dynamodb", "sagemaker", "cloudformation"],
    "GCP": ["gcp", "google cloud", "google cloud platform", "vertex ai", "cloud functions", "cloud run"],
    "Azure": ["azure", "microsoft azure", "azure devops", "azure ml"],
    "Cloud Computing": ["cloud", "cloud computing", "serverless", "iaas", "paas", "saas"],
    
    # DevOps
    "Docker": ["docker", "container", "containerization", "dockerfile"],
    "Kubernetes": ["kubernetes", "k8s", "helm", "kubectl", "container orchestration"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "continuous deployment", "jenkins", "github actions", "gitlab ci"],
    "Terraform": ["terraform", "infrastructure as code", "iac"],
    
    # Frontend
    "React": ["react", "reactjs", "react.js", "redux", "next.js", "nextjs"],
    "Vue": ["vue", "vuejs", "vue.js", "nuxt"],
    "Angular": ["angular", "angularjs"],
    "HTML/CSS": ["html", "css", "html5", "css3", "sass", "scss", "tailwind", "bootstrap"],
    
    # BI & Visualization
    "Tableau": ["tableau", "tableau desktop", "tableau server"],
    "Power BI": ["power bi", "powerbi", "dax"],
    "Looker": ["looker", "looker studio", "data studio"],
    "Excel": ["excel", "spreadsheet", "vlookup", "pivot table", "macros", "vba"],
    
    # Soft Skills
    "Agile": ["agile", "scrum", "kanban", "sprint", "jira"],
    "Leadership": ["leadership", "team lead", "management", "mentoring"],
    "Communication": ["communication", "presentation", "stakeholder", "collaboration"],
    "Problem Solving": ["problem solving", "analytical", "critical thinking"],
    
    # Testing
    "Testing": ["testing", "unit test", "pytest", "jest", "selenium", "qa", "quality assurance"],
    "Git": ["git", "github", "gitlab", "version control", "bitbucket"],
}

# =============================================================================
# LEARNING RESOURCES DATABASE (Skill-Specific!)
# =============================================================================
LEARNING_RESOURCES = {
    "Python": {
        "level": "Medium",
        "time": "2-3 months",
        "courses": ["Python for Everybody (Coursera)", "Complete Python Bootcamp (Udemy)", "Official Python Docs"],
        "practice": "Build a data dashboard with Pandas + Streamlit. Create a web scraper. Automate daily tasks.",
        "cert": "PCAP (Python Institute)",
        "project": "Personal Finance Tracker - Pandas for data, Matplotlib for viz, SQLite for storage"
    },
    "Java": {
        "level": "Medium-High",
        "time": "3-4 months",
        "courses": ["Java MOOC (University of Helsinki)", "Oracle Java Tutorials"],
        "practice": "Build REST API with Spring Boot. Implement CRUD with database.",
        "cert": "Oracle Certified Associate",
        "project": "Employee Management System - Spring Boot + MySQL + REST API"
    },
    "JavaScript": {
        "level": "Medium",
        "time": "2-3 months",
        "courses": ["freeCodeCamp JavaScript", "JavaScript.info"],
        "practice": "Build interactive portfolio. Create weather app using API. Add animations.",
        "cert": "Portfolio projects over certs",
        "project": "Real-Time Chat App - WebSockets for messaging, deploy on Netlify"
    },
    "Machine Learning": {
        "level": "High",
        "time": "4-6 months",
        "courses": ["Andrew Ng's ML Course (Coursera)", "Fast.ai Practical Deep Learning"],
        "practice": "Kaggle competitions (Titanic). Movie recommender. Image classifier.",
        "cert": "Google ML Engineer Certificate",
        "project": "Housing Price Predictor - scikit-learn, feature engineering, Flask API"
    },
    "Data Science": {
        "level": "Medium-High",
        "time": "3-5 months",
        "courses": ["IBM Data Science Professional", "DataCamp Data Scientist Track"],
        "practice": "Analyze public datasets. Create Plotly visualizations. Write technical blog.",
        "cert": "IBM Data Science Certificate",
        "project": "Customer Churn Analysis - EDA with Pandas, predictive model, Streamlit dashboard"
    },
    "SQL": {
        "level": "Low-Medium",
        "time": "3-6 weeks",
        "courses": ["Mode SQL Tutorial", "SQLBolt (Interactive)", "Codecademy Learn SQL"],
        "practice": "Complex JOINs on sample databases. Optimize queries with indexes. Create views.",
        "cert": "Practice > Certifications",
        "project": "E-commerce Analytics DB - Star schema design, KPI queries, stored procedures"
    },
    "AWS": {
        "level": "Medium-High",
        "time": "2-3 months",
        "courses": ["AWS Cloud Practitioner (Free)", "A Cloud Guru"],
        "practice": "Deploy to S3 + CloudFront. Set up EC2. Create Lambda function (free tier).",
        "cert": "AWS Certified Cloud Practitioner",
        "project": "Serverless Image Resizer - S3, Lambda, API Gateway, DynamoDB"
    },
    "GCP": {
        "level": "Medium-High",
        "time": "2-3 months",
        "courses": ["Google Cloud Skills Boost", "Coursera GCP Specialization"],
        "practice": "Deploy to Cloud Run. Use BigQuery for analytics. Set up Cloud Functions.",
        "cert": "Google Cloud Associate Engineer",
        "project": "Data Pipeline - Cloud Functions, BigQuery, Looker Studio dashboard"
    },
    "Docker": {
        "level": "Medium",
        "time": "2-3 weeks",
        "courses": ["Docker Official Guide", "Docker Mastery (Udemy)"],
        "practice": "Dockerize your apps. Use docker-compose for multi-container. Push to Docker Hub.",
        "cert": "Hands-on experience",
        "project": "Microservices Blog - Frontend + Backend + DB containers with docker-compose"
    },
    "React": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["React Official Docs", "Scrimba Learn React"],
        "practice": "Build 5 apps: todo, weather, quiz, cart, blog. Master hooks (useState, useEffect).",
        "cert": "Portfolio projects",
        "project": "Job Board Dashboard - API fetch, search/filter, React Router, deploy to Vercel"
    },
    "Computer Vision": {
        "level": "High",
        "time": "3-5 months",
        "courses": ["CS231n Stanford (YouTube)", "PyImageSearch tutorials"],
        "practice": "Object detection with YOLO. Image classification with CNN. OCR projects.",
        "cert": "Portfolio > Certifications",
        "project": "Document Scanner - OpenCV preprocessing, text extraction, deploy as web app"
    },
    "NLP": {
        "level": "High",
        "time": "3-4 months",
        "courses": ["NLP Specialization (deeplearning.ai)", "Hugging Face Course"],
        "practice": "Sentiment analyzer. Intent chatbot. Fine-tune BERT on custom data.",
        "cert": "Portfolio projects",
        "project": "Job Description Analyzer - spaCy NER, TF-IDF matching, skill trend visualization"
    },
    "Tableau": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["Tableau Desktop Specialist Path", "Tableau Public Gallery"],
        "practice": "5 viz types: bar, line, map, scatter, heatmap. Build dashboard stories.",
        "cert": "Tableau Desktop Specialist",
        "project": "COVID Tracker - Live data, choropleth map, time series, publish to Tableau Public"
    },
    "Power BI": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["Microsoft Power BI Training (Free)", "Enterprise DNA YouTube"],
        "practice": "Connect real data sources. Build interactive dashboards. Publish to Service.",
        "cert": "Microsoft Data Analyst Associate",
        "project": "Sales Dashboard - Star schema, KPI cards, time intelligence, map visual"
    },
    "Excel": {
        "level": "Low-Medium",
        "time": "2-3 weeks",
        "courses": ["Excel Essential Training (LinkedIn)", "Chandoo.org"],
        "practice": "Pivot tables and charts. VLOOKUP, INDEX-MATCH. Macros for automation.",
        "cert": "Microsoft Office Specialist Excel",
        "project": "Budget Manager - Category tracking, formulas, conditional formatting, macro buttons"
    },
    "Git": {
        "level": "Low",
        "time": "1-2 weeks",
        "courses": ["Git Official Tutorial", "Learn Git Branching (Game)"],
        "practice": "Daily Git usage. Feature branches. Resolve merge conflicts. Open source PRs.",
        "cert": "Not needed - practical skill",
        "project": "Practice: 3 feature branches, meaningful commits, rebasing, squashing"
    },
    "Kubernetes": {
        "level": "High",
        "time": "2-3 months",
        "courses": ["Kubernetes for Beginners (Udemy)", "Official K8s Docs"],
        "practice": "Local Minikube cluster. Deployments, services, ingress. Rolling updates.",
        "cert": "CKA (Certified K8s Admin)",
        "project": "Scalable API - 3 replicas, LoadBalancer, health checks, auto-scaling, Prometheus"
    },
    "Agile": {
        "level": "Low-Medium",
        "time": "2-4 weeks",
        "courses": ["Scrum.org Learning Path", "Agile Foundations (LinkedIn)"],
        "practice": "Apply Agile to personal projects. Trello sprints. Daily notes. Retros.",
        "cert": "PSM I (Professional Scrum Master)",
        "project": "Run 2-week sprints on your next project with user stories and velocity tracking"
    },
    "Testing": {
        "level": "Low-Medium",
        "time": "1-2 months",
        "courses": ["Test Automation University (Free)", "Software Testing Fundamentals"],
        "practice": "Unit tests for Python/JS. pytest or Jest. 80%+ coverage. GitHub Actions CI.",
        "cert": "ISTQB Foundation Level",
        "project": "Test To-Do API - Unit, integration, mocked tests, 90% coverage, CI on every PR"
    },
}

# Default for unmapped skills
DEFAULT_RESOURCE = {
    "level": "Varies",
    "time": "1-3 months",
    "courses": ["Search Coursera, Udemy, YouTube"],
    "practice": "Start with official docs. Build 2-3 small projects. Join communities.",
    "cert": "Check for industry certifications",
    "project": "Find a real problem, break into milestones, build incrementally, share on GitHub"
}

# =============================================================================
# ML SKILL MATCHER
# =============================================================================
@st.cache_data
def ml_skill_matcher(cv_text: str, return_debug: bool = False):
    """ML-based skill detection using TF-IDF + Cosine Similarity."""
    if not TfidfVectorizer or not cosine_similarity:
        return (set(), {}) if return_debug else set()
    
    detected = set()
    debug = {"scores": {}, "features": [], "thresholds": {}, "boosted": {}}
    cv_lower = cv_text.lower()
    
    # Co-occurrence boosting
    cooccurrence = {
        "google cloud": ["GCP", "Cloud Computing", "BigQuery"],
        "gcp": ["GCP", "Cloud Computing"],
        "vision api": ["Computer Vision", "GCP"],
        "bigquery": ["SQL", "GCP", "Data Science"],
        "churn": ["Data Science", "Machine Learning", "Python"],
        "tensorflow": ["Machine Learning", "Deep Learning", "Python"],
        "pytorch": ["Machine Learning", "Deep Learning", "Python"],
        "opencv": ["Computer Vision", "Python"],
        "sagemaker": ["AWS", "Machine Learning"],
        "lambda": ["AWS", "Cloud Computing"],
    }
    
    # Build skill descriptions
    skill_desc = {}
    for skill, keywords in SKILL_GROUPS.items():
        desc = " ".join(keywords).lower()
        # Add context
        if skill == "Computer Vision":
            desc += " image processing opencv yolo cnn detection recognition gcp aws vision api"
        elif skill == "Data Science":
            desc += " churn analytics prediction pandas sklearn bigquery gcp aws sagemaker"
        elif skill == "Machine Learning":
            desc += " tensorflow pytorch sklearn xgboost training prediction model"
        elif skill in ["GCP", "Cloud Computing"]:
            desc += " google cloud bigquery vertex ai cloud functions compute engine"
        elif skill == "AWS":
            desc += " ec2 s3 lambda sagemaker rds dynamodb cloudfront"
        skill_desc[skill] = desc
    
    # Calculate boosts
    boost = {}
    for trigger, skills in cooccurrence.items():
        if trigger in cv_lower:
            for s in skills:
                boost[s] = boost.get(s, 0) + 0.05
    
    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=150, stop_words='english', ngram_range=(1, 2))
    
    try:
        texts = list(skill_desc.values()) + [cv_lower]
        matrix = vectorizer.fit_transform(texts)
        cv_vec = matrix[-1]
        skill_vecs = matrix[:-1]
        sims = cosine_similarity(cv_vec, skill_vecs)[0]
        
        if return_debug:
            features = vectorizer.get_feature_names_out()
            arr = cv_vec.toarray()[0]
            top_idx = arr.argsort()[-15:][::-1]
            debug["features"] = [(features[i], arr[i]) for i in top_idx if arr[i] > 0]
        
        for idx, skill in enumerate(skill_desc.keys()):
            score = sims[idx] + boost.get(skill, 0)
            
            # Dynamic thresholds
            if skill in ["Computer Vision", "Data Science", "Machine Learning", "Deep Learning", "NLP"]:
                thresh = 0.05
            elif skill in ["Python", "SQL", "AWS", "GCP", "Cloud Computing"]:
                thresh = 0.07
            else:
                thresh = 0.12
            
            if return_debug:
                debug["scores"][skill] = score
                debug["thresholds"][skill] = thresh
                if skill in boost:
                    debug["boosted"][skill] = boost[skill]
            
            if score > thresh:
                detected.add(skill)
                
    except Exception as e:
        if return_debug:
            debug["error"] = str(e)
    
    return (detected, debug) if return_debug else detected


# =============================================================================
# TEXT EXTRACTION
# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from uploaded PDF."""
    if PdfReader is None:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF reading error: {str(e)}")


def extract_keywords(text: str) -> Set[str]:
    """Extract skills using regex pattern matching."""
    found = set()
    text_lower = text.lower()
    
    for skill, variations in SKILL_GROUPS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                found.add(skill)
                break
    
    return found


# =============================================================================
# MAIN ANALYSIS
# =============================================================================
def analyze_gap(cv_text: str, job_text: str) -> Dict:
    """Analyze skill gap between CV and job requirements."""
    # Extract skills
    cv_regex = extract_keywords(cv_text)
    cv_ml = ml_skill_matcher(cv_text)
    cv_skills = cv_regex | cv_ml
    
    job_regex = extract_keywords(job_text)
    job_ml = ml_skill_matcher(job_text)
    job_skills = job_regex | job_ml
    
    # Calculate gaps
    matching = cv_skills & job_skills
    missing = job_skills - cv_skills
    extra = cv_skills - job_skills
    
    # Match percentage
    match_pct = len(matching) / len(job_skills) * 100 if job_skills else 0
    
    return {
        "cv_skills": cv_skills,
        "job_skills": job_skills,
        "matching": matching,
        "missing": missing,
        "extra": extra,
        "match_percentage": match_pct
    }


# =============================================================================
# SIDEBAR (ML Debug Panel)
# =============================================================================
with st.sidebar:
    st.markdown("## ⚙️ ML Debug Panel")
    st.caption("Password protected debugging tools")
    
    password = st.text_input("Password:", type="password", key="debug_pwd")
    
    if password == "1234":
        st.success("✅ Access Granted")
        st.divider()
        
        debug_on = st.checkbox("🔬 Enable ML Debug Mode", help="Show detailed ML metrics")
        st.session_state["ml_debug"] = debug_on
        
        if debug_on:
            st.markdown("### Model Config")
            st.code("""
TF-IDF Vectorizer:
├─ max_features: 150
├─ ngram_range: (1,2)
└─ metric: cosine_similarity

Thresholds:
├─ CV/DS/ML/NLP: 0.05
├─ Python/SQL/Cloud: 0.07
└─ Others: 0.12
            """, language="yaml")
            
            if "debug_data" in st.session_state:
                data = st.session_state["debug_data"]
                
                if "features" in data and data["features"]:
                    st.markdown("### Top TF-IDF Features")
                    for feat, weight in data["features"][:10]:
                        st.text(f"{feat}: {weight:.4f}")
                
                if "scores" in data:
                    st.markdown("### Skill Scores")
                    import pandas as pd
                    rows = []
                    for skill, score in sorted(data["scores"].items(), key=lambda x: -x[1]):
                        thresh = data["thresholds"].get(skill, 0.12)
                        status = "✅" if score > thresh else "❌"
                        rows.append({"Skill": skill, "Score": f"{score:.3f}", "Thresh": f"{thresh:.2f}", "Match": status})
                    st.dataframe(pd.DataFrame(rows), height=300)
    elif password:
        st.error("❌ Wrong password")


# =============================================================================
# MAIN UI
# =============================================================================
st.title("🎯 Job Seeker Helper")
st.markdown("**Analyze your CV against job descriptions to find skill gaps and get personalized learning recommendations.**")

# Input columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📄 Your CV")
    cv_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="cv_method", horizontal=True)
    
    if cv_input == "Paste Text":
        cv_text = st.text_area("Paste your CV here:", height=250, placeholder="Paste your CV content...")
    else:
        cv_file = st.file_uploader("Upload CV PDF", type=["pdf"], key="cv_pdf")
        cv_text = ""
        if cv_file:
            try:
                cv_text = extract_text_from_pdf(cv_file)
                st.success(f"✅ Extracted {len(cv_text)} characters")
            except Exception as e:
                st.error(f"Error: {e}")

with col2:
    st.markdown("### 💼 Job Description")
    job_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="job_method", horizontal=True)
    
    if job_input == "Paste Text":
        job_text = st.text_area("Paste job description:", height=250, placeholder="Paste job description...")
    else:
        job_file = st.file_uploader("Upload Job PDF", type=["pdf"], key="job_pdf")
        job_text = ""
        if job_file:
            try:
                job_text = extract_text_from_pdf(job_file)
                st.success(f"✅ Extracted {len(job_text)} characters")
            except Exception as e:
                st.error(f"Error: {e}")

# Analyze button
if st.button("🔍 Analyze Skill Gap", type="primary", use_container_width=True):
    if not cv_text or not job_text:
        st.warning("⚠️ Please provide both CV and Job Description")
    else:
        with st.spinner("Analyzing..."):
            # Run ML with debug if enabled
            if st.session_state.get("ml_debug"):
                _, debug_data = ml_skill_matcher(cv_text, return_debug=True)
                st.session_state["debug_data"] = debug_data
            
            results = analyze_gap(cv_text, job_text)
        
        # Results
        st.divider()
        
        # Score
        pct = results["match_percentage"]
        if pct >= 80:
            color = "green"
            msg = "🎉 Excellent match!"
        elif pct >= 60:
            color = "orange"
            msg = "👍 Good match, some gaps to fill"
        else:
            color = "red"
            msg = "📚 Significant skill gaps - learning plan needed"
        
        st.markdown(f"## Match Score: :{color}[{pct:.0f}%] {msg}")
        
        # Skills overview
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("### ✅ Matching Skills")
            if results["matching"]:
                for s in sorted(results["matching"]):
                    st.markdown(f"• {s}")
            else:
                st.info("No matching skills found")
        
        with c2:
            st.markdown("### ❌ Missing Skills")
            if results["missing"]:
                for s in sorted(results["missing"]):
                    st.markdown(f"• {s}")
            else:
                st.success("No missing skills!")
        
        with c3:
            st.markdown("### ➕ Extra Skills")
            if results["extra"]:
                for s in sorted(results["extra"]):
                    st.markdown(f"• {s}")
            else:
                st.info("No extra skills")
        
        # Learning recommendations for missing skills
        if results["missing"]:
            st.divider()
            st.markdown("## 📚 Personalized Learning Plan")
            st.markdown("*Specific recommendations for each missing skill:*")
            
            for skill in sorted(results["missing"]):
                # Get skill-specific resource or default
                resource = LEARNING_RESOURCES.get(skill, DEFAULT_RESOURCE)
                
                with st.expander(f"**{skill}** - {resource['level']} difficulty, ~{resource['time']}", expanded=False):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        st.markdown(f"**⏱️ Time:** {resource['time']}")
                        st.markdown(f"**📊 Level:** {resource['level']}")
                        st.markdown("**📚 Courses:**")
                        for course in resource['courses']:
                            st.markdown(f"   • {course}")
                    
                    with col_b:
                        st.markdown(f"**🏆 Certification:** {resource['cert']}")
                        st.markdown(f"**🛠️ Practice:** {resource['practice']}")
                    
                    st.markdown(f"**💡 Project:** {resource['project']}")

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit | ML-powered skill detection with TF-IDF + Cosine Similarity")
