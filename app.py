import streamlit as st
import pandas as pd
import plotly.express as px
import constants
import ml_utils

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
    
    _, df = ml_utils.train_rf_model()
    st.subheader("Inference Rules")
    st.write(constants.INFERENCE_RULES)
    st.subheader("Clusters")
    st.write(constants.SKILL_CLUSTERS)
    st.subheader("Project Based Skills")
    st.write(constants.PROJECT_BASED_SKILLS)
    st.subheader("Database")
    st.dataframe(df, use_container_width=True)

# =============================================================================
# MAIN UI
# =============================================================================
def render_home():
    with st.sidebar:
        st.title("🎯 Job Seeker Helper")
        st.info("Features:\n- **Smart Inference** (BigQuery → Cloud)\n- **Transferable Skills** (Looker → Power BI)\n- **Project Review** (Computer Vision)")
        st.divider()
        if st.toggle("Developer Mode"):
             if st.button("Open Debugger"):
                st.session_state["page"] = "Debugger"
                st.rerun()

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
            
        res = ml_utils.analyze_gap(cv, jd)
        render_results(res)

def render_results(res):
    st.divider()
    pct = res["match_percentage"]
    
    col1, col2 = st.columns([1, 4])
    with col1:
        color = "green" if pct >= 80 else "orange" if pct >= 60 else "red"
        st.markdown(f"<h1 style='color:{color}'>{pct:.0f}%</h1>", unsafe_allow_html=True)
        st.caption("Technical Match Score")
    with col2:
        if pct >= 80: st.success("Great match!")
        elif pct >= 60: st.warning("Good match.")
        else: st.error("Gaps detected.")

    st.subheader("🛠️ Technical Skills Analysis")
    
    # 5 Columns for: Matched, Transferable, Proj Review, Missing, Bonus
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        st.markdown("#### ✅ Matched")
        for s in res["matching_hard"]: st.write(f"- {s}")
        if not res["matching_hard"]: st.caption("-")
        
    with c2:
        st.markdown("#### ⚠️ Transferable")
        # .get() to avoid KeyError
        transferable = res.get("transferable", {})
        if transferable:
            for missing, present in transferable.items():
                st.write(f"- **{missing}**") 
                st.caption(f"(via {present})")
        else:
            st.caption("-")

    with c3:
        st.markdown("#### 📂 Portfolio")
        # Project based skills
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

    # SOFT SKILLS
    st.divider()
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.subheader("🗣️ Soft Skills (Interview)")
        required_soft = res["matching_soft"] | res["missing_soft"]
        if required_soft:
            for s in required_soft:
                check = "✅" if s in res["matching_soft"] else "⬜"
                st.write(f"{check} {s}")
        else:
            st.caption("No soft skills explicitly found.")
            
    with sc2:
         pass # Spacer

    # LEARNING PLAN
    if res["missing_hard"]:
        st.divider()
        st.subheader("📚 Learning Recommendations")
        for s in res["missing_hard"]:
            r = constants.LEARNING_RESOURCES.get(s, constants.DEFAULT_RESOURCE)
            with st.expander(f"Learn {s}"):
                # Fix: Iterate list properly
                courses = r.get("courses", [])
                st.write("**Courses:**")
                for c in courses:
                    st.markdown(f"- {c}")
                st.write(f"**Project:** {r.get('project', 'N/A')}")

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
