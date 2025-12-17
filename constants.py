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
    "English": ["english", "eng", "en", "inglese"],
    "Spanish": ["spanish", "espanol", "esp", "spagnolo"],
    "French": ["french", "francais", "fr", "francese"],
    "German": ["german", "deutsch", "de", "tedesco"],
    "Italian": ["italian", "italiano", "it"],
    "Chinese": ["chinese", "mandarin", "cantonese"],
    "Japanese": ["japanese"],

    # --- BUSINESS / ADMIN ---
    "Project Management": ["project management", "pmp", "prince2", "scrum master", "project manager", "project coordination", "gestione progetti", "capo progetto", "coordinamento", "program manager"],
    "Microsoft Office": ["microsoft office", "ms office", "office 365", "word", "powerpoint", "excel", "pacchetto office"],
    "Customer Service": ["customer service", "client support", "customer success", "assistenza clienti", "servizio clienti", "supporto clienti", "help desk"],
    "Sales": ["sales", "business development", "cold calling", "negotiation", "vendite", "commerciale", "negoziazione", "account manager"],
    "Accounting": ["accounting", "bookkeeping", "quickbooks", "xero", "finance", "contabilità", "amministrazione", "fatturazione", "bilancio"],
    "HR": ["human resources", "recruiting", "talent acquisition", "employee relations", "recruiter", "hr manager", "risorse umane", "selezione del personale", "gestione personale"],

    # --- MARKETING / CREATIVE ---
    "SEO": ["seo", "search engine optimization", "sem", "seo specialist", "ottimizzazione motori di ricerca"],
    "Social Media": ["social media", "instagram", "linkedin", "tiktok", "facebook ads", "social media manager", "gestione social"],
    "Copywriting": ["copywriting", "content writing", "blogging", "technical writing", "copywriter", "scrittura contenuti", "redazione"],
    "Graphic Design": ["graphic design", "photoshop", "illustrator", "indesign", "figma", "adobe cc", "graphic designer", "grafica", "design grafico"],
    "UX/UI Design": ["ux/ui", "user experience", "user interface", "wireframing", "prototyping", "product designer", "interfaccia utente", "esperienza utente"],

    # --- MEDIA / MARKETING ---
    "Marketing": ["marketing", "market analysis", "analisi di mercato", "marketing specialist", "marketer", "marketing intern", "addetto marketing"],
    "Advertising": ["advertising", "ads", "campagne pubblicitarie", "advertising campaigns", "advertising planning", "pubblicità"],
    "Media Planning": ["media planning", "pianificazione media", "media strategy", "media planner", "strategia media"],

    # --- TRANSLATION ---
    "Translation": ["translation", "translating", "interpreting", "localization", "subtitling", "traduzione", "interpretariato", "localizzazione", "sottotitolaggio"],
    "CAT Tools": ["cat tools", "trados", "memoq", "wordfast"],
}

# SOFT SKILLS
SOFT_SKILLS = {
    "Agile": ["agile", "scrum", "kanban", "sprint", "metodologia agile"],
    "Leadership": ["leadership", "team lead", "management", "mentoring", "gestione team", "supervisione", "guida", "coordinamento team"],
    "Communication": ["communication", "presentation", "stakeholder", "comunicazione", "public speaking", "esposizione", "comunicazione efficace"],
    "Problem Solving": ["problem solving", "analytical thinking", "critical thinking", "capacità analitiche", "risoluzione problemi", "pensiero critico"],
    "Teamwork": ["teamwork", "collaboration", "team player", "lavoro di squadra", "collaborazione", "spirito di squadra"],
    "Time Management": ["time management", "prioritization", "gestione del tempo", "pianificazione", "rispetto scadenze", "organizzazione"],
    "Attention to Detail": ["attention to detail", "precision", "accuracy", "attenzione ai dettagli", "precisione", "accuratezza", "cura dei dettagli"],
    "Creativity": ["creativity", "creative thinking", "innovation", "creatività", "pensiero creativo", "innovazione", "proattività"],
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
