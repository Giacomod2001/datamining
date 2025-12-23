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
    
    # Ristorazione & Hospitality
    "Kitchen Management": ["Cooking", "Food Safety", "Leadership"],
    "Sommelier": ["Wine Knowledge", "Hospitality", "Customer Service"],
    "Bartending": ["Customer Service", "Cash Handling"],
    "Table Service": ["Customer Service", "Communication"],
    "Event Planning": ["Project Management", "Budgeting", "Communication"],
    
    # Sanità
    "Nursing": ["First Aid", "Patient Care", "Medical Devices"],
    "Physiotherapy": ["Rehabilitation", "Patient Care"],
    "Elderly Care": ["Nursing", "First Aid", "Empathy"],
    "Laboratory": ["Attention to Detail", "Medical Records"],
    
    # Legale
    "Litigation": ["Legal Research", "Communication"],
    "Contract Law": ["Legal Research", "Compliance"],
    "Corporate Law": ["Contract Law", "Compliance"],
    
    # Edilizia
    "Electrical": ["Safety Compliance", "Problem Solving"],
    "Plumbing": ["Safety Compliance", "Problem Solving"],
    "HVAC": ["Electrical", "Safety Compliance"],
    "Construction": ["Safety Compliance", "Teamwork"],
    
    # Educazione
    "Teaching": ["Communication", "Curriculum Design", "Empathy"],
    "Training": ["Communication", "E-Learning"],
    
    # Logistica
    "Warehouse": ["Inventory Management", "Forklift"],
    "Supply Chain": ["Shipping", "Order Management", "Budgeting"],
    
    # Finanza
    "Financial Analysis": ["Excel", "Statistics", "Budgeting"],
    "Accounting": ["Budgeting", "Tax Preparation", "Excel"],
    "Payroll": ["Excel", "Attention to Detail"],
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
    "Communication Tools": {"Slack", "Microsoft Teams", "Discord", "Zoom", "Google Meet"},
    
    # --- NEW INDUSTRY CLUSTERS ---
    
    # Hospitality Booking Systems - EQUIVALENT
    "Booking Systems": {"Opera", "Protel", "Mews", "Cloudbeds", "Booking.com Extranet"},
    
    # Medical Records Systems - EQUIVALENT
    "EMR Systems": {"Epic", "Cerner", "Meditech", "Athenahealth", "Practice Fusion"},
    
    # Beauty & Wellness Booking - EQUIVALENT
    "Beauty Booking": {"Fresha", "Treatwell", "Timify", "Booksy", "Vagaro"},
    
    # POS Systems - EQUIVALENT
    "POS Systems": {"Square", "Clover", "Toast", "Lightspeed", "Shopify POS"},
    
    # CAD Software - EQUIVALENT
    "CAD Software": {"AutoCAD", "SolidWorks", "SketchUp", "Revit", "Fusion 360", "Inventor"},
    
    # Accounting Software - EQUIVALENT
    "Accounting Software": {"QuickBooks", "Xero", "SAP", "Sage", "FreshBooks", "Fatture in Cloud"},
    
    # Learning Management - EQUIVALENT
    "LMS": {"Moodle", "Canvas", "Blackboard", "Google Classroom", "Schoology"},
    
    # Shipping/Logistics - EQUIVALENT
    "Logistics Software": {"SAP", "Oracle WMS", "Manhattan", "Blue Yonder", "Infor"},
    
    # Legal Research - EQUIVALENT
    "Legal Research": {"Westlaw", "LexisNexis", "DeJure", "ItalgiureWeb"},
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
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy", "scipy", "matplotlib", "seaborn", "jupyter", "anaconda", "pycharm", "scripting", "automation script"],
    "Pandas": ["pandas", "dataframe", "data manipulation", "data wrangling", "data cleaning", "data preprocessing"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm", "java ee", "hibernate"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6", "react", "vue", "angular", "next.js", "express"],
    "SQL": ["sql", "mysql", "postgresql", "bigquery", "structured query language", "database query", "query", "relational database", "sql server", "oracle", "query optimization", "data query"],
    "R": ["r programming", "r language", "rstudio", "r studio", "tidyverse", "ggplot", "shiny"],
    
    # --- ML / AI / DATA SCIENCE ---
    "Machine Learning": ["machine learning", "ml", "supervised learning", "unsupervised learning", "scikit-learn", "sklearn", "random forest", "k-means", "kmeans", "regression", "classification", "clustering", "modelli predittivi", "apprendimento automatico", "gradient boosting", "xgboost", "lightgbm", "decision tree", "ensemble", "feature engineering", "model training", "hyperparameter tuning"],
    "Deep Learning": ["deep learning", "neural network", "neural networks", "cnn", "rnn", "lstm", "transformer", "rete neurale", "reti neurali", "tensorflow", "pytorch", "keras", "convolutional", "recurrent"],
    "AI": ["artificial intelligence", "ai", "intelligenza artificiale", "ai-powered", "ai powered", "intelligent", "cognitive", "chatbot", "nlp", "natural language processing", "computer vision", "generative ai", "gen ai"],
    "Data Science": ["data science", "data scientist", "data analysis", "big data", "scienza dei dati", "data insights", "exploratory data analysis", "eda", "data mining", "data pipeline"],


    "Modeling": ["modeling", "modelling", "statistical modeling", "statistical modelling", "predictive modeling", "predictive modelling", "ml model", "data model", "modello predittivo", "modellazione dati", "model deployment", "model validation", "model training"],
    "Statistics": ["statistics", "statistical", "statistica", "statistiche", "statistical analysis", "analisi statistica", "hypothesis testing", "regression analysis", "stat", "a/b testing", "statistical significance", "confidence interval", "probability"],
    "Predictive Analytics": ["predictive analytics", "predictive modelling", "predictive modeling", "forecasting", "previsione", "analitica predittiva", "time series", "demand forecasting", "churn prediction"],
    
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
    "Reporting": ["reporting", "reportistica", "business reporting", "data reporting", "report building", "report creation", "analisi report", "report automation"],
    "Business Intelligence": ["business intelligence", "bi tools", "bi software", "bi platform"],
    
    # --- ANALYTICS & TRACKING ---
    "Google Analytics": ["google analytics", "ga4", "google analytics 4", "ga 4"],
    "GA4": ["ga4", "google analytics 4", "analytics 4"],
    "Web Analytics": ["web analytics", "digital analytics", "website analytics", "site analytics", "web tracking"],
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
    "Media Planning": ["media planning", "pianificazione media", "media strategy", "media planner", "strategia media", "media plan", "piano media", "media mix", "media buying", "acquisto media", "media buyer", "programmatic", "programmatic advertising", "dsp", "demand side platform", "dv360", "display video 360", "google dv360", "google marketing platform", "gmp", "trade desk", "thetradedesk", "amazon dsp", "xandr", "rtb", "real time bidding", "cpm", "cpc", "ctr", "click through rate", "impressions", "reach", "frequency", "grp", "gross rating point", "trp", "target rating point", "sov", "share of voice", "media schedule", "flight", "flighting", "dayparting", "geo targeting", "audience targeting", "contextual targeting", "behavioral targeting", "retargeting", "remarketing", "cross media", "multicanale", "omnichannel", "above the line", "atl", "below the line", "btl", "tv planning", "radio planning", "ooh", "out of home", "dooh", "digital out of home", "print media", "stampa", "native advertising", "sponsored content", "influencer marketing", "kpi media", "roas", "return on ad spend", "cpa", "cost per acquisition", "viewability", "brand safety", "ad fraud", "verification", "moat", "ias", "integral ad science", "nielsen", "auditel", "audipress", "comscore", "mediamond", "rai pubblicità", "publitalia", "sky media", "meta business manager", "meta ads manager", "facebook ads", "instagram ads", "linkedin campaign manager", "spotify ads", "youtube ads", "tiktok ads manager"],

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
    "English": ["english", "inglese", "professional proficiency", "fluent english", "english language", "mother tongue english"],
    "Spanish": ["spanish", "espanol", "spagnolo", "spanish language"],
    "French": ["french", "francais", "francese", "french language"],
    "German": ["german", "deutsch", "tedesco", "german language"],
    "Italian": ["italian", "italiano", "madrelingua", "italian language", "lingua italiana"],
    "Chinese": ["chinese", "mandarin", "cantonese"],
    "Japanese": ["japanese"],

    # --- BUSINESS & MANAGEMENT ---
    "Project Management": ["project management", "pmp", "prince2", "scrum master", "project manager", "project coordination", "gestione progetti", "capo progetto", "coordinamento", "program manager", "agile", "scrum"],
    "Customer Service": ["customer service", "client support", "customer success", "assistenza clienti", "servizio clienti", "supporto clienti", "help desk", "customer experience"],
    "Sales": ["sales", "business development", "cold calling", "vendite", "commerciale", "sales manager", "sales representative", "venditore", "account executive"],

    "Accounting": ["accounting", "bookkeeping", "quickbooks", "xero", "finance", "contabilità", "amministrazione", "fatturazione", "bilancio"],
    "HR": ["human resources", "recruiting", "talent acquisition", "employee relations", "recruiter", "hr manager", "risorse umane", "selezione del personale", "gestione personale"],

    # --- TRANSLATION ---
    "Translation": ["translation", "translating", "interpreting", "localization", "subtitling", "traduzione", "interpretariato", "localizzazione", "sottotitolaggio"],
    "CAT Tools": ["cat tools", "trados", "memoq", "wordfast"],

    # --- RISTORAZIONE & FOOD ---
    "Cooking": ["cooking", "cucina", "chef", "cuoco", "cuoca", "culinary", "food preparation", "preparazione cibi", "cottura", "line cook", "sous chef", "executive chef", "chef de partie", "commis", "cucina italiana", "cucina internazionale", "alta cucina", "fine dining", "grill", "griglia", "frittura", "frying", "roasting", "brasatura", "knife skills", "taglio", "mise en place", "food plating", "impiattamento"],
    "Pastry": ["pastry", "pasticceria", "dessert", "baking", "panificazione", "dolci", "pastry chef", "pasticcere", "patisserie", "cake decorating", "decorazione torte", "cioccolateria", "chocolate", "bread making", "lievitati", "croissant", "brioche", "fondant", "glassatura", "frosting"],
    "Food Safety": ["haccp", "food safety", "sicurezza alimentare", "igiene alimentare", "food hygiene", "sanitation", "sanificazione", "allergen management", "allergeni", "food handling", "temperatura alimenti", "cold chain", "catena del freddo", "cross contamination", "contaminazione"],
    "Table Service": ["table service", "servizio sala", "waiter", "waitress", "cameriere", "cameriera", "waiting tables", "silver service", "servizio alla francese", "servizio alla russa", "servizio all'inglese", "taking orders", "presa comande", "table setting", "mise en place tavola", "restaurant service", "fine dining service", "banquet service", "servizio banchetti"],
    "Bartending": ["bartending", "barman", "barmaid", "barista", "mixology", "cocktail", "barista caffetteria", "latte art", "shaker", "cocktail shaking", "stirring", "muddling", "flair bartending", "speed bartending", "coffee brewing", "espresso", "cappuccino", "caffetteria", "spirits knowledge", "distillati", "liquori", "aperitivo"],
    "Wine Knowledge": ["sommelier", "wine", "vino", "enologia", "wine pairing", "abbinamento vini", "wine tasting", "degustazione", "cantina", "wine cellar", "decanting", "decantazione", "wine service", "servizio vino", "corkage", "wine list", "carta dei vini", "terroir", "vintage", "annata"],
    "Kitchen Management": ["kitchen management", "gestione cucina", "head chef", "capo cuoco", "brigade de cuisine", "kitchen brigade", "food cost", "costo cibo", "menu planning", "pianificazione menu", "inventory control", "controllo scorte", "supplier management", "gestione fornitori", "kitchen scheduling", "turni cucina"],


    # --- HOSPITALITY & TURISMO ---
    "Hospitality": ["hospitality", "ospitalità", "hotel", "albergo", "accoglienza", "guest services"],
    "Reception": ["reception", "front desk", "receptionist", "front office", "check-in", "check-out", "booking"],
    "Housekeeping": ["housekeeping", "pulizie", "room service", "servizio in camera", "governante", "housekeeper"],
    "Tour Guide": ["tour guide", "guida turistica", "tourist guide", "accompagnatore turistico", "escursioni"],
    "Travel Agency": ["travel agent", "agente di viaggio", "agenzia viaggi", "tour operator", "booking system"],
    "Event Planning": ["event planning", "event management", "organizzazione eventi", "catering", "banqueting", "wedding planner"],
    "Concierge": ["concierge", "portineria", "guest relations", "vip service"],

    # --- SANITÀ & MEDICINA ---
    "Nursing": ["nursing", "infermieristica", "infermiere", "infermiera", "nurse", "patient care", "assistenza paziente", "registered nurse", "rn", "licensed practical nurse", "lpn", "nursing assistant", "oss", "medication administration", "somministrazione farmaci", "vital signs", "parametri vitali", "wound care", "medicazioni", "catheter", "catetere", "iv therapy", "flebo", "triage", "patient assessment", "valutazione paziente", "nursing diagnosis"],
    "First Aid": ["first aid", "primo soccorso", "bls", "blsd", "cpr", "rianimazione", "emergency care", "aed", "defibrillatore", "heimlich", "emergency response", "pronto soccorso", "trauma care", "basic life support", "advanced life support", "als", "phtls", "acls", "first responder", "soccorritore"],
    "Medical Devices": ["medical devices", "dispositivi medici", "ecg", "ekg", "elettrocardiogramma", "defibrillatore", "monitoring", "monitoraggio", "ventilator", "ventilatore", "infusion pump", "pompa infusione", "pulse oximeter", "saturimetro", "blood pressure", "sfigmomanometro", "glucometer", "glucometro", "nebulizer", "aerosol"],
    "Pharmacy": ["pharmacy", "farmacia", "farmacista", "pharmacist", "dispensing", "pharmaceutical", "prescription", "ricetta", "drug interaction", "interazione farmaci", "compounding", "preparazioni galeniche", "pharmacology", "farmacologia", "dosage", "posologia", "generic drugs", "farmaci generici", "otc", "parafarmaco"],
    "Physiotherapy": ["physiotherapy", "fisioterapia", "physical therapy", "rehabilitation", "riabilitazione", "fisioterapista", "manual therapy", "terapia manuale", "massage therapy", "massoterapia", "electrotherapy", "elettroterapia", "ultrasound therapy", "ultrasuoni", "exercise prescription", "esercizio terapeutico", "kinesio taping", "posture correction", "rieducazione posturale", "mobilization", "mobilizzazione"],
    "Elderly Care": ["elderly care", "assistenza anziani", "oss", "operatore socio sanitario", "geriatric", "geriatria", "dementia care", "alzheimer", "mobility assistance", "assistenza mobilità", "personal hygiene", "igiene personale", "feeding assistance", "assistenza pasti", "companionship", "compagnia", "fall prevention", "prevenzione cadute", "rsa", "casa di riposo", "hospice"],
    "Pediatric Care": ["pediatric", "pediatria", "child care", "assistenza bambini", "neonatology", "neonatologia", "pediatric nurse", "pediatra", "vaccination", "vaccinazioni", "child development", "sviluppo bambino", "nicu", "terapia intensiva neonatale", "infant care", "cura neonati", "breastfeeding support", "allattamento"],
    "Medical Records": ["medical records", "cartelle cliniche", "emr", "ehr", "electronic health records", "patient records", "documentazione sanitaria", "medical coding", "codifica sanitaria", "icd-10", "hipaa", "privacy sanitaria", "health informatics", "informatica sanitaria", "patient database", "archivio pazienti"],
    "Laboratory": ["laboratory", "laboratorio", "lab technician", "tecnico laboratorio", "analisi cliniche", "blood tests", "esami sangue", "urinalysis", "esame urine", "microbiology", "microbiologia", "hematology", "ematologia", "biochemistry", "biochimica", "specimen collection", "prelievi", "centrifuge", "centrifuga", "microscopy", "microscopia"],
    "Radiology": ["radiology", "radiologia", "x-ray", "raggi x", "mri", "risonanza magnetica", "tac", "ct scan", "imaging", "diagnostica per immagini", "ultrasound", "ecografia", "mammography", "mammografia", "fluoroscopy", "radiographer", "tecnico radiologo", "pacs", "contrast media", "mezzo di contrasto"],
    "Surgery Assistance": ["surgery", "chirurgia", "surgical assistant", "sala operatoria", "strumentista", "surgical technician", "operating room", "sterile technique", "tecnica sterile", "surgical instruments", "strumentario chirurgico", "anesthesia", "anestesia", "post-operative care", "assistenza post-operatoria", "wound closure", "suture", "laparoscopy", "laparoscopia"],


    # --- LEGALE & AMMINISTRATIVO ---
    "Legal Research": ["legal research", "ricerca giuridica", "jurisprudence", "case law", "giurisprudenza"],
    "Contract Law": ["contract", "contratti", "contract management", "gestione contratti", "contrattualistica"],
    "Litigation": ["litigation", "contenzioso", "court", "tribunale", "processo", "trial"],
    "Notary": ["notary", "notaio", "atti notarili", "notarial", "rogito"],
    "Paralegal": ["paralegal", "legal assistant", "assistente legale", "praticante", "studio legale"],
    "Compliance": ["compliance", "regulatory", "normativa", "adempimenti", "antiriciclaggio", "gdpr", "privacy"],
    "Corporate Law": ["corporate law", "diritto societario", "m&a", "fusioni", "acquisizioni"],

    # --- EDILIZIA & COSTRUZIONI ---
    "Construction": ["construction", "edilizia", "cantiere", "building", "costruzione"],
    "Carpentry": ["carpentry", "falegnameria", "carpenter", "falegname", "woodwork", "legno"],
    "Plumbing": ["plumbing", "idraulica", "plumber", "idraulico", "tubazioni", "impianti idrici"],
    "Electrical": ["electrical", "elettricista", "electrician", "impianti elettrici", "cablaggio", "wiring", "circuit", "circuito", "panel", "quadro elettrico", "conduit", "voltage", "tensione", "amperage", "amperaggio", "220v", "380v", "trifase", "three phase", "outlet", "presa", "switch", "interruttore", "breaker", "fusibile", "grounding", "messa a terra", "electrician license", "patentino elettricista"],
    "Masonry": ["masonry", "muratura", "muratore", "mason", "bricklayer", "brick", "mattone", "mortar", "malta", "concrete", "cemento", "foundation", "fondamenta", "wall construction", "costruzione muri", "plastering", "intonaco", "tiling", "piastrellatura", "flooring", "pavimentazione", "stone work", "pietra"],
    "Painting": ["painting", "verniciatura", "imbianchino", "painter", "tinteggiatura", "spray painting", "verniciatura a spruzzo", "brush", "pennello", "roller", "rullo", "primer", "fondo", "lacquer", "lacca", "enamel", "smalto", "wallpaper", "carta da parati", "color matching", "abbinamento colori", "textured finish", "effetti decorativi"],
    "HVAC": ["hvac", "climatizzazione", "heating", "riscaldamento", "condizionamento", "air conditioning", "ventilation", "ventilazione", "refrigeration", "refrigerazione", "heat pump", "pompa di calore", "furnace", "caldaia", "thermostat", "termostato", "ductwork", "canalizzazione", "r410a", "refrigerant", "refrigerante", "split system", "vrf"],
    "Welding": ["welding", "saldatura", "welder", "saldatore", "mig welding", "tig welding", "arc welding", "saldatura ad arco", "spot welding", "saldatura a punti", "brazing", "brasatura", "soldering", "stagnatura", "welding torch", "torcia", "electrode", "elettrodo", "flux", "filler metal", "metallo d'apporto", "weld inspection", "controllo saldature"],
    "CAD Design": ["autocad", "cad", "technical drawing", "disegno tecnico", "progettazione", "drafting", "blueprint", "planimetria", "3d modeling", "modellazione 3d", "revit", "solidworks", "inventor", "catia", "rendering", "bim", "building information modeling"],
    "Safety Compliance": ["safety", "sicurezza lavoro", "81/08", "d.lgs 81/08", "rspp", "rls", "dpi", "ppe", "personal protective equipment", "osha", "safety training", "formazione sicurezza", "risk assessment", "valutazione rischi", "dvr", "safety audit", "ispezione sicurezza", "work permit", "permesso lavoro", "lockout tagout", "confined space", "spazi confinati", "fall protection", "protezione anticaduta"],

    # --- MECCANICA & AUTOMOTIVE ---
    "Automotive Repair": ["automotive", "meccanico", "mechanic", "car repair", "officina", "riparazione auto", "engine repair", "riparazione motore", "transmission", "cambio", "brakes", "freni", "suspension", "sospensioni", "exhaust", "scarico", "cooling system", "raffreddamento", "oil change", "cambio olio", "tune-up", "tagliando", "car inspection", "revisione", "mot"],
    "Bodywork": ["bodywork", "carrozzeria", "carrozziere", "body repair", "dent repair", "riparazione ammaccature", "panel beating", "spray booth", "cabina verniciatura", "polishing", "lucidatura", "buffing", "rust repair", "riparazione ruggine", "filler", "stucco", "primer", "clear coat", "trasparente"],
    "Tire Service": ["tire", "pneumatici", "gommista", "tire change", "cambio gomme", "wheel alignment", "convergenza", "balancing", "equilibratura", "tire rotation", "rotazione pneumatici", "puncture repair", "riparazione foratura", "tpms", "sensori pressione", "winter tires", "gomme invernali", "summer tires", "gomme estive"],
    "Diagnostics": ["diagnostics", "diagnostica", "obd", "obd2", "scanner", "diagnosi auto", "fault code", "codice errore", "check engine", "spia motore", "oscilloscope", "oscilloscopio", "multimeter", "tester", "live data", "dati in tempo reale", "ecu", "centralina", "scan tool"],
    "CNC Machining": ["cnc", "tornio", "fresatrice", "lathe", "milling", "machining", "g-code", "cam", "computer aided manufacturing", "turning", "tornitura", "drilling", "foratura", "grinding", "rettifica", "threading", "filettatura", "precision machining", "lavorazione di precisione", "tolerance", "tolleranza", "caliper", "calibro"],

    # --- EDUCAZIONE & FORMAZIONE ---
    "Teaching": ["teaching", "insegnamento", "teacher", "insegnante", "docente", "professor", "professore", "classroom management", "gestione classe", "student assessment", "valutazione studenti", "differentiated instruction", "didattica differenziata", "interactive teaching", "didattica interattiva", "primary school", "scuola primaria", "secondary school", "scuola secondaria", "substitute teacher", "supplente"],
    "Tutoring": ["tutoring", "ripetizioni", "tutor", "private lessons", "lezioni private", "homework help", "aiuto compiti", "exam preparation", "preparazione esami", "one-on-one", "individuale", "study skills", "metodo di studio", "subject tutoring", "materie specifiche"],
    "Curriculum Design": ["curriculum design", "curriculum development", "programmazione didattica", "lesson planning", "syllabus", "learning objectives", "obiettivi didattici", "course design", "progettazione corso", "assessment design", "progettazione verifiche", "learning outcomes", "educational standards", "indicazioni nazionali"],

    "E-Learning": ["e-learning", "online teaching", "formazione online", "lms", "moodle", "didattica a distanza", "dad", "virtual classroom", "classe virtuale", "webinar", "zoom", "teams", "google meet", "asynchronous learning", "blended learning", "scorm", "video lessons", "videolezioni", "screen sharing", "condivisione schermo"],
    "Training": ["training", "formazione", "trainer", "formatore", "corporate training", "formazione aziendale", "workshop", "facilitator", "facilitatore", "onboarding", "skill development", "team building", "coaching", "mentoring", "training needs analysis", "train the trainer"],
    "Special Education": ["special education", "sostegno", "special needs", "bisogni educativi speciali", "bes", "dsa", "learning disabilities", "disturbi apprendimento", "autism", "autismo", "adhd", "iep", "pei", "piano educativo individualizzato", "inclusion", "inclusione", "differentiated learning", "assistive technology", "tecnologie assistive"],

    # --- LOGISTICA & SUPPLY CHAIN ---
    "Warehouse": ["warehouse", "magazzino", "magazziniere", "inventory", "inventario", "stoccaggio", "stock", "picking", "packing", "imballaggio", "receiving", "ricezione merce", "put-away", "stoccaggio", "wms", "warehouse management system", "barcode", "codice a barre", "rfid", "fifo", "lifo", "bin location", "ubicazione"],
    "Forklift": ["forklift", "carrello elevatore", "muletto", "patentino muletto", "pallet jack", "transpallet", "reach truck", "retrattile", "order picker", "commissionatore", "counterbalance", "controbilanciato", "forklift license", "patentino", "load capacity", "portata"],
    "Shipping": ["shipping", "spedizioni", "logistics", "logistica", "trasporto", "courier", "corriere", "freight", "merci", "incoterms", "customs", "dogana", "bill of lading", "polizza di carico", "tracking", "tracciamento", "carrier", "vettore", "dhl", "ups", "fedex", "tnt", "gls", "brt"],
    "Supply Chain": ["supply chain", "catena di fornitura", "procurement", "approvvigionamento", "vendor management", "gestione fornitori", "sourcing", "purchasing", "acquisti", "rfq", "request for quotation", "supplier evaluation", "valutazione fornitori", "lead time", "just in time", "jit", "mrp", "erp", "sap"],
    "Order Management": ["order management", "gestione ordini", "order processing", "evasione ordini", "order fulfillment", "back order", "ordine arretrato", "order tracking", "customer order", "ordine cliente", "sales order", "purchase order", "ordine acquisto", "edi", "order status"],
    "Delivery": ["delivery", "consegne", "driver", "autista", "corriere", "last mile", "route planning", "pianificazione percorsi", "proof of delivery", "prova di consegna", "cod", "contrassegno", "express delivery", "consegna rapida", "scheduled delivery", "consegna programmata", "doorstep delivery", "home delivery"],


    # --- MODA & BEAUTY ---
    "Fashion Design": ["fashion design", "moda", "fashion designer", "stilista", "pattern making", "modellistica"],
    "Tailoring": ["tailoring", "sartoria", "sarto", "sarta", "alterations", "cucito", "sewing"],
    "Hairdressing": ["hairdressing", "parrucchiere", "hairdresser", "hair styling", "acconciature", "taglio capelli"],
    "Makeup": ["makeup", "trucco", "makeup artist", "truccatrice", "cosmetics", "beauty"],
    "Aesthetics": ["aesthetics", "estetica", "estetista", "beauty treatments", "trattamenti estetici", "manicure", "pedicure"],
    "Visual Merchandising": ["visual merchandising", "vetrinista", "window display", "allestimento"],

    # --- RETAIL & VENDITE ---
    "Retail Sales": ["retail", "vendita", "shop assistant", "commesso", "sales floor", "punto vendita"],
    "Inventory Management": ["inventory", "gestione magazzino", "stock control", "scorte", "reorder"],
    "POS Systems": ["pos", "registratore di cassa", "cash register", "payment terminal", "terminale pagamento"],
    "Product Knowledge": ["product knowledge", "conoscenza prodotti", "product training", "formazione prodotto"],

    # --- FINANZA & CONTABILITÀ ---
    "Financial Analysis": ["financial analysis", "analisi finanziaria", "financial modeling", "valutazione"],
    "Budgeting": ["budgeting", "budget", "pianificazione finanziaria", "cost control", "controllo costi"],
    "Tax Preparation": ["tax", "tasse", "fiscale", "dichiarazione redditi", "730", "unico", "iva", "vat"],
    "Payroll": ["payroll", "buste paga", "cedolini", "stipendi", "contributi"],
    "Auditing": ["auditing", "revisione", "audit", "internal audit", "revisore"],
    "Banking": ["banking", "banca", "bank operations", "operazioni bancarie", "credito", "credit"],
    "Insurance": ["insurance", "assicurazione", "polizza", "policy", "claims", "sinistri"],

    # --- AGRICOLTURA & AMBIENTE ---
    "Agriculture": ["agriculture", "agricoltura", "farming", "coltivazione", "agronomia", "agronomy"],
    "Horticulture": ["horticulture", "orticoltura", "gardening", "giardinaggio", "landscaping", "verde"],
    "Animal Husbandry": ["animal husbandry", "allevamento", "livestock", "bestiame", "zootecnia"],
    "Veterinary": ["veterinary", "veterinario", "vet", "animal care", "cura animali"],
    "Organic Farming": ["organic", "biologico", "bio", "sustainable farming", "agricoltura sostenibile"],
    "Pest Control": ["pest control", "disinfestazione", "fumigation", "derattizzazione"],

    # --- MEDIA & COMUNICAZIONE ---
    "Journalism": ["journalism", "giornalismo", "journalist", "giornalista", "reporter", "cronista"],
    "Video Production": ["video production", "video editing", "montaggio video", "filmmaker", "premiere", "final cut", "davinci"],
    "Photography": ["photography", "fotografia", "photographer", "fotografo", "lightroom", "camera"],
    "Audio Production": ["audio production", "audio editing", "sound design", "podcast", "fonico", "pro tools", "audition"],
    "Broadcasting": ["broadcasting", "television broadcasting", "radio broadcasting", "tv station", "radio station", "televisione", "conduttore", "presenter", "on-air", "live broadcast", "studio televisivo"],

    "Press Relations": ["press relations", "ufficio stampa", "pr", "public relations", "media relations"],
    "Social Media Management": ["social media manager", "community manager", "content creator", "influencer", "content planning"],

    # --- SICUREZZA ---
    "Security Guard": ["security", "sicurezza", "security guard", "vigilante", "guardia giurata", "gpg"],
    "Surveillance": ["surveillance", "sorveglianza", "cctv", "videosorveglianza", "monitoring"],
    "Firefighting": ["firefighting", "vigile del fuoco", "firefighter", "pompiere", "antincendio"],
    "Emergency Response": ["emergency response", "pronto intervento", "crisis management", "gestione emergenze"],
    "Cybersecurity": ["cybersecurity", "sicurezza informatica", "information security", "penetration testing", "ethical hacking"],
    "Loss Prevention": ["loss prevention", "antitaccheggio", "theft prevention", "asset protection"],

    # --- SPORT & FITNESS ---
    "Personal Training": ["personal trainer", "personal training", "fitness trainer", "allenatore", "preparatore atletico"],
    "Group Fitness": ["group fitness", "fitness class", "aerobics", "zumba", "spinning", "pilates", "yoga instructor"],
    "Sports Coaching": ["coaching", "coach sportivo", "allenatore sportivo", "sport coach", "team coaching"],
    "Nutrition": ["nutrition", "nutrizione", "dietitian", "dietologo", "nutrizionista", "diet planning"],
    "Physical Education": ["physical education", "educazione fisica", "pe teacher", "motoria"],
    "Sports Management": ["sports management", "gestione sportiva", "club management", "sport marketing"],

    # --- IMMOBILIARE ---
    "Real Estate": ["real estate", "immobiliare", "property", "proprietà", "compravendita"],
    "Property Valuation": ["valuation", "valutazione immobiliare", "appraisal", "perizia", "stima"],
    "Leasing": ["leasing", "affitto", "rental", "locazione", "property management"],
    "Mortgage": ["mortgage", "mutuo", "loan", "finanziamento immobiliare"],
    "Real Estate Marketing": ["real estate marketing", "annunci immobiliari", "property listing", "home staging"],

    # --- ARTE & SPETTACOLO ---
    "Acting": ["acting", "recitazione", "actor", "attore", "attrice", "theatre", "teatro"],
    "Music Performance": ["music", "musica", "musician", "musicista", "singing", "canto", "vocalist"],
    "Dance": ["dance", "danza", "dancer", "ballerino", "ballerina", "choreography", "coreografia"],
    "Fine Arts": ["fine arts", "belle arti", "painting", "pittura", "sculpture", "scultura", "artist"],
    "Stage Production": ["stage production", "tecnico di palco", "lighting", "luci", "sound technician"],
    "Event Entertainment": ["dj", "disc jockey", "mc", "animatore", "entertainer", "animazione"],

    # --- PULIZIE & FACILITY ---
    "Cleaning": ["cleaning", "pulizie", "housekeeping", "sanitation", "igienizzazione", "addetto pulizie"],
    "Industrial Cleaning": ["industrial cleaning", "pulizie industriali", "sanificazione", "disinfection"],
    "Facility Management": ["facility management", "gestione immobili", "building maintenance", "manutenzione"],
    "Laundry": ["laundry", "lavanderia", "dry cleaning", "lavaggio", "stiratura", "ironing"],

    # --- CALL CENTER & CUSTOMER SUPPORT ---
    "Inbound Calls": ["inbound", "call center inbound", "customer support", "assistenza telefonica"],
    "Outbound Calls": ["outbound", "telemarketing", "telesales", "vendita telefonica", "cold calling"],
    "Live Chat Support": ["live chat", "chat support", "online support", "supporto online"],
    "Technical Support": ["technical support", "supporto tecnico", "help desk", "it support", "troubleshooting"],

    # --- MARITTIMO & NAUTICA ---
    "Navigation": ["navigation", "navigazione", "seamanship", "nautica", "maritime"],
    "Deck Operations": ["deck officer", "ufficiale di coperta", "able seaman", "marinaio"],
    "Marine Engineering": ["marine engineering", "ingegneria navale", "ship maintenance", "engine room"],
    "Port Operations": ["port operations", "operazioni portuali", "stevedoring", "cargo handling", "logistica portuale"],
    "Yacht Crew": ["yacht", "superyacht", "crew", "equipaggio", "hostess di bordo", "steward"],
    "Fishing": ["fishing", "pesca", "fisherman", "pescatore", "trawling"],

    # --- AVIAZIONE ---
    "Flight Operations": ["pilot", "pilota", "flight", "volo", "cockpit", "aviation"],
    "Cabin Crew": ["cabin crew", "flight attendant", "hostess di volo", "steward", "assistente di volo"],
    "Ground Handling": ["ground handling", "handling aeroportuale", "baggage", "rampa", "check-in agent"],
    "Air Traffic Control": ["air traffic control", "atc", "controllo traffico aereo", "torre di controllo"],
    "Aircraft Maintenance": ["aircraft maintenance", "manutenzione aeromobili", "aerospace", "avionics"],

    # --- TRASPORTI & MOBILITÀ ---
    "Public Transport": ["public transport", "trasporto pubblico", "bus driver", "autista bus", "tram"],
    "Rail Operations": ["rail", "ferrovia", "train", "treno", "capotreno", "macchinista"],
    "Taxi/Rideshare": ["taxi", "uber", "lyft", "ncc", "noleggio con conducente", "ride sharing"],
    "Fleet Management": ["fleet management", "gestione flotta", "vehicle tracking", "telematics"],
    "Traffic Management": ["traffic management", "gestione traffico", "traffic control", "viabilità"],

    # --- GAMING & ESPORTS ---
    "Game Development": ["game development", "sviluppo videogiochi", "unity", "unreal engine", "game design"],
    "Game Testing": ["game testing", "qa tester", "quality assurance games", "bug testing"],
    "Esports": ["esports", "professional gaming", "streaming", "twitch", "content gaming"],
    "Game Art": ["game art", "3d modeling", "character design", "environment art", "concept art"],

    # --- ENERGIA & AMBIENTE ---
    "Renewable Energy": ["renewable energy", "energie rinnovabili", "solar", "solare", "wind", "eolico", "fotovoltaico"],
    "Oil & Gas": ["oil", "gas", "petrolio", "petroleum", "drilling", "offshore"],
    "Power Grid": ["power grid", "rete elettrica", "grid management", "distribuzione energia"],
    "Energy Audit": ["energy audit", "audit energetico", "energy efficiency", "efficienza energetica"],
    "Environmental Science": ["environmental", "ambiente", "ecology", "ecologia", "sustainability", "sostenibilità"],
    "Waste Management": ["waste management", "gestione rifiuti", "recycling", "riciclaggio", "raccolta differenziata"],

    # --- MANIFATTURIERO & PRODUZIONE ---
    "Assembly Line": ["assembly", "assemblaggio", "production line", "linea di produzione", "manufacturing"],
    "Quality Control": ["quality control", "controllo qualità", "qc", "ispezione", "inspection"],
    "Process Engineering": ["process engineering", "ingegneria di processo", "lean manufacturing", "six sigma"],
    "Textile": ["textile", "tessile", "fabric", "tessuto", "weaving", "tessitura"],
    "Food Processing": ["food processing", "industria alimentare", "food production", "produzione alimentare"],
    "Packaging": ["packaging", "confezionamento", "imballaggio", "pack"],

    # --- PUBBLICA AMMINISTRAZIONE ---
    "Public Administration": ["public administration", "pubblica amministrazione", "pa", "government", "ente pubblico"],
    "Civil Service": ["civil service", "funzionario pubblico", "impiegato comunale", "statale"],
    "Urban Planning": ["urban planning", "urbanistica", "city planning", "pianificazione territoriale"],
    "Public Policy": ["public policy", "politiche pubbliche", "policy analysis", "legislazione"],
    "Diplomacy": ["diplomacy", "diplomazia", "ambassador", "ambasciatore", "foreign affairs", "esteri"],

    # --- RICERCA & ACCADEMIA ---
    "Academic Research": ["research", "ricerca", "researcher", "ricercatore", "publish", "pubblicazione"],
    "Laboratory Research": ["lab research", "ricerca laboratorio", "scientific research", "ricerca scientifica"],
    "Grant Writing": ["grant writing", "finanziamenti ricerca", "proposal writing", "bandi"],
    "Peer Review": ["peer review", "revisione paritaria", "academic review"],
    "University Teaching": ["university teaching", "docenza universitaria", "professor", "lecturer", "academic"],

    # --- SOCIALE & NON-PROFIT ---
    "Social Work": ["social work", "assistente sociale", "social worker", "servizi sociali"],
    "Community Outreach": ["community outreach", "outreach", "volontariato", "volunteer", "community service"],
    "Fundraising": ["fundraising", "raccolta fondi", "donor relations", "charity"],
    "NGO Management": ["ngo", "ong", "non-profit", "no-profit", "terzo settore"],
    "Counseling": ["counseling", "counselling", "consulenza psicologica", "supporto psicologico"],
    "Child Care": ["child care", "assistenza infanzia", "nanny", "tata", "babysitter", "educatrice"],

    # --- PSICOLOGIA & BENESSERE ---
    "Psychology": ["psychology", "psicologia", "psychologist", "psicologo", "psicologa", "therapy"],
    "Coaching": ["life coaching", "executive coaching", "career coaching", "business coaching"],
    "Meditation": ["meditation", "meditazione", "mindfulness", "wellness", "benessere"],

    # --- RELIGIOSO & SPIRITUALE ---
    "Religious Ministry": ["ministry", "ministero religioso", "pastor", "pastore", "priest", "prete", "parroco"],
    "Religious Education": ["catechism", "catechismo", "religious education", "educazione religiosa"],

    # --- CULTURALE & MUSEALE ---
    "Museum": ["museum", "museo", "curator", "curatore", "exhibition", "mostra"],
    "Archaeology": ["archaeology", "archeologia", "archaeologist", "archeologo", "excavation", "scavo"],
    "Conservation": ["conservation", "restauro", "restoration", "conservazione beni culturali"],
    "Library Science": ["library", "biblioteca", "librarian", "bibliotecario", "cataloging"],

    # --- INGEGNERIA ---
    "Civil Engineering": ["civil engineering", "ingegneria civile", "structural", "strutturale", "geotechnical", "geotecnica", "surveying", "topografia", "road design", "progettazione stradale", "bridge", "ponte", "dam", "diga"],
    "Mechanical Engineering": ["mechanical engineering", "ingegneria meccanica", "thermodynamics", "termodinamica", "fluid dynamics", "fluidodinamica", "mechanics", "meccanica", "fea", "finite element analysis"],
    "Chemical Engineering": ["chemical engineering", "ingegneria chimica", "process design", "reactor", "reattore", "distillation", "distillazione", "petrochemical", "petrolchimico"],
    "Electronic Engineering": ["electronic engineering", "ingegneria elettronica", "pcb", "printed circuit board", "microcontroller", "microcontrollore", "embedded systems", "sistemi embedded", "arduino", "raspberry pi", "fpga"],
    "Biomedical Engineering": ["biomedical engineering", "ingegneria biomedica", "prosthetics", "protesi", "medical imaging", "biomaterials", "biomateriali"],
    "Industrial Engineering": ["industrial engineering", "ingegneria gestionale", "operations research", "ricerca operativa", "lean", "six sigma", "kaizen", "production planning"],
    "Environmental Engineering": ["environmental engineering", "ingegneria ambientale", "water treatment", "trattamento acque", "wastewater", "acque reflue", "air quality", "qualità aria", "eia", "via"],

    # --- BIOTECH & FARMACEUTICO ---
    "Biotechnology": ["biotechnology", "biotecnologia", "biotech", "genetic engineering", "ingegneria genetica", "cloning", "clonazione", "bioreactor", "bioreattore"],
    "Molecular Biology": ["molecular biology", "biologia molecolare", "dna", "rna", "pcr", "gel electrophoresis", "elettroforesi", "sequencing", "sequenziamento"],
    "Microbiology": ["microbiology", "microbiologia", "bacteria", "batteri", "virus", "culture", "coltura", "sterilization", "sterilizzazione", "aseptic technique"],
    "Clinical Trials": ["clinical trials", "trial clinici", "gcp", "good clinical practice", "protocol", "protocollo", "cro", "phase i", "phase ii", "phase iii"],
    "Pharmaceutical Manufacturing": ["pharmaceutical manufacturing", "produzione farmaceutica", "gmp", "good manufacturing practice", "validation", "validazione", "clean room", "camera bianca", "batch record"],
    "Regulatory Affairs": ["regulatory affairs", "affari regolatori", "fda", "ema", "aifa", "drug approval", "approvazione farmaco", "dossier", "cth"],

    # --- TELECOMUNICAZIONI ---
    "Telecommunications": ["telecommunications", "telecomunicazioni", "telco", "telecom", "network", "rete", "fiber optic", "fibra ottica", "5g", "4g", "lte"],
    "Network Engineering": ["network engineering", "ingegneria di rete", "cisco", "juniper", "routing", "switching", "firewall", "vpn", "lan", "wan", "tcp/ip"],
    "Radio Frequency": ["radio frequency", "rf", "radiofrequenza", "antenna", "microwave", "microonde", "signal processing", "elaborazione segnali"],
    "Satellite": ["satellite", "satellite communication", "comunicazione satellitare", "gps", "gnss", "earth station", "stazione terrestre"],

    # --- ARCHITETTURA ---
    "Architecture": ["architecture", "architettura", "architect", "architetto", "building design", "progettazione edilizia", "facade", "facciata", "interior design", "arredamento"],
    "Landscape Architecture": ["landscape architecture", "architettura del paesaggio", "garden design", "progettazione giardini", "green spaces", "spazi verdi"],
    "Sustainable Design": ["sustainable design", "progettazione sostenibile", "leed", "green building", "bioedilizia", "passive house", "casa passiva", "nzeb"],
    "3D Visualization": ["3d visualization", "rendering architettonico", "archviz", "lumion", "vray", "enscape", "twinmotion"],

    # --- ODONTOIATRIA ---
    "Dentistry": ["dentistry", "odontoiatria", "dentist", "dentista", "dental hygiene", "igiene dentale", "oral surgery", "chirurgia orale"],
    "Dental Assistance": ["dental assistant", "assistente dentale", "chairside", "sterilization", "dental instruments", "strumentario odontoiatrico", "dental x-ray"],
    "Orthodontics": ["orthodontics", "ortodonzia", "braces", "apparecchio", "invisalign", "retainer", "bite"],
    "Prosthodontics": ["prosthodontics", "protesi dentaria", "crown", "corona", "bridge", "ponte dentale", "denture", "dentiera", "implant", "impianto"],

    # --- VETERINARIA AVANZATA ---
    "Veterinary Surgery": ["veterinary surgery", "chirurgia veterinaria", "spay", "sterilizzazione", "neuter", "castrazione", "orthopedic", "ortopedica"],
    "Animal Diagnostics": ["animal diagnostics", "diagnostica veterinaria", "blood panel", "esami sangue", "ultrasound", "ecografia", "x-ray", "radiografia"],
    "Exotic Animals": ["exotic animals", "animali esotici", "reptiles", "rettili", "birds", "uccelli", "small mammals", "piccoli mammiferi"],
    "Large Animals": ["large animals", "grandi animali", "equine", "equino", "bovine", "bovino", "livestock", "bestiame"],

    # --- CONSULENZA & MANAGEMENT ---
    "Management Consulting": ["management consulting", "consulenza gestionale", "consulente aziendale", "business transformation", "organizational change", "mckinsey", "bcg", "bain", "strategy consulting", "consulenza strategica"],

    "IT Consulting": ["it consulting", "consulenza it", "digital transformation", "trasformazione digitale", "system integration", "integrazione sistemi"],
    "HR Consulting": ["hr consulting", "consulenza hr", "talent management", "organizational design", "compensation", "retribuzione"],
    "Tax Consulting": ["tax consulting", "consulenza fiscale", "tax planning", "pianificazione fiscale", "transfer pricing", "tax audit"],

    # --- GIOIELLERIA & OROLOGERIA ---
    "Jewelry Making": ["jewelry", "gioielleria", "jeweler", "gioielliere", "goldsmith", "orefice", "gemstone", "pietra preziosa", "setting", "incastonatura"],
    "Watch Repair": ["watch repair", "riparazione orologi", "watchmaker", "orologiaio", "horology", "orologeria", "movement", "movimento", "caliber", "calibro"],
    "Gemology": ["gemology", "gemmologia", "diamond", "diamante", "certification", "certificazione", "gia", "grading"],

    # --- NAUTICA SPORTIVA ---
    "Sailing": ["sailing", "vela", "sailor", "velista", "regatta", "regata", "yacht racing", "cruising", "crociera"],
    "Boat Maintenance": ["boat maintenance", "manutenzione barca", "hull", "scafo", "rigging", "attrezzatura", "antifouling"],
    "Marine Navigation": ["marine navigation", "navigazione marittima", "chart", "carta nautica", "gps", "radar", "vhf"],
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
    "Media Planner": {
        "Media Planning", "Campaign Management", "Advertising", "Budgeting",
        "Google Analytics", "Marketing", "Excel", "Communication", "Negotiation",
        "Data Visualization", "Reporting", "Performance Marketing"
    },
    "Media Buyer": {
        "Media Planning", "Advertising", "Campaign Management", "Negotiation",
        "Budgeting", "Performance Marketing", "Google Analytics", "Communication"
    },
    "Programmatic Specialist": {
        "Media Planning", "Data Science", "Google Analytics", "Campaign Management",
        "Advertising", "A/B Testing", "Python", "SQL"
    },
    "Account Manager": {
        "Communication", "Customer Service", "Sales", "Project Management",
        "Negotiation", "Marketing", "CRM"
    },
    "Advertising Specialist": {
        "Advertising", "Campaign Management", "SEM", "Social Media",
        "Google Analytics", "Copywriting", "Marketing", "Performance Marketing"
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
    },
    
    # --- RISTORAZIONE ---
    "Chef": {
        "Cooking", "Kitchen Management", "Food Safety", "Pastry", "Teamwork", "Creativity"
    },
    "Waiter": {
        "Table Service", "Customer Service", "Communication", "Wine Knowledge", "English"
    },
    "Barista": {
        "Bartending", "Customer Service", "Communication", "Cash Handling"
    },
    "Pastry Chef": {
        "Pastry", "Cooking", "Food Safety", "Creativity", "Attention to Detail"
    },
    
    # --- HOSPITALITY & TURISMO ---
    "Hotel Receptionist": {
        "Reception", "Hospitality", "Customer Service", "English", "Communication", "Microsoft Office"
    },
    "Tour Guide": {
        "Tour Guide", "Communication", "English", "Customer Service", "Creativity"
    },
    "Event Planner": {
        "Event Planning", "Project Management", "Communication", "Budgeting", "Creativity"
    },
    "Housekeeping Manager": {
        "Housekeeping", "Leadership", "Organization", "Attention to Detail"
    },
    
    # --- SANITÀ ---
    "Nurse": {
        "Nursing", "First Aid", "Medical Devices", "Patient Care", "Teamwork", "Communication"
    },
    "Pharmacist": {
        "Pharmacy", "Customer Service", "Attention to Detail", "Communication"
    },
    "Physiotherapist": {
        "Physiotherapy", "Communication", "Empathy", "Problem Solving"
    },
    "OSS": {
        "Elderly Care", "Nursing", "First Aid", "Empathy", "Communication"
    },
    "Lab Technician": {
        "Laboratory", "Attention to Detail", "Medical Records"
    },
    
    # --- LEGALE ---
    "Lawyer": {
        "Legal Research", "Litigation", "Contract Law", "Communication", "Problem Solving"
    },
    "Paralegal": {
        "Paralegal", "Legal Research", "Contract Law", "Organization", "Microsoft Office"
    },
    "Compliance Officer": {
        "Compliance", "Legal Research", "Communication", "Attention to Detail"
    },
    
    # --- EDILIZIA & ARTIGIANATO ---
    "Electrician": {
        "Electrical", "Safety Compliance", "Problem Solving", "CAD Design"
    },
    "Plumber": {
        "Plumbing", "Safety Compliance", "Problem Solving"
    },
    "Construction Worker": {
        "Construction", "Masonry", "Safety Compliance", "Teamwork"
    },
    "Welder": {
        "Welding", "Safety Compliance", "Attention to Detail"
    },
    "Carpenter": {
        "Carpentry", "CAD Design", "Attention to Detail", "Creativity"
    },
    
    # --- MECCANICA ---
    "Mechanic": {
        "Automotive Repair", "Diagnostics", "Problem Solving"
    },
    "CNC Operator": {
        "CNC Machining", "CAD Design", "Attention to Detail"
    },
    
    # --- EDUCAZIONE ---
    "Teacher": {
        "Teaching", "Communication", "Curriculum Design", "Creativity", "Empathy"
    },
    "Trainer": {
        "Training", "Communication", "E-Learning", "Creativity"
    },
    "Tutor": {
        "Tutoring", "Teaching", "Communication", "Empathy"
    },
    
    # --- LOGISTICA ---
    "Warehouse Operator": {
        "Warehouse", "Forklift", "Inventory Management", "Order Management"
    },
    "Supply Chain Manager": {
        "Supply Chain", "Shipping", "Project Management", "Budgeting", "Excel"
    },
    "Delivery Driver": {
        "Delivery", "Customer Service", "Time Management"
    },
    
    # --- MODA & BEAUTY ---
    "Fashion Designer": {
        "Fashion Design", "Creativity", "Graphic Design", "Tailoring"
    },
    "Hairdresser": {
        "Hairdressing", "Customer Service", "Creativity", "Communication"
    },
    "Makeup Artist": {
        "Makeup", "Creativity", "Customer Service", "Attention to Detail"
    },
    "Aesthetician": {
        "Aesthetics", "Customer Service", "Communication"
    },
    
    # --- RETAIL ---
    "Sales Associate": {
        "Retail Sales", "Customer Service", "Communication", "Product Knowledge", "POS Systems"
    },
    "Store Manager": {
        "Retail Sales", "Leadership", "Inventory Management", "Budgeting", "Customer Service"
    },
    "Visual Merchandiser": {
        "Visual Merchandising", "Creativity", "Graphic Design", "Fashion Design"
    },
    
    # --- FINANZA ---
    "Accountant": {
        "Accounting", "Tax Preparation", "Excel", "Budgeting", "Financial Analysis"
    },
    "Financial Analyst": {
        "Financial Analysis", "Budgeting", "Excel", "Statistics", "Modeling"
    },
    "Payroll Specialist": {
        "Payroll", "Excel", "Attention to Detail", "Organization"
    },
    "Bank Teller": {
        "Banking", "Customer Service", "Cash Handling", "Communication"
    },
    "Insurance Agent": {
        "Insurance", "Sales", "Customer Service", "Communication"
    },
    
    # --- HR & ADMINISTRATION ---
    "HR Specialist": {
        "HR", "Communication", "Organization", "Empathy"
    },
    "Recruiter": {
        "HR", "Communication", "Negotiation", "Social Media"
    },
    "Administrative Assistant": {
        "Microsoft Office", "Data Entry", "Organization", "Communication", "Customer Service"
    },
    
    # --- TRADUZIONE ---
    "Translator": {
        "Translation", "CAT Tools", "English", "Attention to Detail"
    },
    
    # --- AGRICOLTURA ---
    "Farmer": {
        "Agriculture", "Organic Farming", "Animal Husbandry", "Teamwork"
    },
    "Agronomist": {
        "Agriculture", "Organic Farming", "Problem Solving", "Communication"
    },
    "Gardener": {
        "Horticulture", "Creativity", "Attention to Detail"
    },
    "Veterinarian": {
        "Veterinary", "Animal Husbandry", "Communication", "Empathy"
    },
    
    # --- MEDIA & COMUNICAZIONE ---
    "Journalist": {
        "Journalism", "Communication", "Copywriting", "English"
    },
    "Video Editor": {
        "Video Production", "Creativity", "Attention to Detail"
    },
    "Photographer": {
        "Photography", "Creativity", "Attention to Detail", "Customer Service"
    },
    "Social Media Manager": {
        "Social Media Management", "Social Media", "Copywriting", "Creativity", "Marketing"
    },
    "PR Specialist": {
        "Press Relations", "Communication", "Copywriting", "Marketing"
    },
    "Podcaster": {
        "Audio Production", "Communication", "Creativity"
    },
    
    # --- SICUREZZA ---
    "Security Officer": {
        "Security Guard", "Surveillance", "Emergency Response", "Communication"
    },
    "Firefighter": {
        "Firefighting", "First Aid", "Emergency Response", "Teamwork", "Stress Management"
    },
    "Cybersecurity Analyst": {
        "Cybersecurity", "Problem Solving", "Attention to Detail", "Python"
    },
    
    # --- SPORT & FITNESS ---
    "Personal Trainer": {
        "Personal Training", "Nutrition", "Communication", "Empathy"
    },
    "Fitness Instructor": {
        "Group Fitness", "Communication", "Empathy", "Creativity"
    },
    "Sports Coach": {
        "Sports Coaching", "Leadership", "Communication", "Teamwork"
    },
    "Nutritionist": {
        "Nutrition", "Communication", "Empathy", "Attention to Detail"
    },
    
    # --- IMMOBILIARE ---
    "Real Estate Agent": {
        "Real Estate", "Sales", "Negotiation", "Communication", "Real Estate Marketing"
    },
    "Property Manager": {
        "Leasing", "Customer Service", "Budgeting", "Communication"
    },
    "Appraiser": {
        "Property Valuation", "Real Estate", "Attention to Detail"
    },
    
    # --- ARTE & SPETTACOLO ---
    "Actor": {
        "Acting", "Communication", "Creativity", "Adaptability"
    },
    "Musician": {
        "Music Performance", "Creativity", "Teamwork"
    },
    "Dancer": {
        "Dance", "Creativity", "Teamwork", "Physical Education"
    },
    "DJ": {
        "Event Entertainment", "Creativity", "Communication"
    },
    "Stage Technician": {
        "Stage Production", "Attention to Detail", "Teamwork"
    },
    
    # --- PULIZIE & FACILITY ---
    "Cleaner": {
        "Cleaning", "Attention to Detail", "Time Management"
    },
    "Facility Manager": {
        "Facility Management", "Budgeting", "Leadership", "Problem Solving"
    },
    
    # --- CALL CENTER ---
    "Call Center Agent": {
        "Inbound Calls", "Customer Service", "Communication", "Problem Solving"
    },
    "Telemarketer": {
        "Outbound Calls", "Sales", "Communication", "Negotiation"
    },
    "Technical Support Specialist": {
        "Technical Support", "Problem Solving", "Communication", "Customer Service"
    },
    
    # --- MARITTIMO ---
    "Ship Captain": {
        "Navigation", "Deck Operations", "Leadership", "Safety Compliance"
    },
    "Yacht Stewardess": {
        "Yacht Crew", "Hospitality", "Customer Service", "English"
    },
    "Port Operator": {
        "Port Operations", "Warehouse", "Forklift", "Safety Compliance"
    },
    "Marine Engineer": {
        "Marine Engineering", "Problem Solving", "Safety Compliance"
    },
    
    # --- AVIAZIONE ---
    "Pilot": {
        "Flight Operations", "Leadership", "Stress Management", "English"
    },
    "Flight Attendant": {
        "Cabin Crew", "Customer Service", "First Aid", "English", "Communication"
    },
    "Ground Staff": {
        "Ground Handling", "Customer Service", "Communication", "Teamwork"
    },
    "Air Traffic Controller": {
        "Air Traffic Control", "Stress Management", "Communication", "English"
    },
    
    # --- TRASPORTI ---
    "Bus Driver": {
        "Public Transport", "Customer Service", "Time Management"
    },
    "Train Conductor": {
        "Rail Operations", "Customer Service", "Communication", "Safety Compliance"
    },
    "Fleet Manager": {
        "Fleet Management", "Budgeting", "Leadership", "Problem Solving"
    },
    
    # --- GAMING ---
    "Game Developer": {
        "Game Development", "JavaScript", "Creativity", "Problem Solving"
    },
    "Game Tester": {
        "Game Testing", "Attention to Detail", "Communication"
    },
    "Game Artist": {
        "Game Art", "Creativity", "Graphic Design"
    },
    "Esports Manager": {
        "Esports", "Marketing", "Social Media", "Communication"
    },
    
    # --- ENERGIA ---
    "Solar Technician": {
        "Renewable Energy", "Electrical", "Safety Compliance"
    },
    "Energy Auditor": {
        "Energy Audit", "Environmental Science", "Communication"
    },
    "Environmental Consultant": {
        "Environmental Science", "Communication", "Problem Solving", "Academic Research"
    },
    "Waste Manager": {
        "Waste Management", "Leadership", "Budgeting", "Safety Compliance"
    },
    
    # --- MANIFATTURIERO ---
    "Production Worker": {
        "Assembly Line", "Quality Control", "Teamwork", "Attention to Detail"
    },
    "Quality Inspector": {
        "Quality Control", "Attention to Detail", "Problem Solving"
    },
    "Process Engineer": {
        "Process Engineering", "Problem Solving", "Data Science"
    },
    "Packaging Operator": {
        "Packaging", "Assembly Line", "Attention to Detail"
    },
    
    # --- PUBBLICA AMMINISTRAZIONE ---
    "Civil Servant": {
        "Public Administration", "Civil Service", "Communication", "Microsoft Office"
    },
    "Urban Planner": {
        "Urban Planning", "CAD Design", "Communication", "Problem Solving"
    },
    "Policy Analyst": {
        "Public Policy", "Academic Research", "Communication", "Statistics"
    },
    "Diplomat": {
        "Diplomacy", "Communication", "Negotiation", "English"
    },
    
    # --- RICERCA ---
    "Research Scientist": {
        "Academic Research", "Laboratory Research", "Statistics", "Grant Writing"
    },
    "Research Assistant": {
        "Laboratory Research", "Academic Research", "Attention to Detail", "Organization"
    },
    "University Professor": {
        "University Teaching", "Academic Research", "Communication", "Grant Writing"
    },
    
    # --- SOCIALE ---
    "Social Worker": {
        "Social Work", "Counseling", "Empathy", "Communication"
    },
    "NGO Coordinator": {
        "NGO Management", "Fundraising", "Communication", "Project Management"
    },
    "Child Caregiver": {
        "Child Care", "Empathy", "Communication", "First Aid"
    },
    "Counselor": {
        "Counseling", "Psychology", "Communication", "Empathy"
    },
    
    # --- PSICOLOGIA ---
    "Psychologist": {
        "Psychology", "Communication", "Empathy", "Problem Solving"
    },
    "Life Coach": {
        "Coaching", "Communication", "Empathy", "Creativity"
    },
    "Wellness Coach": {
        "Meditation", "Coaching", "Communication", "Empathy"
    },
    
    # --- MUSEALE & CULTURALE ---
    "Museum Curator": {
        "Museum", "Communication", "Academic Research", "Creativity"
    },
    "Archaeologist": {
        "Archaeology", "Academic Research", "Attention to Detail"
    },
    "Restorer": {
        "Conservation", "Attention to Detail", "Creativity"
    },
    "Librarian": {
        "Library Science", "Organization", "Customer Service", "Attention to Detail"
    },
    
    # --- INGEGNERIA ---
    "Civil Engineer": {
        "Civil Engineering", "CAD Design", "Project Management", "Safety Compliance"
    },
    "Mechanical Engineer": {
        "Mechanical Engineering", "CAD Design", "Problem Solving"
    },
    "Chemical Engineer": {
        "Chemical Engineering", "Process Engineering", "Safety Compliance"
    },
    "Electronics Engineer": {
        "Electronic Engineering", "Problem Solving", "CAD Design"
    },
    "Biomedical Engineer": {
        "Biomedical Engineering", "Medical Devices", "Problem Solving"
    },
    "Environmental Engineer": {
        "Environmental Engineering", "Environmental Science", "Communication"
    },
    
    # --- BIOTECH & FARMACEUTICO ---
    "Biotechnologist": {
        "Biotechnology", "Molecular Biology", "Laboratory Research"
    },
    "Microbiologist": {
        "Microbiology", "Laboratory", "Attention to Detail"
    },
    "Clinical Research Associate": {
        "Clinical Trials", "Communication", "Organization", "English"
    },
    "Regulatory Affairs Specialist": {
        "Regulatory Affairs", "Communication", "Attention to Detail", "English"
    },
    "Pharmaceutical Technician": {
        "Pharmaceutical Manufacturing", "Quality Control", "Attention to Detail"
    },
    
    # --- TELECOMUNICAZIONI ---
    "Telecom Engineer": {
        "Telecommunications", "Network Engineering", "Problem Solving"
    },
    "Network Administrator": {
        "Network Engineering", "Cybersecurity", "Problem Solving"
    },
    "RF Engineer": {
        "Radio Frequency", "Electronic Engineering", "Problem Solving"
    },
    
    # --- ARCHITETTURA ---
    "Architect": {
        "Architecture", "CAD Design", "3D Visualization", "Creativity"
    },
    "Interior Designer": {
        "Architecture", "Creativity", "Customer Service", "3D Visualization"
    },
    "Landscape Architect": {
        "Landscape Architecture", "Horticulture", "CAD Design", "Creativity"
    },
    "BIM Specialist": {
        "CAD Design", "3D Visualization", "Architecture", "Attention to Detail"
    },
    
    # --- ODONTOIATRIA ---
    "Dentist": {
        "Dentistry", "Communication", "Customer Service", "Attention to Detail"
    },
    "Dental Hygienist": {
        "Dental Assistance", "Customer Service", "Communication"
    },
    "Orthodontist": {
        "Orthodontics", "Dentistry", "Communication", "Attention to Detail"
    },
    
    # --- VETERINARIA ---
    "Veterinary Surgeon": {
        "Veterinary Surgery", "Veterinary", "Animal Diagnostics", "Communication"
    },
    "Exotic Animal Vet": {
        "Exotic Animals", "Veterinary", "Communication"
    },
    "Equine Veterinarian": {
        "Large Animals", "Veterinary", "Communication"
    },
    
    # --- CONSULENZA ---
    "Management Consultant": {
        "Management Consulting", "Communication", "Problem Solving", "Statistics"
    },
    "IT Consultant": {
        "IT Consulting", "Problem Solving", "Communication", "Project Management"
    },
    "Tax Consultant": {
        "Tax Consulting", "Accounting", "Communication", "Attention to Detail"
    },
    
    # --- GIOIELLERIA ---
    "Jeweler": {
        "Jewelry Making", "Creativity", "Attention to Detail", "Customer Service"
    },
    "Watchmaker": {
        "Watch Repair", "Attention to Detail", "Problem Solving"
    },
    "Gemologist": {
        "Gemology", "Attention to Detail", "Customer Service"
    },
    
    # --- NAUTICA ---
    "Sailing Instructor": {
        "Sailing", "Teaching", "Communication", "First Aid"
    },
    "Boat Captain": {
        "Marine Navigation", "Navigation", "Leadership", "Safety Compliance"
    },
    "Marine Mechanic": {
        "Boat Maintenance", "Marine Engineering", "Problem Solving"
    }
}

