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
    st.subheader("Inference Rules (Logic)")
    st.write(constants.INFERENCE_RULES)
    st.subheader("Skill Database")
    st.dataframe(df, use_container_width=True)

# =============================================================================
# MAIN UI
# =============================================================================
def render_home():
    with st.sidebar:
        st.title("🎯 Job Seeker Helper")
        st.info("Now with **Smart Inference**:\n\nIf you list 'BigQuery', we know you know 'Cloud Computing'.")
        st.divider()
        if st.toggle("Developer Mode"):
             if st.button("Open Debugger"):
                st.session_state["page"] = "Debugger"
                st.rerun()

    st.title("🎯 Job Seeker Helper")
    st.markdown("Analyze your CV against job descriptions. **Soft skills are evaluated separately.**")
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
    
    # Score
    col1, col2 = st.columns([1, 4])
    with col1:
        color = "green" if pct >= 80 else "orange" if pct >= 60 else "red"
        st.markdown(f"<h1 style='color:{color}'>{pct:.0f}%</h1>", unsafe_allow_html=True)
        st.caption("Technical Match Score")
    with col2:
        if pct >= 80: st.success("Great technical match!")
        elif pct >= 60: st.warning("Good match, check missing skills.")
        else: st.error("Significant technical gap.")

    # HARD SKILLS GRID
    st.subheader("🛠️ Technical Skills (Hard Skills)")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### ✅ Matched")
        for s in res["matching_hard"]: st.write(f"- {s}")
        if not res["matching_hard"]: st.caption("None")
        
    with c2:
        st.markdown("#### ❌ Missing")
        for s in res["missing_hard"]: st.write(f"- **{s}**")
        if not res["missing_hard"]: st.success("All clear!")

    with c3:
        st.markdown("#### ➕ Bonus")
        for s in res["extra_hard"]: st.write(f"- {s}")

    # SOFT SKILLS
    st.divider()
    st.subheader("🗣️ Soft Skills (Interview Check)")
    st.info("Soft skills like Leadership or Communication are hard to judge from text alone. These are often evaluated during the interview.")
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown("**Mentioned in JD:**")
        required_soft = res["matching_soft"] | res["missing_soft"]
        if required_soft:
            for s in required_soft:
                # Check if user has it
                check = "✅" if s in res["matching_soft"] else "⬜"
                st.write(f"{check} {s}")
        else:
            st.caption("No soft skills explicitly mentioned.")
            
    # LEARNING PLAN
    if res["missing_hard"]:
        st.divider()
        st.subheader("📚 Learning Recommendations")
        for s in res["missing_hard"]:
            r = constants.LEARNING_RESOURCES.get(s, constants.DEFAULT_RESOURCE)
            with st.expander(f"Learn {s}"):
                st.write(r["courses"])

if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
