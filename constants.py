"""
================================================================================
CareerMatch AI - Knowledge Base (constants.py)
================================================================================

Universal skill database covering all major industries and career paths.
Suitable for graduates from any Italian university degree program.

================================================================================
"""

# =============================================================================
# ML_MODELS - Modelli ML del Corso (6 selezionati)
# =============================================================================
# Reference: DATA MINING E TEXT.txt - Corso Data Mining & Text Analytics
ML_MODELS = {
    "TF-IDF": {
        "type": "Feature Extraction",
        "desc": "Trasforma testo in Vector Space Model (TF × IDF)",
        "ref": "Text Mining, Word Vector Representation"
    },
    "Random Forest": {
        "type": "Classification (Supervised)",
        "desc": "Ensemble di Decision Trees con majority voting",
        "ref": "Classification and Regression"
    },
    "K-Means": {
        "type": "Clustering (Unsupervised)",
        "desc": "Partitioning: assegna punti → ricalcola centroidi → ripeti",
        "ref": "Clustering Techniques"
    },
    "Hierarchical Clustering": {
        "type": "Clustering (Unsupervised)", 
        "desc": "Agglomerativo bottom-up con Ward linkage → dendrogramma",
        "ref": "Hierarchical Clustering"
    },
    "LDA": {
        "type": "Topic Modeling (Unsupervised)",
        "desc": "Modello generativo: documento = mixture di topic",
        "ref": "Topic Model"
    },
    "NER": {
        "type": "Information Extraction",
        "desc": "Estrae entità nominate (ORG, PERSON, LOC, DATE)",
        "ref": "Named Entity Recognition"
    }
}

# =============================================================================
# INFERENCE RULES (Skill Relationships)
# =============================================================================
# When a user has Skill A, they likely also have competency in related skills
INFERENCE_RULES = {
    # --- TECHNOLOGY ---
    "Python": ["Programming", "Data Analysis", "Scripting", "Automation"],
    "JavaScript": ["Programming", "Web Development", "Frontend"],
    "Java": ["Programming", "Backend Development", "OOP"],
    "SQL": ["Database Management", "Data Analysis", "Data Querying"],
    "Excel": ["Data Analysis", "Spreadsheets", "Reporting", "Financial Modeling"],
    "Power BI": ["Data Visualization", "Business Intelligence", "Reporting"],
    "Tableau": ["Data Visualization", "Business Intelligence", "Analytics"],
    "Google Analytics": ["Web Analytics", "Digital Marketing", "Data Analysis"],
    "SAP": ["ERP", "Enterprise Systems", "Business Processes"],
    "Salesforce": ["CRM", "Sales Management", "Customer Relations"],
    "HubSpot": ["CRM", "Marketing Automation", "Inbound Marketing"],
    "AWS": ["Cloud Computing", "Infrastructure", "DevOps"],
    "Azure": ["Cloud Computing", "Infrastructure", "Enterprise IT"],
    "Docker": ["DevOps", "Containerization", "Deployment"],
    "Figma": ["UI Design", "UX Design", "Prototyping", "Visual Design"],
    "Adobe Photoshop": ["Graphic Design", "Image Editing", "Visual Design"],
    "Adobe Illustrator": ["Graphic Design", "Vector Design", "Branding"],
    "AutoCAD": ["Technical Drawing", "Engineering Design", "CAD"],
    "MATLAB": ["Engineering", "Data Analysis", "Scientific Computing"],
    
    # --- BUSINESS ---
    "Project Management": ["Planning", "Organization", "Leadership", "Stakeholder Management"],
    "Agile": ["Scrum", "Sprint Planning", "Iterative Development"],
    "Scrum": ["Agile", "Team Collaboration", "Project Management"],
    "Financial Analysis": ["Excel", "Reporting", "Business Analysis"],
    "Accounting": ["Financial Reporting", "Bookkeeping", "Tax"],
    "Marketing": ["Communication", "Strategy", "Brand Management"],
    "Digital Marketing": ["SEO", "Social Media", "Content Marketing", "Analytics"],
    "Sales": ["Negotiation", "Customer Relations", "Communication"],
    
    # --- LANGUAGES ---
    "English (C1)": ["English", "International Communication", "Business English"],
    "English (B2)": ["English", "Professional Communication"],
    "French": ["Languages", "International Business"],
    "German": ["Languages", "International Business"],
    "Spanish": ["Languages", "International Business"],
    "Chinese": ["Languages", "International Trade", "Asia Business"],
    
    # --- SCIENCE & QUALITY ---
    "GMP": ["ISO Standards", "Quality Control", "Quality Assurance", "Compliance", "Quality Management"],
    "GLP": ["ISO Standards", "Quality Control", "Quality Assurance", "Lab Safety", "Quality Management"],
    "Data Analysis": ["Statistics", "Excel", "Reporting"],
    "Biotechnology": ["Biology", "Chemistry", "Life Sciences", "Lab Skills", "Microbiology"],
    "Microbiology": ["Biology", "Lab Skills", "Quality Control"],
    "Molecular Biology": ["Biology", "Genetics", "Lab Skills"],
    "Spectrophotometry": ["Analytical Chemistry", "Lab Skills"],
    "Western Blot": ["Biology", "Lab Skills", "Molecular Biology"],
    "HPLC": ["Analytical Chemistry", "Lab Skills", "Quality Control"],
    "PCR": ["Molecular Biology", "Lab Skills"],
}

# =============================================================================
# SKILL CLUSTERS (Equivalent/Transferable Skills)
# =============================================================================
# Skills within same cluster are considered transferable
SKILL_CLUSTERS = {
    # BI & Visualization Tools
    "BI Tools": {"Tableau", "Power BI", "Looker", "Looker Studio", "QlikView", "Metabase", "Data Studio", "Google Data Studio"},
    
    # Analytics Platforms  
    "Analytics Platforms": {"Google Analytics", "GA4", "Adobe Analytics", "Mixpanel", "Amplitude", "Hotjar", "Matomo"},
    
    # Cloud Providers
    "Cloud Platforms": {"AWS", "Azure", "GCP", "Google Cloud", "IBM Cloud", "Oracle Cloud"},
    
    # CRM Systems
    "CRM Systems": {"Salesforce", "HubSpot", "Zoho CRM", "Pipedrive", "Microsoft Dynamics", "SAP CRM", "Oracle CRM"},
    
    # Design Tools
    "Design Software": {"Figma", "Sketch", "Adobe XD", "InVision", "Canva", "Miro"},
    
    # Adobe Suite
    "Adobe Products": {"Photoshop", "Illustrator", "InDesign", "Premiere Pro", "After Effects", "Lightroom", "Adobe Creative Suite"},
    
    # Project Management Tools
    "PM Tools": {"Jira", "Asana", "Trello", "Monday.com", "Notion", "ClickUp", "Basecamp", "MS Project"},
    
    # Office Suites
    "Office Software": {"Microsoft Office", "Google Workspace", "LibreOffice", "iWork"},
    
    # ERP Systems
    "ERP Systems": {"SAP", "Oracle ERP", "Microsoft Dynamics", "Odoo", "NetSuite"},
    
    # E-commerce Platforms
    "E-commerce": {"Shopify", "WooCommerce", "Magento", "PrestaShop", "BigCommerce"},
    
    # Email Marketing
    "Email Platforms": {"Mailchimp", "SendGrid", "Klaviyo", "ActiveCampaign", "Sendinblue", "HubSpot Email"},
    
    # Social Media
    "Social Platforms": {"Facebook", "Instagram", "LinkedIn", "TikTok", "Twitter", "YouTube", "Pinterest"},
    
    # Video Conferencing
    "Video Tools": {"Zoom", "Teams", "Google Meet", "Webex", "Skype"},
    
    # Programming Languages
    "Programming": {"Python", "Java", "JavaScript", "C#", "C++", "Ruby", "PHP", "Go", "Swift", "Kotlin"},
    
    # Databases
    "Databases": {"MySQL", "PostgreSQL", "MongoDB", "Oracle", "SQL Server", "SQLite", "Redis", "Cassandra"},
}

# =============================================================================
# PROJECT BASED SKILLS (Demonstrated through portfolio/projects)
# =============================================================================
PROJECT_BASED_SKILLS = {
    # Technical
    "Programming", "Web Development", "App Development", "Software Development",
    "Machine Learning", "Data Science", "Data Analysis",
    # Creative
    "Graphic Design", "UI Design", "UX Design", "Video Production", "Photography",
    "Writing", "Copywriting", "Content Creation",
    # Research
    "Research", "Academic Research", "Market Research",
    # Business
    "Business Development", "Entrepreneurship", "Consulting",
}

# =============================================================================
# HARD SKILLS (Technical/Measurable Skills)
# =============================================================================
HARD_SKILLS = {
    # ========== TECHNOLOGY & IT ==========
    "Programming": ["programming", "coding", "sviluppo software", "programmazione"],
    "Python": ["python", "py", "pandas", "numpy", "django", "flask"],
    "JavaScript": ["javascript", "js", "node", "react", "vue", "angular", "typescript"],
    "Java": ["java", "spring", "spring boot", "j2ee", "maven"],
    "C#": ["c#", "csharp", ".net", "dotnet", "asp.net"],
    "SQL": ["sql", "mysql", "postgresql", "database", "query", "oracle sql"],
    "HTML": ["html", "html5", "markup", "web structure"],
    "CSS": ["css", "css3", "sass", "scss", "tailwind", "bootstrap"],
    "Git": ["git", "github", "gitlab", "bitbucket", "version control"],
    "APIs": ["api", "rest", "restful", "graphql", "web services", "soap"],
    "Cloud Computing": ["cloud", "aws", "azure", "gcp", "google cloud", "cloud computing"],
    "DevOps": ["devops", "ci/cd", "jenkins", "docker", "kubernetes", "deployment"],
    "Cybersecurity": ["cybersecurity", "security", "information security", "sicurezza informatica"],
    "Networking": ["networking", "network administration", "tcp/ip", "lan/wan"],
    "IT Support": ["it support", "technical support", "helpdesk", "troubleshooting"],
    
    # ========== DATA & ANALYTICS ==========
    "Data Analysis": ["data analysis", "analisi dati", "data analytics", "analytics"],
    "Data Visualization": ["data visualization", "visualizzazione dati", "dashboard", "charts"],
    "Statistics": ["statistics", "statistica", "statistical analysis", "analisi statistica"],
    "Machine Learning": ["machine learning", "ml", "artificial intelligence", "deep learning"],
    "Excel": ["excel", "spreadsheet", "pivot tables", "vlookup", "foglio elettronico"],
    "Power BI": ["power bi", "powerbi", "microsoft power bi"],
    "Tableau": ["tableau", "tableau desktop", "tableau server"],
    "Google Analytics": ["google analytics", "ga4", "ga", "web analytics"],
    "BigQuery": ["bigquery", "big query", "google bigquery"],
    "R": ["r programming", "r language", "rstudio", "r statistics"],
    "SPSS": ["spss", "ibm spss", "statistical software"],
    "Business Intelligence": ["business intelligence", "bi", "intelligence aziendale"],
    "Reporting": ["reporting", "report", "analisi report", "business reporting"],
    
    # ========== MARKETING & DIGITAL ==========
    "Marketing": ["marketing", "marketing strategy", "strategia marketing"],
    "Digital Marketing": ["digital marketing", "marketing digitale", "online marketing"],
    "SEO": ["seo", "search engine optimization", "ottimizzazione motori ricerca", "organic"],
    "SEM": ["sem", "search engine marketing", "ppc", "pay per click", "paid search"],
    "Social Media Marketing": ["social media marketing", "smm", "social media", "social marketing"],
    "Content Marketing": ["content marketing", "content strategy", "contenuti", "blogging"],
    "Email Marketing": ["email marketing", "newsletter", "dem", "email campaigns", "mailchimp"],
    "Google Ads": ["google ads", "adwords", "google advertising", "search ads"],
    "Facebook Ads": ["facebook ads", "meta ads", "instagram ads", "social ads"],
    "Influencer Marketing": ["influencer marketing", "influencer", "creator marketing"],
    "Brand Management": ["brand management", "gestione brand", "branding", "brand strategy"],
    "Market Research": ["market research", "ricerche di mercato", "market analysis"],
    "CRM": ["crm", "customer relationship", "salesforce", "hubspot", "gestione clienti"],
    "Marketing Automation": ["marketing automation", "automazione marketing", "hubspot", "marketo"],
    "Copywriting": ["copywriting", "copy", "scrittura persuasiva", "advertising copy"],
    "Public Relations": ["public relations", "pr", "relazioni pubbliche", "media relations"],
    "Event Marketing": ["event marketing", "eventi", "event planning"],
    
    # ========== BUSINESS & MANAGEMENT ==========
    "Project Management": ["project management", "gestione progetti", "pm", "project manager"],
    "Agile": ["agile", "agile methodology", "metodologia agile", "agile project"],
    "Scrum": ["scrum", "scrum master", "sprint", "scrum framework"],
    "Business Analysis": ["business analysis", "analisi business", "business analyst", "ba"],
    "Strategic Planning": ["strategic planning", "pianificazione strategica", "strategy"],
    "Operations Management": ["operations management", "direzione operativa"],
    "Process Improvement": ["process improvement", "ottimizzazione processi", "bpm"],
    "Change Management": ["change management", "gestione del cambiamento", "change"],
    "Stakeholder Management": ["stakeholder management", "gestione stakeholder"],
    "Risk Management": ["risk management", "gestione rischi", "risk assessment"],
    "Quality Management": ["quality management", "gestione qualità", "iso", "quality"],
    "Lean": ["lean", "lean management", "lean manufacturing", "lean thinking"],
    "Six Sigma": ["six sigma", "6 sigma", "dmaic", "process excellence"],
    "KPI Management": ["kpi", "key performance indicators", "metrics", "performance"],
    "Budgeting": ["budgeting", "budget", "pianificazione budget", "budget management"],
    "Presentation": ["presentation", "presentazioni", "powerpoint", "public speaking"],
    "Negotiation": ["negotiation", "negoziazione", "trattativa", "contrattazione"],
    "Leadership": ["leadership", "team leadership", "people management", "gestione team"],
    
    # ========== FINANCE & ACCOUNTING ==========
    "Financial Analysis": ["financial analysis", "analisi finanziaria", "finance analysis"],
    "Accounting": ["accounting", "contabilità", "ragioneria", "bookkeeping"],
    "Financial Reporting": ["financial reporting", "bilancio", "financial statements"],
    "Budgeting and Forecasting": ["forecasting", "previsioni", "budget forecasting"],
    "Auditing": ["auditing", "revisione contabile", "audit", "internal audit"],
    "Tax": ["tax", "fiscale", "taxation", "imposte", "dichiarazioni fiscali"],
    "Financial Modeling": ["financial modeling", "modellazione finanziaria", "dcf"],
    "Valuation": ["valuation", "valutazione aziendale", "company valuation"],
    "Treasury": ["treasury", "tesoreria", "cash management"],
    "Credit Analysis": ["credit analysis", "analisi credito", "credit risk"],
    "Investment Analysis": ["investment analysis", "analisi investimenti", "portfolio"],
    "SAP": ["sap", "sap erp", "sap fi", "sap co", "sap mm", "sap sd"],
    "Oracle Financials": ["oracle", "oracle financials", "oracle erp"],
    "Bloomberg": ["bloomberg", "bloomberg terminal", "financial data"],
    
    # ========== HUMAN RESOURCES ==========
    "Recruiting": ["recruiting", "recruitment", "selezione", "talent acquisition", "hiring"],
    "HR Management": ["hr", "human resources", "risorse umane", "hr management"],
    "Talent Management": ["talent management", "gestione talenti", "talent development"],
    "Training & Development": ["training delivery", "formazione personale", "learning development", "l&d"],
    "Performance Management": ["performance management", "valutazione performance", "appraisal"],
    "Compensation & Benefits": ["compensation", "retribuzione", "benefits", "total rewards"],
    "Labor Law": ["labor law", "diritto del lavoro", "contrattualistica", "ccnl"],
    "HR Analytics": ["hr analytics", "people analytics", "workforce analytics"],
    "Employer Branding": ["employer branding", "talent attraction", "recruiting marketing"],
    "Onboarding": ["onboarding", "inserimento", "new hire", "induction"],
    "HRIS": ["hris", "hr information system", "workday", "successfactors"],
    
    # ========== SALES & COMMERCIAL ==========
    "Sales": ["sales", "vendita", "vendite", "commerciale", "selling"],
    "B2B Sales": ["b2b", "business to business", "enterprise sales", "corporate sales"],
    "B2C Sales": ["b2c", "business to consumer", "retail sales", "consumer sales"],
    "Account Management": ["account management", "gestione clienti", "key account"],
    "Business Development": ["business development", "sviluppo business", "biz dev"],
    "Lead Generation": ["lead generation", "lead gen", "prospecting", "pipeline"],
    "Sales Management": ["sales management", "direzione vendite", "sales leadership"],
    "Customer Success": ["customer success", "cs", "customer satisfaction", "retention"],
    "Inside Sales": ["inside sales", "telesales", "remote selling"],
    "Field Sales": ["field sales", "outside sales", "vendita esterna"],
    "Retail": ["retail", "vendita al dettaglio", "store management", "negozio"],
    "E-commerce": ["e-commerce", "ecommerce", "online sales", "vendita online"],
    
    # ========== LEGAL ==========
    "Contract Law": ["contract law", "contrattualistica", "contratti", "legal contracts"],
    "Corporate Law": ["corporate law", "diritto societario", "company law"],
    "Labor Law (Legal)": ["diritto del lavoro", "employment law", "giuslavoristico"],
    "Compliance": ["compliance", "conformità normativa", "regulatory compliance"],
    "GDPR": ["gdpr", "data protection", "protezione dati", "regolamento europeo privacy"],
    "Intellectual Property": ["intellectual property", "ip", "proprietà intellettuale", "brevetti"],
    "M&A": ["m&a", "mergers acquisitions", "fusioni acquisizioni", "corporate transactions"],
    "Legal Research": ["legal research", "ricerca giuridica", "giurisprudenza"],
    "Due Diligence": ["due diligence", "analisi due diligence", "dd"],
    "Litigation": ["litigation", "contenzioso", "dispute", "cause legali"],
    
    # ========== DESIGN & CREATIVE ==========
    "Graphic Design": ["graphic design", "grafica", "design grafico", "visual design"],
    "UI Design": ["ui design", "user interface", "interfaccia utente", "interface design"],
    "UX Design": ["ux design", "user experience", "esperienza utente", "ux research"],
    "Web Design": ["web design", "website design", "design siti web"],
    "Adobe Creative Suite": ["adobe", "photoshop", "illustrator", "indesign", "premiere", "after effects"],
    "Figma": ["figma", "figma design"],
    "Sketch": ["sketch", "sketch app"],
    "InDesign": ["indesign", "adobe indesign", "impaginazione", "layout"],
    "Video Editing": ["video editing", "montaggio video", "premiere pro", "final cut"],
    "Motion Graphics": ["motion graphics", "after effects", "animazione"],
    "Photography": ["photography", "fotografia", "photo editing", "lightroom"],
    "3D Modeling": ["3d modeling", "modellazione 3d", "blender", "maya", "3ds max"],
    "Branding": ["branding", "brand identity", "identità visiva", "logo design"],
    "Typography": ["typography", "tipografia", "fonts", "lettering"],
    
    # ========== ENGINEERING ==========
    "Mechanical Engineering": ["mechanical engineering", "ingegneria meccanica", "meccanica"],
    "Electrical Engineering": ["electrical engineering", "ingegneria elettrica", "elettrotecnica"],
    "Civil Engineering": ["civil engineering", "ingegneria civile", "costruzioni"],
    "Industrial Engineering": ["industrial engineering", "ingegneria gestionale", "industriale"],
    "Chemical Engineering": ["chemical engineering", "ingegneria chimica", "impianti chimici"],
    "AutoCAD": ["autocad", "cad", "computer aided design", "disegno tecnico"],
    "SolidWorks": ["solidworks", "solid works", "3d cad"],
    "MATLAB": ["matlab", "simulink", "scientific computing"],
    "PLC Programming": ["plc", "programmazione plc", "automazione industriale"],
    "Quality Control": ["quality control", "qc", "controllo qualità", "ispezione"],
    "Manufacturing": ["manufacturing", "produzione", "fabbricazione", "processo produttivo"],
    "Maintenance": ["maintenance", "manutenzione", "maintenance management"],
    "HSE": ["hse", "health safety environment", "sicurezza lavoro", "ambiente"],
    "ISO Standards": ["iso", "iso 9001", "iso 14001", "iso 45001", "certificazioni"],
    
    # ========== SUPPLY CHAIN & LOGISTICS ==========
    "Supply Chain Management": ["supply chain", "catena fornitura", "supply chain management"],
    "Logistics": ["logistics", "logistica", "trasporti", "distribuzione"],
    "Procurement": ["procurement", "acquisti", "purchasing", "approvvigionamento"],
    "Inventory Management": ["inventory", "magazzino", "stock management", "inventario"],
    "Warehouse Management": ["warehouse", "gestione magazzino", "wms", "logistica magazzino"],
    "Transportation": ["transportation", "trasporto", "spedizioni", "shipping"],
    "Import/Export": ["import export", "commercio estero", "customs", "dogana"],
    "Demand Planning": ["demand planning", "pianificazione domanda", "forecasting"],
    "Vendor Management": ["vendor management", "gestione fornitori", "supplier"],
    
    # ========== SCIENCE & LAB ==========
    "Biology": ["biology", "biologia", "biological sciences", "scienze biologiche"],
    "Chemistry": ["chemistry", "chimica", "chemical science", "scienze chimiche"],
    "Biotechnology": ["biotechnology", "biotecnologie", "biotech"],
    "Microbiology": ["microbiology", "microbiologia", "microbiological analysis"],
    "Molecular Biology": ["molecular biology", "biologia molecolare"],
    "PCR": ["pcr", "qpcr", "polymerase chain reaction"],
    "HPLC": ["hplc", "chromatography", "cromatografia", "liquid chromatography"],
    "Gascromatography": ["gascromatografia", "gas chromatography", "gc-ms"],
    "Cell Culture": ["cell culture", "colture cellulari", "cell lines"],
    "ELISA": ["elisa", "immunoassays", "saggi immunoenzimatici"],
    "Western Blot": ["western blot", "protein analysis", "analisi proteica"],
    "Spectrophotometry": ["spectrophotometry", "spettrofotometria", "spettrofotometro"],
    "Lab Safety": ["lab safety", "sicurezza laboratorio", "glp", "good laboratory practice"],
    "GMP": ["gmp", "good manufacturing practice", "norme di buona fabbricazione"],
    "Analytical Chemistry": ["analytical chemistry", "chimica analitica", "analisi chimiche"],
    
    # ========== HEALTHCARE & PHARMA ==========
    "Clinical Research": ["clinical research", "ricerca clinica", "studi clinici"],
    "GCP": ["gcp", "good clinical practice", "buone pratiche cliniche"],
    "Medical Writing": ["medical writing", "scrittura medica", "regulatory"],
    "Pharmacovigilance": ["pharmacovigilance", "farmacovigilanza", "drug safety"],
    "Regulatory Affairs": ["regulatory affairs", "affari regolatori", "ema", "aifa"],
    "Healthcare Administration": ["healthcare admin", "amministrazione sanitaria"],
    "Medical Sales": ["medical sales", "informazione scientifica", "pharma sales"],
    "Nursing": ["nursing", "infermieristica", "assistenza infermieristica"],
    "Patient Care": ["patient care", "assistenza pazienti", "cura paziente"],
    
    # ========== HOSPITALITY & TOURISM ==========
    "Hotel Management": ["hotel management", "gestione alberghiera", "hospitality"],
    "Front Office": ["front office", "reception", "accoglienza"],
    "F&B Management": ["f&b", "food beverage", "ristorazione", "restaurant"],
    "Event Management": ["event management", "organizzazione eventi", "eventi"],
    "Tourism": ["tourism", "turismo", "tour operator", "travel"],
    "Revenue Management": ["revenue management", "yield management", "pricing"],
    "Customer Service": ["customer service", "servizio clienti", "assistenza clienti"],
    "Reservation Systems": ["reservation", "prenotazioni", "booking", "amadeus", "opera"],
    "Concierge": ["concierge", "guest relations", "guest services"],
    
    # ========== EDUCATION & RESEARCH ==========
    "Teaching": ["teaching", "insegnamento", "docenza", "didattica"],
    "Curriculum Development": ["curriculum development", "sviluppo programmi", "instructional design"],
    "Research": ["research", "ricerca", "academic research", "ricerca scientifica"],
    "Academic Writing": ["academic writing", "scrittura accademica", "pubblicazioni"],
    "E-Learning": ["e-learning", "online learning", "formazione online", "lms"],
    "Tutoring": ["tutoring", "tutoraggio", "ripetizioni"],
    "Training Delivery": ["training delivery", "erogazione formazione"],
    
    # ========== LANGUAGES ==========
    "English (Native)": ["english native", "inglese madrelingua", "native english"],
    "English (C2)": ["english c2", "inglese c2", "fluent english", "inglese fluente"],
    "English (C1)": ["english c1", "inglese c1", "advanced english", "inglese avanzato"],
    "English (B2)": ["english b2", "inglese b2", "upper intermediate", "inglese intermedio alto"],
    "English (B1)": ["english b1", "inglese b1", "intermediate english", "inglese intermedio"],
    "Italian": ["italian", "italiano", "lingua italiana"],
    "French": ["french", "francese", "français", "lingua francese"],
    "German": ["german", "tedesco", "deutsch", "lingua tedesca"],
    "Spanish": ["spanish", "spagnolo", "español", "lingua spagnola"],
    "Portuguese": ["portuguese", "portoghese", "português"],
    "Chinese": ["chinese", "cinese", "mandarin", "mandarino", "中文"],
    "Arabic": ["arabic", "arabo", "العربية"],
    "Russian": ["russian", "russo", "русский"],
    "Japanese": ["japanese", "giapponese", "日本語"],
    
    # ========== TOOLS & SOFTWARE ==========
    "Microsoft Office": ["microsoft office", "ms office", "office 365", "word excel powerpoint"],
    "Google Workspace": ["google workspace", "g suite", "google docs", "google sheets"],
    "Slack": ["slack", "team messaging", "comunicazione team"],
    "Microsoft Teams": ["microsoft teams", "ms teams", "teams software"],
    "Zoom": ["zoom", "video conferencing", "webinar"],
    "Jira": ["jira", "atlassian jira", "issue tracking"],
    "Confluence": ["confluence", "atlassian confluence", "documentation"],
    "Notion": ["notion", "knowledge management", "wiki"],
    "Monday.com": ["monday", "monday.com", "project tracking"],
    "Asana": ["asana", "task management"],
    "Trello": ["trello", "kanban board"],
}

# =============================================================================
# SOFT SKILLS
# =============================================================================
SOFT_SKILLS = {
    # Communication
    "Communication": ["communication", "comunicazione", "communicating", "verbal communication"],
    "Written Communication": ["written communication", "comunicazione scritta", "writing skills"],
    "Presentation Skills": ["presentation", "presentazione", "public speaking", "presenting"],
    "Active Listening": ["active listening", "ascolto attivo", "listening"],
    
    # Teamwork & Leadership
    "Teamwork": ["teamwork", "lavoro di squadra", "team player", "collaboration", "collaborazione"],
    "Leadership": ["leadership", "guida team", "team leading", "people management"],
    "Mentoring": ["mentoring", "coaching", "sviluppo persone"],
    "Conflict Resolution": ["conflict resolution", "risoluzione conflitti", "mediation"],
    
    # Analytical & Problem Solving
    "Problem Solving": ["problem solving", "risoluzione problemi", "solving problems"],
    "Critical Thinking": ["critical thinking", "pensiero critico", "analytical thinking"],
    "Decision Making": ["decision making", "processo decisionale", "decision-making"],
    "Analytical Skills": ["analytical", "analitico", "analysis skills"],
    
    # Personal Effectiveness
    "Time Management": ["time management", "gestione tempo", "organizzazione tempo"],
    "Organization": ["organization", "organizzazione", "organizational skills"],
    "Prioritization": ["prioritization", "priorità", "prioritizing"],
    "Multitasking": ["multitasking", "multitask", "multi-tasking"],
    "Attention to Detail": ["attention to detail", "attenzione dettagli", "precisione", "accuracy"],
    "Self-Motivation": ["self-motivation", "auto-motivazione", "proattività", "initiative"],
    
    # Adaptability
    "Adaptability": ["adaptability", "adattabilità", "flexibility", "flessibilità"],
    "Resilience": ["resilience", "resilienza", "stress management"],
    "Learning Agility": ["learning agility", "apprendimento rapido", "quick learner"],
    "Open-Mindedness": ["open-minded", "apertura mentale", "open to feedback"],
    
    # Creativity & Innovation
    "Creativity": ["creativity", "creatività", "creative thinking", "innovation"],
    "Innovation": ["innovation", "innovazione", "innovative thinking"],
    "Strategic Thinking": ["strategic thinking", "pensiero strategico", "vision"],
    
    # Interpersonal
    "Interpersonal Skills": ["interpersonal", "relazionale", "people skills"],
    "Empathy": ["empathy", "empatia", "emotional intelligence", "eq"],
    "Customer Focus": ["customer focus", "orientamento cliente", "customer-oriented"],
    "Networking": ["networking", "relazioni professionali", "professional network"],
    "Negotiation": ["negotiation", "negoziazione", "persuasion"],
    
    # Work Ethics
    "Work Ethics": ["work ethics", "etica lavorativa", "professionalism"],
    "Reliability": ["reliability", "affidabilità", "dependable"],
    "Integrity": ["integrity", "integrità", "honesty", "ethics"],
    "Accountability": ["accountability", "responsabilità", "ownership"],
}

# =============================================================================
# JOB ARCHETYPES (For Career Compass)
# =============================================================================
# Comprehensive list covering all major career paths
JOB_ARCHETYPES = {
    # ========== TECHNOLOGY ==========
    "Software Developer": {"Programming", "Git", "SQL", "APIs", "Problem Solving"},
    "Frontend Developer": {"JavaScript", "HTML", "CSS", "UI Design", "Git"},
    "Backend Developer": {"Python", "SQL", "APIs", "Cloud Computing", "Git"},
    "Full Stack Developer": {"JavaScript", "Python", "SQL", "Git", "DevOps"},
    "Data Analyst": {"SQL", "Excel", "Data Visualization", "Statistics", "Power BI"},
    "Data Scientist": {"Python", "Machine Learning", "Statistics", "SQL", "Data Analysis"},
    "Data Engineer": {"SQL", "Python", "Cloud Computing", "BigQuery", "DevOps"},
    "Business Intelligence Analyst": {"Power BI", "Tableau", "SQL", "Excel", "Reporting"},
    "UX Designer": {"UX Design", "Figma", "Research", "Prototyping"},
    "UI Designer": {"UI Design", "Figma", "Adobe Creative Suite", "Typography"},
    "DevOps Engineer": {"DevOps", "Cloud Computing", "Docker", "Git", "Networking"},
    "Cybersecurity Analyst": {"Cybersecurity", "Networking", "Compliance", "Risk Management"},
    "IT Support Specialist": {"IT Support", "Networking", "Troubleshooting", "Customer Service"},
    "System Administrator": {"Networking", "Cloud Computing", "IT Support", "Cybersecurity"},
    "Product Manager": {"Project Management", "Agile", "Business Analysis", "UX Design", "Data Analysis"},
    
    # ========== MARKETING & COMMUNICATIONS ==========
    "Marketing Manager": {"Marketing", "Strategic Planning", "Digital Marketing", "Brand Management", "Budgeting"},
    "Digital Marketing Specialist": {"Digital Marketing", "SEO", "Google Analytics", "Social Media Marketing", "Google Ads"},
    "Social Media Manager": {"Social Media Marketing", "Content Marketing", "Copywriting", "Photography"},
    "Content Marketing Manager": {"Content Marketing", "SEO", "Copywriting", "Marketing"},
    "SEO Specialist": {"SEO", "Google Analytics", "Content Marketing", "Data Analysis"},
    "PPC Specialist": {"SEM", "Google Ads", "Facebook Ads", "Data Analysis", "Excel"},
    "Email Marketing Specialist": {"Email Marketing", "Marketing Automation", "Copywriting", "Data Analysis"},
    "Brand Manager": {"Brand Management", "Marketing", "Strategic Planning", "Market Research"},
    "PR Manager": {"Public Relations", "Communication", "Event Marketing", "Writing"},
    "Communications Manager": {"Communication", "Public Relations", "Content Marketing", "Presentation"},
    "Marketing Analyst": {"Marketing", "Data Analysis", "Excel", "Google Analytics", "Reporting"},
    "Growth Marketing Manager": {"Digital Marketing", "Data Analysis", "Marketing Automation", "SEO", "SEM"},
    
    # ========== BUSINESS & MANAGEMENT ==========
    "Project Manager": {"Project Management", "Agile", "Stakeholder Management", "Budgeting", "Leadership"},
    "Business Analyst": {"Business Analysis", "SQL", "Excel", "Process Improvement", "Presentation"},
    "Management Consultant": {"Business Analysis", "Strategic Planning", "Presentation", "Excel", "Problem Solving"},
    "Operations Manager": {"Operations Management", "Process Improvement", "Leadership", "KPI Management", "Budgeting"},
    "General Manager": {"Leadership", "Strategic Planning", "Budgeting", "Operations Management", "Sales"},
    "Strategy Analyst": {"Strategic Planning", "Business Analysis", "Financial Analysis", "Excel", "Presentation"},
    "Business Development Manager": {"Business Development", "Sales", "Negotiation", "Strategic Planning", "Networking"},
    "Program Manager": {"Project Management", "Stakeholder Management", "Leadership", "Strategic Planning"},
    "Office Manager": {"Organization", "Communication", "Microsoft Office", "Administration", "Multitasking"},
    "Executive Assistant": {"Organization", "Communication", "Microsoft Office", "Time Management", "Presentation"},
    
    # ========== FINANCE & ACCOUNTING ==========
    "Financial Analyst": {"Financial Analysis", "Excel", "Financial Modeling", "Valuation", "Reporting"},
    "Accountant": {"Accounting", "Tax", "Financial Reporting", "Excel", "SAP"},
    "Senior Accountant": {"Accounting", "Financial Reporting", "Auditing", "SAP", "Tax"},
    "Controller": {"Financial Analysis", "Budgeting", "Financial Reporting", "SAP", "Leadership"},
    "CFO": {"Financial Analysis", "Strategic Planning", "Leadership", "Budgeting", "M&A"},
    "Auditor": {"Auditing", "Financial Reporting", "Compliance", "Excel", "Attention to Detail"},
    "Tax Specialist": {"Tax", "Accounting", "Financial Reporting", "Compliance", "Excel"},
    "Treasury Analyst": {"Treasury", "Financial Analysis", "Excel", "Cash Management"},
    "Investment Analyst": {"Investment Analysis", "Financial Modeling", "Excel", "Valuation", "Bloomberg"},
    "Credit Analyst": {"Credit Analysis", "Financial Analysis", "Risk Management", "Excel"},
    "Risk Analyst": {"Risk Management", "Financial Analysis", "Compliance", "Excel", "Statistics"},
    "Financial Planner": {"Financial Analysis", "Investment Analysis", "Customer Service", "Communication"},
    
    # ========== HUMAN RESOURCES ==========
    "HR Manager": {"HR Management", "Recruiting", "Labor Law", "Training & Development", "Leadership"},
    "HR Business Partner": {"HR Management", "Strategic Planning", "Talent Management", "Labor Law"},
    "Recruiter": {"Recruiting", "Communication", "Negotiation", "Employer Branding"},
    "Talent Acquisition Specialist": {"Recruiting", "Employer Branding", "Communication", "Interview"},
    "Training Manager": {"Training & Development", "Leadership", "Presentation", "Curriculum Development"},
    "Compensation & Benefits Specialist": {"Compensation & Benefits", "HR Analytics", "Excel", "Labor Law"},
    "HR Generalist": {"HR Management", "Recruiting", "Training & Development", "Labor Law", "Communication"},
    "People Operations Manager": {"HR Management", "Process Improvement", "HR Analytics", "HRIS"},
    
    # ========== SALES ==========
    "Sales Representative": {"Sales", "Negotiation", "CRM", "Communication", "Lead Generation"},
    "Account Executive": {"Sales", "Negotiation", "B2B Sales", "CRM", "Presentation"},
    "Sales Manager": {"Sales Management", "Leadership", "Strategic Planning", "Negotiation", "Budgeting"},
    "Account Manager": {"Account Management", "Customer Success", "CRM", "Negotiation", "Communication"},
    "Business Development Representative": {"Business Development", "Lead Generation", "Sales", "CRM"},
    "Key Account Manager": {"Account Management", "Sales", "Negotiation", "Strategic Planning", "Relationship Building"},
    "Sales Director": {"Sales Management", "Leadership", "Strategic Planning", "Budgeting", "Negotiation"},
    "Inside Sales Representative": {"Inside Sales", "CRM", "Sales", "Communication", "Lead Generation"},
    "E-commerce Manager": {"E-commerce", "Digital Marketing", "SEO", "Data Analysis", "CRM"},
    "Retail Manager": {"Retail", "Sales", "Leadership", "Customer Service", "Inventory Management"},
    "Export Manager": {"Import/Export", "Sales", "Negotiation", "French", "Logistics"},
    
    # ========== LEGAL ==========
    "Lawyer": {"Contract Law", "Legal Research", "Litigation", "Communication", "Negotiation"},
    "Corporate Lawyer": {"Corporate Law", "M&A", "Contract Law", "Due Diligence", "Negotiation"},
    "Legal Counsel": {"Contract Law", "Corporate Law", "Compliance", "Negotiation", "Legal Research"},
    "Compliance Officer": {"Compliance", "GDPR", "Risk Management", "Auditing", "Legal Research"},
    "Paralegal": {"Legal Research", "Contract Law", "Organization", "Attention to Detail"},
    "Contract Manager": {"Contract Law", "Negotiation", "Legal Research", "Organization"},
    "Privacy Officer": {"GDPR", "Compliance", "Legal Research", "Risk Management"},
    
    # ========== DESIGN & CREATIVE ==========
    "Graphic Designer": {"Graphic Design", "Adobe Creative Suite", "Branding", "Typography"},
    "Senior Graphic Designer": {"Graphic Design", "Adobe Creative Suite", "Branding", "Leadership"},
    "Art Director": {"Graphic Design", "Leadership", "Branding", "Strategic Thinking"},
    "Creative Director": {"Graphic Design", "Leadership", "Strategic Planning", "Branding"},
    "UX/UI Designer": {"UX Design", "UI Design", "Figma", "Prototyping", "Research"},
    "Product Designer": {"UX Design", "UI Design", "Figma", "Product Management"},
    "Web Designer": {"Web Design", "HTML", "CSS", "Figma", "Adobe Creative Suite"},
    "Motion Designer": {"Motion Graphics", "Video Editing", "Adobe Creative Suite"},
    "Video Editor": {"Video Editing", "Adobe Creative Suite", "Photography"},
    "Photographer": {"Photography", "Adobe Creative Suite", "Lighting", "Creative"},
    "Copywriter": {"Copywriting", "Writing", "SEO", "Content Marketing", "Creativity"},
    "Content Creator": {"Content Marketing", "Social Media Marketing", "Photography", "Video Editing"},
    
    # ========== ENGINEERING ==========
    "Mechanical Engineer": {"Mechanical Engineering", "AutoCAD", "SolidWorks", "Manufacturing", "Problem Solving"},
    "Electrical Engineer": {"Electrical Engineering", "AutoCAD", "PLC Programming", "Circuit Design"},
    "Civil Engineer": {"Civil Engineering", "AutoCAD", "Project Management", "HSE"},
    "Industrial Engineer": {"Industrial Engineering", "Lean", "Six Sigma", "Process Improvement", "Manufacturing"},
    "Chemical Engineer": {"Chemical Engineering", "Process Improvement", "Quality Control", "HSE"},
    "Process Engineer": {"Process Improvement", "Lean", "Manufacturing", "Quality Control"},
    "Quality Engineer": {"Quality Control", "ISO Standards", "Auditing", "Six Sigma", "Problem Solving"},
    "Maintenance Engineer": {"Maintenance", "Mechanical Engineering", "Electrical Engineering", "Troubleshooting"},
    "HSE Manager": {"HSE", "Compliance", "Auditing", "ISO Standards", "Training & Development"},
    "Production Manager": {"Manufacturing", "Leadership", "Operations Management", "Lean", "Quality Control"},
    "R&D Engineer": {"Research", "Engineering", "Innovation", "Problem Solving", "Technical Writing"},
    
    # ========== SUPPLY CHAIN & LOGISTICS ==========
    "Supply Chain Manager": {"Supply Chain Management", "Logistics", "Procurement", "Vendor Management", "Leadership"},
    "Logistics Manager": {"Logistics", "Transportation", "Warehouse Management", "Leadership", "Operations"},
    "Procurement Manager": {"Procurement", "Vendor Management", "Negotiation", "Budgeting", "Contracts"},
    "Supply Chain Analyst": {"Supply Chain Management", "Data Analysis", "Excel", "Demand Planning"},
    "Logistics Coordinator": {"Logistics", "Transportation", "Warehouse Management", "Organization"},
    "Warehouse Manager": {"Warehouse Management", "Inventory Management", "Leadership", "Operations"},
    "Purchasing Specialist": {"Procurement", "Negotiation", "Vendor Management", "Excel"},
    "Import/Export Specialist": {"Import/Export", "Logistics", "Documentation", "Compliance"},
    "Demand Planner": {"Demand Planning", "Data Analysis", "Excel", "Forecasting"},
    
    # ========== HEALTHCARE & PHARMA ==========
    "Clinical Research Associate": {"Clinical Research", "GCP", "Medical Writing", "Regulatory Affairs"},
    "Regulatory Affairs Specialist": {"Regulatory Affairs", "Compliance", "Medical Writing", "Documentation"},
    "Medical Science Liaison": {"Medical Writing", "Communication", "Presentation", "Healthcare"},
    "Pharmacovigilance Specialist": {"Pharmacovigilance", "GCP", "Data Analysis", "Compliance"},
    "Medical Sales Representative": {"Medical Sales", "Sales", "Healthcare", "Communication"},
    "Quality Assurance (Pharma)": {"Quality Control", "GCP", "Compliance", "Auditing", "ISO Standards"},
    "Healthcare Administrator": {"Healthcare Administration", "Operations Management", "Leadership", "Budgeting"},
    "Clinical Data Manager": {"Clinical Research", "Data Analysis", "SQL", "GCP"},
    "Nurse": {"Nursing", "Patient Care", "Communication", "Empathy"},
    
    # ========== HOSPITALITY & TOURISM ==========
    "Hotel Manager": {"Hotel Management", "Leadership", "Customer Service", "Revenue Management", "Budgeting"},
    "Front Office Manager": {"Front Office", "Customer Service", "Leadership", "Reservation Systems"},
    "Revenue Manager": {"Revenue Management", "Data Analysis", "Excel", "Pricing"},
    "Event Manager": {"Event Management", "Project Management", "Vendor Management", "Budgeting"},
    "Restaurant Manager": {"F&B Management", "Leadership", "Customer Service", "Budgeting"},
    "Tour Manager": {"Tourism", "Customer Service", "Languages", "Organization"},
    "Concierge": {"Concierge", "Customer Service", "Languages", "Problem Solving"},
    "Guest Relations Manager": {"Customer Service", "Communication", "Problem Solving", "Languages"},
    "F&B Manager": {"F&B Management", "Leadership", "Budgeting", "Customer Service"},
    
    # ========== EDUCATION ==========
    "Teacher": {"Teaching", "Communication", "Curriculum Development", "Patience"},
    "University Professor": {"Teaching", "Research", "Academic Writing", "Presentation"},
    "Corporate Trainer": {"Training Delivery", "Presentation", "Curriculum Development", "Communication"},
    "Instructional Designer": {"Curriculum Development", "E-Learning", "Graphic Design", "Writing"},
    "Academic Coordinator": {"Organization", "Communication", "Teaching", "Administration"},
    
    # ========== CUSTOMER SERVICE ==========
    "Customer Service Representative": {"Customer Service", "Communication", "Problem Solving", "CRM"},
    "Customer Service Manager": {"Customer Service", "Leadership", "Process Improvement", "Communication"},
    "Call Center Agent": {"Customer Service", "Communication", "CRM", "Problem Solving"},
    "Technical Support Specialist": {"IT Support", "Customer Service", "Troubleshooting", "Communication"},
    
    # ========== ADMINISTRATION ==========
    "Administrative Assistant": {"Organization", "Microsoft Office", "Communication", "Multitasking"},
    "Receptionist": {"Customer Service", "Communication", "Organization", "Multitasking"},
    "Data Entry Specialist": {"Data Entry", "Excel", "Attention to Detail", "Organization"},
    "Personal Assistant": {"Organization", "Time Management", "Communication", "Multitasking"},
}
