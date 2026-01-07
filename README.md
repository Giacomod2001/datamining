# CareerMatch AI

> AI-Powered CV-to-Job Matching Platform

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0-0077B5?style=flat)](CHANGELOG.md)

---

## Live Demo

**[Try CareerMatch AI Now](https://dataminingiulm.streamlit.app/)**

Click "Try Demo" to see the app in action with sample data.

---

## What is CareerMatch AI?

**CareerMatch AI** is an intelligent analytics platform that uses **Machine Learning** and **NLP** to analyze the compatibility between your CV and job postings.

### Key Features

| Feature | Description |
|---------|-------------|
| **Match Score** | AI-based CV-Job compatibility score |
| **Transferable Skills** | Automatic recognition of equivalent skills |
| **Gap Analysis** | Identifies missing skills to develop |
| **CV Builder** | Create professional CVs with smart skill suggestions |
| **Cover Letter AI** | Intelligent cover letter evaluation |
| **Career Compass** | Alternative role suggestions based on your profile |
| **Learning Path** | Action plan with learning resources |

---

## Quick Start

### Option 1: Online Demo (Zero Installation)

Try directly: **[dataminingiulm.streamlit.app](https://dataminingiulm.streamlit.app/)**

### Option 2: Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/Giacomod2001/datamining.git && cd datamining

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## Data Mining Techniques

This project implements the following Data Mining and Text Analytics techniques from the university course.

### Knowledge Discovery Process (KDD)

The application follows the classic KDD pipeline:

| Step | Implementation |
|------|----------------|
| **1. Data Cleaning** | Text preprocessing, lowercase, noise removal |
| **2. Data Integration** | Merge CV + Job Description + Portfolio |
| **3. Data Selection** | Extract relevant sections |
| **4. Data Transformation** | TF-IDF vectorization |
| **5. Data Mining** | Classification, Clustering, Topic Modeling |
| **6. Pattern Evaluation** | Match scoring, confidence calculation |
| **7. Knowledge Presentation** | Dashboard, charts, reports |

### Machine Learning Algorithms

| Technique | Algorithm | Course Reference |
|-----------|-----------|------------------|
| **Classification** | Random Forest (150 trees) | "Classification and Regression" |
| **Text Vectorization** | TF-IDF (3000 features, trigrams) | "Word Vector Representation" |
| **Partitioning Clustering** | K-Means | "Clustering Techniques" |
| **Hierarchical Clustering** | Agglomerative (Ward linkage) | "Hierarchical Clustering" |
| **Topic Modeling** | LDA (Latent Dirichlet Allocation) | "Topic Model" |
| **Dimensionality Reduction** | PCA (2D visualization) | "Dimensionality Reduction" |
| **Information Extraction** | N-gram matching + Fuzzy | "Information Extraction" |

### Text Mining Pipeline

```
Input Text --> Tokenization --> N-gram Generation --> TF-IDF --> ML Model --> Output
                   |                 |
                Unigrams          Bigrams/Trigrams
```

Key techniques:
- **TF-IDF**: Term Frequency-Inverse Document Frequency for text representation
- **N-grams**: Capture compound skills like "machine learning"
- **Fuzzy Matching**: Handle typos with 85% Levenshtein threshold

---

## How It Works

1. **Upload CV** - PDF or text
2. **Add Job Description** - From any job board
3. **Analyze** - AI processes the documents
4. **Explore Results** - Match score, gap analysis, suggestions

### Skill Legend

| Tag | Meaning |
|-----|---------| 
| Matched | Skill present in CV |
| Transferable | Equivalent skill recognized |
| Project | Verified through portfolio |
| Missing | Gap to fill |
| Bonus | Extra competitive advantage |

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

MIT License - see [LICENSE](LICENSE) for details.

---

## Authors

This project was developed as a collaborative effort with the following primary responsibilities:

- **Giacomo Dellacqua** - Project Design (UI/UX & Application Architecture)
- **Luca Tallarico** - Machine Learning & NLP/Text Mining
- **Ruben Scoletta** - Testing, Quality Assurance & Documentation

---

## Acknowledgments

- **Streamlit Team** - Rapid development framework
- **Scikit-Learn** - ML algorithms
- **NLTK** - Natural Language Processing
- **Claude Opus 4 (thinking)** - Primary AI assistant for development and implementation
- **Gemini 3 Pro High** - Additional AI support for debugging
- **Antigravity** - Agentic development support

---

<div align="center">

**CareerMatch AI**

Data Mining & Text Analytics Project

IULM University - A.Y. 2025-2026

[Live Demo](https://dataminingiulm.streamlit.app/) | [GitHub](https://github.com/Giacomod2001/datamining)

</div>
