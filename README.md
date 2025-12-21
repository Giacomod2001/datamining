# Job Seeker Helper

> AI-Powered Career Analytics for Smarter Job Applications

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0-0077B5?style=flat)](CHANGELOG.md)

---

## What's New in v2.0 Premium Edition

- **Demo Mode** - Try the app instantly with sample CV and job description
- **Premium UI** - LinkedIn-inspired dark theme with glassmorphism effects
- **Progress Tracking** - Animated progress bar during analysis
- **Enhanced UX** - Tooltips, how-it-works guide, better error messages
- **Animated Skill Tags** - Hover effects and gradient backgrounds
- **Formal Presentation** - Professional, clean interface

---

## Overview

**Job Seeker Helper** is an advanced AI-powered analytics platform that transforms how you approach job applications. By leveraging Natural Language Processing, Machine Learning, and Semantic Analysis, it provides intelligent insights into:

- **CV-Job Description Alignment** - Understand your fit percentage with precision
- **Skills Gap Analysis** - Identify missing competencies with learning pathways
- **Cover Letter Optimization** - Get actionable feedback on application quality
- **Career Path Discovery** - Explore alternative roles based on your skillset
- **Job Context Intelligence** - Decode what positions really need

Unlike traditional ATS systems that rely on simple keyword matching, our tool understands **semantic relationships**, recognizes **transferable skills**, and provides **personalized recommendations** for career growth.

---

## Key Features

### Intelligent Skill Analysis

**Semantic Inference Engine**
- Automatically deduces implicit skills (e.g., *BigQuery* infers *SQL*, *Cloud Computing*, *Data Science*)
- Recognizes tool equivalencies (*Looker Studio* = *Power BI*, *GA4* = *Google Analytics*)
- Marks similar tools as "Transferable" rather than "Missing"

**Comprehensive Gap Analysis**
- Separates technical and soft skills evaluation
- Portfolio-based verification for complex competencies
- Bilingual support (English/Italian) with automatic skill mapping
- Smart language detection for native proficiency

### Job Intelligence

**AI-Powered Context Analysis (LDA Topic Modeling)**
- Identifies key themes and focus areas from job descriptions
- Translates technical keywords into human-readable interpretations
- Provides visual summaries with color-coded skill tags
- Supports both English and Italian with localized insights

### Cover Letter Evaluation

**Multi-Dimensional Scoring System**
- **Keyword Coverage** (35%) - Technical skills mentioned vs. required
- **Soft Skills** (15%) - Behavioral competencies alignment
- **Length** (15%) - Optimal word count analysis (250-400 words)
- **Structure** (20%) - Professional formatting validation
- **Personalization** (15%) - Specific examples and customization

**Actionable Feedback**
- Strengths identification with evidence-based insights
- Improvement suggestions with specific recommendations
- Missing keywords highlighting for strategic additions
- Automatic language detection (English/Italian)

### Visual Analytics

**Interactive Dashboards**
- Real-time match score visualization with color-coded gauges
- Skill clustering using K-Means and Hierarchical methods
- Knowledge graph showing skill hierarchies and relationships

**Compact Tag-Based Display**
- Color-coded skill badges (Matched, Transferable, Project-verified, Missing, Bonus)
- Inline keyword tags for space-efficient display
- Visual legend in sidebar for quick reference

### AI Career Compass

**Intelligent Role Recommendations**
- Uses Cosine Similarity on TF-IDF vectors for role matching
- Suggests top 3 alternative career paths based on your skills
- Filters out redundant suggestions (current and target roles)
- Quality threshold (>30%) ensures relevant recommendations only

**Direct Job Search Integration**
- One-click access to Google Jobs, LinkedIn, Indeed Italia
- Pre-filled search queries for immediate application
- Targeted to Italian job market where relevant

### Project Evaluation

**Portfolio Triangulation**
- Upload project descriptions to validate missing skills
- Project-verified skills get highlighted and contribute to match score
- Dynamic 2-4 column layout adapts to enabled features
- Strategic interview preparation suggestions

### Learning Pathways

**Personalized Skill Development**
- Google Search links for tutorials and guides
- YouTube educational content for video learners
- MOOC platform searches (Coursera, Udemy, LinkedIn Learning)
- Curated resources for specific technologies

### Professional Reports

**Comprehensive Export Options**
- PDF reports with executive summary and detailed breakdowns
- Text reports in clean markdown format
- Includes CV match, cover letter analysis, and career recommendations
- Professional formatting for sharing with mentors or coaches

### Developer Mode

**Transparent AI Decision-Making**
- Password-protected debugger interface (default: `1234`)
- View inference rules and skill clusters
- Access to training data and knowledge base
- Topic modeling and NER analysis tools

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Core Framework | Streamlit, Python 3.8+ |
| Machine Learning | scikit-learn (TF-IDF, LDA, Clustering, Cosine Similarity) |
| NLP | NLTK (Named Entity Recognition, tokenization) |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Document Handling | PyPDF2, FPDF |
| Utilities | thefuzz (fuzzy matching), urllib |

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning)

### Quick Setup

1. **Clone or Download**
   ```bash
   git clone https://github.com/Giacomod2001/datamining.git
   cd datamining
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Application**
   ```bash
   streamlit run app.py
   ```

4. **Access Interface**
   - Open browser to `http://localhost:8501`
   - Application will auto-launch in default browser

---

## Usage Guide

### Basic Workflow

**Step 1: Prepare Documents**
- Format your CV (PDF or text)
- Obtain target job description (PDF or text)
- Optional: Prepare cover letter and project descriptions

**Step 2: Configure Analysis**

Enable optional features via sidebar toggles:
- **Project Evaluation** - Validate skills through portfolio
- **Cover Letter Analysis** - Get AI feedback on application letter

**Step 3: Upload and Analyze**
1. Upload CV in column 1
2. Upload optional Project/Cover Letter (if toggles enabled)
3. Upload Job Description in last column
4. Click "Analyze" button

**Step 4: Review Results**

The analysis provides:
- **Match Score** - Overall CV-JD alignment percentage
- **Cover Letter Score** - Application quality assessment (if enabled)
- **Skill Breakdown** - Color-coded tags showing:
  - Green = Matched skills
  - Yellow = Transferable skills (with source)
  - Blue = Project-verified skills
  - Red = Missing skills (to learn)
  - Gray = Bonus skills (competitive advantage)
- **Job Context** - What the position really seeks
- **Career Compass** - Alternative role suggestions
- **Learning Plans** - Resources for skill gaps

**Step 5: Export and Apply**
- Download PDF or Text report
- Use learning pathways to close skill gaps
- Improve cover letter based on suggestions
- Apply via integrated job board links

### Advanced Features

**Developer Mode Access**
1. Enable "Developer Mode" in sidebar
2. Enter password: `1234`
3. Click "Open Debugger"
4. Explore inference rules, clusters, and analysis internals

---

## Scoring Methodology

### CV Match Score
```
Score = (Direct Matches x 1.0) + (Transferable x 0.5) + (Projects x 0.3)
        ───────────────────────────────────────────────────────────────
                        Total Required Skills

Final Percentage = (Score / Total Required) x 100
```

### Cover Letter Score
```
Overall Score = (Keyword Coverage x 35%)
              + (Soft Skills x 15%)
              + (Length x 15%)
              + (Structure x 20%)
              + (Personalization x 15%)
```

**Grading Scale:**
- 80-100% = Excellent
- 60-79% = Good
- 0-59% = Needs Improvement

---

## Use Cases

- **Job Seekers** - Optimize applications for specific roles
- **Career Switchers** - Discover transferable skills and viable pivots
- **Students/Graduates** - Identify skill gaps before entering job market
- **HR Professionals** - Reverse-engineer ATS requirements
- **Career Coaches** - Provide data-driven guidance to clients
- **Recruiters** - Quickly assess candidate-role fit

---

## Privacy and Security

- **100% Local Processing** - All analysis runs on your machine
- **No Data Collection** - Documents never leave your computer
- **No External APIs** - Fully offline operation (except job search links)
- **Open Source** - Transparent code, auditable algorithms
- **No Tracking** - Zero analytics or user monitoring

---

## Roadmap

- [ ] Multi-language support (Spanish, French, German)
- [ ] Resume builder integration
- [ ] LinkedIn profile import
- [ ] Interview question generator
- [ ] Salary range estimation
- [ ] Industry-specific templates
- [ ] Browser extension for job board integration

---

## Contributing

Contributions are welcome! Please feel free to submit:
- Bug reports via Issues
- Feature requests via Discussions
- Pull requests for improvements

**Development Setup:**
```bash
# Fork and clone
git clone https://github.com/Giacomod2001/datamining.git
cd datamining

# Create branch
git checkout -b feature/your-feature-name

# Make changes and test
streamlit run app.py

# Submit PR
git push origin feature/your-feature-name
```

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Built with powerful open-source tools:
- **Streamlit Team** - Exceptional rapid development framework
- **Scikit-Learn Community** - World-class ML algorithms
- **NLTK Contributors** - Comprehensive NLP capabilities
- **Open Source Community** - Continuous innovation and support

The authors would like to acknowledge the assistance of the AI tool Gemini 3 Pro High and the agentic system Antigravity for coding suggestions and debugging support during the development phase.

---

## Support

**Questions or Issues?**
- Check the Wiki for detailed guides
- Open an Issue for bugs
- Star the repo if you find it helpful!

---

**Empower your career journey with AI-driven insights**
