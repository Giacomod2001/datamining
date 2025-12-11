import streamlit as st
import pandas as pd
import plotly.express as px
import styles_config
import constants
import ml_utils

# =============================================================================
# PAGE CONFIG & STATE
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
    styles_config.inject_custom_css()
    
    # Back Button
    if st.button("← Back to Analyze"):
        st.session_state["page"] = "Home"
        st.rerun()
        
    st.title("🛠️ Model Debugger & Database")
    
    # Train Model to get data
    rf_model, training_df = ml_utils.train_rf_model()
    
    if training_df is None:
        st.error("Model could not be trained. Check dependencies.")
        return

    # Tabs
    tab1, tab2, tab3 = st.tabs(["📚 Knowledge Database", "🌲 Random Forest Model", "🧪 Live Test"])
    
    # 1. DATABASE VISUALIZATION
    with tab1:
        st.subheader("Synthetic Training Database")
        st.markdown(f"The model is trained on **{len(training_df)} samples** generated from the Skill Groups.")
        
        # Show Table
        st.dataframe(training_df, use_container_width=True, height=400)
        
        # Stats
        label_counts = training_df['label'].value_counts().reset_index()
        label_counts.columns = ['Skill Label', 'Count']
        fig = px.bar(label_counts.head(20), x='Count', y='Skill Label', orientation='h', title="Top 20 Classes in Training Data")
        st.plotly_chart(fig, use_container_width=True)

    # 2. MODEL INFO
    with tab2:
        st.subheader("Model Architecture")
        st.json({
            "Type": "RandomForestClassifier",
            "N Estimators": 100,
            "Vectorizer": "TfidfVectorizer (ngram 1-2)",
            "Classes Detected": len(rf_model.classes_)
        })
        
        st.subheader("Class Labels")
        st.write(rf_model.classes_)

    # 3. LIVE TEST
    with tab3:
        st.subheader("Test the Classifier")
        text = st.text_input("Enter a phrase (e.g. 'I have experience with Python and SQL')")
        
        if text:
            # Predict
            preds = rf_model.predict([text])
            probs = rf_model.predict_proba([text])[0]
            
            # Show Top 3 Probabilities
            top_3_idx = probs.argsort()[-3:][::-1]
            
            st.markdown("### Prediction:")
            for i in top_3_idx:
                skill = rf_model.classes_[i]
                confidence = probs[i]
                st.markdown(f"- **{skill}**: {confidence:.2%}")

# =============================================================================
# HOME PAGE (Main App)
# =============================================================================
def render_home():
    styles_config.inject_custom_css()
    
    with st.sidebar:
        st.title("🎯 Job Seeker")
        st.info("Analysis powered by **Random Forest**")
        st.markdown("---")
        
        # Debugger Access
        with st.expander("🛠️ Developer Options"):
            pwd = st.text_input("Admin Password", type="password")
            if pwd == "1234":
                if st.button("Open Debugger"):
                    st.session_state["page"] = "Debugger"
                    st.rerun()

    st.title("🎯 Job Seeker Helper")
    st.markdown("""
    <div class="linkedin-card">
        <h3>CV vs Job Description Analysis</h3>
        <p>Uses a Random Forest model to detect skills and identify gaps.</p>
    </div>
    """, unsafe_allow_html=True)

    # Input columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 Your CV")
        cv_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="cv_method", horizontal=True)
        cv_text = ""
        if cv_input == "Paste Text":
            cv_text = st.text_area("Paste your CV here:", height=250)
        else:
            cv_file = st.file_uploader("CV PDF", type=["pdf"])
            if cv_file:
                try:
                    cv_text = ml_utils.extract_text_from_pdf(cv_file)
                    st.success(f"Loaded {len(cv_text)} chars")
                except: st.error("Error reading PDF")

    with col2:
        st.markdown("### 💼 Job Description")
        job_input = st.radio("Input method:", ["Paste Text", "Upload PDF"], key="job_method", horizontal=True)
        job_text = ""
        if job_input == "Paste Text":
            job_text = st.text_area("Paste JD here:", height=250)
        else:
            job_file = st.file_uploader("Job PDF", type=["pdf"])
            if job_file:
                try:
                    job_text = ml_utils.extract_text_from_pdf(job_file)
                    st.success(f"Loaded {len(job_text)} chars")
                except: st.error("Error reading PDF")

    if st.button("🔍 Run Analysis", type="primary", use_container_width=True):
        if not cv_text or not job_text:
            st.warning("Please provide both texts.")
            return
            
        with st.spinner("Training RF Model & Analyzing..."):
            results = ml_utils.analyze_gap(cv_text, job_text)
            
        render_results(results)

def render_results(results):
    st.divider()
    pct = results["match_percentage"]
    
    st.markdown(f"""
    <div class="linkedin-card" style="border-left: 8px solid {styles_config.PRIMARY_COLOR};">
        <h1 style="color: {styles_config.PRIMARY_COLOR}; margin:0;">{pct:.0f}% Match</h1>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### ✅ Skills Found")
        if results["matching"]:
             # Pill badges
            badges = "".join([f"<span style='background:#e7f3ff; color:#0077b5; padding:4px 8px; border-radius:12px; margin-right:5px; display:inline-block; margin-bottom:5px; font-weight:600;'>{s}</span>" for s in sorted(results["matching"])])
            st.markdown(badges, unsafe_allow_html=True)
        else: st.write("None")
        
    with c2:
        st.markdown("### ❌ Missing Skills")
        if results["missing"]:
            badges = "".join([f"<span style='background:#ffe7e7; color:#d11124; padding:4px 8px; border-radius:12px; margin-right:5px; display:inline-block; margin-bottom:5px; font-weight:600;'>{s}</span>" for s in sorted(results["missing"])])
            st.markdown(badges, unsafe_allow_html=True)
        else: st.success("All skills matched!")

    if results["missing"]:
        st.divider()
        st.subheader("📚 Recommended Learning")
        for skill in sorted(results["missing"]):
            res = constants.LEARNING_RESOURCES.get(skill, constants.DEFAULT_RESOURCE)
            with st.expander(f"Learn: {skill}"):
                st.write(f"**Courses:** {', '.join(res['courses'])}")
                st.write(f"**Project:** {res['project']}")

# =============================================================================
# ROUTER
# =============================================================================
if __name__ == "__main__":
    if st.session_state["page"] == "Debugger":
        render_debug_page()
    else:
        render_home()
