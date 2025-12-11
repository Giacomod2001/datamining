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
    layout="wide",
    initial_sidebar_state="expanded"
)

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# =============================================================================
# DEBUGGER PAGE
# =============================================================================
def render_debug_page():
    if st.button("← Back to Analyzer"):
        st.session_state["page"] = "Home"
        st.rerun()
        
    st.title("🛠️ Model Debugger & Knowledge Base")
    
    rf_model, training_df = ml_utils.train_rf_model()
    
    if training_df is None:
        st.error("Model could not be trained. Check dependencies.")
        return

    tab1, tab2, tab3 = st.tabs(["📚 Training Database", "🌲 Model Info", "🧪 Live Test"])
    
    with tab1:
        st.subheader("Synthetic Training Database")
        st.info(f"The Random Forest model is trained on **{len(training_df)} samples** generated from the Skill Groups dictionary.")
        st.dataframe(training_df, use_container_width=True, height=400)
        
        label_counts = training_df['label'].value_counts().reset_index()
        label_counts.columns = ['Skill Label', 'Count']
        fig = px.bar(label_counts.head(20), x='Count', y='Skill Label', orientation='h', 
                     title="Top 20 Classes in Training Data", color='Count', color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Random Forest Architecture")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Algorithm", "RandomForestClassifier")
            st.metric("N Estimators", "100 Trees")
        with col2:
            st.metric("Vectorizer", "TF-IDF (1-2 ngrams)")
            st.metric("Classes", len(rf_model.classes_))
        
        st.subheader("All Skill Classes")
        st.write(list(rf_model.classes_))

    with tab3:
        st.subheader("Test the Classifier")
        text = st.text_input("Enter a phrase:", placeholder="e.g., 'I have 3 years of experience with Python and SQL'")
        
        if text:
            preds = rf_model.predict([text])
            probs = rf_model.predict_proba([text])[0]
            top_3_idx = probs.argsort()[-5:][::-1]
            
            st.markdown("### Top Predictions:")
            for i in top_3_idx:
                skill = rf_model.classes_[i]
                confidence = probs[i]
                if confidence > 0.01:
                    st.progress(confidence, text=f"**{skill}**: {confidence:.1%}")

# =============================================================================
# HOME PAGE
# =============================================================================
def render_home():
    with st.sidebar:
        st.title("🎯 Job Seeker Helper")
        st.caption("AI-Powered Skill Gap Analysis")
        st.divider()
        
        st.markdown("### About")
        st.info("Analyze your CV against job descriptions using Machine Learning to identify skill gaps and get personalized learning recommendations.")
        
        st.divider()
        with st.expander("🛠️ Developer Mode"):
            pwd = st.text_input("Password", type="password")
            if pwd == "1234":
                st.success("Access Granted")
                if st.button("Open Debugger"):
                    st.session_state["page"] = "Debugger"
                    st.rerun()

    st.title("🎯 Job Seeker Helper")
    st.markdown("**Analyze your CV against job descriptions to find skill gaps and get learning recommendations.**")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Your CV")
        cv_method = st.radio("Input:", ["Paste Text", "Upload PDF"], horizontal=True, key="cv_m")
        cv_text = ""
        if cv_method == "Paste Text":
            cv_text = st.text_area("Paste CV content:", height=250, key="cv_txt")
        else:
            cv_file = st.file_uploader("Upload CV (PDF)", type=["pdf"], key="cv_f")
            if cv_file:
                try:
                    cv_text = ml_utils.extract_text_from_pdf(cv_file)
                    st.success(f"✅ Extracted {len(cv_text)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")

    with col2:
        st.subheader("💼 Job Description")
        job_method = st.radio("Input:", ["Paste Text", "Upload PDF"], horizontal=True, key="job_m")
        job_text = ""
        if job_method == "Paste Text":
            job_text = st.text_area("Paste Job Description:", height=250, key="job_txt")
        else:
            job_file = st.file_uploader("Upload JD (PDF)", type=["pdf"], key="job_f")
            if job_file:
                try:
                    job_text = ml_utils.extract_text_from_pdf(job_file)
                    st.success(f"✅ Extracted {len(job_text)} characters")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.divider()
    if st.button("🔍 Analyze Skill Gap", type="primary", use_container_width=True):
        if not cv_text or not job_text:
            st.warning("⚠️ Please provide both CV and Job Description.")
            return
            
        with st.spinner("Training model and analyzing..."):
            results = ml_utils.analyze_gap(cv_text, job_text)
            
        render_results(results)

def render_results(results):
    st.divider()
    pct = results["match_percentage"]
    
    # Score Display
    col_score, col_msg = st.columns([1, 3])
    with col_score:
        if pct >= 80:
            st.success(f"## {pct:.0f}%")
        elif pct >= 60:
            st.warning(f"## {pct:.0f}%")
        else:
            st.error(f"## {pct:.0f}%")
    with col_msg:
        if pct >= 80:
            st.success("🎉 Excellent match! You have most required skills.")
        elif pct >= 60:
            st.warning("👍 Good match. A few skills to learn.")
        else:
            st.error("📚 Skill gap detected. See recommendations below.")

    st.divider()
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.subheader("✅ You Have")
        for s in sorted(results["matching"]):
            st.markdown(f"- {s}")
        if not results["matching"]:
            st.caption("None detected")
            
    with c2:
        st.subheader("❌ You Need")
        for s in sorted(results["missing"]):
            st.markdown(f"- **{s}**")
        if not results["missing"]:
            st.success("All skills matched!")
            
    with c3:
        st.subheader("➕ Bonus Skills")
        for s in sorted(results["extra"]):
            st.markdown(f"- {s}")
        if not results["extra"]:
            st.caption("None")

    if results["missing"]:
        st.divider()
        st.subheader("📚 Personalized Learning Plan")
        for skill in sorted(results["missing"]):
            res = constants.LEARNING_RESOURCES.get(skill, constants.DEFAULT_RESOURCE)
            with st.expander(f"🎓 {skill} ({res['time']})"):
                st.markdown(f"**Difficulty:** {res['level']}")
                st.markdown("**Courses:**")
                for c in res['courses']:
                    st.markdown(f"- {c}")
                st.info(f"💡 **Project Idea:** {res['project']}")

# =============================================================================
# ROUTER
# =============================================================================
if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
