# =============================================================================
# STYLES.PY - Premium Visual Design System for Job Seeker Helper
# Version 2.0 - LinkedIn-Inspired Theme with Glassmorphism
# =============================================================================

def get_premium_css():
    """Returns comprehensive CSS for premium Job Seeker Helper UI."""
    return """
<style>
/* =============================================================================
   CSS VARIABLES - Design Tokens
   ============================================================================= */
:root {
    /* LinkedIn-Inspired Color Palette */
    --primary-blue: #0077B5;
    --primary-dark: #004471;
    --primary-light: #00A0DC;
    --accent-green: #00C853;
    --accent-amber: #FFB300;
    --accent-red: #E53935;
    
    /* Neutral Colors */
    --bg-dark: #0d1117;
    --bg-card: #161b22;
    --bg-elevated: #21262d;
    --text-primary: #f0f6fc;
    --text-secondary: #8b949e;
    --border-color: #30363d;
    
    /* Shadows */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.12);
    --shadow-lg: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    
    /* Transitions */
    --transition-fast: 0.15s ease;
    --transition-normal: 0.3s ease;
    --transition-slow: 0.5s ease;
}

/* =============================================================================
   GLOBAL STYLES
   ============================================================================= */
   
/* Main Container */
.stApp {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%);
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* =============================================================================
   TYPOGRAPHY
   ============================================================================= */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    font-weight: 600 !important;
}

h1 {
    background: linear-gradient(90deg, var(--primary-light), var(--primary-blue), var(--primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* =============================================================================
   BUTTONS
   ============================================================================= */
   
/* Primary Button (Analyze, etc.) */
.stButton > button[kind="primary"],
.stButton > button {
    background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    box-shadow: var(--shadow-md) !important;
    transition: all var(--transition-normal) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-lg), 0 0 20px rgba(0, 119, 181, 0.4) !important;
    background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-blue) 100%) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* =============================================================================
   CARDS & CONTAINERS
   ============================================================================= */
   
/* Glassmorphism Card Effect */
.glass-card {
    background: rgba(22, 27, 34, 0.8);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(48, 54, 61, 0.6);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: var(--shadow-md);
    transition: all var(--transition-normal);
}

.glass-card:hover {
    border-color: var(--primary-blue);
    box-shadow: var(--shadow-lg), 0 0 15px rgba(0, 119, 181, 0.2);
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(135deg, rgba(0, 119, 181, 0.1) 0%, rgba(0, 68, 113, 0.1) 100%);
    border: 1px solid var(--primary-blue);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    transition: all var(--transition-normal);
}

.metric-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(0, 119, 181, 0.3);
}

/* =============================================================================
   SKILL TAGS - Enhanced Colors
   ============================================================================= */
   
.skill-tag-matched {
    background: linear-gradient(135deg, #1e4620 0%, #155724 100%);
    color: #75f083;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    border: 1px solid #2d5a30;
    box-shadow: 0 2px 8px rgba(30, 70, 32, 0.3);
    transition: all var(--transition-fast);
}

.skill-tag-matched:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(117, 240, 131, 0.2);
}

.skill-tag-transferable {
    background: linear-gradient(135deg, #5c4813 0%, #856404 100%);
    color: #ffd666;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    border: 1px solid #7a5f10;
    box-shadow: 0 2px 8px rgba(92, 72, 19, 0.3);
    transition: all var(--transition-fast);
}

.skill-tag-missing {
    background: linear-gradient(135deg, #5c1f23 0%, #842029 100%);
    color: #ff8a8a;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    border: 1px solid #8a3035;
    box-shadow: 0 2px 8px rgba(92, 31, 35, 0.3);
    transition: all var(--transition-fast);
}

.skill-tag-project {
    background: linear-gradient(135deg, #0a3d62 0%, #084298 100%);
    color: #7ec8ff;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    border: 1px solid #0d5aa7;
    box-shadow: 0 2px 8px rgba(10, 61, 98, 0.3);
    transition: all var(--transition-fast);
}

.skill-tag-bonus {
    background: linear-gradient(135deg, #2d333b 0%, #41464b 100%);
    color: #b1b8c0;
    font-weight: 500;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    border: 1px solid #484f58;
    box-shadow: 0 2px 8px rgba(45, 51, 59, 0.3);
    transition: all var(--transition-fast);
}

/* =============================================================================
   SIDEBAR STYLING
   ============================================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #161b22 100%);
    border-right: 1px solid var(--border-color);
}

section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--primary-light) !important;
    -webkit-text-fill-color: var(--primary-light) !important;
}

/* =============================================================================
   INPUT FIELDS
   ============================================================================= */
   
.stTextArea textarea,
.stTextInput input {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
    transition: all var(--transition-fast) !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: var(--primary-blue) !important;
    box-shadow: 0 0 0 3px rgba(0, 119, 181, 0.2) !important;
}

/* =============================================================================
   FILE UPLOADER
   ============================================================================= */
   
.stFileUploader {
    background: var(--bg-elevated);
    border: 2px dashed var(--border-color);
    border-radius: 12px;
    padding: 1rem;
    transition: all var(--transition-normal);
}

.stFileUploader:hover {
    border-color: var(--primary-blue);
    background: rgba(0, 119, 181, 0.05);
}

/* =============================================================================
   EXPANDER STYLING
   ============================================================================= */

.streamlit-expanderHeader {
    background: var(--bg-elevated) !important;
    border-radius: 8px !important;
    border: 1px solid var(--border-color) !important;
    transition: all var(--transition-fast) !important;
}

.streamlit-expanderHeader:hover {
    border-color: var(--primary-blue) !important;
    background: rgba(0, 119, 181, 0.1) !important;
}

/* =============================================================================
   PROGRESS BAR
   ============================================================================= */

.stProgress > div > div {
    background: linear-gradient(90deg, var(--primary-blue), var(--primary-light), var(--accent-green)) !important;
    border-radius: 10px;
}

/* =============================================================================
   METRICS
   ============================================================================= */

[data-testid="stMetricValue"] {
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    background: linear-gradient(90deg, var(--primary-light), var(--primary-blue));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* =============================================================================
   TABS STYLING
   ============================================================================= */

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: var(--bg-elevated);
    padding: 8px;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    padding: 10px 20px !important;
    transition: all var(--transition-fast) !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(0, 119, 181, 0.15) !important;
}

.stTabs [aria-selected="true"] {
    background: var(--primary-blue) !important;
}

/* =============================================================================
   DIVIDER - Custom Styled
   ============================================================================= */

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-color), var(--primary-blue), var(--border-color), transparent);
    margin: 2rem 0;
}

/* =============================================================================
   ANIMATIONS - Fade In
   ============================================================================= */

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeInUp 0.5s ease-out forwards;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

.pulse {
    animation: pulse 2s ease-in-out infinite;
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.skeleton {
    background: linear-gradient(90deg, var(--bg-elevated) 25%, var(--bg-card) 50%, var(--bg-elevated) 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 4px;
}

/* =============================================================================
   SUCCESS/INFO/WARNING ALERTS - Enhanced
   ============================================================================= */

.stAlert {
    border-radius: 12px !important;
    border-left-width: 4px !important;
}

/* =============================================================================
   TOOLTIP STYLING
   ============================================================================= */

.tooltip-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--primary-blue);
    color: white;
    font-size: 12px;
    font-weight: bold;
    cursor: help;
    margin-left: 6px;
    transition: all var(--transition-fast);
}

.tooltip-icon:hover {
    transform: scale(1.1);
    box-shadow: 0 0 10px rgba(0, 119, 181, 0.5);
}

/* =============================================================================
   HERO SECTION
   ============================================================================= */

.hero-gradient {
    background: linear-gradient(135deg, 
        rgba(0, 119, 181, 0.15) 0%, 
        rgba(0, 68, 113, 0.1) 50%,
        rgba(0, 160, 220, 0.1) 100%
    );
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(0, 119, 181, 0.3);
}

/* =============================================================================
   RESPONSIVE DESIGN
   ============================================================================= */

@media (max-width: 768px) {
    .stButton > button {
        width: 100% !important;
    }
    
    .glass-card {
        padding: 1rem;
    }
}
</style>
"""


def get_demo_cv():
    """Returns sample CV text for demo mode."""
    return """
GIACOMO ROSSI
Data Engineer & ML Specialist
Milan, Italy | giacomo.rossi@email.com

SUMMARY
Experienced Data Engineer with 5+ years building scalable data pipelines and ML systems.
Expert in Python, SQL, and cloud technologies (GCP, AWS). Strong background in analytics
and business intelligence.

SKILLS
Technical: Python, SQL, BigQuery, GCP, AWS, Docker, Kubernetes, Airflow, Spark
Analytics: Power BI, Tableau, Looker Studio, Google Analytics, Data Visualization
Languages: Italian (Native), English (Fluent), Spanish (Intermediate)

EXPERIENCE

Senior Data Engineer | Tech Company XYZ | 2021 - Present
- Designed and implemented ETL pipelines processing 10TB+ daily using Airflow and Spark
- Built real-time data streaming infrastructure with Kafka and Dataflow
- Led migration of on-premise data warehouse to BigQuery, reducing costs by 40%
- Developed Python libraries for automated data quality monitoring

Data Analyst | StartUp ABC | 2019 - 2021
- Created executive dashboards in Power BI tracking business KPIs
- Performed advanced analytics using Python (Pandas, Scikit-learn)
- Collaborated with product teams to define metrics and A/B testing

EDUCATION
Master in Data Science | Politecnico di Milano | 2019
Bachelor in Computer Engineering | Università di Milano | 2017

CERTIFICATIONS
- Google Cloud Professional Data Engineer
- AWS Solutions Architect Associate
"""


def get_demo_jd():
    """Returns sample Job Description for demo mode."""
    return """
SENIOR DATA ENGINEER
TechCorp International | Milan, Italy

About the Role:
We are looking for a Senior Data Engineer to join our growing data team. You will be
responsible for designing and building scalable data infrastructure to support our
analytics and machine learning initiatives.

Requirements:

Technical Skills:
- 5+ years experience with Python and SQL
- Strong experience with cloud platforms (GCP, AWS, or Azure)
- Experience with data orchestration tools (Airflow, Luigi)
- Proficiency in big data technologies (Spark, Kafka)
- Experience with containerization (Docker, Kubernetes)
- Knowledge of data warehousing concepts and solutions (BigQuery, Snowflake, Redshift)

Nice to Have:
- Experience with Terraform or Infrastructure as Code
- Machine Learning engineering experience
- Streaming data processing (Pub/Sub, Kinesis)
- Experience with BI tools (Tableau, Power BI, Looker)

Soft Skills:
- Excellent communication and stakeholder management
- Problem-solving mindset
- Ability to work in cross-functional teams
- Leadership experience mentoring junior engineers

What We Offer:
- Competitive salary and benefits
- Remote/Hybrid work options
- Learning and development budget
- International team environment

Languages:
- English (Required)
- Italian (Preferred)
"""
