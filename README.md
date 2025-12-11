# 🎯 Job Seeker Helper

**Universal CV Analyzer & Gap Matcher**

A smart, AI-powered Streamlit dashboard that analyzes your CV against Job Descriptions, detecting both technical gaps and transferable skills. Now supports **all domains** (Tech, Business, Languages, Marketing) and provides dynamic learning resources.

---

## ✨ Key Features

### 🧠 Intelligent Analysis
- **Hierarchical Inference**: Knows that `BigQuery` implies `Cloud Computing` and `SQL`.
- **Transferable Skills Logic**: If a job asks for `Power BI` but you know `Looker`, it's marked as **⚠️ Transferable** (Yellow) rather than Missing.
- **Generic Fallback**: Works for any job type (e.g., Zoology, Translation) by auto-extracting key terms if no standard skills are found.

### 🔍 Deep Insights
- **Hard vs. Soft Skills**: Separates technical requirements from behavioral traits (which are flagged for Interview discussion).
- **Project-Based Skills**: Complex domains like `Computer Vision` or `System Design` are suggested for **Portfolio Review** rather than simple keyword matching.
- **Dynamic Learning Resources**: Generates **one-click search links** (Google, YouTube, Coursera) for any missing skill.

### 🛠️ Developer Mode
- **Protected Debugger**: Access the internal logic (Inference Rules, Skill Clusters) via password protection.
- **Transparent Logic**: Visualize exactly *why* a skill was matched or inferred.

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/job-seeker-helper.git
   cd job-seeker-helper
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Dependencies include `streamlit`, `pandas`, `scikit-learn`, `plotly`, `PyPDF2`.*

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## 📖 Usage

1. **Upload your CV**: Supports PDF upload or text paste.
2. **Upload Job Description**: Supports PDF upload or text paste.
3. **Click "Measure Matching"**:
   - See your **Match Score** (weighted by transferable skills).
   - Review **Missing Skills** with direct learning links.
   - Check **Soft Skills** to prepare stories for your interview.
4. **Developer Mode**:
   - Toggle "Developer Mode" in the sidebar.
   - Enter Password: **`1234`**.
   - Explore the inference engine and database.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **NLP / ML**: `scikit-learn` (TF-IDF & Random Forest), Regex Patterns
- **PDF Parsing**: `PyPDF2`
- **Visualization**: `Plotly`, Streamlit Native Charts

---

## 🙏 Acknowledgments

- **Streamlit Community**: For the amazing layout primitives and theming support.
- **Scikit-Learn**: For the robust TF-IDF and Machine Learning capabilities.
- **Open Source**: Built with ❤️ using Python's open ecosystem.
