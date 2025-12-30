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

## Machine Learning Stack

CareerMatch AI uses ML models optimized to prevent overfitting:

| Component | Technology |
|-----------|------------|
| **Skill Matching** | Random Forest (150 trees, depth 15, regularized) |
| **Text Processing** | TF-IDF (3000 features, trigrams, multilingual) |
| **Topic Discovery** | LDA Topic Modeling (50 iterations) |
| **Skill Extraction** | N-gram + FuzzyWuzzy (85% threshold) |
| **Entity Recognition** | NLTK NER (optimized for IT/EU CVs) |

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

## Acknowledgments

- **Streamlit Team** - Rapid development framework
- **Scikit-Learn** - ML algorithms
- **NLTK** - Natural Language Processing
- **Claude Opus 4 (thinking)** - Primary AI assistant for development and implementation
- **Gemini 3 Pro High** - Additional AI support for debugging

---

<div align="center">

**CareerMatch AI**

[Live Demo](https://dataminingiulm.streamlit.app/) | [GitHub](https://github.com/Giacomod2001/datamining)

</div>
