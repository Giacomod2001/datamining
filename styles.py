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
/* header {visibility: hidden;} */ /* REMOVED: This hides the mobile sidebar toggle! */

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
   INPUT COLUMNS - Uniform Layout Fix
   ============================================================================= */

/* Force all column headers to have consistent height */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] h3,
[data-testid="column"] h3 {
    min-height: 32px !important;
    margin-bottom: 0.5rem !important;
    display: flex !important;
    align-items: center !important;
}

/* Uniform radio button row spacing */
[data-testid="stRadio"] {
    margin-top: 0 !important;
    margin-bottom: 0.5rem !important;
}

/* Consistent text area height in all columns */
[data-testid="stTextArea"] textarea {
    min-height: 250px !important;
    max-height: 250px !important;
}

/* Uniform file uploader height to match text areas */
[data-testid="stFileUploader"] {
    min-height: 250px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
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

/* =============================================================================
   SIDEBAR OPEN - Compact Layout for 4 Columns
   ============================================================================= */

/* When sidebar is open, content area shrinks - make columns more compact */
[data-testid="stAppViewContainer"][data-layout="wide"] [data-testid="column"] {
    padding: 0 0.25rem !important;
}

/* Smaller headers when space is limited */
[data-testid="column"] h3 {
    font-size: 1rem !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

/* Compact radio buttons */
[data-testid="column"] [data-testid="stRadio"] > div {
    gap: 0.5rem !important;
}

[data-testid="column"] [data-testid="stRadio"] label {
    font-size: 0.85rem !important;
    padding: 0.25rem 0.5rem !important;
}

/* Reduce text area height when sidebar is open */
[data-testid="column"] [data-testid="stTextArea"] textarea {
    font-size: 0.85rem !important;
}

/* =============================================================================
   MOBILE SIDEBAR FIX
   ============================================================================= */
@media (max-width: 768px) {
    /* Ensure sidebar container is accessible */
    section[data-testid="stSidebar"] {
        padding-top: 0rem !important;
    }
    
    /* Ensure the collapse/expand control is always visible */
    [data-testid="collapsedControl"] {
        z-index: 1000000 !important;
        visibility: visible !important;
    }
}
</style>
"""


def get_demo_cv():
    """Returns sample CV text for demo mode - optimized for ~73% match."""
    return """
MARCO BIANCHI
Digital Marketing & Data Analyst
Milan, Italy | marco.bianchi@email.com | +39 333 1234567

PROFESSIONAL SUMMARY
Results-driven Marketing Analyst with 4 years of experience in data-driven marketing 
and business intelligence. Expert in Google Analytics, campaign optimization, and 
dashboard creation. Currently pursuing certifications in cloud technologies.

TECHNICAL SKILLS
Programming: Python, SQL, BigQuery
Analytics & BI: Google Analytics 4, Google Tag Manager, Looker Studio, Data Visualization
Marketing: Campaign Management, A/B Testing, Performance Marketing, Social Media, Email Marketing
Tools: CRM Platforms, Microsoft Office, Excel, Google Workspace
Languages: Italian (Native), English (B2 Professional)

PROFESSIONAL EXPERIENCE

Marketing Data Analyst | Digital Agency Milano | 2022 - Present
- Designed interactive dashboards in Looker Studio tracking campaign KPIs and ROI
- Implemented tracking ecosystems using Google Tag Manager across 50+ client websites
- Analyzed performance data using Google Analytics 4 to optimize conversion rates by 25%
- Managed A/B testing programs for landing pages and email campaigns
- Collaborated with creative teams on data-driven marketing strategies

Junior Digital Marketing Specialist | StartUp Italia | 2020 - 2022
- Executed multi-platform social media campaigns increasing engagement by 40%
- Managed email marketing automation and CRM database of 100K+ contacts
- Created campaign performance reports and presented insights to stakeholders
- Supported paid advertising campaigns on Google Ads and Facebook

EDUCATION
Bachelor in Marketing & Communication | Università Bocconi | 2020
Relevant Coursework: Statistics, Consumer Behavior, Digital Marketing, Market Research

CERTIFICATIONS
- Google Analytics Individual Qualification (GAIQ)
- Google Ads Search Certification
- HubSpot Inbound Marketing

KEY PROJECT
E-commerce Analytics Dashboard | Personal Project | 2023
Built end-to-end analytics solution using Python, BigQuery, and Looker Studio
to track customer journey and revenue attribution across marketing channels.
"""


def get_demo_jd():
    """Returns sample Job Description for demo mode - designed for ~73% match."""
    return """
SENIOR MARKETING ANALYST
DataDriven Corp | Milan, Italy (Hybrid)

About Us:
DataDriven Corp is a leading marketing technology company seeking a Senior Marketing 
Analyst to join our Analytics team. You will drive data-informed decision making 
across our marketing organization.

Requirements:

Required Technical Skills:
- 4+ years experience in marketing analytics or data analysis
- Expert proficiency in Google Analytics 4 and Google Tag Manager
- Strong SQL skills for data extraction and analysis
- Experience with BI tools (Looker Studio, Tableau, or Power BI)
- Proficiency in Python for data analysis and automation
- Experience with A/B testing and statistical analysis

Required Marketing Skills:
- Deep understanding of digital marketing channels (SEO, SEM, Social Media)
- Experience with campaign tracking and attribution modeling
- Knowledge of CRM platforms and email marketing
- Strong stakeholder communication and presentation skills

Nice to Have:
- Experience with cloud platforms (GCP, AWS)
- Machine Learning knowledge for predictive analytics
- Tableau or Power BI certification
- Experience with dbt or data transformation tools
- Knowledge of Snowflake or data warehousing concepts

Soft Skills:
- Excellent analytical and problem-solving abilities
- Strong communication skills for technical and non-technical audiences
- Ability to work independently and in cross-functional teams
- Detail-oriented with strong project management skills

What We Offer:
- Competitive salary: EUR 45,000 - 55,000
- Hybrid work arrangement (3 days office, 2 days remote)
- Learning budget for certifications and courses
- Health insurance and wellness benefits
- International team environment

Languages:
- English (Required - working language)
- Italian (Required for client communication)
"""


def get_demo_project():
    """Returns sample project description for demo mode."""
    return """
E-COMMERCE ANALYTICS DASHBOARD
Personal Project | 2023

OBJECTIVE
Developed a comprehensive analytics solution to track customer journey and revenue 
attribution across marketing channels for an e-commerce platform.

TECHNICAL IMPLEMENTATION
- Built data pipeline using Python and BigQuery to process 1M+ daily events
- Created interactive dashboards in Looker Studio with 15+ KPIs
- Implemented Google Tag Manager tracking for enhanced e-commerce events
- Used SQL for complex attribution modeling and cohort analysis
- Applied A/B testing framework for landing page optimization

TECHNOLOGIES USED
- Languages: Python, SQL
- Data: BigQuery, Google Cloud Platform
- Visualization: Looker Studio, Data Visualization
- Analytics: Google Analytics 4, Google Tag Manager
- Marketing: Attribution Modeling, Campaign Tracking

RESULTS
- Reduced data processing time by 60% with optimized queries
- Increased conversion rate by 25% through data-driven optimization
- Automated weekly reporting saving 10+ hours of manual work

---

SOCIAL MEDIA SENTIMENT ANALYZER
University Project | 2022

OBJECTIVE
Built a machine learning pipeline to analyze brand sentiment from Twitter data.

TECHNICAL IMPLEMENTATION
- Collected tweets using Twitter API with Python
- Preprocessed text data with NLP techniques
- Trained sentiment classification model with scikit-learn
- Created visualization dashboard with Plotly

TECHNOLOGIES USED
- Python, SQL, NLP, Machine Learning
- Data Visualization, Statistical Analysis

RESULTS
- Achieved 85% accuracy in sentiment classification
- Processed 50,000+ tweets for brand analysis
"""


def get_demo_cover_letter():
    """Returns sample cover letter for demo mode."""
    return """
Dear Hiring Manager,

I am writing to express my strong interest in the Senior Marketing Analyst position 
at DataDriven Corp. With 4 years of experience in data-driven marketing and business 
intelligence, I am confident that my skills align perfectly with your requirements.

In my current role at Digital Agency Milano, I have developed expertise in the exact 
tools you require. I use Google Analytics 4 and Google Tag Manager daily to implement 
tracking systems across 50+ client websites. My proficiency in SQL and BigQuery enables 
me to extract actionable insights from large datasets, while my experience with Looker 
Studio has allowed me to create dashboards that increased client ROI by 25%.

What excites me most about this opportunity is your focus on data-informed decision 
making. At Digital Agency Milano, I led the implementation of attribution modeling 
that helped clients understand their marketing channel effectiveness. This directly 
aligns with your need for campaign tracking and statistical analysis expertise.

I have hands-on experience with A/B testing programs, having designed and analyzed 
tests for landing pages and email campaigns. My background in Python for data analysis 
and automation complements my marketing analytics skills, enabling me to build 
efficient reporting pipelines.

While I am still developing my Tableau and Power BI skills, my strong foundation in 
Looker Studio and data visualization principles means I can quickly adapt to new 
BI tools. I am particularly interested in expanding my knowledge of cloud platforms, 
which aligns with your GCP requirements.

The hybrid work arrangement and learning budget you offer are valuable benefits that 
would support my professional development goals. I am excited about the opportunity 
to contribute to DataDriven Corp's analytics team.

Thank you for considering my application. I would welcome the opportunity to discuss 
how my experience in marketing analytics can contribute to your team's success.

Best regards,
Marco Bianchi
"""

