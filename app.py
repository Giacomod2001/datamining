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
import constants
import ml_utils
import urllib.parse
import styles

# =============================================================================
# PULIZIA CACHE
# =============================================================================
# Puliamo la cache all'avvio per garantire che le costanti siano ricaricate
# Questo è importante quando constants.py viene aggiornato

st.cache_data.clear()
st.cache_resource.clear()

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
    page_icon="briefcase",
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
    st.session_state["page"] = "Home"
if "demo_mode" not in st.session_state:
    st.session_state["demo_mode"] = False

# =============================================================================
# DEBUGGER / CONSOLE SVILUPPATORE
# =============================================================================
# Questa sezione mostra il "dietro le quinte" degli algoritmi ML.
# Utile per:
# - Capire come funzionano i modelli
# - Verificare i risultati dell'analisi
# - Esplorare la Knowledge Base
# =============================================================================

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
    
    # Header con pulsante per tornare all'app
    col_back, col_title = st.columns([1, 5])
    with col_back:
        st.markdown("<div style='padding-top: 0.5rem;'></div>", unsafe_allow_html=True)
        if st.button("← Back to App"):
            st.session_state["page"] = "Home"
            st.rerun()
    with col_title:
        st.markdown("""
        <h1 style='margin: 0; padding: 0;'>Developer Console</h1>
        <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>Advanced analytics and system diagnostics</p>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Recupera risultati analisi se disponibili
    res = st.session_state.get("last_results", None)
    cv_text = st.session_state.get("last_cv_text", "")
    jd_text = st.session_state.get("last_jd_text", "")
    
    # Tab principali - nomi brevi per evitare troncamento "... and 1 more"
    tabs = ["System", "Analysis", "Clusters", "NLP", "Knowledge"]
    t1, t2, t3, t4, t5 = st.tabs(tabs)
    
    # =========================================================================
    # TAB 1: SYSTEM OVERVIEW - Collapsible Sections with Index
    # =========================================================================
    with t1:
        st.subheader("Machine Learning Models")
        st.caption("Click each section to expand/collapse. All algorithms used in this application.")
        
        # Quick Index
        st.markdown("""
        <div style='background: rgba(0, 119, 181, 0.1); padding: 0.75rem 1rem; border-radius: 8px; margin-bottom: 1rem;'>
            <strong>Quick Index:</strong> 
            Skill Matching | 
            Skill Extraction | 
            Entity Extraction |
            Topic Discovery | 
            Skill Grouping |
            Why These Parameters
        </div>
        """, unsafe_allow_html=True)
        
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
            hard_skills_count = len(constants.HARD_SKILLS)
            soft_skills_count = len(constants.SOFT_SKILLS)
            inference_count = len(constants.INFERENCE_RULES)
            cluster_count = len(constants.SKILL_CLUSTERS)
            total_variations = sum(len(v) for v in constants.HARD_SKILLS.values()) + sum(len(v) for v in constants.SOFT_SKILLS.values())
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
            if st.button("Reset Demo Mode", use_container_width=True):
                st.session_state["demo_mode"] = False
                st.success("Demo mode reset!")
    
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
                        st.caption("These skills directly match job requirements")
                        st.write(sorted(res["matching_hard"]))
                    else:
                        st.caption("No direct matches found")
                
                with st.expander(f"Missing Skills ({missing_count})", expanded=False):
                    if res["missing_hard"]:
                        st.caption("Priority skills to develop")
                        st.write(sorted(res["missing_hard"]))
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
                        for missing, present in res["transferable"].items():
                            st.markdown(f"**{missing}** ← *{present}*")
            
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
            <strong>2. K-Means Clustering:</strong> Skills are grouped by similarity. The algorithm finds natural groupings 
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
                    with st.expander("Hierarchical Dendrogram"):
                        st.caption("Tree structure showing how skills relate. Skills that branch together are similar.")
                        st.image(dendro_path, caption="Ward's Linkage Clustering")
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
            cv_sentences = cv_text.count('.') + cv_text.count('!') + cv_text.count('?')
            jd_sentences = jd_text.count('.') + jd_text.count('!') + jd_text.count('?')
            
            stat1, stat2, stat3, stat4 = st.columns(4)
            with stat1:
                st.metric("CV Words", cv_words)
            with stat2:
                st.metric("JD Words", jd_words)
            with stat3:
                st.metric("CV Sentences", cv_sentences)
            with stat4:
                st.metric("JD Sentences", jd_sentences)
            
            st.markdown("")
            
            # =============================================
            # Row 2: Skill Extraction Breakdown
            # =============================================
            st.markdown("### Skill Extraction Analysis")
            
            cv_hard, cv_soft = ml_utils.extract_skills_from_text(cv_text)
            jd_hard, jd_soft = ml_utils.extract_skills_from_text(jd_text)
            
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
        
        kb_tab1, kb_tab2, kb_tab3 = st.tabs(["Inference Rules", "Skill Clusters", "Training Data"])
        
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
            st.markdown("**ML Training Data:** Sample data used to train the Random Forest classifier.")
            _, df = ml_utils.train_rf_model()
            st.dataframe(df, use_container_width=True, hide_index=True)

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

def render_home():
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
    
    # =========================================================================
    # SIDEBAR - Controlli e Navigazione
    # =========================================================================
    with st.sidebar:
        # Header con branding
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='font-size: 1.8rem; margin-bottom: 0.2rem;'>CareerMatch AI</h1>
            <p style='color: #00A0DC; font-size: 0.9rem; font-weight: 600;'>Smart Career Analytics Platform</p>
            <p style='color: #8b949e; font-size: 0.75rem;'>v2.0 - Powered by Machine Learning</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Modalità Demo - Carica dati di esempio per test rapido
        st.markdown("### Quick Start")
        
        col_demo1, col_demo2 = st.columns(2)
        with col_demo1:
            if st.button("Try Demo", use_container_width=True, help="Load sample CV and Job Description to see the app in action"):
                st.session_state["demo_mode"] = True
                # Force update the text area values in session state
                st.session_state["cv_text"] = styles.get_demo_cv()
                st.session_state["jd_text"] = styles.get_demo_jd()
                # Also load project and cover letter demos
                st.session_state["proj_text"] = styles.get_demo_project()
                st.session_state["cl_text"] = styles.get_demo_cover_letter()
                # Enable the toggles so user sees the full demo
                st.session_state["show_project_toggle"] = True
                st.session_state["show_cl_toggle"] = True
                st.rerun()
        with col_demo2:
            if st.session_state.get("demo_mode"):
                if st.button("Reset", use_container_width=True):
                    st.session_state["demo_mode"] = False
                    # Clear all text areas
                    st.session_state["cv_text"] = ""
                    st.session_state["jd_text"] = ""
                    st.session_state["proj_text"] = ""
                    st.session_state["cl_text"] = ""
                    # Reset toggles
                    st.session_state["show_project_toggle"] = False
                    st.session_state["show_cl_toggle"] = False
                    st.rerun()
        
        if st.session_state.get("demo_mode"):
            st.success("Demo mode active. Sample data loaded below.")
        
        # --- RESULTS NAVIGATOR (appears after analysis) ---
        if st.session_state.get("last_results"):
            st.divider()
            st.markdown("### Results Navigator")
            st.caption("Click to jump to section")
            
            res = st.session_state["last_results"]
            cl_analysis = st.session_state.get("last_cl_analysis")
            
            # Navigation using direct anchor links (simpler, more reliable)
            st.markdown("""
            <style>
            .sidebar-nav a {
                display: block;
                padding: 0.4rem 0.6rem;
                margin: 0.2rem 0;
                background: rgba(0, 119, 181, 0.15);
                border-radius: 6px;
                color: #00A0DC !important;
                text-decoration: none;
                font-size: 0.85rem;
            }
            .sidebar-nav a:hover {
                background: rgba(0, 119, 181, 0.3);
            }
            </style>
            <div class="sidebar-nav">
            """, unsafe_allow_html=True)
            
            # Build navigation items
            nav_sections = [
                ("Match Score", "section-score"),
                ("Skills Analysis", "section-skills"),
            ]
            if res.get("project_verified"):
                nav_sections.append(("Project Coaching", "section-projects"))
            if cl_analysis:
                nav_sections.append(("Cover Letter", "section-cover"))
            if res.get("missing_hard"):
                nav_sections.append(("Learning Path", "section-learning"))
            nav_sections.extend([
                ("Job Context", "section-context"),
                ("AI Compass", "section-compass"),
                ("Export", "section-export"),
            ])
            
            # Render all links
            links_html = "".join([f"<a href='#{anchor}'>{name}</a>" for name, anchor in nav_sections])
            st.markdown(links_html + "</div>", unsafe_allow_html=True)
        
        st.divider()
        
        # How It Works
        with st.expander("How It Works", expanded=False):
            st.markdown("""
            **1. Upload Your CV**
            - PDF or paste text directly
            - AI extracts 620+ skill types automatically
            
            **2. Add the Job Description**  
            - Copy from any job board
            - We analyze what the company really needs
            
            **3. Click Analyze**
            - Instant skill matching
            - Transferable skills recognition
            - Compatibility score
            
            **4. Explore Results**
            - Personalized learning path
            - Alternative role suggestions
            - Interview talking points
            """)
        
        st.divider()
        
        # Optional Features Section
        st.markdown("### Analysis Options")
        
        # Initialize toggle states if not present
        if "show_project_toggle" not in st.session_state:
            st.session_state["show_project_toggle"] = False
        if "show_cl_toggle" not in st.session_state:
            st.session_state["show_cl_toggle"] = False
        
        show_project_eval = st.toggle(
            "Project Evaluation", 
            key="show_project_toggle",
            help="Upload project descriptions to verify skills through your portfolio. Increases match score when projects demonstrate missing skills."
        )
        
        show_cover_letter = st.toggle(
            "Cover Letter Analysis", 
            key="show_cl_toggle",
            help="Get AI feedback on keyword coverage, structure, and personalization of your application letter."
        )
        
        st.divider()
        
        # Skills Legend - Compact & Visual
        with st.expander("Skills Legend", expanded=True):
            st.markdown("""
            <div style='line-height: 2;'>
                <span class='skill-tag-matched' style='font-size: 0.8em;'>Matched</span> Direct skill match<br>
                <span class='skill-tag-transferable' style='font-size: 0.8em;'>Transfer</span> Similar skill found<br>
                <span class='skill-tag-project' style='font-size: 0.8em;'>Project</span> Portfolio verified<br>
                <span class='skill-tag-missing' style='font-size: 0.8em;'>Missing</span> Gap to fill<br>
                <span class='skill-tag-bonus' style='font-size: 0.8em;'>Bonus</span> Extra advantage
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        # Developer Mode - Hidden by Default
        if st.toggle("Developer Mode", help="Access debugging tools and analytics internals"):
            pwd = st.text_input("Password", type="password", key="dev_pwd", placeholder="Enter dev password")
            if pwd == "1234":
                if st.button("Open Debugger", use_container_width=True):
                    st.session_state["page"] = "Debugger"
                    st.rerun()
            elif pwd:
                st.error("Wrong password")
        
        # Footer
        st.divider()
        st.markdown("""
        <div style='text-align: center; color: #8b949e; font-size: 0.75rem;'>
            CareerMatch AI<br>
            <a href='https://github.com/Giacomod2001/datamining' style='color: #00A0DC;'>GitHub</a> | 
            <a href='https://dataminingiulm.streamlit.app/' style='color: #00A0DC;'>Live Demo</a>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================================================
    # MAIN CONTENT AREA - Hero Section
    # ==========================================================================
    
    # Hero Header with Gradient - Centered and Enhanced
    st.markdown("""
    <div class='hero-gradient'>
        <h1 style='margin: 0; font-size: 2.5rem; font-weight: 700;'>CareerMatch AI</h1>
        <p style='font-size: 1.2rem; color: #00A0DC; margin: 0.5rem 0; font-weight: 600;'>
            AI-Powered CV-to-Job Matching
        </p>
        <p style='color: #8b949e; font-size: 0.95rem; max-width: 600px; margin: 0.5rem auto 1rem auto;'>
            Upload your CV and job description to discover your compatibility level,
            transferable skills, and a personalized action plan
        </p>
        <div style='display: flex; justify-content: center; gap: 2rem; margin-top: 1rem; flex-wrap: wrap;'>
            <div style='text-align: center;'>
                <div style='font-size: 1.5rem; font-weight: bold; color: #00A0DC;'>620+</div>
                <div style='font-size: 0.75rem; color: #6e7681;'>Skills Analyzed</div>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 1.5rem; font-weight: bold; color: #00C853;'>85%</div>
                <div style='font-size: 0.75rem; color: #6e7681;'>Match Accuracy</div>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 1.5rem; font-weight: bold; color: #FFB300;'>5 sec</div>
                <div style='font-size: 0.75rem; color: #6e7681;'>Analysis Time</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            st.session_state["demo_mode"] = False
            st.session_state["last_results"] = None
            st.rerun()
    
    if analyze_clicked:
        # Input validation
        if not cv or not jd:
            st.error("Please provide both your CV and the Job Description to continue.")
            st.info("Tip: Click 'Try Demo' in the sidebar to see the app in action with sample data.")
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
        
        # Salva risultati in session_state per il debugger
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
             
        # Mostra risultati
        render_results(res, jd, cv, cl_analysis)

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
    RENDERING RISULTATI ANALISI
    ============================
    Riferimento corso: "Knowledge Presentation" (KDD Step 7)
    
    Visualizza i pattern estratti dal Data Mining in modo comprensibile:
    - Grafici interattivi (Plotly)
    - Tag colorati per skill
    - Metriche percentuali
    - Suggerimenti azionabili
    """
    st.divider()
    pct = res["match_percentage"]
    
    # =========================================================================
    # NAVIGAZIONE SEZIONI
    # =========================================================================
    # Indice cliccabile per saltare alle sezioni - UX improvement
    
    nav_items = [
        ("Match Score", "section-score"),
        ("Skills Analysis", "section-skills"),
    ]
    
    # Conditional sections
    if cl_analysis:
        nav_items.append(("Cover Letter", "section-cover"))
    if res["missing_hard"]:
        nav_items.append(("Learning Path", "section-learning"))
    if jd_text:
        nav_items.append(("Job Context", "section-context"))
    
    nav_items.append(("AI Compass", "section-compass"))
    nav_items.append(("Export", "section-export"))
    
    # Build navigation HTML
    nav_links = " | ".join([f"<a href='#{anchor}' style='color: #00A0DC; text-decoration: none;'>{name}</a>" for name, anchor in nav_items])
    
    # Quick Navigation - Only shows when sidebar is collapsed
    # Uses CSS to detect sidebar state
    st.markdown(f"""
    <style>
    /* Hide in-content nav when sidebar is expanded */
    section[data-testid="stSidebar"][aria-expanded="true"] ~ section .quick-nav-inline {{
        display: none !important;
    }}
    /* Also hide when sidebar is in default expanded state */
    @media (min-width: 768px) {{
        .quick-nav-inline {{
            display: none !important;
        }}
    }}
    /* Show only on mobile or when sidebar collapsed */
    @media (max-width: 767px) {{
        .quick-nav-inline {{
            display: block !important;
        }}
    }}
    </style>
    <div class='quick-nav-inline' style='background: rgba(0, 119, 181, 0.1); padding: 0.75rem 1rem; border-radius: 8px; margin-bottom: 1rem; text-align: center;'>
        <strong>Quick Navigation:</strong> {nav_links}
    </div>
    """, unsafe_allow_html=True)

    # --- MAIN SCORE SECTION ---
    st.markdown("<div id='section-score'></div>", unsafe_allow_html=True)
    st.header("Analysis Results")
    
    # Row 1: Main Match Score (larger, more prominent)
    score_col1, score_col2 = st.columns([1, 2])
    
    with score_col1:
        # Clean Gauge Indicator
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            number={'suffix': '%', 'font': {'size': 48, 'color': '#ffffff'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#8b949e", 'tickfont': {'color': '#8b949e'}},
                'bar': {'color': "#00A0DC"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(239, 85, 59, 0.3)'},
                    {'range': [40, 70], 'color': 'rgba(255, 193, 7, 0.3)'},
                    {'range': [70, 100], 'color': 'rgba(0, 204, 150, 0.3)'}
                ],
                'threshold': {
                    'line': {'color': "#00cc96", 'width': 4},
                    'thickness': 0.8,
                    'value': pct
                }
            }
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=40, b=20, l=40, r=40),
            height=200,
            font={'color': '#ffffff'}
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with score_col2:
        st.subheader("Profile Match Assessment")
        st.markdown("")
        if pct >= 80:
            st.success("**Excellent Match!** Your profile is highly aligned with this role.")
            st.markdown("You have most required skills. Focus on highlighting your experience.")
        elif pct >= 60:
            st.warning("**Good Potential.** You have a solid foundation for this role.")
            st.markdown("Some gaps exist, but your transferable skills can bridge them.")
        else:
            st.error("**Significant Gap.** This role requires skills you're still developing.")
            st.markdown("Consider the learning path below to build missing competencies.")
        
        # Quick stats
        st.markdown("")
        stat1, stat2, stat3 = st.columns(3)
        stat1.metric("Matched", len(res["matching_hard"]))
        stat2.metric("Missing", len(res["missing_hard"]))
        stat3.metric("Bonus", len(res["extra_hard"]))
    
    # Row 2: Additional metrics (if present)
    if ("project_verified" in res and res["project_verified"]) or cl_analysis:
        st.markdown("")
        add_cols = st.columns(2)
        add_idx = 0
        
        if "project_verified" in res and res["project_verified"]:
            with add_cols[add_idx]:
                st.subheader("Portfolio Intelligence")
                
                # Portfolio Quality Score
                quality = res.get('portfolio_quality', 0)
                st.metric("Portfolio Score", f"{quality:.0f}%", 
                         help="Based on skill coverage, project complexity, and job relevance")
                
                # Verified Skills Count
                verified_list = list(res['project_verified'])
                st.caption(f"**{len(verified_list)} skills verified** through your projects")
                
                # Talking Points (most useful for interviews)
                talking_points = res.get('talking_points', [])
                if talking_points:
                    st.markdown("**Interview Talking Points:**")
                    for tp in talking_points[:3]:
                        st.markdown(f"- {tp}")
            add_idx += 1
    
    # --- DEDICATED PROJECT COACHING SECTION ---
    if "project_verified" in res and res["project_verified"]:
        st.divider()
        st.markdown("<div id='section-projects'></div>", unsafe_allow_html=True)
        st.subheader("Project Interview Coaching")
        st.caption("How to present your portfolio in interviews for this role")
        
        verified_skills = res.get('project_verified', set())
        missing_skills = res.get('missing_hard', set())
        matching_skills = res.get('matching_hard', set())
        
        pc1, pc2, pc3 = st.columns(3)
        
        # Build focus points
        focus_points = []
        if verified_skills:
            focus_points.append(f"Highlight: **{', '.join(list(verified_skills)[:3])}**")
        if matching_skills:
            overlap = verified_skills & matching_skills
            if overlap:
                focus_points.append(f"Emphasize overlap: **{', '.join(list(overlap)[:2])}**")
        focus_points.append("Quantify impact with metrics")
        focus_points.append("Explain your role & decisions")
        focus_points.append("Discuss challenges overcome")
        
        # Column 1: FOCUS ON - Personalized based on analysis
        with pc1:
            st.markdown("**FOCUS ON**", help="Specific strengths to highlight")
            focus_points = []
            
            # Highlight verified skills that match job requirements (most valuable!)
            overlap = verified_skills & matching_skills
            if overlap:
                focus_points.append(f"**Star projects**: {', '.join(list(overlap)[:2])} (verified + required)")
            
            # Skills verified by projects
            if verified_skills:
                other_verified = verified_skills - overlap if overlap else verified_skills
                if other_verified:
                    focus_points.append(f"Demonstrate: **{', '.join(list(other_verified)[:2])}**")
            
            # Specific advice based on match quality
            if res.get('match_percentage', 0) >= 70:
                focus_points.append("Lead with your strongest matching project")
            else:
                focus_points.append("Show learning trajectory and growth")
            
            # Add transferable skills angle
            transferable = res.get('transferable', {})
            if transferable:
                focus_points.append(f"Leverage transferable: **{list(transferable.keys())[0]}**")
            
            for point in focus_points[:4]:
                st.markdown(f"<span style='color: #00C853;'>•</span> {point}", unsafe_allow_html=True)
        
        # Column 2: AVOID - Personalized based on analysis
        with pc2:
            st.markdown("**AVOID**", help="Specific pitfalls for your situation")
            avoid_points = []
            
            # Personalized warnings based on analysis
            if missing_skills:
                top_missing = list(missing_skills)[:2]
                avoid_points.append(f"Don't claim **{', '.join(top_missing)}** without proof")
            
            # Check for skills in CV but not verified by projects
            unverified = matching_skills - verified_skills
            if unverified:
                avoid_points.append(f"Be ready to demo: **{', '.join(list(unverified)[:2])}**")
            
            # If match is low, warn about overselling
            if res.get('match_percentage', 0) < 50:
                avoid_points.append("Don't oversell - focus on learning ability")
            
            # Generic but useful if no specific issues
            if len(avoid_points) < 3:
                avoid_points.append("Vague descriptions without metrics")
            if len(avoid_points) < 4:
                avoid_points.append("Ignoring skill gaps - address them proactively")
            
            for point in avoid_points[:4]:
                st.markdown(f"<span style='color: #E53935;'>•</span> {point}", unsafe_allow_html=True)
        
        # Column 3: CONSIDER ADDING - Personalized project suggestions
        with pc3:
            st.markdown("**CONSIDER ADDING**", help="Specific projects to build")
            add_suggestions = []
            
            if missing_skills:
                for skill in list(missing_skills)[:3]:
                    # Specific project ideas per skill type
                    if skill in ["Machine Learning", "Deep Learning"]:
                        add_suggestions.append(f"Kaggle competition using **{skill}**")
                    elif skill in ["Data Science", "Statistics"]:
                        add_suggestions.append(f"End-to-end analysis project (**{skill}**)")
                    elif skill in ["Power BI", "Tableau", "Looker Studio"]:
                        add_suggestions.append(f"Public dashboard on **{skill}**")
                    elif skill in ["Python", "SQL", "R"]:
                        add_suggestions.append(f"GitHub repo with **{skill}** scripts")
                    elif skill in ["AWS", "GCP", "Azure"]:
                        add_suggestions.append(f"Deploy an app on **{skill}**")
                    elif skill in ["Docker", "Kubernetes"]:
                        add_suggestions.append(f"Containerize existing project (**{skill}**)")
                    else:
                        add_suggestions.append(f"Mini-project: **{skill}**")
            
            if not add_suggestions:
                # No missing skills - suggest enhancement
                add_suggestions.append("Add quantified case studies")
                add_suggestions.append("Document architecture decisions")
                if verified_skills:
                    add_suggestions.append(f"Deep-dive on **{list(verified_skills)[0]}**")
            
            for sugg in add_suggestions[:4]:
                st.markdown(f"<span style='color: #FFB300;'>•</span> {sugg}", unsafe_allow_html=True)
        
        if cl_analysis:
            with add_cols[add_idx] if add_idx < 2 else st.container():
                st.subheader("Cover Letter Assessment")
                cl_score = cl_analysis['overall_score']
                
                if cl_score >= 80:
                    st.success(f"**{cl_score:.0f}%** - Excellent cover letter!")
                elif cl_score >= 60:
                    st.warning(f"**{cl_score:.0f}%** - Good, with room for improvement")
                else:
                    st.error(f"**{cl_score:.0f}%** - Needs Work")
                
                st.caption(f"{cl_analysis['word_count']} words | {cl_analysis['language'] or 'EN'}")

    st.divider()
    st.markdown("<div id='section-skills'></div>", unsafe_allow_html=True)
    st.subheader("Technical Skills Analysis")
    st.caption("Breakdown of your skill alignment with this position")
    st.markdown("")  # Spacing

    # ==========================================================================
    # SKILL DISPLAY - Simple tag-based layout (no radar chart)
    # ==========================================================================
    
    # Matched Skills - Green tags
    if res["matching_hard"]:
        st.markdown("**Matched Skills:**")
        matched_html = " ".join([f"<span class='skill-tag-matched'>{skill}</span>" for skill in sorted(res["matching_hard"])])
        st.markdown(matched_html, unsafe_allow_html=True)
        st.markdown("")
    
    # Transferable Skills - Yellow tags with source
    transferable = res.get("transferable", {})
    if transferable:
        st.markdown("**Transferable Skills:**")
        st.caption("You have equivalent skills that match these requirements")
        transfer_tags = []
        for missing, present in transferable.items():
            transfer_tags.append(f"<span class='skill-tag-transferable'>{missing} ← <em>{present}</em></span>")
        st.markdown(" ".join(transfer_tags), unsafe_allow_html=True)
        st.markdown("")
    
    # Project-Verified Skills - Blue tags (FIXED: was using wrong key 'project_review')
    project_verified = res.get("project_verified", set())
    if project_verified:
        st.markdown("**Project-Verified Skills:**")
        st.caption("Skills demonstrated in your portfolio - highlight these in interviews")
        project_html = " ".join([f"<span class='skill-tag-project'>{skill}</span>" for skill in sorted(project_verified)])
        st.markdown(project_html, unsafe_allow_html=True)
        st.markdown("")
    
    # Missing Skills - Red tags
    if res["missing_hard"]:
        st.markdown("**Missing Skills:**")
        missing_html = " ".join([f"<span class='skill-tag-missing'>{skill}</span>" for skill in sorted(res["missing_hard"])])
        st.markdown(missing_html, unsafe_allow_html=True)
    else:
        st.success("No missing skills - Perfect match!")
    
    st.markdown("")
    
    # Bonus Skills - Gray tags
    if res["extra_hard"]:
        st.markdown("**Bonus Skills:**")
        st.caption("Additional skills that give you competitive advantage")
        bonus_html = " ".join([f"<span class='skill-tag-bonus'>+ {skill}</span>" for skill in sorted(res["extra_hard"])])
        st.markdown(bonus_html, unsafe_allow_html=True)

    st.divider()
    
    # --- COVER LETTER DETAILED ANALYSIS ---
    if cl_analysis:
        st.markdown("<div id='section-cover'></div>", unsafe_allow_html=True)
        st.subheader("Cover Letter Analysis")
        
        # Metrics Row
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Keyword Coverage", f"{cl_analysis['hard_coverage']:.0f}%", 
                     help="Technical skills from JD mentioned in your cover letter")
        with m2:
            st.metric("Soft Skills", f"{cl_analysis['soft_coverage']:.0f}%",
                     help="Soft skills from JD mentioned")
        with m3:
            st.metric("Structure", f"{cl_analysis['structure_score']:.0f}%",
                     help="Professional formatting (greeting, closing, paragraphs)")
        with m4:
            st.metric("Personalization", f"{cl_analysis['personalization_score']:.0f}%",
                     help="Specific examples and personal touch")
        
        # Feedback Columns
        fc1, fc2 = st.columns(2)
        
        with fc1:
            st.markdown("#### Strengths")
            if cl_analysis['strengths']:
                for strength in cl_analysis['strengths']:
                    st.markdown(strength)
            else:
                st.info("No specific strengths identified yet")
        
        with fc2:
            st.markdown("#### Improvements")
            if cl_analysis['improvements']:
                for improvement in cl_analysis['improvements']:
                    st.markdown(improvement)
            else:
                st.success("Great job! No major improvements needed")
        
        # Keywords Coverage Detail
        if cl_analysis['hard_mentioned'] or cl_analysis['hard_missing']:
            st.markdown("#### Technical Keywords Status")
            
            # Mentioned keywords as rounded tags (matching skill tag style)
            if cl_analysis['hard_mentioned']:
                st.markdown("**Mentioned in Cover Letter:**")
                mentioned_html = " ".join([f"<span class='skill-tag-matched'>{skill}</span>" for skill in sorted(cl_analysis['hard_mentioned'])])
                st.markdown(mentioned_html, unsafe_allow_html=True)
                st.markdown("")
            
            # Missing keywords as rounded tags
            if cl_analysis['hard_missing']:
                st.markdown("**Consider Adding:**")
                missing_list = sorted(list(cl_analysis['hard_missing'])[:15])
                missing_html = " ".join([f"<span class='skill-tag-transferable'>{skill}</span>" for skill in missing_list])
                st.markdown(missing_html, unsafe_allow_html=True)
                if len(cl_analysis['hard_missing']) > 15:
                    st.caption(f"... and {len(cl_analysis['hard_missing']) - 15} more")

    st.divider()

    # LEARNING PLAN
    if res["missing_hard"]:
        st.markdown("<div id='section-learning'></div>", unsafe_allow_html=True)
        st.subheader("Learning Actions")
        
        for skill in res["missing_hard"]:
            with st.expander(f"Action Plan: **{skill}**", expanded=len(res["missing_hard"]) == 1):
                q_skill = urllib.parse.quote(skill)
                
                lc1, lc2, lc3, lc4 = st.columns(4)
                with lc1:
                    st.markdown(f"<a href='https://www.coursera.org/search?query={q_skill}' target='_blank'><b>Coursera</b></a>", unsafe_allow_html=True)
                    st.caption("Free courses")
                with lc2:
                    st.markdown(f"<a href='https://www.udemy.com/courses/search/?q={q_skill}' target='_blank'><b>Udemy</b></a>", unsafe_allow_html=True)
                    st.caption("Paid courses")
                with lc3:
                    st.markdown(f"<a href='https://www.youtube.com/results?search_query=learn+{q_skill}+tutorial' target='_blank'><b>YouTube</b></a>", unsafe_allow_html=True)
                    st.caption("Free tutorials")
                with lc4:
                    st.markdown(f"<a href='https://www.linkedin.com/learning/search?keywords={q_skill}' target='_blank'><b>LinkedIn Learning</b></a>", unsafe_allow_html=True)
                    st.caption("Professional")

    # --- ADVANCED MINING MOVED TO DEBUGGER ---
    # The 'Advanced Data Mining', 'Topic Modeling', and 'NER' sections have been moved 
    # to the 'render_debug_page' function as requested to clean up the main view.

    # --- JOB CONTEXT ANALYSIS ---
    if jd_text:
        st.divider()
        st.markdown("<div id='section-context'></div>", unsafe_allow_html=True)
        st.subheader("What Does This Position Really Need?")
        
        jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
        
        if len(jd_corpus) > 5:
            result = ml_utils.perform_topic_modeling(jd_corpus)
            
            if result:
                # Show summary prominently
                st.info(result['summary'])
                
                # Show interpretations in columns
                st.markdown("#### Key Areas Required:")
                cols_topic = st.columns(len(result['topics']))
                for idx, (col, topic) in enumerate(zip(cols_topic, result['topics'])):
                    with col:
                        st.markdown(f"**Area {idx+1}**")
                        st.write(topic)
                
                # Show keywords as tags (rounded like other skill tags)
                st.markdown("#### Main Keywords:")
                keyword_html = " ".join([f"<span class='skill-tag-bonus'>{kw}</span>" for kw in result['keywords']])
                st.markdown(keyword_html, unsafe_allow_html=True)
        else:
            st.info("Job Description too brief for contextual analysis.")
    
    # --- JOB RECOMMENDER (AI Career Compass) ---
    st.divider()
    st.markdown("<div id='section-compass'></div>", unsafe_allow_html=True)
    st.subheader("AI Career Compass (Alternative Paths)")
    st.info("Based on your skill vector, here are the market roles that fit you best.")
    
    # Use all skills found in CV (Matched, Missing, Extra) to define the candidate vector
    candidate_skills = res["matching_hard"] | res["missing_hard"] | res["extra_hard"]
    
    # Pass JD Text to filter out the target role is redundant
    recs = ml_utils.recommend_roles(candidate_skills, jd_text if jd_text else "")
    
    if recs:
        rc1, rc2, rc3 = st.columns(3)
        cols = [rc1, rc2, rc3]
        for i, rec in enumerate(recs):
             with cols[i]:
                 st.markdown(f"##### {i+1}. {rec['role']}")
                 st.progress(int(rec['score']))
                 st.caption(f"**{rec['score']:.0f}% Similarity**")
                 
                 # Dynamic Links - Working Job Boards Only
                 role_query = urllib.parse.quote(rec['role'])
                 italy_query = urllib.parse.quote(f"{rec['role']} Italia")
                 
                 st.markdown(f"<a href='https://www.google.com/search?q={role_query}+jobs' target='_blank'>Google Jobs</a>", unsafe_allow_html=True)
                 st.markdown(f"<a href='https://www.linkedin.com/jobs/search/?keywords={role_query}' target='_blank'>LinkedIn Jobs</a>", unsafe_allow_html=True)
                 st.markdown(f"<a href='https://it.indeed.com/jobs?q={italy_query}' target='_blank'>Indeed Italia</a>", unsafe_allow_html=True)
                 
                 with st.expander("Missing Skills"):
                     for s in rec['missing'][:5]:
                         st.markdown(f"- {s}")
    else:
        st.info("**Quality Mode**: No alternative roles met the confidence threshold (>30%). Your profile is uniquely specialized.")

    # --- EXPORT REPORT ---
    st.divider()
    st.markdown("<div id='section-export'></div>", unsafe_allow_html=True)
    st.subheader("Export Comprehensive Report")
    st.caption("Download your complete analysis including CV match, skills, and cover letter evaluation")
    
    # Generate Detailed Content
    report_text = ml_utils.generate_detailed_report_text(res, jd_text if jd_text else "", cl_analysis)
    report_pdf = ml_utils.generate_pdf_report(report_text)
    
    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        st.download_button("Download Text Report", report_text, file_name="Job_Seeker_Report.txt", mime="text/plain", use_container_width=True)
    with col_dl2:
        if report_pdf:
            st.download_button("Download PDF Report", report_pdf, file_name="Job_Seeker_Report.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.warning("PDF Generation unavailable (fpdf missing).")

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
