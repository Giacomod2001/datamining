import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List

# Optional Imports with robust handling
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
except ImportError:
    RandomForestClassifier = None
    TfidfVectorizer = None
    Pipeline = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

import constants

# =============================================================================
# TRAINING (Used for Debugger & Future ML features)
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
# GENERIC FALLBACK (TF-IDF)
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
# SKILL EXTRACTION CORE
# =============================================================================
def extract_skills_from_text(text: str) -> Tuple[Set[str], Set[str]]:
    hard_found = set()
    soft_found = set()
    text_lower = text.lower()
    
    hard_skills = getattr(constants, "HARD_SKILLS", {})
    soft_skills = getattr(constants, "SOFT_SKILLS", {})
    inference_rules = getattr(constants, "INFERENCE_RULES", {})
    
    # 1. Regex Match Hard Skills
    for skill, variations in hard_skills.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                hard_found.add(skill)
                break 
                
    # 2. Regex Match Soft Skills
    for skill, variations in soft_skills.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
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
# PDF EXTRACTION
# =============================================================================
def extract_text_from_pdf(pdf_file) -> str:
    if PdfReader is None: 
        raise ImportError("PyPDF2 missing")
    try:
        reader = PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise Exception(f"PDF Error: {str(e)}")

# =============================================================================
# GAP ANALYSIS
# =============================================================================
def analyze_gap(cv_text: str, job_text: str) -> Dict:
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text)
    
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
