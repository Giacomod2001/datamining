import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import constants
import ml_utils
import urllib.parse
import styles

# Clear cache on startup to ensure constants are reloaded
# This is important when constants.py is updated
st.cache_data.clear()
st.cache_resource.clear()

# =============================================================================
# PAGE CONFIG - v2.0 Premium Edition
# =============================================================================
st.set_page_config(
    page_title="Job Seeker Helper v2.0 - AI Career Analytics",
    page_icon="briefcase",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Premium CSS Theme
st.markdown(styles.get_premium_css(), unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "demo_mode" not in st.session_state:
    st.session_state["demo_mode"] = False

# =============================================================================
# DEBUGGER
# =============================================================================
def render_debug_page():
    """Developer/Debug mode with advanced analytics and system insights."""
    
    # Header with back button
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← Back to App"):
            st.session_state["page"] = "Home"
            st.rerun()
    with col_title:
        st.title("Developer Console")
        st.caption("Advanced analytics and system diagnostics")
    
    st.divider()
    
    # Get analysis results if available
    res = st.session_state.get("last_results", None)
    cv_text = st.session_state.get("last_cv_text", "")
    jd_text = st.session_state.get("last_jd_text", "")
    
    # Main tabs
    tabs = ["System Overview", "Analysis Data", "Skill Intelligence", "NLP Insights", "Knowledge Base"]
    t1, t2, t3, t4, t5 = st.tabs(tabs)
    
    # =========================================================================
    # TAB 1: SYSTEM OVERVIEW
    # =========================================================================
    with t1:
        # ML Models Used - Professional Header
        st.subheader("Machine Learning Models")
        st.caption("Algorithms used in this application")
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0, 119, 181, 0.15) 0%, rgba(0, 68, 113, 0.1) 100%); 
                    border-radius: 12px; padding: 1.5rem; border: 1px solid rgba(0, 119, 181, 0.3); margin-bottom: 1rem;'>
            <table style='width: 100%; color: #e0e6ed;'>
                <tr>
                    <td style='padding: 10px 0; width: 35%;'><strong>Skill Matching</strong></td>
                    <td>Random Forest Classifier - identifies skills from text</td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><strong>Entity Extraction</strong></td>
                    <td>NLTK NER - finds people, organizations, locations</td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><strong>Topic Discovery</strong></td>
                    <td>LDA (Latent Dirichlet Allocation) - extracts main themes</td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><strong>Skill Grouping</strong></td>
                    <td>K-Means Clustering - groups related skills together</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.subheader("System Status")
        
        # System metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Skills in Database", len(constants.SKILL_LIST) if hasattr(constants, 'SKILL_LIST') else "N/A")
        with m2:
            st.metric("Inference Rules", len(constants.INFERENCE_RULES) if hasattr(constants, 'INFERENCE_RULES') else "N/A")
        with m3:
            st.metric("Skill Clusters", len(constants.SKILL_CLUSTERS) if hasattr(constants, 'SKILL_CLUSTERS') else "N/A")
        with m4:
            has_analysis = "Yes" if res else "No"
            st.metric("Analysis Cached", has_analysis)
        
        st.markdown("")
        
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
    # TAB 2: ANALYSIS DATA
    # =========================================================================
    with t2:
        st.subheader("Last Analysis Results")
        st.markdown("""
        **What is this?** This shows the raw data from your CV vs Job Description comparison.
        Use this to understand exactly how your match score was calculated.
        """)
        
        if res:
            # Summary metrics
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.metric("Match Score", f"{res['match_percentage']:.1f}%")
                st.metric("Matched Skills", len(res["matching_hard"]))
                st.metric("Missing Skills", len(res["missing_hard"]))
                st.metric("Bonus Skills", len(res["extra_hard"]))
                if "transferable" in res:
                    st.metric("Transferable", len(res["transferable"]))
            
            with col2:
                # Raw data expanders
                with st.expander("Matched Skills (Raw)", expanded=False):
                    st.write(sorted(res["matching_hard"]))
                
                with st.expander("Missing Skills (Raw)", expanded=False):
                    st.write(sorted(res["missing_hard"]))
                
                with st.expander("Extra/Bonus Skills (Raw)", expanded=False):
                    st.write(sorted(res["extra_hard"]))
                
                if "transferable" in res and res["transferable"]:
                    with st.expander("Transferable Mappings", expanded=False):
                        for missing, present in res["transferable"].items():
                            st.write(f"- {missing} ← {present}")
            
            # Full JSON export
            st.markdown("### Export Analysis")
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
    # TAB 3: SKILL INTELLIGENCE
    # =========================================================================
    with t3:
        st.subheader("Skill Clustering Analysis")
        st.markdown("""
        **What is this?** Clustering groups similar skills together based on their meaning.
        This helps identify which skill areas you're strong in and where there are gaps.
        Skills that appear close on the chart are semantically related.
        """)
        
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
                
                # Cluster breakdown
                st.markdown("### Cluster Breakdown")
                if clusters and isinstance(clusters, dict):
                    for cluster_name, skills in clusters.items():
                        if skills and hasattr(skills, '__iter__'):
                            skills_list = list(skills) if not isinstance(skills, list) else skills
                            matched_in_cluster = [s for s in skills_list if s in res["matching_hard"]]
                            missing_in_cluster = [s for s in skills_list if s in res["missing_hard"]]
                            
                            with st.expander(f"{cluster_name} ({len(skills_list)} skills)"):
                                if matched_in_cluster:
                                    st.markdown(f"**Matched:** {', '.join(matched_in_cluster)}")
                                if missing_in_cluster:
                                    st.markdown(f"**Missing:** {', '.join(missing_in_cluster)}")
                
                # Dendrogram
                if dendro_path:
                    with st.expander("Hierarchical Dendrogram"):
                        st.image(dendro_path, caption="Ward's Linkage Clustering")
        else:
            st.info("Run an analysis first to see skill clustering.")
    
    # =========================================================================
    # TAB 4: NLP INSIGHTS
    # =========================================================================
    with t4:
        st.subheader("Natural Language Processing")
        st.markdown("""
        **What is this?** NLP (Natural Language Processing) allows computers to understand human text.
        Here we extract key information automatically from your CV and job description.
        """)
        
        nlp_tab1, nlp_tab2 = st.tabs(["Named Entities (CV)", "Topic Analysis (JD)"])
        
        with nlp_tab1:
            if cv_text:
                entities = ml_utils.extract_entities_ner(cv_text)
                
                if entities:
                    e1, e2, e3 = st.columns(3)
                    
                    with e1:
                        st.markdown("#### Organizations")
                        orgs = entities.get("Organizations", [])
                        if orgs:
                            for org in orgs[:10]:
                                st.markdown(f"<span class='skill-tag-bonus'>{org}</span>", unsafe_allow_html=True)
                        else:
                            st.caption("None detected")
                    
                    with e2:
                        st.markdown("#### Locations")
                        locs = entities.get("Locations", [])
                        if locs:
                            for loc in locs[:10]:
                                st.markdown(f"<span class='skill-tag-bonus'>{loc}</span>", unsafe_allow_html=True)
                        else:
                            st.caption("None detected")
                    
                    with e3:
                        st.markdown("#### People")
                        pers = entities.get("Persons", [])
                        if pers:
                            for per in pers[:10]:
                                st.markdown(f"<span class='skill-tag-bonus'>{per}</span>", unsafe_allow_html=True)
                        else:
                            st.caption("None detected")
                else:
                    st.info("No named entities extracted.")
            else:
                st.info("Upload a CV first to extract named entities.")
        
        with nlp_tab2:
            if jd_text:
                jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
                
                if len(jd_corpus) > 5:
                    result = ml_utils.perform_topic_modeling(jd_corpus)
                    
                    if result:
                        st.markdown("#### Identified Topics")
                        for idx, topic in enumerate(result['topics'], 1):
                            st.success(f"**Topic {idx}:** {topic}")
                        
                        st.markdown("#### Top Keywords")
                        keywords_html = " ".join([f"<span class='skill-tag-bonus'>{kw}</span>" for kw in result['keywords']])
                        st.markdown(keywords_html, unsafe_allow_html=True)
                else:
                    st.info("Job description too short for topic analysis.")
            else:
                st.info("Add a job description first to analyze topics.")
    
    # =========================================================================
    # TAB 5: KNOWLEDGE BASE
    # =========================================================================
    with t5:
        st.subheader("System Knowledge Base")
        
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
# MAIN UI
# =============================================================================
def render_home():
    with st.sidebar:
        # Header
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='font-size: 1.8rem; margin-bottom: 0.2rem;'>Job Seeker Helper</h1>
            <p style='color: #00A0DC; font-size: 0.9rem; font-weight: 600;'>AI-Powered Career Analytics</p>
            <p style='color: #8b949e; font-size: 0.75rem;'>Version 2.0</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Demo Mode - Quick Start
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
        
        st.divider()
        
        # How It Works
        with st.expander("How It Works", expanded=False):
            st.markdown("""
            **1. Upload Your CV**
            - PDF or paste text directly
            - Our AI extracts 100+ skill types
            
            **2. Add Job Description**  
            - Paste from any job board
            - We decode what they really need
            
            **3. Click Analyze**
            - Get instant skill matching
            - See transferable skills identified
            - Discover your career fit score
            
            **4. Review Insights**
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
            Job Seeker Helper<br>
            <a href='https://github.com/Giacomod2001/datamining' style='color: #00A0DC;'>GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================================================
    # MAIN CONTENT AREA - Hero Section
    # ==========================================================================
    
    # Hero Header with Gradient
    st.markdown("""
    <div class='hero-gradient'>
        <h1 style='margin: 0; font-size: 2.5rem;'>Job Seeker Helper</h1>
        <p style='font-size: 1.2rem; color: #00A0DC; margin: 0.5rem 0;'>
            AI-Powered Career Analytics for Smarter Applications
        </p>
        <p style='color: #8b949e; font-size: 0.95rem;'>
            Upload your CV and job description to get instant insights on skills, gaps, and career opportunities
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================================================================
    # DYNAMIC LAYOUT: Calculate how many columns are needed based on active toggles
    # =============================================================================
    # Base: 2 columns (CV + JD)
    # +1 if Project Evaluation is active
    # +1 if Cover Letter Evaluation is active
    # Maximum: 4 columns (CV + Project + Cover Letter + JD)
    
    num_cols = 2  # CV + JD (base)
    if show_project_eval: num_cols += 1
    if show_cover_letter: num_cols += 1
    
    # Create columns based on calculated number
    if num_cols == 2:
        c1, c2 = st.columns(2)
        c3, c4 = None, None
    elif num_cols == 3:
        c1, c2, c3 = st.columns(3)
        c4 = None
    else:  # 4 columns
        c1, c2, c3, c4 = st.columns(4)

    # =============================================================================
    # COLUMN 1: CV (always present)
    # =============================================================================
    with c1:
        st.markdown("### Your CV")
        input_type_cv = st.radio("Input Type", ["Text", "PDF"], key="cv_input", horizontal=True, label_visibility="collapsed")
        
        cv = ""
        if input_type_cv == "Text":
            cv = st.text_area(
                "Paste CV text", 
                height=250, 
                key="cv_text", 
                placeholder="Paste your CV here or click 'Try Demo' in sidebar...",
                label_visibility="collapsed"
            )
        else:
            uploaded_cv = st.file_uploader("Upload CV (PDF)", type=["pdf"], key="cv_pdf", label_visibility="visible")
            if uploaded_cv:
                try: cv = ml_utils.extract_text_from_pdf(uploaded_cv)
                except Exception as e: st.error(f"PDF Error: {e}")
    
    # =============================================================================
    # OPTIONAL COLUMNS MANAGEMENT: Dynamically assign Project, Cover Letter, JD
    # =============================================================================
    project_text = ""
    cover_letter_text = ""
    current_col = 2  # Start from column 2 (first is CV)
    
    # Project Column (if enabled via toggle)
    if show_project_eval:
        # Assign the correct column based on how many are already used
        proj_col = c2 if current_col == 2 else (c3 if current_col == 3 else c4)
        with proj_col:
            st.subheader("Project Context")
            input_type_proj = st.radio("Input Type", ["Text", "PDF"], key="proj_input", horizontal=True, label_visibility="collapsed")
            if input_type_proj == "Text":
                project_text = st.text_area("Paste Project Desc", height=250, key="proj_text", label_visibility="visible")
            else:
                uploaded_proj = st.file_uploader("Upload Project (PDF)", type=["pdf"], key="proj_pdf", label_visibility="visible")
                if uploaded_proj:
                    try: project_text = ml_utils.extract_text_from_pdf(uploaded_proj)
                    except Exception as e: st.error(f"Error: {e}")
        current_col += 1  # Move to next column
    
    # Cover Letter Column (if enabled via toggle)
    if show_cover_letter:
        cl_col = c2 if current_col == 2 else (c3 if current_col == 3 else c4)
        with cl_col:
            st.subheader("Cover Letter")
            input_type_cl = st.radio("Input Type", ["Text", "PDF"], key="cl_input", horizontal=True, label_visibility="collapsed")
            if input_type_cl == "Text":
                cover_letter_text = st.text_area("Paste Cover Letter", height=250, key="cl_text", label_visibility="visible")
            else:
                uploaded_cl = st.file_uploader("Upload Cover Letter (PDF)", type=["pdf"], key="cl_pdf", label_visibility="visible")
                if uploaded_cl:
                    try: cover_letter_text = ml_utils.extract_text_from_pdf(uploaded_cl)
                    except Exception as e: st.error(f"Error: {e}")
        current_col += 1
    
    # =============================================================================
    # COLUMN JD: Job Description (always present, last column)
    # =============================================================================
    jd_col = c2 if current_col == 2 else (c3 if current_col == 3 else c4)
    with jd_col:
        st.markdown("### Job Description")
        input_type_jd = st.radio("Input Type", ["Text", "PDF"], key="jd_input", horizontal=True, label_visibility="collapsed")
        
        jd = ""
        if input_type_jd == "Text":
            jd = st.text_area(
                "Paste Job text", 
                height=250, 
                key="jd_text",
                placeholder="Paste job description here or click 'Try Demo' in sidebar...",
                label_visibility="collapsed"
            )
        else:
            uploaded_jd = st.file_uploader("Upload JD (PDF)", type=["pdf"], key="jd_pdf", label_visibility="visible")
            if uploaded_jd:
                try: jd = ml_utils.extract_text_from_pdf(uploaded_jd)
                except Exception as e: st.error(f"PDF Error: {e}")

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
        
        # Stage 2: Cover Letter (if enabled)
        cl_analysis = None
        if show_cover_letter and cover_letter_text:
            progress_bar.progress(60, text="Evaluating cover letter...")
            cl_analysis = ml_utils.analyze_cover_letter(cover_letter_text, jd, cv)
        
        # Stage 3: Generating insights
        progress_bar.progress(80, text="Generating career insights...")
        
        # Save results in session state for debugger
        st.session_state["last_results"] = res
        st.session_state["last_cv_text"] = cv
        st.session_state["last_jd_text"] = jd
        st.session_state["last_cl_analysis"] = cl_analysis
        
        # Complete!
        progress_bar.progress(100, text="Analysis complete.")
        
        # Small delay to show completion, then display
        import time
        time.sleep(0.5)
        progress_bar.empty()
        
        # Success message
        st.success("Analysis complete. Scroll down to see your personalized career insights.")
             
        # Display results
        render_results(res, jd, cv, cl_analysis)

def render_results(res, jd_text=None, cv_text=None, cl_analysis=None):
    st.divider()
    pct = res["match_percentage"]

    # --- MAIN SCORE SECTION ---
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
                st.subheader("Project Portfolio Verification")
                st.metric("Skills Verified", len(res["project_verified"]), 
                         help="Skills demonstrated through your projects")
                verified_list = list(res['project_verified'])[:5]
                st.markdown("**Top verified:** " + ", ".join(verified_list))
            add_idx += 1
        
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
    
    # Project-Verified Skills - Blue tags
    projects = res.get("project_review", set())
    if projects:
        st.markdown("**Project-Verified Skills:**")
        st.caption("Highlight these in your interview")
        project_html = " ".join([f"<span class='skill-tag-project'>{skill}</span>" for skill in sorted(projects)])
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
        st.subheader("Learning Actions")
        
        for skill in res["missing_hard"]:
            with st.expander(f"Action Plan: **{skill}**", expanded=len(res["missing_hard"]) == 1):
                q_skill = urllib.parse.quote(skill)
                
                lc1, lc2, lc3 = st.columns(3)
                with lc1:
                    st.markdown(f"**[Google Search](https://www.google.com/search?q=learn+{q_skill}+tutorial)**")
                    st.caption("General guides")
                with lc2:
                    st.markdown(f"**[YouTube](https://www.youtube.com/results?search_query=learn+{q_skill})**")
                    st.caption("Video tutorials")
                with lc3:
                    st.markdown(f"**[Courses](https://www.google.com/search?q=site:coursera.org+OR+site:udemy.com+OR+site:linkedin.com/learning+{q_skill})**")
                    st.caption("Platform specific")

    # --- ADVANCED MINING MOVED TO DEBUGGER ---
    # The 'Advanced Data Mining', 'Topic Modeling', and 'NER' sections have been moved 
    # to the 'render_debug_page' function as requested to clean up the main view.

    # --- JOB CONTEXT ANALYSIS ---
    if jd_text:
        st.divider()
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
                 
                 st.markdown(f"[Google Jobs](https://www.google.com/search?q={role_query}+jobs)")
                 st.markdown(f"[LinkedIn](https://www.linkedin.com/jobs/search/?keywords={role_query})")
                 st.markdown(f"[Indeed Italia](https://it.indeed.com/jobs?q={italy_query})")
                 
                 with st.expander("Missing Skills"):
                     for s in rec['missing'][:5]:
                         st.markdown(f"- {s}")
    else:
        st.info("**Quality Mode**: No alternative roles met the confidence threshold (>30%). Your profile is uniquely specialized.")

    # --- EXPORT REPORT ---
    st.divider()
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
