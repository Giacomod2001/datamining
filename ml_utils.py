import re
import pandas as pd
import streamlit as st
from typing import Set, Dict, Tuple, List
import urllib.parse

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

try:
    from fpdf import FPDF
except ImportError:
    FPDF = None

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
# =============================================================================
# OPTIONAL IMPORTS
# =============================================================================
try:
    from thefuzz import fuzz
except ImportError:
    fuzz = None

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
# REPORT UTILS
# =============================================================================
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
# GAP ANALYSIS
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
