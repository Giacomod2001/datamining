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
    
    # ML & AI - General
    "TensorFlow": ["Machine Learning", "Deep Learning", "Python", "AI"],
    "PyTorch": ["Machine Learning", "Deep Learning", "Python", "AI"],
    "Scikit-learn": ["Machine Learning", "Python", "Statistics", "Modeling"],
    "Keras": ["Machine Learning", "Deep Learning", "Python", "AI"],
    "XGBoost": ["Machine Learning", "Python", "Modeling"],
    "LightGBM": ["Machine Learning", "Python", "Modeling"],
    "Random Forest": ["Machine Learning", "Modeling", "Statistics"],
    "K-Means": ["Machine Learning", "Clustering", "Statistics"],
    
    # ML/AI Concept Implications - If you do ML, you have AI skills
    "Machine Learning": ["AI", "Statistics", "Modeling", "Python"],
    "Deep Learning": ["AI", "Machine Learning", "Modeling"],
    "Predictive Modeling": ["Machine Learning", "Statistics", "Modeling", "AI"],
    "Statistical Modeling": ["Statistics", "Modeling", "Data Analysis"],
    
    # Computer Vision - Projects with these tools imply CV skills
    "OpenCV": ["Computer Vision", "Image Processing", "Python"],
    "YOLO": ["Computer Vision", "Object Detection", "Deep Learning"],
    "YOLOv5": ["Computer Vision", "Object Detection", "Deep Learning", "Python"],
    "YOLOv8": ["Computer Vision", "Object Detection", "Deep Learning", "Python"],
    "Detectron2": ["Computer Vision", "Object Detection", "Deep Learning"],
    "MediaPipe": ["Computer Vision", "Image Processing", "Python"],
    "PIL": ["Image Processing", "Python"],
    "Pillow": ["Image Processing", "Python"],
    "ImageNet": ["Computer Vision", "Deep Learning"],
    "ResNet": ["Computer Vision", "Deep Learning", "Image Classification"],
    "VGG": ["Computer Vision", "Deep Learning", "Image Classification"],
    "CNN": ["Computer Vision", "Deep Learning", "Neural Networks"],
    "Convolutional Neural Network": ["Computer Vision", "Deep Learning"],
    "Image Segmentation": ["Computer Vision", "Deep Learning"],
    "Object Detection": ["Computer Vision", "Deep Learning"],
    "Face Recognition": ["Computer Vision", "Deep Learning", "Biometrics"],
    "OCR": ["Computer Vision", "Image Processing", "Text Extraction"],
    "Tesseract": ["Computer Vision", "OCR", "Text Extraction"],
    
    # NLP - Natural Language Processing
    "NLTK": ["NLP", "Natural Language Processing", "Python"],
    "spaCy": ["NLP", "Natural Language Processing", "Python"],
    "Hugging Face": ["NLP", "Deep Learning", "Transformers"],
    "BERT": ["NLP", "Deep Learning", "Transformers"],
    "GPT": ["NLP", "Deep Learning", "Transformers", "LLM"],
    "LLM": ["NLP", "AI", "Machine Learning"],
    "Transformers": ["NLP", "Deep Learning", "Python"],
    "Word2Vec": ["NLP", "Machine Learning"],
    "Sentiment Analysis": ["NLP", "Text Analytics"],
    "Text Classification": ["NLP", "Machine Learning"],
    
    # Programming Languages & Tools (implicit skills)
    "Pandas": ["Python", "Data Analysis"],
    "NumPy": ["Python", "Data Analysis"],
    "Python": ["Pandas"],  # Python users often know Pandas
    "Django": ["Python", "Backend", "Web Development"],
    "Flask": ["Python", "Backend", "Web Development"],
    "FastAPI": ["Python", "Backend", "API Development"],
    "Spring Boot": ["Java", "Backend"],
    "Node.js": ["JavaScript", "Backend"],
    
    # BI Tools imply Dashboards and Reporting
    "Looker Studio": ["Data Visualization", "BI", "Dashboards", "Reporting"],
    "Power BI": ["Data Visualization", "BI", "Dashboards", "Reporting"],
    "Tableau": ["Data Visualization", "BI", "Dashboards", "Reporting"],
    "Google Data Studio": ["Data Visualization", "BI", "Dashboards", "Reporting"],
    
    # Digital Marketing implications
    "GA4": ["Web Analytics", "Analytics", "Google Analytics", "Reporting"],
    "Google Analytics": ["Web Analytics", "Analytics", "Reporting"],
    "Google Tag Manager": ["Web Analytics", "Tracking", "Marketing"],
    
    # Performance Marketing implies campaign skills
    "Performance Marketing": ["Campaign Management", "SEM", "Digital Marketing"],
    "Google Ads": ["SEM", "Campaign Management", "Advertising"],
    "Facebook Ads": ["Social Media", "Campaign Management", "Advertising"],
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

# HARD SKILLS (Technical, quantifiable) - EXPANDED FOR BETTER MATCHING
HARD_SKILLS = {
    # --- PROGRAMMING & DATA ---
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy", "scipy", "matplotlib", "seaborn", "jupyter"],
    "Pandas": ["pandas", "dataframe", "data manipulation"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6", "react", "vue", "angular"],
    "SQL": ["sql", "mysql", "postgresql", "bigquery", "structured query language", "database query", "query", "relational database"],
    "R": ["r programming", "r language", "rstudio", "r studio"],
    
    # --- ML / AI / DATA SCIENCE ---
    "Machine Learning": ["machine learning", "ml", "supervised learning", "unsupervised learning", "scikit-learn", "sklearn", "random forest", "k-means", "kmeans", "regression", "classification", "clustering", "modelli predittivi", "apprendimento automatico"],
    "Deep Learning": ["deep learning", "neural network", "neural networks", "cnn", "rnn", "lstm", "transformer", "rete neurale", "reti neurali"],
    "AI": ["artificial intelligence", "ai", "intelligenza artificiale", "ai-powered", "ai powered", "intelligent", "cognitive"],
    "Data Science": ["data science", "data scientist", "data analysis", "analytics", "big data", "scienza dei dati", "analisi dati"],
    "Modeling": ["modeling", "modelling", "statistical modeling", "statistical modelling", "predictive modeling", "predictive modelling", "model", "models", "modello", "modelli", "modellazione"],
    "Statistics": ["statistics", "statistical", "statistica", "statistiche", "statistical analysis", "analisi statistica", "hypothesis testing", "regression analysis", "stat"],
    "Predictive Analytics": ["predictive analytics", "predictive modelling", "predictive modeling", "forecasting", "previsione", "analitica predittiva"],
    
    # --- CLOUD & PLATFORMS ---
    "Cloud Computing": ["cloud", "azure", "gcp", "cloud computing", "cloud platform", "cloud native", "cloud-native"],
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda", "redshift", "sagemaker"],
    "Azure": ["azure", "microsoft azure"],
    "GCP": ["gcp", "google cloud platform", "google cloud", "bigquery ml", "cloud functions", "vertex ai"],
    "BigQuery": ["bigquery", "big query", "bq"],
    "Streamlit": ["streamlit"],
    
    # --- BI & VISUALIZATION ---
    "Power BI": ["power bi", "powerbi", "dax", "power query"],
    "Tableau": ["tableau", "tableau desktop", "tableau server"],
    "Looker": ["looker"],
    "Looker Studio": ["looker studio", "google looker studio", "data studio", "google data studio", "datastudio"],
    "Data Visualization": ["data visualization", "data viz", "visualizzazione dati", "charts", "graphs", "visualization", "visualizations"],
    "Dashboards": ["dashboard", "dashboards", "interactive dashboard", "interactive dashboards", "cruscotto", "pannello di controllo", "report dashboard"],
    "Reporting": ["reporting", "report", "reports", "reportistica", "business reporting", "data reporting", "analisi report"],
    "Business Intelligence": ["business intelligence", "bi", "intelligence"],
    
    # --- ANALYTICS & TRACKING ---
    "Google Analytics": ["google analytics", "analytics", "ga"],
    "GA4": ["ga4", "google analytics 4", "analytics 4"],
    "Web Analytics": ["web analytics", "analytics", "digital analytics", "analisi web", "website analytics", "site analytics"],
    "Google Tag Manager": ["google tag manager", "gtm", "tag manager", "tagging", "tracking implementation"],
    "A/B Testing": ["a/b testing", "ab testing", "split testing", "test a/b", "conversion optimization", "cro"],
    
    # --- DIGITAL MARKETING ---
    "SEO": ["seo", "search engine optimization", "organic search", "ottimizzazione motori di ricerca", "posizionamento"],
    "SEM": ["sem", "search engine marketing", "ppc", "pay per click", "paid search", "google ads", "adwords", "advertising campaigns", "paid advertising"],
    "Social Media": ["social media", "instagram", "linkedin", "tiktok", "facebook", "twitter", "social media marketing", "gestione social", "social network", "social platform", "multi-platform social", "social media presence"],
    "Campaign Management": ["campaign management", "campaign", "campaigns", "advertising campaigns", "marketing campaigns", "campaign planning", "gestione campagne", "campagne", "performance campaigns", "campagne pubblicitarie", "campaign monitoring"],
    "Performance Marketing": ["performance marketing", "performance", "digital performance", "paid performance", "paid campaigns"],
    "Marketing Automation": ["marketing automation", "automation", "email automation", "crm automation"],
    "Email Marketing": ["email marketing", "email", "newsletter", "email newsletters", "email campaigns", "mailing"],
    "E-commerce": ["e-commerce", "ecommerce", "online store", "shopify", "magento", "woocommerce", "vendita online"],
    
    # --- CONTENT & CREATIVE ---
    "Copywriting": ["copywriting", "content writing", "blogging", "technical writing", "copywriter", "scrittura contenuti", "redazione", "content creation", "content strategy"],
    "Marketing": ["marketing", "market analysis", "analisi di mercato", "marketing specialist", "marketer", "marketing intern", "addetto marketing", "marketing analytics", "digital marketing", "marketing strategy"],
    "Advertising": ["advertising", "ads", "campagne pubblicitarie", "advertising campaigns", "advertising planning", "pubblicità", "adv"],
    "Media Planning": ["media planning", "pianificazione media", "media strategy", "media planner", "strategia media"],
    "Graphic Design": ["graphic design", "photoshop", "illustrator", "indesign", "figma", "adobe cc", "graphic designer", "grafica", "design grafico", "canva"],
    "UX/UI Design": ["ux/ui", "user experience", "user interface", "wireframing", "prototyping", "product designer", "interfaccia utente", "esperienza utente", "ux", "ui"],
    
    # --- TOOLS & SOFTWARE ---
    "Excel": ["excel", "spreadsheet", "vlookup", "pivot table", "pivot tables", "fogli di calcolo", "microsoft excel", "advanced excel"],
    "Microsoft Office": ["microsoft office", "ms office", "office 365", "word", "powerpoint", "excel", "pacchetto office", "office suite"],
    "CRM": ["crm", "salesforce", "hubspot", "zoho", "customer relationship", "crm platforms", "crm systems", "gestione clienti"],
    "Git": ["git", "github", "gitlab", "version control", "bitbucket"],
    "System Design": ["system design", "distributed systems", "scalability", "architecture"],
    "JMP": ["jmp", "jmp statistical"],
    
    # --- LANGUAGES ---
    "English": ["english", "eng", "en", "inglese", "professional proficiency", "fluent english", "b2", "c1", "c2"],
    "Spanish": ["spanish", "espanol", "esp", "spagnolo"],
    "French": ["french", "francais", "fr", "francese"],
    "German": ["german", "deutsch", "de", "tedesco"],
    "Italian": ["italian", "italiano", "it", "native", "madrelingua"],
    "Chinese": ["chinese", "mandarin", "cantonese"],
    "Japanese": ["japanese"],

    # --- BUSINESS & MANAGEMENT ---
    "Project Management": ["project management", "pmp", "prince2", "scrum master", "project manager", "project coordination", "gestione progetti", "capo progetto", "coordinamento", "program manager", "agile", "scrum"],
    "Customer Service": ["customer service", "client support", "customer success", "assistenza clienti", "servizio clienti", "supporto clienti", "help desk", "customer experience"],
    "Sales": ["sales", "business development", "cold calling", "negotiation", "vendite", "commerciale", "negoziazione", "account manager"],
    "Accounting": ["accounting", "bookkeeping", "quickbooks", "xero", "finance", "contabilità", "amministrazione", "fatturazione", "bilancio"],
    "HR": ["human resources", "recruiting", "talent acquisition", "employee relations", "recruiter", "hr manager", "risorse umane", "selezione del personale", "gestione personale"],

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
# Skills should match what extract_skills_from_text will find
JOB_ARCHETYPES = {
    "Data Scientist": {
        "Python", "SQL", "Machine Learning", "Data Science", "Statistics", 
        "Deep Learning", "Data Visualization", "AI", "Modeling", "BigQuery",
        "TensorFlow", "PyTorch", "Predictive Analytics", "GCP", "Cloud Computing"
    },
    "Data Analyst": {
        "Excel", "SQL", "Power BI", "Tableau", "Looker Studio", "Data Visualization", 
        "Statistics", "Reporting", "Python", "Dashboards", "Google Analytics", "GA4",
        "BigQuery", "Data Science", "Business Intelligence"
    },
    "Data Engineer": {
        "Python", "SQL", "BigQuery", "AWS", "Azure", "GCP", "Airflow", 
        "Cloud Computing", "Docker", "Kubernetes", "Git", "Data Science"
    },
    "Backend Developer": {
        "Python", "Java", "SQL", "Docker", "Kubernetes", "Git", 
        "System Design", "FastAPI", "Django", "Flask", "Cloud Computing"
    },
    "Frontend Developer": {
        "JavaScript", "React", "Vue", "TypeScript", "Git", "UX/UI Design"
    },
    "Full Stack Developer": {
        "JavaScript", "Python", "React", "SQL", "Docker", "Git", "Node.js"
    },
    "Digital Marketing Analyst": {
        "Google Analytics", "GA4", "Google Tag Manager", "Looker Studio", 
        "A/B Testing", "Data Visualization", "Python", "SQL", "Marketing",
        "Campaign Management", "Performance Marketing", "Dashboards", "Web Analytics"
    },
    "Digital Marketer": {
        "SEO", "SEM", "Social Media", "Google Analytics", "GA4", "Marketing", 
        "Copywriting", "Advertising", "Campaign Management", "Email Marketing",
        "Performance Marketing", "Google Tag Manager", "A/B Testing", "CRM"
    },
    "Marketing Analyst": {
        "Google Analytics", "GA4", "Looker Studio", "Data Visualization",
        "Marketing", "Campaign Management", "A/B Testing", "SQL", "Python",
        "Dashboards", "Reporting", "Statistics", "Performance Marketing"
    },
    "Business Analyst": {
        "SQL", "Excel", "Power BI", "Tableau", "Data Visualization",
        "Communication", "Reporting", "Dashboards", "Data Science"
    },
    "Project Manager": {
        "Project Management", "Communication", "Leadership", "Teamwork"
    },
    "Product Manager": {
        "Data Science", "Communication", "UX/UI Design", "Marketing"
    }
}

