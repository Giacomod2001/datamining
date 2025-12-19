import streamlit as st
import pandas as pd
import plotly.express as px
import constants
import ml_utils
import urllib.parse

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Job Seeker Helper v1.4",
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
                topics, wc_path = ml_utils.perform_topic_modeling(jd_corpus)
                
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.markdown("**Discovered Topics:**")
                    for t in topics:
                        st.success(t)
                with c2:
                    if wc_path:
                        st.image(wc_path, caption="Topic Keywords Word Cloud")
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
        st.caption("v1.4 (DEBUG BUILD)")
        st.markdown("### 🚀 Instructions")
        st.markdown("1. **Upload CV**: PDF or Text.")
        st.markdown("2. **Upload JD**: Job Description.")
        st.markdown("3. **Analyze**: Get insights.")
        st.markdown("---")
        st.info("Features:\n- **Smart Inference** (BigQuery → Cloud)\n- **Transferable Skills** (Looker → Power BI)\n- **Visual Analytics** (New!)")
        st.divider()
        
        show_project_eval = st.toggle("Project Evaluation", value=False, help="Analyze your projects alongside your CV")
        
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

    # Dynamic Layout
    if show_project_eval:
        c1, c2, c3 = st.columns(3)
    else:
        c1, c2 = st.columns(2)
        c3 = None

    # Column 1: CV
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
    
    # Column 2: Project or JD
    project_text = ""
    col2 = c2
    if show_project_eval and c3:
        with col2:
             st.subheader("Project Context")
             input_type_proj = st.radio("Input Type", ["Text", "PDF"], key="proj_input", horizontal=True, label_visibility="collapsed")
             if input_type_proj == "Text":
                 project_text = st.text_area("Paste Project Desc", height=250, key="proj_text", label_visibility="visible")
             else:
                 uploaded_proj = st.file_uploader("Upload Project (PDF)", type=["pdf"], key="proj_pdf", label_visibility="visible")
                 if uploaded_proj:
                     try: project_text = ml_utils.extract_text_from_pdf(uploaded_proj)
                     except Exception as e: st.error(f"Error: {e}")
        jd_col = c3
    else:
        jd_col = c2
        project_text = ""

    # Column 3 (or 2): Job Description
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
            
            # Save state for debugger
            st.session_state["last_results"] = res
            st.session_state["last_cv_text"] = cv
            st.session_state["last_jd_text"] = jd
                 
            render_results(res, jd, cv)

def render_results(res, jd_text=None, cv_text=None):
    st.divider()
    pct = res["match_percentage"]

    # --- METRICS SECTION ---
    cols = st.columns([1, 1, 1]) if "project_verified" in res else st.columns([1, 1])

    with cols[0]:
        # Plotly Gauge
        fig = px.pie(values=[pct, 100-pct], names=["Match", "Gap"], hole=0.7, 
                     color_discrete_sequence=["#00cc96", "#EF553B"])
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=150)
        fig.add_annotation(text=f"{pct:.0f}%", showarrow=False, font_size=20)
        st.plotly_chart(fig, use_container_width=True)

    with cols[1]:
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
        
    if "project_verified" in res and res["project_verified"]:
        with cols[2]:
            st.subheader("🏆 Project Boost")
            st.metric("Verified Skills", len(res["project_verified"]))
            st.caption(f"Validating: {', '.join(list(res['project_verified'])[:3])}...")

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

    # --- EXPORT REPORT ---
    st.divider()
    report_text = f"Job Seeker Report:\nMatch Percentage: {res['match_percentage']:.0f}%\nMatched Skills: {', '.join(res['matching_hard'])}\nMissing Skills: {', '.join(res['missing_hard'])}"
    st.download_button("⬇️ Download Report (TXT)", report_text, file_name="report.txt")

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
