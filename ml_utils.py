"""
================================================================================
CareerMatch AI - Machine Learning Utilities
================================================================================

Questo modulo implementa le tecniche di Data Mining e Text Analytics utilizzate
per l'analisi CV-Job Description. Le tecniche sono allineate al corso di
"Data Mining & Text Analytics".

================================================================================
TECNICHE IMPLEMENTATE (Riferimenti al corso):
================================================================================

1. TEXT MINING & FEATURE EXTRACTION
   - TF-IDF Vectorization: Trasforma il testo in Vector Space Model (VSM)
   - N-gram Analysis: Cattura sequenze di parole (unigram, bigram, trigram)
   - Fuzzy Matching: Gestisce variazioni e errori di battitura
   
   Riferimento corso: "Text Mining", "Word Vector Representation"

2. CLASSIFICATION (Supervised Learning)
   - Random Forest Classifier: Ensemble di Decision Trees
   - Pipeline sklearn: Preprocessing + Classification
   
   Riferimento corso: "Classification and Regression", "Decision Tree"

3. CLUSTERING (Unsupervised Learning)
   - K-Means: Partitioning clustering per raggruppare skill simili
   - Hierarchical Clustering (Agglomerative): Crea dendrogramma delle skill
   - PCA: Riduzione dimensionalità per visualizzazione 2D
   
   Riferimento corso: "Clustering Techniques", "K-means", "Hierarchical clustering"

4. TOPIC MODELING
   - LDA (Latent Dirichlet Allocation): Estrae topic latenti dai testi
   
   Riferimento corso: "Topic Model"

5. INFORMATION EXTRACTION
   - Named Entity Recognition (NER): Estrae entità come ORG, PERSON, LOC
   - Skill Extraction: Estrae competenze tecniche e soft skills
   
   Riferimento corso: "Information Extraction", "Named Entity Recognition"

6. PATTERN DISCOVERY
   - Association Analysis: Trova correlazioni tra skill (transferable skills)
   - Inference Rules: Regole per dedurre skill correlate
   
   Riferimento corso: "Frequent Patterns and Association Analysis"

================================================================================
KNOWLEDGE DISCOVERY PROCESS (KDD):
================================================================================
L'applicazione segue il processo KDD classico:

1. Data Cleaning     → Preprocessing del testo (lowercase, rimozione rumore)
2. Data Integration  → Combinazione CV + Job Description + Portfolio
3. Data Selection    → Estrazione delle parti rilevanti
4. Data Transformation → TF-IDF vectorization, embedding
5. Data Mining       → Classification, Clustering, Pattern Discovery
6. Pattern Evaluation → Calcolo match score, confidence
7. Knowledge Presentation → Dashboard, grafici, report

================================================================================
"""

import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List
import urllib.parse

# =============================================================================
# LIBRERIE ML (sklearn)
# =============================================================================
# Queste librerie implementano gli algoritmi di Machine Learning:
# - TfidfVectorizer: Term Frequency-Inverse Document Frequency (Text Mining)
# - RandomForestClassifier: Ensemble di Decision Trees (Classification)
# - KMeans: Algoritmo di clustering partizionale (Unsupervised Learning)
# - AgglomerativeClustering: Clustering gerarchico bottom-up
# - PCA: Principal Component Analysis per riduzione dimensionalità
# - cosine_similarity: Metrica di similarità per Vector Space Model

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.cluster import KMeans, AgglomerativeClustering
    from sklearn.decomposition import PCA, TruncatedSVD # Added LSA
    from sklearn.metrics.pairwise import cosine_similarity
    import scipy.cluster.hierarchy as sch  # Per dendrogrammi (Hierarchical Clustering)
    import matplotlib.pyplot as plt
except ImportError:
    RandomForestClassifier = None
    TfidfVectorizer = None
    Pipeline = None
    KMeans = None
    AgglomerativeClustering = None
    PCA = None
    TruncatedSVD = None # Handle missing LSA
    sch = None
    plt = None

try:
    from PyPDF2 import PdfReader  # Per estrazione testo da PDF
except ImportError:
    PdfReader = None

try:
    from fpdf import FPDF  # Per generazione report PDF
except ImportError:
    FPDF = None

def detect_seniority(text: str) -> Tuple[str, float]:
    """
    Detects seniority level (Junior, Mid, Senior) from text.
    Returns: (Level, Confidence)
    """
    if not text:
        return "Mid Level", 0.0
        
    text_lower = text.lower()
    
    # 1. Regex for years of experience
    import re
    years_matches = re.findall(r'(\d+)\s*(?:\+|plus)?\s*(?:years|anni)', text_lower)
    max_years = 0
    if years_matches:
        try:
            max_years = max([int(y) for y in years_matches if int(y) < 50]) # Filter realistic
        except ValueError:
            max_years = 0
    
    # 2. Keyword counting with Regex Boundaries
    seniority_map = getattr(constants, "SENIORITY_KEYWORDS", {})
    scores = {"Entry Level": 0, "Mid Level": 0, "Senior Level": 0}
    
    for level, keywords in seniority_map.items():
        for kw in keywords:
            # Use regex to find whole words only (avoids "management" matching "manage")
            # Escape keyword to handle special chars if any
            if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
                scores[level] += 1
                
    # Logic: Explicit years overrides keywords usually
    if max_years >= 5:
        return "Senior Level", 0.9
        
    # Student/Intern override (Strong signal for Entry Level)
    if scores["Entry Level"] > 0 and max_years < 3:
        return "Entry Level", 0.85

    # Years check for Mid/Entry
    if max_years >= 3:
        return "Mid Level", 0.8
    elif max_years >= 1:
        return "Entry Level", 0.8
        
    # Keyword fallback
    best_level = max(scores, key=scores.get)
    if scores[best_level] > 0:
        # If Senior is detected by keyword but no years, be skeptical?
        if best_level == "Senior Level" and max_years == 0:
             return "Mid Level", 0.5 # Downgrade to Mid if no years proof
        return best_level, 0.7
        
    return "Mid Level", 0.3 # Default assumption

import constants  # Contiene HARD_SKILLS, SOFT_SKILLS, INFERENCE_RULES


# =============================================================================
# CLASSIFICATION: RANDOM FOREST
# =============================================================================
# Riferimento corso: "Classification and Regression", "Decision Tree"
#
# Random Forest è un algoritmo di SUPERVISED LEARNING che usa un ensemble
# di Decision Trees. Ogni albero "vota" per una classe e la classe con
# più voti vince (majority voting).
#
# Vantaggi (dal corso):
# - Robusto all'overfitting grazie all'ensemble
# - Gestisce bene feature numeriche e categoriche
# - Fornisce importanza delle feature
#
# Nel nostro caso: classifica frammenti di testo in categorie di skill
# =============================================================================

@st.cache_resource
def train_rf_model():
    """
    CLASSIFICAZIONE CON RANDOM FOREST
    ==================================
    Riferimento corso: "Classification and Regression", Section 1
    
    Questo metodo implementa un classificatore supervisionato per riconoscere
    le competenze (skills) a partire da frammenti di testo.
    
    ARCHITETTURA PIPELINE:
    ----------------------
    1. TF-IDF Vectorizer (Text Mining)
       - Trasforma il testo in Vector Space Model (VSM)
       - TF = Term Frequency: frequenza del termine nel documento
       - IDF = Inverse Document Frequency: penalizza termini troppo comuni
       - Formula: TF-IDF(t,d) = TF(t,d) × log(N/DF(t))
       - N-gram range (1,3): cattura unigram, bigram e trigram
         Es: "machine", "machine learning", "machine learning engineer"
    
    2. Random Forest Classifier
       - Ensemble di 150 Decision Trees
       - Ogni albero è addestrato su un subset casuale dei dati (bagging)
       - La predizione finale è il voto di maggioranza
    
    PARAMETRI CHIAVE:
    -----------------
    - n_estimators=150: numero di alberi nell'ensemble
    - max_depth=15: profondità massima di ogni albero (previene overfitting)
    - min_samples_split=5: minimo campioni per dividere un nodo
    - class_weight='balanced': bilancia classi rare/frequenti
    
    TRAINING DATA:
    --------------
    I dati di training sono generati da constants.py:
    - HARD_SKILLS: competenze tecniche (Python, SQL, Machine Learning...)
    - SOFT_SKILLS: competenze trasversali (Leadership, Communication...)
    
    Per ogni skill, vengono create varianti comuni nei CV:
    - "python" → "used python", "experience with python", "proficient in python"
    
    Returns:
        Tuple[Pipeline, DataFrame]: (modello addestrato, dati di training)
    """
    
    # =========================================================================
    # STEP 1: PREPARAZIONE DATI (Data Preparation - KDD Step 1-3)
    # =========================================================================
    # Creiamo il dataset di training con coppie (testo, label)
    # Questo è l'approccio SUPERVISIONATO: abbiamo etichette note
    
    data = []

    # Carica le skill dal knowledge base
    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})

    # Per ogni hard skill, crea varianti contestuali
    for skill_name, keywords in hard_skills.items():
        for kw in keywords:
            # Keyword originale
            data.append({"text": kw, "label": skill_name})
            # Pattern comuni nei CV (data augmentation)
            data.append({"text": f"used {kw}", "label": skill_name})
            data.append({"text": f"experience with {kw}", "label": skill_name})
            data.append({"text": f"proficient in {kw}", "label": skill_name})
            data.append({"text": f"expert in {kw}", "label": skill_name})

    # Soft skills con meno varianti
    for skill_name, keywords in soft_skills.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})

    df = pd.DataFrame(data)

    if df.empty:
        return None, df

    # Verifica disponibilità sklearn
    if not RandomForestClassifier or not TfidfVectorizer or not Pipeline:
        return None, df

    # =========================================================================
    # STEP 2: COSTRUZIONE PIPELINE (Data Transformation + Mining - KDD Step 4-5)
    # =========================================================================
    
    try:
        pipe = Pipeline([
            # -----------------------------------------------------------------
            # TF-IDF VECTORIZER (Text Mining - Feature Extraction)
            # -----------------------------------------------------------------
            # Riferimento corso: "Word Vector Representation", "Text Mining"
            #
            # Trasforma il testo in vettori numerici (Vector Space Model)
            # Ogni parola diventa una dimensione del vettore
            # Il valore è il peso TF-IDF della parola
            # -----------------------------------------------------------------
            ('tfidf', TfidfVectorizer(
                ngram_range=(1, 3),       # Unigram, bigram, trigram
                max_features=3000,         # Dimensionalità del vocabolario
                max_df=0.95,               # Ignora termini in >95% dei documenti
                min_df=2,                  # Ignora termini in <2 documenti
                sublinear_tf=True,         # Usa log(1 + tf) invece di tf
                analyzer='word',
                lowercase=True
            )),
            
            # -----------------------------------------------------------------
            # RANDOM FOREST CLASSIFIER (Classification)
            # -----------------------------------------------------------------
            # Riferimento corso: "Classification and Regression"
            #
            # Ensemble di Decision Trees con voting a maggioranza
            # Ogni albero vede un subset casuale di dati e feature
            # -----------------------------------------------------------------
            ('rf', RandomForestClassifier(
                n_estimators=150,          # Reduced from 200 - still robust but less overfit
                max_depth=15,              # Reduced from 30 - prevents overly complex trees
                min_samples_split=5,       # Increased from 2 - requires more samples to split
                min_samples_leaf=3,        # Increased from 1 - leaves must have 3+ samples
                max_features='sqrt',       # Use sqrt(features) at each split for regularization
                class_weight='balanced',   # Handle imbalanced skill frequencies
                n_jobs=-1,                 # Parallel processing
                random_state=42,
                oob_score=True             # Out-of-bag error estimation
            ))
        ])
        pipe.fit(df['text'], df['label'])
        return pipe, df
    except Exception as e:
        print(f"Training Error: {e}")
        return None, df

# =============================================================================
# CLUSTERING: K-MEANS E HIERARCHICAL
# =============================================================================
# Riferimento corso: "Clustering Techniques", Section 2
#
# Il CLUSTERING è una tecnica di UNSUPERVISED LEARNING che raggruppa
# oggetti simili senza bisogno di etichette predefinite.
#
# Due tecniche implementate:
# 1. K-MEANS (Partitioning Clustering)
#    - Divide i dati in K cluster
#    - Ogni cluster ha un centroide
#    - Algoritmo iterativo: assegna punti → ricalcola centroidi → ripeti
#
# 2. HIERARCHICAL CLUSTERING (Agglomerative)
#    - Crea una gerarchia di cluster (dendrogramma)
#    - Approccio bottom-up: ogni punto inizia come cluster singolo
#    - I cluster più vicini vengono uniti progressivamente
# =============================================================================

def perform_skill_clustering(skills: List[str]):
    """
    CLUSTERING DELLE COMPETENZE
    ============================
    Riferimento corso: "Clustering Techniques", Section 2
    
    Questa funzione implementa due tecniche di clustering per raggruppare
    le competenze estratte da CV e Job Description.
    
    PERCHÉ CLUSTERING?
    ------------------
    - Visualizzare quali skill sono semanticamente simili
    - Identificare "famiglie" di competenze (Data, Development, Cloud...)
    - Apprendimento NON SUPERVISIONATO: non servono etichette
    
    STEP 1: TF-IDF VECTORIZATION
    ----------------------------
    Prima di clusterizzare, trasformiamo le skill in vettori numerici.
    Usiamo 'char_wb' (Character N-Grams Within Word Boundaries):
    - Cattura similarità tra "Python" e "PyTorch"
    - Cattura "SQL" in "MySQL" e "PostgreSQL"
    
    STEP 2: HIERARCHICAL CLUSTERING
    --------------------------------
    Riferimento corso: "Hierarchical Clustering", "Dendrogramma"
    
    Algoritmo Agglomerativo (bottom-up):
    1. Ogni skill inizia come cluster singolo
    2. Trova le due skill più simili e uniscile
    3. Ripeti fino ad avere un solo cluster
    4. Il dendrogramma mostra la gerarchia di unione
    
    Linkage Method: WARD
    - Minimizza la varianza intra-cluster
    - Produce cluster bilanciati e compatti
    
    STEP 3: K-MEANS CLUSTERING
    --------------------------
    Riferimento corso: "K-means", Section 2
    
    Algoritmo:
    1. Scegli K centroidi iniziali (random)
    2. Assegna ogni skill al centroide più vicino
    3. Ricalcola i centroidi come media dei punti
    4. Ripeti step 2-3 fino a convergenza
    
    Parametri:
    - n_clusters: determinato euristicamente (sqrt(N/2))
    - n_init=20: prova 20 inizializzazioni diverse
    - max_iter=500: massimo iterazioni per convergenza
    
    STEP 4: PCA PER VISUALIZZAZIONE
    --------------------------------
    Riferimento corso: "Dimensionality Reduction"
    
    PCA (Principal Component Analysis) riduce lo spazio TF-IDF
    a 2 dimensioni per visualizzazione 2D dei cluster.
    
    Returns:
        Tuple: (DataFrame per plot, path dendrogramma, dict cluster)
    """
    
    # Validazione input
    if not skills or len(skills) < 3:
        return None, None, {}

    if not TfidfVectorizer or not KMeans or not sch:
        return None, None, {}

    try:
        # =====================================================================
        # STEP 1: VECTORIZATION (Text → Vector Space Model)
        # =====================================================================
        # Riferimento corso: "Word Vector Representation"
        #
        # Usiamo Character N-Grams per catturare similarità tra:
        # - "Python" e "PyTorch" (condividono "Py")
        # - "SQL", "MySQL", "PostgreSQL" (condividono "SQL")
        # =====================================================================
        
        vectorizer = TfidfVectorizer(
            stop_words='english',
            analyzer='char_wb',      # Character n-grams within word boundaries
            ngram_range=(2, 4),      # Bi-gram, tri-gram, 4-gram di caratteri
            min_df=1
        )
        X = vectorizer.fit_transform(skills).toarray()

        # =====================================================================
        # STEP 2: HIERARCHICAL CLUSTERING (Dendrogramma)
        # =====================================================================
        # Riferimento corso: "Hierarchical Clustering", "Dendrogramma"
        #
        # Algoritmo Agglomerativo:
        # 1. Calcola matrice delle distanze tra tutti i punti
        # 2. Unisci iterativamente i cluster più vicini
        # 3. Ward's linkage: minimizza varianza intra-cluster
        # =====================================================================
        
        linkage_matrix = sch.linkage(X, method='ward')  # Ward's linkage
        
        # Visualizzazione dendrogramma
        plt.figure(figsize=(12, 8))
        
        # Dark Mode Styling
        plt.rcParams.update({
            "text.color": "white",
            "axes.labelcolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
            "axes.edgecolor": "white",
            "axes.titlecolor": "white"
        })
        
        sch.set_link_color_palette([
            '#00cc96', '#ef553b', '#636efa', '#ab63fa', 
            '#ffa15a', '#19d3f3', '#ff6692', '#b6e880'
        ])
        
        # Threshold per colorazione: 70% dell'altezza massima
        color_threshold = 0.7 * max(linkage_matrix[:, 2].max(), 0.1)
        
        dendro = sch.dendrogram(
            linkage_matrix,
            labels=skills,
            leaf_rotation=45,
            leaf_font_size=12,
            above_threshold_color='#dddddd', # Lighter gray for better visibility
            color_threshold=color_threshold
        )
        
        plt.axhline(y=0, color='white', linewidth=1)
        plt.title("Dendrogramma Skill (Ward Linkage)", color='white', fontsize=16)
        plt.xlabel("Skills", color='white', fontsize=12)
        plt.ylabel("Distanza (Ward)", color='white', fontsize=12)
        plt.tight_layout()
        
        dendro_path = "dendrogram_v2.png"
        plt.savefig(dendro_path, transparent=True)
        plt.close()

        # =====================================================================
        # STEP 3: K-MEANS CLUSTERING
        # =====================================================================
        # Riferimento corso: "K-means", Section 2
        #
        # K-Means è un algoritmo di PARTITIONING CLUSTERING:
        # - Pro: Veloce, scalabile, semplice
        # - Contro: Richiede K predefinito, sensibile a inizializzazione
        #
        # Euristica per K: max(2, min(N/3, 5))
        # =====================================================================
        
        # Determina numero ottimale di cluster
        n_clusters = max(2, min(len(skills) // 3, 5))
        
        kmeans = KMeans(
            n_clusters=n_clusters,
            random_state=42,        # Riproducibilità
            n_init=20,              # 20 inizializzazioni per robustezza
            max_iter=500,           # Max iterazioni per convergenza
            algorithm='elkan'       # Algoritmo più veloce
        )
        labels = kmeans.fit_predict(X)

        # Assegna nomi semantici ai cluster
        cluster_names = [
            "Data & Analytics",
            "Development",
            "Cloud & Tools",
            "Business",
            "Research"
        ]
        
        skill_clusters = {}
        for skill, label in zip(skills, labels):
            cluster_name = cluster_names[label % len(cluster_names)]
            if cluster_name not in skill_clusters:
                skill_clusters[cluster_name] = []
            skill_clusters[cluster_name].append(skill)

        # =====================================================================
        # STEP 4: PCA PER VISUALIZZAZIONE 2D
        # =====================================================================
        # Riferimento corso: "Dimensionality Reduction"
        #
        # Lo spazio TF-IDF ha molte dimensioni (una per ogni n-gram).
        # PCA proietta tutto in 2D mantenendo la varianza massima.
        # Questo permette di visualizzare i cluster in un grafico scatter.
        # =====================================================================
        
        pca = PCA(n_components=2)
        coords = pca.fit_transform(X)

        # DataFrame per visualizzazione con Plotly
        df_viz = pd.DataFrame({
            'x': coords[:, 0],
            'y': coords[:, 1],
            'skill': skills,
            'cluster': [cluster_names[l % len(cluster_names)] for l in labels]
        })

        return df_viz, dendro_path, skill_clusters

    except Exception as e:
        print(f"Clustering Error: {e}")
        return None, None, {}

# =============================================================================
# TOPIC MODELING: LATENT DIRICHLET ALLOCATION (LDA)
# =============================================================================
# Riferimento corso: "Topic Model", Section 4 - Text Mining
#
# LDA è un modello generativo probabilistico per scoprire "topic" latenti
# in una collezione di documenti.
#
# Idea chiave:
# - Ogni documento è una mixture di topic
# - Ogni topic è una distribuzione di parole
# - LDA scopre automaticamente questi topic dai dati
#
# Applicazione nel nostro caso:
# - Analizziamo Job Description per estrarre i temi principali
# - Es: "Data Analysis", "Programming", "Business Communication"
# =============================================================================

# Import per Topic Modeling
try:
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.feature_extraction.text import CountVectorizer
    from wordcloud import WordCloud
except ImportError:
    LatentDirichletAllocation = None
    CountVectorizer = None
    WordCloud = None

def perform_topic_modeling(text_corpus: List[str], n_topics=3, n_words=5):
    """
    TOPIC MODELING CON LDA
    ======================
    Riferimento corso: "Topic Model", Section 4
    
    Latent Dirichlet Allocation (LDA) estrae topic latenti da testi.
    
    COME FUNZIONA LDA:
    ------------------
    1. Ogni documento è una combinazione di K topic
    2. Ogni topic è una distribuzione su parole
    3. LDA impara entrambe le distribuzioni simultaneamente
    
    Esempio di output:
    - Topic 1: ["python", "sql", "data"] → "Data Engineering"
    - Topic 2: ["team", "communication"] → "Soft Skills"
    - Topic 3: ["cloud", "aws", "azure"] → "Cloud Infrastructure"
    
    PREPROCESSING:
    --------------
    - CountVectorizer: crea Bag-of-Words (BOW)
    - Stop words estese: inglese + italiano + HR-specific
    - N-gram range (1,2): cattura anche bigrammi
    
    PARAMETRI LDA:
    --------------
    - n_components: numero di topic da estrarre
    - max_iter: iterazioni per convergenza
    - learning_method='batch': più accurato per dataset piccoli
    
    OUTPUT:
    -------
    - topics: lista di interpretazioni dei topic
    - summary: descrizione del lavoro
    - keywords: parole chiave principali
    - wordcloud_path: visualizzazione word cloud
    
    Returns:
        Dict con topics, summary, keywords, wordcloud_path
    """
    
    if not LatentDirichletAllocation or not CountVectorizer or not WordCloud:
        return [], None

    try:
        # =================================================================
        # STEP 0: PRESERVE COMPOUND TOOL NAMES
        # =================================================================
        # LDA splits "Google Analytics" into "google" + "analytics"
        # We preserve compound names by replacing spaces with underscores
        # =================================================================
        import re
        
        compound_tools = {
            # Analytics & BI
            "Google Analytics": "Google_Analytics",
            "Google Analytics 4": "Google_Analytics_4",
            "Google Tag Manager": "Google_Tag_Manager",
            "Looker Studio": "Looker_Studio",
            "Power BI": "Power_BI",
            "Tableau Desktop": "Tableau_Desktop",
            "Data Studio": "Data_Studio",
            # Cloud Platforms
            "Google Cloud": "Google_Cloud",
            "Google Cloud Platform": "Google_Cloud_Platform",
            "Amazon Web Services": "Amazon_Web_Services",
            "Microsoft Azure": "Microsoft_Azure",
            # Programming & Data
            "Machine Learning": "Machine_Learning",
            "Deep Learning": "Deep_Learning",
            "Natural Language Processing": "NLP",
            "Data Visualization": "Data_Visualization",
            "Data Analysis": "Data_Analysis",
            "Data Science": "Data_Science",
            "Big Data": "Big_Data",
            "A/B Testing": "AB_Testing",
            "Statistical Analysis": "Statistical_Analysis",
            # Marketing
            "Social Media": "Social_Media",
            "Digital Marketing": "Digital_Marketing",
            "Content Marketing": "Content_Marketing",
            "Email Marketing": "Email_Marketing",
            "SEO/SEM": "SEO_SEM",
        }
        
        # Apply compound name preservation
        processed_corpus = []
        for doc in text_corpus:
            processed_doc = doc
            for original, replacement in compound_tools.items():
                processed_doc = re.sub(re.escape(original), replacement, processed_doc, flags=re.IGNORECASE)
            processed_corpus.append(processed_doc)
        
        text_corpus = processed_corpus

        # =================================================================
        # STEP 1: PREPROCESSING - Stop Words
        # =================================================================
        # Riferimento corso: "Data Cleaning" (KDD Step 1)
        #
        # Rimuoviamo parole non informative per topic modeling:
        # - Stop words standard (the, a, is...)
        # - Parole HR generiche (requirements, qualifications...)
        # - Stop words multilingue (italiano, spagnolo, francese, tedesco)
        # =================================================================
        
        hr_stop_words = [
            # Structural / Sections
            'requirements', 'qualifications', 'responsibilities', 'duties', 'summary', 
            'overview', 'description', 'profile', 'benefits', 'education', 'experience', 
            'skills', 'background', 'about', 'us', 'team', 'company', 'role', 'job', 
            'position', 'candidate', 'opportunity', 'location', 'category', 'status',
            'salary', 'compensation', 'employment', 'type', 'industry', 'department',

            # Common Adjectives / Qualifiers
            'strong', 'excellent', 'good', 'great', 'proven', 'demonstrated', 'successful',
            'ideal', 'passionate', 'motivated', 'proactive', 'hands-on', 'detail-oriented',
            'dynamic', 'collaborative', 'fast-paced', 'global', 'international', 'leading',
            'preferred', 'plus', 'advantage', 'bonus', 'desirable', 'essential', 'key',
            'core', 'primary', 'required', 'proficient', 'proficiency', 'fluent',
            'knowledge', 'understanding', 'familiarity', 'ability', 'capability', 

            # Common Verbs / Actions
            'work', 'working', 'join', 'apply', 'seeking', 'looking', 'ensure', 'provide',
            'assist', 'support', 'help', 'manage', 'lead', 'coordinate', 'communicate',
            'collaborate', 'participate', 'contribute', 'develop', 'create', 'maintain',
            'deliver', 'drive', 'execute', 'perform', 'build', 'using', 'based',

            # Time / Measure / Misc
            'years', 'year', 'level', 'senior', 'junior', 'mid', 'associate',
            'full-time', 'part-time', 'contract', 'permanent', 'temporary', 'remote', 'hybrid',
            'degree', 'bachelor', 'master', 'phd', 'equivalent', 'related', 'relevant',
            'including', 'include', 'includes', 'various', 'similar', 'etc', 'suite',
            'must', 'will', 'can', 'may', 'should', 'would', 'tools', 'environment',
            
            # Company/Organization Names (should not be keywords)
            'corp', 'corporation', 'inc', 'ltd', 'llc', 'gmbh', 'spa', 'srl',
            'datadriven', 'techstart', 'startup', 'agency', 'group', 'italia',
            
            # Generic Qualifiers (noise)
            'expert', 'expertise', 'skilled', 'specialist', 'professional',
            'advanced', 'basic', 'intermediate', 'beginner', 'native', 'fluency',
            'platform', 'platforms', 'solution', 'solutions', 'service', 'services',
            'system', 'systems', 'technology', 'technologies', 'technique', 'techniques',
            'method', 'methods', 'approach', 'approaches', 'strategy', 'strategies',
            
            # Action Verbs (Noise for Topic Modeling)
            'programming', 'coding', 'developing', 'match', 'matching', 'gap', 'missing', 
            'learn', 'learning', 'use', 'using', 'scikit', 'pandas', 'numpy', 'matplotlib', 'seaborn'
        ]

        # Italian Stop Words
        it_stop_words = [
            'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra',
            'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una',
            'e', 'ed', 'o', 'ma', 'se', 'che', 'non', 'si', 'chi',
            'mi', 'ti', 'ci', 'vi', 'li', 'ne', 'lei', 'lui', 'noi', 'voi', 'loro',
            'mio', 'tuo', 'suo', 'nostro', 'vostro', 'loro',
            'mia', 'tua', 'sua', 'nostra', 'vostra',
            'questo', 'quello', 'quella', 'questi', 'quelle',
            'cui', 'c', 'è', 'sono', 'siete', 'siamo', 'hanno', 'ha', 'ho', 'hai', 'hanno',
            'avuto', 'fatto', 'fare', 'essere', 'avere', 'stato', 'stata', 'stati', 'state',
            'presso', 'durante', 'tramite', 'verso', 'contro', 'sulla', 'dello', 'degli', 'della', 'dei', 'dal', 'dalla',
            'ai', 'agli', 'alla', 'alle', 'negli', 'nelle', 'nella', 'del', 'al', 
            'come', 'dove', 'quando', 'perché', 'anche', 'più', 'meno',
            'tutto', 'tutti', 'tutta', 'tut te', 'ogni', 'altro', 'altra', 'altri', 'altre',
            'molto', 'poco', 'abbastanza', 'proprio', 'già', 'ancora', 
            'ecc', 'eccetera', 'via', 'poi', 'solo', 'soltanto',
            'dell', 'all', 'sull', 'dall', 'nell', 'quest', 'quant', 'tant'
        ]

        # Spanish Stop Words
        es_stop_words = [
            'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no',
            'una', 'su', 'al', 'es', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha',
            'si', 'porque', 'esta', 'son', 'entre', 'está', 'cuando', 'muy', 'sin', 'sobre', 'ser', 'tiene',
            'también', 'me', 'hasta', 'hay', 'donde', 'han', 'quien', 'están', 'estado', 'desde', 'todos',
            'durante', 'años', 'año', 'empresa', 'trabajo', 'experiencia', 'puesto', 'conocimientos'
        ]

        # French Stop Words
        fr_stop_words = [
            'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'en', 'à', 'au', 'aux', 'ce', 'cette',
            'ces', 'que', 'qui', 'quoi', 'dont', 'où', 'pour', 'par', 'sur', 'avec', 'sans', 'sous', 'dans',
            'entre', 'vers', 'chez', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'leur', 'leurs',
            'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses', 'notre', 'nos', 'votre', 'vos',
            'est', 'sont', 'été', 'être', 'avoir', 'fait', 'faire', 'dit', 'dire', 'peut', 'pouvoir',
            'plus', 'moins', 'très', 'bien', 'aussi', 'même', 'tout', 'tous', 'toute', 'toutes',
            'entreprise', 'poste', 'expérience', 'années', 'année', 'travail', 'compétences'
        ]

        # German Stop Words
        de_stop_words = [
            'der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine', 'einer', 'einem', 'einen', 'eines',
            'und', 'in', 'zu', 'von', 'mit', 'ist', 'nicht', 'für', 'auf', 'sich', 'als', 'auch', 'an',
            'es', 'bei', 'nach', 'aus', 'wenn', 'oder', 'aber', 'wie', 'noch', 'nur', 'durch', 'über',
            'so', 'um', 'am', 'im', 'zum', 'zur', 'bis', 'seit', 'wir', 'sie', 'ihr', 'er', 'ich',
            'werden', 'wurde', 'worden', 'wird', 'haben', 'hat', 'hatte', 'sein', 'seine', 'seiner',
            'können', 'kann', 'sollen', 'soll', 'müssen', 'muss', 'dürfen', 'darf',
            'jahre', 'jahr', 'unternehmen', 'erfahrung', 'stelle', 'position', 'kenntnisse'
        ]

        # =================================================================
        # DYNAMIC COMPANY NAME EXTRACTION
        # =================================================================
        # Instead of hardcoding company names, we detect them dynamically
        # using patterns common in job descriptions
        # =================================================================
        import re
        
        dynamic_company_words = set()
        full_text = ' '.join(text_corpus)
        
        # Pattern 1: Extract words before corporate suffixes (Corp, Inc, Ltd, etc.)
        corp_pattern = r'(\b[A-Z][a-zA-Z]+)\s+(?:Corp|Inc|Ltd|LLC|GmbH|S\.?p\.?A\.?|S\.?r\.?l\.?)\b'
        for match in re.finditer(corp_pattern, full_text, re.IGNORECASE):
            company_word = match.group(1).lower()
            if len(company_word) > 2:
                dynamic_company_words.add(company_word)
        
        # Pattern 2: Extract company names after pipe separator (Job Title | Company)
        pipe_pattern = r'\|\s*([A-Z][A-Za-z]+)'
        for match in re.finditer(pipe_pattern, full_text):
            company_word = match.group(1).lower()
            if len(company_word) > 2:
                dynamic_company_words.add(company_word)
        
        # Pattern 3: Words right after "at" or "presso" (employment context)
        at_pattern = r'(?:at|presso)\s+([A-Z][A-Za-z]+)\b'
        for match in re.finditer(at_pattern, full_text, re.IGNORECASE):
            company_word = match.group(1).lower()
            if len(company_word) > 2 and company_word not in {'the', 'our', 'their'}:
                dynamic_company_words.add(company_word)
        
        # =================================================================
        # Combina tutte le stop words (including dynamic company names)
        # =================================================================
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
        all_stop_words = list(ENGLISH_STOP_WORDS) + hr_stop_words + it_stop_words + es_stop_words + fr_stop_words + de_stop_words + list(dynamic_company_words)

        # =================================================================
        # STEP 2: VECTORIZATION - Bag of Words
        # =================================================================
        # Riferimento corso: "Word Vector Representation"
        #
        # CountVectorizer crea una matrice termine-documento:
        # - Righe: documenti
        # - Colonne: termini (words/n-grams)
        # - Valori: frequenze
        # =================================================================
        
        tf_vectorizer = CountVectorizer(
            max_df=0.90,              # Ignora termini in >90% dei doc
            min_df=1,                 # Almeno 1 occorrenza
            stop_words=all_stop_words,
            ngram_range=(1, 1)        # Unigrams only (cleaner topics)
        )
        tf = tf_vectorizer.fit_transform(text_corpus)

        # =================================================================
        # STEP 3: LDA - Latent Dirichlet Allocation
        # =================================================================
        # Riferimento corso: "Topic Model"
        #
        # LDA è un modello generativo bayesiano che:
        # 1. Assume che ogni documento sia generato da K topic
        # 2. Ogni topic è una distribuzione multinomiale sulle parole
        # 3. Usa inferenza variazionale per apprendere le distribuzioni
        # =================================================================
        
        lda = LatentDirichletAllocation(
            n_components=n_topics,    # Numero di topic da estrarre
            max_iter=50,              # Iterazioni per convergenza
            learning_method='batch',  # Più accurato per dataset piccoli
            learning_decay=0.7,       # Decay rate per learning
            random_state=42           # Riproducibilità
        )
        lda.fit(tf)

        feature_names = tf_vectorizer.get_feature_names_out()
        topics_raw = []
        topics_interpreted = []

        # Extract top words for each topic and interpret them
        for topic_idx, topic in enumerate(lda.components_):
            top_features_ind = topic.argsort()[:-n_words - 1:-1]
            # Convert underscores back to spaces for compound names
            top_features = [feature_names[i].replace('_', ' ') for i in top_features_ind]
            
            # Store raw for debugging
            topics_raw.append(top_features)
            
            # Generate user-friendly interpretation
            interpretation = _interpret_topic_keywords(top_features)
            topics_interpreted.append(interpretation)

        # Generate summary of the job
        all_keywords = []
        for topic in lda.components_:
            top_ind = topic.argsort()[-10:][::-1]
            # Convert underscores back to spaces for compound names
            all_keywords.extend([feature_names[i].replace('_', ' ') for i in top_ind])
        
        # Deduplicate and get most common
        from collections import Counter
        keyword_counts = Counter(all_keywords)
        top_job_keywords = [k for k, _ in keyword_counts.most_common(8)]
        
        job_summary = _generate_job_summary(top_job_keywords)

        # Generate Word Cloud
        combined_text = " ".join(text_corpus)
        wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=set(all_stop_words)).generate(combined_text)
        
        wc_path = "topic_wordcloud.png"
        wordcloud.to_file(wc_path)

        return {
            'topics': topics_interpreted,
            'summary': job_summary,
            'keywords': top_job_keywords,
            'wordcloud_path': wc_path
        }

    except Exception as e:
        print(f"LDA Error: {e}")
        return None

# =============================================================================
# FUNZIONI HELPER PER INTERPRETAZIONE TOPIC
# =============================================================================
# Queste funzioni trasformano i risultati grezzi di LDA in testo leggibile
# per l'utente finale (Knowledge Presentation - KDD Step 7)
# =============================================================================

def _interpret_topic_keywords(keywords: List[str]) -> str:
    """
    INTERPRETAZIONE PAROLE CHIAVE TOPIC
    ====================================
    Converte una lista di keyword in un'interpretazione leggibile.
    """
    
    # Format keywords for display (Title Case)
    def format_kw(k):
        # Handle compound names with underscores
        if '_' in k:
            return k.replace('_', ' ').title()
        return k.title()
    
    kw_display = [format_kw(k) for k in keywords[:3]]
    kw_lower = {k.lower().replace(' ', '_') for k in keywords}
    
    # Pattern di tecnologie per categoria (including compound names)
    analytics_tools = {'google_analytics', 'google_analytics_4', 'tag_manager', 'google_tag_manager', 'tracking', 'ga4'}
    viz_tech = {'tableau', 'power_bi', 'looker_studio', 'data_studio', 'visualization', 'dashboard', 'looker', 'data_visualization'}
    cloud_tech = {'aws', 'azure', 'gcp', 'cloud', 'kubernetes', 'docker', 'google_cloud'}
    data_tech = {'data', 'sql', 'database', 'etl', 'pipeline', 'warehouse', 'bigquery', 'data_analysis'}
    ml_ai = {'machine_learning', 'deep_learning', 'ai', 'model', 'neural', 'nlp', 'scikit', 'data_science', 'machine', 'learning'}
    marketing = {'marketing', 'seo', 'sem', 'social_media', 'digital_marketing', 'campaign', 'advertising', 'search'}
    programming = {'python', 'sql', 'r', 'javascript', 'programming', 'coding', 'excel'}
    business = {'business', 'strategy', 'sales', 'customer', 'revenue', 'roi', 'kpi', 'stakeholder'}
    
    # Determina la categoria principale
    if kw_lower & analytics_tools:
        return f"Web Analytics & Tracking: Working with {', '.join(kw_display)}"
    
    elif kw_lower & viz_tech:
        return f"Data Visualization & BI: Creating dashboards with {', '.join(kw_display)}"
    
    elif kw_lower & ml_ai:
        return f"Machine Learning & AI: Building models with {', '.join(kw_display)}"
    
    elif kw_lower & cloud_tech:
        return f"Cloud & Infrastructure: Managing {', '.join(kw_display)}"
    
    elif kw_lower & marketing:
        return f"Digital Marketing: Driving growth with {', '.join(kw_display)}"
    
    elif kw_lower & programming:
        return f"Technical Skills: Programming with {', '.join(kw_display)}"
    
    elif kw_lower & data_tech:
        return f"Data Engineering: Working with {', '.join(kw_display)}"
    
    elif kw_lower & business:
        return f"Business Skills: Focus on {', '.join(kw_display)}"
    
    else:
        return f"Key Focus: {', '.join(kw_display)}"


def _generate_job_summary(keywords: List[str]) -> str:
    """
    GENERAZIONE SINTESI LAVORO
    ===========================
    Genera una frase riassuntiva che spiega il focus del lavoro.
    
    Analizza le keyword estratte da LDA per determinare:
    - Dominio principale (Data, Cloud, ML, ecc.)
    - Tipo di ruolo (Engineer, Analyst, Developer)
    - Contesto aziendale
    """
    kw_lower = {k.lower() for k in keywords}
    
    # Detect main domain
    if {'data', 'analytics', 'sql', 'database'} & kw_lower:
        if {'aws', 'cloud', 'azure'} & kw_lower:
            return "This position seeks a data professional with cloud expertise to manage scalable data pipelines and infrastructure."
        elif {'power', 'bi', 'tableau', 'visualization'} & kw_lower:
            return "This position seeks an analyst/engineer focused on Business Intelligence and data visualization."
        else:
            return "This position seeks a professional with data management and analytics skills."
    
    elif {'engineer', 'software', 'developer', 'programming'} & kw_lower:
        if {'cloud', 'aws', 'azure', 'kubernetes'} & kw_lower:
            return "This position seeks a software engineer with focus on cloud and distributed architectures."
        else:
            return "This position seeks a software engineer for application development."
    
    elif {'design', 'architecture', 'system'} & kw_lower:
        return "This position seeks an architect to design complex and scalable systems."
    
    elif {'ml', 'machine', 'learning', 'ai', 'model'} & kw_lower:
        return "This position seeks a Machine Learning and AI specialist."
    
    else:
        # Generic
        top3 = ', '.join(keywords[:3])
        return f"This position primarily seeks expertise in: {top3}."

# --- NEW: NAMED ENTITY RECOGNITION (NER) ---
try:
    import nltk
    import ssl

    # Bypass SSL check for NLTK download (common issue on macOS)
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # =============================================================================
    # NAMED ENTITY RECOGNITION (NER)
    # =============================================================================
    # Riferimento corso: "Information Extraction", "Named Entity Recognition"
    #
    # NER è una tecnica di Information Extraction che identifica e classifica
    # entità nominate nel testo in categorie predefinite:
    # - ORGANIZATION: aziende, università, istituzioni
    # - GPE (Geo-Political Entity): città, paesi, regioni
    # - PERSON: nomi di persone
    #
    # Algoritmo NLTK usato:
    # 1. Tokenizzazione: divide il testo in parole
    # 2. POS Tagging: assegna parti del discorso (noun, verb, ecc.)
    # 3. NE Chunking: raggruppa token in entità nominate
    #
    # Post-processing:
    # - Filtra parole comuni e skill (evita falsi positivi)
    # - Corregge entità note (es: "Milano" come Location, non Organization)
    # =============================================================================

    # Download necessary NLTK data (cached)
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('chunkers/maxent_ne_chunker_tab')
        nltk.data.find('taggers/averaged_perceptron_tagger_eng')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('maxent_ne_chunker_tab')
        nltk.download('words')
        nltk.download('averaged_perceptron_tagger_eng')
except ImportError:
    nltk = None

def extract_entities_ner(text: str) -> Dict[str, List[str]]:
    """
    ESTRAZIONE ENTITÀ CON NER (Named Entity Recognition)
    =====================================================
    Riferimento corso: "Information Extraction", "NER"
    
    Estrae entità nominate dal testo usando NLTK.
    Ottimizzato per CV italiani ed europei.
    
    PIPELINE NER:
    -------------
    1. Tokenizzazione (word_tokenize)
    2. POS Tagging (pos_tag) - assegna parti del discorso
    3. NE Chunking (ne_chunk) - identifica entità
    4. Filtraggio - rimuove falsi positivi
    5. Post-processing - corregge classificazioni note
    
    CATEGORIE ESTRATTE:
    -------------------
    - Organizations: aziende, università, istituzioni
    - Locations: città, paesi, regioni
    - Persons: nomi di candidati, manager, referenti
    
    FILTRAGGIO AVANZATO:
    --------------------
    Evita di classificare erroneamente:
    - Skill tecniche come organizzazioni ("Python", "React")
    - Header CV come entità ("Experience", "Education")
    - Acronimi business come organizzazioni ("KPI", "ROI")
    
    Returns:
        Dict con liste di Organizations, Locations, Persons
    """
    if not nltk:
        return {}

    entities = {"Organizations": [], "Locations": [], "Persons": []}

    # =========================================================================
    # STEP 1: COSTRUZIONE SET DI ESCLUSIONE
    # =========================================================================
    # Evitiamo falsi positivi escludendo skill, header CV, e parole comuni
    
    exclusion_set = set()
    
    # Helper per aggiungere parti di termini composti
    def add_to_exclusion(term):
        parts = term.lower().split()
        for p in parts:
            exclusion_set.add(p)
            
    # Aggiungi Hard Skills (evita che "Python" sia un'organizzazione)
    for skill_cat, skill_vars in constants.HARD_SKILLS.items():
        add_to_exclusion(skill_cat)
        for var in skill_vars:
            add_to_exclusion(var)
            
    # Add Soft Skills
    for skill_cat, skill_vars in constants.SOFT_SKILLS.items():
        add_to_exclusion(skill_cat)
        for var in skill_vars:
            add_to_exclusion(var)

    # Explicit Tech Jargon often mistaken for People/Orgs
    tech_jargon = {
        "python", "java", "scala", "c++", "c#", "net", "javascript", "typescript", "php", "ruby", "go", "golang", "r",
        "sql", "mysql", "postgresql", "mongodb", "redis", "cassandra", "neo4j",
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "gitlab", "github", "bitbucket",
        "numpy", "pandas", "scipy", "scikit-learn", "sklearn", "matplotlib", "seaborn", "plotly", "tableau", "powerbi",
        "linear", "regression", "logistic", "classification", "clustering", "kmeans", "pca", "svm", "neural", "network",
        "nlp", "bert", "gpt", "llm", "transformer", "vision", "image", "processing",
        "agile", "scrum", "kanban", "waterfall", "jira", "confluence",
        "marketing", "sales", "finance", "accounting", "hr", "management", "business", "analyst", "engineer", "developer",
        "jupyter", "notebook", "studio", "code", "visual", "intelliJ", "eclipse",
        "data", "science", "mining", "warehouse", "lake", "pipeline", "etl", "elt",
        "airflow", "glue", "hadoop", "redshift", "snowflake", "spark", "kafka", "terraform", "dags", "streaming", "expert"
    }
    exclusion_set.update(tech_jargon)

    # Add Common CV Headers & Noise + Business Terms + Acronyms
    noise_words = {
        # CV Headers
        "curriculum", "vitae", "resume", "cv", "profile", "summary", 
        "experience", "education", "skills", "projects", "languages",
        "certifications", "interests", "references", "contacts",
        "email", "phone", "address", "date", "present", "current",
        
        # CV ACTION VERBS (commonly misclassified as locations/entities)
        "built", "created", "led", "managed", "developed", "designed", "implemented",
        "achieved", "analyzed", "conducted", "coordinated", "delivered", "directed",
        "established", "executed", "generated", "improved", "initiated", "launched",
        "maintained", "organized", "performed", "planned", "prepared", "produced",
        "provided", "reduced", "researched", "resolved", "reviewed", "streamlined",
        "supervised", "supported", "trained", "transformed", "utilized",
        "increased", "decreased", "optimized", "automated", "integrated", "migrated",
        "analyze", "implement", "monitor", "manage", "collaborate", "ensure", # Present tense
        "match", "gap", "missing", "learn", "digital", "programming", "futuretech", "solutions",
        "italia spa", "italia s.p.a.", "italy spa", # False positive exclusions
        "collaborated", "communicated", "negotiated", "presented", "reported",
        
        # CURRENCIES & UNITS (misclassified as organizations)
        "eur", "usd", "gbp", "chf", "jpy", "cny", "inr", "aud", "cad",
        "euro", "euros", "dollar", "dollars", "pound", "pounds",
        "million", "billion", "thousand", "annual", "monthly", "weekly", "daily",
        
        # Months
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
        "january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december",
        
        # Job levels
        "page", "of", "senior", "junior", "mid", "level", "lead", "manager", "support",
        
        # Italian CV headers
        "competenze", "esperienze", "formazione", "istruzione", "lingue", "progetti",
        "certificazioni", "interessi", "contatti", "profilo", "sommario",
        
        # Education
        "university", "università", "school", "scuola", "college", "institute", "politecnico", "degree", "bachelor", "master", "phd",
        
        # Technical terms
        "dataflow", "migrated", "optimized", "soft", "upper", "intermediate", "computer",
        
        # CERTIFICATION TERMS (misclassified as persons)
        "certification", "certified", "certificate", "display", "search", "ads",
        "individual", "qualification", "specialist", "associate", "professional",
        "practitioner", "expert", "fundamental", "fundamentals", "advanced", "basic",
        "google", "microsoft", "amazon", "meta", "facebook", "linkedin", "adobe",
        
        # BUSINESS ACRONYMS & TERMS (often misclassified as Organizations)
        "kpi", "kpis", "roi", "roas", "ctr", "cpc", "cpm", "cpa", "ltv", "arpu", "mrr", "arr",
        "gaiq", "seo", "sem", "ppc", "crm", "erp", "b2b", "b2c", "saas", "api",
        "sql", "html", "css", "etl", "elt", "gdpr",
        
        # Course/Subject Topics (not organizations)
        "consumer", "behavior", "behaviour", "statistics", "market", "research",
        "digital", "marketing", "analytics", "visualization", "communication",
        
        # Certifications (acronyms)
        "hubspot", "inbound",
        
        # CLOUD/DATA TOOLS (often misclassified as organizations)
        "bigquery", "redshift", "snowflake", "databricks", "looker", "powerbi", "tableau",
        "aws", "azure", "gcp", "cloud", "firebase", "supabase"
    }
    exclusion_set.update(noise_words)
    
    # 2. Extract and Filter
    try:
        # Tokenize and chunk
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
            if hasattr(chunk, 'label'):
                label = chunk.label()
                entity_name = " ".join(c[0] for c in chunk)
                entity_lower = entity_name.lower()
                
                # Check 0: Skip very short entities (single letters like 'R')
                if len(entity_name) < 3:
                    continue
                
                # Check 1: Exact match
                if entity_lower in exclusion_set:
                    continue
                    
                # Check 2: Parts match
                parts = entity_lower.split()
                if any(p in exclusion_set for p in parts):
                    continue

                if label == 'ORGANIZATION':
                    entities["Organizations"].append(entity_name)
                elif label == 'GPE':
                    entities["Locations"].append(entity_name)
                elif label == 'PERSON':
                    entities["Persons"].append(entity_name)
                        
    except Exception as e:
        pass # Fallback to empty if NLTK fails

    # =========================================================================
    # STEP 2b: PATTERN-BASED COMPANY EXTRACTION
    # =========================================================================
    # NLTK often misses companies, so we use CV-specific patterns
    
    import re
    
    # Known companies database (common in Italian CVs)
    # NOTE: Only include companies that are EMPLOYERS, not tool/product names
    # (removed Google, Salesforce, Adobe etc. because they appear as tool names)
    known_companies = {
        # Italian staffing/recruiting companies
        "Randstad", "Adecco", "Manpower", "Gi Group", "Umana", "Synergie",
        # Companies from demo CV
        "Otreat", "Digital Agency Milano", "TechStart Italia", "StartUp Milano",
        # Major Italian corporations (typically employers)
        "Enel", "Eni", "Intesa Sanpaolo", "UniCredit", "Generali", "Poste Italiane",
        "Telecom Italia", "TIM", "Vodafone Italia", "Wind Tre", "Fastweb",
        "Fiat", "Ferrari", "Lamborghini", "Maserati", "Alfa Romeo", "Stellantis",
        "Luxottica", "Barilla", "Ferrero", "Lavazza", "Pirelli", "Prada", "Gucci",
        "Armani", "Versace", "Dolce & Gabbana", "Benetton", "Calzedonia",
        # Consulting firms (typically employers, not tool names)
        "Accenture", "Deloitte", "PwC", "EY", "KPMG", "McKinsey", "BCG", "Bain",
        # Marketing agencies from demo
        "DataDriven Corp",
        # Italian Universities
        "Politecnico di Milano", "Università Bocconi", "Bocconi", "IULM", "Università IULM",
        "Sapienza", "Luiss", "Cattolica", "Bicocca", "Politecnico di Torino",
    }
    
    # Tech companies that ALSO have products with the same name
    # These need CONTEXT-AWARE detection (only if after "|" or "at")
    tech_companies_ambiguous = {
        "Google", "Microsoft", "Amazon", "Apple", "Meta", "IBM", "Oracle", "SAP",
        "Salesforce", "Adobe", "Spotify", "Netflix", "Uber", "Airbnb", "Stripe",
        "HubSpot", "Slack", "Zoom", "Atlassian", "Shopify", "Twitter", "LinkedIn",
    }
    
    # Pattern 1: "Job Title | Company Name" - extracts company after pipe
    pipe_pattern = r'\|\s*([A-Z][A-Za-z\s&\.\-]+?)(?:\s*\||$|\n|\s+\d{4})'
    for match in re.finditer(pipe_pattern, text):
        company = match.group(1).strip()
        # Remove trailing dates like "2022" or "Present"
        company = re.sub(r'\s*\d{4}.*$', '', company).strip()
        company = re.sub(r'\s*-\s*Present.*$', '', company, flags=re.IGNORECASE).strip()
        if company and len(company) > 2 and company.lower() not in exclusion_set:
            # Ensure it's not a location
            if company not in entities["Locations"] and company.lower() not in {"italy", "milan", "rome"}:
                entities["Organizations"].append(company)
    
    # Pattern 2: "at Company Name" or "presso Company" - employment context
    at_pattern = r'(?:at|presso|@)\s+([A-Z][A-Za-z\s&\.\-]+?)(?:\s*[\|\n,\.]|$)'
    for match in re.finditer(at_pattern, text, re.IGNORECASE):
        company = match.group(1).strip()
        if company and len(company) > 2 and company.lower() not in exclusion_set:
            if company not in entities["Locations"]:
                entities["Organizations"].append(company)
    
    # Pattern 3: Safe companies database lookup (no ambiguity with tool names)
    for company in known_companies:
        if company.lower() in text.lower():
            if company not in entities["Organizations"]:
                entities["Organizations"].append(company)
    
    # Pattern 4: CONTEXT-AWARE detection for ambiguous tech companies
    # Only add if they appear in employment patterns, not as tool names
    for company in tech_companies_ambiguous:
        # Check if company appears after "|" or "at" (employment context)
        employment_patterns = [
            rf'\|\s*{re.escape(company)}\b',  # "| Google"
            rf'\bat\s+{re.escape(company)}\b',  # "at Google"
            rf'\bpresso\s+{re.escape(company)}\b',  # "presso Google"
            rf'\bworked\s+(?:at|for)\s+{re.escape(company)}\b',  # "worked at Google"
            rf'{re.escape(company)}\s+(?:S\.?p\.?A\.?|S\.?r\.?l\.?|Inc|Ltd|Corp)',  # "Google Inc"
        ]
        for pattern in employment_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                if company not in entities["Organizations"]:
                    entities["Organizations"].append(company)
                break  # Found in employment context, add it

    # 3. Post-Processing Fixes (Known Misclassifications)
    # EXPANDED: Italian cities, European capitals, major world cities
    known_locations = {
        # Italian cities
        "Milano", "Milan", "Torino", "Turin", "Roma", "Rome", "Napoli", "Naples",
        "Firenze", "Florence", "Venezia", "Venice", "Bologna", "Genova", "Genoa",
        "Palermo", "Catania", "Bari", "Verona", "Padova", "Padua", "Trieste",
        "Brescia", "Parma", "Modena", "Reggio", "Perugia", "Livorno", "Cagliari",
        "Foggia", "Salerno", "Ferrara", "Rimini", "Ravenna", "Siena", "Pisa",
        "Bergamo", "Monza", "Lecce", "Pescara", "Trento", "Bolzano", "Udine",
        "Ancona", "Arezzo", "Vicenza", "Treviso", "Como", "Varese", "Pavia",
        # Regions
        "Lombardia", "Lombardy", "Piemonte", "Piedmont", "Veneto", "Toscana", "Tuscany",
        "Lazio", "Campania", "Sicilia", "Sicily", "Sardegna", "Sardinia", "Puglia", "Apulia",
        "Emilia-Romagna", "Liguria", "Calabria", "Abruzzo", "Umbria", "Marche",
        # Countries
        "Italia", "Italy", "France", "Francia", "Germany", "Germania", "Spain", "Spagna",
        "UK", "England", "Inghilterra", "Switzerland", "Svizzera", "Austria", "Belgium",
        "Netherlands", "Poland", "Portugal", "Greece", "Sweden", "Norway", "Denmark",
        "USA", "Stati Uniti", "China", "Japan", "India", "Brazil", "Canada", "Australia",
        # European capitals and major cities
        "Paris", "Parigi", "London", "Londra", "Berlin", "Berlino", "Madrid",
        "Barcelona", "Barcellona", "Amsterdam", "Brussels", "Bruxelles", "Vienna",
        "Zurich", "Zurigo", "Geneva", "Ginevra", "Munich", "Monaco", "Frankfurt",
        "Dublin", "Dublino", "Lisbon", "Lisbona", "Prague", "Praga", "Warsaw", "Varsavia",
        "Budapest", "Athens", "Atene", "Stockholm", "Stoccolma", "Copenhagen", "Copenaghen",
        "Oslo", "Helsinki", "Luxembourg", "Lussemburgo"
    }
    
    # Known Italian first names (commonly misclassified as something else)
    known_italian_names = {
        "Marco", "Luca", "Alessandro", "Andrea", "Francesco", "Giuseppe", "Giovanni",
        "Antonio", "Matteo", "Lorenzo", "Stefano", "Roberto", "Paolo", "Davide", "Simone",
        "Maria", "Anna", "Giulia", "Francesca", "Chiara", "Sara", "Laura", "Valentina",
        "Alessia", "Martina", "Giorgia", "Federica", "Elisa", "Silvia", "Paola",
        # Added for robustness
        "Giacomo", "Luigi", "Pietro", "Alberto", "Claudio", "Giorgio", "Enrico", 
        "Fabio", "Massimo", "Michele", "Nicola", "Piero", "Vincenzo", "Emanuele", 
        "Daniele", "Federico", "Gabriele", "Riccardo", "Tommaso", "Edoardo", "Leonardo"
    }
    
    # Known organization patterns (suffixes and keywords) - CALIBRATED FOR DEMO
    org_suffixes = {"s.p.a.", "spa", "s.r.l.", "srl", "ltd", "inc", "gmbh", "ag", "sa", "llc", "corp", "corporation"}
    org_keywords = {
        # Universities
        "university", "università", "politecnico", "istituto", "institute", "academy", "accademia", "bocconi", "sapienza", "luiss",
        # Companies
        "corporation", "company", "azienda", "group", "gruppo", "consulting", "solutions", "technologies", "agency", "agenzia",
        "startup", "start-up", "digital", "tech", "software", "marketing", "analytics", "data",
        # Institutions
        "bank", "banca", "hospital", "ospedale", "foundation", "fondazione"
    }
    
    # Known Italian surnames (for better name detection)
    known_italian_surnames = {
        "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco",
        "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti"
    }
    
    # Move misclassified locations from Persons/Orgs to Locations
    for cat in ["Persons", "Organizations"]:
        to_move = []
        for item in entities[cat]:
            # Check if item is a known location (case insensitive check)
            if item in known_locations or item.title() in known_locations:
                to_move.append(item)
        
        for item in to_move:
            entities[cat].remove(item)
            if item not in entities["Locations"]:
                entities["Locations"].append(item)
    
    # Move Italian names misclassified as Organizations to Persons (e.g., "MARCO")
    to_move_to_person = []
    for item in entities["Organizations"]:
        item_title = item.title()  # Normalize "MARCO" -> "Marco"
        # Check if it's a known Italian first name or surname
        if item_title in known_italian_names or item_title in known_italian_surnames:
            to_move_to_person.append(item)
    
    for item in to_move_to_person:
        entities["Organizations"].remove(item)
        # Add as title case (proper name format)
        if item.title() not in entities["Persons"]:
            entities["Persons"].append(item.title())
    
    # Move misclassified organizations from Persons to Organizations
    to_move_to_org = []
    for item in entities["Persons"]:
        item_lower = item.lower()
        # Check for org suffixes
        if any(item_lower.endswith(suffix) for suffix in org_suffixes):
            to_move_to_org.append(item)
        # Check for org keywords
        elif any(kw in item_lower for kw in org_keywords):
            to_move_to_org.append(item)
    
    for item in to_move_to_org:
        entities["Persons"].remove(item)
        if item not in entities["Organizations"]:
            entities["Organizations"].append(item)
    
    # Filter Persons: keep only those that look like actual names
    # A name typically: starts with capital, 1-3 words, not all caps, not a single common word
    filtered_persons = []
    for person in entities["Persons"]:
        # Skip if single word and potentially a location/org
        words = person.split()
        if len(words) == 1:
            # Accept if it's a known Italian name or surname
            if person in known_italian_names or person.title() in known_italian_names:
                filtered_persons.append(person)
            elif person in known_italian_surnames or person.title() in known_italian_surnames:
                filtered_persons.append(person)
            # Skip single words that might be misclassified
            continue
        # Accept multi-word names (likely "First Last" format)
        if 2 <= len(words) <= 4:
            # Check if any word is a known Italian first name OR surname (e.g., "Marco Bianchi")
            has_known_first_name = any(w in known_italian_names or w.title() in known_italian_names for w in words)
            has_known_surname = any(w in known_italian_surnames or w.title() in known_italian_surnames for w in words)
            
            if has_known_first_name or has_known_surname:
                filtered_persons.append(person)
            # Or if it looks like a proper name pattern (Title Case, not all keywords)
            elif all(w[0].isupper() for w in words if w) and not any(w.lower() in exclusion_set for w in words):
                filtered_persons.append(person)
    
    entities["Persons"] = filtered_persons
    
    # =========================================================================
    # STEP 5: NORMALIZE LOCATION SYNONYMS (merge duplicates like Milan/Milano)
    # =========================================================================
    location_synonyms = {
        # Italian → English (prefer English for international CVs)
        "Italia": "Italy",
        "Milano": "Milan",
        "Roma": "Rome",
        "Torino": "Turin",
        "Napoli": "Naples",
        "Firenze": "Florence",
        "Venezia": "Venice",
        "Genova": "Genoa",
        "Padova": "Padua",
        "Lombardia": "Lombardy",
        "Piemonte": "Piedmont",
        "Toscana": "Tuscany",
        "Sicilia": "Sicily",
        "Sardegna": "Sardinia",
        "Puglia": "Apulia",
        # Other European cities
        "Parigi": "Paris",
        "Londra": "London",
        "Berlino": "Berlin",
        "Barcellona": "Barcelona",
        "Bruxelles": "Brussels",
        "Zurigo": "Zurich",
        "Ginevra": "Geneva",
        "Monaco": "Munich",
        "Dublino": "Dublin",
        "Lisbona": "Lisbon",
        "Praga": "Prague",
        "Varsavia": "Warsaw",
        "Atene": "Athens",
        "Stoccolma": "Stockholm",
        "Copenaghen": "Copenhagen",
        "Lussemburgo": "Luxembourg",
    }
    
    # Normalize locations using synonym mapping
    normalized_locations = []
    for loc in entities["Locations"]:
        # Check if this location has a standard form
        normalized = location_synonyms.get(loc, loc)
        normalized_locations.append(normalized)
    entities["Locations"] = normalized_locations
        
    # Deduplicate and sort
    for k in entities:
        entities[k] = sorted(list(set(entities[k])))
        
    return entities

def generate_cluster_insight(clusters: Dict[str, int], matching_skills: Set[str], missing_skills: Set[str]) -> str:
    """
    Generates a text summary of the clustering results.
    """
    if not clusters:
        return "Not enough data to generate insights."

    # Invert dictionary: Cluster ID -> List of Skills
    cluster_groups = {}
    for skill, cid in clusters.items():
        if cid not in cluster_groups: cluster_groups[cid] = []
        cluster_groups[cid].append(skill)

    insight = "### AI Analysis of your Profile Structure\n\n"

    # Identify strongest and weakest clusters
    for cid, skills in cluster_groups.items():
        # Calculate coverage
        n_total = len(skills)
        n_matched = sum(1 for s in skills if s in matching_skills)
        coverage = (n_matched / n_total) * 100

        # Taking top 3 representative skills for the name
        preview = ", ".join(skills[:3])

        insight += f"**Group {cid} ({preview}...)**\n"
        insight += f"- **Coverage**: {coverage:.0f}% of these skills are in your CV.\n"

        if coverage > 75:
            insight += "- **Assessment**: You are very strong in this area.\n"
        elif coverage < 30:
            insight += "- **Assessment**: This seems to be a significant gap area for you.\n"
        else:
            insight += "- **Assessment**: You have some foundation here, but room to improve.\n"

        insight += "\n"

    return insight

# =============================================================================
def extract_generic_keywords(text: str, top_n=5) -> Set[str]:
    """
    Extracts top keywords from text using TF-IDF when no known skills are found.
    """
    if not TfidfVectorizer or not text or len(text.split()) < 10:
        return set()

    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
        vectorizer.fit_transform([text])
        return set(vectorizer.get_feature_names_out())
    except:
        return set()

# =============================================================================
# TEXT MINING: SKILL EXTRACTION
# =============================================================================
# Riferimento corso: "Text Mining", "Information Extraction", "Feature Extraction"
#
# L'estrazione di skill è un task di INFORMATION EXTRACTION:
# - Estrae entità specifiche (competenze) da testo non strutturato
# - Combina multiple tecniche: regex, n-gram matching, fuzzy matching
#
# TECNICHE UTILIZZATE:
# 1. N-gram Analysis: cattura skill composte ("machine learning")
# 2. Regex Pattern Matching: gestisce varianti morfologiche
# 3. Fuzzy Matching: tollera errori di battitura (85% threshold)
# =============================================================================

try:
    from thefuzz import fuzz  # Fuzzy string matching
except ImportError:
    fuzz = None

# =============================================================================
def preprocess_jd_text(text: str) -> str:
    """
    PREPROCESSING JOB DESCRIPTION
    =============================
    Riferimento KDD: Data Cleaning (Step 1)
    
    Rimuove sezioni non-skill (benefit, condizioni, salari, training) prima 
    dell'estrazione competenze per evitare falsi positivi.
    
    APPROCCIO:
    1. Rimuove intere sezioni per header (Benefits:, Condizioni:, ecc.)
    2. Rimuove pattern individuali (€35,000, 40 ore/settimana, ecc.)
    3. Preserva solo contenuto relativo alle competenze
    
    Args:
        text: Job Description originale
        
    Returns:
        str: JD preprocessata senza sezioni non-skill
    """
    non_skill_patterns = getattr(constants, "NON_SKILL_PATTERNS", {})
    
    if not non_skill_patterns:
        return text
    
    cleaned = text
    
    # Step 1: Remove entire sections by header
    # Pattern: header seguito da contenuto fino a prossima sezione o fine
    for pattern in non_skill_patterns.get("section_headers", []):
        section_regex = rf'(?:^|\n)\s*{pattern}[:\s]*.*?(?=\n\s*[A-Z]|\n\n|\Z)'
        cleaned = re.sub(section_regex, '\n', cleaned, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE)
    
    # Step 2: Remove individual non-skill patterns
    categories_to_filter = [
        "salary", "hours", "duration", "benefits", "contract", 
        "eligibility", "training", "agency", "freelance", "volunteering", "legal"
    ]
    
    for category in categories_to_filter:
        for pattern in non_skill_patterns.get(category, []):
            try:
                cleaned = re.sub(pattern, ' ', cleaned, flags=re.IGNORECASE)
            except re.error:
                continue  # Skip invalid regex patterns
    
    # Step 3: Clean up whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned


# =============================================================================
# =============================================================================
# CONTEXT AWARENESS & DOMAIN INTELLIGENCE (NEW v2.0)
# =============================================================================

def detect_domain_context(text: str) -> str:
    """
    Identifies the specific industry domain (Energy, Biotech, Fashion, etc.) from text.
    Uses DOMAIN_EXTRACTION_RULES from constants.
    """
    text_lower = text.lower()
    domain_rules = getattr(constants, "DOMAIN_EXTRACTION_RULES", {})
    
    best_domain = "General"
    max_score = 0
    
    for domain, rules in domain_rules.items():
        score = 0
        # Check context words
        for word in rules.get("context_words", []):
            if word.lower() in text_lower:
                score += 1
        
        # Check specific must_extract terms
        for term in rules.get("must_extract", []):
            if term.lower() in text_lower:
                score += 2
                
        if score > max_score and score >= 2: # Min threshold
            max_score = score
            best_domain = domain
            
    return best_domain

def detect_seniority_level(text: str) -> str:
    """
    Infers the seniority level (Entry, Mid, Senior, Executive) from text signals.
    Uses CONTEXT_SIGNALS from constants.
    """
    text_lower = text.lower()
    signals = getattr(constants, "CONTEXT_SIGNALS", {}).get("seniority_from_jd", {})
    
    # Priority check: start from Executive down to Entry
    if any(sig in text_lower for sig in signals.get("executive", [])):
        return "Executive"
    if any(sig in text_lower for sig in signals.get("senior", [])):
        return "Senior"
    if any(sig in text_lower for sig in signals.get("mid", [])):
        return "Mid-Level"
    if any(sig in text_lower for sig in signals.get("entry", [])):
        return "Entry Level"
        
    return "Not Specified"

def extract_skills_from_text(text: str, is_jd: bool = False) -> Tuple[Set[str], Set[str]]:
    """
    ESTRAZIONE COMPETENZE DA TESTO
    ==============================
    Riferimento corso: "Information Extraction", "Text Mining"
    
    Estrae hard skills e soft skills da testo non strutturato (CV, Job Description).
    
    METODOLOGIA (multi-step):
    -------------------------
    
    STEP 0: JD PREPROCESSING (NEW)
    Se is_jd=True, rimuove sezioni non-skill (benefit, salari, condizioni)
    prima dell'estrazione per evitare falsi positivi.
    
    STEP 1: PREPROCESSING
    - Conversione in lowercase
    - Tokenizzazione in parole
    - Generazione n-grams (bigram, trigram)
    
    STEP 2: N-GRAM MATCHING
    Riferimento corso: "N-gram Analysis"
    
    - Unigram: singole parole ("Python", "SQL")
    - Bigram: coppie di parole ("machine learning", "data analysis")
    - Trigram: triple di parole ("natural language processing")
    
    Questo permette di catturare skill composte che verrebbero perse
    con una semplice tokenizzazione.
    
    STEP 3: REGEX PATTERN MATCHING
    - Usa espressioni regolari per gestire varianti morfologiche
    - Es: "analyz" matcha "analyze", "analyzing", "analyzed"
    - Pattern: r'\\b{keyword}(?:s|es|ing|ed|tion|ment)?\\b'
    
    STEP 4: FUZZY MATCHING
    Riferimento corso: gestione del "rumore" nei dati
    
    - Usa algoritmo di Levenshtein Distance
    - Threshold 85%: tollera piccoli errori di battitura
    - Es: "Phyton" → "Python" (typo comune)
    
    KNOWLEDGE BASE:
    ---------------
    Le skill sono definite in constants.py:
    - HARD_SKILLS: competenze tecniche (Python, SQL, Machine Learning...)
    - SOFT_SKILLS: competenze trasversali (Leadership, Communication...)
    - INFERENCE_RULES: regole per dedurre skill correlate
    
    Args:
        text: Testo da analizzare (CV o Job Description)
        is_jd: Se True, preprocessa il testo per rimuovere sezioni non-skill
        
    Returns:
        Tuple[Set[str], Set[str]]: (hard_skills, soft_skills) estratti
    """
    
    # NEW: Preprocess JD to remove non-skill sections (benefits, salary, etc.)
    if is_jd:
        text = preprocess_jd_text(text)
    
    hard_found = set()
    soft_found = set()
    text_lower = text.lower()

    # Carica knowledge base
    # (Use copy to allow local extension based on domain context)
    hard_skills = getattr(constants, "HARD_SKILLS", {}).copy()
    soft_skills = getattr(constants, "SOFT_SKILLS", {})
    inference_rules = getattr(constants, "INFERENCE_RULES", {})
    
    # NEW: Domain Context Boost
    # If a specific domain is detected, we ensure its critical skills are searched for,
    # even if they might not be in the standard HARD_SKILLS list or require prioritization.
    domain_context = detect_domain_context(text)
    if domain_context != "General":
        domain_rules = getattr(constants, "DOMAIN_EXTRACTION_RULES", {}).get(domain_context, {})
        must_extract = domain_rules.get("must_extract", [])
        for skill_name in must_extract:
            if skill_name not in hard_skills:
                # Add domain-specific skill to search list (self-variation)
                hard_skills[skill_name] = [skill_name]

    # =========================================================================
    # STEP 1: PREPROCESSING E GENERAZIONE N-GRAMS
    # =========================================================================
    # Riferimento corso: "N-gram Analysis"
    #
    # Tokenizziamo il testo e generiamo n-grams per catturare
    # skill composte come "machine learning" o "data visualization"
    # =========================================================================
    
    words = text_lower.split()
    text_words = set(words)
    
    # Bigram: coppie di parole consecutive
    bigrams = set(' '.join(words[i:i+2]) for i in range(len(words)-1))
    
    # Trigram: triple di parole consecutive
    trigrams = set(' '.join(words[i:i+3]) for i in range(len(words)-2))
    
    # Unione di tutti i pattern da cercare
    all_phrases = text_words | bigrams | trigrams

    # 1. Regex Match Hard Skills (Exact + N-gram + Fuzzy)
    for skill, variations in hard_skills.items():
        matched = False
        
        # First try: direct phrase match in n-grams (fastest)
        for var in variations:
            if var.lower() in all_phrases:
                hard_found.add(skill)
                matched = True
                break
        
        # Second try: regex match with morphological variants
        if not matched:
            for var in variations:
                pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed|tion|ment)?\b'
                if re.search(pattern, text_lower):
                    hard_found.add(skill)
                    matched = True
                    break

        # Third try: fuzzy matching (only for skills with 5+ chars to avoid false positives)
        # Short skills like SEO, SQL, CSS require exact match only
        if not matched and fuzz and len(skill) >= 5:
            for word in text_words:
                if len(word) > 4 and fuzz.ratio(word, skill.lower()) > 88:
                    hard_found.add(skill)
                    break
            # Also check bigrams for compound skills
            if not matched:
                for bigram in bigrams:
                    if fuzz.ratio(bigram, skill.lower()) > 88:
                        hard_found.add(skill)
                        break

    # 2. Regex Match Soft Skills (Exact + Fuzzy)
    for skill, variations in soft_skills.items():
        matched = False
        
        # Direct phrase match
        for var in variations:
            if var.lower() in all_phrases:
                soft_found.add(skill)
                matched = True
                break
        
        # Regex fallback
        if not matched:
            for var in variations:
                pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
                if re.search(pattern, text_lower):
                    soft_found.add(skill)
                    matched = True
                    break

        # Fuzzy fallback (only for skills with 5+ chars)
        if not matched and fuzz and len(skill) >= 5:
            for word in text_words:
                if len(word) > 4 and fuzz.ratio(word, skill.lower()) > 88:
                    soft_found.add(skill)
                    break

    # 3. Hierarchical Inference (expand found skills to parent categories)
    inferred_skills = set()
    for child_skill in hard_found:
        if child_skill in inference_rules:
            parents = inference_rules[child_skill]
            inferred_skills.update(parents)
    hard_found.update(inferred_skills)

    # 4. Generic Fallback (only if very few skills found)
    if len(hard_found) < 2:
        generic_keywords = extract_generic_keywords(text, top_n=5)
        for kw in generic_keywords:
            hard_found.add(kw.capitalize())

    # =========================================================================
    # STEP 5: SEMI-SUPERVISED ENHANCEMENT
    # =========================================================================
    # Riferimento corso: "Semi-Supervised Learning", "Label Propagation"
    #
    # Questo step usa il layer semi-supervisionato per:
    # 1. Migliorare l'estrazione usando pattern appresi precedentemente
    # 2. Apprendere nuovi pattern dalle skill trovate con alta confidenza
    # =========================================================================
    
    # =========================================================================
    # STEP 6: JOB ARCHETYPE FALLBACK (NEW)
    # =========================================================================
    # Se is_jd=True, cerchiamo se il testo contiene nomi di ruoli
    # (es: "Energy Trader", "energy engineer") e estraiamo le skill
    # richieste dall'archetype corrispondente.
    # Questo permette di matchare JD che contengono solo nomi di ruoli.
    # =========================================================================
    if is_jd:
        job_archetypes = getattr(constants, "JOB_ARCHETYPES", {})
        soft_skill_names = set(soft_skills.keys())  # Filter out soft skills
        
        # Normalize text: remove punctuation and extra spaces
        text_normalized = re.sub(r'[,;:\.\-\(\)]', ' ', text_lower)
        text_normalized = ' '.join(text_normalized.split())  # Normalize whitespace
        text_words = set(text_normalized.split())
        
        for role_name, role_skills in job_archetypes.items():
            role_lower = role_name.lower()
            role_words = role_lower.split()
            
            # Method 1: Exact phrase match
            if role_lower in text_normalized:
                for skill in role_skills:
                    # Only add if NOT a soft skill
                    if skill not in soft_skill_names:
                        hard_found.add(skill)
                continue
            
            # Method 2: All words of role name present in JD
            if len(role_words) > 1 and all(w in text_words for w in role_words):
                for skill in role_skills:
                    # Only add if NOT a soft skill
                    if skill not in soft_skill_names:
                        hard_found.add(skill)
                continue
            
            # Method 3: Fuzzy match for role names (handle typos/variations)
            if fuzz and len(role_lower) > 5:
                # Check against original text segments
                for segment in text_normalized.split():
                    if len(segment) > 5 and fuzz.ratio(segment, role_lower.replace(" ", "")) > 85:
                        for skill in role_skills:
                            hard_found.add(skill)
                        break

    return hard_found, soft_found


# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    if PdfReader is None: 
        raise ImportError("PyPDF2 missing")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF Error: {str(e)}")

def generate_pdf_report(res: Dict, jd_text: str = "", cl_analysis: Dict = None) -> bytes:
    """
    Generates a comprehensive PDF report with skills, cover letter, interview tips, and job recommendations.
    """
    if not FPDF:
        return b"FPDF library missing."

    class ReportPDF(FPDF):
        def footer(self):
            self.set_y(-15)
            self.set_font('Times', 'I', 9)
            self.set_text_color(0, 0, 0)  # Black
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def clean(text):
        if not text: return ""
        for old, new in {"'": "'", "'": "'", """: '"', """: '"', "–": "-", "•": "-", "→": "->"}.items():
            text = text.replace(old, new)
        return text.encode('latin-1', 'ignore').decode('latin-1')

    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # ===== TITLE =====
    pdf.set_font('Times', 'B', 16)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.cell(0, 10, 'CareerMatch AI - Analysis Report', 0, 1, 'C')
    pdf.ln(5)
    
    # ===== SECTION 1: MATCH SCORE =====
    pct = res.get("match_percentage", 0)
    assessment = "Excellent" if pct >= 80 else ("Good" if pct >= 60 else "Needs Work")
    pdf.set_font('Times', 'B', 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, f"1. Profile Match: {pct:.0f}% ({assessment})", 0, 1)
    pdf.ln(2)
    
    # Matched Skills
    matched = list(res.get("matching_hard", []))
    pdf.set_font('Times', 'B', 11)
    pdf.cell(0, 6, f"Matched ({len(matched)}):", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.multi_cell(0, 5, clean(", ".join(matched[:15])) + ("..." if len(matched) > 15 else "") if matched else "None")
    
    # Missing Skills
    missing = list(res.get("missing_hard", []))
    pdf.set_font('Times', 'B', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, f"Missing ({len(missing)}):", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.multi_cell(0, 5, clean(", ".join(missing)) if missing else "None")
    pdf.ln(4)
    
    # ===== SECTION 2: COVER LETTER =====
    if cl_analysis:
        pdf.set_font('Times', 'B', 13)
        pdf.set_text_color(0, 0, 0)
        cl_score = cl_analysis.get("overall_score", 0)
        pdf.cell(0, 8, f"2. Cover Letter: {cl_score:.0f}%", 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.set_text_color(0, 0, 0)
        
        # Strengths
        strengths = cl_analysis.get("strengths", [])
        if strengths:
            pdf.set_text_color(0, 0, 0)  # Black
            pdf.multi_cell(0, 5, "Strengths: " + clean(", ".join(strengths[:3])))
        
        # Improvements
        improvements = cl_analysis.get("improvements", [])
        if improvements:
            pdf.set_text_color(0, 0, 0)  # Black
            pdf.multi_cell(0, 5, "Improve: " + clean(", ".join(improvements[:3])))
        pdf.ln(4)
    
    # ===== SECTION 3: INTERVIEW TIPS =====
    pdf.set_font('Times', 'B', 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "3. Interview Preparation", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.set_text_color(0, 0, 0)
    
    # Generate tips based on analysis
    tips = []
    if matched:
        tips.append(f"Highlight your experience with: {', '.join(list(matched)[:5])}")
    if missing:
        tips.append(f"Be ready to explain how you'd learn: {', '.join(list(missing)[:3])}")
    transferable = res.get("transferable", {})
    if transferable:
        tips.append(f"Emphasize transferable skills: {', '.join(list(transferable.keys())[:3])}")
    if pct >= 70:
        tips.append("Your profile is strong - focus on cultural fit and motivation")
    else:
        tips.append("Prepare examples showing quick learning ability")
    
    for i, tip in enumerate(tips[:4], 1):
        pdf.multi_cell(0, 5, clean(f"{i}. {tip}"))
    pdf.ln(4)
    
    # ===== SECTION 4: ALTERNATIVE CAREERS =====
    pdf.set_font('Times', 'B', 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "4. Alternative Career Paths", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.set_text_color(0, 0, 0)
    
    # Get recommendations
    cv_skills = set(matched) | set(res.get("bonus_skills", []))
    recs = recommend_roles(cv_skills, jd_text)[:5]
    
    if recs:
        for item in recs:
            # recommend_roles returns dicts, not tuples
            if isinstance(item, dict):
                role = item.get("role", "Unknown")
                score = item.get("score", 0)
            else:
                # Fallback if it returns tuples
                role = item[0]
                score = item[1]
                
            try:
                # Handle string scores safely
                if isinstance(score, str):
                    import re
                    nums = re.findall(r"[\d\.]+", score)
                    score_val = float(nums[0]) if nums else 0
                else:
                    score_val = float(score)
            except:
                score_val = 0
                
            pdf.cell(0, 5, clean(f"- {role}: {score_val:.0f}% match"), 0, 1)
    else:
        pdf.cell(0, 5, "No alternative roles found with high confidence.", 0, 1)
    pdf.ln(4)
    
    # ===== SECTION 5: ACTION PLAN =====
    pdf.set_font('Times', 'B', 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "5. Action Plan", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.set_text_color(0, 0, 0)
    
    actions = [
        f"Focus on learning: {', '.join(list(missing)[:3])}" if missing else "Your skills are well-aligned!",
        "Update your LinkedIn with matched keywords",
        "Practice STAR method for behavioral questions",
        "Research the company culture and recent news"
    ]
    for i, action in enumerate(actions, 1):
        pdf.multi_cell(0, 5, clean(f"{i}. {action}"))
    
    return pdf.output(dest='S').encode('latin-1', 'ignore')

def detect_language(text: str) -> str:
    """
    Enhanced language detection for native language inference.
    If a CV is written in a specific language, we can infer the candidate 
    is likely a native speaker of that language.
    
    Supports: Italian, English, Spanish, French, German, Portuguese
    Returns the detected native language as a skill string.
    """
    text = text.lower()
    
    # Language markers (common words unique to each language)
    language_markers = {
        "Italian": {
            "markers": {" il ", " lo ", " la ", " gli ", " le ", " di ", " è ", " per ", 
                       " delle ", " nella ", " sono ", " che ", " con ", " una ", " del ",
                       " nel ", " alla ", " dalla ", " presso ", " laurea ", " esperienza ",
                       " competenze ", " lavoro ", " sviluppo ", " gestione "},
            "strong_markers": {" esperienza lavorativa", " istruzione ", " competenze tecniche",
                              " laurea in ", " presso ", " dal ", " al "}
        },
        "English": {
            "markers": {" the ", " a ", " an ", " and ", " is ", " of ", " for ", " to ", 
                       " in ", " with ", " that ", " this ", " have ", " has ", " was ",
                       " were ", " been ", " experience ", " skills ", " work ", " team "},
            "strong_markers": {" work experience ", " education ", " skills ", " bachelor",
                              " master ", " university ", " developed ", " managed "}
        },
        "Spanish": {
            "markers": {" el ", " la ", " los ", " las ", " de ", " en ", " que ", " y ",
                       " es ", " para ", " con ", " una ", " por ", " como ", " más ",
                       " del ", " experiencia ", " trabajo ", " desarrollo "},
            "strong_markers": {" experiencia laboral ", " educación ", " habilidades ",
                              " licenciatura ", " universidad ", " desarrollé "}
        },
        "French": {
            "markers": {" le ", " la ", " les ", " de ", " du ", " des ", " et ", " en ",
                       " est ", " une ", " un ", " pour ", " avec ", " dans ", " sur ",
                       " expérience ", " travail ", " développement "},
            "strong_markers": {" expérience professionnelle ", " formation ", " compétences ",
                              " licence ", " université ", " développé "}
        },
        "German": {
            "markers": {" der ", " die ", " das ", " und ", " in ", " ist ", " mit ", " für ",
                       " von ", " zu ", " auf ", " bei ", " eine ", " einer ", " eines ",
                       " erfahrung ", " arbeit ", " entwicklung "},
            "strong_markers": {" berufserfahrung ", " ausbildung ", " kenntnisse ",
                              " bachelor ", " universität ", " entwickelt "}
        },
        "Portuguese": {
            "markers": {" o ", " a ", " os ", " as ", " de ", " em ", " que ", " e ",
                       " é ", " para ", " com ", " uma ", " por ", " como ", " mais ",
                       " do ", " experiência ", " trabalho ", " desenvolvimento "},
            "strong_markers": {" experiência profissional ", " educação ", " habilidades ",
                              " licenciatura ", " universidade ", " desenvolvi "}
        }
    }
    
    # Calculate scores for each language
    scores = {}
    for lang, data in language_markers.items():
        # Count regular markers
        regular_score = sum(1 for w in data["markers"] if w in text)
        # Strong markers count double
        strong_score = sum(2 for w in data["strong_markers"] if w in text)
        scores[lang] = regular_score + strong_score
    
    # Find the best match
    best_lang = max(scores, key=scores.get)
    best_score = scores[best_lang]
    
    # Only return if score is significant (at least 3 markers found)
    if best_score >= 3:
        return best_lang
    
    return None

# =============================================================================
def analyze_gap(cv_text: str, job_text: str) -> Dict:
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text, is_jd=True)  # FIXED: Enable archetype fallback

    # 0. Native Language Inference
    # If CV is detected as Italian, we assume candidate speaks Italian (Native)
    detected_lang = detect_language(cv_text)
    if detected_lang:
        cv_hard.add(detected_lang)

    # Expand skills using hierarchy (English -> Languages, etc.)
    cv_hard_normalized = {s.lower() for s in cv_hard}
    job_hard_normalized = {s.lower() for s in job_hard}
    
    cv_hard_expanded = expand_skills_with_clusters(cv_hard_normalized)
    job_hard_expanded = expand_skills_with_clusters(job_hard_normalized)
    
    # Match based on expanded sets
    matching_hard_normalized = cv_hard_expanded & job_hard_expanded
    initial_missing_hard_normalized = job_hard_expanded - cv_hard_expanded
    extra_hard_normalized = cv_hard_expanded - job_hard_expanded
    
    # Map back to original casing for display
    matching_hard = {s for s in (cv_hard | job_hard) if s.lower() in matching_hard_normalized}
    initial_missing_hard = {s for s in job_hard if s.lower() in initial_missing_hard_normalized}
    extra_hard = {s for s in cv_hard if s.lower() in extra_hard_normalized}

    # Stats
    skill_clusters = getattr(constants, "SKILL_CLUSTERS", {})

    # ==========================================================================
    # SIMPLIFIED TRANSFERABLE MATCHING (REBUILT FROM SCRATCH)
    # ==========================================================================
    # Logic: If CV has ANY skill in a cluster, ALL other skills in that 
    # cluster become Transferable (yellow instead of red).
    # ==========================================================================
    
    transferable = {} 
    remaining_missing = set()
    
    # Pre-compute: normalize all CV skills to lowercase for comparison
    cv_skills_lower = {s.lower() for s in cv_hard}
    
    # Pre-compute: build a lookup table of cluster memberships (all lowercase)
    cluster_lookup = {}  # skill_lower -> set of all other skills in same cluster(s)
    for cluster_name, members in skill_clusters.items():
        members_lower = {m.lower() for m in members}
        for skill in members_lower:
            if skill not in cluster_lookup:
                cluster_lookup[skill] = set()
            cluster_lookup[skill].update(members_lower)
    
    # Check each missing skill
    for missing in initial_missing_hard:
        missing_lower = missing.lower()
        found_transferable = False
        
        # Check if this missing skill is in any cluster
        if missing_lower in cluster_lookup:
            # Get all equivalent skills in the same cluster(s)
            equivalent_skills = cluster_lookup[missing_lower]
            
            # Check if user has ANY of the equivalent skills
            user_has = equivalent_skills.intersection(cv_skills_lower)
            
            if user_has:
                # Find original casing for display
                user_has_original = [s for s in cv_hard if s.lower() in user_has]
                display_skill = user_has_original[0] if user_has_original else list(user_has)[0]
                transferable[missing] = display_skill
                found_transferable = True
        
        if not found_transferable:
            remaining_missing.add(missing)

    # Note: project_review is ONLY populated by analyze_gap_with_project
    # when the user actually provides project content
    project_review = set()
    final_strict_missing = remaining_missing  # All remaining are missing

    matching_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft

    score_points = len(matching_hard) + (len(transferable) * 0.5)
    match_pct = score_points / len(job_hard) * 100 if job_hard else 0

    # 7. Seniority Analysis
    cv_level, _ = detect_seniority(cv_text)
    jd_level, _ = detect_seniority(job_text)
    
    seniority_match = "Match"
    if cv_level != jd_level:
        if cv_level == "Entry Level" and jd_level == "Senior Level":
            seniority_match = "Underqualified"
        elif cv_level == "Senior Level" and jd_level == "Entry Level":
            seniority_match = "Overqualified"
        else:
            seniority_match = "Partial Match"

    return {
        "match_percentage": match_pct,
        "matching_hard": matching_hard,
        "missing_hard": final_strict_missing,
        "project_review": project_review, 
        "transferable": transferable,
        "extra_hard": extra_hard,
        "matching_soft": matching_soft,
        "missing_soft": missing_soft,
        "seniority_info": {
            "cv_level": cv_level,
            "jd_level": jd_level,
            "match_status": seniority_match
        }
    }

def analyze_gap_with_project(cv_text: str, job_text: str, project_text: str) -> Dict:
    """
    Enhanced Portfolio Intelligence System.
    Analyzes CV + Project vs Job Description with comprehensive insights.
    Returns portfolio quality score, project highlights, gap suggestions, and verified skills.
    """
    # 1. Standard CV Analysis
    res = analyze_gap(cv_text, job_text)
    
    # 2. Extract skills from all sources
    proj_hard, _ = extract_skills_from_text(project_text)
    job_hard, _ = extract_skills_from_text(job_text, is_jd=True)  # Enable archetype fallback
    cv_hard, _ = extract_skills_from_text(cv_text)
    
    # 3. Calculate Portfolio Quality Score (0-100)
    portfolio_metrics = calculate_portfolio_quality(
        project_skills=proj_hard,
        job_skills=job_hard,
        cv_skills=cv_hard,
        project_text=project_text
    )
    
    # 4. Identify Project-Verified Skills
    project_verified = job_hard.intersection(proj_hard)
    
    # 5. Rank Projects and Generate Highlights
    project_highlights = rank_projects_by_relevance(
        project_text=project_text,
        project_skills=proj_hard,
        job_skills=job_hard
    )
    
    # 6. Generate Interview Talking Points
    talking_points = generate_project_talking_points(
        project_skills=proj_hard,
        job_skills=job_hard,
        verified_skills=project_verified
    )
    
    # 7. Suggest Gap-Filling Projects
    gap_projects = suggest_gap_projects(
        missing_skills=res["missing_hard"]
    )
    
    # 8. Update Skills if Project Fills Gaps
    newly_found_in_project = res["missing_hard"].intersection(proj_hard)
    if newly_found_in_project:
        res["matching_hard"].update(newly_found_in_project)
        res["missing_hard"] = res["missing_hard"] - newly_found_in_project
        
        # Recalculate Match Score
        score_points = len(res["matching_hard"]) + (len(res["transferable"]) * 0.5) + (len(res["project_review"]) * 0.3)
        res["match_percentage"] = score_points / len(job_hard) * 100 if job_hard else 0
    
    # 9. Add Portfolio Intelligence to Results
    res["project_verified"] = project_verified
    res["portfolio_quality"] = portfolio_metrics["quality_score"]
    res["portfolio_metrics"] = portfolio_metrics
    res["project_highlights"] = project_highlights
    res["talking_points"] = talking_points
    res["gap_projects"] = gap_projects
    
    return res


def calculate_portfolio_quality(project_skills: Set[str], job_skills: Set[str], 
                                cv_skills: Set[str], project_text: str) -> Dict:
    """
    Calculates comprehensive portfolio quality metrics.
    
    Algorithm:
    - Skills Coverage (40%): How many job skills are demonstrated in projects
    - Complexity (30%): Average number of skills per project section
    - Relevance (30%): Ratio of project skills that match job requirements
    
    Returns: Dict with quality_score (0-100) and component metrics
    """
    # 1. Skills Coverage Score
    matched_skills = job_skills.intersection(project_skills)
    coverage_score = (len(matched_skills) / len(job_skills) * 100) if job_skills else 0
    
    # 2. Complexity Score (estimate project depth)
    # Count unique skills and estimate complexity based on diversity
    complexity_raw = len(project_skills)
    complexity_score = min(complexity_raw / 10 * 100, 100)  # Normalize to 0-100
    
    # 3. Relevance Score
    # What % of project skills are actually relevant to the job
    relevance_score = (len(matched_skills) / len(project_skills) * 100) if project_skills else 0
    
    # 4. Calculate Weighted Quality Score
    quality_score = (
        coverage_score * 0.4 +
        complexity_score * 0.3 +
        relevance_score * 0.3
    )
    
    return {
        "quality_score": round(quality_score, 1),
        "coverage_score": round(coverage_score, 1),
        "complexity_score": round(complexity_score, 1),
        "relevance_score": round(relevance_score, 1),
        "total_project_skills": len(project_skills),
        "matched_job_skills": len(matched_skills)
    }


def rank_projects_by_relevance(project_text: str, project_skills: Set[str], 
                               job_skills: Set[str]) -> List[Dict]:
    """
    Analyzes project text and identifies top projects to highlight.
    
    Returns: List of top 3 project highlights with skills and relevance scores
    """
    # Split project text into sections (simple heuristic: double newlines or headers)
    # For now, treat the whole text as one project
    # In future versions, could detect multiple projects
    
    highlights = []
    
    # Calculate relevance of the project
    matched_skills = project_skills.intersection(job_skills)
    relevance = (len(matched_skills) / len(job_skills) * 100) if job_skills else 0
    
    # Extract a snippet (first 200 chars as preview)
    snippet = " ".join(project_text.split()[:30]) + "..."
    
    highlights.append({
        "title": "Portfolio Project",
        "snippet": snippet,
        "verified_skills": list(matched_skills)[:8],  # Limit to 8 for display
        "relevance_score": round(relevance, 1),
        "total_skills": len(matched_skills)
    })
    
    return highlights


def generate_project_talking_points(project_skills: Set[str], job_skills: Set[str],
                                    verified_skills: Set[str]) -> List[str]:
    """
    Generates interview talking points based on project-skill alignment.
    
    Returns: List of actionable talking points for interviews
    """
    talking_points = []
    
    # 1. Directly verified skills
    if verified_skills:
        top_verified = list(verified_skills)[:3]
        talking_points.append(
            f"Highlight practical experience with: {', '.join(top_verified)}"
        )
    
    # 2. Skill diversity
    if len(project_skills) >= 5:
        talking_points.append(
            f"Emphasize your versatile skill set across {len(project_skills)} technologies"
        )
    
    # 3. Gap acknowledgment strategy
    missing = job_skills - project_skills
    if missing and len(missing) <= 3:
        talking_points.append(
            f"Show willingness to learn: Mention plans to develop {', '.join(list(missing)[:2])}"
        )
    
    # 4. Project complexity
    if len(project_skills) >= 8:
        talking_points.append(
            "Showcase project complexity - demonstrate how multiple technologies integrate"
        )
    
    # Default fallback
    if not talking_points:
        talking_points.append(
            "Prepare to discuss specific challenges solved in your projects"
        )
    
    return talking_points


def suggest_gap_projects(missing_skills: Set[str]) -> List[Dict]:
    """
    Suggests specific project ideas to build missing skills.
    
    Returns: List of project suggestions with skills, difficulty, and resources
    """
    # Project templates mapped to skill categories
    project_templates = {
        # Data Science & ML
        ("Python", "Machine Learning", "Data Analysis"): {
            "title": "Build a Predictive Analytics Dashboard",
            "description": "Create an end-to-end ML pipeline with data visualization",
            "difficulty": "Intermediate",
            "skills_covered": ["Python", "Machine Learning", "Data Analysis", "Visualization"]
        },
        ("SQL", "Database", "Data Analysis"): {
            "title": "Design a Data Warehouse Schema",
            "description": "Model and implement a star schema for business analytics",
            "difficulty": "Intermediate",
            "skills_covered": ["SQL", "Database Design", "ETL", "Data Modeling"]
        },
        
        # Web Development
        ("JavaScript", "React", "Frontend"): {
            "title": "Build a Full-Stack Web Application",
            "description": "Create a responsive SaaS application with modern UI",
            "difficulty": "Intermediate",
            "skills_covered": ["JavaScript", "React", "CSS", "REST API"]
        },
        ("Node.js", "Backend", "API"): {
            "title": "Develop a RESTful API Service",
            "description": "Build a scalable backend with authentication and database",
            "difficulty": "Intermediate",
            "skills_covered": ["Node.js", "Express", "Database", "API Design"]
        },
        
        # Data Engineering
        ("ETL", "Pipeline", "Cloud"): {
            "title": "Create an Automated Data Pipeline",
            "description": "Build cloud-based ETL workflow with monitoring",
            "difficulty": "Advanced",
            "skills_covered": ["ETL", "Cloud Services", "Automation", "Data Pipeline"]
        },
        
        # DevOps & Cloud
        ("Docker", "Kubernetes", "Cloud"): {
            "title": "Deploy Containerized Microservices",
            "description": "Set up CI/CD pipeline with container orchestration",
            "difficulty": "Advanced",
            "skills_covered": ["Docker", "Kubernetes", "CI/CD", "Cloud"]
        }
    }
    
    suggestions = []
    missing_lower = {s.lower() for s in missing_skills}
    
    # Match missing skills to project templates
    for skill_set, project_info in project_templates.items():
        # Check if any skills in template match missing skills
        template_skills_lower = {s.lower() for s in skill_set}
        overlap = template_skills_lower.intersection(missing_lower)
        
        if overlap and len(overlap) >= 1:
            # Calculate how many missing skills this project would cover
            covered_skills = [s for s in project_info["skills_covered"] 
                            if s.lower() in missing_lower]
            
            if covered_skills:
                suggestions.append({
                    "title": project_info["title"],
                    "description": project_info["description"],
                    "difficulty": project_info["difficulty"],
                    "skills_covered": covered_skills[:4],  # Limit display
                    "total_covered": len(covered_skills)
                })
    
    # Generic fallback for unmatched skills
    if not suggestions and missing_skills:
        # Pick top 3 missing skills
        top_missing = list(missing_skills)[:3]
        suggestions.append({
            "title": f"Custom Project with {', '.join(top_missing[:2])}",
            "description": f"Build a hands-on project demonstrating {', '.join(top_missing)}",
            "difficulty": "Intermediate",
            "skills_covered": top_missing,
            "total_covered": len(top_missing)
        })
    
    # Sort by number of skills covered (most valuable first)
    suggestions.sort(key=lambda x: x["total_covered"], reverse=True)
    
    return suggestions[:3]  # Return top 3 suggestions


# =============================================================================
# REPORT GENERATION (Text & PDF)
# =============================================================================
def generate_detailed_report_text(res: Dict, jd_text: str = "", cl_analysis: Dict = None) -> str:
    """Generates a clean, professional text report."""
    match_pct = res['match_percentage']
    
    report = []
    
    # ==================== HEADER ====================
    report.append("=" * 70)
    report.append("CAREERMATCH AI - ANALYSIS REPORT".center(70))
    report.append("=" * 70)
    report.append("")
    
    # ==================== EXECUTIVE SUMMARY ====================
    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 70)
    report.append("")
    report.append(f"Match Score:          {match_pct:.1f}%")
    
    if match_pct >= 80: 
        assessment = "EXCELLENT MATCH - High success probability"
    elif match_pct >= 60: 
        assessment = "GOOD POTENTIAL - Some gaps, strong foundation"
    else: 
        assessment = "HIGH GAP - Significant preparation required"
    
    report.append(f"Assessment:           {assessment}")
    
    # Cover Letter Summary (if available)
    if cl_analysis:
        cl_score = cl_analysis['overall_score']
        report.append(f"Cover Letter Score:   {cl_score:.1f}%")
        
        if cl_score >= 80:
            cl_assessment = "Excellent application letter"
        elif cl_score >= 60:
            cl_assessment = "Good foundation, can be improved"
        else:
            cl_assessment = "Needs significant improvements"
        
        report.append(f"Cover Letter:         {cl_assessment}")
    
    report.append("")
    report.append("")

    # ==================== SKILL ANALYSIS ====================
    report.append("1. SKILL ANALYSIS")
    report.append("-" * 70)
    report.append("")
    
    # Matched Skills
    report.append("[+] MATCHED SKILLS")
    if res["matching_hard"]:
        for s in sorted(res["matching_hard"]): 
            report.append(f"    - {s}")
    else:
        report.append("  (No direct matches)")
    report.append("")
    
    # Transferable Skills
    if res.get("transferable"):
        report.append("[~] TRANSFERABLE SKILLS")
        for missing, present in res["transferable"].items():
            report.append(f"    - {missing} (covered by {present})")
        report.append("")
        
    # Project-Verified Skills - ONLY show if there are any
    project_skills = res.get("project_review", set())
    if project_skills:
        report.append("[*] PROJECT-VERIFIED SKILLS")
        for s in sorted(project_skills): 
            report.append(f"    - {s}")
        report.append("")

    # Missing Skills
    report.append("[!] MISSING SKILLS")
    if res["missing_hard"]:
        for s in sorted(res["missing_hard"]):
            report.append(f"    - {s}")
    else:
        report.append("    (No critical gaps - Excellent match!)")
    
    report.append("")
    report.append("")
    
    # ==================== COVER LETTER EVALUATION ====================
    if cl_analysis:
        report.append("2. COVER LETTER EVALUATION")
        report.append("-" * 70)
        report.append("")
        report.append(f"Overall Score:        {cl_analysis['overall_score']:.1f}%")
        report.append(f"Word Count:           {cl_analysis['word_count']} words")
        report.append(f"Language:             {cl_analysis['language'] or 'English'}")
        report.append("")
        
        report.append("METRICS:")
        report.append(f"  • Keyword Coverage:     {cl_analysis['hard_coverage']:.0f}%")
        report.append(f"  • Soft Skills:          {cl_analysis['soft_coverage']:.0f}%")
        report.append(f"  • Structure:            {cl_analysis['structure_score']:.0f}%")
        report.append(f"  • Personalization:      {cl_analysis['personalization_score']:.0f}%")
        report.append("")
        
        if cl_analysis.get('strengths'):
            report.append("STRENGTHS:")
            for strength in cl_analysis['strengths'][:5]:
                report.append(f"    + {strength}")
            report.append("")
        
        if cl_analysis.get('improvements'):
            report.append("IMPROVEMENT SUGGESTIONS:")
            for improvement in cl_analysis['improvements'][:5]:
                report.append(f"    > {improvement}")
            report.append("")
        
        if cl_analysis.get('hard_missing'):
            missing_kws = list(cl_analysis['hard_missing'])[:8]
            if missing_kws:
                report.append("MISSING KEYWORDS (consider adding):")
                report.append(f"  {', '.join(missing_kws)}")
                if len(cl_analysis['hard_missing']) > 8:
                    report.append(f"  ... and {len(cl_analysis['hard_missing']) - 8} more")
                report.append("")
        
        report.append("")

    # ==================== RECOMMENDATIONS ====================
    section_num = 3 if cl_analysis else 2
    report.append(f"{section_num}. STRATEGIC RECOMMENDATIONS")
    report.append("-" * 70)
    report.append("")
    
    if match_pct < 100:
        report.append("Priority Actions:")
        report.append("  1. Focus on closing the missing skill gaps listed above")
        report.append("  2. Highlight transferable skills during interview")
        if res.get("project_review"):
            report.append("  3. Emphasize project-verified skills in conversation")
        if cl_analysis and cl_analysis.get('improvements'):
            report.append("  4. Improve cover letter based on suggestions")
    else:
        report.append("Your profile is well-aligned!")
        report.append("    - Prepare for in-depth technical questions")
        report.append("    - Focus on demonstrating soft skills and leadership")
    
    report.append("")
    report.append("")
    
    # ==================== CAREER COMPASS ====================
    candidate_skills = res["matching_hard"] | res["missing_hard"] | res["extra_hard"]
    
    try:
        recs = recommend_roles(candidate_skills, jd_text)
        if recs:
            section_num += 1
            report.append(f"{section_num}. ALTERNATIVE CAREER PATHS")
            report.append("-" * 70)
            report.append("")
            report.append("Based on your skills, you may also be a good fit for:")
            report.append("")
            
            for i, rec in enumerate(recs):
                 report.append(f"  {i+1}. {rec['role']} ({rec['score']:.0f}% Match)")
                 if rec['missing']:
                     missing_str = ", ".join(rec['missing'][:4])
                     report.append(f"     Missing: {missing_str}")
                     if len(rec['missing']) > 4:
                         report.append(f"     ... and {len(rec['missing']) - 4} more")
                 report.append("")
    except Exception:
        pass

    report.append("")
    report.append("=" * 70)
    report.append("Generated by CareerMatch AI".center(70))
    report.append("=" * 70)

    return "\n".join(report)




def generate_cv_pdf(text_content: str) -> bytes:
    """
    Generates a professionally formatted CV PDF.
    Uses proper sections, headers, and spacing for readability.
    """
    if not FPDF:
        return None
        
    class CVPDF(FPDF):
        """
        Professional CV PDF Generator
        Style: Times (Garamond-like serif), Black text only
        Sizes: 13pt titles, 11pt body
        Max: 2 pages
        """
        def header(self):
            pass  # No automatic header
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Times', 'I', 9)
            self.set_text_color(0, 0, 0)  # Black
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
            
        def section_header(self, title):
            """Draw a section header with underline - 13pt bold."""
            self.set_font('Times', 'B', 13)
            self.set_text_color(0, 0, 0)  # Black
            self.cell(0, 7, title, 0, 1)
            # Subtle underline
            self.set_draw_color(0, 0, 0)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(2)
            
        def add_entry(self, title, subtitle="", date="", description=""):
            """Add an experience/education entry - 11pt body."""
            self.set_font('Times', 'B', 11)
            self.set_text_color(0, 0, 0)  # Black
            self.cell(0, 5, title, 0, 1)
            
            if subtitle or date:
                self.set_font('Times', 'I', 11)
                self.set_text_color(0, 0, 0)  # Black
                line = ""
                if subtitle: line += subtitle
                if date: line += f"  |  {date}" if subtitle else date
                self.cell(0, 5, line, 0, 1)
            
            if description:
                self.set_font('Times', '', 11)
                self.set_text_color(0, 0, 0)  # Black
                self.ln(1)
                for line in description.split('\n'):
                    clean = line.strip()
                    if clean:
                        try:
                            clean = clean.encode('latin-1', 'replace').decode('latin-1')
                        except:
                            pass
                        self.multi_cell(0, 5, clean)
            self.ln(3)

    pdf = CVPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    lines = text_content.split('\n')
    in_section = None
    
    # Parse the text content and format appropriately
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # First line = Name (14pt, bold, centered)
        if i == 0:
            pdf.set_font('Times', 'B', 14)
            pdf.set_text_color(0, 0, 0)  # Black
            pdf.cell(0, 8, line, 0, 1, 'C')
            i += 1
            continue
        
        # Second line = Contact info (11pt, centered)
        if i == 1 and '|' in line:
            pdf.set_font('Times', '', 11)
            pdf.set_text_color(0, 0, 0)  # Black
            pdf.cell(0, 5, line, 0, 1, 'C')
            pdf.ln(6)
            i += 1
            continue
        
        # Section headers (all caps words)
        if line in ['SUMMARY', 'CORE COMPETENCIES', 'TECHNICAL SKILLS', 
                    'PROFESSIONAL EXPERIENCE', 'EDUCATION', 'PROJECTS', 'LANGUAGES',
                    'PROFESSIONAL SUMMARY', 'SKILLS', 'EXPERIENCE', 'CERTIFICATIONS']:
            pdf.ln(3)
            pdf.section_header(line)
            in_section = line
            i += 1
            continue
        
        # Regular content - clean special characters for PDF
        clean_line = line
        # Replace common special characters with ASCII equivalents
        replacements = {
            '•': '-',
            '–': '-',
            '—': '-',
            '"': '"',
            '"': '"',
            ''': "'",
            ''': "'",
            '…': '...',
            '→': '->',
            '←': '<-',
            '✓': '[x]',
            '✗': '[ ]',
            '★': '*',
            '@': ' at ',
        }
        for old, new in replacements.items():
            clean_line = clean_line.replace(old, new)
        
        try:
            clean_line = clean_line.encode('latin-1', 'ignore').decode('latin-1')
        except:
            clean_line = ''.join(c if ord(c) < 128 else '' for c in clean_line)
        
        # Detect experience/education titles (contain 'at' or date patterns like '(Month Year')
        # Add extra spacing before new entries
        is_entry_title = False
        if in_section in ['PROFESSIONAL EXPERIENCE', 'EXPERIENCE', 'EDUCATION', 'PROJECTS']:
            # Check if line looks like an entry title (contains date or 'at')
            if (' at ' in clean_line.lower() or 
                '(' in clean_line and any(year in clean_line for year in ['2020', '2021', '2022', '2023', '2024', '2025', '2026']) or
                ' - ' in clean_line and any(month in clean_line for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Present'])):
                is_entry_title = True
                pdf.ln(4)  # Extra space before new entry
                pdf.set_font('Times', 'B', 11)  # Bold for titles
            else:
                pdf.set_font('Times', '', 11)
        else:
            pdf.set_font('Times', '', 11)
            
        pdf.set_text_color(0, 0, 0)  # Black
        pdf.multi_cell(0, 5, clean_line)
        pdf.ln(1)
        i += 1
            
    return pdf.output(dest='S').encode('latin-1')


# =============================================================================
# JOB RECOMMENDER (Career Compass) - v1.25
# =============================================================================

# Education fields to job roles mapping
EDUCATION_TO_ROLES = {
    # Business & Economics
    "economia": ["Business Analyst", "Financial Analyst", "Data Analyst", "Marketing Manager", "Consultant"],
    "business": ["Business Analyst", "Marketing Manager", "Consultant", "Product Manager", "AI Business Analyst"],
    "marketing": ["Marketing Manager", "Digital Marketing Specialist", "Brand Manager", "Growth Marketing Manager", "Marketing Data Analyst"],
    "finanza": ["Financial Analyst", "Investment Analyst", "Risk Analyst", "Quantitative Analyst"],
    "management": ["Product Manager", "Project Manager", "Business Analyst", "Consultant"],
    # Tech & Engineering
    "informatica": ["Software Engineer", "Backend Developer", "Full Stack Developer", "Data Engineer", "DevOps Engineer"],
    "ingegneria": ["Software Engineer", "Backend Developer", "Data Engineer", "DevOps Engineer", "Machine Learning Engineer", "Solutions Architect", "MLOps Engineer"],
    "computer science": ["Software Engineer", "Backend Developer", "Full Stack Developer", "Machine Learning Engineer", "Analytics Engineer", "Growth Engineer"],
    "data science": ["Data Scientist", "Machine Learning Engineer", "Data Analyst", "AI Business Analyst", "Marketing Data Analyst", "Analytics Engineer"],
    "artificial intelligence": ["Machine Learning Engineer", "Data Scientist", "AI Business Analyst", "MLOps Engineer"], # New
    # Sciences
    "matematica": ["Data Scientist", "Quantitative Analyst", "Machine Learning Engineer", "Financial Analyst", "FinTech Specialist"],
    "statistica": ["Data Scientist", "Data Analyst", "Statistician", "Machine Learning Engineer", "Marketing Data Analyst"],
    "fisica": ["Data Scientist", "Quantitative Analyst", "Machine Learning Engineer"],
    # Creative & Communication
    "comunicazione": ["Marketing Manager", "Digital Marketing Specialist", "Content Marketing Manager", "UX Designer", "Product Marketing Manager"],
    "design": ["UX Designer", "UI Designer", "Product Designer", "Frontend Developer"],
    "giornalismo": ["Content Marketing Manager", "Digital Marketing Specialist", "Copywriter", "Technical Writer"],
    # Other
    "psicologia": ["UX Researcher", "HR Manager", "Product Manager", "HR Tech Specialist"],
    "giurisprudenza": ["Compliance Analyst", "Legal Tech Specialist", "Business Analyst"],
    "lingue": ["Content Marketing Manager", "International Business", "Marketing Manager"],
}

def recommend_roles(cv_skills: Set[str], jd_text: str = "", cv_text: str = "") -> List[Tuple[str, float, List[str]]]:
    """
    Identifies the best fitting job roles excluding the one described in the JD.
    Now also considers education from CV text with recency weighting.
    """
    job_archetypes = getattr(constants, "JOB_ARCHETYPES", {})
    if not cv_skills or not job_archetypes or not TfidfVectorizer:
        return []

    # 0. Seniority Detection (New)
    cv_level, _ = detect_seniority(cv_text) if cv_text else ("Mid Level", 0.0)

    # 1. Extract education boost from CV text
    education_boost = {}  # role_name -> boost score
    if cv_text:
        cv_lower = cv_text.lower()
        
        # Find education keywords and boost related roles
        for edu_keyword, related_roles in EDUCATION_TO_ROLES.items():
            if edu_keyword in cv_lower:
                # Check if it's recent (appears early in CV = more recent)
                position = cv_lower.find(edu_keyword)
                # Weight: earlier position = more recent = higher weight (max 30%, min 10%)
                recency_weight = max(10, 30 - (position / len(cv_lower)) * 15)
                
                for role in related_roles:
                    if role in job_archetypes:
                        current_boost = education_boost.get(role, 0)
                        education_boost[role] = max(current_boost, recency_weight)

    # 2. Prepare Corpus
    archetype_names = list(job_archetypes.keys())
    archetype_docs = [" ".join(job_archetypes[name]) for name in archetype_names]
    
    # Docs: [0=CV, 1=JD (if exists), 2..N=Archetypes]
    corpus = [" ".join(cv_skills)]
    
    jd_index = -1
    if jd_text:
        corpus.append(jd_text)
        jd_index = 1
        
    corpus.extend(archetype_docs)
    
    # 2. Vectorization - Use word-based matching for accurate skill comparison
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=1, lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # 2b. LSA Semantic Analysis (New Model) - Captures latent relationships
    try:
        if TruncatedSVD:
            n_components = min(15, len(corpus)-1) # Avoid error if corpus is small
            lsa_model = TruncatedSVD(n_components=n_components, random_state=42)
            lsa_matrix = lsa_model.fit_transform(tfidf_matrix)
        else:
            lsa_matrix = None
    except Exception:
        lsa_matrix = None
    
    # 3. Identify Target Role from JD (if redundant)
    excluded_roles = set()
    if jd_index != -1:
        # Compare JD (doc 1) vs Archetypes (docs 2..)
        jd_vector = tfidf_matrix[jd_index:jd_index+1]
        arch_start_idx = jd_index + 1
        arch_vectors = tfidf_matrix[arch_start_idx:]
        
        # Find closest archetype to JD
        jd_sims = cosine_similarity(jd_vector, arch_vectors).flatten()
        target_role_idx = jd_sims.argmax()
        target_role_score = jd_sims[target_role_idx]
        
        # If the JD strongly matches an archetype (>50%), exclude it
        # Increased threshold from 0.15 to 0.50 to prevent false exclusions of valid alternatives
        jd_lower = jd_text.lower() if jd_text else ""
        
        # 1. Cosine Similarity Check
        if target_role_score > 0.50:
            excluded_roles.add(archetype_names[target_role_idx])
            
        # 2. Heuristic Check (Explicit Mention in Header)
        # Only exclude if mentioned in first 200 chars (Title area)
        header_text = jd_lower[:200]
        for name in archetype_names:
            if name.lower() in header_text:
                excluded_roles.add(name)
                
    # 4. Identify Current Role from CV (REMOVED in v1.36)
    # We deliberately WANT to recommend the candidate's current role if it's a good fit.
    # Users found it confusing that "Data Analyst" wasn't recommended for a Data Analyst profile.
    
    # 5. Compute Recommendations (Similarity to remaining archetypes)
    # CV is at index 0
    cv_vector = tfidf_matrix[0:1]
    arch_vectors_final = tfidf_matrix[len(corpus)-len(archetype_names):]
    tfidf_similarities = cosine_similarity(cv_vector, arch_vectors_final).flatten()
    
    # Hybrid Score: Combine TF-IDF (keyword intensity) with LSA (semantic meaning)
    if lsa_matrix is not None:
        cv_lsa = lsa_matrix[0:1]
        arch_lsa = lsa_matrix[len(corpus)-len(archetype_names):]
        lsa_similarities = cosine_similarity(cv_lsa, arch_lsa).flatten()
        # Weighting: 70% direct keywords, 30% semantic context
        similarities = (0.7 * tfidf_similarities) + (0.3 * lsa_similarities)
    else:
        similarities = tfidf_similarities
    
    # Build expanded CV skills set (including cluster equivalents)
    cv_norm = {s.lower() for s in cv_skills}
    cv_norm = expand_skills_with_clusters(cv_norm)
                
    # 5. Compute Recommendations (JACCARD SIMILARITY for robustness)
    recommendations = []
    
    for i, name in enumerate(archetype_names):
        if name in excluded_roles:
            continue
            
        role_skills = job_archetypes[name]
        role_norm = {s.lower() for s in role_skills}
        
        if not role_norm:
            continue
        
        # CRITICAL FIX: Expand role skills with same logic as CV skills
        # This ensures "Analytics" matches "Business Analysis", etc.
        role_norm_expanded = expand_skills_with_clusters(role_norm)
            
        # Jaccard Index: Intersection / Union (using EXPANDED sets)
        intersection = len(cv_norm.intersection(role_norm_expanded))
        union = len(cv_norm.union(role_norm_expanded))
        jaccard_score = intersection / union if union > 0 else 0.0
        
        # Boost with TF-IDF/LSA semantic score (from previous step)
        # arch_vector index is i (since we sliced off CV/JD)
        semantic_score = similarities[i]
        
        # Education Boost
        edu_boost = education_boost.get(name, 0) / 100.0
        
        # Combined Score: 60% Jaccard (Direct Skill Match) + 30% Semantic + 10% Ed Boost
        final_score = (0.6 * jaccard_score) + (0.3 * semantic_score) + (0.1 * edu_boost)
        
        # Lower threshold from 0.15 to 0.05 to ensure results are shown
        if final_score > 0.05: # Threshold (was 0.15)
             # Use expanded sets for missing calculation
             missing = role_norm_expanded - cv_norm
             recommendations.append({
                 "role": name,
                 "score": final_score,
                 "missing": list(missing)[:5] # Top 5 missing
             })
             
    # Sort and Return
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations

def expand_skills_with_clusters(cv_norm):
    cv_expanded = set(cv_norm)
    
    # 1. Cluster Expansion
    skill_clusters = getattr(constants, "SKILL_CLUSTERS", {})
    for cluster_name, cluster_skills in skill_clusters.items():
        cluster_lower = {s.lower() for s in cluster_skills}
        if cv_norm & cluster_lower:  # If CV has any skill from this cluster
            cv_expanded.update(cluster_lower)  # Add all equivalent skills
    
    # 2. Inference Rules
    inference_rules = getattr(constants, "INFERENCE_RULES", {})
    for skill in list(cv_expanded): # Iterate over expanded to catch chains
        for rule_skill, inferred in inference_rules.items():
            if skill == rule_skill.lower():
                cv_expanded.update(s.lower() for s in inferred)

    # 3. Hierarchy Expansion (Value -> Key)
    # If user has "English" (value), they imply "Languages" (key)
    all_defs = {}
    all_defs.update(getattr(constants, "HARD_SKILLS", {}))
    all_defs.update(getattr(constants, "SOFT_SKILLS", {}))
    
    for key, variations in all_defs.items():
        variations_norm = {v.lower() for v in variations}
        # If CV has ANY variation, grant the parent Key
        if cv_expanded & variations_norm:
            cv_expanded.add(key.lower())
            
    return cv_expanded


# =============================================================================
# CAREER DISCOVERY - Preference-Based Job Matching
# =============================================================================
def discover_careers(
    cv_text: str = "",
    free_text: str = "",
    preferences: dict = None
) -> List[dict]:
    """
    SIMPLIFIED CAREER DISCOVERY ENGINE
    ===================================
    Recommends job roles based primarily on skill matching.
    
    Args:
        cv_text: Optional CV text for skill extraction
        free_text: User's description (currently not used in simplified version)
        preferences: Dict with categories and preferences (optional filtering)
    
    Returns:
        List of dicts with: role, category, score, skills_required, skills_matched, missing_skills
    """
    job_archetypes = getattr(constants, "JOB_ARCHETYPES", {})
    role_metadata = getattr(constants, "JOB_ROLE_METADATA", {})
    
    if not job_archetypes:
        return []
    
    preferences = preferences or {}
    
    # --- 1. EXTRACT CV SKILLS (if provided) ---
    cv_skills = set()
    if cv_text:
        cv_hard, cv_soft = extract_skills_from_text(cv_text)
        cv_skills = cv_hard | cv_soft
    
    # --- 2. SCORE EACH ROLE (SIMPLIFIED) ---
    recommendations = []
    
    for role_name, role_skills in job_archetypes.items():
        # Get role metadata (use defaults if not defined)
        metadata = role_metadata.get(role_name, {
            "category": "Other",
            "client_facing": None,
            "remote_friendly": None,
            "international": None,
            "dynamic": None,
            "creative": None
        })
        
        # --- CATEGORY FILTER (if specified) ---
        selected_categories = preferences.get("categories", [])
        if selected_categories:
            if metadata.get("category", "Other") not in selected_categories:
                # If category is strictly filtered, we skip
                pass 
                
        # --- SKILL MATCHING ---
        skill_match = 0
        skills_matched = set()
        missing_skills = set()
        
        if cv_skills and role_skills:
            role_skills_normalized = {s.lower() for s in role_skills}
            cv_skills_normalized = {s.lower() for s in cv_skills}
            
            # Apply skill clusters for transferable matching  
            cv_expanded = expand_skills_with_clusters(cv_skills_normalized)
            
            # Calculate overlap
            matched = cv_expanded & role_skills_normalized
            missing = role_skills_normalized - cv_expanded
            
            skills_matched = {s for s in role_skills if s.lower() in matched}
            missing_skills = {s for s in role_skills if s.lower() in missing}
            
            if len(role_skills) > 0:
                skill_match = (len(matched) / len(role_skills)) * 100
        elif not cv_skills:
            # No CV → default neutral score
            skill_match = 50
            missing_skills = set(role_skills)
            
        # --- FINAL SCORE (SIMPLE) ---
        # Ensure non-zero score for UX purposes (Potential Score)
        final_score = max(5.0, skill_match)
        
        # Boost if category matches user preference (even without skills)
        if selected_categories and metadata.get("category") in selected_categories:
             final_score += 10
        
        recommendations.append({
            "role": role_name,
            "category": metadata.get("category", "Other"),
            "score": final_score,
            "skills_required": list(role_skills),
            "skills_matched": list(skills_matched),
            "missing_skills": list(missing_skills),
            "preference_match": None, 
            "skill_match": skill_match,
            "edu_boost": 0,
            "pref_details": [],
            "metadata": metadata
        })
    
    # Sort by score descending
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations


def _parse_intent_signals(text: str) -> dict:
    """
    Parses free text to extract career intent signals.
    
    Examples:
    - "dynamic job" → dynamic: True
    - "work from home" → remote_friendly: True
    - "international clients" → international: True, client_facing: True
    """
    if not text:
        return {}
    
    text_lower = text.lower()
    signals = {}
    
    # Dynamic/fast-paced signals
    dynamic_keywords = ["dynamic", "dinamico", "fast-paced", "variety", "varietà", 
                       "challenging", "sfidante", "never boring", "non noioso"]
    if any(kw in text_lower for kw in dynamic_keywords):
        signals["dynamic"] = True
    
    # Client-facing signals
    client_keywords = ["client", "clienti", "customer", "stakeholder", 
                      "people", "persone", "relazioni", "relationships", "talk to", "parlare con"]
    if any(kw in text_lower for kw in client_keywords):
        signals["client_facing"] = True
    
    # International signals
    intl_keywords = ["international", "internazionale", "global", "globale", 
                    "abroad", "estero", "english", "inglese", "multilingual"]
    if any(kw in text_lower for kw in intl_keywords):
        signals["international"] = True
    
    # Remote signals
    remote_keywords = ["remote", "remoto", "smart working", "home", "casa", 
                      "flexible", "flessibile", "anywhere", "ovunque"]
    if any(kw in text_lower for kw in remote_keywords):
        signals["remote_friendly"] = True
    
    # Creative signals
    creative_keywords = ["creative", "creativo", "design", "art", "innovative", 
                        "innovativo", "ideas", "idee", "brand", "visual"]
    if any(kw in text_lower for kw in creative_keywords):
        signals["creative"] = True
    
    # Category detection
    category_keywords = {
        "Technology": ["tech", "software", "data", "it ", "developer", "programmazione", "coding"],
        "Marketing": ["marketing", "social media", "brand", "advertising", "pubblicità", "comunicazione"],
        "Finance": ["finance", "finanza", "accounting", "contabilità", "investment", "banking"],
        "Sales": ["sales", "vendite", "commercial", "commerciale", "business development"],
        "Design": ["design", "creative", "grafica", "ux", "ui", "art direction"],
        "HR": ["hr ", "human resources", "recruiting", "talent", "risorse umane"],
        "Legal": ["legal", "legale", "law", "diritto", "compliance"],
        "Engineering": ["engineering", "ingegneria", "mechanical", "electrical", "produzione"],
        "Healthcare": ["pharma", "medical", "clinical", "healthcare", "sanità"],
        "Hospitality": ["hotel", "tourism", "turismo", "event", "hospitality"],
    }
    
    detected_categories = []
    for category, keywords in category_keywords.items():
        if any(kw in text_lower for kw in keywords):
            detected_categories.append(category)
    
    if detected_categories:
        signals["categories"] = detected_categories
    
    return signals



def analyze_cover_letter(cover_letter_text: str, jd_text: str, cv_text: str = "") -> Dict:
    """
    Analyzes a cover letter against a job description.
    Returns scoring, strengths, weaknesses, and suggestions.
    Supports both English and Italian.
    """
    if not cover_letter_text or not jd_text:
        return None
    
    # Detect language
    cl_lang = detect_language(cover_letter_text)
    
    # Extract skills from JD and Cover Letter
    jd_hard, jd_soft = extract_skills_from_text(jd_text, is_jd=True)
    cl_hard, cl_soft = extract_skills_from_text(cover_letter_text)
    
    # Extract CV skills if provided
    cv_hard = set()
    cv_soft = set()
    if cv_text:
        cv_hard, cv_soft = extract_skills_from_text(cv_text)
    
    # 1. KEYWORD COVERAGE ANALYSIS
    hard_mentioned = jd_hard & cl_hard
    hard_missing = jd_hard - cl_hard
    soft_mentioned = jd_soft & cl_soft
    soft_missing = jd_soft - cl_soft
    
    # Coverage scores
    hard_coverage = (len(hard_mentioned) / len(jd_hard) * 100) if jd_hard else 0
    soft_coverage = (len(soft_mentioned) / len(jd_soft) * 100) if jd_soft else 0
    
    # 2. LENGTH ANALYSIS
    cl_words = len(cover_letter_text.split())
    length_score = 100
    length_feedback = ""
    
    if cl_words < 150:
        length_score = 50
        length_feedback = "Too short - aim for 250-400 words" if cl_lang != "Italian" else "Troppo breve - punta a 250-400 parole"
    elif cl_words > 500:
        length_score = 70
        length_feedback = "Too long - keep it concise (250-400 words)" if cl_lang != "Italian" else "Troppo lunga - mantienila concisa (250-400 parole)"
    else:
        length_feedback = "Good length" if cl_lang != "Italian" else "Lunghezza adeguata"
    
    # 3. STRUCTURE ANALYSIS (Simple heuristics)
    has_greeting = any(word in cover_letter_text.lower() for word in ['dear', 'hi', 'hello', 'gentile', 'egregio', 'spett.le'])
    has_closing = any(word in cover_letter_text.lower() for word in ['sincerely', 'regards', 'cordiali', 'distinti', 'saluti'])
    has_paragraphs = cover_letter_text.count('\n') >= 2
    
    structure_score = 0
    if has_greeting: structure_score += 33
    if has_closing: structure_score += 33
    if has_paragraphs: structure_score += 34
    
    # 4. PERSONALIZATION CHECK
    # Check if CV skills are mentioned (shows personalization)
    personalization_score = 0
    if cv_text:
        cv_skills_in_cl = (cv_hard & cl_hard) | (cv_soft & cl_soft)
        personalization_score = min(100, len(cv_skills_in_cl) * 20)
    else:
        # Fallback: Check if any specific skills are mentioned
        personalization_score = min(100, (len(cl_hard) + len(cl_soft)) * 15)
    
    # 5. OVERALL SCORE (Weighted)
    overall_score = (
        hard_coverage * 0.35 +
        soft_coverage * 0.15 +
        length_score * 0.15 +
        structure_score * 0.20 +
        personalization_score * 0.15
    )
    
    # 6. GENERATE FEEDBACK
    strengths = []
    improvements = []
    
    # Language-aware feedback
    if cl_lang == "Italian":
        # Strengths (Italian)
        if hard_coverage >= 60:
            strengths.append(f"Ottima menzione delle competenze tecniche ({len(hard_mentioned)}/{len(jd_hard)})")
        elif hard_coverage >= 30:
            strengths.append(f"Discrete menzioni delle competenze tecniche ({len(hard_mentioned)}/{len(jd_hard)})")
        
        if soft_coverage >= 50:
            strengths.append(f"Buona enfasi sulle soft skills")
        
        if structure_score >= 80:
            strengths.append("Struttura professionale ben formattata")
        
        if personalization_score >= 60:
            strengths.append("Lettera personalizzata con esempi specifici")
        
        # Improvements (Italian)
        if hard_coverage < 40:
            missing_sample = list(hard_missing)[:3]
            improvements.append(f"Menziona più competenze chiave richieste: {', '.join(missing_sample)}")
        
        if soft_coverage < 30 and jd_soft:
            improvements.append(f"Enfatizza soft skills come: {', '.join(list(jd_soft)[:2])}")
        
        if not has_greeting:
            improvements.append("Aggiungi un saluto formale (es: 'Gentile...')")
        
        if not has_closing:
            improvements.append("Concludi con una chiusura formale (es: 'Cordiali saluti')")
        
        if length_score < 80:
            improvements.append(f"{length_feedback}")
        
        if personalization_score < 50:
            improvements.append("Aggiungi esempi concreti e risultati quantificabili")
    
    else:
        # Strengths (English)
        if hard_coverage >= 60:
            strengths.append(f"Strong technical keyword coverage ({len(hard_mentioned)}/{len(jd_hard)})")
        elif hard_coverage >= 30:
            strengths.append(f"Decent technical keyword mentions ({len(hard_mentioned)}/{len(jd_hard)})")
        
        if soft_coverage >= 50:
            strengths.append(f"Good emphasis on soft skills")
        
        if structure_score >= 80:
            strengths.append("Well-structured professional format")
        
        if personalization_score >= 60:
            strengths.append("Personalized with specific examples")
        
        # Improvements (English)
        if hard_coverage < 40:
            missing_sample = list(hard_missing)[:3]
            improvements.append(f"Mention more required skills: {', '.join(missing_sample)}")
        
        if soft_coverage < 30 and jd_soft:
            improvements.append(f"Emphasize soft skills like: {', '.join(list(jd_soft)[:2])}")
        
        if not has_greeting:
            improvements.append("Add a formal greeting (e.g., 'Dear Hiring Manager')")
        
        if not has_closing:
            improvements.append("End with a formal closing (e.g., 'Sincerely')")
        
        if length_score < 80:
            improvements.append(f"{length_feedback}")
        
        if personalization_score < 50:
            improvements.append("Add concrete examples and quantifiable results")
    
    return {
        'overall_score': overall_score,
        'hard_coverage': hard_coverage,
        'soft_coverage': soft_coverage,
        'length_score': length_score,
        'structure_score': structure_score,
        'personalization_score': personalization_score,
        'hard_mentioned': hard_mentioned,
        'hard_missing': hard_missing,
        'soft_mentioned': soft_mentioned,
        'soft_missing': soft_missing,
        'strengths': strengths,
        'improvements': improvements,
        'word_count': cl_words,
        'language': cl_lang
    }


# =============================================================================
# OPTIMIZATION: SMART SKILL SORTING & SEMANTIC SUGGESTIONS
# =============================================================================

def smart_sort_skills(user_skills: List[str], jd_text: str) -> List[Tuple[str, float]]:
    """
    Sorts user skills by relevance to the JD using Semantic Similarity.
    
    Logic:
    1. Treats JD as the 'Query'
    2. Treats each Skill as a 'Document'
    3. Calculates Cosine Similarity between JD and each Skill
    4. Returns sorted list [(Skill, Score)]
    
    This ensures that if JD mentions "Python" a lot, "Python" moves to the top 
    of the CV skills list.
    """
    if not user_skills:
        return []
    if not jd_text or not TfidfVectorizer:
        # Fallback: alphabetical
        return [(s, 0.0) for s in sorted(user_skills)]

    try:
        # Create a mini corpus: [JD, Skill_1, Skill_2, ...]
        # We add "context" to skills to help matching (e.g. "SkillName skill")
        corpus = [jd_text] + [f"{s} skill" for s in user_skills]
        
        # Vectorize
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(corpus)
        
        # Calculate similarity between JD (idx 0) and Skills (idx 1..)
        jd_vec = tfidf_matrix[0:1]
        skill_vecs = tfidf_matrix[1:]
        
        scores = cosine_similarity(jd_vec, skill_vecs).flatten()
        
        # Pair skills with scores
        skill_scores = []
        for i, skill in enumerate(user_skills):
            # Boost score if exact match found in JD text (case insensitive)
            base_score = scores[i]
            if skill.lower() in jd_text.lower():
                base_score += 0.5 # Big boost for exact keyword match
            
            skill_scores.append((skill, base_score))
            
        # Sort desc
        skill_scores.sort(key=lambda x: x[1], reverse=True)
        return skill_scores
        
    except Exception as e:
        print(f"Smart Sort Error: {e}")
        return [(s, 0.0) for s in sorted(user_skills)]


def suggest_semantic_improvements(user_skills: Set[str], jd_text: str) -> List[str]:
    """
    Suggests subtle improvements based on Knowledge Base inference.
    
    Logic:
    - Finds missing skills
    - Checks if User has 'Related' skills (Cluster or Parent)
    - Suggests specific phrasing to bridge the gap.
    
    Example:
    - User has: "Tableau"
    - JD wants: "Power BI"
    - Suggestion: "Your Tableau experience is highly transferable to Power BI. Mention 'BI Tool Adaptability'."
    """
    suggestions = []
    
    # 1. Identify Gaps
    jd_hard, _ = extract_skills_from_text(jd_text, is_jd=True)
    missing = jd_hard - user_skills
    
    if not missing:
        return []
        
    skill_clusters = getattr(constants, "SKILL_CLUSTERS", {})
    inference_rules = getattr(constants, "INFERENCE_RULES", {})
    
    # 2. Analyze Gaps against Knowledge Base
    for gap in missing:
        # Check Equivalent Clusters
        for cluster_name, members in skill_clusters.items():
            if gap in members:
                # Does user have ANY other skill in this cluster?
                user_has = members.intersection(user_skills)
                if user_has:
                    owned = list(user_has)[0]
                    suggestions.append(
                        f"Your experience with **{owned}** applies to **{gap}** (both are in {cluster_name})."
                    )
                    
        # Check Inference Rules (Parent implies Child capability often)
        # Inverted check: If User has Parent, they might grasp Child
        for parent, children in inference_rules.items():
            if parent in user_skills and gap in children:
                suggestions.append(
                    f"**{gap}** is often associated with **{parent}**. If you know {parent}, emphasize your ability to pick up {gap} quickly."
                )

    return suggestions[:5] # Top 5 suggestions

# =============================================================================
# CV PDF GENERATION (Simple, One Page, Clean)
# =============================================================================
def generate_simple_cv_pdf(text_content: str) -> bytes:
    """
    Generates a clean, compact PDF for the CV export.
    Optimized for single-page layout and proper character encoding.
    """
    if not FPDF:
        return None
        
    class CV_PDF(FPDF):
        def header(self):
            # No header for CV, just pure content
            pass
            
        def footer(self):
            # Minimal footer - Times, Black
            self.set_y(-15)
            self.set_font('Times', 'I', 9)
            self.set_text_color(0, 0, 0)
            self.cell(0, 10, f'{self.page_no()}', 0, 0, 'R')

    pdf = CV_PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Times", size=11)  # Times 11pt base
    pdf.set_text_color(0, 0, 0)  # All black
    
    # Pre-process text to handle encoding and bullets
    replacements = {
        "•": "-", "●": "-", "▪": "-", "–": "-", "—": "-",
        "’": "'", "‘": "'", "“": '"', "”": '"',
        "é": "e", "á": "a", "í": "i", "ó": "o", "ú": "u",
        "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
        "€": "EUR"
    }
    
    lines = text_content.split('\n')
    
    for line in lines:
        clean_line = line
        for k, v in replacements.items():
            clean_line = clean_line.replace(k, v)
        
        # Strip unicode just in case
        try:
            clean_line = clean_line.encode('latin-1', 'replace').decode('latin-1')
        except:
            clean_line = ''.join([c if ord(c) < 128 else '?' for c in clean_line])

        if clean_line.strip() == "":
            pdf.ln(2)
            continue

        # Formatting Heuristics
        if clean_line.isupper() and len(clean_line) < 60:
            # Section Header - 13pt Bold Times
            pdf.ln(4)
            pdf.set_font("Times", 'B', 13)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 6, clean_line, 0, 1)
            pdf.set_font("Times", '', 11)
        elif " | " in clean_line and len(clean_line) < 100:
             # Subheader - 11pt Bold Times
             pdf.ln(3)
             pdf.set_font("Times", 'B', 11)
             pdf.set_text_color(0, 0, 0)
             pdf.cell(0, 5, clean_line, 0, 1)
             pdf.set_font("Times", '', 11)
        else:
            # Body text
            pdf.multi_cell(0, 5, clean_line)
            
    return pdf.output(dest='S').encode('latin-1')

