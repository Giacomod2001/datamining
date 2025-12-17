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
    page_title="Job Seeker Helper",
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
        st.markdown("### 🚀 Instructions")
        st.markdown("1. **Upload CV**: PDF or Text.")
        st.markdown("2. **Upload JD**: Job Description.")
        st.markdown("3. **Analyze**: Get insights.")
        st.markdown("---")
        st.info("Features:\n- **Smart Inference** (BigQuery → Cloud)\n- **Transferable Skills** (Looker → Power BI)\n- **Visual Analytics** (New!)")
        st.divider()
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

    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Your CV")
        input_type = st.radio("Input Type", ["Text", "PDF"], key="cv_input", horizontal=True)
        cv = ""
        if input_type == "Text":
            cv = st.text_area("Paste CV text", height=200, key="cv_text")
        else:
            uploaded_cv = st.file_uploader("Upload CV (PDF)", type=["pdf"], key="cv_pdf")
            if uploaded_cv:
                try: 
                    cv = ml_utils.extract_text_from_pdf(uploaded_cv)
                    st.success(f"Loaded {len(cv)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")
                    
    with c2:
        st.subheader("Job Description")
        input_type_jd = st.radio("Input Type", ["Text", "PDF"], key="jd_input", horizontal=True)
        jd = ""
        if input_type_jd == "Text":
            jd = st.text_area("Paste Job text", height=200, key="jd_text")
        else:
            uploaded_jd = st.file_uploader("Upload JD (PDF)", type=["pdf"], key="jd_pdf")
            if uploaded_jd:
                try: 
                    jd = ml_utils.extract_text_from_pdf(uploaded_jd)
                    st.success(f"Loaded {len(jd)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")
        
    if st.button("🔍 Analyze", type="primary", use_container_width=True):
        if not cv or not jd:
            st.warning("Please provide both CV and Job Description.")
            return
            
        with st.spinner("Analyzing profile..."):
            res = ml_utils.analyze_gap(cv, jd)
            render_results(res, jd)

def render_results(res, jd_text=None):
    st.divider()
    pct = res["match_percentage"]
    
    # --- METRICS SECTION ---
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Plotly Gauge
        fig = px.pie(values=[pct, 100-pct], names=["Match", "Gap"], hole=0.7, 
                     color_discrete_sequence=["#00cc96", "#EF553B"])
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=150)
        fig.add_annotation(text=f"{pct:.0f}%", showarrow=False, font_size=20)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
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
            for s in projects:
                st.info(f"**{s}**")
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
            # Check if we have a specific known resource, otherwise DEFAULT (empty)
            r = constants.LEARNING_RESOURCES.get(skill, None)
            
            with st.expander(f"Action Plan: **{skill}**"):
                if r:
                    # Known resource
                    st.markdown("**Recommended Courses:**")
                    for c in r["courses"]:
                        st.write(f"- {c}")
                    st.markdown(f"**Project:** {r['project']}")
                else:
                    # Dynamic Fallback
                    st.warning(f"No specific guide found for '{skill}', but here are direct search links:")
                    
                    # Create safe URL queries
                    q_skill = urllib.parse.quote(skill)
                    
                    lc1, lc2, lc3 = st.columns(3)
                    with lc1:
                        st.markdown(f"**[🔍 Google Search](https://www.google.com/search?q=learn+{q_skill}+tutorial)**")
                    with lc2:
                        st.markdown(f"**[📺 YouTube Courses](https://www.youtube.com/results?search_query=learn+{q_skill})**")
                    with lc3:
                         st.markdown(f"**[🎓 Coursera / Udemy](https://www.google.com/search?q=site:coursera.org+OR+site:udemy.com+{q_skill})**")

    # --- EXPORT REPORT ---
    st.divider()
    
    # Generate PDF
    pdf_bytes = ml_utils.generate_pdf_report(res)
    st.download_button(
        label="⬇️ Download Professional Report (PDF)",
        data=pdf_bytes,
        file_name="job_seeker_report.pdf",
        mime="application/pdf",
        type="primary"
    )
    # Assuming report_text is generated elsewhere or needs to be defined
    # For now, let's create a placeholder report_text
    report_text = f"Job Seeker Report:\nMatch Percentage: {res['match_percentage']:.0f}%\nMatched Skills: {', '.join(res['matching_hard'])}\nMissing Skills: {', '.join(res['missing_hard'])}"
    st.download_button("⬇️ Download Report (TXT)", report_text, file_name="report.txt")

# =============================================================================
def render_project_evaluation():
    if st.button("← Back"):
        st.session_state["page"] = "Home"
        st.rerun()
        
    st.title("🧪 Project Evaluation Lab")
    st.markdown("Analyze how your **Portfolio Projects** bridge the gap to your dream job.")
    st.info("Skills found in projects are treated as **Verified Skills** and can fill gaps in your CV.")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.subheader("1. Your CV")
        input_type = st.radio("CV Input", ["Text", "PDF"], key="pe_cv_input", horizontal=True)
        cv = ""
        if input_type == "Text":
            cv = st.text_area("Paste CV", height=150, key="pe_cv_text")
        else:
            uploaded_cv = st.file_uploader("Upload CV", type=["pdf"], key="pe_cv_pdf")
            if uploaded_cv:
                try: cv = ml_utils.extract_text_from_pdf(uploaded_cv)
                except: st.error("Error reading CV")
                
    with c2:
        st.subheader("2. Job Description")
        input_type_jd = st.radio("JD Input", ["Text", "PDF"], key="pe_jd_input", horizontal=True)
        jd = ""
        if input_type_jd == "Text":
            jd = st.text_area("Paste JD", height=150, key="pe_jd_text")
        else:
            uploaded_jd = st.file_uploader("Upload JD", type=["pdf"], key="pe_jd_pdf")
            if uploaded_jd:
                try: jd = ml_utils.extract_text_from_pdf(uploaded_jd)
                except: st.error("Error reading JD")

    with c3:
        st.subheader("3. Project Context")
        input_type_proj = st.radio("Project Input", ["Text", "PDF"], key="pe_proj_input", horizontal=True)
        proj = ""
        if input_type_proj == "Text":
            proj = st.text_area("Paste Project Desc", height=150, key="pe_proj_text", placeholder="Describe your projects, tech stack used, challenges solved...")
        else:
            uploaded_proj = st.file_uploader("Upload Project Docs", type=["pdf"], key="pe_proj_pdf")
            if uploaded_proj:
                try: proj = ml_utils.extract_text_from_pdf(uploaded_proj)
                except: st.error("Error reading Project")

    if st.button("🚀 Analyze Impact", type="primary", use_container_width=True):
        if not cv or not jd or not proj:
            st.warning("Please fill in all 3 sections.")
            return
            
        with st.spinner("Triangulating Skills..."):
            res = ml_utils.analyze_gap_with_project(cv, jd, proj)
            
            # Custom Results View for Project Lab
            st.divider()
            
            # Metrics
            m1, m2, m3 = st.columns(3)
            with m1: st.metric("Match Score", f"{res['match_percentage']:.0f}%")
            with m2: st.metric("Project Verified Skills", len(res["project_verified"]))
            with m3: st.metric("Remaining Gaps", len(res["missing_hard"]))
            
            st.divider()
            
            # Visualizing the Impact
            st.subheader("🏆 Project Impact Analysis")
            
            verified = res["project_verified"]
            if verified:
                st.success(f"**Verified by Projects:** {', '.join(verified)}")
                st.markdown("These skills were requested by the job and **proven** by your project experience.")
            else:
                st.warning("No direct skill matches found in the project description.")

            # Reuse standard result view for the rest
            render_results(res, jd)

if __name__ == "__main__":
    # Sidebar Global Controls
    with st.sidebar:
        st.divider()
        # Corrected Toggle Syntax
        show_project_eval = st.toggle("🧪 Project Evaluation", value=False, help="Analyze your projects alongside your CV")
        if show_project_eval:
             if st.button("Open Lab 🚀"):
                 st.session_state["page"] = "ProjectEval"
                 st.rerun()

    if st.session_state["page"] == "Debugger":
        render_debug_page()
    elif st.session_state["page"] == "ProjectEval":
        render_project_evaluation()
    else:
        render_home()
