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
    # ===========================================================================
    # CLEANED INFERENCE RULES - Max 1-2 direct technical inferences per skill
    # No soft skills (Communication, Problem Solving), no cross-domain cascading
    # ===========================================================================

    # --- TECHNOLOGY & IT ---
    "React": ["JavaScript"],
    "Vue": ["JavaScript"],
    "Angular": ["JavaScript", "TypeScript"],
    "TypeScript": ["JavaScript"],
    "Django": ["Python"],
    "Flask": ["Python"],
    "Spring": ["Java"],
    "Hibernate": ["Java"],
    "AWS": ["Cloud Computing"],
    "Azure": ["Cloud Computing"],
    "GCP": ["Cloud Computing"],
    "Docker": ["DevOps"],
    "Kubernetes": ["DevOps"],
    "Terraform": ["DevOps"],
    "Git": ["Version Control"],

    # --- MARKETING & DIGITAL ---
    "Google Ads": ["SEM"],
    "Facebook Ads": ["Social Media Marketing"],
    "LinkedIn Ads": ["Social Media Marketing"],
    "Google Analytics": ["Web Analytics"],
    "GA4": ["Web Analytics"],
    "HubSpot": ["CRM"],
    "Salesforce": ["CRM"],

    # --- BUSINESS & MANAGEMENT ---
    "Jira": ["Project Management"],
    "Trello": ["Project Management"],
    "Asana": ["Project Management"],
    "Scrum": ["Agile"],
    "Kanban": ["Agile"],

    # --- FINANCE & ACCOUNTING ---
    "Financial Reporting": ["Accounting"],
    "Auditing": ["Accounting"],
    "Tax": ["Accounting"],
    "Financial Modeling": ["Excel"],
    "SAP": ["ERP"],
    "IFRS": ["Accounting"],
    "GAAP": ["Accounting"],

    # --- DESIGN & CREATIVE ---
    "Adobe Photoshop": ["Graphic Design"],
    "Adobe Illustrator": ["Graphic Design"],
    "Adobe InDesign": ["Graphic Design"],
    "Figma": ["UI Design"],
    "Sketch": ["UI Design"],
    "Premiere Pro": ["Video Editing"],
    "After Effects": ["Video Editing"],

    # --- LEGAL ---
    "GDPR": ["Compliance"],
    "M&A": ["Corporate Law"],

    # --- DATA & ANALYTICS ---
    "Power BI": ["Data Visualization"],
    "Tableau": ["Data Visualization"],
    "Looker": ["Data Visualization"],
    "BigQuery": ["SQL"],
    "Snowflake": ["SQL"],

    # --- LAB & SCIENCE (only direct, no cascading) ---
    "HPLC": ["Lab Skills"],
    "PCR": ["Lab Skills"],
    "GMP": ["Quality Management"],

    # --- ENGINEERING ---
    "SolidWorks": ["CAD"],
    "AutoCAD": ["CAD"],
    "PLC": ["Automation"],

    # --- HR ---
    "Recruiting": ["Talent Acquisition"],
    "ATS Management": ["Recruiting"],
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
    # ========== TECHNOLOGY & IT (DETAILED) ==========
    "Programming": ["programming", "coding", "sviluppo software", "programmazione"],
    "Python": ["python", "py", "pandas", "numpy", "django", "flask", "fastapi"],
    "JavaScript": ["javascript", "js", "node", "react", "vue", "angular", "typescript", "es6+"],
    "Java": ["java", "spring", "spring boot", "jakarta ee", "hibernate", "maven", "gradle"],
    "C#": ["c#", "csharp", ".net", "dotnet", "asp.net core", "entity framework", "blazor"],
    "SQL": ["sql", "mysql", "postgresql", "t-sql", "pl/sql", "database design", "query optimization"],
    
    # Frontend (Killer Keywords)
    "Frontend Development": ["frontend", "front-end", "ui implementation"],
    "State Management": ["redux", "pinia", "zustand", "mobx", "context api", "ngrx", "recoil"],
    "Modern Web": ["pwa", "progressive web apps", "service workers", "webassembly", "wasm", "webgl", "three.js"],
    "Testing (Frontend)": ["jest", "cypress", "playwright", "react testing library", "selenium", "puppeteer"],
    "Performance": ["web performance", "core web vitals", "lazy loading", "tree shaking", "lighthouse"],
    "Accessibility": ["wcag", "wai-aria", "accessibility", "a11y", "screen readers"],

    # Backend (Killer Keywords)
    "Backend Development": ["backend", "back-end", "server-side"],
    "Microservices": ["microservices", "micro-services", "distributed systems", "service mesh", "istio"],
    "API Design": ["rest", "graphql", "grpc", "openapi", "swagger", "api gateway"],
    "Messaging": ["kafka", "apache kafka", "rabbitmq", "activemq", "pub/sub", "event-driven", "sqs", "sns"],
    "Serverless": ["serverless", "aws lambda", "azure functions", "google cloud functions", "faas"],

    # DevOps & Cloud (Killer Keywords)
    "DevOps": ["devops", "sre", "site reliability engineering"],
    "Cloud Computing": ["aws", "azure", "gcp", "google cloud", "cloud native"],
    "Containerization": ["docker", "kubernetes", "k8s", "helm", "openshift", "containerd"],
    "IaC": ["terraform", "infrastructure as code", "ansible", "cloudformation", "pulumi"],
    "CI/CD": ["jenkins", "gitlab ci", "github actions", "circleci", "argo cd", "pipelines"],
    "Monitoring": ["prometheus", "grafana", "datadog", "elk stack", "splunk", "new relic", "observability"],

    # ========== MARKETING & COMMUNICATION (DETAILED) ==========
    "Marketing Strategy": ["marketing strategy", "pianificazione marketing", "marketing mix", "go-to-market"],
    
    # SEO (Killer Keywords)
    "SEO": ["seo", "optimization", "organic traffic"],
    "Technical SEO": ["technical seo", "schema markup", "structured data", "core web vitals", "log file analysis", "crawl budget"],
    "Keyword Strategy": ["keyword research", "search intent", "semrush", "ahrefs", "long-tail keywords"],
    "Local SEO": ["local seo", "google my business", "local pack", "citation building"],

    # PPC/SEM (Killer Keywords)
    "SEM": ["sem", "ppc", "pay per click", "paid search"],
    "Programmatic Ads": ["programmatic advertising", "rtb", "real-time bidding", "dsp", "ssp", "dv360"],
    "Ad Tech": ["google tag manager", "gtm", "facebook pixel", "conversion api", "server-side tagging"],
    "Conversion Optimization": ["cro", "conversion rate optimization", "a/b testing", "multivariate testing", "hotjar", "crazy egg"],

    # Social & Content (Killer Keywords)
    "Social Media": ["social media marketing", "smm", "community management"],
    "Social Listening": ["social listening", "sentiment analysis", "brandwatch", "sprout social", "mention"],
    "Influencer Strategy": ["influencer marketing", "creator economy", "affiliate marketing", "ugc campaigns"],
    "Content Strategy": ["content marketing", "storytelling", "editorial calendar", "content governance"],
    "Specialized Content": ["technical writing", "ghostwriting", "video scripting", "white papers", "case studies"],

    # Communication
    "Public Relations": ["public relations", "pr", "media relations", "press release", "crisis communication"],
    "Corporate Communication": ["corporate communication", "internal communication", "investor relations", "stakeholder engagement"],
    
    # ========== BUSINESS, SALES & LEGAL (DETAILED) ==========
    # Sales (Killer Keywords)
    "Tech Sales": ["saas sales", "technical sales", "solution selling", "consultative selling", "demo skills"],
    "Sales Methodologies": ["spin selling", "challenger sale", "meddic", "sandler training", "bant"],
    "Sales Operations": ["sales ops", "pipeline management", "sales forecasting", "territory planning", "quota management"],
    "CRM Admin": ["salesforce admin", "hubspot crm", "crm implementation", "workflow automation"],

    # Legal (Killer Keywords)
    "Corporate Law": ["corporate law", "m&a", "mergers and acquisitions", "due diligence", "corporate governance"],
    "IP Law": ["intellectual property", "trademark", "patent", "copyright", "licensing", "freedom to operate"],
    "Contract Law": ["contract negotiation", "drafting", "nda", "sla", "master service agreement"],
    "Compliance": ["regulatory compliance", "gdpr", "data privacy", "anti-money laundering", "aml", "kyc"],
    
    # Business Management
    "Project Management": ["project management", "pmp", "prince2"],
    "Agile Frameworks": ["agile", "scrum", "kanban", "safe", "less", "sprint planning"],
    "Product Management": ["product management", "product roadmap", "user stories", "product lifecycle", "mvp"],
    "Business Analysis": ["business analysis", "requirements gathering", "bpmn", "process mapping", "gap analysis"],

    # ========== FINANCE & ECONOMICS (DETAILED) ==========
    "Accounting": ["accounting", "financial statements", "ifrs", "gaap", "bookkeeping", "general ledger"],
    "Financial Analysis": ["financial analysis", "financial modeling", "dcf", "valuation", "fp&a"],
    "Taxation": ["tax compliance", "tax planning", "transfer pricing", "vat", "corporate tax"],
    
    # Quantitative Finance (Killer Keywords)
    "Quant Finance": ["quantitative finance", "stochastic calculus", "black-scholes", "garch", "time series analysis"],
    "Risk Management": ["value at risk", "var", "stress testing", "credit risk modeling", "market risk", "basel iii"],
    "Algorithmic Trading": ["algorithmic trading", "hft", "high-frequency trading", "market microstructure", "order book dynamics"],
    "Derivatives": ["derivatives", "options pricing", "futures", "swaps", "structured products", "exotics"],
    "Investment Management": ["asset allocation", "portfolio construction", "factor investing", "smart beta", "esg investing"],

    # ========== ENGINEERING (DETAILED) ==========
    "Mechanical Engineering": ["mechanical engineering", "mechanics"],
    
    # Simulation & Analysis (Killer Keywords)
    "Simulation": ["fem", "finite element analysis", "cfd", "computational fluid dynamics", "ansys", "abaqus", "nastran"],
    "CAD/Design": ["catia", "solidworks", "creo", "inventor", "gd&t", "geometric dimensioning", "tolerance analysis"],
    "Thermodynamics": ["thermodynamics", "heat transfer", "hvac design", "fluid mechanics", "combustion"],

    # Mechatronics & Automation (Killer Keywords)
    "PLC & SCADA": ["plc programming", "siemens step 7", "tia portal", "allen bradley", "rslogix", "scada", "wonderware", "hmi"],
    "Robotics": ["industrial robotics", "kuka", "fanuc", "abb", "robot programming", "ros", "robot operating system", "kinematics"],
    "Control Systems": ["control theory", "pid control", "matlab/simulink", "state estimations", "kalman filter"],
    "Embedded": ["embedded c", "microcontrollers", "stm32", "arduino", "rtos", "firmware development", "i2c", "spi", "uart"],

    # Energy (Killer Keywords)
    "Renewable Energy": ["renewable energy", "solar pv", "photovoltaics", "wind energy", "pvsyst", "helioscope", "windsim"],
    "Grid & Storage": ["smart grid", "energy storage", "bess", "battery management systems", "high voltage", "power systems analysis"],
    "Sustainability": ["energy efficiency", "carbon footprint", "lca", "life cycle assessment", "leed", "energy audit"],

    # ========== LANGUAGES & TRANSLATION (DETAILED) ==========
    "Languages": ["english", "italian", "french", "german", "spanish", "chinese", "japanese"],
    
    # Translation (Killer Keywords)
    "Translation Tech": ["cat tools", "trados studio", "memoq", "memsource", "wordfast", "terminology management"],
    "Specialized Translation": ["legal translation", "biomedical translation", "patent translation", "technical translation", "financial translation"],
    "Localization": ["localization", "l10n", "internationalization", "i18n", "software localization", "game localization", "transcreation"],
    "Post-Editing": ["mtpe", "machine translation post-editing", "neural machine translation"],

    # Interpreting (Killer Keywords)
    "Interpreting Modes": ["simultaneous interpreting", "consecutive interpreting", "chuchotage", "liaison interpreting"],
    "Remote Interpreting": ["rsi", "remote simultaneous interpreting", "kudo", "interpretfy", "zoom interpretation"],
    
    # ========== HUMAN RESOURCES (DETAILED) ==========
    # Talent Acquisition (Killer Keywords)
    "Sourcing": ["boolean search", "x-ray search", "github sourcing", "stackoverflow sourcing", "talent mapping"],
    "Recruitment Marketing": ["employer branding", "career page optimization", "recruitment analytics", "candidate experience"],
    "Assessment": ["psychometric testing", "assessment centers", "behavioral interviewing", "star method", "coding challenges"],
    
    # Comp & Ben (Killer Keywords)
    "Compensation": ["salary benchmarking", "job grading", "hay method", "mercer", "towers watson", "executive compensation"],
    "Benefits": ["benefits administration", "welfare plans", "pension schemes", "health insurance", "total rewards"],

    # ========== SUPPLY CHAIN & LOGISTICS (DETAILED) ==========
    "Supply Chain": ["supply chain management", "scm"],
    "Planning (Killer Keywords)": ["demand planning", "s&op", "sales and operations planning", "mrp ii", "inventory optimization", "safety stock analysis"],
    "Procurement (Killer Keywords)": ["strategic sourcing", "category management", "rfq/rfp management", "supplier relationship management", "srm", "contract negotiation"],
    "Logistics (Killer Keywords)": ["freight forwarding", "incoterms 2020", "last mile delivery", "fleet telematics", "reverse logistics", "wms configuration"],

    # ========== DATA & ANALTYICS (STANDARD) ==========
    "Data Analysis": ["data analysis", "pandas", "numpy", "excel", "power query"],
    "Visualization": ["power bi", "tableau", "looker", "qlik", "domo", "google data studio"],
    "Big Data": ["hadoop", "spark", "hive", "databricks", "snowflake", "redshift"],
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

    # ========== CONSTRUCTION & REAL ESTATE (NEW) ==========
    "Construction Manager": {"Construction Management", "Project Management", "Budgeting", "Leadership", "Safety"},
    "Architect": {"Architecture", "Design", "AutoCAD", "SketchUp", "Creativity"},
    "Civil Engineer (Site)": {"Civil Engineering", "Construction Management", "AutoCAD", "Surveying"},
    "Real Estate Agent": {"Real Estate", "Sales", "Negotiation", "Communication", "Customer Service"},
    "Property Manager": {"Property Management", "Customer Service", "Organization", "Maintenance"},
    "Facility Manager": {"Facility Management", "Maintenance", "Leadership", "Budgeting"},

    # ========== INSURANCE & ACTUARIAL (NEW) ==========
    "Actuary": {"Actuarial Science", "Statistics", "Math", "Risk Management", "Excel"},
    "Underwriter": {"Underwriting", "Risk Analysis", "Insurance", "Analytical Skills"},
    "Claims Adjuster": {"Claims", "Insurance", "Customer Service", "Negotiation", "Investigation"},
    "Insurance Broker": {"Insurance", "Sales", "Negotiation", "Communication"},

    # ========== CREATIVE ARTS & MEDIA (NEW) ==========
    "Journalist": {"Journalism", "Writing", "Research", "Communication", "Interviewing"},
    "Sound Engineer": {"Audio Engineering", "Pro Tools", "Mixing", "Music"},
    "Video Producer": {"Video Production", "Project Management", "Creativity", "Budgeting"},
    "Art Curator": {"Art History", "Organization", "Communication", "Research"},

    # ========== LABORATORY & QC (NEW) ==========
    "Lab Technician": {"Lab Skills", "HPLC", "Gas Chromatography", "Quality Control", "GMP", "Sample Preparation"},
    "QC Analyst": {"Quality Control", "HPLC", "Gas Chromatography", "Microbiological Analysis", "GMP", "ISO Standards"},
    "Research Scientist": {"Research", "Lab Skills", "Data Analysis", "Scientific Writing", "Molecular Biology"},
    "Formulation Chemist": {"Chemistry", "Formulation", "Lab Skills", "Product Development"},
    "Cosmetic Chemist": {"Chemistry", "Cosmetic Regulations", "ISO 22716", "Formulation", "Quality Control"},
    "Regulatory Affairs Specialist (Pharma)": {"Regulatory", "Compliance", "GMP", "Clinical Trials", "Documentation"},
    "Microbiologist": {"Microbiology", "Lab Skills", "Microbiological Analysis", "Quality Control", "GLP"},
}

# =============================================================================
# NON-SKILL PATTERNS - Sections to filter from JD before skill extraction
# =============================================================================
# These patterns identify non-skill elements in Job Descriptions that should
# NOT be extracted as missing skills (benefits, salaries, contract terms, etc.)
# Supports: Italian, English, UK, USA, Australian terminology
# =============================================================================
NON_SKILL_PATTERNS = {
    # Section headers to remove entirely
    "section_headers": [
        r"benefic[i]?|benefits|cosa (?:ti )?offriamo|what we offer|perks",
        r"condizioni|conditions|termini|terms|nota (?:importante|legale)",
        r"piano formativo|training plan|formazione|learning objectives",
        r"chi siamo|about us|la nostra azienda|our company|about the company",
        r"come funziona|how (?:it )?works|come candidarsi|how to apply",
        r"vantaggi(?: per te)?|advantages|cosa non offriamo|what we don't offer",
        r"testimonianza|testimonial|success metrics|timeline",
        r"struttura programma|programme structure",
    ],
    
    # Salary/compensation (IT/EN/UK/USA with symbols)
    "salary": [
        r"[€$£]\s*[\d.,]+(?:k|K)?(?:\s*/\s*(?:anno|year|mese|month|ora|hour))?",
        r"(?:RAL|retribuzione|salary|compensation|compenso|stipendio|indennità)[\s:]*[\d€$£.,]+",
        r"(?:lordo|gross|netto|net|all-inclusive)\b",
        r"pagamento (?:milestone|settimanale|mensile|weekly|monthly)",
        r"(?:invoice|fattura)\s*(?:mensile|monthly)?",
        r"timesheet\s*(?:settimanale|weekly)?",
    ],
    
    # Work hours/schedule
    "hours": [
        r"\d+\s*(?:ore|hours?)(?:\s*/\s*(?:settimana|week))?",
        r"(?:full-time|part-time|tempo (?:pieno|parziale))",
        r"(?:lunedì|monday)[\s\-–a]+(?:venerdì|friday|domenica|sunday)",
        r"\d{1,2}[:\-\.]\d{2}\s*(?:am|pm)?(?:\s*[\-–a]\s*\d{1,2}[:\-\.]\d{2})?",
        r"(?:turni?|shifts?)[\s\w]*(?:serali?|notturni?|weekend|flessibil[ei])?",
        r"(?:on-call|a chiamata|zero[- ]?hour)",
    ],
    
    # Duration/dates
    "duration": [
        r"\d+\s*(?:mesi|months?|anni|years?|settimane|weeks?|giorni|days?)",
        r"(?:dal|from|fino al?|until|entro)\s+[\d\/\-\w]+",
        r"(?:gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)\s+\d{4}",
        r"(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{4}",
        r"\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}",
    ],
    
    # Benefits (IT/EN/UK/USA/AU comprehensive)
    "benefits": [
        r"(?:ferie|vacation|holidays?|annual leave)(?:\s+(?:pagate?|paid|pro-rata))?",
        r"(?:assicurazione|insurance)(?:\s+(?:sanitaria|health|integrativa|RC|civile))?",
        r"(?:pensione|pension|fondo pensione|retirement|superannuation)",
        r"(?:buoni pasto|meal vouchers?|pasti gratuiti|free meals?|mensa)",
        r"(?:smart working|remote work|lavoro (?:da )?remoto|hybrid|home working)",
        r"(?:tredicesima|quattordicesima|bonus|premio|performance-based)",
        r"(?:contributi|contributions?)(?:\s+(?:previdenziali|INPS|pension|ordinari))?",
        r"(?:housing|alloggio|residence)(?:\s+(?:gratuito|free))?",
        r"(?:mentorato?|mentorship|mentoring|coaching)",
        r"(?:attestato|certificate|certificato)(?:\s+(?:di stage|riconosciuto|volontariato))?",
        r"(?:rimborso?|reimbursement)(?:\s+(?:spese?|viaggio|trasporto|expenses?))?",
        r"(?:networking|community|coorte|cohort)",
        r"(?:campus|access|accesso)\s+(?:technology|tecnologia)?",
        r"(?:corsi|courses?|training)(?:\s+(?:leadership|sviluppo|development))?",
    ],
    
    # Contract terms (IT/EN/UK/USA/AU)
    "contract": [
        r"(?:contratto|contract)\s+(?:a scadenza|rinnovabile|non rinnovabile|determinato|indeterminato|permanent|fixed)",
        r"(?:pro-rata|prorated)",
        r"(?:CCNL|collective agreement|at-will|employment)",
        r"(?:trasformazione|conversion|passaggio)(?:\s+(?:a indeterminato|to permanent|automatica?|dirett[oa]))?",
        r"(?:return offer|potential (?:hire|assunzione)|possibile assunzione)",
        r"(?:clausola|clause)(?:\s+(?:di )?(?:esclusiva|exclusivity))?",
        r"(?:cancellazione|cancellation)(?:\s+(?:con )?\d+\s*(?:h|ore|hours?)\s*(?:di )?preavviso)?",
        r"(?:nessun[ao]?\s+)?(?:garanzia|obblig[oa]|guarantee|obligation)",
        r"(?:estendibile|extendable|renewable)",
        r"(?:limite massimo|maximum limit)\s*\d+",
        r"400\s*(?:giorni|days?|gg)",
    ],
    
    # Age/eligibility (apprenticeship, internship, graduate)
    "eligibility": [
        r"(?:età|age)[\s:]*(?:dai?|from)?\s*\d+\s*(?:ai?|to|\-)?\s*\d*\s*(?:anni|years?)?",
        r"(?:studente|student|neolaureato?|graduate)(?:\s+(?:ultimo anno|entro \d+ mesi|currently enrolled))?",
        r"(?:GPA|media)[\s:]*\d+[.,]?\d*",
        r"(?:laurea|degree|bachelor|master|phd)(?:\s+(?:triennale|magistrale|entro))?",
        r"(?:graduation|laureat[oi])(?:\s+(?:tra|between|entro))?",
        r"(?:nessun[ao]?\s+)?(?:esperienza|experience)(?:\s+(?:richiesta|required))?",
        r"(?:entry-level|junior|senior)",
    ],
    
    # Training/certification context (not skills)
    "training": [
        r"(?:qualifica|qualification)(?:\s+(?:professionale|riconosciuta|statale))?",
        r"(?:certificazione|certification)(?:\s+(?:ITS|professionale|europea|internazionale))?",
        r"(?:diploma|degree)(?:\s+(?:ITS|riconosciuto|internazionalmente))?",
        r"(?:obiettivi di apprendimento|learning objectives)",
        r"(?:formazione)(?:\s+(?:teorica|pratica|continua|pre-servizio))?",
        r"(?:assessment center|phone screen|final interview)",
    ],
    
    # Agency/intermediary patterns
    "agency": [
        r"(?:agenzia|agency)[\s:]+\w+",
        r"(?:Randstad|Adecco|Manpower|Kelly|Gi Group|Caritas)",
        r"(?:azienda cliente|client company|presso sede)",
        r"(?:somministrazione|staffing|temporary|tramite)",
    ],
    
    # Freelance/project patterns
    "freelance": [
        r"(?:P\.?IVA|VAT|partita iva)(?:\s+(?:attiva|obbligatorio|required))?",
        r"(?:milestone|deliverable)\s*\d*",
        r"(?:progetto|project)(?:\s+(?:fisso|based))?",
        r"(?:workspace|attrezzature|equipment)(?:\s+(?:non (?:fornit[oai]|included)))?",
        r"(?:kick-off|jira|tracking|riunioni settimanali)",
    ],
    
    # Volunteering patterns
    "volunteering": [
        r"(?:volontar[io]|volunteer|unpaid)",
        r"(?:impegno minimo|minimum commitment)",
        r"(?:impatto civile|social impact)",
        r"(?:puoi interrompere|you can stop)",
    ],
    
    # Legal/regulatory notes
    "legal": [
        r"(?:conversione automatica|automatic conversion)",
        r"(?:primary beneficiary test)",
        r"(?:legge italiana|italian law|secondo la legge|employment (?:rights )?act)",
        r"(?:fair work act|nlra|fsla)",
        r"(?:pari opportunità|equal opportunity|dei statement)",
        r"(?:accommodation|disabilità|disability)",
    ],
}
