# CareerMatch AI

> AI-powered job search toolkit: CV-JD match scoring, skill gap analysis, smart CV Builder with suggestions, and personalized learning paths. Built with ML/NLP on Streamlit.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-PolyForm--NC-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.1-0077B5?style=flat)](README.md)

---

## Live Demo

**[Try CareerMatch AI Now](https://dataminingiulm.streamlit.app/)**

**New Features**:

- **Demo Mode**: Use "Load Demo" in the sidebar to populate the CV Builder. Click "Exit Demo" to clear data.
- **Improved Navigation**: Switch easily between "CV Builder" and "CV Evaluation" from the sidebar.

---

## What is CareerMatch AI?

**CareerMatch AI** analyzes CV-Job compatibility using **ML/NLP**. Get match scores, discover transferable skills, and receive personalized learning paths.

### Key Features

| **Feature** | **Description** |
|---------|-------------|
| **CV Builder (v2.0)** | Interactive wizard to build professional CVs with real-time AI suggestions |
| **Match Score** | AI-based CV-Job compatibility score (0-100%) |
| **Education-Aware** | Smart weighting of recent education degrees for career pathing |
| **Gap Analysis** | Identifies missing skills vs Job Description |
| **Career Compass** | Advanced role discovery using Skills + Education + Interests (Unlimited model) |
| **Psychometric Profile** | Silent Burnout & Resilience detection |

---

## Quick Start

### Option 1: Online Demo (Zero Installation)

Try directly: **[dataminingiulm.streamlit.app](https://dataminingiulm.streamlit.app/)**

### Option 2: Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/Giacomod2001/datamining.git
cd datamining

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## CV Builder Workflow

The application features a 4-step guided process:

1. **Personal Profile**: Enter details and professional summary.
    - *Smart Feature*: Paste a Job Description to get real-time optimization scoring.
2. **Skills & Competencies**: Select from 600+ database skills or add custom ones.
    - *AI Insight*: System suggests skills missing from your profile but required by the JD.
3. **Experience**: Add work history, projects, and education.
4. **Review & Export**: Download as TXT or PDF, or send directly to the Analysis Engine.

---

## Data Mining Techniques

This project implements the following Data Mining and Text Analytics techniques:

### Knowledge Discovery Process (KDD)

| Step | Implementation |
|------|----------------|
| **1. Data Cleaning** | Text preprocessing, lowercase, noise removal |
| **2. Data Integration** | Merge CV + Job Description + Portfolio |
| **3. Data Selection** | Extract relevant sections |
| **4. Data Transformation** | TF-IDF vectorization |
| **5. Data Mining** | Classification (Random Forest), Clustering (K-Means), Topic Modeling (LDA) |
| **6. Pattern Evaluation** | Match scoring, confidence calculation |
| **7. Knowledge Presentation** | Streamlit Dashboard & PDF Reports |

### Advanced Machine Learning (v2.1)

#### 1. Hybrid Semantic Matching (TF-IDF + LSA)

Combines **Keyword Frequency (TF-IDF)** with **Latent Semantic Analysis (SVD)** to understand context.

- *Benefit*: Recognizes that "Data Analysis" matches "Business Intelligence" conceptually, even if words differ.
- *Weighting*: 70% Precision (Keywords) + 30% Context (Semantics).

#### 2. Automatic Seniority Detection

Analyzes CV context (years of experience, keywords like "Head", "Junior") to determine the candidate's level.

- *Application*: Penalizes mismatches (e.g. Junior applying for Director) and filters external job searches automatically (e.g. searching for "Junior Data Scientist").

### Text Mining Pipeline

```
Input Text --> Tokenization --> N-gram Generation --> TF-IDF --> ML Model --> Output
                   |                 |
                Unigrams          Bigrams/Trigrams
```

---

## Privacy

- **100% Local Processing** - No data leaves your computer
- **Zero Data Collection** - We don't collect any information
- **Open Source** - Transparent and verifiable code

---

## Contributing

Contributions welcome! Open an Issue or Pull Request.

---

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

You are free to use, modify, and distribute this software for **non-commercial purposes only**.
Commercial use requires explicit written permission from the authors.

See [LICENSE](LICENSE) for full terms.

---

## Authors

This project was developed as a collaborative effort with the following primary responsibilities:

- **Giacomo Dellacqua** - Project Design (UI/UX & Application Architecture)
- **Luca Tallarico** - Machine Learning & NLP/Text Mining
- **Ruben Scoletta** - Testing, Quality Assurance & Documentation

---

<div align="center">

**CareerMatch AI**

Data Mining & Text Analytics Project

IULM University - A.Y. 2025-2026

[Live Demo](https://dataminingiulm.streamlit.app/) | [GitHub](https://github.com/Giacomod2001/datamining)

</div>
