import streamlit as st
import pandas as pd
import styles_config
import constants
import ml_utils

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Job Seeker Helper",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# SIDEBAR
# =============================================================================
def render_sidebar():
    with st.sidebar:
        st.title("🎯 Job Seeker Helper")
        st.caption("AI-Powered Gap Analysis")
        st.markdown("---")
        
        st.markdown("### 🔍 How It Works")
        st.info("""
        **1. Skill Detection**
        We use NLP & Machine Learning to extract skills from your CV and the Job Description.
        
        **2. Gap Analysis** 
        We compare them to find what you have and what you miss.
        
        **3. Recommendations**
        Get personalized learning resources for every missing skill.
        """)
        
        st.markdown("---")
        
        # Debug Mode (Hidden)
        with st.expander("🛠️ Debug Mode"):
            password = st.text_input("Password:", type="password", key="debug_pwd")
            if password == "1234":
                st.success("Access Granted")
                debug_on = st.checkbox("Show Detection Details")
                st.session_state["ml_debug"] = debug_on

# =============================================================================
# MAIN INTERFACE
# =============================================================================
def main():
    styles_config.inject_custom_css()
    render_sidebar()

    st.title("🎯 Job Seeker Helper")
    st.markdown("""
    <div class="linkedin-card">
        <h3>Analyze your CV against job descriptions</h3>
        <p>Find skill gaps and get personalized learning recommendations to land your dream job.</p>
    </div>
    """, unsafe_allow_html=True)

    # Input columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 Your CV")
        cv_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="cv_method", horizontal=True)
        
        cv_text = ""
        if cv_input == "Paste Text":
            cv_text = st.text_area("Paste your CV here:", height=250, placeholder="Paste your CV content...")
        else:
            cv_file = st.file_uploader("Upload CV PDF", type=["pdf"], key="cv_pdf")
            if cv_file:
                try:
                    cv_text = ml_utils.extract_text_from_pdf(cv_file)
                    st.success(f"✅ Extracted {len(cv_text)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")

    with col2:
        st.markdown("### 💼 Job Description")
        job_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="job_method", horizontal=True)
        
        job_text = ""
        if job_input == "Paste Text":
            job_text = st.text_area("Paste job description:", height=250, placeholder="Paste job description...")
        else:
            job_file = st.file_uploader("Upload Job PDF", type=["pdf"], key="job_pdf")
            if job_file:
                try:
                    job_text = ml_utils.extract_text_from_pdf(job_file)
                    st.success(f"✅ Extracted {len(job_text)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")

    # Analyze Button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("magnifying_glass Analyze Skill Gap", type="primary", use_container_width=True):
        if not cv_text or not job_text:
            st.warning("⚠️ Please provide both CV and Job Description")
            return
            
        with st.spinner("Analyzing..."):
            # Run ML with debug if enabled
            if st.session_state.get("ml_debug"):
                _, debug_data = ml_utils.ml_skill_matcher(cv_text, return_debug=True)
                st.session_state["debug_data"] = debug_data
            
            results = ml_utils.analyze_gap(cv_text, job_text)
        
        render_results(results)

# =============================================================================
# RESULTS RENDERING
# =============================================================================
def render_results(results):
    st.divider()
    pct = results["match_percentage"]
    
    # Header Card
    color_class = "green" if pct >= 80 else "orange" if pct >= 60 else "red"
    msg = "Excellent match!" if pct >= 80 else "Good match!" if pct >= 60 else "Skills gap detected."
    
    st.markdown(f"""
    <div class="linkedin-card" style="border-left: 5px solid {styles_config.PRIMARY_COLOR};">
        <div style="display: flex; align-items: center; gap: 20px;">
            <h1 style="margin: 0; font-size: 3.5rem; color: {styles_config.PRIMARY_COLOR};">{pct:.0f}%</h1>
            <div>
                <h3 style="margin: 0;">{msg}</h3>
                <p style="margin: 0;">Match Score based on skills analysis</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Skills Grid
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### ✅ You Have")
        if results["matching"]:
            for s in sorted(results["matching"]):
                st.markdown(f"- {s}")
        else:
            st.markdown("*None found*")
            
    with c2:
        st.markdown("#### ❌ You Need")
        if results["missing"]:
            for s in sorted(results["missing"]):
                st.markdown(f"- :red[{s}]")
        else:
            st.success("None! You have everything.")
            
    with c3:
        st.markdown("#### ➕ Bonus")
        if results["extra"]:
            st.markdown(", ".join(sorted(results["extra"])))
        else:
            st.markdown("*No extra skills*")

    # Learning Plan
    if results["missing"]:
        st.divider()
        st.subheader("📚 Learning Plan")
        
        for skill in sorted(results["missing"]):
            res = constants.LEARNING_RESOURCES.get(skill, constants.DEFAULT_RESOURCE)
            
            with st.expander(f"🎓 Learn **{skill}** ({res['time']})"):
                c_left, c_right = st.columns(2)
                with c_left:
                    st.markdown("**Best Courses:**")
                    for course in res['courses']:
                        st.markdown(f"• {course}")
                    st.markdown(f"**Certification:** {res['cert']}")
                    
                with c_right:
                    st.markdown("**Practice:**")
                    st.markdown(res['practice'])
                    st.info(f"💡 **Project:** {res['project']}")

    # Debug Section
    if st.session_state.get("ml_debug") and "debug_data" in st.session_state:
        st.divider()
        st.subheader("🛠️ ML Debug Info")
        
        data = st.session_state["debug_data"]
        cols = st.columns(2)
        with cols[0]:
            st.write("Top extracted TF-IDF features:", data.get("features", [])[:10])
        with cols[1]:
            scores = data.get("scores", {})
            st.write("Skill Scores:", {k: f"{v:.3f}" for k, v in scores.items() if v > 0})

if __name__ == "__main__":
    main()
