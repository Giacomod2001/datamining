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

    # --- FASHION & LUXURY (NEW) ---
    "Fashion Design": ["Sketching"],
    "Textile Design": ["Fabric Knowledge"],
    "Visual Merchandising": ["Retail Design"],
    "CLO3D": ["3D Fashion Design"],
    "Gerber": ["Pattern Making"],
    "Lectra": ["Pattern Making"],
    "Luxury Retail": ["Clienteling"],

    # --- FOOD, BEVERAGE & AGRITECH (NEW) ---
    "HACCP": ["Food Safety"],
    "ISO 22000": ["Food Safety"],
    "Enology": ["Winemaking"],
    "Sensory Analysis": ["Food Quality"],
    "Menu Engineering": ["F&B Management"],

    # --- MANUFACTURING 4.0 (NEW) ---
    "CNC Programming": ["Machining"],
    "Fanuc": ["Robotics"],
    "Siemens PLC": ["Automation"],
    "Predictive Maintenance": ["Maintenance Management"],
    "Lean Manufacturing": ["Process Improvement"],
    "Six Sigma": ["Quality Management"],

    # --- DESIGN & ARCHITECTURE (NEW) ---
    "Revit": ["BIM"],
    "ArchiCAD": ["BIM"],
    "SketchUp": ["3D Modeling"],
    "V-Ray": ["Rendering"],
    "AutoCAD": ["CAD"],
    
    # --- BANKING & INSURANCE (NEW) ---
    "MiFID II": ["Compliance"],
    "Anti-Money Laundering": ["Compliance"],
    "Credit Risk": ["Risk Management"],
    "Wealth Management": ["Financial Planning"],

    # --- ENGINEERING DEEP DIVE (NEW) ---
    "SolidWorks": ["CAD"],
    "CATIA": ["CAD"],
    "Ansys": ["Simulation"],
    "Altium Designer": ["PCB Design"],
    "Revit": ["BIM"],
    "Navisworks": ["BIM"],
    "Embedded C": ["Embedded Systems"],
    "PLC Programming": ["Automation"],

    # --- BIOTECH & PHARMA (NEW) ---
    "PCR": ["Lab Skills"],
    "ELISA": ["Lab Skills"],
    "Clinical Trials": ["GCP"],
    "GMP": ["Quality Assurance"],
    "Regulatory Affairs": ["Compliance"],

    # --- LANGUAGES (NEW) ---
    "Trados Studio": ["Translation Tech"],
    "MemoQ": ["Translation Tech"],
    "Simultaneous Interpreting": ["Interpreting"],
    
    # --- ECONOMICS (NEW) ---
    "IFRS": ["Accounting"],
    "GAAP": ["Accounting"],
    "Audit": ["Compliance"],
    "Transfer Pricing": ["Taxation"],

    # --- ENERGY ENGINEERING & TRADING (NEW) ---
    "ENTSO-E": ["Energy Markets", "Grid Operators"],
    "TERNA": ["Grid Operators", "Energy Markets"],
    "GME": ["Energy Markets", "Grid Operators"],
    "Hypatia": ["Energy Software", "Renewable Energy"],
    "Thermodynamics": ["Energy & Renewables"],
    "NASA CEA": ["Aerospace Propulsion", "Combustion"],
    "Balancing Market": ["Energy Markets", "Energy Trading"],
    "PVsyst": ["Renewable Energy", "Energy Software"],
    "MATLAB": ["Simulation", "Data Analysis"],
    "Simulink": ["MATLAB", "Simulation"],
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
# SENIORITY KEYWORDS
# =============================================================================
SENIORITY_KEYWORDS = {
    "Entry Level": ["entry level", "junior", "intern", "internship", "trainee", "graduate", "associate", "stage", "tirocinio", "student", "studente", "laureando", "neo-laureato", "apprentice"],
    "Mid Level": ["mid level", "mid-level", "experienced", "specialist", "analyst", "consultant", "manager", "gestion"],
    "Senior Level": ["senior", "lead", "principal", "head of", "director", "vp", "executive", "chief", "partner", "founder"],
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
    "SEO": ["seo", "search engine optimization", "organic traffic", "organic search"],
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
    
    # ========== ENERGY ENGINEERING & TRADING (NEW) ==========
    "Energy Markets": ["energy markets", "power markets", "electricity markets", "wholesale market", "day-ahead", "intraday", "balancing market", "ancillary services", "mercato elettrico", "msd", "mgp", "mi"],
    "Energy Trading": ["energy trading", "power trading", "commodity trading", "ppa", "power purchase agreement", "hedging", "price forecasting", "trading desk", "energy derivatives"],
    "Grid Operators": ["entso-e", "terna", "gme", "gestore mercati", "tso", "transmission system operator", "gmme", "arera", "acer", "res integration"],
    "Thermodynamics": ["thermodynamics", "termodinamica", "heat transfer", "cicli termodinamici", "brayton", "rankine", "heat recovery", "hrsg", "steam cycle", "gas cycle"],
    "Aerospace Propulsion": ["propulsion", "propulsione", "turbomachinery", "gas turbine", "jet engine", "combustion", "nasa cea", "aerospace systems", "aerospace engineering", "ingegneria aerospaziale"],
    "Energy Forecasting": ["load forecasting", "demand forecasting", "price forecasting", "renewable forecasting", "time series forecasting", "predictive models", "predictive analytics", "quantitative analysis"],
    "Energy Software": ["hypatia", "pvsyst", "homer", "retscreen", "energyplus", "openmodelica", "plexos", "psse", "digsilent"],
    "MATLAB": ["matlab", "simulink", "matlab/simulink", "mathworks"],

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
    "Excel": ["excel", "microsoft excel", "advanced excel", "excel advanced", "vba", "pivot table", "vlookup", "xlookup"],
    "Data Analysis": ["data analysis", "pandas", "numpy", "power query"],
    "Visualization": ["power bi", "tableau", "looker", "qlik", "domo", "google data studio", "looker studio", "google looker studio", "data visualization"],
    "Big Data": ["hadoop", "spark", "hive", "databricks", "snowflake", "redshift", "bigquery"],
    "Google Analytics": ["google analytics", "ga4", "google analytics 4", "universal analytics", "web analytics"],

    # ========== FASHION & LUXURY (DETAILED) ==========
    "Fashion Design": ["fashion design", "stilista", "fashion sketching", "moodboard", "modellistica", "draping"],
    "Textile Knowledge": ["textile", "tessuti", "merciologia tessile", "fabric knowledge", "yarns", "filati", "leather"],
    "Pattern Making": ["pattern making", "modellista", "cartamodello", "lectra", "gerber", "clo3d", "cad fashion"],
    "Visual Merchandising": ["visual merchandising", "vetrinista", "store layout", "display design", "in-store experience"],
    "Luxury Retail": ["luxury retail", "vendita assistita", "luxury sales", "clienteling", "vic", "very important client"],
    "Buying": ["buying", "buyer", "acquisti moda", "budgeting", "assortment planning", "oted"],
    "Merchandising": ["merchandising", "allocator", "stock management", "sales analysis", "open to buy"],

    # ========== FOOD & BEVERAGE & ARGITECH (DETAILED) ==========
    "Food Safety": ["haccp", "iso 22000", "brc", "ifs", "sicurezza alimentare", "food defense"],
    "Food Technology": ["food technology", "tecnologie alimentari", "processo produttivo", "scienza degli alimenti", "shelf life"],
    "Enology": ["enology", "enologia", "winemaking", "vinificazione", "sommelier", "degustazione", "cantina"],
    "Agronomy": ["agronomy", "agronomia", "coltivazioni", "crop management", "precision agriculture", "agritech"],
    "F&B Management": ["food & beverage", "f&b", "food cost", "menu engineering", "gestione sala", "ristorazione"],

    # ========== MANUFACTURING 4.0 (DETAILED) ==========
    "CNC Machining": ["cnc", "macchine utensili", "tornitura", "fresatura", "fanuc", "siemens sinumerik", "heidenhain"],
    "Industrial Automation": ["automazione industriale", "plc", "scada", "hmi", "robotics", "kuka", "abb", "yaskawa"],
    "Lean Manufacturing": ["lean manufacturing", "kaizen", "5s", "tpm", "smed", "continuous improvement", "toyota production system"],
    "Maintenance Management": ["manutenzione", "maintenance", "gmaw", "tig", "mig", "saldatura", "elettromeccanica"],
    "Quality Management": ["quality management", "sistema qualità", "iso 9001", "iatf 16949", "audit", "non conformity"],

    # ========== DESIGN & ARCHITECTURE (DETAILED) ==========
    "Interior Design": ["interior design", "architettura d'interni", "arredamento", "space planning", "homestaging"],
    "BIM & CAD": ["bim", "revit", "archicad", "autocad", "2d drawing", "technical drawing", "disegno tecnico"],
    "3D Modeling & Rendering": ["3d modeling", "rendering", "sketchup", "rhino", "3ds max", "v-ray", "corona renderer", "lumion"],
    "Restoration": ["restoration", "restauro", "conservazione", "beni culturali", "history of architecture"],

    # ========== BANKING & INSURANCE (DETAILED) ==========
    "Wealth Management": ["wealth management", "gestione patrimoni", "private banking", "portafogli", "asset allocation"],
    "Banking Compliance": ["compliance bancaria", "mifid", "antiriciclaggio", "aml", "kyc", "basel"],
    "Credit Analysis": ["analisi del credito", "credit risk", "rischio di credito", "fidi", "istruttoria"],
    "Insurance Products": ["assicurazioni", "polizze", "ramo danni", "ramo vita", "insurance underwriting", "claims"],

    # ========== ENGINEERING DEEP DIVE (DETAILED) ==========
    "Mechanical Design": ["catia", "solidworks", "creo", "nx", "gd&t", "meccanica", "disegno meccanico"],
    "Simulation (FEA/CFD)": ["ansys", "abaqus", "fem", "cfd", "nastran", "hypermesh", "simulazione"],
    "Automotive Engineering": ["automotive", "powertrain", "chassis", "nvh", "ecu", "calibrazione", "adas", "iso 26262"],
    "Electrical Engineering": ["electrical engineering", "elettrotecnica", "schema elettrico", "medium voltage", "high voltage", "cabine"],
    "Embedded Systems": ["embedded c", "microcontrollers", "stm32", "pic", "fpga", "vhdl", "verilog", "rtos", "firmware"],
    "Civil Engineering": ["ingegneria civile", "strutture", "calcolo strutturale", "direzione lavori", "computo metrico", "primus"],
    "BIM": ["bim", "revit", "navisworks", "archicad", "tekla", "building information modeling"],
    "Energy & Renewables": ["rinnovabili", "fotovoltaico", "eolico", "efficienza energetica", "energy manager", "pvsyst", "high voltage"],

    # ========== BIOTECH, PHARMA & SCIENCE (DETAILED) ==========
    "Clinical Research": ["clinical trials", "studi clinici", "gcp", "good clinical practice", "cra", "ich-gcp"],
    "Regulatory Affairs": ["regulatory affairs", "aifa", "ema", "fda", "dossier", "market access"],
    "Quality Assurance (Pharma)": ["gmp", "good manufacturing practice", "glp", "capa", "change control", "data integrity"],
    "Lab Techniques": ["pcr", "elisa", "westem blot", "hplc", "cell culture", "biologia molecolare", "chromatography"],
    "R&D (Science)": ["ricerca e sviluppo", "r&d", "protocolli", "sperimentazione", "formulazione"],

    # ========== LANGUAGES & TRANSLATION (DETAILED) ==========
    "Translation": ["translation", "traduzione", "trados", "memoq", "post-editing", "mtpe", "localization"],
    "Interpreting": ["interpreting", "interpretariato", "simultanea", "consecutiva", "chuchotage"],
    "Teaching": ["teaching", "insegnamento", "didattica", "docenza", "esl", "tefl"],

    # ========== ECONOMICS & FINANCE (DETAILED) ==========
    "Auditing": ["audit", "revisione legale", "internal audit", "big 4", "isa", "controllo di gestione"],
    "Taxation": ["tax", "fiscalità", "dichiarazione redditi", "transfer pricing", "iva", "vat"],
    "Economics": ["econometrics", "stata", "eviews", "macroeconomics", "economic policy", "antitrust"],
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
    "Software Engineer": {"Programming", "Git", "System Design", "Algorithms", "Testing"}, # Renamed from Software Developer for prestige
    "Frontend Developer": {"JavaScript", "React", "HTML", "CSS", "UI Design", "Git"}, # Added React
    "Backend Developer": {"Python", "Java", "SQL", "Microservices", "System Design", "Redis", "Docker"}, # Removed generic APIs/Cloud to allow specificity
    "Full Stack Developer": {"JavaScript", "Python", "React", "SQL", "Git", "DevOps", "Node.js"}, # Added Node
    "Data Analyst": {"SQL", "Excel", "Data Visualization", "Python", "Statistics"}, # Added Python
    "Data Scientist": {"Python", "Machine Learning", "Deep Learning", "Statistics", "SQL"},
    "Data Engineer": {"SQL", "Python", "Spark", "Cloud Computing", "ETL", "BigQuery"}, # Added Spark/ETL
    "Business Intelligence Analyst": {"Power BI", "Tableau", "SQL", "Data Modelling", "Reporting"},
    "Machine Learning Engineer": {"Python", "Machine Learning", "TensorFlow", "MLOps", "Cloud Computing"}, # New
    "AI Business Analyst": {"Artificial Intelligence", "Business Analysis", "Strategy", "Data Analysis", "Python"}, # New Hybrid
    "UX Designer": {"UX Design", "Figma", "User Research", "Prototyping", "Wireframing"},
    "UI Designer": {"UI Design", "Figma", "Adobe Creative Suite", "Typography", "Visual Design"},
    "DevOps Engineer": {"DevOps", "CI/CD", "Docker", "Kubernetes", "Cloud Computing"},
    "Cybersecurity Analyst": {"Cybersecurity", "Network Security", "Compliance", "Risk Management", "Incident Response"},
    "IT Support Specialist": {"IT Support", "Troubleshooting", "Hardware", "Windows", "Customer Service"},
    "System Administrator": {"Linux", "Windows Server", "Networking", "Cloud Computing", "Scripting"},
    "Product Manager": {"Product Management", "Agile", "User Stories", "Roadmap", "Data Analysis"},
    
    # ========== TECHNOLOGY & DATA (HYBRID) ==========
    "Analytics Engineer": {"SQL", "dbt", "Python", "Data Modeling", "BigQuery", "Snowflake", "Git"},
    "Solutions Architect": {"Cloud Computing", "System Design", "Communication", "Sales", "AWS", "Azure"},
    "Technical Product Manager": {"Product Management", "APIs", "System Design", "Agile", "Data Analysis"},
    "Growth Engineer": {"JavaScript", "Python", "A/B Testing", "Marketing", "Data Analysis", "Automation"},
    "MLOps Engineer": {"Machine Learning", "DevOps", "Docker", "Kubernetes", "Python", "CI/CD"},
    "Legal Tech Specialist": {"Law", "Technology", "Automation", "Legal Research", "Project Management"},
    "FinTech Specialist": {"Finance", "Technology", "Blockchain", "Python", "Data Analysis"},
    
    # ========== MARKETING & COMMUNICATIONS ==========
    "Marketing Manager": {"Marketing Strategy", "Campaign Management", "Budgeting", "Leadership", "Analytics"},
    "Product Marketing Manager": {"Product Management", "Marketing Strategy", "Go-to-Market", "Messaging", "Sales Enablement"},
    "Digital Marketing Specialist": {"Digital Marketing", "SEO", "SEM", "Google Analytics", "Content Marketing"},
    "Marketing Data Analyst": {"Digital Marketing", "Google Analytics", "SQL", "Python", "Data Visualization"}, # New Hybrid
    "Social Media Manager": {"Social Media Marketing", "Content Creation", "Community Management", "Copywriting", "Analytics"},
    "Content Marketing Manager": {"Content Marketing", "SEO", "Copywriting", "Storytelling", "Strategy"},
    "SEO Specialist": {"SEO", "Keyword Research", "Technical SEO", "Google Search Console", "Content Strategy"},
    "PPC Specialist": {"Google Ads", "Facebook Ads", "SEM", "Data Analysis", "ROI Optimization"},
    "Email Marketing Specialist": {"Email Marketing", "Automation", "Copywriting", "A/B Testing", "Segmentation"},
    "Brand Manager": {"Brand Strategy", "Marketing", "Market Research", "Identity", "Communication"},
    "PR Manager": {"Public Relations", "Media Relations", "Press Releases", "Crisis Communication", "Events"},
    "Communications Manager": {"Corporate Communication", "Internal Communication", "PR", "Writing", "Strategy"},
    "Growth Marketing Manager": {"Growth Hacking", "Experimentation", "Data Analysis", "Funnel Optimization", "SEO"},
    
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

    # ========== FASHION & LUXURY (NEW) ==========
    "Fashion Designer": {"Fashion Design", "Textile Knowledge", "Sketching", "Adobe Creative Suite", "Creativity"},
    "Textile Designer": {"Textile Knowledge", "Fashion Design", "Adobe Creative Suite", "Creativity", "Technical Drawing"},
    "Pattern Maker": {"Pattern Making", "Lectra", "Gerber", "Attention to Detail", "Textile Knowledge"},
    "Merchandiser": {"Merchandising", "Data Analysis", "Excel", "Fashion Knowledge", "Detailed Oriented"},
    "Fashion Buyer": {"Buying", "Negotiation", "Trend Analysis", "Fashion Knowledge", "Budgeting"},
    "Visual Merchandiser": {"Visual Merchandising", "Creativity", "Retail Design", "Fashion Knowledge"},
    "Store Manager": {"Retail Management", "Leadership", "Sales", "KPI Analysis", "Customer Service"},
    "Luxury Sales Associate": {"Luxury Retail", "Sales", "Communication", "Clienteling", "Languages"},

    # ========== FOOD & BEVERAGE (NEW) ==========
    "Food Technologist": {"Food Technology", "HACCP", "Quality Control", "R&D", "Lab Skills"},
    "Enologist": {"Enology", "Chemistry", "Sensory Analysis", "Viticulture", "Lab Skills"},
    "Sommelier": {"Enology", "Sensory Analysis", "Communication", "Sales", "Customer Service"},
    "Agronomist": {"Agronomy", "Technical Knowledge", "Project Management", "Sustainability"},
    "F&B Manager": {"F&B Management", "Food Cost", "Leadership", "Budgeting", "Customer Service"},
    "Executive Chef": {"Cooking", "Kitchen Management", "Food Cost", "Leadership", "Creativity"},
    "Quality Manager (Food)": {"Quality Management", "HACCP", "ISO 22000", "Auditing", "Compliance"},

    # ========== MANUFACTURING 4.0 (NEW) ==========
    "Plant Manager": {"Manufacturing", "Leadership", "Lean Manufacturing", "Budgeting", "Operations"},
    "Production Planner": {"Production Planning", "Excel", "Supply Chain", "ERP", "Organization"},
    "Maintenance Manager": {"Maintenance Management", "Leadership", "Problem Solving", "Technical Knowledge"},
    "Process Engineer": {"Process Engineering", "Lean Manufacturing", "Six Sigma", "Data Analysis"},
    "Automation Engineer": {"Industrial Automation", "PLC", "Robotics", "SCADA", "Programming"},
    "CNC Programmer": {"CNC Machining", "Technical Drawing", "CAD/CAM", "Precision"},
    "Quality Manager": {"Quality Management", "ISO 9001", "Auditing", "Continuous Improvement"},

    # ========== DESIGN & ARCHITECTURE (NEW) ==========
    "Interior Designer": {"Interior Design", "AutoCAD", "SketchUp", "Rendering", "Creativity"},
    "Architect": {"Architecture", "BIM", "Revit", "AutoCAD", "Project Management"},
    "Landscape Architect": {"Architecture", "Botany", "AutoCAD", "Design", "Sustainability"},
    "Restoration Architect": {"Restoration", "Architecture", "History", "Materials Science"},
    
    # ========== BANKING & FINANCE (NEW) ==========
    "Private Banker": {"Wealth Management", "Sales", "Financial Analysis", "Relationship Management", "Regulations"},
    "Branch Manager": {"Banking", "Leadership", "Sales", "Operations", "Customer Service"},
    "Credit Risk Analyst": {"Credit Analysis", "Risk Management", "Financial Analysis", "Excel", "Compliance"},
    "Insurance Underwriter": {"Insurance Products", "Risk Analysis", "Data Analysis", "Decision Making"},

    # ========== ENGINEERING DEEP DIVE (NEW ARCHETYPES) ==========
    "Mechanical Engineer (Auto)": {"Mechanical Design", "Automotive Engineering", "CATIA", "Simulink", "Problem Solving"},
    "NVH Engineer": {"Automotive Engineering", "Simulation (FEA/CFD)", "Matlab", "Testing", "Data Analysis"},
    "Embedded Software Engineer": {"Embedded Systems", "C++", "Electronics", "Debugging", "RTOS"},
    "Firmware Engineer": {"Embedded Systems", "C", "Microcontrollers", "Hardware", "Testing"},
    "Electrical Design Engineer": {"Electrical Engineering", "AutoCAD", "Eplan", "Project Management"},
    "Renewable Energy Engineer": {"Energy & Renewables", "Project Management", "AutoCAD", "Sustainability"},
    "Civil Structural Engineer": {"Civil Engineering", "Structural Analysis", "AutoCAD", "Revit", "Attention to Detail"},
    "BIM Manager": {"BIM", "Revit", "Navisworks", "Coordination", "Project Management"},
    "Site Manager": {"Civil Engineering", "Construction Management", "Leadership", "Safety", "Problem Solving"},

    # ========== BIOTECH & PHARMA (NEW ARCHETYPES) ==========
    "Clinical Research Associate (CRA)": {"Clinical Research", "GCP", "Organization", "Travel", "Medical Terminology"},
    "Regulatory Affairs Specialist": {"Regulatory Affairs", "Documentation", "Attention to Detail", "Legal Knowledge"},
    "QC Micro Analyst": {"Quality Assurance (Pharma)", "Lab Techniques", "Microbiology", "GMP", "Precision"},
    "R&D Scientist": {"R&D (Science)", "Lab Techniques", "Data Analysis", "Innovation", "Problem Solving"},
    "Medical Science Liaison": {"Medical Knowledge", "Communication", "Presentation", "Relationship Building"},

    # ========== LANGUAGES & TRANSLATION (NEW ARCHETYPES) ==========
    "Translator": {"Translation", "Writing", "Attention to Detail", "Cultural Knowledge", "CAT Tools"},
    "Interpreter": {"Interpreting", "Public Speaking", "Stress Management", "Active Listening", "Memory"},
    "Localization Specialist": {"Translation", "Tech Savvy", "Project Management", "Cultural Knowledge"},
    "Language Teacher": {"Teaching", "Communication", "Patience", "Creativity", "Empathy"},

    # ========== ECONOMICS & FINANCE (NEW ARCHETYPES) ==========
    "Auditor (Big 4)": {"Auditing", "Accounting", "Excel", "Attention to Detail", "Teamwork"},
    "Tax Consultant": {"Taxation", "Law", "Problem Solving", "Attention to Detail", "Communication"},
    "Transfer Pricing Specialist": {"Taxation", "Economics", "Writing", "Data Analysis", "Excel"},
    "Economist": {"Economics", "Data Analysis", "Statistics", "Research", "Writing"},

    # ========== ENERGY ENGINEERING & TRADING (NEW ARCHETYPES) ==========
    "Energy Engineer": {"Thermodynamics", "Energy & Renewables", "MATLAB", "Simulation", "Excel", "Python"},
    "Energy Analyst": {"Energy Markets", "Data Analysis", "Python", "Excel", "Energy Forecasting", "SQL"},
    "Energy Trader": {"Energy Trading", "Energy Markets", "Python", "Data Analysis", "Excel", "Energy Forecasting", "MATLAB"},
    "Power Market Analyst": {"Energy Markets", "Grid Operators", "Python", "Energy Forecasting", "Data Analysis", "Statistics"},
    "Energy Consultant": {"Energy & Renewables", "Data Analysis", "Excel", "Project Management", "Communication", "Sustainability"},
    "Aerospace Engineer": {"Aerospace Propulsion", "MATLAB", "Thermodynamics", "Simulation", "CAD", "Python"},
    "Gas Turbine Engineer": {"Thermodynamics", "Aerospace Propulsion", "Simulation", "Mechanical Engineering", "MATLAB"},
    "Quantitative Energy Analyst": {"Energy Markets", "Python", "Statistics", "Financial Analysis", "Energy Trading", "Machine Learning"},
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

# =============================================================================
# CAREER DISCOVERY - Role Metadata for Smart Matching
# =============================================================================
# Maps job roles to preferences for the Career Discovery questionnaire
# Categories: Technology, Marketing, Business, Finance, HR, Sales, Legal, 
#             Design, Engineering, Supply Chain, Healthcare, Hospitality, Education

JOB_ROLE_METADATA = {
    # ========== TECHNOLOGY ==========
    "Software Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Frontend Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Backend Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Full Stack Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Data Analyst": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Data Scientist": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Data Engineer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Business Intelligence Analyst": {"category": "Technology", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "UX Designer": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "UI Designer": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "DevOps Engineer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Cybersecurity Analyst": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "IT Support Specialist": {"category": "Technology", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "System Administrator": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Product Manager": {"category": "Business", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # ========== MARKETING & COMMUNICATIONS ==========
    "Marketing Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Digital Marketing Specialist": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Social Media Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Content Marketing Manager": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "SEO Specialist": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "PPC Specialist": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Email Marketing Specialist": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Brand Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "PR Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Communications Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Marketing Analyst": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Growth Marketing Manager": {"category": "Marketing", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # ========== BUSINESS & MANAGEMENT ==========
    "Project Manager": {"category": "Business", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Business Analyst": {"category": "Business", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Management Consultant": {"category": "Business", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Operations Manager": {"category": "Business", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "General Manager": {"category": "Business", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Strategy Analyst": {"category": "Business", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Business Development Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Program Manager": {"category": "Business", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Office Manager": {"category": "Business", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": False, "creative": False},
    "Executive Assistant": {"category": "Business", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    
    # ========== FINANCE & ACCOUNTING ==========
    "Financial Analyst": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Accountant": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Senior Accountant": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Controller": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "CFO": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Auditor": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "Tax Specialist": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Treasury Analyst": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Investment Analyst": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Credit Analyst": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Risk Analyst": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Financial Planner": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    
    # ========== HUMAN RESOURCES ==========
    "HR Manager": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "HR Business Partner": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Recruiter": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Talent Acquisition Specialist": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Training Manager": {"category": "HR", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": True},
    "Compensation & Benefits Specialist": {"category": "HR", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "HR Generalist": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": True, "creative": False},
    "People Operations Manager": {"category": "HR", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # ========== SALES ==========
    "Sales Representative": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Account Executive": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Sales Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Account Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Business Development Representative": {"category": "Sales", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Key Account Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Sales Director": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Inside Sales Representative": {"category": "Sales", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": True, "creative": False},
    "E-commerce Manager": {"category": "Sales", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Retail Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Export Manager": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    
    # ========== LEGAL ==========
    "Lawyer": {"category": "Legal", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Corporate Lawyer": {"category": "Legal", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Legal Counsel": {"category": "Legal", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Compliance Officer": {"category": "Legal", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Paralegal": {"category": "Legal", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Contract Manager": {"category": "Legal", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Privacy Officer": {"category": "Legal", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    
    # ========== DESIGN & CREATIVE ==========
    "Graphic Designer": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Senior Graphic Designer": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Art Director": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Creative Director": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "UX/UI Designer": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Product Designer": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Web Designer": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Motion Designer": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Video Editor": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Photographer": {"category": "Design", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Copywriter": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Content Creator": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # ========== ENGINEERING ==========
    "Mechanical Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Electrical Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Civil Engineer": {"category": "Engineering", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": False, "creative": False},
    "Industrial Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Chemical Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Process Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Quality Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "Maintenance Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "HSE Manager": {"category": "Engineering", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Production Manager": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "R&D Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    
    # ========== SUPPLY CHAIN & LOGISTICS ==========
    "Supply Chain Manager": {"category": "Supply Chain", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Logistics Manager": {"category": "Supply Chain", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Procurement Manager": {"category": "Supply Chain", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "Supply Chain Analyst": {"category": "Supply Chain", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Logistics Coordinator": {"category": "Supply Chain", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Warehouse Manager": {"category": "Supply Chain", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Purchasing Specialist": {"category": "Supply Chain", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Import/Export Specialist": {"category": "Supply Chain", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Demand Planner": {"category": "Supply Chain", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    
    # ========== HEALTHCARE & PHARMA ==========
    "Clinical Research Associate": {"category": "Healthcare", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Regulatory Affairs Specialist": {"category": "Healthcare", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Medical Science Liaison": {"category": "Healthcare", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Pharmacovigilance Specialist": {"category": "Healthcare", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Medical Sales Representative": {"category": "Healthcare", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Quality Assurance (Pharma)": {"category": "Healthcare", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "Healthcare Administrator": {"category": "Healthcare", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Clinical Data Manager": {"category": "Healthcare", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Nurse": {"category": "Healthcare", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    
    # ========== HOSPITALITY & TOURISM ==========
    "Hotel Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Front Office Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Revenue Manager": {"category": "Hospitality", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Event Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Restaurant Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Tour Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Concierge": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Guest Relations Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "F&B Manager": {"category": "Hospitality", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": True},
    
    # ========== EDUCATION ==========
    "Teacher": {"category": "Education", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": True},
    "University Professor": {"category": "Education", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Corporate Trainer": {"category": "Education", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Instructional Designer": {"category": "Education", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Academic Coordinator": {"category": "Education", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    
    # ========== CUSTOMER SERVICE ==========
    "Customer Service Representative": {"category": "Customer Service", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": True, "creative": False},
    "Customer Service Manager": {"category": "Customer Service", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Call Center Agent": {"category": "Customer Service", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": True, "creative": False},
    "Technical Support Specialist": {"category": "Technology", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    
    # ========== ADMINISTRATION ==========
    "Administrative Assistant": {"category": "Administration", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Receptionist": {"category": "Administration", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Data Entry Specialist": {"category": "Administration", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Personal Assistant": {"category": "Administration", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    
    # ========== OTHER ==========
    "Construction Manager": {"category": "Engineering", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Architect": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Real Estate Agent": {"category": "Sales", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Property Manager": {"category": "Business", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Facility Manager": {"category": "Business", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Actuary": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Underwriter": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Claims Adjuster": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": True, "creative": False},
    "Insurance Broker": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Journalist": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Lab Technician": {"category": "Healthcare", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "QC Analyst": {"category": "Healthcare", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},
    "Research Scientist": {"category": "Healthcare", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    
    # ========== FASHION & LUXURY (NEW) ==========
    "Fashion Designer": {"category": "Fashion", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Merchandiser": {"category": "Fashion", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Fashion Buyer": {"category": "Fashion", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Store Manager": {"category": "Fashion", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Luxury Sales Associate": {"category": "Fashion", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    
    # ========== FOOD & BEVERAGE (NEW) ==========
    "Food Technologist": {"category": "Food & Beverage", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Enologist": {"category": "Food & Beverage", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "F&B Manager": {"category": "Food & Beverage", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Agronomist": {"category": "Food & Beverage", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},

    # ========== MANUFACTURING & INDUSTRY (NEW) ==========
    "Plant Manager": {"category": "Manufacturing", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Maintenance Manager": {"category": "Manufacturing", "client_facing": False, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    "Automation Engineer": {"category": "Manufacturing", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Quality Manager": {"category": "Manufacturing", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": False},

    # ========== DESIGN & ARCHITECTURE (NEW) ==========
    "Interior Designer": {"category": "Design", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Architect": {"category": "Design", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    
    # ========== BANKING (NEW) ==========
    "Private Banker": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Branch Manager": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": False, "dynamic": True, "creative": False},
    
    # ========== ENGINEERING DEEP DIVE (NEW METADATA) ==========
    "Mechanical Engineer (Auto)": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "NVH Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Embedded Software Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Firmware Engineer": {"category": "Engineering", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
    "Renewable Energy Engineer": {"category": "Engineering", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "BIM Manager": {"category": "Engineering", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # ========== BIOTECH & PHARMA (NEW METADATA) ==========
    "Clinical Research Associate (CRA)": {"category": "Healthcare", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "Regulatory Affairs Specialist": {"category": "Healthcare", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "R&D Scientist": {"category": "Healthcare", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    
    # ========== LANGUAGES (NEW METADATA) ==========
    "Translator": {"category": "Languages", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Interpreter": {"category": "Languages", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": True},
    "Localization Specialist": {"category": "Languages", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    
    # ========== ECONOMICS (NEW METADATA) ==========
    "Auditor (Big 4)": {"category": "Finance", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Tax Consultant": {"category": "Finance", "client_facing": True, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    "Economist": {"category": "Finance", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
}

# Career Discovery Categories with descriptions
CAREER_CATEGORIES = {
    "Technology": "Software, data, IT, cybersecurity, and digital infrastructure",
    "Marketing": "Digital marketing, branding, communications, and growth",
    "Business": "Management, consulting, operations, and strategy",
    "Finance": "Accounting, financial analysis, investment, and risk",
    "HR": "Recruiting, talent management, training, and people operations",
    "Sales": "B2B/B2C sales, account management, and business development",
    "Legal": "Corporate law, compliance, contracts, and regulatory",
    "Design": "UX/UI, graphic design, creative direction, and content",
    "Engineering": "Mechanical, electrical, industrial, and process engineering",
    "Supply Chain": "Logistics, procurement, warehouse, and demand planning",
    "Healthcare": "Clinical research, pharma, medical sales, and quality",
    "Hospitality": "Hotels, events, tourism, and food & beverage",
    "Education": "Teaching, training, instructional design, and academia",
    "Customer Service": "Support, call centers, and client relations",
    "Administration": "Office management, data entry, and executive assistance",
    "Fashion": "Design, merchandising, buying, and luxury retail",
    "Food & Beverage": "Food tech, enology, Horeca management, and agronomy",
    "Manufacturing": "Industry 4.0, automation, quality, and plant management",
    "Languages": "Translation, interpreting, localization, and teaching",
}
