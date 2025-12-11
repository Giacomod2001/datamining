import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
except ImportError:
    RandomForestClassifier = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

import constants

# =============================================================================
# LOGIC & INFERENCE
# =============================================================================
def extract_skills_from_text(text: str) -> Tuple[Set[str], Set[str]]:
    """
    Extracts Hard and Soft skills using regex + inference rules.
    Returns: (hard_skills_found, soft_skills_found)
    """
    hard_found = set()
    soft_found = set()
    text_lower = text.lower()
    
    # 1. Direct Regex Match (Hard Skills)
    for skill, variations in constants.HARD_SKILLS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                hard_found.add(skill)
                break
                
    # 2. Direct Regex Match (Soft Skills)
    for skill, variations in constants.SOFT_SKILLS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                soft_found.add(skill)
                break

    # 3. Hierarchical Inference (If Child -> Then Parent)
    # E.g. If "BigQuery" found, Add "Cloud Computing"
    inferred_skills = set()
    for child_skill in hard_found:
        if child_skill in constants.INFERENCE_RULES:
            parents = constants.INFERENCE_RULES[child_skill]
            inferred_skills.update(parents)
            
    hard_found.update(inferred_skills)
    
    return hard_found, soft_found

# =============================================================================
# ML MODEL (Optional enhancement)
# =============================================================================
@st.cache_resource
def train_rf_model():
    # Only training on Hard Skills for now to keep focus technical
    data = []
    for skill_name, keywords in constants.HARD_SKILLS.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})
            data.append({"text": f"used {kw}", "label": skill_name})
            
    # Add Soft Skills too just for completeness in debugger
    for skill_name, keywords in constants.SOFT_SKILLS.items():
        for kw in keywords:
            data.append({"text": kw, "label": skill_name})

    df = pd.DataFrame(data)
    
    if not RandomForestClassifier:
        return None, df
        
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=1000)),
        ('rf', RandomForestClassifier(n_estimators=50, random_state=42))
    ])
    try:
        pipe.fit(df['text'], df['label'])
        return pipe, df
    except:
        return None, df

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
    # Extract
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text)
    
    # Calculate Gaps (Hard Skills Only for Match Score)
    matching_hard = cv_hard & job_hard
    missing_hard = job_hard - cv_hard
    extra_hard = cv_hard - job_hard
    
    # Soft Skills Analysis (Just for info)
    matching_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft
    
    # Score logic
    match_pct = len(matching_hard) / len(job_hard) * 100 if job_hard else 0
    
    return {
        "match_percentage": match_pct,
        "matching_hard": matching_hard,
        "missing_hard": missing_hard,
        "extra_hard": extra_hard,
        "matching_soft": matching_soft,
        "missing_soft": missing_soft
    }
