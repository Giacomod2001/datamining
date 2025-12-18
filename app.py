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
    page_title="Job Seeker Helper v1.26 (TUNED AI)",
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
    st.title("🛠️ Debugger")
    st.info("This panel helps developers understand how skills are detected and inferred.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🧠 Inference Logic", "🔗 Skill Clusters", "📂 Project Skills", "📚 Knowledge DB"])
    
    with tab1:
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

    with tab2:
        st.subheader("Interchangeable Groups")
        st.markdown("Skills in the same cluster are considered **Transferable**.")
        # Flatten clusters for display
        cluster_data = [{"Cluster Name": k, "Members": ", ".join(sorted(v))} for k, v in constants.SKILL_CLUSTERS.items()]
        st.dataframe(pd.DataFrame(cluster_data), use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("Portfolio/Project Based")
        st.markdown("These complex skills should be discussed in an interview/portfolio.")
        st.write(sorted(list(constants.PROJECT_BASED_SKILLS)))

    with tab4:
        st.subheader("Training Data (Sample)")
        _, df = ml_utils.train_rf_model()
        st.dataframe(df, use_container_width=True)

# =============================================================================
# MAIN UI
# =============================================================================
def render_home():
    with st.sidebar:
        st.title("🎯 Job Seeker Helper")
        st.caption("v1.26 (TUNED AI)")
        st.markdown("### 🚀 Instructions")
        st.markdown("1. **Upload CV**: PDF or Text.")
        st.markdown("2. **Upload JD**: Job Description.")
        st.markdown("3. **Analyze**: Get insights.")
        st.markdown("---")
        st.info("Features:\n- **Smart Inference** (BigQuery → Cloud)\n- **Transferable Skills** (Looker → Power BI)\n- **Visual Analytics** (New!)")
        st.divider()
        
        # EXPERIMENTAL FEATURE TOGGLE
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

                    st.markdown(f"**[🎓 Courses](https://www.google.com/search?q=site:coursera.org+OR+site:udemy.com+OR+site:linkedin.com/learning+{q_skill})**")
                    st.caption("Platform specific")

    # --- ADVANCED MINING (Clustering) ---
    st.divider()
    st.subheader("🧠 Advanced Data Mining (Skill Clans)")
    st.info("Using Unsupervised Learning (Hierarchical Clustering & K-Means) to group your skills logicially.")
    
    # 1. Prepare Data
    all_skills = list(res["matching_hard"] | res["missing_hard"] | res["extra_hard"])
    
    if len(all_skills) > 3:
        # Run Clustering
        df_viz, dendro_path, clusters = ml_utils.perform_skill_clustering(all_skills)
        
        if df_viz is not None:
            t1, t2 = st.tabs(["📊 Scatter Plot (K-Means)", "🌳 Dendrogram (Hierarchical)"])
            
            with t1:
                # Enrich with Status
                def get_status(s):
                    if s in res["matching_hard"]: return "Matched"
                    if s in res["missing_hard"]: return "Missing"
                    return "Extra"
                
                df_viz["Status"] = df_viz["skill"].apply(get_status)
                
                fig_cls = px.scatter(df_viz, x="x", y="y", color="cluster", symbol="Status",
                                     hover_data=["skill"], title="Skill Semantic Map (PCA + K-Means)")
                fig_cls.update_traces(marker=dict(size=14, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
                # Fix overlap: Move legend to the right (outside) or bottom. Using standard right side.
                fig_cls.update_layout(
                    showlegend=True, 
                    legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
                    margin=dict(r=150) # Add margin for legend
                )
                st.plotly_chart(fig_cls, use_container_width=True)
                
            with t2:
                if dendro_path:
                    st.image(dendro_path, caption="Skill Hierarchy (Ward's Method)")
                    st.caption("Skills joined lower down are more similar/related.")
        
        # GENEARTE INSIGHT (User Request: "Make it less cold")
        st.markdown("---")
        insight_text = ml_utils.generate_cluster_insight(clusters, res["matching_hard"], res["missing_hard"])
        st.info(insight_text)
                    
    else:
        st.warning("Not enough skills detected to perform clustering analysis (Need > 3).")

    # --- NEW: TOPIC MODELING (JD) ---
    if jd_text:
        st.divider()
        st.subheader("🧩 Job Context Analysis (Topic Modeling)")
        st.caption("Using Latent Dirichlet Allocation (LDA) to identify key themes in the Job Description.")
        
        # Split JD into "sentences" or chunks for LDA (simple split by newline for now)
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

    # --- NEW: ENTITY EXTRACTION (CV) ---
    if cv_text:
        st.divider()
        st.subheader("🏷️ Resume Entity Extraction (NER)")
        st.caption("Automatically extracting standardized entities using NLTK.")
        
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

    # --- JOB RECOMMENDER (AI Career Compass) ---
    st.divider()
    st.subheader("🔮 AI Career Compass (Alternative Paths)")
    st.info("Based on your skill vector, here are the market roles that fit you best.")
    
    # Use all skills found in CV (Matched, Missing, Extra) to define the candidate vector
    candidate_skills = res["matching_hard"] | res["missing_hard"] | res["extra_hard"]
    
    recs = ml_utils.recommend_roles(candidate_skills)
    
    if recs:
        rc1, rc2, rc3 = st.columns(3)
        cols = [rc1, rc2, rc3]
        
        for i, rec in enumerate(recs):
            with cols[i]:
                st.markdown(f"**{i+1}. {rec['role']}**")
                score = rec['score']
                st.progress(score / 100, text=f"{score:.0f}% Similarity")
                
                # "Apply Now" Link
                q_role = urllib.parse.quote(rec['role'])
                st.markdown(f"[🌐 Search Jobs](https://www.google.com/search?q={q_role}+jobs+near+me)")
                st.markdown(f"[💼 LinkedIn](https://www.linkedin.com/jobs/search?keywords={q_role})")
                
                with st.expander("Gaps"):
                    if rec["missing"]:
                        for m in rec["missing"]: st.caption(f"❌ {m}")
                    else:
                        st.caption("Perfect Fit!")
    else:
        st.warning("Not enough skills extracted to recommend specific roles.")

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
