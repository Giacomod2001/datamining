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
        
        # EXPERIMENTAL FEATURE TOGGLE
        show_project_eval = st.toggle("Project Evaluation", value=False, help("Analyze your projects alongside your CV"))
        
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
    
    # Project Column (if enabled)
    project_text = ""
    if show_project_eval and c3:
        with c2: # Shift JD to c3, put Project in c2? User said "difianco a cv" (Use c2 for Project, c3 for JD)
             st.subheader("Project Context")
             input_type_proj = st.radio("Input Type", ["Text", "PDF"], key="proj_input", horizontal=True)
             if input_type_proj == "Text":
                 project_text = st.text_area("Paste Project Desc", height=200, key="proj_text", placeholder="Describe your projects...")
             else:
                 uploaded_proj = st.file_uploader("Upload Project (PDF)", type=["pdf"], key="proj_pdf")
                 if uploaded_proj:
                     try: 
                         project_text = ml_utils.extract_text_from_pdf(uploaded_proj)
                         st.success(f"Loaded {len(project_text)} chars")
                     except Exception as e:
                         st.error(f"Error: {e}")

    # JD Column (Position depends on toggle)
    jd_col = c3 if show_project_eval else c2
    with jd_col:
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
            if show_project_eval and project_text:
                 res = ml_utils.analyze_gap_with_project(cv, jd, project_text)
            else:
                 res = ml_utils.analyze_gap(cv, jd)
                 
            render_results(res, jd)

def render_results(res, jd_text=None):
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

    # --- WORD CLOUD SECTION ---
    if jd_text:
        st.divider()
        st.subheader("☁️ Job Keywords Cloud")
        with st.expander("Show Word Cloud", expanded=True):
            fig_wc = ml_utils.generate_wordcloud(jd_text)
            if fig_wc:
                st.pyplot(fig_wc)
            else:
                st.info("Install 'wordcloud' to see this feature.")

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

    # LEARNING PLAN (Simplified for brevity)
    if res["missing_hard"]:
        st.subheader("📚 Learning Actions")
        for skill in res["missing_hard"]:
            st.caption(f"Search for: **{skill}**")

    # --- EXPORT REPORT ---
    st.divider()
    report_text = f"Job Seeker Report:\nMatch Percentage: {res['match_percentage']:.0f}%\nMatched Skills: {', '.join(res['matching_hard'])}\nMissing Skills: {', '.join(res['missing_hard'])}"
    st.download_button("⬇️ Download Report (TXT)", report_text, file_name="report.txt")

if __name__ == "__main__":
    # Sidebar Global Controls
    with st.sidebar:
        st.divider()
        # The experimental features checkbox and project evaluation button are now handled within render_home.

    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
