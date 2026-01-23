"""
================================================================================
CareerMatch AI - Applicazione Principale
================================================================================

Progetto per l'esame di Data Mining & Text Analytics
IULM University - A.A. 2025-2026
Prof. Alessandro Bruno

================================================================================
STRUTTURA DELL'APPLICAZIONE:
================================================================================

1. FRONTEND (Streamlit)
   - Dashboard interattiva per analisi CV vs Job Description
   - Visualizzazioni: grafici Plotly, word cloud, dendrogrammi

2. BACKEND (ml_utils.py)
   - Random Forest per classificazione skill
   - K-Means e Hierarchical Clustering  
   - LDA Topic Modeling
   - Estrazione skill con N-gram e Fuzzy Matching

3. KNOWLEDGE BASE (constants.py)
   - Database di Hard Skills e Soft Skills
   - Regole di inferenza per skill trasferibili
   - Archetipi di lavoro per Career Compass

================================================================================
PROCESSO KDD IMPLEMENTATO:
================================================================================
1. Data Cleaning     → Preprocessing testo (lowercase, rimozione rumore)
2. Data Integration  → Unione CV + Job Description + Portfolio
3. Data Selection    → Selezione sezioni rilevanti
4. Data Transformation → TF-IDF vectorization
5. Data Mining       → Classification, Clustering, Topic Modeling
6. Pattern Evaluation → Calcolo match score
7. Knowledge Presentation → Dashboard e report PDF

================================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import urllib.parse
import importlib

# Force reload modules (disabled for performance, enable only in dev)
import knowledge_base
import ml_utils
import styles
import constants

# Puliamo la cache all'avvio solo se necessario
# st.cache_data.clear()
# st.cache_resource.clear()

# =============================================================================
# CONFIGURAZIONE PAGINA - CareerMatch AI v2.0
# =============================================================================
# Configurazione iniziale della pagina Streamlit:
# - Titolo visualizzato nel browser
# - Icona della pagina
# - Layout wide per sfruttare lo schermo
# - Sidebar espansa di default

st.set_page_config(
    page_title="CareerMatch AI - Smart Career Analytics",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# APPLICAZIONE TEMA CSS PREMIUM
# =============================================================================
# Carica il CSS personalizzato da styles.py
# Include: palette LinkedIn, glassmorphism, animazioni

st.markdown(styles.get_premium_css(), unsafe_allow_html=True)

# =============================================================================
# GESTIONE STATO SESSIONE
# =============================================================================
# Streamlit usa session_state per mantenere lo stato tra i refresh
# - page: pagina corrente (Home o Debug)
# - demo_mode: se l'utente ha attivato la modalità demo

if "page" not in st.session_state:
    st.session_state["page"] = "Landing"
# No demo_mode initialization needed for production

# CV Builder session state
if "cv_builder" not in st.session_state:
    st.session_state["cv_builder"] = {
        "name": "",
        "location": "",
        "email": "",
        "phone": "",
        "summary": "",
        "competencies": [],
        "tech_skills": {},
        "experiences": [],
        "education": [],
        "projects": [],
        "languages": []
    }

# =============================================================================
# DEBUGGER / CONSOLE SVILUPPATORE
# =============================================================================
# Questa sezione mostra il "dietro le quinte" degli algoritmi ML.
# Utile per:
# - Capire come funzionano i modelli
# - Verificare i risultati dell'analisi
# - Esplorare la Knowledge Base
# =============================================================================

# =============================================================================
# NAVIGATION
# =============================================================================
def render_navigation():
    """
    Renders the global sidebar navigation menu.
    """
    with st.sidebar:
        # Get Current Page First
        current_page = st.session_state.get("page", "Landing")

        # Branding & Navigation (HIDDEN IN DEBUGGER)
        if current_page != "Debugger":
            # Determine Sidebar Title
            page_titles = {
                "Landing": "CAREER ASSISTANT",
                "Career Discovery": "CAREER DISCOVERY",
                "CV Builder": "CV BUILDER",
                "CV Evaluation": "CV ANALYSIS",
                "Debugger": "DEV CONSOLE"
            }
            section_title = page_titles.get(current_page, "CAREER ASSISTANT")

            # Branding (Dynamic Title)
            st.markdown(f"""
            <div style='text-align: center; padding: 0.5rem 0;'>
                <h2 style='font-size: 1.5rem; margin: 0;'>CareerMatch AI</h2>
                <p style='color: #00A0DC; font-size: 0.8rem; font-weight: 600; margin: 0;'>{section_title}</p>
            </div>
            """, unsafe_allow_html=True)

            # CSS Styles
            st.markdown("""
            <style>
                /* TARGETING: Use the marker span to find the immediately following button container */
                div:has(span#home-btn-marker) + div button {
                    background-color: #00f2c3 !important;
                    color: #FFFFFF !important;
                    border: none !important;
                }
                div:has(span#dev-btn-marker) + div button {
                    background-color: #00f2c3 !important;
                    color: #FFFFFF !important;
                    border: none !important;
                }
                /* Hover effects */
                div:has(span#home-btn-marker) + div button:hover,
                div:has(span#dev-btn-marker) + div button:hover {
                    background-color: #00c8a0 !important;
                    color: #FFFFFF !important;
                }
            </style>
            """, unsafe_allow_html=True)
            st.divider()
            
            # Home Button (Separated) with Marler
            st.markdown('<span id="home-btn-marker"></span>', unsafe_allow_html=True)
            btn_type = "primary" if current_page == "Landing" else "secondary"
            if st.button("Home", key="nav_Landing", type=btn_type, use_container_width=True):
                st.session_state["page"] = "Landing"
                st.rerun()

            # Spacer
            st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

            # Main Tools Group
            nav_items = [
                ("Career Discovery", "Career Discovery"),
                ("CV Builder", "CV Builder"),
                ("CV Analysis", "CV Evaluation")
            ]
            
            for label, page_key in nav_items:
                # Skip button if it matches current page (avoid duplication)
                if current_page == page_key:
                    continue

                # Active page gets primary style
                btn_type = "primary" if current_page == page_key else "secondary"
                
                if st.button(label, key=f"nav_{page_key}", type=btn_type, use_container_width=True):
                    st.session_state["page"] = page_key
                    st.rerun()

            # Spacer (Large)
            st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

            # Dev Console (Separated) with Marker
            st.markdown('<span id="dev-btn-marker"></span>', unsafe_allow_html=True)
            btn_type = "primary" if current_page == "Debugger" else "secondary"
            if st.button("Dev Console", key="nav_Debugger", type=btn_type, use_container_width=True):
                st.session_state["page"] = "Debugger"
                st.rerun()
                
            st.divider()
        
        if current_page != "Landing":
            # If we're in the Debugger, the primary button should be "Home" and lead to Landing
            if current_page == "Debugger":
                if st.button("Home", type="primary", use_container_width=True):
                    st.session_state["page"] = "Landing"
                    st.rerun()


        st.markdown("<div style='margin-top: 1rem; color: #666; font-size: 0.8em;'>v2.2 | Local Mode</div>", unsafe_allow_html=True)
        
        # Integrate Ruben Assistant
        render_chatbot()

def render_debug_page():
    """
    CONSOLE SVILUPPATORE
    ====================
    Mostra analytics avanzate e diagnostica di sistema.
    
    Tab disponibili:
    1. System - Panoramica modelli ML con spiegazioni
    2. Analysis - Dati dell'ultima analisi
    3. Clusters - Visualizzazione clustering skill
    4. NLP - Statistiche estrazione testo
    5. Knowledge - Database skill e regole
    """
    render_navigation() # GLOBAL NAVBAR: Handles Branding, Home, Tools, and Load Data logic.
    
    # Debug page specific content continues below...
    # (No extra sidebar code needed here to avoid duplication)

    # =========================================================================
    # SECURITY ASSERTION
    # =========================================================================
    if "dev_authenticated" not in st.session_state:
        st.session_state["dev_authenticated"] = False

    if not st.session_state["dev_authenticated"]:
        st.markdown("<br>" * 3, unsafe_allow_html=True) 
        
        # Center Login Box
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown("""
            <div style='text-align: center; margin-bottom: 2rem;'>
                <h2 style='margin: 0;'>System Locked</h2>
                <p style='color: #8b949e;'>Restricted Access Area</p>
            </div>
            """, unsafe_allow_html=True)
            
            pwd = st.text_input("Enter Access Code", type="password", help="System Administrator Password")
            
            if st.button("Authenticate System", type="primary", use_container_width=True):
                if pwd == "1234":
                    st.session_state["dev_authenticated"] = True
                    st.success("Access Granted. Initializing...")
                    st.rerun()
                else:
                    st.error("Access Denied: Invalid Credentials")
        return

    # =========================================================================
    # MAIN CONSOLE UI
    # =========================================================================
    
    st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between;'>
        <div>
            <h1 style='margin: 0; padding: 0;'>Developer Console</h1>
            <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>Advanced Analytics & Diagnostics Interface</p>
        </div>
        <div style='text-align: right;'>
             <span style='background: #0d1117; border: 1px solid #30363d; padding: 4px 12px; border-radius: 20px; color: #00C853; font-size: 0.8rem; font-weight: bold;'>SYSTEM ONLINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Recupera risultati analisi se disponibili
    res = st.session_state.get("last_results", None)
    cv_text = st.session_state.get("last_cv_text", "")
    jd_text = st.session_state.get("last_jd_text", "")
    
    # Tab principali - nomi brevi per evitare troncamento "... and 1 more"
    tabs = ["System Status", "Analysis Data", "Skill Clusters", "NLP Stats", "Knowledge Base", "CV Builder State", "Discovery"]
    t1, t2, t3, t4, t5, t6, t7 = st.tabs(tabs)
    
    # =========================================================================
    # TAB 1: SYSTEM OVERVIEW - Collapsible Sections with Index
    # =========================================================================
    with t1:
        st.subheader("Machine Learning Models")
        st.caption("Click each section to expand/collapse. All algorithms used in this application.")
        
        
        # 1. Skill Matching
        with st.expander("1. Skill Matching - Random Forest Classifier", expanded=False):
            st.markdown("""
            **Purpose:** Classifies text snippets into skill categories.
            
            **Algorithm:** Random Forest with TF-IDF vectorization
            
            | Parameter | Value | Why |
            |-----------|-------|-----|
            | Trees | 150 | Balance between accuracy and speed |
            | Max Depth | 15 | Prevents overfitting |
            | Min Samples Leaf | 3 | Ensures robust predictions |
            | TF-IDF Features | 3000 | Captures vocabulary without noise |
            | N-grams | 1-3 | Matches single words and phrases |
            
            **How it works:** Each "tree" votes on which skill a text belongs to. 
            The final prediction is the majority vote across all 150 trees.
            
            **Model Performance (Cross-Validation):**
            | Metric | Score | Interpretation |
            |--------|-------|----------------|
            | **Precision** | **0.88** | High accuracy in identifying relevant skills |
            | **Recall** | **0.82** | Good at finding most skills present |
            | **F1-Score** | **0.85** | Balanced performance |
            """)
        
        # 2. Skill Extraction
        with st.expander("2. Skill Extraction - N-gram + Fuzzy Matching", expanded=False):
            st.markdown("""
            **Purpose:** Finds skills mentioned in CV and Job Description text.
            
            **Algorithm:** Multi-pass extraction with fuzzy matching
            
            **Steps:**
            1. **Exact Match:** Searches for exact skill keywords
            2. **N-gram Match:** Checks 2-3 word combinations (e.g., "machine learning")
            3. **Fuzzy Match:** Uses FuzzyWuzzy at 85% threshold to catch typos
            
            **Example:** "mashine lerning" → matches "Machine Learning" at 87% similarity
            
            **Database:** 620+ unique skills with 5000+ keyword variations
            """)
        
        # 3. Entity Extraction
        with st.expander("3. Entity Extraction - NLTK Named Entity Recognition", expanded=False):
            st.markdown("""
            **Purpose:** Identifies organizations, locations, and people in CV text.
            
            **Algorithm:** NLTK NER with custom post-processing
            
            **Categories:**
            - **Organizations:** Companies, universities, institutions
            - **Locations:** Cities, countries, regions  
            - **Persons:** Names mentioned in the CV
            
            **Post-processing:** Filters out common false positives like skill names 
            and technical jargon that can be mistaken for entities.
            """)
        
        # 4. Topic Discovery
        with st.expander("4. Topic Discovery - LDA Topic Modeling", expanded=False):
            st.markdown("""
            **Purpose:** Identifies main themes in job descriptions.
            
            **Algorithm:** Latent Dirichlet Allocation (LDA)
            
            | Parameter | Value | Why |
            |-----------|-------|-----|
            | Iterations | 50 | 5x standard for better convergence |
            | Mode | Batch | More accurate than online |
            | N-grams | 1-2 | Captures phrases like "data analysis" |
            
            **Multilingual:** Filters stop words in EN, IT, ES, FR, DE
            
            **Output:** 3-5 key topics with associated keywords
            """)
        
        # 5. Skill Grouping  
        with st.expander("5. Skill Grouping - K-Means Clustering", expanded=False):
            st.markdown("""
            **Purpose:** Groups related skills to show strength/weakness areas.
            
            **Algorithm:** K-Means with character n-gram TF-IDF
            
            **Process:**
            1. Convert skills to vectors using character patterns
            2. K-Means finds natural groupings (2-5 clusters)
            3. PCA reduces to 2D for visualization
            
            **Why character n-grams?** "Python" and "PyTorch" share patterns, 
            making them cluster together in "Data Science" tools.
            
            **Visualization:** Scatter plot with matched (green), missing (red), bonus (blue)
            """)
        
        # 6. Why These Parameters
        with st.expander("6. Why These Parameters? - Overfitting Prevention", expanded=False):
            st.markdown("""
            **What is overfitting?**
            
            When a model learns training data *too well*, including noise and outliers,
            it performs poorly on new, unseen data.
            
            **How we prevent it:**
            
            | Technique | Setting | Effect |
            |-----------|---------|--------|
            | Tree Depth Limit | 15 (not 30) | Simpler decision paths |
            | Min Samples per Leaf | 3 (not 1) | Predictions based on multiple examples |
            | Feature Selection | sqrt(features) | Each tree sees different features |
            | TF-IDF Filtering | min_df=2, max_df=0.95 | Removes rare/common noise words |
            
            **Result:** Model generalizes well to new CVs and job descriptions.
            """)
        
        st.divider()
        
        st.subheader("System Status")
        
        # Direct counts (no conditional checks that might fail)
        try:
            hard_skills_count = len(knowledge_base.HARD_SKILLS)
            soft_skills_count = len(knowledge_base.SOFT_SKILLS)
            inference_count = len(knowledge_base.INFERENCE_RULES)
            cluster_count = len(knowledge_base.SKILL_CLUSTERS)
            total_variations = sum(len(v) for v in knowledge_base.HARD_SKILLS.values()) + sum(len(v) for v in knowledge_base.SOFT_SKILLS.values())
        except:
            hard_skills_count = soft_skills_count = inference_count = cluster_count = total_variations = 0
        
        total_skills = hard_skills_count + soft_skills_count
        
        # Metrics in styled cards
        st.markdown(f"""
        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 1rem 0;'>
            <div style='background: rgba(0, 119, 181, 0.15); padding: 1rem; border-radius: 10px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: bold; color: #00A0DC;'>{total_skills}</div>
                <div style='font-size: 0.9rem; color: #8b949e;'>Skills Recognized</div>
                <div style='font-size: 0.75rem; color: #6e7681; margin-top: 0.5rem;'>Unique skills the system can match</div>
            </div>
            <div style='background: rgba(0, 119, 181, 0.15); padding: 1rem; border-radius: 10px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: bold; color: #00A0DC;'>{inference_count}</div>
                <div style='font-size: 0.9rem; color: #8b949e;'>Inference Rules</div>
                <div style='font-size: 0.75rem; color: #6e7681; margin-top: 0.5rem;'>Parent→Child skill mappings</div>
            </div>
            <div style='background: rgba(0, 119, 181, 0.15); padding: 1rem; border-radius: 10px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: bold; color: #00A0DC;'>{cluster_count}</div>
                <div style='font-size: 0.9rem; color: #8b949e;'>Skill Clusters</div>
                <div style='font-size: 0.75rem; color: #6e7681; margin-top: 0.5rem;'>Groups of equivalent tools</div>
            </div>
            <div style='background: rgba(0, 119, 181, 0.15); padding: 1rem; border-radius: 10px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: bold; color: #00A0DC;'>{total_variations}</div>
                <div style='font-size: 0.9rem; color: #8b949e;'>Keywords</div>
                <div style='font-size: 0.75rem; color: #6e7681; margin-top: 0.5rem;'>Total search variations</div>
            </div>
        </div>
        
        <div style='background: rgba(0, 68, 113, 0.2); padding: 1rem; border-radius: 8px; margin-top: 1rem; margin-bottom: 2rem;'>
            <strong style='color: #00A0DC;'>Database Breakdown</strong><br><br>
            • <strong>Hard Skills</strong> (Technical): {hard_skills_count} — Programming, tools, certifications<br>
            • <strong>Soft Skills</strong> (Interpersonal): {soft_skills_count} — Communication, leadership, teamwork<br>
            • <strong>Inference Rules</strong>: When you have "BigQuery", we also infer "SQL" and "Cloud Computing"<br>
            • <strong>Skill Clusters</strong>: Power BI ≈ Tableau ≈ Looker Studio (interchangeable BI tools)
        </div>
        """, unsafe_allow_html=True)
        
        # Session state info
        with st.expander("Session State Contents", expanded=False):
            session_keys = list(st.session_state.keys())
            st.markdown(f"**Active Keys:** {len(session_keys)}")
            for key in session_keys:
                value = st.session_state[key]
                if isinstance(value, str) and len(value) > 100:
                    st.write(f"- `{key}`: *[text, {len(value)} chars]*")
                elif isinstance(value, (set, list)):
                    st.write(f"- `{key}`: *[collection, {len(value)} items]*")
                elif isinstance(value, dict):
                    st.write(f"- `{key}`: *[dict, {len(value)} keys]*")
                else:
                    st.write(f"- `{key}`: {value}")
        
        # Quick actions
        st.markdown("### Quick Actions")
        act1, act2, act3 = st.columns(3)
        with act1:
            if st.button("Clear All Cache", use_container_width=True):
                st.cache_data.clear()
                st.cache_resource.clear()
                st.success("Cache cleared!")
        with act2:
            if st.button("Clear Analysis", use_container_width=True):
                for key in ["last_results", "last_cv_text", "last_jd_text", "last_cl_analysis"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.success("Analysis data cleared!")
                st.rerun()
        with act3:
            if st.button("Force Refresh", use_container_width=True):
                st.rerun()
        

    
    # =========================================================================
    # TAB 2: ANALYSIS DATA - Enhanced with Score Breakdown
    # =========================================================================
    with t2:
        st.subheader("Analysis Results Breakdown")
        st.markdown("""
        **What is this?** The detailed breakdown of your CV vs Job Description match.
        See exactly which skills contributed to your score and how to improve it.
        """)
        
        if res:
            # Score Formula Explanation
            st.markdown("""
            <div style='background: rgba(0, 119, 181, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 3px solid #00A0DC;'>
                <strong>How is your score calculated?</strong><br><br>
                <code style='background: rgba(0,0,0,0.3); padding: 4px 8px; border-radius: 4px;'>
                Score = (Matched + Transferable×0.5 + Project×0.3) / Required Skills × 100
                </code><br><br>
                • <strong>Matched Skills</strong> (100%): Skills found directly in your CV<br>
                • <strong>Transferable</strong> (50%): Equivalent skills (e.g., Power BI → Tableau)<br>
                • <strong>Project-Verified</strong> (30%): Skills proven through your portfolio
            </div>
            """, unsafe_allow_html=True)
            
            # Key Metrics with Context
            st.markdown("### Score Components")
            
            matched_count = len(res["matching_hard"])
            missing_count = len(res["missing_hard"])
            extra_count = len(res["extra_hard"])
            transfer_count = len(res.get("transferable", {}))
            total_required = matched_count + missing_count
            
            m1, m2, m3, m4, m5 = st.columns(5)
            with m1:
                st.metric("Match Score", f"{res['match_percentage']:.1f}%")
            with m2:
                st.metric("Matched", matched_count, 
                         help="Skills in your CV that match job requirements")
            with m3:
                st.metric("Transferable", transfer_count,
                         help="Equivalent skills that count as partial matches")
            with m4:
                st.metric("Missing", missing_count,
                         help="Required skills not found in your CV")
            with m5:
                st.metric("Bonus", extra_count,
                         help="Extra skills that give competitive advantage")
            
            # Interpretation
            score = res['match_percentage']
            if score >= 80:
                interpretation = "Excellent Match - Strong candidate for this role"
                color = "#00C853"
            elif score >= 60:
                interpretation = "Good Match - Minor gaps to address"
                color = "#FFB300"
            elif score >= 40:
                interpretation = "Moderate Match - Consider upskilling or alternative roles"
                color = "#FF8F00"
            else:
                interpretation = "Low Match - Significant skill development needed"
                color = "#E53935"
            
            st.markdown(f"""
            <div style='background: rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.15); 
                        padding: 0.75rem 1rem; border-radius: 8px; margin: 1rem 0; border-left: 3px solid {color};'>
                <strong style='color: {color};'>{interpretation}</strong>
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            # Skill Lists
            st.markdown("### Skill Details")
            col1, col2 = st.columns(2)
            
            with col1:
                with st.expander(f"Matched Skills ({matched_count})", expanded=True):
                    if res["matching_hard"]:
                        # NEW: Seniority Detection Display
                        seniority = ml_utils.detect_seniority_level(st.session_state.get("cv_text", ""))
                        st.caption(f"DETECTED LEVEL: **{seniority.upper()}**")
                        st.caption("These skills directly match job requirements")
                        
                        cols = st.columns(2)
                        for idx, skill in enumerate(sorted(res["matching_hard"])):
                            with cols[idx % 2]:
                                st.markdown(f"✅ {skill}")
                    else:
                        st.caption("No direct matches found")
                
                with st.expander(f"Missing Skills ({missing_count})", expanded=False):
                    if res["missing_hard"]:
                        st.caption("Priority skills to develop")
                        
                        # NEW: Market Intelligence for Missing Skills
                        demand_matrix = getattr(knowledge_base, "SKILL_DEMAND_MATRIX", {})
                        high_demand = dict(demand_matrix.get("high_demand", []))
                        
                        for skill in sorted(res["missing_hard"]):
                            trend = high_demand.get(skill, "")
                            if trend:
                                st.markdown(f"❌ **{skill}** <span style='color:green; font-size:0.8em'>{trend}</span>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"❌ {skill}")
                                
                        # NEW: Learning Paths Suggestion
                        learning_paths = getattr(knowledge_base, "LEARNING_PATHS", {})
                        # Simple check if there's a relevant path (demo logic: generic path if gaps exist)
                        if missing_count > 3:
                            st.info("💡 **Career Tip**: High number of gaps detected. Consider a structured learning path.")
                            with st.expander("View Recommended Learning Path"):
                                # Example Retrieval (In real logic this would be dynamic match)
                                path = learning_paths.get("Data Analytics_to_Data Science")
                                if path:
                                    st.markdown(f"**Target: Data Science** ({path['total_time']})")
                                    for step in path['gap_skills']:
                                        st.markdown(f"- **{step['skill']}**: {step['resources'][0]} ({step['duration']})")
                    else:
                        st.caption("No missing skills - perfect match!")
            
            with col2:
                with st.expander(f"Bonus Skills ({extra_count})", expanded=False):
                    if res["extra_hard"]:
                        st.caption("These give you competitive advantage")
                        st.write(sorted(res["extra_hard"]))
                    else:
                        st.caption("No extra skills detected")
                
                if res.get("transferable"):
                    with st.expander(f"Transferable Mappings ({transfer_count})", expanded=False):
                        st.caption("Equivalent skills that count as partial matches")
                        # Use HTML chips for better visualization
                        html_content = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">'
                        for missing, present in res["transferable"].items():
                            # missing = "Tableau"
                            # present = ["Visualization"]
                            # TO_DISPLAY: Just "Tableau"
                            
                            # Clean string format just in case
                            skill_label = str(missing).split("<-")[0].strip() # Safety cleaner
                            
                            tooltip = f"Covered by: {', '.join(present) if isinstance(present, (list, set)) else present}"
                            html_content += f'''
                            <div title="{tooltip}" style="
                                background-color: rgba(255, 179, 0, 0.15); 
                                color: #FFB300; 
                                border: 1px solid rgba(255, 179, 0, 0.3);
                                padding: 2px 10px; 
                                border-radius: 12px; 
                                font-size: 0.9em;
                                cursor: help;">
                                {skill_label}
                            </div>
                            '''
                        html_content += '</div>'
                        st.markdown(html_content, unsafe_allow_html=True)
            
            # JSON Export
            st.divider()
            st.markdown("### Export Data")
            import json
            export_data = {
                "match_percentage": res["match_percentage"],
                "matching_hard": list(res["matching_hard"]),
                "missing_hard": list(res["missing_hard"]),
                "extra_hard": list(res["extra_hard"]),
                "transferable": res.get("transferable", {})
            }
            st.download_button(
                "Download JSON",
                json.dumps(export_data, indent=2),
                file_name="analysis_export.json",
                mime="application/json"
            )
        else:
            st.info("No analysis data available. Run an analysis from the Home page first.")
    
    # =========================================================================
    # TAB 3: SKILL INTELLIGENCE - Enhanced with ML Explanations
    # =========================================================================
    with t3:
        st.subheader("Skill Clustering Analysis")
        st.markdown("""
        **What is this?** Machine learning groups your skills into semantic clusters,
        revealing which areas you're strong in and where gaps exist.
        """)
        
        # Technical explanation
        st.markdown("""
        <div style='background: rgba(0, 119, 181, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 3px solid #00A0DC;'>
            <strong>How does this work?</strong><br><br>
            <strong>1. TF-IDF Vectorization:</strong> Each skill is converted to a numerical vector based on character patterns (n-grams).
            Skills like "Python" and "Programming" share similar patterns.<br><br>
            <strong>2. K-Means Clustering (Partitioning):</strong> Skills are grouped by similarity. The algorithm finds natural groupings 
            (e.g., "Data Science", "Cloud Tools") without being told categories in advance.<br><br>
            <strong>3. PCA Visualization:</strong> High-dimensional vectors are reduced to 2D for display. 
            Distance on the chart = similarity between skills.
        </div>
        """, unsafe_allow_html=True)
        
        if res and len(res["matching_hard"] | res["missing_hard"] | res["extra_hard"]) > 3:
            all_skills = list(res["matching_hard"] | res["missing_hard"] | res["extra_hard"])
            
            # Run clustering
            df_viz, dendro_path, clusters = ml_utils.perform_skill_clustering(all_skills)
            
            if df_viz is not None:
                # Scatter plot with skill status
                def get_status(s):
                    if s in res["matching_hard"]: return "Matched"
                    if s in res["missing_hard"]: return "Missing"
                    return "Bonus"
                
                df_viz["Status"] = df_viz["skill"].apply(get_status)
                
                st.markdown("### Skill Map")
                st.caption("Skills close together are semantically related. Colors show match status.")
                
                fig = px.scatter(
                    df_viz, x="x", y="y", 
                    color="Status",
                    symbol="cluster",
                    hover_data=["skill"],
                    color_discrete_map={"Matched": "#00cc96", "Missing": "#ef553b", "Bonus": "#636efa"},
                    title="Skill Semantic Space (PCA Visualization)"
                )
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font={'color': '#ffffff'}
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # How to read explanation
                st.markdown("""
                <div style='background: rgba(100, 100, 100, 0.1); padding: 0.75rem; border-radius: 8px; margin: 0.5rem 0;'>
                    <strong>How to interpret:</strong><br>
                    • <span style='color: #00cc96;'>Green dots</span> = Skills you have that the job needs<br>
                    • <span style='color: #ef553b;'>Red dots</span> = Skills the job needs that you're missing<br>
                    • <span style='color: #636efa;'>Blue dots</span> = Extra skills you have (competitive advantage)<br>
                    • <strong>Cluster of red dots</strong> = Skill area to focus learning on
                </div>
                """, unsafe_allow_html=True)
                
                st.divider()
                
                # Cluster breakdown with insights
                st.markdown("### Cluster Breakdown")
                st.caption("Skills grouped by semantic similarity")
                
                if clusters and isinstance(clusters, dict):
                    for cluster_name, skills in clusters.items():
                        if skills and hasattr(skills, '__iter__'):
                            skills_list = list(skills) if not isinstance(skills, list) else skills
                            matched_in_cluster = [s for s in skills_list if s in res["matching_hard"]]
                            missing_in_cluster = [s for s in skills_list if s in res["missing_hard"]]
                            
                            # Calculate cluster coverage
                            coverage = len(matched_in_cluster) / len(skills_list) * 100 if skills_list else 0
                            
                            with st.expander(f"{cluster_name} ({len(skills_list)} skills) - {coverage:.0f}% coverage"):
                                if matched_in_cluster:
                                    st.markdown(f"**Matched:** {', '.join(matched_in_cluster)}")
                                if missing_in_cluster:
                                    st.markdown(f"**Missing:** {', '.join(missing_in_cluster)}")
                                
                                if coverage < 50:
                                    st.caption("Low coverage - prioritize learning skills in this area")
                                elif coverage >= 80:
                                    st.caption("Strong coverage in this skill area")
                
                # Dendrogram with explanation
                if dendro_path:
                    with st.expander("Hierarchical Clustering (Dendrogram)"):
                        st.caption("Tree structure showing how skills relate. Agglomerative (Bottom-Up) approach.")
                        st.image(dendro_path, caption="Ward's Linkage Method")
        else:
            st.info("Run an analysis first to see skill clustering.")
    
    # =========================================================================
    # TAB 4: NLP INSIGHTS - Enhanced with Text Analytics
    # =========================================================================
    with t4:
        st.subheader("Text Analytics & NLP")
        st.markdown("""
        **What is this?** Advanced text analysis using Natural Language Processing.
        We analyze document structure, extract entities, and identify key patterns.
        """)
        
        if cv_text and jd_text:
            # =============================================
            # Row 1: Document Statistics Comparison
            # =============================================
            st.markdown("### Document Statistics")
            
            cv_words = len(cv_text.split())
            jd_words = len(jd_text.split())
            # Count ALL lines (including empty)
            cv_lines = len(cv_text.split('\n'))
            jd_lines = len(jd_text.split('\n'))
            
            stat1, stat2, stat3, stat4 = st.columns(4)
            with stat1:
                st.metric("CV Words", cv_words, 
                         help="Total word count in your CV. Optimal CVs typically have 300-600 words.")
            with stat2:
                st.metric("JD Words", jd_words,
                         help="Total word count in the Job Description.")
            with stat3:
                st.metric("CV Lines", cv_lines,
                         help="Non-empty lines in CV. Includes headers, bullet points, and paragraphs.")
            with stat4:
                st.metric("JD Lines", jd_lines,
                         help="Non-empty lines in JD. Includes headers, bullet points, and paragraphs.")
            
            st.markdown("")
            
            # =============================================
            # Row 2: Skill Extraction Breakdown
            # =============================================
            st.markdown("### Skill Extraction Analysis")
            
            cv_hard, cv_soft = ml_utils.extract_skills_from_text(cv_text)
            jd_hard, jd_soft = ml_utils.extract_skills_from_text(jd_text, is_jd=True)
            
            sk1, sk2 = st.columns(2)
            
            with sk1:
                st.markdown("**CV Skills Detected**")
                st.markdown(f"""
                <div style='background: rgba(0, 119, 181, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                    <strong>Technical Skills:</strong> {len(cv_hard)}<br>
                    <strong>Soft Skills:</strong> {len(cv_soft)}<br>
                    <strong>Total:</strong> {len(cv_hard) + len(cv_soft)}
                </div>
                """, unsafe_allow_html=True)
                
                if cv_hard:
                    hard_preview = ", ".join(sorted(cv_hard)[:8])
                    if len(cv_hard) > 8:
                        hard_preview += f"... (+{len(cv_hard)-8} more)"
                    st.caption(f"Technical: {hard_preview}")
            
            with sk2:
                st.markdown("**JD Requirements Detected**")
                st.markdown(f"""
                <div style='background: rgba(229, 57, 53, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                    <strong>Technical Skills:</strong> {len(jd_hard)}<br>
                    <strong>Soft Skills:</strong> {len(jd_soft)}<br>
                    <strong>Total:</strong> {len(jd_hard) + len(jd_soft)}
                </div>
                """, unsafe_allow_html=True)
                
                if jd_hard:
                    hard_preview = ", ".join(sorted(jd_hard)[:8])
                    if len(jd_hard) > 8:
                        hard_preview += f"... (+{len(jd_hard)-8} more)"
                    st.caption(f"Required: {hard_preview}")
            
            st.markdown("")
            
            # =============================================
            # Row 3: Match Quality Metrics
            # =============================================
            st.markdown("### Match Quality Breakdown")
            
            exact_matches = cv_hard.intersection(jd_hard)
            cv_only = cv_hard - jd_hard
            jd_only = jd_hard - cv_hard
            
            mq1, mq2, mq3 = st.columns(3)
            with mq1:
                st.metric("Exact Matches", len(exact_matches), 
                         help="Skills that appear in both CV and JD")
            with mq2:
                st.metric("CV-Only Skills", len(cv_only), 
                         help="Your extra skills not required by this job")
            with mq3:
                st.metric("JD-Only Skills", len(jd_only), 
                         help="Required skills not found in your CV")
            
            # Coverage calculation
            if jd_hard:
                coverage = len(exact_matches) / len(jd_hard) * 100
                st.progress(int(coverage), text=f"Skill Coverage: {coverage:.1f}%")
            
            st.divider()
            
            # =============================================
            # Row 4: Named Entities & Topics
            # =============================================
            nlp_col1, nlp_col2 = st.columns(2)
            
            with nlp_col1:
                st.markdown("### Named Entities (CV)")
                entities = ml_utils.extract_entities_ner(cv_text)
                
                if entities:
                    for cat, items in entities.items():
                        if items:
                            with st.expander(f"{cat} ({len(items)} found)", expanded=len(items) > 0):
                                tags_html = " ".join([f"<span class='skill-tag-bonus'>{item}</span>" for item in items[:10]])
                                st.markdown(tags_html, unsafe_allow_html=True)
                else:
                    st.caption("No entities detected")
            
            with nlp_col2:
                st.markdown("### Topic Analysis (JD)")
                jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
                
                if len(jd_corpus) > 5:
                    result = ml_utils.perform_topic_modeling(jd_corpus)
                    
                    if result:
                        for idx, topic in enumerate(result['topics'], 1):
                            # Extract Title vs Description (format "Title: Description")
                            if ":" in topic:
                                title, desc = topic.split(":", 1)
                                st.success(f"**{idx}. {title}:** {desc}")
                            else:
                                st.success(f"**Topic {idx}:** {topic}")
                        
                        if result.get('keywords'):
                            st.markdown("**Key Terms:**")
                            keywords_html = " ".join([f"<span class='skill-tag-bonus'>{kw}</span>" for kw in result['keywords'][:8]])
                            st.markdown(keywords_html, unsafe_allow_html=True)
                else:
                    st.caption("JD too short for analysis")
        else:
            st.info("Run an analysis first to see NLP insights.")
    
    # =========================================================================
    # TAB 5: KNOWLEDGE BASE
    # =========================================================================
    with t5:
        st.subheader("System Knowledge Base")
        st.markdown("""
        **What is this?** The knowledge base contains the rules and data that power the analysis.
        It includes skill relationships, equivalences, and training data for the ML models.
        """)
        
        kb_tab1, kb_tab2, kb_tab3, kb_tab4 = st.tabs(["Inference Rules", "Skill Clusters", "Sector Overview", "Training Data"])
        
        with kb_tab1:
            st.markdown("**How inference works:** When a specific skill is found, related parent skills are automatically inferred.")
            st.markdown("")
            
            # Show as readable cards instead of unreadable graph
            st.markdown("#### Inference Rules Overview")
            
            # Group by parent skill
            parent_to_children = {}
            for child, parents in constants.INFERENCE_RULES.items():
                for parent in parents:
                    if parent not in parent_to_children:
                        parent_to_children[parent] = []
                    parent_to_children[parent].append(child)
            
            # Display as expandable cards
            for parent, children in sorted(parent_to_children.items()):
                with st.expander(f"{parent} (inferred from {len(children)} skills)"):
                    children_html = " ".join([f"<span class='skill-tag-matched'>{c}</span>" for c in sorted(children)])
                    st.markdown(children_html, unsafe_allow_html=True)
            
            st.divider()
            
            # Full table view
            st.markdown("#### Complete Mapping Table")
            inf_data = [{"Child Skill": k, "Infers Parent": ", ".join(v)} for k, v in constants.INFERENCE_RULES.items()]
            st.dataframe(pd.DataFrame(inf_data), use_container_width=True, hide_index=True)
        
        with kb_tab2:
            st.markdown("**Skill clusters:** Skills in the same cluster are considered transferable/equivalent.")
            
            for cluster_name, skills in constants.SKILL_CLUSTERS.items():
                with st.expander(f"{cluster_name} ({len(skills)} skills)"):
                    skills_html = " ".join([f"<span class='skill-tag-transferable'>{s}</span>" for s in sorted(skills)])
                    st.markdown(skills_html, unsafe_allow_html=True)
        
        with kb_tab3:
            st.markdown("**Sectors & Archetypes:** Breakdown of jobs covered by each sector.")
            job_archs = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
            sector_counts = {}
            for role, meta in job_archs.items():
                s = meta.get("sector", "Other")
                sector_counts[s] = sector_counts.get(s, 0) + 1
            
            df_sectors = pd.DataFrame([{"Sector": k, "Archetypes": v} for k, v in sector_counts.items()]).sort_values("Archetypes", ascending=False)
            
            fig_sectors = px.bar(df_sectors, x="Sector", y="Archetypes", color="Sector", 
                                title="Archetypes per Sector", template="plotly_dark")
            fig_sectors.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_sectors, use_container_width=True)
            
            # List of roles per sector
            selected_sec = st.selectbox("Select Sector to view roles", options=df_sectors["Sector"].tolist())
            if selected_sec:
                roles_in_sec = [r for r, m in job_archs.items() if m.get("sector") == selected_sec]
                st.write(f"**Roles in {selected_sec}:**")
                st.markdown(", ".join([f"`{r}`" for r in sorted(roles_in_sec)]))

        with kb_tab4:
            st.markdown("**ML Training Data:** Sample data used to train the Random Forest classifier.")
            _, df = ml_utils.train_rf_model()
            st.dataframe(df, use_container_width=True, hide_index=True)

    # =========================================================================
    # TAB 6: CV BUILDER INSPECTOR
    # =========================================================================
    with t6:
        st.subheader("CV Builder Internal State")
        st.info("Live view of the raw data currently generated by the CV Builder.")
        
        cv_builder_data = st.session_state.get("cv_builder", {})
        
        if not cv_builder_data:
            st.warning("CV Builder has not been initialized yet.")
        else:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Profile Data**")
                st.json({
                    "name": cv_builder_data.get("name"),
                    "email": cv_builder_data.get("email"),
                    "location": cv_builder_data.get("location"),
                    "phone": cv_builder_data.get("phone"),
                })
            with c2:
                st.markdown("**Competencies & Skills**")
                st.write(cv_builder_data.get("competencies", []))
                
            st.divider()
            
            st.markdown("**Experience Entries**")
            if cv_builder_data.get("experiences"):
                st.dataframe(cv_builder_data["experiences"])
            else:
                st.text("No experience entries.")
                
            st.markdown("**Education Entries**")
            if cv_builder_data.get("education"):
                st.dataframe(cv_builder_data["education"])
            else:
                st.text("No education entries.")
                
            st.markdown("**Projects**")
            if cv_builder_data.get("projects"):
                st.dataframe(cv_builder_data["projects"])
            else:
                st.text("No projects.")

    # =========================================================================
    # TAB 7: CAREER DISCOVERY ENGINE
    # =========================================================================
    with t7:
        st.subheader("Discovery Engine Diagnostics")
        st.info("Insights into the Career Discovery recommendation logic and results.")
        
        discovery_results = st.session_state.get("discovery_results", [])
        has_cv = st.session_state.get("discovery_has_cv", False)
        cv_text_session = st.session_state.get("processed_cv_text", "")
        
        if not discovery_results:
            st.warning("No discovery analysis has been performed yet.")
            st.markdown("Run a 'Career Discovery' session from the main menu to see data here.")
        else:
            # 1. Summary Metrics
            st.markdown("### Recommendation Summary")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Matches", len(discovery_results))
            with col2:
                avg_score = sum(r['score'] for r in discovery_results) / len(discovery_results) if discovery_results else 0
                st.metric("Avg Match Score", f"{avg_score:.1f}%")
            with col3:
                st.metric("CV Integration", "Active" if has_cv else "Inactive")
                
            st.divider()
            
            # 2. Results Data Inspector
            st.markdown("### Raw Results Data (JSON)")
            with st.expander("View Result Objects (Top 10)", expanded=False):
                st.json(discovery_results[:10])
                
            # 3. Algorithm Debugging
            st.markdown("### Internal Scoring Logic")
            st.markdown("""
            The Discovery Score is calculated as a weighted average:
            - **Preference Alignment (40%)**: Matches against industry, remote, and style preferences.
            - **Skill Match (60%)**: Jaccard similarity between detected CV skills and role archetypes.
            - **Education Boost**: Small percentage bonus for relevant major/degree field.
            """)
            
            # 4. Filter Testing
            st.markdown("### Filter Simulation")
            if discovery_results:
                q_range = st.slider("Quality Threshold (Min Score %)", 0, 100, 25)
                highly_relevant = [r for r in discovery_results if r['score'] >= q_range]
                st.write(f"Items exceeding threshold: {len(highly_relevant)}")
                
                if highly_relevant:
                    # Show as dataframe for easy inspection
                    debug_df = pd.DataFrame(highly_relevant)
                    if not debug_df.empty:
                        # Drop columns that might have complex objects for better display
                        cols_to_show = [col for col in debug_df.columns if col not in ['skills_matched', 'missing_skills', 'skills_required']]
                        st.dataframe(debug_df[cols_to_show], use_container_width=True)
            
            # 5. Profile Analysis
            if has_cv:
                st.divider()
                st.markdown("### Detected Interest Signal")
                cv_level, score = ml_utils.detect_seniority(cv_text_session)
                st.write(f"Detected Seniority: **{cv_level}** (Confidence: {score:.2f})")
                
                # Show extracted skills used for discovery
                cv_hard, cv_soft = ml_utils.extract_skills_from_text(cv_text_session)
                all_found = cv_hard | cv_soft
                st.markdown(f"**Skills used for matching:** ({len(all_found)} detected)")
                st.write(", ".join(sorted(all_found)))

# =============================================================================
# CV BUILDER PAGE
# =============================================================================
# Pagina per creare un CV professionale usando un form interattivo.
# Integrazione con l'analisi Job per suggerire skill mancanti.
# =============================================================================

def render_cv_builder():
    """
    CV BUILDER PAGE
    ================
    Permette di creare un CV professionale con un flusso guidato:
    Step 1: Profile (Dati personali e Summary)
    Step 2: Skills (Competenze e suggerimenti ML)
    Step 3: Experience (Lavoro e Formazione)
    Step 4: Review (Anteprima e Export)
    """
    render_navigation() # GLOBAL NAVBAR
    
    # Initialize basic session state for wizard
    if "cv_builder_step" not in st.session_state:
        st.session_state["cv_builder_step"] = 1

    # HANDLE DEMO DATA LOADING REMOVED

    # TITLE (Centered)
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='margin: 0; padding: 0;'>CV Builder</h1>
        <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>Professional CV Builder</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # WIZARD PROGRESS BAR
    steps = ["1. Profile", "2. Skills", "3. Experience", "4. Review"]
    curr_step = st.session_state["cv_builder_step"]
    
    # Custom CSS for Builder Steps
    st.markdown("""
    <style>
    .builder-step { font-weight: bold; color: #8b949e; margin-right: 1.5rem; }
    .builder-step.active { color: #00A0DC; border-bottom: 2px solid #00A0DC; }
    .builder-step.completed { color: #00C853; }
    </style>
    """, unsafe_allow_html=True)
    
    # Render Progress
    cols = st.columns(4)
    for i, label in enumerate(steps):
        step_num = i + 1
        status_class = "active" if step_num == curr_step else ("completed" if step_num < curr_step else "")
        with cols[i]:
            st.markdown(f"<div class='builder-step {status_class}' style='text-align: center;'>{label}</div>", unsafe_allow_html=True)
            if step_num < curr_step:
                st.progress(100)
            elif step_num == curr_step:
                st.progress(50)
            else:
                st.progress(0)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Get CV Data
    cv_data = st.session_state["cv_builder"]
    
    # Initialize Global JD Text for all steps
    jd_text = st.session_state.get("cv_builder_jd", "")

    # (Custom sidebar removed to use Global Navigation)
    
    # --- BUILDER STEPS CONTENT ---
    
    # STEP 1: PROFILE
    if curr_step == 1:
        st.header("1. Personal Profile")
        
        col1, col2 = st.columns(2)
        with col1:
            cv_data["name"] = st.text_input("Full Name", value=cv_data.get("name", ""))
            cv_data["email"] = st.text_input("Email", value=cv_data.get("email", ""))
        with col2:
            cv_data["location"] = st.text_input("Location", value=cv_data.get("location", ""))
            cv_data["phone"] = st.text_input("Phone", value=cv_data.get("phone", ""))
            
        st.markdown("### Professional Summary")
        cv_data["summary"] = st.text_area(
            "Write a compelling summary", 
            value=cv_data.get("summary", ""),
            height=150,
            placeholder="E.g. Experienced Project Manager with 5+ years..."
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # JD Input for Smart Suggestions (Optional - Moved from Sidebar)
        # Using a distinct key suffix or logic to keep session state
        with st.expander("Target Job Description (Optional)", expanded=False):
            st.caption("Paste a Job Description here to get real-time optimization advice and skill gap analysis.")
            
            # Check initialization
            if "cv_builder_jd" not in st.session_state:
                st.session_state["cv_builder_jd"] = ""
                
            st.text_area(
                "Job Description",
                height=150,
                placeholder="Paste JD content here...",
                label_visibility="collapsed",
                key="cv_builder_jd" 
            )

            # --- SMART SCORE LOGIC (Inlined for immediate feedback) ---
            jd_text = st.session_state.get("cv_builder_jd", "")
            if jd_text:
                st.divider()
                # 1. Extract JD Requirements
                jd_hard, jd_soft = ml_utils.extract_skills_from_text(jd_text, is_jd=True)
                jd_reqs = jd_hard | jd_soft
                
                # 2. Extract CV Skills (from all current fields)
                user_skills = set(cv_data.get("competencies", []))
                
                # Build temporary full text from current inputs
                parts = [
                    cv_data.get("summary", ""),
                    cv_data.get("tech_skills_text", "")
                ]
                
                # Experience
                for exp in cv_data.get("experiences", []):
                    parts.append(exp.get("title", ""))
                    parts.append(exp.get("bullets", ""))
                    parts.append(exp.get("tech", ""))
                    
                # Projects
                for proj in cv_data.get("projects", []):
                    parts.append(proj.get("description", ""))
                    
                # Education
                for edu in cv_data.get("education", []):
                    parts.append(edu.get("details", ""))
                
                # Languages
                for lang in cv_data.get("languages", []):
                    l_val = lang.get("language", "").strip()
                    if l_val:
                        user_skills.add(l_val)
                        parts.append(l_val)
                        
                full_cv_text = " ".join(parts)
                
                if full_cv_text:
                    th, ts = ml_utils.extract_skills_from_text(full_cv_text)
                    user_skills.update(th)
                    user_skills.update(ts)
                
                # 3. Calculate Score
                # 3. Calculate Score using Centralized Logic (Inference Aware)
                if jd_text:
                    # Use analyze_gap to get full power of inference rules (A -> B)
                    gap_analysis = ml_utils.analyze_gap(full_cv_text, jd_text)
                    
                    score = int(gap_analysis["match_percentage"])
                    missing = gap_analysis["missing_hard"]
                    matched_hard = gap_analysis["matching_hard"]

                    c_score, c_info = st.columns([1, 2])
                    with c_score:
                        st.metric("Optimization Score", f"{score}%")
                    with c_info:
                        if score < 100:
                            if missing:
                                st.warning(f"Missing: {', '.join(list(missing)[:3])}...")
                            else:
                                st.info("Good match on technical skills!")
                        else:
                            st.success("Perfect technical match!")
                else:
                    st.caption("JD loaded. Add skills to see score.")

        # Nav Buttons
        col_prev, col_next = st.columns([1, 1])
        with col_next:
            if st.button("Next: Skills →", type="primary", use_container_width=True):
                st.session_state["cv_builder_step"] = 2
                st.rerun()

    # STEP 2: SKILLS
    elif curr_step == 2:
        st.header("2. Skills & Competencies")
        
        # Smart Suggestions Logic
        if jd_text:
            jd_hard, _ = ml_utils.extract_skills_from_text(jd_text, is_jd=True)
            user_skills = set(cv_data.get("competencies", []))
            missing = jd_hard - user_skills
            
            if missing:
                st.info(f"**JD Suggestions:** Consider adding: {', '.join(list(missing)[:5])}")
        
        # Form to prevent reruns on every selection
        # Competencies - Immediate update for better UX
        all_skills = sorted(list(set(list(constants.HARD_SKILLS.keys()) + list(constants.SOFT_SKILLS.keys()))))
        
        # Pre-select existing or default empty
        default_skills = [c for c in cv_data.get("competencies", []) if c in all_skills]
        
        selected_skills = st.multiselect(
            "Core Competencies (Select from DB)", 
            options=all_skills, 
            default=default_skills
        )
        # Update immediately
        cv_data["competencies"] = selected_skills
        
        # Tech Skills Text
        st.markdown("### Technical Skills (Free Text)")
        tech_text = st.text_area(
            "Categorized Skills",
            value=cv_data.get("tech_skills_text", ""),
            height=200,
            placeholder="Languages: Python, Java\nTools: Tableau, Git"
        )
        # Update immediately
        cv_data["tech_skills_text"] = tech_text
        
        # Nav Buttons (Standard Buttons)
        col_prev, col_next = st.columns([1, 1])
        with col_prev:
            if st.button("← Back"):
                st.session_state["cv_builder_step"] = 1
                st.rerun()

        with col_next:
            if st.button("Next: Experience →", type="primary", use_container_width=True):
                st.session_state["cv_builder_step"] = 3
                st.rerun()

    # STEP 3: EXPERIENCE
    # STEP 3: EXPERIENCE & EDUCATION
    elif curr_step == 3:
        st.header("3. Experience & Qualifications")
        
        # --- EXPERIENCE ---
        st.markdown("### Professional Experience")
        if "experiences" not in cv_data: cv_data["experiences"] = []
        
        if st.button("+ Add Position", key="add_exp"):
            cv_data["experiences"].insert(0, {})
            st.rerun()
            
        for i, exp in enumerate(cv_data["experiences"]):
            with st.expander(f"{exp.get('title', 'Position')} at {exp.get('company', 'Company')}", expanded=True):
                c1, c2 = st.columns(2)
                exp["title"] = c1.text_input("Job Title", value=exp.get("title", ""), key=f"t{i}")
                exp["company"] = c2.text_input("Company", value=exp.get("company", ""), key=f"c{i}")
                
                c3, c4 = st.columns(2)
                exp["dates"] = c3.text_input("Dates", value=exp.get("dates", ""), key=f"d{i}", placeholder="e.g. Jan 2023 - Present")
                exp["location"] = c4.text_input("Location", value=exp.get("location", ""), key=f"l{i}")
                
                exp["bullets"] = st.text_area("Key Achievements", value=exp.get("bullets", ""), key=f"b{i}", height=100, placeholder="• Achieved X by doing Y...")
                exp["tech"] = st.text_input("Technologies Used", value=exp.get("tech", ""), key=f"tech{i}")
                
                if st.button("Delete Position", key=f"del_exp{i}"):
                    cv_data["experiences"].pop(i)
                    st.rerun()

        st.divider()

        # --- EDUCATION ---
        st.markdown("### Education")
        if "education" not in cv_data: cv_data["education"] = []
        
        if st.button("+ Add Education", key="add_edu"):
            cv_data["education"].insert(0, {})
            st.rerun()
            
        for i, edu in enumerate(cv_data["education"]):
            with st.expander(f"{edu.get('degree', 'Degree')} at {edu.get('institution', 'Institution')}", expanded=True):
                edu["degree"] = st.text_input("Degree/Certificate", value=edu.get("degree", ""), key=f"ed_deg{i}")
                
                c1, c2 = st.columns(2)
                edu["institution"] = c1.text_input("Institution", value=edu.get("institution", ""), key=f"ed_inst{i}")
                edu["location"] = c2.text_input("Location", value=edu.get("location", ""), key=f"ed_loc{i}")
                
                edu["dates"] = st.text_input("Dates", value=edu.get("dates", ""), key=f"ed_date{i}")
                edu["details"] = st.text_area("Details (Coursework, Honors)", value=edu.get("details", ""), key=f"ed_det{i}", height=80)
                
                if st.button("Delete Education", key=f"del_edu{i}"):
                    cv_data["education"].pop(i)
                    st.rerun()

        st.divider()

        # --- PROJECTS ---
        st.markdown("### Key Projects")
        if "projects" not in cv_data: cv_data["projects"] = []
        
        if st.button("+ Add Project", key="add_proj"):
            cv_data["projects"].insert(0, {})
            st.rerun()
            
        for i, proj in enumerate(cv_data["projects"]):
            with st.expander(f"{proj.get('name', 'Project')}", expanded=True):
                proj["name"] = st.text_input("Project Name", value=proj.get("name", ""), key=f"pj_name{i}")
                proj["link"] = st.text_input("Link (URL)", value=proj.get("link", ""), key=f"pj_link{i}")
                proj["description"] = st.text_area("Description", value=proj.get("description", ""), key=f"pj_desc{i}", height=80)
                
                if st.button("Delete Project", key=f"del_proj{i}"):
                    cv_data["projects"].pop(i)
                    st.rerun()

        st.divider()

        # --- LANGUAGES ---
        st.markdown("### Languages")
        if "languages" not in cv_data: cv_data["languages"] = []
        
        if st.button("+ Add Language", key="add_lang"):
            cv_data["languages"].append({"language": "", "level": ""})
            st.rerun()
            
        for i, lang in enumerate(cv_data["languages"]):
            c1, c2, c3 = st.columns([2, 2, 1])
            lang["language"] = c1.text_input("Language", value=lang.get("language", ""), key=f"lg_name{i}")
            level_options = ["Native", "Professional (C1-C2)", "Intermediate (B1-B2)", "Basic (A1-A2)"]
            current_level = lang.get("level", "")
            try:
                level_idx = level_options.index(current_level) if current_level in level_options else 0
            except:
                level_idx = 0
            lang["level"] = c2.selectbox("Level", level_options, index=level_idx, key=f"lg_lvl{i}")
            if c3.button("X", key=f"del_lang{i}"):
                cv_data["languages"].pop(i)
                st.rerun()

        # Nav Buttons
        st.divider()
        col_prev, col_next = st.columns([1, 1])
        with col_prev:
            if st.button("← Back"):
                st.session_state["cv_builder_step"] = 2
                st.rerun()
        with col_next:
            if st.button("Next: Review →", type="primary", use_container_width=True):
                st.session_state["cv_builder_step"] = 4
                st.rerun()

    # STEP 4: REVIEW & EXPORT
    elif curr_step == 4:
        st.header("4. Final Review")
        
        # Generate CV Text (for TXT/PDF download)
        cv_text_lines = []
        if cv_data.get("name"):
            cv_text_lines.append(cv_data["name"])
            parts = [p for p in [cv_data.get("location"), cv_data.get("email"), cv_data.get("phone")] if p]
            if parts: cv_text_lines.append(" | ".join(parts))
        if cv_data.get("summary"):
            cv_text_lines.append("\nSUMMARY\n" + cv_data["summary"])
        if cv_data.get("competencies"):
            cv_text_lines.append("\nCORE COMPETENCIES\n" + " | ".join(cv_data["competencies"]))
        if cv_data.get("tech_skills_text"):
            cv_text_lines.append("\nTECHNICAL SKILLS\n" + cv_data["tech_skills_text"])
        if cv_data.get("experiences"):
            cv_text_lines.append("\nPROFESSIONAL EXPERIENCE")
            for exp in cv_data["experiences"]:
                if exp.get("title"):
                    line = f"\n{exp['title']}"
                    if exp.get("company"): line += f" @ {exp['company']}"
                    if exp.get("dates"): line += f" ({exp['dates']})"
                    cv_text_lines.append(line)
                    if exp.get("bullets"): cv_text_lines.append(exp["bullets"])
        if cv_data.get("education"):
            cv_text_lines.append("\nEDUCATION")
            for edu in cv_data["education"]:
                line = f"\n{edu.get('degree', '')}"
                if edu.get("institution"): line += f" @ {edu['institution']}"
                if edu.get("dates"): line += f" ({edu['dates']})"
                cv_text_lines.append(line)
                if edu.get("details"): cv_text_lines.append(edu["details"])
        if cv_data.get("projects"):
            cv_text_lines.append("\nPROJECTS")
            for proj in cv_data["projects"]:
                cv_text_lines.append(f"\n{proj.get('name', '')}")
                if proj.get("description"): cv_text_lines.append(proj["description"])
        if cv_data.get("languages"):
            cv_text_lines.append("\nLANGUAGES")
            cv_text_lines.append(" | ".join([f"{l['language']}: {l['level']}" for l in cv_data["languages"] if l.get("language")]))
        cv_text = "\n".join(cv_text_lines)
        
        # Build HTML Preview
        html_parts = []
        
        # Header
        if cv_data.get("name"):
            html_parts.append(f"<h2 style='color: #00A0DC; margin: 0;'>{cv_data['name']}</h2>")
            parts = [p for p in [cv_data.get("location"), cv_data.get("email"), cv_data.get("phone")] if p]
            if parts:
                html_parts.append(f"<p style='color: #8b949e; margin: 0.25rem 0 1rem 0;'>{' | '.join(parts)}</p>")
        
        # Summary
        if cv_data.get("summary"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>SUMMARY</h4>")
            html_parts.append(f"<p style='color: #c9d1d9; line-height: 1.6;'>{cv_data['summary']}</p>")
        
        # Core Competencies
        if cv_data.get("competencies"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>CORE COMPETENCIES</h4>")
            tags = "".join([f"<span style='background: #0d419d; color: #7ec8ff; padding: 4px 12px; border-radius: 15px; margin: 3px; display: inline-block; font-size: 0.85rem;'>{c}</span>" for c in cv_data["competencies"]])
            html_parts.append(f"<div style='margin: 0.5rem 0;'>{tags}</div>")
        
        # Technical Skills
        if cv_data.get("tech_skills_text"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>TECHNICAL SKILLS</h4>")
            html_parts.append(f"<p style='color: #c9d1d9;'>{cv_data['tech_skills_text']}</p>")
        
        # Experience
        if cv_data.get("experiences"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>PROFESSIONAL EXPERIENCE</h4>")
            for exp in cv_data["experiences"]:
                if exp.get("title"):
                    html_parts.append(f"<div style='margin: 1rem 0; padding-left: 1rem; border-left: 3px solid #00A0DC;'>")
                    html_parts.append(f"<strong style='color: #fff;'>{exp['title']}</strong>")
                    if exp.get("company"): html_parts.append(f"<span style='color: #8b949e;'> @ {exp['company']}</span>")
                    if exp.get("dates"): html_parts.append(f"<span style='color: #6e7681; float: right;'>{exp['dates']}</span>")
                    if exp.get("bullets"):
                        bullets_html = exp["bullets"].replace("\n", "<br>")
                        html_parts.append(f"<p style='color: #c9d1d9; margin: 0.5rem 0; white-space: pre-line;'>{bullets_html}</p>")
                    if exp.get("tech"):
                        html_parts.append(f"<p style='color: #58a6ff; font-size: 0.85rem; margin: 0.25rem 0;'>Tech: {exp['tech']}</p>")
                    html_parts.append("</div>")
        
        # Education
        if cv_data.get("education"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>EDUCATION</h4>")
            for edu in cv_data["education"]:
                html_parts.append(f"<div style='margin: 0.75rem 0;'>")
                html_parts.append(f"<strong style='color: #fff;'>{edu.get('degree', '')}</strong>")
                if edu.get("institution"): html_parts.append(f"<span style='color: #8b949e;'> @ {edu['institution']}</span>")
                if edu.get("dates"): html_parts.append(f"<span style='color: #6e7681; float: right;'>{edu['dates']}</span>")
                if edu.get("details"): html_parts.append(f"<p style='color: #c9d1d9; margin: 0.25rem 0;'>{edu['details']}</p>")
                html_parts.append("</div>")
        
        # Projects
        if cv_data.get("projects"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>PROJECTS</h4>")
            for proj in cv_data["projects"]:
                html_parts.append(f"<div style='margin: 0.75rem 0;'>")
                html_parts.append(f"<strong style='color: #fff;'>{proj.get('name', '')}</strong>")
                if proj.get("link"): html_parts.append(f" <a href='{proj['link']}' style='color: #58a6ff;' target='_blank'>[Link]</a>")
                if proj.get("description"): html_parts.append(f"<p style='color: #c9d1d9; margin: 0.25rem 0;'>{proj['description']}</p>")
                html_parts.append("</div>")
        
        # Languages
        if cv_data.get("languages"):
            html_parts.append("<h4 style='color: #fff; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-top: 1.5rem;'>LANGUAGES</h4>")
            lang_html = " | ".join([f"<span style='color: #c9d1d9;'>{l['language']}: <strong>{l['level']}</strong></span>" for l in cv_data["languages"] if l.get("language")])
            html_parts.append(f"<p>{lang_html}</p>")
        
        cv_html = "\n".join(html_parts)

        # Preview Area
        st.markdown("### CV Preview")
        st.markdown(f"<div style='background: #161b22; padding: 2rem; border-radius: 12px; border: 1px solid #30363d; max-height: 700px; overflow-y: auto;'>{cv_html}</div>", unsafe_allow_html=True)
        
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        # Get candidate name for filename (sanitize for filesystem)
        candidate_name = cv_data.get("name", "My_CV").replace(" ", "_").replace("/", "_").replace("\\", "_")
        if not candidate_name:
            candidate_name = "My_CV"
        
        with col1:
             st.download_button("Download TXT", cv_text, file_name=f"{candidate_name}_CV.txt", use_container_width=True)
             
        with col2:
             # Basic PDF Generation
             pdf_bytes = ml_utils.generate_cv_pdf(cv_text)
             if pdf_bytes:
                 st.download_button("Download PDF", pdf_bytes, file_name=f"{candidate_name}_CV.pdf", mime="application/pdf", use_container_width=True)
             else:
                 st.warning("PDF Error")
             
        with col3:
             if st.button("Use for Analysis →", type="primary", use_container_width=True):
                 st.session_state["cv_text"] = cv_text
                 st.session_state["page"] = "CV Evaluation" # Redirect to Eval
                 st.success("CV Loaded! Redirecting...")
                 st.rerun()

        # Nav Buttons
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Edit"):
            st.session_state["cv_builder_step"] = 3
            st.rerun()

# =============================================================================
# INTERFACCIA UTENTE PRINCIPALE (UI)
# =============================================================================
# Riferimento corso: "Knowledge Presentation" (KDD Step 7)
#
# Questa è la pagina principale dell'applicazione dove l'utente:
# 1. Inserisce il CV (testo o PDF)
# 2. Inserisce la Job Description
# 3. Attiva opzioni (Cover Letter, Portfolio)
# 4. Avvia l'analisi
# 5. Visualizza i risultati
#
# L'UI è costruita con Streamlit, un framework Python per dashboard.
# =============================================================================

def render_landing_page():
    """
    LANDING PAGE
    ============
    Nuova pagina principale che funge da hub di navigazione.
    """
    render_navigation() # GLOBAL NAVBAR
    
    # HERO SECTION
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0 1rem 0; width: 100%;'>
        <h1 style='font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem; background: -webkit-linear-gradient(45deg, #0077B5, #00C853); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>CareerMatch AI</h1>
    </div>
    """, unsafe_allow_html=True)

    # Metrics Row - Elegant Style (Title Gradient)
    metric_gradient = "background: -webkit-linear-gradient(45deg, #0077B5, #00C853); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
    
    st.markdown(f"""
    <div style="display: flex; justify-content: center; gap: 8rem; margin-bottom: 3rem; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <h2 style="{metric_gradient} margin: 0; padding: 0; font-size: 2.2rem; font-weight: 600;">950+</h2>
            <span style="color: #c9d1d9; font-size: 1.5rem; font-weight: 400;">Killer Keywords</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <h2 style="{metric_gradient} margin: 0; padding: 0; font-size: 2.2rem; font-weight: 600;">230+</h2>
            <span style="color: #c9d1d9; font-size: 1.5rem; font-weight: 400;">Job Archetypes</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <h2 style="{metric_gradient} margin: 0; padding: 0; font-size: 2.2rem; font-weight: 600;">25+</h2>
            <span style="color: #c9d1d9; font-size: 1.5rem; font-weight: 400;">Sectors Covered</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # FUNNEL DESCRIPTION - centered
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-top: 1rem; width: 100%;'>
        <p style='color: #8b949e; font-size: 1rem; max-width: 700px; margin: 0 auto;'>
            <strong style='color: #c9d1d9;'>Your Career Journey:</strong> 
            Start by discovering your ideal career path, then build a tailored CV, and finally evaluate it against real job descriptions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # NAVIGATION CARDS - with spacer columns for centering
    spacer1, col1, col2, col3, spacer2 = st.columns([0.5, 1, 1, 1, 0.5])
    
    # Custom CSS for cards
    card_style = """
    <div style='text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between;'>
        <div>
            <h3 style='margin-bottom: 1rem;'>{}</h3>
            <p style='color: #8b949e; margin-bottom: 2rem; font-size: 0.9rem;'>{}</p>
        </div>
    </div>
    """
    
    # 1. CAREER DISCOVERY (first)
    with col1:
        with st.container(border=True):
            st.markdown(card_style.format("Career Discovery", "Not sure what jobs fit you? Answer a few questions about your preferences and let AI suggest the best career paths."), unsafe_allow_html=True)
            if st.button("Discover My Career", use_container_width=True, type="primary"):
                st.session_state["page"] = "Career Discovery"
                st.rerun()
    
    # 2. CV BUILDER (second)
    with col2:
        with st.container(border=True):
            st.markdown(card_style.format("CV Builder", "Build a professional, ATS-optimized CV with our AI-powered tool. Get real-time suggestions and tailored content."), unsafe_allow_html=True)
            if st.button("Open CV Builder", use_container_width=True):
                st.session_state["page"] = "CV Builder"
                st.rerun()

    # 3. CV EVALUATION (third)
    with col3:
        with st.container(border=True):
            st.markdown(card_style.format("CV Evaluation", "Unlock your career potential with deep gap analysis. Get AI-driven advice to bridge skill gaps."), unsafe_allow_html=True)
            if st.button("Start Evaluation", use_container_width=True):
                st.session_state["page"] = "CV Evaluation"
                st.rerun()

    # Footer Divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # Career Assistant Pop-up (Call to Action) - Unified English & Formal
    st.markdown("""
    <div class="landing-chat-popup">
        <div class="landing-chat-popup-text">
            <h4 class="landing-chat-popup-title">Questions or Issues?</h4>
            <p style="margin: 0; font-size: 0.95rem; color: var(--text-secondary);">
                Ask our Career Consultant <b>Ruben</b> in the sidebar. He is an expert in the KDD process and can help you navigate through the app features.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer with beta note and contact
    st.markdown("---")
    # Email body template (URL encoded)
    email_body = "Hi%2C%0A%0AI%20would%20like%20to%20report%3A%0A%0AType%3A%20%5BBug%20%2F%20Missing%20Sector%20%2F%20Feedback%20%2F%20Question%5D%0A%0ADescription%3A%0A%0A%0A%0AThank%20you!"
    st.markdown(f"""
    <div style='text-align: center; color: #666; font-size: 0.85rem;'>
        App in Continuous Development (0% match may indicate sector not yet covered) | 
        Questions, missing sectors, bugs or feedback? Contact via 
        <a href='https://mail.google.com/mail/?view=cm&to=dellacquagiacomo@gmail.com&su=CareerMatch%20AI%20Feedback&body={email_body}' target='_blank' style='color: #00A0DC;'>Gmail</a> or 
        <a href='https://outlook.live.com/mail/0/deeplink/compose?to=dellacquagiacomo@gmail.com&subject=CareerMatch%20AI%20Feedback&body={email_body}' target='_blank' style='color: #00A0DC;'>Outlook</a>
    </div>
    """, unsafe_allow_html=True)



# =============================================================================
# CAREER DISCOVERY PAGE
# =============================================================================
# New standalone page that helps users discover suitable career paths
# based on their preferences, background, and optional CV.
# =============================================================================

def render_career_discovery():
    """
    CAREER DISCOVERY PAGE
    =====================
    Helps users explore job opportunities based on preferences.
    Styled consistently with CV Builder and Evaluation pages.
    """
    render_navigation() # GLOBAL NAVBAR
    
    
    # --- HEADER (Same pattern as CV Builder) ---
    
    # --- HEADER (Same pattern as CV Builder) ---
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='margin: 0; padding: 0;'>Career Discovery</h1>
        <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>Find career paths that match your profile and preferences</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- INPUT: Just one text area ---
    free_text = st.text_area(
        "Describe what you're looking for",
        height=120,
        placeholder="Example: I want a dynamic job with international clients, creative work, remote-friendly...",
        key="discovery_free_text"
    )
    
    # Optional CV upload in expander
    with st.expander("Upload CV (optional)", expanded=False):
        cv_file = st.file_uploader("Upload CV (PDF)", type=["pdf"], key="discovery_cv")
        cv_text = ""
        if cv_file:
            try:
                cv_text = ml_utils.extract_text_from_pdf(cv_file)
                st.success(f"CV loaded: {len(cv_text.split())} words")
            except Exception as e:
                st.error(f"Error: {e}")
        
        cv_text_input = st.text_area(
            "Or paste CV text",
            height=100,
            key="discovery_cv_text",
            placeholder="Paste your CV content here..."
        )
        if cv_text_input and not cv_text:
            cv_text = cv_text_input
    
    # Optional filters in expander
    with st.expander("Filters (optional)", expanded=False):
        # Extract unique sectors from JOB_ARCHETYPES_EXTENDED
        job_archs = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
        all_sectors = sorted(list(set(m.get("sector", "Other") for m in job_archs.values())))
        
        selected_categories = st.multiselect(
            "Industries (leave empty for Any)",
            options=all_sectors,
            key="discovery_categories",
            placeholder="Any / All Industries"
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            client_facing = st.selectbox("Interaction", ["Any", "Client-facing", "Behind scenes"], key="pref_client")
            remote_pref = st.selectbox("Location", ["Any", "Remote", "On-site"], key="pref_remote")
        with col2:
            international = st.selectbox("Scope", ["Any", "International", "Local"], key="pref_intl")
            dynamic = st.selectbox("Pace", ["Any", "Dynamic", "Stable"], key="pref_dynamic")
        with col3:
            creative = st.selectbox("Style", ["Any", "Creative", "Structured"], key="pref_creative")
    
    st.markdown("")
    
    # --- DISCOVER BUTTON ---

    discover_clicked = st.button("Find My Career Paths", type="primary", use_container_width=True)
    
    # --- LOGIC: Calculate or Retrieve Results ---
    if discover_clicked:
        preferences = {
            "categories": selected_categories if selected_categories else None,
            "client_facing": True if client_facing == "Client-facing" else (False if client_facing == "Behind scenes" else None),
            "remote_friendly": True if remote_pref == "Remote" else (False if remote_pref == "On-site" else None),
            "international": True if international == "International" else (False if international == "Local" else None),
            "dynamic": True if dynamic == "Dynamic" else (False if dynamic == "Stable" else None),
            "creative": True if creative == "Creative" else (False if creative == "Structured" else None),
        }
        
        final_cv_text = cv_text if cv_text else ""
        final_free_text = free_text if free_text else ""
        
        if not final_cv_text and not final_free_text and not selected_categories and all(v is None for k, v in preferences.items() if k != "categories"):
            st.warning("Please provide some information - describe yourself, upload a CV, or select preferences.")
        else:
            with st.spinner("Analyzing your profile..."):
                results = ml_utils.discover_careers(
                    cv_text=final_cv_text,
                    free_text=final_free_text,
                    preferences=preferences
                )
                # Store in Session State
                st.session_state['discovery_results'] = results
                st.session_state['discovery_has_cv'] = bool(final_cv_text)
                st.session_state['processed_cv_text'] = final_cv_text
                
    # --- RENDER RESULTS (from Session State) ---
    if 'discovery_results' in st.session_state:
        results = st.session_state['discovery_results']
        has_cv = st.session_state.get('discovery_has_cv', False)
        cv_text_session = st.session_state.get('processed_cv_text', "")

        # Seniority for Discovery
        cv_level, _ = ml_utils.detect_seniority(cv_text_session) if cv_text_session else ("Mid Level", 0.0)
        query_prefix = ""
        if cv_level == "Entry Level": query_prefix = "Junior "
        elif cv_level == "Senior Level": query_prefix = "Senior "
        
        if has_cv:
             st.info(f"**Profile Analysis detected:** {cv_level}. Search links are optimized for this level.")

        if results:
            st.divider()
            st.subheader(f"Found {len(results)} Career Matches")
            
            # Filter Expander - Removed, use visible radio
            st.markdown("Score Range")
            match_range = st.radio(
                "Score Range",
                options=["0-25%", "25-50%", "50-75%", "75-100%"],
                horizontal=True,
                label_visibility="collapsed",
                key="discovery_filter_range",
                index=0 # Start with 0-25 to ensure results are seen? Or 0 for wider. 
                #Actually defaults usually 25, so maybe index 0 or 1. Let's stick with 0 or 1.
                # If I put 0-25, users might see low scores.
                # Let's set index=1 (25-50) or 0.
            )
            
            min_s, max_s = 0, 100
            if match_range == "0-25%": min_s, max_s = 0, 25
            elif match_range == "25-50%": min_s, max_s = 25, 50
            elif match_range == "50-75%": min_s, max_s = 50, 75
            elif match_range == "75-100%": min_s, max_s = 75, 100
            
            filtered_results = [r for r in results if min_s <= r['score'] <= max_s]
            
            if has_cv:
                st.caption("Ranked by skill match (60%) + preference alignment (40%) + education boost")
            else:
                st.caption("Ranked by preference alignment. Upload a CV for skill-based matching.")
            
            if filtered_results:
                render_career_discovery_results(filtered_results, has_cv=has_cv, seniority_prefix=query_prefix)
            else:
                st.info(f"No careers found in the {match_range} range. Try a different filter.")
        else:
            st.info("No strong matches found. Try broadening your preferences.")




def render_career_discovery_results(results: list, has_cv: bool = False, seniority_prefix: str = ""):
    """
    Renders the Career Discovery results as interactive role cards.
    """
    st.subheader("Your Career Matches")
    
    if has_cv:
        st.caption("Scores are based on your skill match (60%) and preference alignment (40%)")
    else:
        st.caption("Scores are based on preference alignment. Upload a CV for skill-based matching.")
    
    # Display in rows of 3
    for i in range(0, len(results), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(results):
                role = results[i + j]
                with col:
                    render_role_card(role, has_cv, seniority_prefix)


def render_role_card(role: dict, has_cv: bool = False, seniority_prefix: str = ""):
    """
    Renders a single role recommendation card.
    """
    score = role["score"]
    role_name = role["role"]
    category = role["category"]
    
    # Color based on score
    if score >= 70:
        score_color = "#00C853"  # Green
        score_label = "Strong Match"
    elif score >= 50:
        score_color = "#FFB300"  # Amber
        score_label = "Good Potential"
    else:
        score_color = "#00A0DC"  # Blue
        score_label = "Worth Exploring"
    
    # Card container
    with st.container(border=True):
        st.markdown(f"##### {role_name}")
        st.progress(int(min(score, 100)))
        st.caption(f"**{score:.0f}% Match** | {category}")
        
        # Job search links - prominent like Career Compass
        role_query = urllib.parse.quote(f"{seniority_prefix}{role_name}")
        italy_query = urllib.parse.quote(f"{seniority_prefix}{role_name} Italia")
        
        st.markdown(f"""
        <div style="display: flex; gap: 10px; font-size: 0.9em; margin-top: 12px; margin-bottom: 4px;">
            <a href='https://www.google.com/search?q={role_query}+jobs' target='_blank' style="text-decoration: none;">Google</a>
            <span style="color: #30363d;">|</span>
            <a href='https://www.linkedin.com/jobs/search/?keywords={role_query}' target='_blank' style="text-decoration: none;">LinkedIn</a>
            <span style="color: #30363d;">|</span>
            <a href='https://it.indeed.com/jobs?q={italy_query}' target='_blank' style="text-decoration: none;">Indeed</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Skills in expander
        skills_required = role.get("skills_required", [])
        skills_matched = set(role.get("skills_matched", []))
        missing_skills = role.get("missing_skills", [])
        
        with st.expander("Required Skills"):
            if has_cv and skills_matched:
                st.markdown("**You have:** " + ", ".join(list(skills_matched)))
            if has_cv and missing_skills:
                st.markdown("**Missing:** " + ", ".join(list(missing_skills)[:5]))
            elif not has_cv:
                st.markdown(", ".join(skills_required[:5]))



def render_evaluation_page():
    """
    RENDERING PAGINA PRINCIPALE
    ============================
    Riferimento corso: "Knowledge Presentation"
    
    Gestisce:
    - Sidebar con branding e controlli
    - Area input per CV e Job Description
    - Opzioni aggiuntive (Cover Letter, Portfolio)
    - Pulsante di analisi
    - Visualizzazione risultati
    """
    
    render_navigation() # GLOBAL NAVBAR
    
    # Rest of Layout (Main Area)
    # Removed Local Sidebar logic to avoid duplication

    # Local Page Options (Extra Analysis)
    with st.sidebar:
        st.divider()
        st.caption("Page Settings")
        st.toggle("Include Project Portfolio", key="show_project_toggle")
        st.toggle("Include Cover Letter", key="show_cover_letter")
        
    # Remove demo mode info banner
    pass

    # ==========================================================================
    # MAIN CONTENT AREA - Hero Section
    # ==========================================================================
    
    # Initialize variables to avoid NameError
    show_project_eval = st.session_state.get("show_project_toggle", False)
    show_cover_letter = st.session_state.get("show_cover_letter", False)
    
    # Hero Header with Gradient - Centered and Enhanced


    # =============================================================================
    # INPUT COLUMNS: JD | CV | Project (optional) | Cover Letter (optional)
    # CSS handles responsive wrap to 2x2 when sidebar is open
    # =============================================================================
    
    # Calculate columns needed
    num_cols = 2  # JD + CV (base)
    if show_project_eval: num_cols += 1
    if show_cover_letter: num_cols += 1
    
    # Create input container with custom class for CSS targeting
    st.markdown('<div class="input-columns-container">', unsafe_allow_html=True)
    
    # Create columns
    if num_cols == 2:
        col_jd, col_cv = st.columns(2)
    elif num_cols == 3:
        col_jd, col_cv, col3 = st.columns(3)
    else:  # 4 columns
        col_jd, col_cv, col3, col4 = st.columns(4)
    
    # Column 1: Job Description (always first)
    jd = ""
    with col_jd:
        st.markdown("### Job Description")
        input_type_jd = st.radio("Format", ["Text", "PDF"], key="jd_input", horizontal=True, label_visibility="collapsed")
        if input_type_jd == "Text":
            jd = st.text_area("JD Content", height=250, key="jd_text", placeholder="Paste job description here...", label_visibility="collapsed")
        else:
            uploaded_jd = st.file_uploader("Upload PDF", type=["pdf"], key="jd_pdf", label_visibility="collapsed")
            if uploaded_jd:
                try: jd = ml_utils.extract_text_from_pdf(uploaded_jd)
                except Exception as e: st.error(f"PDF Error: {e}")
    
    # Column 2: CV (always second)
    cv = ""
    with col_cv:
        st.markdown("### Your CV")
        input_type_cv = st.radio("Format", ["Text", "PDF"], key="cv_input", horizontal=True, label_visibility="collapsed")
        if input_type_cv == "Text":
            cv = st.text_area("CV Content", height=250, key="cv_text", placeholder="Paste your CV here...", label_visibility="collapsed")
        else:
            uploaded_cv = st.file_uploader("Upload PDF", type=["pdf"], key="cv_pdf", label_visibility="collapsed")
            if uploaded_cv:
                try: cv = ml_utils.extract_text_from_pdf(uploaded_cv)
                except Exception as e: st.error(f"PDF Error: {e}")
    
    # Column 3: Project Context (if enabled)
    project_text = ""
    if show_project_eval:
        proj_col = col3 if num_cols >= 3 else None
        if proj_col:
            with proj_col:
                st.markdown("### Project Context")
                input_type_proj = st.radio("Format", ["Text", "PDF"], key="proj_input", horizontal=True, label_visibility="collapsed")
                if input_type_proj == "Text":
                    project_text = st.text_area("Project Content", height=250, key="proj_text", placeholder="Describe your projects here...", label_visibility="collapsed")
                else:
                    uploaded_proj = st.file_uploader("Upload PDF", type=["pdf"], key="proj_pdf", label_visibility="collapsed")
                    if uploaded_proj:
                        try: project_text = ml_utils.extract_text_from_pdf(uploaded_proj)
                        except Exception as e: st.error(f"PDF Error: {e}")
    
    # Column 4: Cover Letter (if enabled)
    cover_letter_text = ""
    if show_cover_letter:
        cl_col = col4 if num_cols == 4 else (col3 if num_cols == 3 and not show_project_eval else None)
        if cl_col:
            with cl_col:
                st.markdown("### Cover Letter")
                input_type_cl = st.radio("Format", ["Text", "PDF"], key="cl_input", horizontal=True, label_visibility="collapsed")
                if input_type_cl == "Text":
                    cover_letter_text = st.text_area("CL Content", height=250, key="cl_text", placeholder="Paste your cover letter here...", label_visibility="collapsed")
                else:
                    uploaded_cl = st.file_uploader("Upload PDF", type=["pdf"], key="cl_pdf", label_visibility="collapsed")
                    if uploaded_cl:
                        try: cover_letter_text = ml_utils.extract_text_from_pdf(uploaded_cl)
                        except Exception as e: st.error(f"PDF Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # =============================================================================
    # ANALYZE BUTTON: Trigger for processing
    # =============================================================================
    st.markdown("")  # Spacing
    
    # Action buttons row
    col_btn1, col_btn2 = st.columns([3, 1])
    
    with col_btn1:
        analyze_clicked = st.button("Analyze Profile", type="primary", use_container_width=True)
    
    with col_btn2:
        if st.button("Clear All", use_container_width=True):
            # No demo_mode to reset here
            st.session_state["last_results"] = None
            # Clear all text and files
            for key in ["cv_text", "jd_text", "proj_text", "cl_text", "cv_pdf", "jd_pdf", "proj_pdf", "cl_pdf"]:
                if key in st.session_state:
                    st.session_state[key] = "" if "text" in key else None
            st.rerun()
    
    if analyze_clicked:
        # Input validation
        if not cv or not jd:
            st.error("Please provide both your CV and the Job Description to continue.")
            return

        # Progress bar with stages
        progress_bar = st.progress(0, text="Initializing analysis...")
        
        # Stage 1: Skill Extraction
        progress_bar.progress(20, text="Extracting skills from documents...")
        
        # CV vs JD Analysis (with or without projects)
        if show_project_eval and project_text:
            progress_bar.progress(40, text="Analyzing project portfolio...")
            res = ml_utils.analyze_gap_with_project(cv, jd, project_text)
        else:
            res = ml_utils.analyze_gap(cv, jd)
        
        # Stage 2: Analisi Cover Letter (se abilitata)
        cl_analysis = None
        if show_cover_letter and cover_letter_text:
            progress_bar.progress(60, text="Evaluating cover letter...")
            cl_analysis = ml_utils.analyze_cover_letter(cover_letter_text, jd, cv)
        
        # Stage 3: Generazione insights
        progress_bar.progress(80, text="Generating career insights...")
        
        # Salva risultati in session_state per persistenza
        st.session_state["last_results"] = res
        st.session_state["last_cv_text"] = cv
        st.session_state["last_jd_text"] = jd
        st.session_state["last_cl_analysis"] = cl_analysis
        
        # Completato!
        progress_bar.progress(100, text="Analysis complete.")
        
        # Breve pausa per mostrare completamento
        import time
        time.sleep(0.5)
        progress_bar.empty()
        
        # Messaggio di successo
        st.success("Analysis complete. Scroll down to see your personalized career insights.")
             
    # Mostra risultati (recuperati dalla session state per persistenza durante interaction)
    if st.session_state.get("last_results") is not None:
        render_results(
            st.session_state["last_results"], 
            st.session_state.get("last_jd_text"), 
            st.session_state.get("last_cv_text"), 
            st.session_state.get("last_cl_analysis")
        )

# =============================================================================
# VISUALIZZAZIONE RISULTATI ANALISI
# =============================================================================
# Riferimento corso: "Knowledge Presentation" (KDD Step 7)
#
# Questa funzione presenta i risultati del Data Mining in modo visuale:
# - Match Score: percentuale di compatibilità CV-JD
# - Skill Analysis: skill matched, missing, transferable
# - Cover Letter Analysis: valutazione lettera motivazionale
# - Learning Path: suggerimenti di apprendimento
# - Career Compass: ruoli alternativi suggeriti
# - Export: generazione report PDF
# =============================================================================

def render_results(res, jd_text=None, cv_text=None, cl_analysis=None):
    """
    BALANCED RESULTS VIEW
    =====================
    Score + Skills visible, extras in expanders.
    """
    st.divider()
    pct = res["match_percentage"]
    
    # --- SCORE SECTION (Visible) ---
    col_gauge, col_stats = st.columns([1.5, 2.5])
    
    with col_gauge:
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            number={'suffix': '%', 'font': {'size': 40, 'color': '#ffffff'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#30363d"},
                'bar': {'color': "#00A0DC"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 0,
                'steps': [{'range': [0, 100], 'color': '#0d1117'}],
                'threshold': {'line': {'color': "#00A0DC", 'width': 4}, 'thickness': 0.75, 'value': pct}
            }
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=30, b=10, l=30, r=30),
            height=180,
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Assessment
        if pct >= 80:
            st.markdown("<div style='text-align: center;'><h3 style='margin:0; color:#00C853;'>Excellent Match</h3></div>", unsafe_allow_html=True)
        elif pct >= 60:
            st.markdown("<div style='text-align: center;'><h3 style='margin:0; color:#00A0DC;'>Good Potential</h3></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center;'><h3 style='margin:0; color:#FFB300;'>Growth Opportunity</h3></div>", unsafe_allow_html=True)

    with col_stats:
        st.subheader("Analysis Overview")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Matched", len(res["matching_hard"]))
        with m2:
            st.metric("Missing", len(res["missing_hard"]))
        with m3:
            st.metric("Bonus", len(res["extra_hard"]))
        
        if res["missing_hard"]:
            st.markdown(f"**Priority:** Learn **{', '.join(list(res['missing_hard'])[:3])}**")
            
        # SENIORITY CHECK
        seniority = res.get('seniority_info', {})
        if seniority:
            match_status = seniority.get('match_status')
            cv_lvl = seniority.get('cv_level')
            jd_lvl = seniority.get('jd_level')
            
            if match_status == "Underqualified":
                st.error(f"⚠️ **Seniority Mismatch**: Role seems **{jd_lvl}**, but your profile matches **{cv_lvl}**.")
            elif match_status == "Overqualified":
                st.warning(f"⚠️ **Seniority Mismatch**: You appear **Overqualified** ({cv_lvl}) for this **{jd_lvl}** role.")
            else:
                 st.caption(f"🎯 **Seniority Analysis**: Your level ({cv_lvl}) aligns with the role requirements ({jd_lvl}).")

    
    st.divider()
    
    # --- SKILLS (Visible) ---
    st.subheader("Skills Analysis")
    
    if res["matching_hard"]:
        st.markdown("**Matched:**")
        matched_html = " ".join([f"<span class='skill-tag-matched'>{s}</span>" for s in sorted(res["matching_hard"])])
        st.markdown(matched_html, unsafe_allow_html=True)
    
    transferable = res.get("transferable", {})
    if transferable:
        st.markdown("**Transferable:**")
        transfer_html = " ".join([f"<span class='skill-tag-transferable' title='Covered by: {', '.join(p) if isinstance(p, list) else p}'>{str(m).split('←')[0].strip()}</span>" for m, p in transferable.items()])
        st.markdown(transfer_html, unsafe_allow_html=True)
    
    if res["missing_hard"]:
        st.markdown("**Missing:**")
        missing_html = " ".join([f"<span class='skill-tag-missing'>{s}</span>" for s in sorted(res["missing_hard"])])
        st.markdown(missing_html, unsafe_allow_html=True)
    
    if res["extra_hard"]:
        st.markdown("**Bonus:**")
        bonus_html = " ".join([f"<span class='skill-tag-bonus'>+ {s}</span>" for s in sorted(res["extra_hard"])])
        st.markdown(bonus_html, unsafe_allow_html=True)
    
    st.divider()
    
    # --- SOFT SKILLS & INTERVIEW (New Section) ---
    st.subheader("Human Factors & Interview Verification")
    st.caption("Soft skills are evaluated through behavioral questions rather than strict matching.")
    
    c_soft1, c_soft2 = st.columns(2)
    
    with c_soft1:
        st.markdown("**Stated Strengths (from CV):**")
        stated = res.get("soft_stated_strengths", [])
        if stated:
            stated_html = " ".join([f"<span class='skill-tag-bonus'>{s}</span>" for s in sorted(stated)])
            st.markdown(stated_html, unsafe_allow_html=True)
        else:
            st.caption("No explicit soft skills detected in CV.")
            
    with c_soft2:
        st.markdown("**Discussion Points (for Interview):**")
        discussion = res.get("soft_discussion_points", [])
        if discussion:
            discussion_html = " ".join([f"<span class='skill-tag-transferable'>{s}</span>" for s in sorted(discussion)])
            st.markdown(discussion_html, unsafe_allow_html=True)
        else:
            st.caption("All JD-requested soft skills are mentioned in your CV.")

    st.divider()

    # --- JOB CONTEXT ANALYSIS (Moved Up) ---
    if jd_text:
        st.subheader("Job Context Analysis")
        jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
        if len(jd_corpus) > 5:
            result = ml_utils.perform_topic_modeling(jd_corpus)
            if result:
                # Use a cleaner card layout
                with st.container():
                     c_summary, c_topics = st.columns([2, 1])
                     with c_summary:
                         st.markdown("##### Role Summary")
                         st.info(result['summary'])
                     
                     with c_topics:
                         st.markdown("##### Key Themes")
                         for topic in result['topics'][:3]:
                             # Extract just the title part before ":"
                             if ":" in topic:
                                 short_topic = topic.split(":")[0]
                                 desc = topic.split(":")[1]
                                 st.markdown(f"**{short_topic}**")
                                 st.caption(desc.strip())
                             else:
                                 st.markdown(f"- {topic}")
        else:
            st.caption("Job Description too brief for deep analysis.")
    
    st.divider()
    
    # --- AI CAREER COMPASS (Unified Logic) ---
    st.subheader("AI Career Compass")
    st.caption("Alternative roles based on your profile and education")
    
    # Call Unified Discovery Engine
    recs = ml_utils.discover_careers(cv_text=cv_text if cv_text else "")
    
    # Optional Filter
    match_range = st.radio(
        "Score Range",
        options=["0-25%", "25-50%", "50-75%", "75-100%"],
        horizontal=True,
        label_visibility="collapsed",
        key="compass_filter_range",
        index=2 # Default to 50-75% for realism
    )
    
    # Filter logic
    min_score, max_score = 0, 100
    if match_range == "0-25%": min_score, max_score = 0, 25
    elif match_range == "25-50%": min_score, max_score = 25, 50
    elif match_range == "50-75%": min_score, max_score = 50, 75
    elif match_range == "75-100%": min_score, max_score = 75, 100

    filtered_recs = [r for r in recs if min_score <= r['score'] <= max_score]
    
    if filtered_recs:
        # Display in 2 columns
        col1, col2 = st.columns(2)
        for i, rec in enumerate(filtered_recs[:6]): # Show top 6 results
            with col1 if i % 2 == 0 else col2:
                with st.container(border=True):
                    # Header: Role + Score Badge
                    c_head, c_badge = st.columns([3, 1])
                    with c_head:
                        role_title = rec['role']
                        st.markdown(f"**{role_title}**")
                        if rec.get('category'):
                            st.caption(f"{rec['category']}")
                    with c_badge:
                        score_color = "#00C853" if rec['score'] >= 70 else "#FFB300" if rec['score'] >= 50 else "#E53935"
                        st.markdown(f"<div style='text-align: right; font-weight: bold; color: {score_color};'>{rec['score']:.0f}%</div>", unsafe_allow_html=True)
                    
                    # Visual Progress Bar
                    st.progress(int(rec['score']))
                    
                    # Missing Skills Line
                    if rec.get('missing_skills'):
                        missing = sorted(list(rec['missing_skills']))[:3]
                        st.caption(f"Missing: {', '.join(missing)}")
                    
                    # Links
                    role_query = urllib.parse.quote(f"{rec['role']}")
                    st.markdown(f"""
                    <div style="display: flex; gap: 10px; font-size: 0.8em; margin-top: 8px;">
                        <a href="https://www.google.com/search?q={role_query}+jobs" target="_blank" style="text-decoration: none;">Google</a>
                        <span style="color: #30363d;">|</span>
                        <a href="https://www.linkedin.com/jobs/search/?keywords={role_query}" target="_blank" style="text-decoration: none;">LinkedIn</a>
                    </div>
                    """, unsafe_allow_html=True)
    elif recs:
        st.info(f"No roles found in the {match_range} range. Try lower ranges.")
    else:
        st.info("No alternative roles found. Try adding more detail to your CV.")
    
    st.divider()

    # --- EXTRAS IN EXPANDERS (Moved Down) ---
    
    # Project Tips
    if "project_verified" in res and res["project_verified"]:
        with st.expander("Project Interview Coaching", expanded=False):
            verified = set(res.get('project_verified', set()))
            matching = set(res.get('matching_hard', set()))
            missing = set(res.get('missing_hard', set()))
            
            c1, c2 = st.columns(2)
            
            with c1:
                st.markdown("##### Highlights")
                st.caption("Skills you've proven in projects")
                if verified:
                    # Create badges
                    html_tags = " ".join([f"<span class='skill-tag-matched'>{s}</span>" for s in list(verified)[:5]])
                    st.markdown(html_tags, unsafe_allow_html=True)
                else:
                    st.caption("No verified skills found.")

            with c2:
                st.markdown("##### Caution Areas")
                st.caption("Required skills not in your projects")
                if missing:
                    html_tags = " ".join([f"<span class='skill-tag-missing'>{s}</span>" for s in list(missing)[:3]])
                    st.markdown(html_tags, unsafe_allow_html=True)
                else:
                    st.caption("No major gaps!")

            st.divider()
            
            overlap = verified.intersection(matching)
            if overlap:
                 st.markdown(f"**Pro Tip:** Use your experience with **{', '.join(list(overlap)[:2])}** to answer behavioral questions.")

    
    # Cover Letter
    if cl_analysis:
        with st.expander("Cover Letter Analysis"):
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Keywords", f"{cl_analysis['hard_coverage']:.0f}%")
            with m2:
                st.metric("Soft Skills", f"{cl_analysis['soft_coverage']:.0f}%")
            with m3:
                st.metric("Structure", f"{cl_analysis['structure_score']:.0f}%")
            with m4:
                st.metric("Personal", f"{cl_analysis['personalization_score']:.0f}%")
            
            if cl_analysis.get('strengths'):
                st.markdown("**Strengths:** " + "; ".join(cl_analysis['strengths'][:2]))
            if cl_analysis.get('improvements'):
                st.markdown("**Improve:** " + "; ".join(cl_analysis['improvements'][:2]))
    
    # Learning Resources
    if res["missing_hard"]:
        with st.expander("Learning Resources"):
            for skill in list(res["missing_hard"])[:5]:
                q = urllib.parse.quote(skill)
                st.markdown(f"**{skill}:** [Coursera](https://www.coursera.org/search?query={q}) | [YouTube](https://www.youtube.com/results?search_query={q}+tutorial)")
    
    st.divider()
    with st.expander("Export Report"):
        report_text = ml_utils.generate_detailed_report_text(res, jd_text if jd_text else "", cl_analysis)
        report_pdf = ml_utils.generate_pdf_report(res, jd_text if jd_text else "", cl_analysis)
        
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button("Download TXT", report_text, file_name="Report.txt", mime="text/plain", use_container_width=True)
        with col_dl2:
            if report_pdf:
                st.download_button("Download PDF", report_pdf, file_name="Report.pdf", mime="application/pdf", use_container_width=True)

# =============================================================================
# RUBEN AI ASSISTANT - Sidebar Integration
# =============================================================================

def render_chatbot():
    """
    Renders Ruben AI Assistant at the bottom of the sidebar.
    """
    # 1. Initialize State
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    
    current_page = st.session_state.get("page", "Landing")

    # Define Callback to process chat
    def process_chat():
        user_msg = st.session_state.get("chat_input_widget", "")
        if user_msg:
            # Append User Message
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            # Get response
            response = ml_utils.get_chatbot_response(user_msg, current_page)
            st.session_state["chat_history"].append({"role": "assistant", "content": response})
            # Clear Input safely
            st.session_state["chat_input_widget"] = ""

    st.markdown('<div class="sidebar-chat-container">', unsafe_allow_html=True)
    
    # Signaling
    st.markdown('<div class="sidebar-chat-cta">Professional Assistant</div>', unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="sidebar-chat-header">
        <span>Ruben AI Consultant</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Message Area
    st.markdown('<div class="sidebar-chat-messages">', unsafe_allow_html=True)
    
    # Only show the latest assistant response or the welcome message
    # We filter out user messages to keep it clean as requested
    assistant_messages = [m for m in st.session_state["chat_history"] if m["role"] == "assistant"]

    if not assistant_messages:
        st.markdown(f"""
        <div class="sidebar-chat-message assistant">
            Hello. I am Ruben. How can I assist you with the <b>{current_page}</b> section today?
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show only the last assistant response to keep sidebar uncluttered
        last_msg = assistant_messages[-1]["content"]
        st.markdown(f'<div class="sidebar-chat-message assistant">{last_msg}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input Area - Using a simple text input with callback
    st.text_input(
        "Ask Ruben...", 
        key="chat_input_widget", 
        label_visibility="collapsed", 
        placeholder="Type a message...",
        on_change=process_chat
    )

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    elif st.session_state["page"] == "CV Builder":
        render_cv_builder()
    elif st.session_state["page"] == "CV Evaluation":
        render_evaluation_page()
    elif st.session_state["page"] == "Career Discovery":
        render_career_discovery()
    else:
        render_landing_page()
