import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List
import urllib.parse

# Force Streamlit Cloud Update
# Optional Imports with robust handling
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.cluster import KMeans, AgglomerativeClustering
    from sklearn.decomposition import PCA
    from sklearn.metrics.pairwise import cosine_similarity
    import scipy.cluster.hierarchy as sch
    import matplotlib.pyplot as plt
except ImportError:
    RandomForestClassifier = None
    TfidfVectorizer = None
    Pipeline = None
    KMeans = None
    AgglomerativeClustering = None
    PCA = None
    sch = None
    plt = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from fpdf import FPDF
except ImportError:
    FPDF = None

import constants

# =============================================================================
@st.cache_resource
def train_rf_model():
    """
    Trains a Random Forest model on Hard Skills from constants.py.
    Returns (pipeline, dataframe).
    """
    # Prepare Data
    data = []

    # Check if HARD_SKILLS exists in constants (Backward compatibility)
    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})

    for skill_name, keywords in hard_skills.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})
            data.append({"text": f"used {kw}", "label": skill_name})

    for skill_name, keywords in soft_skills.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})

    df = pd.DataFrame(data)

    if df.empty:
        return None, df

    # If sklearn is missing or failed to import
    if not RandomForestClassifier or not TfidfVectorizer or not Pipeline:
        return None, df

    try:
        pipe = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=1000)),
            ('rf', RandomForestClassifier(n_estimators=50, random_state=42))
        ])
        pipe.fit(df['text'], df['label'])
        return pipe, df
    except Exception as e:
        print(f"Training Error: {e}")
        return None, df

# =============================================================================
def perform_skill_clustering(skills: List[str]):
    """
    Performs K-Means and Hierarchical Clustering on a list of skills.
    Returns:
    - kmeans_fig: Plotly figure for K-Means (PCA 2D)
    - dendrogram_img_path: Path to saved dendrogram image
    - clusters: Dict of {skill: cluster_id}
    """
    if not skills or len(skills) < 3:
        return None, None, {}

    if not TfidfVectorizer or not KMeans or not sch:
        return None, None, {}

    try:
        # 1. Vectorize Skills
        # ACTION: Use 'char_wb' (Character N-Grams Within Boundaries)
        # This is CRITICAL for skills. 'char' matches "Java" and "JavaScript" well, but 'char_wb' matches "Data" in "Data Science" better.
        # ngram_range=(2, 4) captures "SQ" in "SQL", "Py" in "Python".
        vectorizer = TfidfVectorizer(stop_words='english', analyzer='char_wb', ngram_range=(2, 4), min_df=1)
        X = vectorizer.fit_transform(skills).toarray()

        # 2. Hierarchical Clustering (Dendrogram)
        # Using Ward's linkage (Minimizes Variances) to create balanced clusters
        linkage_matrix = sch.linkage(X, method='ward')
        
        plt.figure(figsize=(12, 8)) # Taller figure
        # Thicker lines and explicit color threshold to ensure visual coloring
        sch.set_link_color_palette(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
        
        # Threshold: 0.7 * max (Standard for Ward).
        dendro = sch.dendrogram(linkage_matrix, labels=skills, leaf_rotation=45, leaf_font_size=12, above_threshold_color='#AAAAAA', color_threshold=0.7*max(linkage_matrix[:,2].max(), 0.1))
        
        plt.rcParams['lines.linewidth'] = 2.5 # Global setting for line thickness
        plt.title("Skill Dendrogram (Ward Linkage - v2)") # Explicit title to reassure user
        plt.tight_layout()
        # CACHE BUSTING: Change filename to force browser reload
        dendro_path = "dendrogram_v2.png" 
        plt.savefig(dendro_path)
        plt.close()

        # 3. K-Means Clustering
        # Determine K (simple heuristic: sqrt(N/2) or max 3-5 for small skill sets)
        n_clusters = max(2, min(len(skills) // 3, 5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)

        skill_clusters = {skill: int(label) for skill, label in zip(skills, labels)}

        # 4. Visualization (PCA to 2D)
        pca = PCA(n_components=2)
        coords = pca.fit_transform(X)

        df_viz = pd.DataFrame({
            'x': coords[:, 0],
            'y': coords[:, 1],
            'skill': skills,
            'cluster': [f"Cluster {l}" for l in labels]
        })

        return df_viz, dendro_path, skill_clusters

    except Exception as e:
        print(f"Clustering Error: {e}")
        return None, None, {}

# --- NEW: TOPIC MODELING (LDA) ---
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
    Performs Latent Dirichlet Allocation (LDA) to extract topics from text.
    Returns a list of topics (each topic is a string of keywords) and a WordCloud image path.
    """
    if not LatentDirichletAllocation or not CountVectorizer or not WordCloud:
        return [], None

    try:
        # Custom Stop Words for HR/Recruiting Context (Aggressive)
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
            'years', 'year', 'level', 'senior', 'junior', 'mid', 'associate', # debatable, but often generic in topic
            'full-time', 'part-time', 'contract', 'permanent', 'temporary', 'remote', 'hybrid',
            'degree', 'bachelor', 'master', 'phd', 'equivalent', 'related', 'relevant',
            'including', 'include', 'includes', 'various', 'similar', 'etc', 'suite',
            'must', 'will', 'can', 'may', 'should', 'would', 'tools', 'environment'
        ]

        # Italian Stop Words (Manual List to avoid dependency issues)
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
            # Apostrophe handling (tokenizers often split 'dell', 'all')
            'dell', 'all', 'sull', 'dall', 'nell', 'quest', 'quant', 'tant'
        ]

        # Manually filter stop words from vocabulary if CountVectorizer didn't catch them
        # (Alternatively, pass list to stop_words, but 'english' + list is tricky in sklearn < 0.24)
        # Better approach: extend the built-in english list
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
        all_stop_words = list(ENGLISH_STOP_WORDS) + hr_stop_words + it_stop_words

        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=all_stop_words)
        tf = tf_vectorizer.fit_transform(text_corpus)

        lda = LatentDirichletAllocation(n_components=n_topics, max_iter=10, learning_method='online', random_state=42)
        lda.fit(tf)

        feature_names = tf_vectorizer.get_feature_names_out()
        topics = []

        # Extract top words for each topic
        for topic_idx, topic in enumerate(lda.components_):
            top_features_ind = topic.argsort()[:-n_words - 1:-1]
            top_features = [feature_names[i] for i in top_features_ind]
            topics.append(f"Topic {topic_idx+1}: {', '.join(top_features)}")

        # Generate Word Cloud for the first topic (or combined)
        # Flattening simple corpus for cloud
        # Flattening simple corpus for cloud
        combined_text = " ".join(text_corpus)
        wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=set(all_stop_words)).generate(combined_text)
        
        wc_path = "topic_wordcloud.png"
        wordcloud.to_file(wc_path)

        return topics, wc_path

    except Exception as e:
        print(f"LDA Error: {e}")
        return [], None

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
    Extracts named entities (Organizations, GPE, Date) using NLTK with advanced filtering.
    """
    if not nltk:
        return {}

    entities = {"Organizations": [], "Locations": [], "Persons": []}

    # 1. Build Exclusion Set (Skills + Headers + Common Noise)
    # 1. Build Exclusion Set (Skills + Headers + Common Noise)
    exclusion_set = set()
    
    # helper to add flattened parts of skills
    def add_to_exclusion(term):
        parts = term.lower().split()
        for p in parts:
            exclusion_set.add(p)
            
    # Add Hard Skills
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
        "python", "java", "scala", "c++", "c#", "net", "javascript", "typescript", "php", "ruby", "go", "golang",
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

    # Add Common CV Headers & Noise
    noise_words = {
        "curriculum", "vitae", "resume", "cv", "profile", "summary", 
        "experience", "education", "skills", "projects", "languages",
        "certifications", "interests", "references", "contacts",
        "email", "phone", "address", "date", "present", "current",
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
        "january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december",
        "page", "of", "senior", "junior", "mid", "level", "lead", "manager", "support",
        "competenze", "esperienze", "formazione", "istruzione", "lingue", "progetti",
        "certificazioni", "interessi", "contatti", "profilo", "sommario",
        "university", "università", "school", "scuola", "college", "institute", "politecnico", "degree", "bachelor", "master", "phd",
        "dataflow" 
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

    insight = "### 💡 AI Analysis of your Profile Structure\n\n"

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
            insight += "- 🚀 **Assessment**: You are very strong in this area.\n"
        elif coverage < 30:
            insight += "- ⚠️ **Assessment**: This seems to be a significant gap area for you.\n"
        else:
            insight += "- ℹ️ **Assessment**: You have some foundation here, but room to improve.\n"

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
try:
    from thefuzz import fuzz
except ImportError:
    fuzz = None

# =============================================================================
def extract_skills_from_text(text: str) -> Tuple[Set[str], Set[str]]:
    hard_found = set()
    soft_found = set()
    text_lower = text.lower()

    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})
    inference_rules = getattr(constants, "INFERENCE_RULES", {})

    # Pre-process text for fuzzy matching (split into words)
    text_words = set(text_lower.split())

    # 1. Regex Match Hard Skills (Exact + Fuzzy)
    for skill, variations in hard_skills.items():
        matched = False
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                hard_found.add(skill)
                matched = True
                break

        # FUZZY FALLBACK (Robustness)
        if not matched and fuzz:
            # Check if any word in text is > 90% similar to the skill name
            for word in text_words:
                if fuzz.ratio(word, skill.lower()) > 90:
                    hard_found.add(skill)
                    break

    # 2. Regex Match Soft Skills (Exact + Fuzzy)
    for skill, variations in soft_skills.items():
        matched = False
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                soft_found.add(skill)
                matched = True
                break

        # FUZZY FALLBACK
        if not matched and fuzz:
             for word in text_words:
                if fuzz.ratio(word, skill.lower()) > 90:
                    soft_found.add(skill)
                    break

    # 3. Hierarchical Inference
    inferred_skills = set()
    for child_skill in hard_found:
        if child_skill in inference_rules:
            parents = inference_rules[child_skill]
            inferred_skills.update(parents)
    hard_found.update(inferred_skills)

    # 4. Generic Fallback
    if len(hard_found) < 2:
        generic_keywords = extract_generic_keywords(text, top_n=5)
        for kw in generic_keywords:
            hard_found.add(kw.capitalize())

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

def generate_pdf_report(res: Dict, jd_text: str = "") -> bytes:
    """
    Generates a professional PDF report with advanced styling.
    """
    if not FPDF:
        return b"FPDF library missed."

    class PDF(FPDF):
        def header(self):
            # Banner Navy Blue
            self.set_fill_color(20, 29, 44)  # #141d2c
            self.rect(0, 0, 210, 40, 'F')

            # Title
            self.set_font('Arial', 'B', 24)
            self.set_text_color(255, 255, 255)
            self.set_xy(10, 10)
            self.cell(0, 15, 'JOB SEEKER ANALYTICS', 0, 1, 'L')

            # Subtitle
            self.set_font('Arial', 'I', 10)
            self.set_text_color(200, 200, 200)
            self.cell(0, 5, 'Automated Gap Analysis & Learning Roadmap', 0, 1, 'L')
            self.ln(20)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f'Job Seeker Helper | Generated with AI | Page {self.page_no()}', 0, 0, 'C')

        def section_title(self, label):
            self.set_font('Arial', 'B', 14)
            self.set_text_color(33, 33, 33)
            self.set_fill_color(240, 240, 240)
            self.cell(0, 10, f"  {label}", 0, 1, 'L', fill=True)
            self.ln(4)

        def card(self, title, content, link=None):
            self.set_fill_color(250, 250, 250)
            self.set_draw_color(220, 220, 220)
            self.set_font('Arial', 'B', 11)
            self.set_text_color(0, 0, 0)

            x = self.get_x()
            y = self.get_y()

            self.rect(x, y, 190, 25, 'FD')

            self.set_xy(x + 5, y + 5)
            self.cell(0, 5, title, 0, 1)

            self.set_font('Arial', '', 10)
            self.set_text_color(80, 80, 80)
            self.set_xy(x + 5, y + 12)
            self.cell(0, 5, content, 0, 1)

            if link:
                self.set_font('Arial', 'U', 9)
                self.set_text_color(0, 102, 204)
                self.set_xy(x + 150, y + 12)
                self.cell(30, 5, "Open Resource ->", 0, 0, link=link)

            self.ln(20)

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    def clean(text):
        """Sanitize text for FPDF (Latin-1)"""
        if not text: return ""
        # Replace common unicode chars
        replacements = {
            "’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
            "…": "...", "✅": "[V]", "❌": "[X]", "⚠️": "[!]", "➕": "[+]",
            "🚀": "", "📂": "", "☁️": "", "🛠️": "", "🎯": ""
        }
        for k, v in replacements.items():
            text = text.replace(k, v)

        # Force encode to latin-1, replacing unknown with ?
        return text.encode('latin-1', 'replace').decode('latin-1')

    # 1. EXECUTIVE SCORECARD
    pct = res["match_percentage"]

    # Logic for colors
    if pct >= 80:
        bg_r, bg_g, bg_b = 209, 231, 221 # Green-ish
        txt_color = "Excellent Match"
    elif pct >= 60:
        bg_r, bg_g, bg_b = 255, 243, 205 # Yellow-ish
        txt_color = "Good Potential"
    else:
        bg_r, bg_g, bg_b = 248, 215, 218 # Red-ish
        txt_color = "High Gap"

    pdf.set_fill_color(bg_r, bg_g, bg_b)
    pdf.rect(10, 50, 190, 30, 'F')

    pdf.set_y(55)
    pdf.set_x(15)
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(40, 10, f"{pct:.0f}%", 0, 0)

    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, f"Match Score: {txt_color}", 0, 1)

    pdf.set_y(65)
    pdf.set_x(15)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, "Based on comprehensive analysis of Hard Skills, Soft Skills, and Portfolio triggers.", 0, 1)

    pdf.ln(20)

    # 2. SKILL MATRIX
    pdf.section_title("SKILL BREAKDOWN")

    # Matched
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(0, 100, 0) # Dark Green
    pdf.cell(95, 10, clean("MATCHED SKILLS"), 0, 0)

    # Missing
    pdf.set_text_color(150, 0, 0) # Dark Red
    pdf.cell(95, 10, clean("MISSING SKILLS"), 0, 1)

    # Reset text
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(50, 50, 50)

    matched_str = "\n".join([f"- {clean(s)}" for s in res["matching_hard"]])
    missing_str = "\n".join([f"- {clean(s)}" for s in res["missing_hard"]])

    y_start = pdf.get_y()
    pdf.multi_cell(95, 6, matched_str if matched_str else "None", border=1)
    y_end1 = pdf.get_y()

    pdf.set_xy(105, y_start)
    pdf.multi_cell(95, 6, missing_str if missing_str else "None", border=1)
    y_end2 = pdf.get_y()

    pdf.set_y(max(y_end1, y_end2) + 10)

    # Transferable
    if res.get("transferable"):
        pdf.set_font('Arial', 'B', 11)
        pdf.set_text_color(204, 153, 0) # Dark Yellow/Orange
        pdf.cell(0, 10, clean("TRANSFERABLE SKILLS (Equivalents Found)"), 0, 1)

        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(50, 50, 50)
        for missing, present in res["transferable"].items():
             pdf.cell(0, 7, clean(f"• Required: {missing}  ->  You have: {present}"), 0, 1)
        pdf.ln(10)

    # 3. LEARNING ROADMAP
    if res["missing_hard"]:
        pdf.add_page()
        pdf.section_title("LEARNING ROADMAP")
        pdf.ln(5)

        for skill in res["missing_hard"]:
            r = constants.LEARNING_RESOURCES.get(skill, None)

            content = "Use general search engines to find tutorials."
            link_url = f"https://www.google.com/search?q=learn+{urllib.parse.quote(skill)}"

            if r:
                course_str = ", ".join(r['courses'][:1]) # Take first course
                content = f"Recommended: {course_str}. Project Layout: {r['project']}"
                # We assume a generic search link if no direct URL in DB (DB currently has strings titles)

            pdf.card(clean(f"Skill Gap: {skill}"), clean(content), link=link_url)

    # Output with correct encoding handling
    return pdf.output(dest='S').encode('latin-1', 'ignore')

def detect_language(text: str) -> str:
    """
    Simple heuristic to detect non-explicit native language.
    """
    text = text.lower()
    it_markers = {" il ", " lo ", " la ", " i ", " gli ", " le ", " di ", " è ", " e ", " per ", " delle ", " nella "}
    en_markers = {" the ", " a ", " an ", " and ", " is ", " of ", " for ", " to ", " in ", " with ", " that ", " this "}

    it_score = sum(1 for w in it_markers if w in text)
    en_score = sum(1 for w in en_markers if w in text)

    if it_score > en_score: return "Italian"
    if en_score > it_score: return "English"
    return None

# =============================================================================
def analyze_gap(cv_text: str, job_text: str) -> Dict:
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text)

    # 0. Native Language Inference
    # If CV is detected as Italian, we assume candidate speaks Italian (Native)
    detected_lang = detect_language(cv_text)
    if detected_lang:
        cv_hard.add(detected_lang)

    matching_hard = cv_hard & job_hard
    initial_missing_hard = job_hard - cv_hard
    extra_hard = cv_hard - job_hard

    # Stats
    skill_clusters = getattr(constants, "SKILL_CLUSTERS", {})
    project_skills = getattr(constants, "PROJECT_BASED_SKILLS", set())

    # Logic 1: Transferable
    transferable = {} 
    remaining_missing = set()
    for missing in initial_missing_hard:
        found_transferable = False
        for cluster_name, members in skill_clusters.items():
            if missing in members:
                user_has = members.intersection(cv_hard)
                if user_has:
                    transferable[missing] = list(user_has)[0] 
                    found_transferable = True
                    break
        if not found_transferable:
            remaining_missing.add(missing)

    # Logic 2: Project-Based
    project_review = set()
    final_strict_missing = set()
    for skill in remaining_missing:
        if skill in project_skills:
            project_review.add(skill)
        else:
            final_strict_missing.add(skill)

    matching_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft

    score_points = len(matching_hard) + (len(transferable) * 0.5) + (len(project_review) * 0.3)
    match_pct = score_points / len(job_hard) * 100 if job_hard else 0

    return {
        "match_percentage": match_pct,
        "matching_hard": matching_hard,
        "missing_hard": final_strict_missing,
        "project_review": project_review, 
        "transferable": transferable,
        "extra_hard": extra_hard,
        "matching_soft": matching_soft,
        "missing_soft": missing_soft
    }

def analyze_gap_with_project(cv_text: str, job_text: str, project_text: str) -> Dict:
    """
    Analyzes CV + Project vs Job Description.
    Returns standard gap analysis plus 'project_verified' skills.
    """
    # 1. Standard CV Analysis
    res = analyze_gap(cv_text, job_text)

    # 2. Project Analysis
    proj_hard, _ = extract_skills_from_text(project_text)

    # 3. Identify Verified Skills (Requested by JD AND found in Projects)
    # These are skills that might be in 'matching_hard' (CV+JD) or 'missing_hard' (JD only)
    # If they are in Projects, we upgrade/verify them.

    job_hard, _ = extract_skills_from_text(job_text) # Re-extract to be sure or pass it if possible, but cheap enough

    project_verified = job_hard.intersection(proj_hard)

    # Update Result
    res["project_verified"] = project_verified

    # Boost Score? Optional. Let's keep it simple: just identifying them for now.
    # We could recalculate match_percentage if we wanted project skills to fill gaps.

    # If a skill was missing in CV but found in Project, move it from missing to matching?
    # Strategy: "Project skills count as skills"

    newly_found_in_project = res["missing_hard"].intersection(proj_hard)
    if newly_found_in_project:
        res["matching_hard"].update(newly_found_in_project)
        res["missing_hard"] = res["missing_hard"] - newly_found_in_project

        # Recalculate Score
        # (Simplified recalc based on previous formula in analyze_gap)
        # score_points = len(matching_hard) + (len(transferable) * 0.5) + (len(project_review) * 0.3)

        score_points = len(res["matching_hard"]) + (len(res["transferable"]) * 0.5) + (len(res["project_review"]) * 0.3)
        res["match_percentage"] = score_points / len(job_hard) * 100 if job_hard else 0

    return res

# =============================================================================
# REPORT GENERATION (Text & PDF)
# =============================================================================
def generate_detailed_report_text(res: Dict, jd_text: str = "") -> str:
    """Generates a detailed text/markdown report."""
    match_pct = res['match_percentage']
    
    # 1. Executive Summary
    report = []
    report.append("==================================================")
    report.append("              JOB SEEKER ANALYSIS REPORT          ")
    report.append("==================================================")
    report.append(f"Match Score: {match_pct:.1f}%")
    if match_pct >= 80: assessment = "EXCELLENT MATCH - High probability of success."
    elif match_pct >= 60: assessment = "GOOD POTENTIAL - Some gaps, but strong foundation."
    else: assessment = "HIGH GAP - Significant preparation required."
    report.append(f"Assessment: {assessment}")
    report.append("\n")

    # 2. Skill Profile
    report.append("--------------------------------------------------")
    report.append("1. SKILL PROFILE ANALYSIS")
    report.append("--------------------------------------------------")
    report.append("A. DIRECT MATCHES (The Core)")
    if res["matching_hard"]:
        for s in sorted(res["matching_hard"]): report.append(f"   [+] {s}")
    else:
        report.append("   (No direct matches found)")
    
    report.append("\nB. TRANSFERABLE SKILLS (The Bridge)")
    if res.get("transferable"):
        for missing, present in res["transferable"].items():
            report.append(f"   [~] {missing} (covered by {present})")
    else:
        report.append("   (No transferable skills identified)")
        
    report.append("\nC. PORTFOLIO ASSETS (The Boost)")
    if res.get("project_review"):
        for s in res["project_review"]: report.append(f"   [*] {s}")
    else:
        report.append("   (No specific portfolio items detected)")
        
    report.append("\n")

    # 3. Gap Analysis
    report.append("--------------------------------------------------")
    report.append("2. CRITICAL GAP ANALYSIS")
    report.append("--------------------------------------------------")
    if res["missing_hard"]:
        report.append("The following skills are required but missing from your profile:")
        for s in sorted(res["missing_hard"]):
            report.append(f"   [!] {s}")
            # Add simple analysis if known (mock logic for now, could use knowledge graph)
            if s in ["Python", "SQL", "Java"]: report.append(f"       -> Core technical skill. High Priority.")
            if s in ["AWS", "Azure", "GCP"]: report.append(f"       -> Cloud infrastructure. Essential for modern roles.")
    else:
        report.append("No critical gaps detected. You are well aligned!")
    report.append("\n")

    # 4. Strategic Recommendations
    report.append("--------------------------------------------------")
    report.append("3. STRATEGIC RECOMMENDATIONS")
    report.append("--------------------------------------------------")
    if match_pct < 100:
        report.append("* Close the Gap: Focus on the 'Critical Gaps' listed above.")
        report.append("* Leverage Portfolio: Explicitly mention your 'Portfolio Assets' in the interview.")
        if res.get("transferable"):
            report.append("* Explain Transferability: Be ready to explain how your existing skills apply to the missing ones.")
    else:
        report.append("* Prepare for Depth: Since you match well, expect deep technical questions.")
        report.append("* Soft Skills: Focus on demonstrating leadership and communication.")

    report.append("\n")
    report.append("\n")
    
    # 5. Career Compass (Context Aware)
    candidate_skills = res["matching_hard"] | res["missing_hard"] | res["extra_hard"]
    
    try:
        # Pass JD Text to allow filtering of redundant roles
        recs = recommend_roles(candidate_skills, jd_text)
        if recs:
            report.append("--------------------------------------------------")
            report.append("4. AI CAREER COMPASS (Alternative Paths)")
            report.append("--------------------------------------------------")
            report.append("Based on your skill vector, you might also be a good fit for:")
            for i, rec in enumerate(recs):
                 report.append(f"   {i+1}. {rec['role']} ({rec['score']:.0f}% Match)")
                 if rec['missing']:
                     missing_str = ", ".join(rec['missing'][:5])
                     report.append(f"      Missing: {missing_str}...")
            report.append("\n")
    except Exception as e:
        # Fallback if recommend_roles isn't ready or fails
        pass

    report.append("==================================================")
    report.append("Generated by Job Seeker Helper AI")
    report.append("==================================================")

    return "\n".join(report)


def generate_pdf_report(text_content: str) -> bytes:
    """Converts the text report into a PDF bytes object."""
    if not FPDF:
        return None
        
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 15)
            self.cell(0, 10, 'Job Seeker Analysis Report', 0, 1, 'C')
            self.ln(10)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Simple line-by-line write
    for line in text_content.split('\n'):
        # Handle simple bolding logic based on markers
        if "====" in line or "----" in line:
            pdf.ln(2)
            pdf.cell(0, 5, line, 0, 1)
            pdf.ln(2)
        elif line.startswith("Assessment:") or line.startswith("Match Score:"):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, line, 0, 1)
            pdf.set_font("Arial", '', 12)
        elif line.strip().startswith(("1.", "2.", "3.")):
             pdf.set_font("Arial", 'B', 12)
             pdf.cell(0, 10, line, 0, 1)
             pdf.set_font("Arial", '', 12)
        elif line.strip().startswith(("A.", "B.", "C.")):
             pdf.set_font("Arial", 'B', 12)
             pdf.cell(0, 8, line, 0, 1)
             pdf.set_font("Arial", '', 12)
        else:
            # Handle unicode chars roughly (FPDF doesn't love emojis/unicode standard font)
            # Replace common bullets to safe chars
            clean_line = line.replace('✅', '[+]').replace('❌', '[!]').replace('⚠️', '[~]').replace('🚀', '')
            try:
                clean_line = clean_line.encode('latin-1', 'replace').decode('latin-1')
            except:
                clean_line = clean_line # Fallback
            pdf.multi_cell(0, 6, clean_line)
            
    return pdf.output(dest='S').encode('latin-1') # Return bytes


# =============================================================================
# JOB RECOMMENDER (Career Compass) - v1.24
# =============================================================================
def recommend_roles(cv_skills: Set[str], jd_text: str = "") -> List[Tuple[str, float, List[str]]]:
    """
    Identifies the best fitting job roles excluding the one described in the JD.
    """
    if not cv_skills or not constants.JOB_ARCHETYPES or not TfidfVectorizer:
        return []

    # 1. Prepare Corpus
    archetype_names = list(constants.JOB_ARCHETYPES.keys())
    archetype_docs = [" ".join(constants.JOB_ARCHETYPES[name]) for name in archetype_names]
    
    # Docs: [0=CV, 1=JD (if exists), 2..N=Archetypes]
    corpus = [" ".join(cv_skills)]
    
    jd_index = -1
    if jd_text:
        corpus.append(jd_text)
        jd_index = 1
        
    corpus.extend(archetype_docs)
    
    # 2. Vectorization
    vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4), min_df=1)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
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
    similarities = cosine_similarity(cv_vector, arch_vectors_final).flatten()
    
    # 6. Rank and Format
    recommendations = []
    for i, score in enumerate(similarities):
        role_name = archetype_names[i]
        
        # Skip excluded roles (redundant)
        if role_name in excluded_roles:
            continue
            
        role_skills = constants.JOB_ARCHETYPES[role_name]
        cv_norm = {s.lower() for s in cv_skills}
        role_norm = {s.lower() for s in role_skills}
        missing_norm = role_norm - cv_norm
        missing_display = [s for s in role_skills if s.lower() in missing_norm]
        
        # 7. Quality Filter (v1.33 -> v1.34 Junior Friendly)
        # Only show recommendations that have a decent overlap (>30%)
        # 40% was still too high for "Junior -> Senior" pivots. 30% is safer.
        final_score = score * 100
        if final_score < 30:
            continue
            
        recommendations.append({
            "role": role_name,
            "score": final_score, 
            "missing": missing_display
        })
        
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:3]
