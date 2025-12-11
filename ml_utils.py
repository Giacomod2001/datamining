import re
import numpy as np
from typing import Set, Dict, List
import streamlit as st

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

import constants

# =============================================================================
# TEXT EXTRACTION
# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from uploaded PDF."""
    if PdfReader is None:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF reading error: {str(e)}")

def extract_keywords(text: str) -> Set[str]:
    """Extract skills using regex pattern matching."""
    found = set()
    text_lower = text.lower()
    
    for skill, variations in constants.SKILL_GROUPS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                found.add(skill)
                break
    
    return found

# =============================================================================
# ML SKILL MATCHER
# =============================================================================
@st.cache_data
def ml_skill_matcher(cv_text: str, return_debug: bool = False):
    """ML-based skill detection using TF-IDF + Cosine Similarity."""
    if not TfidfVectorizer or not cosine_similarity:
        return (set(), {}) if return_debug else set()
    
    detected = set()
    debug = {"scores": {}, "features": [], "thresholds": {}, "boosted": {}}
    cv_lower = cv_text.lower()
    
    # Co-occurrence boosting
    cooccurrence = {
        "google cloud": ["GCP", "Cloud Computing", "BigQuery"],
        "gcp": ["GCP", "Cloud Computing"],
        "vision api": ["Computer Vision", "GCP"],
        "bigquery": ["SQL", "GCP", "Data Science"],
        "churn": ["Data Science", "Machine Learning", "Python"],
        "tensorflow": ["Machine Learning", "Deep Learning", "Python"],
        "pytorch": ["Machine Learning", "Deep Learning", "Python"],
        "opencv": ["Computer Vision", "Python"],
        "sagemaker": ["AWS", "Machine Learning"],
        "lambda": ["AWS", "Cloud Computing"],
    }
    
    # Build skill descriptions
    skill_desc = {}
    for skill, keywords in constants.SKILL_GROUPS.items():
        desc = " ".join(keywords).lower()
        # Add context
        if skill == "Computer Vision":
            desc += " image processing opencv yolo cnn detection recognition gcp aws vision api"
        elif skill == "Data Science":
            desc += " churn analytics prediction pandas sklearn bigquery gcp aws sagemaker"
        elif skill == "Machine Learning":
            desc += " tensorflow pytorch sklearn xgboost training prediction model"
        elif skill in ["GCP", "Cloud Computing"]:
            desc += " google cloud bigquery vertex ai cloud functions compute engine"
        elif skill == "AWS":
            desc += " ec2 s3 lambda sagemaker rds dynamodb cloudfront"
        skill_desc[skill] = desc
    
    # Calculate boosts
    boost = {}
    for trigger, skills in cooccurrence.items():
        if trigger in cv_lower:
            for s in skills:
                boost[s] = boost.get(s, 0) + 0.05
    
    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=150, stop_words='english', ngram_range=(1, 2))
    
    try:
        texts = list(skill_desc.values()) + [cv_lower]
        matrix = vectorizer.fit_transform(texts)
        cv_vec = matrix[-1]
        skill_vecs = matrix[:-1]
        sims = cosine_similarity(cv_vec, skill_vecs)[0]
        
        if return_debug:
            features = vectorizer.get_feature_names_out()
            arr = cv_vec.toarray()[0]
            top_idx = arr.argsort()[-15:][::-1]
            debug["features"] = [(features[i], arr[i]) for i in top_idx if arr[i] > 0]
        
        for idx, skill in enumerate(skill_desc.keys()):
            score = sims[idx] + boost.get(skill, 0)
            
            # Dynamic thresholds
            if skill in ["Computer Vision", "Data Science", "Machine Learning", "Deep Learning", "NLP"]:
                thresh = 0.05
            elif skill in ["Python", "SQL", "AWS", "GCP", "Cloud Computing"]:
                thresh = 0.07
            else:
                thresh = 0.12
            
            if return_debug:
                debug["scores"][skill] = score
                debug["thresholds"][skill] = thresh
                if skill in boost:
                    debug["boosted"][skill] = boost[skill]
            
            if score > thresh:
                detected.add(skill)
                
    except Exception as e:
        if return_debug:
            debug["error"] = str(e)
    
    return (detected, debug) if return_debug else detected

def analyze_gap(cv_text: str, job_text: str) -> Dict:
    """Analyze skill gap between CV and job requirements."""
    # Extract skills
    cv_regex = extract_keywords(cv_text)
    cv_ml = ml_skill_matcher(cv_text)
    cv_skills = cv_regex | cv_ml
    
    job_regex = extract_keywords(job_text)
    job_ml = ml_skill_matcher(job_text)
    job_skills = job_regex | job_ml
    
    # Calculate gaps
    matching = cv_skills & job_skills
    missing = job_skills - cv_skills
    extra = cv_skills - job_skills
    
    # Match percentage
    match_pct = len(matching) / len(job_skills) * 100 if job_skills else 0
    
    return {
        "cv_skills": cv_skills,
        "job_skills": job_skills,
        "matching": matching,
        "missing": missing,
        "extra": extra,
        "match_percentage": match_pct
    }
