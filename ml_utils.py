import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
except ImportError:
    RandomForestClassifier = None
    TfidfVectorizer = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

import constants

# =============================================================================
# LOGIC & INFERENCE
# =============================================================================
def extract_generic_keywords(text: str, top_n=5) -> Set[str]:
    """
    Fallback: Extracts top unique keywords using TF-IDF if dictionary match is low.
    Used for unsupported domains (e.g. Zoology, History).
    """
    if not TfidfVectorizer or not text or len(text.split()) < 10:
        return set()
        
    try:
        # We treat the input text as one doc, and compare against a "standard English" background effectively
        # by using stop_words='english'. 
        vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
        vectorizer.fit_transform([text])
        return set(vectorizer.get_feature_names_out())
    except:
        return set()

def extract_skills_from_text(text: str) -> Tuple[Set[str], Set[str]]:
    """
    Extracts Hard and Soft skills. 
    If HARD skill count is very low (<2), attempts Generic Extraction.
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
                # break matching variations for this skill, continue to next skill
                break 
                
    # 2. Direct Regex Match (Soft Skills)
    for skill, variations in constants.SOFT_SKILLS.items():
        for var in variations:
            pattern = r'\b' + re.escape(var.lower()) + r'(?:s|es|ing|ed)?\b'
            if re.search(pattern, text_lower):
                soft_found.add(skill)
                break

    # 3. Hierarchical Inference
    inferred_skills = set()
    for child_skill in hard_found:
        if child_skill in constants.INFERENCE_RULES:
            parents = constants.INFERENCE_RULES[child_skill]
            inferred_skills.update(parents)
    hard_found.update(inferred_skills)
    
    # 4. GENERIC FALLBACK (If domain seems unsupported)
    if len(hard_found) < 2:
        generic_keywords = extract_generic_keywords(text, top_n=5)
        # We add them to hard_found, capitalizing them to look like skills
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
    # Extract
    cv_hard, cv_soft = extract_skills_from_text(cv_text)
    job_hard, job_soft = extract_skills_from_text(job_text)
    
    # Calculate Gaps
    matching_hard = cv_hard & job_hard
    initial_missing_hard = job_hard - cv_hard
    extra_hard = cv_hard - job_hard
    
    # Logic 1: Transferable
    transferable = {} 
    remaining_missing = set()
    for missing in initial_missing_hard:
        found_transferable = False
        for cluster_name, members in constants.SKILL_CLUSTERS.items():
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
        if skill in constants.PROJECT_BASED_SKILLS:
            project_review.add(skill)
        else:
            final_strict_missing.add(skill)
            
    # Soft Skills
    matching_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft
    
    # Score
    score_points = len(matching_hard) + (len(transferable) * 0.5) + (len(project_review) * 0.3)
    match_pct = score_points / len(job_hard) * 100 if job_hard else 0
    
    # Optional: Return a flag if generic fallback was likely used
    is_generic_mode = (len(job_hard) > 0 and len(job_hard.intersection(constants.HARD_SKILLS.keys())) < 2)

    return {
        "match_percentage": match_pct,
        "matching_hard": matching_hard,
        "missing_hard": final_strict_missing,
        "project_review": project_review, 
        "transferable": transferable,
        "extra_hard": extra_hard,
        "matching_soft": matching_soft,
        "missing_soft": missing_soft,
        "is_generic_mode": is_generic_mode
    }
