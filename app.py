import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import constants
import ml_utils
import urllib.parse

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Job Seeker Helper v1.34 (NER FIX)",
    page_icon="🎯",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# =============================================================================
# DEBUGGER
# =============================================================================
def render_debug_page():
    if st.button("← Back"):
        st.session_state["page"] = "Home"
        st.rerun()
    st.title("🛠️ Debugger & Experimental Analytics")
    st.info("This panel provides advanced insights into your profile data.")
    
    # Check if we have analysis results in session
    res = st.session_state.get("last_results", None)
    
    tabs = ["🧠 Inference", "🔗 Clusters (Rules)", "📊 Deep Clustering", "🧩 Topic Modeling", "🏷️ PER/LOC/ORG", "📚 Knowledge DB"]
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
        st.subheader("🧠 Advanced Data Mining (Skill Clans)")
        st.caption("Using unsupervised learning (K-Means & Ward's Method) to group your specific skills.")
        
        if res:
             # 1. Prepare Data
            all_skills = list(res["matching_hard"] | res["missing_hard"] | res["extra_hard"])
            
            if len(all_skills) > 3:
                # Run Clustering
                df_viz, dendro_path, clusters = ml_utils.perform_skill_clustering(all_skills)
                
                if df_viz is not None:
                    c_t1, c_t2 = st.tabs(["📊 Scatter Plot", "🌳 Dendrogram"])
                    
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
        st.subheader("🧩 Job Context Analysis (LDA)")
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
        st.subheader("🏷️ Resume Entity Extraction (NER)")
        if st.session_state.get("last_cv_text"):
            cv_text = st.session_state["last_cv_text"]
            entities = ml_utils.extract_entities_ner(cv_text)
            
            if entities:
                ec1, ec2, ec3 = st.columns(3)
                with ec1:
                    st.markdown("#### 🏛️ Organizations")
                    for org in entities.get("Organizations", [])[:10]: st.write(f"- {org}")
                with ec2:
                    st.markdown("#### 📍 Locations")
                    for loc in entities.get("Locations", [])[:10]: st.write(f"- {loc}")
                with ec3:
                    st.markdown("#### 👤 People")
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
        st.title("🎯 Job Seeker Helper")
        st.caption("v1.34 (NER FIX)")
        st.markdown("### 🚀 Instructions")
        st.markdown("1. **Upload CV**: PDF or Text.")
        st.markdown("2. **Upload JD**: Job Description.")
        st.markdown("3. **Analyze**: Get insights.")
        st.markdown("---")
        st.info("Features:\n- **Smart Inference** (BigQuery → Cloud)\n- **Transferable Skills** (Looker → Power BI)\n- **Visual Analytics** (New!)")
        st.divider()
        
        show_project_eval = st.toggle("📂 Project Evaluation", value=False, help="Analyze your projects alongside your CV")
        show_cover_letter = st.toggle("✉️ Cover Letter Evaluation", value=False, help="Evaluate your cover letter against the job description")
        
        if st.toggle("Developer Mode"):
             pwd = st.text_input("Enter Password", type="password", key="dev_pwd")
             if pwd == "1234":
                 if st.button("Open Debugger"):
                    st.session_state["page"] = "Debugger"
                    st.rerun()
             elif pwd:
                 st.error("Wrong password")

    st.title("🎯 Job Seeker Helper")
    st.markdown("Analyze your CV against job descriptions.")
    st.divider()

    # Dynamic Layout based on toggles
    num_cols = 2  # CV + JD (base)
    if show_project_eval: num_cols += 1
    if show_cover_letter: num_cols += 1
    
    if num_cols == 2:
        c1, c2 = st.columns(2)
        c3, c4 = None, None
    elif num_cols == 3:
        c1, c2, c3 = st.columns(3)
        c4 = None
    else:  # 4 columns
        c1, c2, c3, c4 = st.columns(4)

    # Column 1: CV (always present)
    with c1:
        st.subheader("Your CV")
        input_type_cv = st.radio("Input Type", ["Text", "PDF"], key="cv_input", horizontal=True, label_visibility="collapsed")
        cv = ""
        if input_type_cv == "Text":
            cv = st.text_area("Paste CV text", height=250, key="cv_text", label_visibility="visible")
        else:
            uploaded_cv = st.file_uploader("Upload CV (PDF)", type=["pdf"], key="cv_pdf", label_visibility="visible")
            if uploaded_cv:
                try: cv = ml_utils.extract_text_from_pdf(uploaded_cv)
                except Exception as e: st.error(f"Error: {e}")
    
    # Determine which columns to use for Project, Cover Letter, and JD
    project_text = ""
    cover_letter_text = ""
    current_col = 2  # Start from column 2
    
    # Project Column (if enabled)
    if show_project_eval:
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
        current_col += 1
    
    # Cover Letter Column (if enabled)
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
    
    # Job Description Column (always present, last column)
    jd_col = c2 if current_col == 2 else (c3 if current_col == 3 else c4)
    with jd_col:
        st.subheader("Job Description")
        input_type_jd = st.radio("Input Type", ["Text", "PDF"], key="jd_input", horizontal=True, label_visibility="collapsed")
        jd = ""
        if input_type_jd == "Text":
            jd = st.text_area("Paste Job text", height=250, key="jd_text", label_visibility="visible")
        else:
            uploaded_jd = st.file_uploader("Upload JD (PDF)", type=["pdf"], key="jd_pdf", label_visibility="visible")
            if uploaded_jd:
                try: jd = ml_utils.extract_text_from_pdf(uploaded_jd)
                except Exception as e: st.error(f"Error: {e}")

    if st.button("🔍 Analyze", type="primary", use_container_width=True):
        if not cv or not jd:
            st.warning("Please provide both CV and Job Description.")
            return

        with st.spinner("Analyzing profile..."):
            if show_project_eval and project_text:
                 res = ml_utils.analyze_gap_with_project(cv, jd, project_text)
            else:
                 res = ml_utils.analyze_gap(cv, jd)
            
            # Analyze cover letter if provided
            cl_analysis = None
            if show_cover_letter and cover_letter_text:
                cl_analysis = ml_utils.analyze_cover_letter(cover_letter_text, jd, cv)
            
            # Save state for debugger
            st.session_state["last_results"] = res
            st.session_state["last_cv_text"] = cv
            st.session_state["last_jd_text"] = jd
            st.session_state["last_cl_analysis"] = cl_analysis
                 
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
        # Plotly Pie Chart (go.Pie for absolute control)
        fig = go.Figure(data=[go.Pie(
            labels=['Match', 'Gap'],
            values=[pct, 100-pct],
            hole=0.7,
            marker_colors=['#00cc96', '#EF553B'],
            sort=False, # CRITICAL to keep colors aligned
            textinfo='none'
        )])
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=150)
        
        # Center Annotation
        fig.add_annotation(text=f"{pct:.0f}%", showarrow=False, font_size=20, x=0.5, y=0.5)
        st.plotly_chart(fig, use_container_width=True)
    
    col_idx += 1

    with cols[col_idx]:
        st.subheader("Match Score")
        if pct >= 80: 
            st.success("🚀 Excellent Match!")
            st.markdown("Your profile is very aligned with this role.")
        elif pct >= 60: 
            st.warning("⚠️ Good Potential")
            st.markdown("Some gaps exist, but many skills are transferable.")
        else: 
            st.error("❌ High Gap")
            st.markdown("Significant learning required for this specific role.")
    
    col_idx += 1
        
    if "project_verified" in res and res["project_verified"]:
        with cols[col_idx]:
            st.subheader("🏆 Project Boost")
            st.metric("Verified Skills", len(res["project_verified"]))
            st.caption(f"Validating: {', '.join(list(res['project_verified'])[:3])}...")
        col_idx += 1
    
    # Cover Letter Analysis Section
    if cl_analysis:
        with cols[col_idx]:
            st.subheader("✉️ Cover Letter Score")
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
    st.subheader("🛠️ Technical Skills Analysis")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown("#### ✅ Matched")
        for s in res["matching_hard"]: st.write(f"- {s}")
        if not res["matching_hard"]: st.caption("-")

    with c2:
        st.markdown("#### ⚠️ Transferable")
        transferable = res.get("transferable", {})
        if transferable:
            for missing, present in transferable.items():
                st.write(f"- **{missing}**") 
                st.caption(f"(via {present})")
        else:
            st.caption("-")

    with c3:
        st.markdown("#### 📂 Portfolio")
        projects = res.get("project_review", set())
        if projects:
            for s in projects: st.info(f"**{s}**")
            st.caption("Mention these in interview!")
        else:
            st.caption("-")
            
    with c4:
        st.markdown("#### ❌ Missing")
        for s in res["missing_hard"]: st.write(f"- **{s}**")
        if not res["missing_hard"]: st.success("Clear!")

    with c5:
        st.markdown("#### ➕ Bonus")
        for s in res["extra_hard"]: st.write(f"- {s}")

    st.divider()
    
    # --- COVER LETTER DETAILED ANALYSIS ---
    if cl_analysis:
        st.subheader("✉️ Cover Letter Analysis")
        
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
            st.markdown("#### ✅ Strengths")
            if cl_analysis['strengths']:
                for strength in cl_analysis['strengths']:
                    st.markdown(strength)
            else:
                st.info("No specific strengths identified yet")
        
        with fc2:
            st.markdown("#### 💡 Improvements")
            if cl_analysis['improvements']:
                for improvement in cl_analysis['improvements']:
                    st.markdown(improvement)
            else:
                st.success("Great job! No major improvements needed")
        
        # Keywords Coverage Detail
        if cl_analysis['hard_mentioned'] or cl_analysis['hard_missing']:
            st.markdown("#### 🏷️ Technical Keywords Status")
            kc1, kc2 = st.columns(2)
            
            with kc1:
                st.markdown("**✅ Mentioned**")
                if cl_analysis['hard_mentioned']:
                    for skill in sorted(cl_analysis['hard_mentioned']):
                        st.write(f"- {skill}")
                else:
                    st.caption("None")
            
            with kc2:
                st.markdown("**⚠️ Missing**")
                if cl_analysis['hard_missing']:
                    for skill in sorted(list(cl_analysis['hard_missing'])[:10]):
                        st.write(f"- {skill}")
                else:
                    st.success("All covered!")

    st.divider()

    # LEARNING PLAN
    if res["missing_hard"]:
        st.subheader("📚 Learning Actions")
        
        for skill in res["missing_hard"]:
            with st.expander(f"Action Plan: **{skill}**", expanded=len(res["missing_hard"]) == 1):
                q_skill = urllib.parse.quote(skill)
                
                lc1, lc2, lc3 = st.columns(3)
                with lc1:
                    st.markdown(f"**[🔍 Google Search](https://www.google.com/search?q=learn+{q_skill}+tutorial)**")
                    st.caption("General guides")
                with lc2:
                    st.markdown(f"**[📺 YouTube](https://www.youtube.com/results?search_query=learn+{q_skill})**")
                    st.caption("Video tutorials")
                with lc3:
                    st.markdown(f"**[🎓 Courses](https://www.google.com/search?q=site:coursera.org+OR+site:udemy.com+OR+site:linkedin.com/learning+{q_skill})**")
                    st.caption("Platform specific")

    # --- ADVANCED MINING MOVED TO DEBUGGER ---
    # The 'Advanced Data Mining', 'Topic Modeling', and 'NER' sections have been moved 
    # to the 'render_debug_page' function as requested to clean up the main view.

    # --- JOB CONTEXT ANALYSIS ---
    if jd_text:
        st.divider()
        st.subheader("💡 Cosa Cerca Davvero Questa Posizione?")
        
        jd_corpus = [line for line in jd_text.split('\n') if len(line.split()) > 3]
        
        if len(jd_corpus) > 5:
            result = ml_utils.perform_topic_modeling(jd_corpus)
            
            if result:
                # Show summary prominently
                st.info(result['summary'])
                
                # Show interpretations in columns
                st.markdown("#### 📋 Aree Chiave Richieste:")
                cols_topic = st.columns(len(result['topics']))
                for idx, (col, topic) in enumerate(zip(cols_topic, result['topics'])):
                    with col:
                        st.markdown(f"**Area {idx+1}**")
                        st.write(topic)
                
                # Show keywords as tags
                st.markdown("#### 🏷️ Parole Chiave Principali:")
                keyword_html = " ".join([f"<span style='background-color: #e1f5ff; color: #1a1a1a; font-weight: 500; padding: 5px 10px; border-radius: 5px; margin: 2px; display: inline-block;'>{kw}</span>" for kw in result['keywords']])
                st.markdown(keyword_html, unsafe_allow_html=True)
        else:
            st.info("Job Description troppo breve per l'analisi contestuale.")
    
    # --- JOB RECOMMENDER (AI Career Compass) ---
    st.divider()
    st.subheader("🔮 AI Career Compass (Alternative Paths)")
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
                 
                 st.markdown(f"🌐 [Google Jobs](https://www.google.com/search?q={role_query}+jobs)")
                 st.markdown(f"💼 [LinkedIn](https://www.linkedin.com/jobs/search/?keywords={role_query})")
                 st.markdown(f"🔍 [Indeed Italia](https://it.indeed.com/jobs?q={italy_query})")
                 
                 with st.expander("Missing Skills"):
                     for s in rec['missing'][:5]:
                         st.markdown(f"- {s}")
    else:
        st.info("ℹ️ **Quality Mode**: No alternative roles met the confidence threshold (>30%). Your profile is uniquely specialized.")

    # --- EXPORT REPORT ---
    st.divider()
    st.subheader("📥 Export Report")
    
    # Generate Detailed Content
    report_text = ml_utils.generate_detailed_report_text(res, jd_text if jd_text else "")
    report_pdf = ml_utils.generate_pdf_report(report_text)
    
    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        st.download_button("📄 Download Text Report", report_text, file_name="Job_Seeker_Report.txt", mime="text/plain", use_container_width=True)
    with col_dl2:
        if report_pdf:
            st.download_button("📕 Download PDF Report", report_pdf, file_name="Job_Seeker_Report.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.warning("PDF Generation unavailable (fpdf missing).")

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
