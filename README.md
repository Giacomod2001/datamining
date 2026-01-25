# CareerMatch AI

> Professional Career Analytics Toolkit: Multi-factor match scoring, advanced skill gap analysis, ATS-optimized CV Builder, and personal AI consultation. Built on solid Data Mining (KDD) principles.

⚠️ **Beta Notice**: This application is under active development. A **0.0% match score** may indicate that your specific industry or niche is not yet fully mapped in our Knowledge Base. Please contact the development team for support.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-PolyForm--NC-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.1-0077B5?style=flat)](README.md)

---

## Live Demo

**[Access CareerMatch AI Dashboard](https://dataminingiulm.streamlit.app/)**

**Version 3.1 Highlights**:

- **Ruben AI Consultant**: Integrated sidebar assistant with **6-language support** (EN, IT, ES, FR, DE, PT)
- **Harmonized Scoring**: Unified **65/20/15** matching engine (Skills/Semantics/Education) across all modules
- **Enhanced Intelligence**: Expanded database featuring **950+ keywords** and **230+ job archetypes**
- **Improved PDF Handling**: Migrated to `pypdf` for better stability and performance
- **Comprehensive Test Suite**: 18 automated tests covering scoring, multilingual support, and AI assistant

---

## Core Methodology

**CareerMatch AI** bridges the gap between candidates and complex recruitment algorithms using structured **Knowledge Discovery in Databases (KDD)**.

### Platform Modules

| **Module** | **Core Function** |
| ----------- | --------------- |
| **Career Discovery** | Exploratory search engine matching lifestyle preferences with job archetypes |
| **CV Builder** | ATS-compliant document generator with real-time semantic suggestions |
| **CV Analysis** | Precision evaluation engine using weighted Cosine Similarity and Gap Analysis |
| **Ruben Assistant** | Professional AI consultant providing contextual help and multilingual support |
| **Dev Console** | Full-stack transparency module ("Glass Box") to inspect ML logic and raw vectors |

---

## Installation

### Local Deployment

```bash
# 1. Clone the repository
git clone https://github.com/Giacomod2001/datamining.git
cd datamining

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch application
streamlit run app.py
```

The application will be accessible at `http://localhost:8501`.

---

## Data Mining Process (KDD Implementation)

| Step | Project Implementation |
| ---- | -------------- |
| **1. Data Cleaning** | Text normalization, noise filtering, and pypdf extraction |
| **2. Data Integration** | Merging CV, Job Description, and internal Knowledge Base |
| **3. Data Selection** | Targeted extraction of professional competencies and education |
| **4. Data Transformation** | TF-IDF vectorization and N-Gram expansion (Unigrams to Trigrams) |
| **5. Data Mining** | Random Forest (Classification), K-Means (Clustering), and LDA (Topic Modeling) |
| **6. Pattern Evaluation** | Multi-factor match scoring and Keyword Gap Analysis |
| **7. Knowledge Presentation** | Professional Dashboard with interactive Plotly analytics |

---

## Architecture

Our **Unified Multi-Factor Scoring (v3.1)** calculates compatibility based on a weighted composite formula:

1. **Skill Match (65%)**: Evaluates direct, inferred, and transferable skills
2. **Semantic Context (20%)**: Uses LSA to understand the underlying professional context
3. **Education Optimization (15%)**: Assesses degree relevance with recency scaling

---

## Project Structure

```
datamining/
├── app.py              # Main Streamlit application
├── ml_utils.py         # Core ML functions (scoring, gap analysis, Ruben AI)
├── knowledge_base.py   # Job archetypes, skill clusters, inference rules
├── constants.py        # Global constants and configurations
├── styles.py           # CSS styling for Streamlit
├── requirements.txt    # Python dependencies
├── test_*.py           # Automated test suite (18 tests)
├── LICENSE             # PolyForm Noncommercial License
└── README.md           # This documentation
```

---

## Testing

Run the automated test suite:

```bash
pytest test_scoring.py test_multilingual.py test_ruben.py test_deep.py -v
```

---

## Authors & Contributors

This project is the result of a collaborative effort at **IULM University (A.Y. 2025-2026)**:

- **Giacomo Dell'Acqua** - Lead UI/UX Designer & System Architect
- **Luca Tallarico** - Data Scientist (ML & NLP Implementation)
- **Ruben Scoletta** - QA Engineer & Technical Documentation

---

## License

Subject to the **PolyForm Noncommercial License 1.0.0**. Professional and commercial usage requires explicit authorization.

[Live Demo](https://dataminingiulm.streamlit.app/) | [GitHub](https://github.com/Giacomod2001/datamining)
