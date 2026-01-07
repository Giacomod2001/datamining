"""
================================================================================
CareerMatch AI - Knowledge Base (constants.py)
================================================================================

Questo file contiene la KNOWLEDGE BASE dell'applicazione, rigorosamente limitata
ai concetti presenti nel file "DATA MINING E TEXT.txt".

================================================================================
"""

# =============================================================================
# REGOLE DI INFERENZA (Basate sul corso)
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
# SKILL CLUSTERS (Raggruppamenti concettuali del corso)
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
# HARD SKILLS (Estratte da DATA MINING E TEXT.txt)
# =============================================================================
HARD_SKILLS = {
    # --- CONCETTI GENERALI ---
    "Data Mining": ["data mining", "knowledge discovery", "kdd", "estrazione dati"],
    "Big Data": ["big data", "grandi quantità di dati", "large datasets"],
    "Business Intelligence": ["business intelligence", "bi"],
    
    # --- PROCESSO KDD ---
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

    # --- TECNICHE DI ANALISI ---
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
# Manteniamo solo quelle vagamente deducibili dal contesto di analisi/business
# citato nel testo (es. "Decision Making" supportato dal Data Warehouse)
SOFT_SKILLS = {
    "Analytical Thinking": ["analytical thinking", "pensiero analitico", "analisi critica", "interpretazione dati"],
    "Problem Solving": ["problem solving", "risoluzione problemi", "trovare soluzioni"],
    "Decision Making": ["decision making", "processo decisionale", "scelte strategiche", "business decisions"],
    "Communication": ["communication", "comunicazione", "presentazione risultati", "reporting"],
}
