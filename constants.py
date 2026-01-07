"""
================================================================================
CareerMatch AI - Knowledge Base (constants.py)
================================================================================

This file contains the KNOWLEDGE BASE of the application, strictly limited
to concepts from the course material "DATA MINING E TEXT.txt".

================================================================================
"""

# =============================================================================
# INFERENCE RULES (Based on course material)
# =============================================================================
INFERENCE_RULES = {
    # Data Mining Process
    "KDD": ["Data Cleaning", "Data Integration", "Data Transformation", "Data Mining", "Pattern Evaluation", "Knowledge Presentation"],
    "Data Mining": ["Pattern Discovery", "Knowledge Discovery"],
    
    # Techniques
    "Clustering": ["Unsupervised Learning", "K-Means", "Hierarchical Clustering"],
    "Classification": ["Supervised Learning", "Decision Tree", "Random Forest", "Neural Network", "Rule-Based Classifier"],
    "Regression": ["Supervised Learning", "Prediction", "Linear Regression"],
    "Association Analysis": ["Pattern Discovery", "Frequent Patterns", "Market Basket Analysis"],
    
    # Databases
    "Data Warehouse": ["OLAP", "Data Integration", "Historical Data"],
    "Data Lake": ["Unstructured Data", "Big Data", "Raw Data"],
    "Database": ["SQL", "Data Management", "Structured Data"],
    
    # Specific Tools/Concepts found in text
    "SQL": ["Query", "Select", "Join", "Database"],
    "Excel": ["Spreadsheet", "Data Analysis"],
    "Python": ["Data Analysis", "Machine Learning"], # Inferring Python as the tool for these, though text focuses on concepts
}

# =============================================================================
# SKILL CLUSTERS (Conceptual groupings from course)
# =============================================================================
SKILL_CLUSTERS = {
    "Supervised Learning": {"Classification", "Regression", "Decision Tree", "Random Forest", "Neural Network", "Supervised Learning"},
    "Unsupervised Learning": {"Clustering", "K-Means", "Hierarchical Clustering", "Unsupervised Learning", "Cluster Analysis"},
    "Data Storage": {"Database", "Data Warehouse", "Data Lake", "DBMS", "Relational Database", "Transactional Database"},
    "Pattern Discovery": {"Association Analysis", "Frequent Patterns", "Market Basket Analysis", "Sequence Analysis"},
    "Data Preprocessing": {"Data Cleaning", "Data Integration", "Data Transformation", "Noise Reduction"},
}

# =============================================================================
# PROJECT BASED SKILLS
# =============================================================================
PROJECT_BASED_SKILLS = {
    "Data Mining", "Machine Learning", "Clustering", "Classification", 
    "Data Warehouse Design", "SQL Querying"
}

# =============================================================================
# HARD SKILLS (Extracted from DATA MINING E TEXT.txt)
# =============================================================================
HARD_SKILLS = {
    # --- GENERAL CONCEPTS ---
    "Data Mining": ["data mining", "knowledge discovery", "kdd", "estrazione dati"],
    "Big Data": ["big data", "grandi quantità di dati", "large datasets"],
    "Business Intelligence": ["business intelligence", "bi"],
    
    # --- KDD PROCESS ---
    "Data Cleaning": ["data cleaning", "pulizia dati", "rimozione rumore", "noise reduction", "data cleansing"],
    "Data Integration": ["data integration", "integrazione dati", "data fusion"],
    "Data Transformation": ["data transformation", "trasformazione dati", "normalizzazione", "aggregazione"],
    "Pattern Evaluation": ["pattern evaluation", "valutazione pattern", "modelli utili"],
    "Knowledge Presentation": ["knowledge presentation", "visualizzazione conoscenza", "data visualization"],

    # --- DATABASES & STORAGE ---
    "Database": ["database", "dbms", "database management system", "relational database", "db"],
    "Data Warehouse": ["data warehouse", "dw", "enterprise data warehouse", "data mart"],
    "Data Lake": ["data lake", "repository dati", "raw data storage"],
    "SQL": ["sql", "structured query language", "query", "select", "join", "insert", "update", "delete"],
    "OLAP": ["olap", "online analytical processing", "drill-down", "roll-up"],

    # --- ANALYSIS TECHNIQUES ---
    "Clustering": ["clustering", "cluster analysis", "raggruppamento", "segmentazione"],
    "K-Means": ["k-means", "kmeans", "k means", "partitioning method"],
    "Hierarchical Clustering": ["hierarchical clustering", "dendrogram", "dendrogramma", "agglomerative clustering"],
    
    "Classification": ["classification", "classificazione", "supervised learning", "predictive model"],
    "Decision Tree": ["decision tree", "albero decisionale", "alberi decisionali"],
    "Random Forest": ["random forest", "foresta casuale"],
    "Neural Network": ["neural network", "rete neurale", "reti neurali"],
    "Rule-Based Classifier": ["rule-based", "if-then rules", "regole if-then"],

    "Regression": ["regression", "regressione", "linear regression", "regressione lineare", "prediction", "previsione numerica"],
    
    "Association Analysis": ["association analysis", "association rules", "regole di associazione", "market basket analysis", "frequent patterns"],
    "Outlier Analysis": ["outlier analysis", "anomaly detection", "rilevamento anomalie", "outlier"],
    
    # --- DATA TYPES ---
    "Structured Data": ["structured data", "dati strutturati", "tabelle"],
    "Unstructured Data": ["unstructured data", "dati non strutturati", "text data", "images", "video", "audio"],
    "Semi-Structured Data": ["semi-structured data", "dati semi-strutturati", "xml", "json"],
    "Time Series": ["time series", "serie storiche", "dati temporali"],

    # --- STATISTICS ---
    "Statistics": ["statistics", "statistica", "probability", "probabilità", "distribuzione", "varianza", "deviazione standard"],
    "Hypothesis Testing": ["hypothesis testing", "test ipotesi", "significatività statistica"],
}

# =============================================================================
# SOFT SKILLS
# =============================================================================
# Only those deducible from the analysis/business context
# mentioned in the text (e.g., "Decision Making" supported by Data Warehouse)
SOFT_SKILLS = {
    "Analytical Thinking": ["analytical thinking", "pensiero analitico", "analisi critica", "interpretazione dati"],
    "Problem Solving": ["problem solving", "risoluzione problemi", "trovare soluzioni"],
    "Decision Making": ["decision making", "processo decisionale", "scelte strategiche", "business decisions"],
    "Communication": ["communication", "comunicazione", "presentazione risultati", "reporting"],
}

# =============================================================================
# JOB ARCHETYPES (For Career Compass)
# =============================================================================
# These define typical skill profiles for different job roles.
# Covers major career paths from Italian university degrees.
JOB_ARCHETYPES = {
    # --- DATA & ANALYTICS ---
    "Data Analyst": {"SQL", "Data Visualization", "Statistics", "Data Mining", "Business Intelligence", "Data Cleaning"},
    "Data Scientist": {"Machine Learning", "Data Mining", "Statistics", "Classification", "Clustering", "Regression"},
    "Business Intelligence Analyst": {"Business Intelligence", "Data Warehouse", "OLAP", "Data Visualization", "SQL"},
    "Data Engineer": {"SQL", "Database", "Data Warehouse", "Data Lake", "Data Integration", "Big Data"},
    
    # --- MARKETING & COMMUNICATION ---
    "Marketing Manager": {"Marketing", "Digital Marketing", "Campaign Management", "Brand Management", "Market Research"},
    "Digital Marketing Specialist": {"SEO", "SEM", "Social Media", "Google Analytics", "Content Marketing", "Email Marketing"},
    "Social Media Manager": {"Social Media", "Content Creation", "Community Management", "Instagram", "TikTok", "Facebook"},
    "Content Strategist": {"Content Marketing", "Copywriting", "SEO", "Editorial Planning", "Brand Voice"},
    "PR Specialist": {"Public Relations", "Media Relations", "Press Release", "Crisis Management", "Corporate Communication"},
    "Communication Manager": {"Corporate Communication", "Internal Communication", "Public Relations", "Event Management"},
    
    # --- BUSINESS & MANAGEMENT ---
    "Project Manager": {"Project Management", "Agile", "Scrum", "Stakeholder Management", "Risk Management", "Budgeting"},
    "Business Analyst": {"Business Analysis", "Requirements Gathering", "Process Improvement", "Data Analysis", "Stakeholder Management"},
    "Management Consultant": {"Strategy", "Business Analysis", "Problem Solving", "Presentation", "Financial Analysis"},
    "Operations Manager": {"Operations Management", "Supply Chain", "Process Optimization", "Team Leadership", "KPI Management"},
    "Product Manager": {"Product Management", "User Research", "Roadmapping", "Agile", "Market Analysis", "UX"},
    "Account Manager": {"Account Management", "Client Relations", "Sales", "Negotiation", "CRM"},
    
    # --- FINANCE & ECONOMICS ---
    "Financial Analyst": {"Financial Analysis", "Excel", "Financial Modeling", "Valuation", "Reporting", "Statistics"},
    "Accountant": {"Accounting", "Bookkeeping", "Tax", "Financial Reporting", "Auditing", "SAP"},
    "Controller": {"Controlling", "Budgeting", "Financial Planning", "Cost Analysis", "Reporting"},
    "Investment Analyst": {"Investment Analysis", "Portfolio Management", "Risk Assessment", "Financial Markets"},
    "Risk Manager": {"Risk Management", "Compliance", "Regulatory", "Financial Analysis", "Insurance"},
    "Auditor": {"Auditing", "Compliance", "Internal Control", "Financial Reporting", "Risk Assessment"},
    
    # --- HR & PEOPLE ---
    "HR Manager": {"Human Resources", "Talent Acquisition", "Employee Relations", "HR Strategy", "Labor Law"},
    "Recruiter": {"Recruiting", "Talent Acquisition", "Interviewing", "Employer Branding", "Sourcing", "LinkedIn"},
    "Training Specialist": {"Training", "Learning Development", "E-Learning", "Curriculum Design", "Facilitation"},
    "HR Business Partner": {"HR Strategy", "Talent Management", "Performance Management", "Change Management"},
    
    # --- TECHNOLOGY & IT ---
    "Software Developer": {"Programming", "Software Development", "Git", "Problem Solving", "Testing", "APIs"},
    "Frontend Developer": {"HTML", "CSS", "JavaScript", "React", "UI Development", "Responsive Design"},
    "Backend Developer": {"Python", "Java", "SQL", "APIs", "Databases", "Server Management"},
    "Full Stack Developer": {"Frontend", "Backend", "JavaScript", "Python", "Database", "DevOps"},
    "UX Designer": {"UX Design", "User Research", "Wireframing", "Prototyping", "Figma", "Usability Testing"},
    "UI Designer": {"UI Design", "Visual Design", "Figma", "Adobe Creative Suite", "Typography", "Color Theory"},
    "IT Support Specialist": {"Technical Support", "Troubleshooting", "Windows", "Networking", "Hardware"},
    "System Administrator": {"System Administration", "Linux", "Windows Server", "Networking", "Security"},
    "Cybersecurity Analyst": {"Cybersecurity", "Security", "Network Security", "Threat Analysis", "Compliance"},
    
    # --- SALES & COMMERCIAL ---
    "Sales Representative": {"Sales", "Negotiation", "CRM", "Lead Generation", "Customer Relations", "Presentation"},
    "Sales Manager": {"Sales Management", "Team Leadership", "Strategy", "Forecasting", "KPI", "Negotiation"},
    "Business Development Manager": {"Business Development", "Sales", "Partnership", "Strategy", "Networking"},
    "E-commerce Manager": {"E-commerce", "Digital Marketing", "SEO", "Analytics", "Conversion Optimization"},
    "Export Manager": {"International Trade", "Export", "Negotiation", "Languages", "Logistics", "Contracts"},
    
    # --- LEGAL ---
    "Legal Counsel": {"Legal", "Contract Law", "Corporate Law", "Compliance", "Negotiation", "Legal Research"},
    "Paralegal": {"Legal Research", "Document Review", "Contracts", "Legal Writing", "Case Management"},
    "Compliance Officer": {"Compliance", "Regulatory", "Risk Management", "Auditing", "Policy Development"},
    
    # --- HEALTHCARE & PHARMA ---
    "Clinical Research Associate": {"Clinical Trials", "GCP", "Medical Research", "Data Management", "Regulatory"},
    "Medical Science Liaison": {"Medical Affairs", "Scientific Communication", "Healthcare", "Pharma", "Stakeholder Management"},
    "Pharmaceutical Sales Rep": {"Pharma Sales", "Medical Knowledge", "Relationship Building", "Presentation"},
    "Healthcare Manager": {"Healthcare Management", "Hospital Administration", "Budget", "Team Leadership"},
    
    # --- ENGINEERING ---
    "Mechanical Engineer": {"Mechanical Engineering", "CAD", "Design", "Manufacturing", "Problem Solving"},
    "Electrical Engineer": {"Electrical Engineering", "Electronics", "Circuit Design", "Testing", "Automation"},
    "Civil Engineer": {"Civil Engineering", "Structural Design", "AutoCAD", "Construction", "Project Management"},
    "Industrial Engineer": {"Industrial Engineering", "Process Optimization", "Lean", "Six Sigma", "Operations"},
    "Quality Engineer": {"Quality Assurance", "QA", "Testing", "ISO", "Process Improvement", "Auditing"},
    
    # --- EDUCATION & RESEARCH ---
    "Research Assistant": {"Research", "Data Collection", "Statistical Analysis", "Academic Writing", "Literature Review"},
    "Teacher": {"Teaching", "Curriculum Development", "Student Assessment", "Classroom Management", "Communication"},
    "Professor": {"Research", "Teaching", "Academic Publishing", "Grant Writing", "Mentoring"},
    
    # --- CREATIVE & DESIGN ---
    "Graphic Designer": {"Graphic Design", "Adobe Creative Suite", "Illustrator", "Photoshop", "InDesign", "Branding"},
    "Art Director": {"Art Direction", "Creative Strategy", "Brand Design", "Team Leadership", "Visual Communication"},
    "Video Producer": {"Video Production", "Video Editing", "Premiere Pro", "After Effects", "Storytelling"},
    "Copywriter": {"Copywriting", "Creative Writing", "Advertising", "Brand Voice", "SEO"},
    
    # --- HOSPITALITY & TOURISM ---
    "Hotel Manager": {"Hotel Management", "Hospitality", "Customer Service", "Revenue Management", "Team Leadership"},
    "Event Manager": {"Event Planning", "Event Management", "Logistics", "Vendor Management", "Budget"},
    "Tour Operator": {"Tourism", "Travel Planning", "Customer Service", "Languages", "Destination Knowledge"},
    
    # --- LOGISTICS & SUPPLY CHAIN ---
    "Supply Chain Manager": {"Supply Chain", "Logistics", "Procurement", "Inventory Management", "Vendor Relations"},
    "Logistics Coordinator": {"Logistics", "Shipping", "Warehouse", "Transportation", "Documentation"},
    "Procurement Specialist": {"Procurement", "Vendor Management", "Negotiation", "Contract Management", "Cost Reduction"},
    
    # --- ENVIRONMENT & SUSTAINABILITY ---
    "Environmental Consultant": {"Environmental Science", "Sustainability", "EIA", "Compliance", "Reporting"},
    "Sustainability Manager": {"Sustainability", "ESG", "Carbon Footprint", "Reporting", "Strategy", "Compliance"},
    
    # --- ARCHITECTURE & REAL ESTATE ---
    "Architect": {"Architecture", "AutoCAD", "Revit", "3D Modeling", "Design", "Building Codes"},
    "Real Estate Agent": {"Real Estate", "Sales", "Negotiation", "Market Analysis", "Customer Relations"},
    "Property Manager": {"Property Management", "Tenant Relations", "Maintenance", "Budgeting", "Contracts"},
}

