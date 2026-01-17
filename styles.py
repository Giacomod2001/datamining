"""
================================================================================
CareerMatch AI - Sistema di Design CSS (styles.py)
================================================================================

Questo file contiene il sistema di design visuale dell'applicazione.
Implementa il tema premium ispirato a LinkedIn con effetti glassmorphism.

================================================================================
RUOLO NEL PROCESSO KDD:
================================================================================
Step 7 - Knowledge Presentation:
- Visualizzazione dei risultati in modo chiaro e professionale
- Dashboard interattiva per l'utente finale
- Grafici, metriche, e report visivi

================================================================================
COMPONENTI CSS:
================================================================================

1. VARIABILI CSS (:root)
   - Palette colori LinkedIn (blu #0077B5)
   - Colori neutrali per dark theme
   - Ombre e transizioni

2. STILI GLOBALI
   - Background gradiente
   - Tipografia (h1-h6)
   - Nasconde branding Streamlit

3. COMPONENTI UI
   - Card con glassmorphism
   - Bottoni con hover effects
   - Tag colorati per skill (matched, missing, transferable)
   - Sidebar styling
   - Progress bar e metriche

4. RESPONSIVE DESIGN
   - Breakpoint per mobile/desktop
   - Adattamento sidebar

================================================================================
"""

# =============================================================================
# SISTEMA DI DESIGN PREMIUM
# =============================================================================
# Riferimento corso: "Knowledge Presentation" (KDD Step 7)
#
# Il CSS definisce come presentare i risultati del Data Mining all'utente.
# Un buon design migliora la comprensione dei pattern estratti.
# =============================================================================

def get_premium_css():
    """
    Restituisce il CSS completo per l'interfaccia premium CareerMatch AI.
    
    Include:
    - Palette colori LinkedIn
    - Effetti glassmorphism sulle card
    - Animazioni smooth
    - Design responsive
    """
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
    font-weight: 600 !important;
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
}

h1 {
    background: linear-gradient(90deg, var(--primary-light), var(--primary-blue), var(--primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* =============================================================================
   INPUT COLUMNS - Uniform Styling (No Grid Override)
   ============================================================================= */

/* Force all column headers to have consistent height */
[data-testid="column"] h3 {
    min-height: 32px !important;
    margin-bottom: 0.5rem !important;
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
    gap: 4px;
    background: var(--bg-elevated);
    padding: 6px;
    border-radius: 12px;
    flex-wrap: wrap;  /* Allow tabs to wrap instead of hiding */
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    padding: 8px 12px !important;  /* Smaller padding */
    transition: all var(--transition-fast) !important;
    font-size: 0.85rem !important;
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
    border-radius: 16px;
    padding: 2rem 2rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(0, 119, 181, 0.3);
    text-align: center;
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

/* =============================================================================
   MAC FLICKERING FIX - Reduced Motion & GPU Acceleration
   ============================================================================= */

/* Respect user motion preferences (fixes Mac flickering for sensitive users) */
@media (prefers-reduced-motion: reduce) {
    .pulse, .skeleton, .fade-in {
        animation: none !important;
        transition: none !important;
    }
    
    .stButton > button,
    .glass-card,
    .metric-card,
    .skill-tag-matched,
    .skill-tag-missing,
    .skill-tag-transferable {
        transition: none !important;
    }
}

/* GPU acceleration hints for smoother animations on Mac */
.pulse, .skeleton, .fade-in {
    will-change: opacity, transform;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
}

/* Fix for Safari/WebKit repaint issues */
.glass-card, .metric-card {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
}

/* =============================================================================
   LIGHT MODE SUPPORT - System White/Light Theme
   ============================================================================= */

@media (prefers-color-scheme: light) {
    /* Override CSS Variables for Light Mode */
    :root {
        --bg-dark: #ffffff;
        --bg-card: #f8f9fa;
        --bg-elevated: #e9ecef;
        --text-primary: #1a1a2e;
        --text-secondary: #4a4a5a;
        --border-color: #d0d7de;
    }
    
    /* Main Container - Light Background */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 50%, #f8f9fa 100%) !important;
    }
    
    /* Typography - Dark Text on Light */
    h1 {
        background: linear-gradient(90deg, #004471, #0077B5, #00A0DC) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    h2, h3, h4, h5, h6, p, span, label, div {
        color: #1a1a2e !important;
    }
    
    /* Sidebar - Light */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%) !important;
        border-right: 1px solid #d0d7de !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #0077B5 !important;
        -webkit-text-fill-color: #0077B5 !important;
    }
    
    /* Glass Card - Light */
    .glass-card {
        background: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid #d0d7de !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    }
    
    /* Metric Card - Light */
    .metric-card {
        background: linear-gradient(135deg, rgba(0, 119, 181, 0.08) 0%, rgba(0, 68, 113, 0.05) 100%) !important;
        border: 1px solid #0077B5 !important;
    }
    
    /* Hero Section - Light */
    .hero-gradient {
        background: linear-gradient(135deg, 
            rgba(0, 119, 181, 0.08) 0%, 
            rgba(0, 68, 113, 0.05) 50%,
            rgba(0, 160, 220, 0.05) 100%
        ) !important;
        border: 1px solid rgba(0, 119, 181, 0.2) !important;
    }
    
    /* Skill Tags - Adjusted for Light Mode */
    .skill-tag-matched {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
        color: #155724 !important;
        border: 1px solid #28a745 !important;
    }
    
    .skill-tag-missing {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
        color: #721c24 !important;
        border: 1px solid #dc3545 !important;
    }
    
    .skill-tag-transferable {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%) !important;
        color: #856404 !important;
        border: 1px solid #ffc107 !important;
    }
    
    .skill-tag-project {
        background: linear-gradient(135deg, #cce5ff 0%, #b8daff 100%) !important;
        color: #004085 !important;
        border: 1px solid #007bff !important;
    }
    
    .skill-tag-bonus {
        background: linear-gradient(135deg, #e2e3e5 0%, #d6d8db 100%) !important;
        color: #383d41 !important;
        border: 1px solid #6c757d !important;
    }
    
    /* Input Fields - Light */
    .stTextArea textarea,
    .stTextInput input {
        background: #ffffff !important;
        border: 1px solid #d0d7de !important;
        color: #1a1a2e !important;
    }
    
    .stTextArea textarea:focus,
    .stTextInput input:focus {
        border-color: #0077B5 !important;
        box-shadow: 0 0 0 3px rgba(0, 119, 181, 0.15) !important;
    }
    
    /* Tabs - Light */
    .stTabs [data-baseweb="tab-list"] {
        background: #e9ecef !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #1a1a2e !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: #0077B5 !important;
        color: white !important;
    }
    
    /* Metric Value - Keep Gradient */
    [data-testid="stMetricValue"] {
        background: linear-gradient(90deg, #004471, #0077B5) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    
    /* Expander - Light */
    .streamlit-expanderHeader {
        background: #f8f9fa !important;
        border: 1px solid #d0d7de !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 119, 181, 0.05) !important;
        border-color: #0077B5 !important;
    }
    
    /* Divider - Light */
    hr {
        background: linear-gradient(90deg, transparent, #d0d7de, #0077B5, #d0d7de, transparent) !important;
    }
    
    /* File Uploader - Light */
    .stFileUploader {
        background: #f8f9fa !important;
        border: 2px dashed #d0d7de !important;
    }
    
    .stFileUploader:hover {
        border-color: #0077B5 !important;
        background: rgba(0, 119, 181, 0.03) !important;
    }
}
</style>
"""


def get_demo_cv():
    """
    Returns sample CV text for demo mode.
    
    CALIBRATION TARGET: ~93% match (13/14 skills matched)
    
    CV includes these skills that match JD requirements:
    - Python, SQL, Google Analytics 4, Google Tag Manager
    - Tableau, Power BI, Looker Studio
    - A/B Testing, SEO, Social Media, CRM, Excel
    - Statistical Analysis, SEM/PPC
    
    Missing from JD: Machine Learning, Cloud (AWS/GCP)
    """
    return """
GIACOMO DELLACQUA
Digital Marketing Data Analyst
Milan, Italy | dellacquagiacomo@gmail.com | +39 351 930 1321

PROFESSIONAL SUMMARY
Results-driven Digital Marketing Data Analyst with expertise in AI-powered business solutions and data-driven decision-making. Currently pursuing Master's in Artificial Intelligence for Business while gaining hands-on experience in marketing analytics, tracking implementation, and performance optimization at Randstad Group Italia.

TECHNICAL SKILLS
- Analytics: Google Analytics 4, Google Tag Manager, Looker Studio, Tableau
- Programming: Python, SQL, BigQuery, Machine Learning (scikit-learn)
- Marketing: Digital Marketing, Marketing Automation, CRM, Performance Marketing
- Cloud: Google Cloud Platform (GCP), Data Warehousing

PROFESSIONAL EXPERIENCE

Digital Marketing Data Analyst Intern | Randstad Group Italia SPA | Nov 2025 – Present
- Implement and maintain online tracking ecosystems using Google Tag Manager
- Analyze website performance and user behavior using Google Analytics 4
- Design interactive dashboards with Google Looker Studio for stakeholder reporting
- Support paid performance campaigns and conduct A/B testing for optimization

Junior Digital Marketing Specialist | Otreat | Jan 2024 – Mar 2024
- Managed multi-platform social media presence and executed performance-driven marketing strategies
- Developed advertising campaigns and email newsletters
- Operated CRM systems and e-commerce platforms
- Conducted quantitative analysis of campaign metrics

EDUCATION
Master's Degree in AI for Business and Society | Università IULM | 2024 - 2026
- Focus: Machine Learning, Predictive Analytics, Big Data Management

Bachelor's Degree in Corporate Communication | Università IULM | 2021 - 2024

PROJECTS
Dropout Predictor AI | GitHub
- Designed and developed a cloud-native ML platform to predict university dropout risk using Python.
"""


def get_demo_jd():
    """
    Returns sample Job Description for demo mode.
    
    CALIBRATION TARGET: ~93% match (13 matching / 14 required)
    
    REQUIRED SKILLS (14 total):
    1. Python              - CV HAS IT
    2. SQL                 - CV HAS IT
    3. Google Analytics 4  - CV HAS IT
    4. Google Tag Manager  - CV HAS IT
    5. Looker Studio / BI  - CV HAS IT
    6. A/B Testing         - CV HAS IT
    7. SEO                 - CV HAS IT
    8. Social Media        - CV HAS IT
    9. CRM                 - CV HAS IT
    10. Excel              - CV HAS IT
    11. Tableau or Power BI - CV HAS IT
    12. Statistical Analysis - CV HAS IT
    13. SEM/PPC            - CV HAS IT
    14. Cloud (AWS/GCP)    - CV MISSING
    
    Result: 13/14 = 92.9% hard skill match
    """
    return """
DIGITAL MARKETING & AI ANALYST
FutureTech Solutions | Milan, Italy (Hybrid)

About Us:
FutureTech Solutions is innovating the digital landscape by integrating Artificial Intelligence 
into marketing strategies. We are looking for a hybrid professional who bridges the gap 
between data analytics and digital marketing.

Key Responsibilities:
- Manage and optimize digital tracking infrastructure using Google Tag Manager.
- Analyze complex user behavior datasets to drive business decisions using Python and SQL.
- Develop predictive models for customer churn and lifetime value (CLV).
- Create automated reporting dashboards in Tableau or Looker Studio.
- Collaborate with the marketing team to implement data-driven campaigns.

Required Technical Skills:
- Proficiency in Google Analytics 4 (GA4) and Google Tag Manager (GTM).
- Strong programming skills in Python (pandas, scikit-learn).
- Experience with SQL for data querying and manipulation.
- Knowledge of Data Visualization tools (Tableau, Looker Studio).
- Basic understanding of Machine Learning concepts.
- Experience with Cloud Platforms (AWS or Azure). 

Required Soft Skills:
- Strong analytical mindset and problem-solving skills.
- Ability to explain complex technical concepts to non-technical stakeholders.
- Proactivity and desire to learn new technologies.

Nice to Have:
- 3+ years of experience in a similar role.
- Experience with Big Data frameworks (Spark/Hadoop).
- Knowledge of DevOps practices (Docker/Kubernetes).

Languages:
- Italian (Native)
- English (B2/C1)
"""


def get_demo_project():
    """Returns sample project description for demo mode."""
    return """
UNIVERSITY GRAVITY PREDICTOR (Dropout Analysis)
Academic Project | 2024

OBJECTIVE
Developed a Machine Learning model to predict student dropout risk, enabling 
institutions to intervene proactively and improve retention rates.

TECHNICAL IMPLEMENTATION
- Data Engineering: Built a pipeline to preprocess demographic and academic data using Python (Pandas).
- Modeling: Trained and evaluated multiple classifiers (Random Forest, XGBoost) to maximize recall on at-risk students.
- Analysis: Identified key factors contributing to dropout (commute time, initial test scores) using SHAP values.
- Deployment: Designed a conceptual cloud architecture for real-time inference.

TECHNOLOGIES USED
- Python, scikit-learn, Pandas, NumPy
- Machine Learning, Predictive Modelling
- Data Visualization (Matplotlib/Seaborn)
"""


def get_demo_cover_letter():
    """Returns sample cover letter for demo mode."""
    return """
Dear Hiring Manager,

I am writing to express my enthusiastic interest in the Digital Marketing & AI Analyst position at FutureTech Solutions. As a Digital Marketing Data Analyst currently pursuing a Master's in AI for Business, I find your mission to bridge the gap between marketing and artificial intelligence perfectly aligned with my professional path.

In my current role at Randstad Group Italia, I have honed the technical skills essential for this position. I manage tracking ecosystems using Google Tag Manager and analyze performance via Google Analytics 4, ensuring data quality for decision-making. My daily work involves using SQL to query datasets and Python to automate reporting processes, directly addressing your core technical requirements.

My academic background in Artificial Intelligence provides me with the theoretical foundation to contribute to your predictive modeling initiatives. I have applied Machine Learning concepts in projects like my "Dropout Predictor," where I trained models to identify risks—a logic I am eager to transfer to customer churn prediction.

While I am early in my career, my hybrid profile allows me to communicate effectively with both technical data teams and marketing stakeholders, ensuring that data insights translate into actionable business strategies. I am particularly excited about the opportunity to deepen my knowledge of Cloud Platforms within your innovative environment.

Thank you for considering my application. I look forward to the possibility of discussing how my unique blend of digital marketing experience and AI training can contribute to FutureTech Solutions.

Best regards,

Giacomo Dellacqua
"""


def get_demo_cv_builder_data():
    """
    Returns a complete dictionary for populating the CV Builder.
    Structure matches st.session_state["cv_builder"].
    """
    return {
        "name": "Giacomo Dellacqua",
        "location": "Vigevano, Lombardia, Italy",
        "email": "dellacquagiacomo@gmail.com",
        "phone": "+39 351 930 1321",
        "summary": "Results-driven Digital Marketing Data Analyst with expertise in AI-powered business solutions and data-driven decision-making. Currently pursuing Master's in Artificial Intelligence for Business while gaining hands-on experience in marketing analytics, tracking implementation, and performance optimization at Randstad Group Italia.",
        "competencies": ["Machine Learning", "Data Analytics", "Digital Marketing", "Google Cloud Platform", "Business Intelligence", "Predictive Modeling", "Marketing Automation", "Python", "SQL", "BigQuery"],
        "experiences": [
            {
                "title": "Digital Marketing Data Analyst Intern",
                "company": "Randstad Group Italia SPA",
                "dates": "November 2025 – Present",
                "location": "Milan, Italy (Hybrid)",
                "bullets": "• Implement and maintain online tracking ecosystems using Google Tag Manager.\n• Analyze website performance using Google Analytics 4.\n• Design interactive dashboards with Google Looker Studio.\n• Support paid performance campaigns and conduct A/B testing.",
                "tech": "Google Analytics 4, Google Tag Manager, Google Looker Studio, SQL, Python"
            },
            {
                "title": "Junior Digital Marketing Specialist",
                "company": "Otreat",
                "dates": "January 2024 – March 2024",
                "location": "Milan, Italy (Hybrid)",
                "bullets": "• Managed multi-platform social media presence and executed performance-driven marketing strategies.\n• Developed advertising campaigns and email newsletters.\n• Operated CRM systems and e-commerce platforms.\n• Conducted quantitative analysis of campaign metrics.",
                "tech": "Social Media Tools, CRM Platforms, E-commerce Systems, Email Marketing"
            }
        ],
        "education": [
            {
                "degree": "Master's Degree in Artificial Intelligence for Business and Society",
                "institution": "Università IULM",
                "dates": "2024 - 2026",
                "location": "Milan, Italy",
                "details": "Specialized curriculum integrating AI, Big Data, Marketing Analytics. Coursework: Machine Learning, Predictive Analytics, Big Data Management."
            },
            {
                "degree": "Bachelor's Degree in Corporate Communication and Public Relations",
                "institution": "Università IULM",
                "dates": "2021 - 2024",
                "location": "Milan, Italy",
                "details": "Specialized in strategic communication, stakeholder relations, and business management."
            }
        ],
        "projects": [
            {
                "name": "Dropout Predictor AI",
                "link": "https://github.com/Giacomod2001/dropout-predictor", 
                "description": "Designed and developed a functional MVP of a cloud-native ML platform to predict university dropout risk, demonstrating data-driven retention strategies."
            }
        ],
        "languages": [
            {"language": "Italian", "level": "Native"},
            {"language": "English", "level": "Intermediate (B1-B2)"}
        ]
    }


def get_demo_builder_jd():
    """Returns sample JD for the CV Builder suggestions (Target ~75% match)."""
    return """
DATA ANALYST - MARKETING FOCUS
TechCorp Italia | Milan, Italy (Hybrid)

About the Job:
We are looking for a Data Analyst to join our Marketing Intelligence team. The ideal candidate has a strong background in data analysis and digital marketing.

Key Responsibilities:
- Analyze marketing performance using Google Analytics 4 (GA4) and SQL.
- Build and maintain dashboards in Looker Studio and Tableau.
- Implement tracking via Google Tag Manager (GTM).
- Collaborate with the marketing team to optimize ROI and campaign strategies.
- Use Python for data cleaning and predictive modeling.

Requirements:
- 2+ years of experience in Data Analysis or Digital Marketing.
- Proficiency in SQL and Python (pandas, scikit-learn).
- Expert knowledge of Google Analytics 4 and GTM.
- Experience with Data Visualization tools (Looker Studio required, Tableau is a plus).
- Knowledge of Cloud Platforms (AWS or Azure preferred).
- Fluent in Italian and English (B2+).
"""



def get_energy_demo_cv():
    """Returns sample CV for Energy Engineer (100% match case study)."""
    return """
LUCA VERDI
Energy Engineer | RES Specialist
Milan, Italy | l.verdi@email.com | +39 333 123 4567

SUMMARY
Highly analytical Energy Engineer with a strong background in thermodynamics and power systems. 
Expert in renewable energy integration and energy efficiency optimization for industrial plants.

SKILLS
- Core: Thermodynamics, Power Systems, Energy Efficiency, Renewable Energy
- Tools: MATLAB, Simulink, AutoCAD, Excel (Advanced), Python
- General: Engineering, Project Management, Statistical Analysis

EXPERIENCE
Junior Energy Engineer | GreenPower Solutions | 2023 - Present
- Conducted energy audits for industrial facilities, improving energy efficiency by 15%.
- Modeled complex thermodynamics systems to optimize heat recovery.
- Designed power systems for large-scale solar and wind farms using AutoCAD.

RESEARCH PROJECT
Smart Grid Optimization | University Case Study
- Developed a Python-based simulation for demand-response in smart grids.
- Calculated energy efficiency metrics for various renewable energy scenarios.

EDUCATION
Master's Degree in Energy Engineering | Politecnico di Milano | 2021 - 2023
- Focus: Renewable Energy Systems and Power Grid Stability
"""

def get_energy_demo_jd():
    """Returns sample JD for Energy Engineer (100% match case study)."""
    return """
ENERGY ENGINEER
Enel Green Power | Rome, Italy

We are seeking a dedicated Energy Engineer to join our Renewable Energy division.

RESPONSIBILITIES:
- Perform thermodynamics analysis for energy generation plants.
- Design and optimize power systems for renewable energy integration.
- Implement energy efficiency programs across our operations.
- Use MATLAB and Python for system modeling and simulation.

REQUIREMENTS:
- Degree in Energy Engineering or similar.
- Strong knowledge of Thermodynamics and Power Systems.
- Proficiency in MATLAB, Python, and Excel.
- Experience with Renewable Energy technologies.
- Background in Engineering fundamentals.
"""

def get_energy_demo_project():
    """Returns sample project for Energy Engineer demo."""
    return """
RENEWABLE GRID SIMULATOR
Key Skills: Thermodynamics, Power Systems, Python, Energy Efficiency

Developed a comprehensive simulator to evaluate the impact of high renewable energy 
penetration on national power systems. Used Python and MATLAB for modeling 
thermodynamic cycles and grid stability.
"""
