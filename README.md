# 🎯 Job Seeker Helper

> **A Universal AI-Powered Career Analysis Tool**

**Job Seeker Helper** is an advanced open-source dashboard designed to bridge the semantic gap between Candidate Profiles (CVs) and Job Descriptions (JDs). Leveraging **Hierarchical Inference** and **Machine Learning**, it goes beyond simple keyword matching to understand the *context* of a candidate's skillset—recognizing transferable skills, project-based competencies, and implicit knowledge.

---

## 🚀 Key Features

### 🧠 Semantic & Hierarchical Inference
Unlike traditional ATS systems, this tool understands skill relationships.
- **Inference Engine**: Automatically deduces implicit skills (e.g., *BigQuery* $\rightarrow$ *Cloud Computing* & *SQL*).
- **Transferable Logic**: Recognizes equivalent tools (e.g., *Looker* $\approx$ *Power BI*), marking them as **"Transferable"** rather than "Missing".

### 📊 Comprehensive Gap Analysis
- **Technical vs. Soft Skills**: Distinct evaluation pipelines for Hard Skills (Quantifiable) and Soft Skills (Behavioral).
- **Portfolio-Based Triggers**: Complex domains (e.g., *Computer Vision*, *System Design*) are flagged for **Portfolio Review** rather than binary rejection.
- **Universal Domain Support**: Capable of analyzing roles across Tech, Business, Marketing, and Languages using TF-IDF fallback mechanisms.

### 🎓 Actionable Learning Pathways
- **Dynamic Resource Generation**: Instantly generates targeted search queries for missing skills across:
  - 🔍 **Google Search**
  - 📺 **YouTube Educational Content**
  - 🎓 **MOOC Platforms (Coursera/Udemy)**

### �️ Secure Developer Environment
- **Encrypted Debugger**: Inspect the internal decision-making logic, inference rules, and dataset through a password-protected interface.

---

## 💻 Tech Stack

The application is built using a robust, modern Python stack:

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF_Parsing-red?style=for-the-badge)

---

## �️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/job-seeker-helper.git
   cd job-seeker-helper
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

---

## 📖 Usage Manual

1. **Input Data**:
   - **CV Section**: Upload your formatted CV (PDF) or paste raw text.
   - **Job Description**: Upload the target JD (PDF) or paste raw text.

2. **Analyze**:
   - Click the **"🔍 Measure Matching"** button to initiate the NLP pipeline.

3. **Review Results**:
   - **Match Score**: A weighted percentage indicating technical fit.
   - **Skill Breakdown**:
     - ✅ **Matched**: Skills present in both documents.
     - ⚠️ **Transferable**: Skills you possess that strictly substitute requirements.
     - 📂 **Portfolio**: Advanced topics to discuss in an interview.
     - ❌ **Missing**: Critical gaps with associated learning resources.

4. **Developer Options**:
   - Access the Sidebar $\rightarrow$ Toggle **"Developer Mode"**.
   - Input Credential: **`1234`**.

---

## � License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- **Streamlit Team**: For the rapid application development framework.
- **Open Source Community**: For the continuous maintenance of `scikit-learn` and NLP libraries.
