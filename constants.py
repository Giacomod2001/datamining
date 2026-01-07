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
# Used by recommend_roles() to suggest alternative career paths.
JOB_ARCHETYPES = {
    "Data Analyst": {
        "SQL", "Data Visualization", "Statistics", "Data Mining", "Business Intelligence",
        "Data Cleaning", "Data Transformation", "OLAP", "Database"
    },
    "Data Scientist": {
        "Machine Learning", "Data Mining", "Statistics", "Classification", "Clustering",
        "Regression", "Neural Network", "Data Transformation", "Data Cleaning"
    },
    "Business Intelligence Analyst": {
        "Business Intelligence", "Data Warehouse", "OLAP", "Data Visualization", "SQL",
        "Database", "Data Mining", "Statistics", "Decision Making"
    },
    "Database Administrator": {
        "Database", "SQL", "Data Warehouse", "Data Integration", "Data Cleaning",
        "Structured Data", "OLAP"
    },
    "Machine Learning Engineer": {
        "Machine Learning", "Classification", "Clustering", "Regression", "Neural Network",
        "Random Forest", "Decision Tree", "Data Transformation"
    },
    "Marketing Analyst": {
        "Data Mining", "Statistics", "Data Visualization", "Business Intelligence",
        "Association Analysis", "Clustering", "Data Cleaning"
    },
    "Data Engineer": {
        "SQL", "Database", "Data Warehouse", "Data Lake", "Data Integration",
        "Data Transformation", "Data Cleaning", "Big Data"
    },
    "Research Analyst": {
        "Statistics", "Hypothesis Testing", "Data Mining", "Data Cleaning",
        "Data Transformation", "Analytical Thinking", "Problem Solving"
    },
}
