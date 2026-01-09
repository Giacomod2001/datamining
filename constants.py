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
    # --- TECHNOLOGY & IT ---
    "React": ["JavaScript", "Frontend Development", "Web Development", "UI Design"],
    "Vue": ["JavaScript", "Frontend Development", "Web Development"],
    "Angular": ["JavaScript", "Frontend Development", "Web Development", "TypeScript"],
    "TypeScript": ["JavaScript", "Frontend Development"],
    "Django": ["Python", "Backend Development", "Web Development", "API Development"],
    "Flask": ["Python", "Backend Development", "Web Development", "API Development"],
    "Spring": ["Java", "Backend Development", "OOP", "API Development"],
    "Hibernate": ["Java", "Database Management", "ORM"],
    "AWS": ["Cloud Computing", "Infrastructure", "DevOps"],
    "Azure": ["Cloud Computing", "Infrastructure", "Enterprise IT"],
    "GCP": ["Cloud Computing", "Infrastructure", "Google Cloud"],
    "Docker": ["DevOps", "Containerization", "Deployment", "Infrastructure"],
    "Kubernetes": ["DevOps", "Containerization", "Orchestration"],
    "Terraform": ["DevOps", "Infrastructure as Code", "Cloud Computing"],
    "Git": ["Version Control", "Collaboration", "Software Development"],
    "Linux": ["Operating Systems", "System Administration", "DevOps"],

    # --- MARKETING & DIGITAL ---
    "Google Ads": ["SEM", "Digital Marketing", "Paid Advertising", "PPC", "Marketing Strategy"],
    "Facebook Ads": ["Social Media Marketing", "Digital Marketing", "Paid Advertising", "Marketing Strategy"],
    "LinkedIn Ads": ["B2B Marketing", "Social Media Marketing", "Paid Advertising"],
    "Google Analytics": ["Data Analysis", "Web Analytics", "Digital Marketing", "Reporting"],
    "GA4": ["Data Analysis", "Web Analytics", "Google Analytics"],
    "SEO": ["Digital Marketing", "Content Marketing", "Website Optimization", "Organic Growth"],
    "HubSpot": ["CRM", "Marketing Automation", "Inbound Marketing", "Lead Generation"],
    "Salesforce": ["CRM", "Sales Management", "Customer Relations", "Pipeline Management"],
    "Copywriting": ["Content Marketing", "Writing", "Communication", "Marketing"],
    
    # --- BUSINESS & MANAGEMENT ---
    "Jira": ["Project Management", "Agile", "Organization", "Task Management"],
    "Trello": ["Project Management", "Organization", "Kanban"],
    "Asana": ["Project Management", "Organization", "Task Management"],
    "Scrum": ["Agile", "Project Management", "Team Leadership"],
    "Kanban": ["Agile", "Project Management", "Process Improvement"],
    "Budgeting": ["Financial Analysis", "Management", "Strategic Planning"],
    "Stakeholder Management": ["Communication", "Leadership", "Relationship Building"],
    
    # --- FINANCE & ACCOUNTING ---
    "Financial Reporting": ["Accounting", "Excel", "Compliance"],
    "Auditing": ["Accounting", "Compliance", "Financial Reporting", "Internal Controls"],
    "Tax": ["Accounting", "Compliance", "Financial Reporting"],
    "Financial Modeling": ["Excel", "Valuation", "Corporate Finance", "Investment Analysis"],
    "SAP": ["ERP", "Accounting", "Business Processes"],
    "Oracle Financials": ["ERP", "Accounting", "Financial Reporting"],
    "IFRS": ["Accounting", "Financial Reporting", "Compliance"],
    "GAAP": ["Accounting", "Financial Reporting", "Compliance"],
    
    # --- DESIGN & CREATIVE ---
    "Adobe Photoshop": ["Graphic Design", "Image Editing", "Visual Design", "Adobe Creative Suite"],
    "Adobe Illustrator": ["Graphic Design", "Vector Design", "Branding", "Adobe Creative Suite"],
    "Adobe InDesign": ["Graphic Design", "Layout", "Publishing", "Adobe Creative Suite"],
    "Figma": ["UI Design", "UX Design", "Prototyping", "Web Design"],
    "Sketch": ["UI Design", "UX Design", "Prototyping"],
    "Premiere Pro": ["Video Editing", "Content Creation", "Adobe Creative Suite"],
    "After Effects": ["Motion Graphics", "Video Editing", "Animation"],
    
    # --- LEGAL ---
    "GDPR": ["Compliance", "Privacy Law", "Data Protection", "Legal Research"],
    "M&A": ["Corporate Law", "Due Diligence", "Legal Contracts", "Corporate Finance"],
    "Contract Law": ["Legal Research", "Negotiation", "Documentation"],
    
    # --- ANALYTICAL CHEMISTRY & QC LAB (NEW) ---
    "HPLC": ["Chromatography", "Analytical Chemistry", "Lab Skills", "QC Lab"],
    "Gas Chromatography": ["Chromatography", "Analytical Chemistry", "Lab Skills", "QC Lab"],
    "Spectroscopy": ["Analytical Chemistry", "Lab Skills", "Material Analysis"],
    "Western Blot": ["Protein Analysis", "Lab Skills", "Molecular Biology"],
    "ELISA": ["Protein Analysis", "Lab Skills", "Immunoassay"],
    "PCR": ["Molecular Techniques", "Lab Skills", "Molecular Biology"],
    "qPCR": ["Molecular Techniques", "Lab Skills", "Molecular Biology", "PCR"],
    "GMP": ["Quality Management", "Compliance", "Pharma", "Manufacturing"],
    "GLP": ["Quality Management", "Compliance", "Lab Safety", "Research"],
    "ISO 22716": ["Cosmetic Regulations", "Quality Management", "GMP"],
    "Cosmetic Regulations": ["Regulatory", "Compliance", "Quality Control"],
    "CLP Regulation": ["Regulatory", "Compliance", "Safety", "Chemical Safety"],
    "Microbiological Analysis": ["Lab Skills", "Quality Control", "Microbiology"],
    
    # --- HR & RECRUITING (DETAILED) ---
    "Recruiting": ["Talent Acquisition", "Interviewing", "HR Management", "Communication"],
    "Sourcing": ["Recruiting", "Talent Acquisition", "LinkedIn Recruiter", "Boolean Search"],
    "Headhunting": ["Recruiting", "Executive Search", "Networking", "Sourcing"],
    "ATS Management": ["Recruiting", "Data Analysis", "HRIS", "Process Optimization"],
    "HR Management": ["Employee Relations", "Labor Law", "Performance Management", "Organizational Development"],
    "Payroll": ["Accounting", "HR Management", "Compliance", "Excel", "Admin"],
    "Labor Law": ["HR Management", "Compliance", "Legal", "Industrial Relations"],
    "Compensation & Benefits": ["HR Management", "Payroll", "Data Analysis", "Total Rewards"],
    "Training & Development": ["HR Management", "Public Speaking", "Mentoring", "Education", "L&D"],
    "Talent Management": ["HR Management", "Leadership", "Succession Planning", "Employee Engagement"],
    
    # --- SUPPLY CHAIN & LOGISTICS (DETAILED) ---
    "Supply Chain Management": ["Logistics", "Procurement", "Inventory Management", "Operations Management"],
    "Logistics": ["Transportation", "Warehouse Management", "Inventory Management", "Supply Chain Management"],
    "Fleet Management": ["Logistics", "Transportation", "Operations"],
    "Warehouse Management": ["Logistics", "Inventory Management", "Safety", "WMS"],
    "Procurement": ["Negotiation", "Vendor Management", "Supply Chain Management", "Purchasing", "Sourcing"],
    "Strategic Sourcing": ["Procurement", "Negotiation", "Market Research", "Cost Analysis"],
    "Vendor Management": ["Procurement", "Relationship Management", "Supply Chain Management"],
    "Demand Planning": ["Supply Chain Management", "Data Analysis", "Forecasting", "Inventory Management"],
    "Inventory Management": ["Supply Chain Management", "Logistics", "Data Analysis"],
    "SAP": ["ERP", "Logistics", "Inventory Management", "Business Processes"],
    
    # --- HOSPITALITY & TOURISM (DETAILED) ---
    "Hotel Management": ["Hospitality", "Customer Service", "Operations Management", "Team Leadership"],
    "Front Office": ["Customer Service", "Reception", "Hospitality", "Communication"],
    "Housekeeping Management": ["Hospitality", "Operations Management", "Quality Control"],
    "F&B Management": ["Hospitality", "Customer Service", "Budgeting", "Food Safety"],
    "HACCP": ["Food Safety", "Compliance", "Quality Control"],
    "Menu Engineering": ["F&B Management", "Marketing", "Cost Control"],
    "Tourism": ["Travel Planning", "Customer Service", "Geography", "Languages"],
    "Ticketing": ["Travel Planning", "Customer Service", "GDS"],
    "GDS": ["Ticketing", "Travel Planning"],
    
    # --- EDUCATION & TRAINING ---
    "Teaching": ["Communication", "Public Speaking", "Mentoring", "Curriculum Development"],
    "Training Delivery": ["Public Speaking", "Presentation", "Facilitation", "Adult Learning"],
    "Curriculum Development": ["Teaching", "Instructional Design", "Planning"],
    "E-Learning": ["Instructional Design", "LMS", "Digital Literacy", "Training & Development"],
    
    # --- CUSTOMER SERVICE & RETAIL ---
    "Customer Service": ["Communication", "Problem Solving", "Conflict Resolution", "Empathy"],
    "Retail": ["Sales", "Customer Service", "Inventory Management", "Merchandising"],
    "Visual Merchandising": ["Retail", "Creativity", "Design", "Marketing"],
    
    # --- BIOTECH & SCIENCE (DETAILED) ---
    "Biotechnology": ["Biology", "Chemistry", "Life Sciences", "Lab Skills"],
    "Molecular Biology": ["Biology", "Genetics", "Lab Skills", "PCR", "Research"],
    "PCR": ["Molecular Biology", "Lab Skills", "Genetics"],
    "Cell Culture": ["Biology", "Lab Skills", "Sterile Technique", "Research"],
    "Western Blot": ["Molecular Biology", "Lab Skills", "Protein Analysis"],
    "Bioinformatics": ["Biology", "Computer Science", "Data Analysis", "Genomics", "Python", "R"],
    "Genetics": ["Biology", "Molecular Biology", "Research"],
    "Clinical Research": ["Healthcare", "GCP", "Data Analysis", "Regulatory Affairs"],
    "Regulatory Affairs": ["Compliance", "Healthcare", "Legal", "Life Sciences", "FDA/EMA"],
    "Pharmacovigilance": ["Healthcare", "Drug Safety", "Compliance"],
    
    # --- LANGUAGES (DETAILED) ---
    "Translation": ["Languages", "Writing", "Intercultural Communication"],
    "Interpretation": ["Languages", "Public Speaking", "Active Listening", "Memory"],
    "Simultaneous Interpretation": ["Interpretation", "Concentration", "Multitasking"],
    "CAT Tools": ["Translation", "Technology", "Localization"],
    "Business English": ["English", "Business Communication"],
    "Localization": ["Translation", "Cultural Adaptation", "Tech"],
    
    # --- ENGINEERING (SPECIALIZED) ---
    "Mechanical Engineering": ["Engineering", "Physics", "Math", "CAD"],
    "Energy Engineering": ["Engineering", "Sustainability", "Physics"],
    "Renewable Energy": ["Energy Engineering", "Sustainability", "Environmental Science"],
    "Mechatronics": ["Mechanical Engineering", "Electronics", "Computer Science", "Robotics"],
    "Robotics": ["Mechatronics", "Automation", "Programming"],
    "PLC Programming": ["Automation", "Electrical Engineering", "Control Systems"],
    "PLC": ["Automation", "Industrial Engineering"],
    "CAD": ["Design", "Engineering", "Technical Drawing", "Modeling"],
    "SolidWorks": ["CAD", "Mechanical Engineering", "3D Modeling"],
    "Simulation": ["Engineering", "Analysis", "Math"],
    
    # --- ADVANCED FINANCE & IT ---
    "Quantitative Finance": ["Finance", "Math", "Statistics", "Programming"],
    "Algorithmic Trading": ["Quantitative Finance", "Programming", "Data Analysis"],
    "Stochastic Calculus": ["Math", "Quantitative Finance"],
    "Quantum Computing": ["Computer Science", "Physics", "Math"],
    "Cybersecurity": ["IT", "Risk Management", "System Administration"],
    "Algorithms": ["Computer Science", "Programming", "Logic"],
    "Accounting": ["Finance", "Math", "Compliance", "Detail Oriented"],
    "Financial Analysis": ["Finance", "Excel", "Data Analysis"],
    
    # --- MARKETING & SALES (NEW) ---
    "SEO": ["Digital Marketing", "Analytics", "Content Strategy"],
    "SEM": ["Digital Marketing", "Advertising", "Analytics"],
    "Content Marketing": ["Marketing", "Writing", "Creativity"],
    "Social Media": ["Marketing", "Communication", "Community Management"],
    "Sales": ["Communication", "Negotiation", "Customer Service"],
    "Tech Sales": ["Sales", "Technology", "Presentation"],
    "CRM": ["Sales", "Data Management", "Organization"],

    # --- LEGAL (NEW) ---
    "Corporate Law": ["Legal", "Contract Law", "Business"],
    "IP Law": ["Legal", "Intellectual Property", "Research"],
    # --- CONSTRUCTION & REAL ESTATE ---
    "Construction Management": ["Project Management", "Engineering", "Leadership"],
    "Architecture": ["Design", "Creativity", "Engineering", "Software"],
    "BIM": ["Architecture", "Engineering", "Software", "Construction Management"],
    "Real Estate": ["Sales", "Negotiation", "Finance", "Customer Service"],
    "Facility Management": ["Operations", "Maintenance", "Management"],

    # --- INSURANCE & ACTUARIAL ---
    "Actuarial Science": ["Math", "Statistics", "Finance", "Risk Management"],
    "Underwriting": ["Insurance", "Risk Management", "Analysis", "Finance"],
    "Claims": ["Insurance", "Customer Service", "Negotiation", "Problem Solving"],
    
    # --- CREATIVE & MEDIA ---
    "Video Production": ["Creativity", "Technology", "Storytelling", "Art"],
    "Audio Engineering": ["Technology", "Music", "Creativity"],
    "Journalism": ["Writing", "Communication", "Research", "Media"],
    
    # --- EDUCATION ---
    "Instructional Design": ["Education", "Technology", "Creativity", "Training"],
    "Special Education": ["Teaching", "Patience", "Communication", "Empathy"],
    
    # --- MANUFACTURING ---
    "Lean Manufacturing": ["Manufacturing", "Process Improvement", "Efficiency"],
    "Quality Assurance": ["Quality Control", "Compliance", "Attention to Detail"],
    "Six Sigma": ["Process Improvement", "Statistics", "Quality Management"],
    
    # --- SCIENCE & QUALITY ---
    # GMP/GLP - Reduced to prevent over-matching (was: 5 inferences each)
    "GMP": ["Quality Management", "Compliance"],
    "GLP": ["Quality Management", "Lab Safety"],
    "Data Analysis": ["Statistics", "Excel", "Reporting"],
    "Biotechnology": ["Biology", "Chemistry", "Life Sciences", "Lab Skills", "Microbiology"],
    "Microbiology": ["Biology", "Lab Skills", "Quality Control"],
    "Molecular Biology": ["Biology", "Genetics", "Lab Skills"],
    "Spectrophotometry": ["Analytical Chemistry", "Lab Skills"],
    "Western Blot": ["Biology", "Lab Skills", "Molecular Biology"],
    # Note: HPLC/PCR inference rules are defined above in the ANALYTICAL CHEMISTRY section
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

    # ========== BIOTECHNOLOGY & LIFE SCIENCES (DETAILED) ==========
    "Biotechnology": ["biotechnology", "life sciences", "pharma"],
    
    # Molecular Biology (Killer Keywords)
    "Gene Editing": ["crispr", "crispr/cas9", "gene editing", "genome engineering", "talens", "zinc finger nucleases"],
    "Molecular Techniques": ["cloning", "plasmid design", "site-directed mutagenesis", "transfection", "rna interference", "qpcr"],
    "Sequencing": ["ngs", "next-generation sequencing", "illumina", "sanger sequencing", "library preparation", "rna-seq", "scrna-seq"],
    "Protein Analysis": ["western blot", "elisa", "protein purification", "chromatography", "akts", "sds-page", "mass spectrometry"],
    
    # Cell Biology (Killer Keywords)
    "Cell Culture": ["mammalian cell culture", "primary cells", "stem cells", "ipsc", "organoids", "3d culture"],
    "Cytometry": ["flow cytometry", "facs", "cell sorting", "immunophenotyping", "gating strategies"],
    "Microscopy": ["confocal microscopy", "fluorescence microscopy", "live cell imaging", "sem", "tem", "imagej"],
    
    # Bioinformatics (Killer Keywords)
    "Bioinformatics": ["bioinformatics", "computational biology", "genomics", "metagenomics", "phylogenetics"],
    "Structural Biology": ["pymol", "chimera", "molecular docking", "molecular dynamics", "alphafold", "rosetta"],
    "Bio-Scripting": ["biopython", "bioconductor", "r programming", "bash scripting", "pipeline development"],

    # Pharma & Clinical
    "Clinical Trials": ["clinical trials", "clinical development", "gcp", "ich-gcp", "clinical data management", "edc"],
    "Regulatory": ["regulatory affairs", "fda submissions", "ema", "ind", "nda", "medical device regulation", "iso 13485"],

    # ========== ANALYTICAL CHEMISTRY & QC LAB (NEW - Killer Keywords) ==========
    # These are DISTINCT from molecular biology - required for QC/Lab Technician roles
    
    "HPLC": ["hplc", "high performance liquid chromatography", "uplc"],
    "Gas Chromatography": ["gas chromatography", "gc-ms", "gascromatografia"],
    "Spectroscopy": ["spectroscopy", "uv-vis", "ir spectroscopy", "nmr", "mass spectrometry", "spettrometria"],
    "Titration": ["titration", "titolazione", "volumetric analysis", "acid-base titration"],
    "Sample Preparation": ["sample preparation", "preparazione campioni", "extraction", "filtration", "homogenization"],
    
    # Quality Control Lab Specific (Removed QC Lab - too generic, "controllo qualità" matches everything)
    "Analytical Method Validation": ["method validation", "validazione metodo", "analytical validation", "icq q2"],
    "Stability Testing": ["stability testing", "test stabilità", "accelerated stability", "shelf life"],
    "Microbiological Analysis": ["microbiological analysis", "analisi microbiologiche", "microbial testing", "bioburden"],
    "Raw Material Testing": ["raw material testing", "materie prime", "incoming inspection", "material qualification"],
    
    # Cosmetic & Detergent Industry Specific
    "Cosmetic Regulations": ["cosmetic regulation 1223/2009", "regolamento cosmetico", "1223/2009", "cosmetic gmp"],
    "CLP Regulation": ["clp regulation", "clp 1272/2008", "1272/2008", "classification labeling packaging", "ghs"],
    "ISO 22716": ["iso 22716", "cosmetic gmp", "good manufacturing practice cosmetics"],
    "Detergent Testing": ["detergent testing", "detergenza", "surfactant analysis", "cleaning validation"],
    
    # ISO Standards (Lab Specific)
    "ISO 9001": ["iso 9001", "quality management system", "sistema gestione qualità"],
    "ISO 14001": ["iso 14001", "environmental management", "gestione ambientale"],
    "ISO 17025": ["iso 17025", "lab accreditation", "laboratory accreditation", "accreditamento laboratorio"],

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
    "Formulation Chemist": {"Chemistry", "Formulation", "Lab Skills", "QC Lab", "Product Development"},
    "Cosmetic Chemist": {"Chemistry", "Cosmetic Regulations", "ISO 22716", "Formulation", "Quality Control"},
    "Regulatory Affairs Specialist (Pharma)": {"Regulatory", "Compliance", "GMP", "Clinical Trials", "Documentation"},
    "Microbiologist": {"Microbiology", "Lab Skills", "Microbiological Analysis", "Quality Control", "GLP"},
}
