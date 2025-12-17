# Job Seeker Helper

## Overview

**Job Seeker Helper** is an advanced open-source analytics dashboard designed to bridge the semantic gap between Candidate Profiles (CVs) and Job Descriptions (JDs). Leveraging **Hierarchical Inference** and **Machine Learning** techniques, it goes beyond simple keyword matching to understand the *context* of a candidate's skillset—recognizing transferable skills, project-based competencies, and implicit knowledge without manual intervention.

This project demonstrates the application of Natural Language Processing (NLP) in the HR Tech domain, utilizing a modern Python stack to provide actionable career insights.

---

## Key Features

### Semantic & Hierarchical Inference
Unlike traditional Applicant Tracking Systems (ATS), this tool understands skill relationships through a custom inference engine.
- **Inference Engine**: Automatically deduces implicit skills (e.g., *BigQuery* implies *Cloud Computing* and *SQL*).
- **Transferable Logic**: Recognizes equivalent tools (e.g., *Looker* is treated as functionally equivalent to *Power BI*), marking them as "Transferable" rather than "Missing".

### Comprehensive Gap Analysis
- **Technical vs. Soft Skills**: Implements distinct evaluation pipelines for Hard Skills (Quantifiable) and Soft Skills (Behavioral).
- **Portfolio-Based Triggers**: Complex domains (e.g., *Computer Vision*, *System Design*) are flagged for **Portfolio Review** rather than binary rejection, acknowledging that deep expertise requires qualitative assessment.
- **Universal Domain Support**: Capable of analyzing roles across Tech, Business, Marketing, and Languages using TF-IDF fallback mechanisms for unsupported domains.
- **Bilingual Support (IT/EN)**: Native support for cross-language matching. You can upload an **Italian CV** and an **English JD** (or vice versa), and the system will correctly map skills like "Gestione Progetti" to "Project Management".

- **Smart Language Detection**: Automatically fills "Native" skills (e.g., Italian) by analyzing CV context, removing bias for native speakers who omit language proficiency.

### Visual Analytics & Advanced Mining
- **Knowledge Graph (Developer Mode)**: Interactive visualization of the skill ontology using `graphviz`, showing hierarchical relationships (e.g., BigQuery → SQL).
- **Fuzzy Matching**: Implements `thefuzz` (Levenshtein distance) to handle typos in CVs (e.g., "Phyton" is correctly mapped to "Python").
- **Match Gauge**: Interactive Plotly chart for instant score assessment.
- **Professional PDF Reports**: Download a comprehensive analysis report including skill breakdowns, match scores, and a personalized learning plan with actionable links.

### Project Evaluation (NEW)
Validate your skills through practical experience.
- **Portfolio Triangulation**: Upload or paste project descriptions to prove skills missing in your CV.
- **Project verified Skills**: Skills confirmed by projects are highlighted as "Project Verified" and contribute to the final match score.
- **3-Column Dynamic Layout**: Toggle the feature to add a dedicated "Project Context" column to the main interface.

### Actionable Learning Pathways
- **Dynamic Resource Generation**: For every missing skill, the system generates a personalized Action Plan:
  - **🔍 Google Search**: Targeted queries for quick tutorials.
  - **📺 YouTube Educational Content**: Direct links to video-based learning.
  - **🎓 MOOC Hub**: Simultaneous search across Coursera, Udemy, and LinkedIn Learning.

### Secure Developer Environment
- **Encrypted Debugger**: Allows inspection of the internal decision-making logic, inference rules, and dataset through a password-protected interface, ensuring transparency in the AI decision process.

---

## Tech Stack

The application is built using a robust, modern Python stack:

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF_Parsing-red?style=for-the-badge)

---

## Installation & Setup

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

## Usage Manual

1. **Input Data**:
   - **CV Section**: Upload your formatted CV (PDF) or paste raw text.
   - **Job Description**: Upload the target JD (PDF) or paste raw text.
   - **(Optional) Project Evaluation**: Toggle this in the sidebar to add a column for your portfolio text.

2. **Analyze**:
   - Click the **"🔍 Analyze"** button to initiate the NLP pipeline.

3. **Review Results**:
   - **Match Score**: A weighted percentage indicating technical fit (boosted by project experience).
   - **Skill Breakdown**:
     - **Matched**: Skills present in both documents.
     - **Project Boost**: Skills validated by your portfolio projects.
     - **Transferable**: Skills possessed that substitute requirements.
     - **Missing**: Critical gaps with personalized action plans.

4. **Developer Options**:
   - Access the Sidebar and toggle **"Developer Mode"**.
   - Input Credential: **`1234`**.

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## Acknowledgments

- **Streamlit Team**: For the rapid application development framework.
- **Open Source Community**: For the continuous maintenance of `scikit-learn` and NLP libraries.
