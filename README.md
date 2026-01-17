# CareerMatch AI

> AI-powered job search toolkit: CV-JD match scoring, skill gap analysis, smart CV Builder with suggestions, lifestyle-based Career Discovery, and personalized learning paths. Built with ML/NLP on Streamlit.

> ⚠️ **Beta Notice**: This app is continuously updated. A **0% match** may indicate that your sector/role is not yet covered by our models. Please try again later or contact us at [dellacquagiacomo@gmail.com](mailto:dellacquagiacomo@gmail.com) for support.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-PolyForm--NC-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.1-0077B5?style=flat)](README.md)

---

## Live Demo

**[Try CareerMatch AI Now](https://dataminingiulm.streamlit.app/)**

**New Features**:

- **Refined UI/UX**: New Customer Journey-oriented Sidebar with visual cues.
- **Enhanced Knowledge Base**: Expanded to **950+ Killer Keywords** and **230+ Job Archetypes**.
- **Career Discovery**: Specialized module to find career paths based on lifestyle & preferences.
- **Advanced Match Engine**: Powered by TF-IDF, Cosine Similarity, and Jaccard Index.

---

## What is CareerMatch AI?

**CareerMatch AI** analyzes CV-Job compatibility using **ML/NLP**. Get match scores, discover transferable skills, and receive personalized learning paths. It acts as a bridge between candidates and ATS systems.

### Key Metrics

- **950+** Killer Keywords mapped
- **230+** Job Archetypes defined
- **25+** Industry Sectors coverage

### Key Features

| **Feature** | **Description** |
|---------|-------------|
| **CV Builder (v2.0)** | Interactive wizard to build professional CVs with real-time AI suggestions |
| **Match Score** | AI-based CV-Job compatibility score (0-100%) |
| **Gap Analysis** | Identifies missing hard/soft skills vs Job Description |
| **Career Compass** | Recommendation engine using **Jaccard Similarity** to suggest alternative roles |
| **Career Discovery** | Explore career paths based on lifestyle & work preferences (Remote, Creative, etc.) |
| **Developer Console** | "Glass Box" view to inspect ML logic, clusters, and raw vectors |

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

## App Structure & Modules

The application is composed of 4 main integrated environments, accessible via the ordered sidebar:

### 1. Home

The landing page featuring:

- Real-time Knowledge Base metrics.
- Direct funnels to the core modules.

### 2. Career Discovery

A lifestyle-based career explorer for users without a specific target job.

- **Mechanism**: Recommends roles based on preferences (e.g., Remote vs On-site, Creative vs Logical).
- **Integration**: Direct link to external job boards with seniority filters.

### 3. Smart CV Builder

An interactive wizard to create professional CVs from scratch.

- **Features**: Real-time AI suggestions based on target job roles.
- **Export**: Generates ATS-friendly PDF and TXT files.

### 4. CV Analysis (Evaluation Engine)

The core determination engine.

- **Inputs**: PDF or Text for both CV and JD.
- **Logic**: Performs Weighted Cosine Similarity and Keyword Gap Analysis.
- **Outputs**: Match Score, Missing Skills, and Seniority warning.

### 5. Developer Console (Debugger)

A transparent interface for examiners and developers.

- **Purpose**: Inspect the exact ML logic (TF-IDF vectors, Clustering, NLP tokens) behind every decision.
- **Access**: Located at the bottom of the sidebar (Teal button).

---

## Data Mining Techniques

This project implements the following Data Mining and Text Analytics techniques:

### Knowledge Discovery Process (KDD)

| Step | Implementation |
|------|----------------|
| **1. Data Cleaning** | Text preprocessing, lowercase, noise removal, PyPDF2 extraction |
| **2. Data Integration** | Merge CV + Job Description + Archetype Knowledge Base |
| **3. Data Selection** | Extract relevant sections (Skills, Experience, Education) |
| **4. Data Transformation** | TF-IDF vectorization, N-Gram generation |
| **5. Data Mining** | Classification (Random Forest), Clustering (K-Means), Similarity (Cosine/Jaccard) |
| **6. Pattern Evaluation** | Match scoring, confidence calculation, Gap Analysis |
| **7. Knowledge Presentation** | Streamlit Dashboard & Dynamic Visualizations |

### Advanced Machine Learning (v2.1)

#### 1. Hybrid Semantic Matching (TF-IDF + LSA)

Combines **Keyword Frequency (TF-IDF)** with **Latent Semantic Analysis (SVD)** to understand context.

- *Benefit*: Recognizes that "Data Analysis" matches "Business Intelligence" conceptually.
- *Weighting*: Balanced Precision (Keywords) + Context (Semantics).

#### 2. Archetype Fallback System

If a Job Description is sparse, the system "injects" missing implied skills from our **230+ Job Archetypes** database to provide a fairer analysis.

### Text Mining Pipeline

```text
Input Text --> Tokenization --> N-gram Generation --> TF-IDF --> ML Model --> Output
                   |                 |
                Unigrams          Bigrams/Trigrams
```

---

## Privacy

- **100% Local Processing** - No data leaves your computer (in local mode).
- **Stateless Session** - Data is wiped upon reload.
- **Open Source** - Transparent and verifiable code.

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

- **Giacomo Dell'Acqua** - Project Design (UI/UX & Application Architecture)
- **Luca Tallarico** - Machine Learning & NLP/Text Mining
- **Ruben Scoletta** - Testing, Quality Assurance & Documentation

---

<div align="center">

**CareerMatch AI**

Data Mining & Text Analytics Project

IULM University - A.Y. 2025-2026

[Live Demo](https://dataminingiulm.streamlit.app/) | [GitHub](https://github.com/Giacomod2001/datamining)

</div>
