# HIERARCHICAL INFERENCE RULES (Parent -> Child implied)
# If you have the child skill, you definitely have the parent skill.
INFERENCE_RULES = {
    "BigQuery": ["Cloud Computing", "SQL", "Data Science"],
    "GCP": ["Cloud Computing"],
    "AWS": ["Cloud Computing"],
    "Azure": ["Cloud Computing"],
    "React": ["Frontend"],
    "Vue": ["Frontend"],
    "Angular": ["Frontend"],
    "Git": ["Version Control", "DevOps"],
    "Docker": ["DevOps"],
    "Kubernetes": ["DevOps"],
    "Terraform": ["DevOps"],
    "Tableau": ["Data Visualization"],
    "Power BI": ["Data Visualization"],
    "Looker": ["Data Visualization"],
    "TensorFlow": ["Machine Learning", "Deep Learning"],
    "PyTorch": ["Machine Learning", "Deep Learning"],
}

# SKILL CLUSTERS (Interchangeable skills)
# Knowing one implies strong transferable knowledge of others.
SKILL_CLUSTERS = {
    "BI Tools": {"Tableau", "Power BI", "Looker", "Data Studio", "QlikView"},
    "Cloud Providers": {"AWS", "GCP", "Azure"},
    "JS Frameworks": {"React", "Vue", "Angular", "Svelte"},
    "Containerization": {"Docker", "Podman", "Containerd"},
    "Orchestration": {"Kubernetes", "OpenShift", "Nomad"},
    "IaC": {"Terraform", "CloudFormation", "Ansible"},
    "Deep Learning": {"TensorFlow", "PyTorch", "Keras"},
    "SQL Dialects": {"MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"},
}

# HARD SKILLS (Technical, quantifiable)
HARD_SKILLS = {
    # Programming
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6"],
    "C++": ["c++", "cpp", "c plus plus"],
    "C#": ["c#", "csharp", "c sharp", ".net", "dotnet", "asp.net"],
    "Go": ["go", "golang"],
    "Rust": ["rust", "rustlang"],
    "R": ["r language", "r programming", "rstudio", "tidyverse"],
    
    # Domains
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural network", "scikit-learn", "sklearn"],
    "Data Science": ["data science", "data scientist", "data analysis", "analytics", "statistical analysis"],
    "Computer Vision": ["computer vision", "cv", "image processing", "opencv", "yolo"],
    "NLP": ["nlp", "natural language processing", "text mining", "bert", "gpt"],
    "Deep Learning": ["deep learning", "neural network", "cnn", "rnn", "lstm"],
    "Frontend": ["frontend", "front-end", "ui development"],
    "DevOps": ["devops", "sre", "site reliability"],
    "Data Visualization": ["data visualization", "viz", "dashboarding"],
    "Cloud Computing": ["cloud", "cloud computing", "serverless", "iaas", "paas", "saas"],
    "Version Control": ["version control", "source control"],

    # Tools/Tech
    "SQL": ["sql", "mysql", "postgresql", "postgres", "sqlite", "oracle", "sql server"],
    "BigQuery": ["bigquery", "big query", "bq"],
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda"],
    "GCP": ["gcp", "google cloud", "vertex ai", "cloud run"],
    "Docker": ["docker", "container"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Git": ["git", "github", "gitlab"],
    "React": ["react", "reactjs", "next.js"],
    "Tableau": ["tableau"],
    "Power BI": ["power bi", "powerbi"],
    "Looker": ["looker", "looker studio"],
    "Excel": ["excel", "spreadsheet", "vba"],
    "Testing": ["testing", "unit test", "pytest", "jest", "selenium", "qa"],
}

# SOFT SKILLS (Behavioral, require interview)
SOFT_SKILLS = {
    "Agile": ["agile", "scrum", "kanban", "sprint"],
    "Leadership": ["leadership", "team lead", "management", "mentoring"],
    "Communication": ["communication", "presentation", "stakeholder"],
    "Problem Solving": ["problem solving", "analytical thinking", "critical thinking"],
    "Teamwork": ["teamwork", "collaboration", "team player"],
    "Time Management": ["time management", "prioritization"],
}

# Combine for broader searches if needed
ALL_SKILLS = {**HARD_SKILLS, **SOFT_SKILLS}

# LEARNING RESOURCES
LEARNING_RESOURCES = {
    "Python": {"level": "Medium", "time": "2-3 months", "courses": ["Python for Everybody (Coursera)", "Complete Python Bootcamp (Udemy)"], "project": "Personal Finance Tracker"},
    "Java": {"level": "Medium-High", "time": "3-4 months", "courses": ["Java MOOC (Helsinki)", "Oracle Tutorials"], "project": "Employee Management API"},
    "Machine Learning": {"level": "High", "time": "4-6 months", "courses": ["Andrew Ng ML (Coursera)", "Fast.ai"], "project": "Housing Price Predictor"},
    "Data Science": {"level": "Medium", "time": "3-5 months", "courses": ["IBM Data Science (Coursera)", "DataCamp"], "project": "Customer Churn Analysis"},
    "SQL": {"level": "Low-Medium", "time": "3-6 weeks", "courses": ["Mode SQL Tutorial", "SQLBolt"], "project": "E-commerce DB Queries"},
    "BigQuery": {"level": "Medium", "time": "2-4 weeks", "courses": ["Google Cloud Skills Boost", "Coursera GCP"], "project": "Public Dataset Analytics"},
    "AWS": {"level": "Medium-High", "time": "2-3 months", "courses": ["AWS Cloud Practitioner", "A Cloud Guru"], "project": "Serverless Image Resizer"},
    "GCP": {"level": "Medium-High", "time": "2-3 months", "courses": ["Google Cloud Engineer", "Coursera"], "project": "Cloud Run Pipeline"},
    "Cloud Computing": {"level": "Medium", "time": "1-3 months", "courses": ["Intro to Cloud (Udacity)", "AWS/GCP Basics"], "project": "Deploy a simple App"},
    "Docker": {"level": "Medium", "time": "2-3 weeks", "courses": ["Docker Mastery (Udemy)", "Official Docs"], "project": "Microservices Blog"},
    "Git": {"level": "Low", "time": "1-2 weeks", "courses": ["Git Official", "Learn Git Branching"], "project": "Open Source Contribution"},
    "React": {"level": "Medium", "time": "1-2 months", "courses": ["React Docs", "Scrimba"], "project": "Job Board Frontend"},
    "Testing": {"level": "Low-Medium", "time": "1 month", "courses": ["Test Automation University"], "project": "Test Suite for API"},
}

DEFAULT_RESOURCE = {
    "level": "Varies", 
    "time": "1-3 months", 
    "courses": ["Search Coursera/Udemy", "Official Docs"], 
    "project": "Build a small demo app"
}
