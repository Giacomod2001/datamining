import re
import numpy as np
import pandas as pd
from typing import Set, Dict, List
import streamlit as st

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    TfidfVectorizer = None
    RandomForestClassifier = None
    Pipeline = None
    cosine_similarity = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

import constants

# =============================================================================
# RF MODEL TRAINING (Synthetic Data)
# =============================================================================
@st.cache_resource
def train_rf_model():
    """
    Trains a Random Forest model on synthetic data generated from SKILL_GROUPS.
    Returns: pipeline, training_df
    """
    if not RandomForestClassifier:
        return None, None
    
    # Generate Synthetic Data
    data = []
    
    # 1. Positive Samples (The skills themselves and variations)
    for skill_name, keywords in constants.SKILL_GROUPS.items():
        for kw in keywords:
            # Add exact keyword
            data.append({"text": kw, "label": skill_name})
            # Add context variations
            data.append({"text": f"experience with {kw}", "label": skill_name})
            data.append({"text": f"proficient in {kw}", "label": skill_name})
            data.append({"text": f"using {kw} for development", "label": skill_name})
            
    # 2. Negative/Context Samples (Common words in CVs that aren't skills)
    common_words = ["team player", "hard working", "university", "degree", "responsible for", "managed", "created", "worked on", "years of experience", "project manager"]
    for word in common_words:
        data.append({"text": word, "label": "Other"})
        
    df = pd.DataFrame(data)
    
    # Pipeline: TF-IDF -> Random Forest
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=1000)),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    pipe.fit(df['text'], df['label'])
    
    return pipe, df

# =============================================================================
# RF PREDICTION
# =============================================================================
def predict_skills_rf(text: str, model_pipe) -> Set[str]:
    """
    Detects skills in text using the RF model.
    Applies sliding window or sentence splitting since model is trained on short phrases.
    """
    if not model_pipe:
        return set()
    
    found_skills = set()
    
    # Split text into chunks (e.g., by punctuation or lines) for classification
    # This is a simple heuristic approach
    chunks = re.split(r'[,\.\n•-]', text)
    chunks = [c.strip() for c in chunks if len(c.strip()) > 2]
    
    if not chunks:
        return set()
    
    preds = model_pipe.predict(chunks)
    probs = model_pipe.predict_proba(chunks)
    
    classes = model_pipe.classes_
    
    for i, pred_label in enumerate(preds):
        if pred_label != "Other":
            # Check confidence
            prob = probs[i].max()
            if prob > 0.6: # Confidence threshold
                found_skills.add(pred_label)
                
    return found_skills

# =============================================================================
# LEGACY / HYBRID
# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    if PdfReader is None:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF reading error: {str(e)}")

def extract_keywords(text: str) -> Set[str]:
    found = set()
    text_lower = text.lower()
    for skill, variations in constants.SKILL_GROUPS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                found.add(skill)
                break
    return found

def analyze_gap(cv_text: str, job_text: str) -> Dict:
    # Train/Get Model
    rf_model, _ = train_rf_model()
    
    # 1. Regex Extraction (Baseline)
    cv_base = extract_keywords(cv_text)
    job_base = extract_keywords(job_text)
    
    # 2. RF Prediction (ML Enhancement)
    cv_rf = predict_skills_rf(cv_text, rf_model)
    job_rf = predict_skills_rf(job_text, rf_model)
    
    # Combine
    cv_skills = cv_base | cv_rf
    job_skills = job_base | job_rf
    
    matching = cv_skills & job_skills
    missing = job_skills - cv_skills
    extra = cv_skills - job_skills
    match_pct = len(matching) / len(job_skills) * 100 if job_skills else 0
    
    return {
        "cv_skills": cv_skills,
        "job_skills": job_skills,
        "matching": matching,
        "missing": missing,
        "extra": extra,
        "match_percentage": match_pct
    }
