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
    if st.button("← Back"):
        st.session_state["page"] = "Home"
        st.rerun()
    st.title("Debugger & Experimental Analytics")
    st.info("This panel provides advanced insights into your profile data.")
    
    # Check if we have analysis results in session
    res = st.session_state.get("last_results", None)
    
    tabs = ["Inference", "Clusters (Rules)", "Deep Clustering", "Topic Modeling", "PER/LOC/ORG", "Knowledge DB"]
    t1, t2, t3, t4, t5, t6 = st.tabs(tabs)
    
    with t1:
        st.subheader("Hierarchical Rules (Knowledge Graph)")
        st.markdown("If **Child Skill** is found → **Parent Skill** is added.")
        
        # Internal Graph Logic
        import graphviz
        graph = graphviz.Digraph()
        for child, parents in constants.INFERENCE_RULES.items():
            for parent in parents:
                graph.edge(child, parent)
        
        st.graphviz_chart(graph)
        
        with st.expander("Show Tabular Data"):
            inf_data = [{"Child Skill": k, "Inferred Parent(s)": ", ".join(v)} for k, v in constants.INFERENCE_RULES.items()]
            st.dataframe(pd.DataFrame(inf_data), use_container_width=True, hide_index=True)

    with t2:
        st.subheader("Interchangeable Groups")
        st.markdown("Skills in the same cluster are considered **Transferable**.")
        # Flatten clusters for display
        cluster_data = [{"Cluster Name": k, "Members": ", ".join(sorted(v))} for k, v in constants.SKILL_CLUSTERS.items()]
        st.dataframe(pd.DataFrame(cluster_data), use_container_width=True, hide_index=True)

    with t3:
        st.subheader("Advanced Data Mining (Skill Clans)")
        st.caption("Using unsupervised learning (K-Means & Ward's Method) to group your specific skills.")
        
        if res:
             # 1. Prepare Data
            all_skills = list(res["matching_hard"] | res["missing_hard"] | res["extra_hard"])
            
            if len(all_skills) > 3:
                # Run Clustering
                df_viz, dendro_path, clusters = ml_utils.perform_skill_clustering(all_skills)
                
                if df_viz is not None:
                    c_t1, c_t2 = st.tabs(["Scatter Plot", "Dendrogram"])
                    
                    with c_t1:
                        # Enrich with Status
                        def get_status(s):
                            if s in res["matching_hard"]: return "Matched"
                            if s in res["missing_hard"]: return "Missing"
                            return "Extra"
                        
                        df_viz["Status"] = df_viz["skill"].apply(get_status)
                        
                        fig_cls = px.scatter(df_viz, x="x", y="y", color="cluster", symbol="Status",
                                            hover_data=["skill"], title="Skill Semantic Map (PCA + K-Means)")
                        st.plotly_chart(fig_cls, use_container_width=True)
                        
                    with c_t2:
                        if dendro_path:
                            st.image(dendro_path, caption="Skill Hierarchy (Ward's Method)")
                
                # GENEARTE INSIGHT
                st.markdown("---")
                insight_text = ml_utils.generate_cluster_insight(clusters, res["matching_hard"], res["missing_hard"])
                st.info(insight_text)
            else:
                st.warning("Not enough skills detected (<3) to perform clustering.")
        else:
            st.warning("Please run an analysis on the Home page first to see data here.")

    with t4:
        st.subheader("Job Context Analysis (LDA)")
        if st.session_state.get("last_jd_text"):
            jd_text = st.session_state["last_jd_text"]
            jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
            
            if len(jd_corpus) > 5:
                result = ml_utils.perform_topic_modeling(jd_corpus)
                
                if result:
                    c1, c2 = st.columns([1, 2])
                    with c1:
                        st.markdown("**Aree Tematiche Identificate:**")
                        for topic in result['topics']:
                            st.success(topic)
                    with c2:
                        if result['wordcloud_path']:
                            st.image(result['wordcloud_path'], caption="Topic Keywords Word Cloud")
            else:
                st.info("Job Description too short for Topic Modeling.")
        else:
            st.warning("Please analyse a job description first.")

    with t5:
        st.subheader("Resume Entity Extraction (NER)")
        if st.session_state.get("last_cv_text"):
            cv_text = st.session_state["last_cv_text"]
            entities = ml_utils.extract_entities_ner(cv_text)
            
            if entities:
                ec1, ec2, ec3 = st.columns(3)
                with ec1:
                    st.markdown("#### Organizations")
                    for org in entities.get("Organizations", [])[:10]: st.write(f"- {org}")
                with ec2:
                    st.markdown("#### Locations")
                    for loc in entities.get("Locations", [])[:10]: st.write(f"- {loc}")
                with ec3:
                    st.markdown("#### People")
                    for per in entities.get("Persons", [])[:10]: st.write(f"- {per}")
            else:
                st.info("No named entities found.")
        else:
            st.warning("Please analyse a CV first.")

    with t6:
        st.subheader("Training Data (Sample)")
        _, df = ml_utils.train_rf_model()
        st.dataframe(df, use_container_width=True)

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
            value=st.session_state["show_project_toggle"],
            key="show_project_toggle",
            help="Upload project descriptions to verify skills through your portfolio. Increases match score when projects demonstrate missing skills."
        )
        
        show_cover_letter = st.toggle(
            "Cover Letter Analysis", 
            value=st.session_state["show_cl_toggle"],
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

    # --- METRICS SECTION ---
    # Determine number of metrics columns based on what we have
    metrics_cols_count = 2  # Base: CV match + assessment
    if "project_verified" in res and res["project_verified"]:
        metrics_cols_count += 1
    if cl_analysis:
        metrics_cols_count += 1
    
    cols = st.columns(metrics_cols_count)
    col_idx = 0

    with cols[col_idx]:
        # Clean Gauge Indicator with transparent background
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            number={'suffix': '%', 'font': {'size': 36, 'color': '#ffffff'}},
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
                    'line': {'color': "#00cc96", 'width': 3},
                    'thickness': 0.8,
                    'value': pct
                }
            }
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=30, b=10, l=30, r=30),
            height=160,
            font={'color': '#ffffff'}
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    col_idx += 1

    with cols[col_idx]:
        st.subheader("Match Score")
        if pct >= 80: 
            st.success("Excellent Match!")
            st.markdown("Your profile is very aligned with this role.")
        elif pct >= 60: 
            st.warning("Good Potential")
            st.markdown("Some gaps exist, but many skills are transferable.")
        else: 
            st.error("High Gap")
            st.markdown("Significant learning required for this specific role.")
    
    col_idx += 1
        
    if "project_verified" in res and res["project_verified"]:
        with cols[col_idx]:
            st.subheader("Project Boost")
            st.metric("Verified Skills", len(res["project_verified"]))
            st.caption(f"Validating: {', '.join(list(res['project_verified'])[:3])}...")
        col_idx += 1
    
    # Cover Letter Analysis Section
    if cl_analysis:
        with cols[col_idx]:
            st.subheader("Cover Letter Score")
            cl_score = cl_analysis['overall_score']
            
            # Color-coded gauge
            if cl_score >= 80:
                st.success(f"**{cl_score:.0f}%** - Excellent!")
            elif cl_score >= 60:
                st.warning(f"**{cl_score:.0f}%** - Good")
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
            
            # Mentioned keywords as tags
            if cl_analysis['hard_mentioned']:
                st.markdown("**Mentioned:**")
                mentioned_html = " ".join([f"<span style='background-color: #d4edda; color: #155724; font-weight: 500; padding: 4px 8px; border-radius: 4px; margin: 2px; display: inline-block; font-size: 0.9em;'>{skill}</span>" for skill in sorted(cl_analysis['hard_mentioned'])])
                st.markdown(mentioned_html, unsafe_allow_html=True)
                st.markdown("")  # Spacing
            
            # Missing keywords as tags
            if cl_analysis['hard_missing']:
                st.markdown("**Missing (consider adding):**")
                missing_list = sorted(list(cl_analysis['hard_missing'])[:15])  # Limit to 15 for readability
                missing_html = " ".join([f"<span style='background-color: #fff3cd; color: #856404; font-weight: 500; padding: 4px 8px; border-radius: 4px; margin: 2px; display: inline-block; font-size: 0.9em;'>{skill}</span>" for skill in missing_list])
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
                
                # Show keywords as tags
                st.markdown("#### Main Keywords:")
                keyword_html = " ".join([f"<span style='background-color: #e1f5ff; color: #1a1a1a; font-weight: 500; padding: 5px 10px; border-radius: 5px; margin: 2px; display: inline-block;'>{kw}</span>" for kw in result['keywords']])
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
