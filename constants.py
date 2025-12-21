# HIERARCHICAL INFERENCE RULES (Parent -> Child implied)
INFERENCE_RULES = {
    # Cloud & Data
    "BigQuery": ["Cloud Computing", "SQL", "Data Science", "Data Warehousing"],
    "GCP": ["Cloud Computing"],
    "AWS": ["Cloud Computing"],
    "Azure": ["Cloud Computing"],
    "Snowflake": ["Cloud Computing", "SQL", "Data Warehousing"],
    "Redshift": ["Cloud Computing", "SQL", "Data Warehousing", "AWS"],
    
    # Frontend
    "React": ["Frontend", "JavaScript"],
    "Vue": ["Frontend", "JavaScript"],
    "Angular": ["Frontend", "JavaScript", "TypeScript"],
    "Next.js": ["Frontend", "React", "JavaScript"],
    
    # DevOps & Infrastructure
    "Git": ["Version Control", "DevOps"],
    "Docker": ["DevOps", "Containerization"],
    "Kubernetes": ["DevOps", "Containerization", "Orchestration"],
    "Terraform": ["DevOps", "IaC"],
    "Airflow": ["Data Engineering", "ETL", "Python"],
    
    # BI & Visualization
    "Tableau": ["Data Visualization", "BI"],
    "Power BI": ["Data Visualization", "BI"],
    "Looker": ["Data Visualization", "BI"],
    "Looker Studio": ["Data Visualization", "BI"],
    "Data Studio": ["Data Visualization", "BI"],
    "Google Data Studio": ["Data Visualization", "BI"],
    "Metabase": ["Data Visualization", "BI"],
    
    # Analytics
    "GA4": ["Web Analytics", "Analytics", "Google Analytics"],
    "Google Analytics": ["Web Analytics", "Analytics"],
    "Adobe Analytics": ["Web Analytics", "Analytics"],
    
    # ML & AI
    "TensorFlow": ["Machine Learning", "Deep Learning", "Python"],
    "PyTorch": ["Machine Learning", "Deep Learning", "Python"],
    "Scikit-learn": ["Machine Learning", "Python"],
    
    # Programming Languages (implicit skills)
    "Pandas": ["Python", "Data Analysis"],
    "NumPy": ["Python", "Data Analysis"],
    "Django": ["Python", "Backend", "Web Development"],
    "Flask": ["Python", "Backend", "Web Development"],
    "FastAPI": ["Python", "Backend", "API Development"],
    "Spring Boot": ["Java", "Backend"],
    "Node.js": ["JavaScript", "Backend"],
}

# SKILL CLUSTERS (Interchangeable/Equivalent skills)
# If a job requires skill A and candidate has skill B from the same cluster, 
# it counts as a transferable skill
SKILL_CLUSTERS = {
    # BI & Visualization Tools - ALL EQUIVALENT
    "BI Tools": {
        "Tableau", "Power BI", "Looker", "Looker Studio", "Data Studio", 
        "Google Data Studio", "QlikView", "Qlik Sense", "Metabase", "Superset",
        "Sisense", "Domo", "Mode Analytics", "Redash"
    },
    
    # Web Analytics - ALL EQUIVALENT
    "Analytics Tools": {
        "Google Analytics", "GA4", "Adobe Analytics", "Matomo", 
        "Mixpanel", "Amplitude", "Heap", "Pendo", "Hotjar"
    },
    
    # Cloud Providers - EQUIVALENT for general cloud skills
    "Cloud Providers": {"AWS", "GCP", "Azure", "Google Cloud", "Amazon Web Services"},
    
    # JavaScript Frameworks - EQUIVALENT
    "JS Frameworks": {"React", "Vue", "Angular", "Svelte", "Next.js", "Nuxt.js"},
    
    # Python Web Frameworks - EQUIVALENT
    "Python Web Frameworks": {"Django", "Flask", "FastAPI", "Pyramid"},
    
    # Containerization - EQUIVALENT
    "Containerization": {"Docker", "Podman", "Containerd", "LXC"},
    
    # Container Orchestration - EQUIVALENT
    "Orchestration": {"Kubernetes", "OpenShift", "Nomad", "Docker Swarm", "K8s"},
    
    # Infrastructure as Code - EQUIVALENT
    "IaC": {"Terraform", "CloudFormation", "Ansible", "Pulumi", "Chef", "Puppet"},
    
    # ML Frameworks - EQUIVALENT
    "ML Frameworks": {"TensorFlow", "PyTorch", "Keras", "JAX", "MXNet"},
    
    # SQL Databases - EQUIVALENT for SQL skills
    "SQL Databases": {
        "MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery", 
        "Snowflake", "Redshift", "SQLite", "MariaDB"
    },
    
    # NoSQL Databases - EQUIVALENT
    "NoSQL Databases": {"MongoDB", "Cassandra", "DynamoDB", "Redis", "Elasticsearch", "Neo4j"},
    
    # Data Orchestration - EQUIVALENT
    "Data Orchestration": {"Airflow", "Luigi", "Prefect", "Dagster", "dbt"},
    
    # Office Suites - EQUIVALENT
    "Office Suites": {"Microsoft Office", "Google Workspace", "LibreOffice", "Office 365"},
    
    # Spreadsheets - EQUIVALENT
    "Spreadsheets": {"Excel", "Google Sheets", "Numbers", "Calc"},
    
    # Project Management - EQUIVALENT
    "Project Mgmt": {"Jira", "Asana", "Trello", "Monday.com", "ClickUp", "Notion", "Basecamp"},
    
    # CRM - EQUIVALENT
    "CRM": {"Salesforce", "HubSpot", "Zoho", "Pipedrive", "Microsoft Dynamics"},
    
    # Design Tools - EQUIVALENT
    "Design Tools": {"Figma", "Sketch", "Adobe XD", "InVision", "Axure"},
    
    # Graphic Design - EQUIVALENT
    "Graphic Suite": {"Photoshop", "Illustrator", "InDesign", "Canva", "GIMP", "Affinity"},
    
    # Translation/CAT Tools - EQUIVALENT
    "Translation Tools": {"Trados", "MemoQ", "Wordfast", "OmegaT", "Memsource", "Smartcat"},
    
    # Version Control - EQUIVALENT
    "Version Control": {"Git", "GitHub", "GitLab", "Bitbucket", "SVN"},
    
    # Communication Tools - EQUIVALENT
    "Communication": {"Slack", "Microsoft Teams", "Discord", "Zoom", "Google Meet"},
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
    "Cloud Computing": ["cloud", "azure", "gcp"],
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda"],
    "Azure": ["azure", "microsoft azure"],
    "GCP": ["gcp", "google cloud platform"],
    "Power BI": ["power bi", "powerbi", "dax"],
    "Tableau": ["tableau"],
    "Looker": ["looker"],
    "Looker Studio": ["looker studio", "google looker studio"],
    "Data Studio": ["data studio", "google data studio", "datastudio"],
    "Data Visualization": ["data visualization", "data viz", "visualizzazione dati", "dashboard", "reporting", "charts"],
    "Google Analytics": ["google analytics", "analytics"],
    "GA4": ["ga4", "google analytics 4", "analytics 4"],
    "Web Analytics": ["web analytics", "analytics", "digital analytics", "analisi web"],
    "System Design": ["system design", "distributed systems", "scalability"],
    "Git": ["git", "github", "gitlab"],
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

# SOFT SKILLS (Expanded for Versatility)
SOFT_SKILLS = {
    # --- PERSONAL ---
    "Creativity": ["creativity", "creative thinking", "innovation", "creatività", "pensiero creativo", "innovazione", "proattività", "iniziativa"],
    "Problem Solving": ["problem solving", "analytical thinking", "critical thinking", "capacità analitiche", "risoluzione problemi", "pensiero critico", "troubleshooting"],
    "Adaptability": ["adaptability", "flexibility", "resilience", "adattabilità", "flessibilità", "resilienza", "gestione del cambiamento", "open to change"],
    "Time Management": ["time management", "prioritization", "gestione del tempo", "pianificazione", "rispetto scadenze", "organizzazione", "puntualità"],
    "Stress Management": ["stress management", "working under pressure", "gestione dello stress", "lavoro sotto pressione", "controllo emotivo"],

    # --- INTERPERSONAL ---
    "Communication": ["communication", "presentation", "stakeholder", "comunicazione", "public speaking", "esposizione", "comunicazione efficace", "ascolto attivo", "active listening"],
    "Teamwork": ["teamwork", "collaboration", "team player", "lavoro di squadra", "collaborazione", "spirito di squadra", "cooperazione"],
    "Leadership": ["leadership", "team lead", "management", "mentoring", "gestione team", "supervisione", "guida", "coordinamento team", "delega"],
    "Negotiation": ["negotiation", "persuasion", "conflict resolution", "negoziazione", "mediazione", "risoluzione conflitti", "persuasione"],
    "Empathy": ["empathy", "emotional intelligence", "patia", "intelligenza emotiva", "comprensione", "sensibilità"],

    # --- RETAIL / SERVICE ---
    "Customer Service": ["customer service", "client support", "customer orientation", "assistenza clienti", "orientamento al cliente", "servizio clienti", "supporto clienti", "gestione reclami"],
    "Cash Handling": ["cash handling", "pos", "cash register", "uso cassa", "registratore di cassa", "gestione pagamenti", "maneggio denaro"],
    "Sales Assistant": ["sales assistant", "shop assistant", "commesso", "addetto vendite", "visual merchandising", "allestimento"],

    # --- ADMIN / OFFICE ---
    "Data Entry": ["data entry", "typing", "inserimento dati", "velocità di digitazione", "archiviazione", "gestione documenti"],
    "Organization": ["organization", "multitasking", "planning", "organizzazione", "ordine", "precisione", "gestione agenda"],
    "Attention to Detail": ["attention to detail", "precision", "accuracy", "attenzione ai dettagli", "precisione", "accuratezza", "cura dei dettagli"],
}

ALL_SKILLS = {**HARD_SKILLS, **SOFT_SKILLS}

# LEARNING RESOURCES (Generic fallback added)
LEARNING_RESOURCES = {
    "Python": {"courses": ["Python for Everybody (Coursera)"], "project": "Scripting automation"},
    # ... (Keep existing detailed ones if needed, but reducing size for brevity/maintenance)
    "Excel": {"courses": ["Excel Skills for Business (Coursera)"], "project": "Budget Dashboard"},
    "SEO": {"courses": ["Moz Beginner Guide", "Google Digital Garage"], "project": "Audit a website"},
    "Translation": {"courses": ["Translation in Practice (Coursera)"], "project": "Translate a Wikipedia article"},
    
    # --- DEMO UPDATES ---
    "Tableau": {"courses": ["Tableau 2024 A-Z (Udemy)", "Data Visualization with Tableau (Coursera)"], "project": "Create a Sales Dashboard"},
    "Power BI": {"courses": ["Microsoft Power BI Data Analyst (Coursera)", "Power BI Masterclass (Udemy)"], "project": "Build an Executive Dashboard"},
    "AWS": {"courses": ["AWS Certified Cloud Practitioner (Udemy)", "AWS Fundamentals (Coursera)"], "project": "Deploy a web app on EC2"},
    "System Design": {"courses": ["System Design Interview (Alex Xu)", "Grokking System Design"], "project": "Design a Scalable URL Shortener"},
}

DEFAULT_RESOURCE = {
    "courses": ["Search on Coursera, Udemy, or LinkedIn Learning", "Read Official Documentation"], 
    "project": "Build a portfolio piece showing this skill"
}

# JOB ARCHETYPES (Centroids for Classification)
# Used to recommend roles when the specific JD match is low.
JOB_ARCHETYPES = {
    "Data Scientist": {"Python", "SQL", "Machine Learning", "Data Science", "Pandas", "Statistics", "Deep Learning", "Data Visualization", "AI", "Modeling"},
    "Data Analyst": {"Excel", "SQL", "Power BI", "Tableau", "Data Analysis", "Statistics", "Reporting", "Python", "Dashboards", "KPI"},
    "Data Engineer": {"Python", "SQL", "BigQuery", "AWS", "Azure", "GCP", "Spark", "Airflow", "ETL", "Pipelines", "Database", "Data Warehousing", "Cloud Computing", "NoSQL", "DevOps"},
    "Backend Developer": {"Python", "Java", "SQL", "API", "Docker", "Kubernetes", "Git", "System Design", "Microservices", "Database", "Server"},
    "Frontend Developer": {"JavaScript", "React", "Vue", "CSS", "HTML", "TypeScript", "UI/UX", "Git", "Responsive Design", "Web Development"},
    "Full Stack Developer": {"JavaScript", "Python", "React", "Node.js", "SQL", "API", "Git", "Docker", "Web Development", "Database"},
    "Project Manager": {"Project Management", "Agile", "Scrum", "Communication", "Leadership", "Stakeholder Management", "Jira", "Planning", "Budgeting", "Risk Management"},
    "Product Manager": {"Product Management", "User Stories", "Roadmap", "Strategy", "UX/UI", "Data Analysis", "Communication", "Product Lifecycle"},
    "Digital Marketer": {"SEO", "Social Media", "Google Analytics", "Content Marketing", "Copywriting", "Advertising", "Campaign Management", "SEM"},
    "Business Analyst": {"Business Analysis", "Requirements Gathering", "SQL", "Excel", "Process Mapping", "Communication", "Stakeholder Management", "BPMN"}
}

