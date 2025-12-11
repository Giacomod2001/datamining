# HIERARCHICAL INFERENCE RULES (Parent -> Child implied)
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
SKILL_CLUSTERS = {
    "BI Tools": {"Tableau", "Power BI", "Looker", "Data Studio", "QlikView"},
    "Cloud Providers": {"AWS", "GCP", "Azure"},
    "JS Frameworks": {"React", "Vue", "Angular", "Svelte"},
    "Containerization": {"Docker", "Podman", "Containerd"},
    "Orchestration": {"Kubernetes", "OpenShift", "Nomad"},
    "IaC": {"Terraform", "CloudFormation", "Ansible"},
    "Deep Learning": {"TensorFlow", "PyTorch", "Keras"},
    "SQL Dialects": {"MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"},
    "Office Suites": {"Microsoft Office", "Google Workspace", "LibreOffice"},
    "Project Mgmt": {"Jira", "Asana", "Trello", "Monday.com", "ClickUp"},
    "CRM": {"Salesforce", "HubSpot", "Zoho"},
    "Translation Tools": {"Trados", "MemoQ", "Wordfast", "OmegaT"},
}

# PROJECT BASED SKILLS (Evaluation via Portfolio)
PROJECT_BASED_SKILLS = {
    "Computer Vision", "Deep Learning", "NLP", "Machine Learning", 
    "Data Science", "System Design", "Cloud Architecture", 
    "Graphic Design", "UX/UI Design", "Copywriting", "Translation"
}

# HARD SKILLS (Technical, quantifiable)
HARD_SKILLS = {
    # --- TECH ---
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6"],
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural network", "scikit-learn"],
    "Data Science": ["data science", "data scientist", "data analysis", "analytics"],
    "SQL": ["sql", "mysql", "postgresql", "bigquery"],
    "Cloud Computing": ["cloud", "aws", "gcp", "azure"],
    "Excel": ["excel", "spreadsheet", "vlookup"],

    # --- LANGUAGES ---
    "English": ["english", "eng", "en"],
    "Spanish": ["spanish", "espanol", "esp"],
    "French": ["french", "francais", "fr"],
    "German": ["german", "deutsch", "de"],
    "Italian": ["italian", "italiano", "it"],
    "Chinese": ["chinese", "mandarin", "cantonese"],
    "Japanese": ["japanese"],

    # --- BUSINESS / ADMIN ---
    "Project Management": ["project management", "pmp", "prince2", "scrum master"],
    "Microsoft Office": ["microsoft office", "ms office", "office 365", "word", "powerpoint"],
    "Customer Service": ["customer service", "client support", "customer success"],
    "Sales": ["sales", "business development", "cold calling", "negotiation"],
    "Accounting": ["accounting", "bookkeeping", "quickbooks", "xero", "finance"],
    "HR": ["human resources", "recruiting", "talent acquisition", "employee relations"],

    # --- MARKETING / CREATIVE ---
    "SEO": ["seo", "search engine optimization", "sem"],
    "Social Media": ["social media", "instagram", "linkedin", "tiktok", "facebook ads"],
    "Copywriting": ["copywriting", "content writing", "blogging", "technical writing"],
    "Graphic Design": ["graphic design", "photoshop", "illustrator", "indesign", "figma", "adobe cc"],
    "UX/UI Design": ["ux/ui", "user experience", "user interface", "wireframing", "prototyping"],

    # --- TRANSLATION ---
    "Translation": ["translation", "translating", "interpreting", "localization", "subtitling"],
    "CAT Tools": ["cat tools", "trados", "memoq", "wordfast"],
}

# SOFT SKILLS
SOFT_SKILLS = {
    "Agile": ["agile", "scrum", "kanban", "sprint"],
    "Leadership": ["leadership", "team lead", "management", "mentoring"],
    "Communication": ["communication", "presentation", "stakeholder"],
    "Problem Solving": ["problem solving", "analytical thinking", "critical thinking"],
    "Teamwork": ["teamwork", "collaboration", "team player"],
    "Time Management": ["time management", "prioritization"],
    "Attention to Detail": ["attention to detail", "precision", "accuracy"],
    "Creativity": ["creativity", "creative thinking", "innovation"],
}

ALL_SKILLS = {**HARD_SKILLS, **SOFT_SKILLS}

# LEARNING RESOURCES (Generic fallback added)
LEARNING_RESOURCES = {
    "Python": {"courses": ["Python for Everybody (Coursera)"], "project": "Scripting automation"},
    # ... (Keep existing detailed ones if needed, but reducing size for brevity/maintenance)
    "Excel": {"courses": ["Excel Skills for Business (Coursera)"], "project": "Budget Dashboard"},
    "SEO": {"courses": ["Moz Beginner Guide", "Google Digital Garage"], "project": "Audit a website"},
    "Translation": {"courses": ["Translation in Practice (Coursera)"], "project": "Translate a Wikipedia article"},
}

DEFAULT_RESOURCE = {
    "courses": ["Search on Coursera, Udemy, or LinkedIn Learning", "Read Official Documentation"], 
    "project": "Build a portfolio piece showing this skill"
}
