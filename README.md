# Job Seeker Helper 🎯

## Overview

**Job Seeker Helper** is an advanced open-source AI-powered analytics dashboard designed to revolutionize job application analysis. By leveraging **Hierarchical Inference**, **Machine Learning**, and **Natural Language Processing**, it provides comprehensive evaluation of CVs, Job Descriptions, and Cover Letters—going far beyond simple keyword matching to understand the *semantic context* of your professional profile.

This cutting-edge tool empowers job seekers with actionable insights, skill gap analysis, personalized learning pathways, and intelligent career recommendations.

---

## ✨ Key Features

### 🧠 Semantic & Hierarchical Inference
Unlike traditional ATS systems, our engine understands skill relationships through custom semantic logic:
- **Inference Engine**: Automatically deduces implicit skills (e.g., *BigQuery* → *Cloud Computing* + *SQL*)
- **Transferable Logic**: Recognizes equivalent tools (*Looker* ≈ *Power BI*), marking them as "Transferable" rather than "Missing"
- **Cross-Domain Support**: Analyzes roles across Tech, Business, Marketing, and more using TF-IDF fallback mechanisms

### 📊 Comprehensive Gap Analysis
- **Technical vs. Soft Skills**: Distinct evaluation pipelines for quantifiable and behavioral competencies
- **Portfolio-Based Triggers**: Complex domains (*Computer Vision*, *System Design*) flagged for qualitative portfolio review
- **Bilingual Support (IT/EN)**: Upload Italian CV + English JD (or vice versa) with automatic skill mapping
- **Smart Language Detection**: Automatically assigns native language proficiency based on CV context

### 💡 Job Context Intelligence (NEW!)
**Understand what the job REALLY wants:**
- **AI-Powered Topic Analysis**: LDA-based analysis identifies key themes from job descriptions
- **Human-Readable Interpretations**: Converts raw keywords into clear explanations (e.g., "Cloud Data Engineering: Work with AWS to manage scalable data pipelines")
- **Visual Summary**: Shows job focus areas with interpreted categories and keyword tags
- **Multilingual Support**: Provides insights in Italian or English based on document language

### ✉️ Cover Letter Evaluation (NEW!)
**Optimize your application letters:**
- **Comprehensive Scoring**: Analyzes keyword coverage (35%), soft skills (15%), length (15%), structure (20%), and personalization (15%)
- **Actionable Feedback**: Get specific strengths and improvement suggestions
- **Keyword Coverage**: See which required skills you mentioned vs. missed
- **Bilingual Analysis**: Automatic language detection with localized feedback (IT/EN)
- **Structure Validation**: Checks for proper greeting, closing, and professional formatting

### 🎨 Visual Analytics & Advanced Mining
- **Skill Clustering**: K-Means and Hierarchical Clustering visualize skill relationships with interactive scatter plots and dendrograms
- **Knowledge Graph**: Interactive skill ontology visualization showing hierarchical relationships
- **Topic Modeling**: LDA-based job theme identification with word cloud visualization
- **Named Entity Recognition (NER)**: Extracts Organizations, Locations, and People from resumes
- **Fuzzy Matching**: Handles typos and variations (e.g., "Phyton" → "Python")
- **Interactive Plotly Charts**: Real-time match score visualization

### 🔮 AI Career Compass
**Discover your best career paths:**
- **Intelligent Role Recommendation**: Uses Cosine Similarity on TF-IDF vectors to suggest top 3 alternative roles
- **Smart Filtering**: Excludes your target and current roles to show only true alternatives
- **Quality Threshold**: Only suggests roles with >30% match to avoid low-quality recommendations
- **Direct Job Search Links**: One-click access to:
  - 🌐 Google Jobs
  - 💼 LinkedIn
  - 🔍 Indeed Italia

### 📂 Project Evaluation
**Validate skills through practical experience:**
- **Portfolio Triangulation**: Upload project descriptions to prove missing skills
- **Project-Verified Badge**: Highlighted skills confirmed through projects
- **Dynamic Layout**: Toggle to add dedicated "Project Context" column
- **Score Boost**: Project-verified skills contribute to final match percentage

### 📚 Actionable Learning Pathways
**Personalized skill development plans for every gap:**
- 🔍 **Google Search**: Targeted tutorial queries
- 📺 **YouTube**: Direct links to educational content
- 🎓 **MOOC Hub**: Multi-platform search (Coursera, Udemy, LinkedIn Learning)

### 📄 Professional Reports
**Export comprehensive analysis:**
- **PDF Reports**: Beautifully formatted with executive summary, skill breakdowns, and learning roadmap
- **Text Reports**: Detailed markdown-formatted analysis for easy sharing
- **Cover Letter Analysis**: Included in reports when evaluated

### 🔐 Developer Mode
**Transparent AI decision-making:**
- Password-protected debugger interface
- View inference rules, skill clusters, and internal logic
- Access to training data and knowledge base
- Topic modeling and NER analysis tools

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Scipy](https://img.shields.io/badge/Scipy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-blue?style=for-the-badge&logo=python&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF_Parsing-red?style=for-the-badge)
![FPDF](https://img.shields.io/badge/FPDF-Report_Gen-green?style=for-the-badge)
![WordCloud](https://img.shields.io/badge/WordCloud-Visualization-orange?style=for-the-badge)

**Core Libraries:**
- **NLP**: NLTK, scikit-learn (TF-IDF, LDA, Clustering)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib, WordCloud, Graphviz
- **PDF Handling**: PyPDF2, FPDF
- **Fuzzy Matching**: thefuzz

---

## 🚀 Installation & Setup

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

4. **Access the App**
   - Open your browser to `http://localhost:8501`
   - The app will automatically open in your default browser

---

## 📖 Usage Manual

### Basic Workflow

1. **Input Your Documents**:
   - **CV** (Required): Upload PDF or paste text of your resume
   - **Job Description** (Required): Upload PDF or paste JD text
   - **Project Context** (Optional): Toggle in sidebar to add project descriptions
   - **Cover Letter** (Optional): Toggle in sidebar to evaluatecover letter

2. **Configure Optional Features** (Sidebar):
   - ✅ `📂 Project Evaluation` - Validate skills through portfolio
   - ✅ `✉️ Cover Letter Evaluation` - Analyze application letter quality
   - ✅ `Developer Mode` - Access advanced debugging tools (password: `1234`)

3. **Run Analysis**:
   - Click **"🔍 Analyze"** button
   - Wait for comprehensive AI-powered evaluation

4. **Review Results**:
   - **Match Score**: Weighted percentage showing CV-JD alignment
   - **Cover Letter Score**: (if enabled) Analysis of your application letter
   - **Skill Breakdown**:
     - ✅ **Matched**: Direct skill overlaps
     - ⚠️ **Transferable**: Equivalent skills you possess
     - 📂 **Portfolio**: Skills verified by projects
     - ❌ **Missing**: Gaps with learning resources
     - ➕ **Bonus**: Extra skills bringing competitive advantage
   - **Job Context Analysis**: What the position really seeks
   - **Career Compass**: Alternative role recommendations
   - **Learning Plans**: Personalized resources for skill gaps

5. **Export Reports**:
   - Download **PDF Report** for professional presentation
   - Download **Text Report** for easy sharing and editing

### Advanced Features

#### Developer Mode
Access internal analytics:
1. Enable "Developer Mode" toggle in sidebar
2. Enter password: `1234`
3. Click "Open Debugger"
4. Explore:
   - 🧠 Inference rules visualization
   - 🔗 Skill cluster relationships
   - 📊 Advanced clustering analysis
   - 🧩 Topic modeling results
   - 🏷️ NER entity extraction
   - 📚 Training data inspection

---

## 🎯 Use Cases

- **Job Seekers**: Optimize CV and cover letters for specific roles
- **Career Switchers**: Discover transferable skills and alternative paths
- **Students/Graduates**: Identify skill gaps before entering job market
- **HR Professionals**: Reverse-engineer ATS requirements
- **Career Coaches**: Provide data-driven guidance to clients

---

## 📊 Scoring Methodology

### CV Match Score
- **Direct Matches**: 100% weight
- **Transferable Skills**: 50% weight
- **Project-Verified Skills**: 30% weight
- **Formula**: `(Matched + Transferable×0.5 + Projects×0.3) / Total Required × 100`

### Cover Letter Score
- **Keyword Coverage**: 35% - Technical skills mentioned
- **Soft Skills**: 15% - Behavioral competencies
- **Length**: 15% - Optimal 250-400 words
- **Structure**: 20% - Professional formatting
- **Personalization**: 15% - Specific examples and custom content

---

## 🔒 Privacy & Security

- **100% Local Processing**: All analysis runs on your machine
- **No Data Collection**: Your documents never leave your computer
- **No External APIs**: Fully offline operation (except optional job search links)
- **Open Source**: Transparent codeand auditable algorithms

---

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- **Streamlit Team**: For the exceptional rapid development framework
- **Scikit-Learn Community**: For world-class machine learning tools
- **NLTK Contributors**: For comprehensive NLP capabilities
- **Open Source Community**: For continuous innovation and support

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

## 📧 Support

For questions, suggestions, or feedback, please open an issue on GitHub.

---

**Made with ❤️ for job seekers worldwide**
