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
    margin-top: 1.5rem !important;
    margin-bottom: 1rem !important;
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
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-md);
    transition: all var(--transition-normal);
}

/* Ensure the widget container inside the column also stretches */
[data-testid="stVerticalBlockBordered"] {
    background: rgba(31, 38, 52, 0.4) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    padding: 2rem !important;
    margin-bottom: 1.5rem !important;
    min-height: 100px !important; 
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    transition: all var(--transition-normal) !important;
}

[data-testid="stVerticalBlockBordered"] h4 {
    margin-top: 0 !important;
    margin-bottom: 1rem !important;
}

[data-testid="stVerticalBlockBordered"]:hover {
    border-color: var(--primary-blue) !important;
    box-shadow: 0 0 15px rgba(0, 119, 181, 0.1) !important;
}

[data-testid="stVerticalBlockBordered"] h1,
[data-testid="stVerticalBlockBordered"] h2,
[data-testid="stVerticalBlockBordered"] h3,
[data-testid="stVerticalBlockBordered"] h4 {
    margin-top: 0 !important;
    color: var(--text-primary) !important;
}

.section-spacer {
    height: 1.5rem;
    width: 100%;
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
    /* =============================================================================
       RUBEN AI ASSISTANT UI
       ============================================================================= */
    
    .sidebar-chat-container {
        margin-top: 1.5rem;
        padding: 1.25rem;
        background: rgba(0, 119, 181, 0.05);
        border: 1px solid rgba(0, 119, 181, 0.3);
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        box-shadow: inset 0 0 20px rgba(0, 119, 181, 0.05);
    }
    
    .sidebar-chat-header {
        font-size: 0.9rem;
        font-weight: 800;
        color: #00C9A7 !important;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 0.6rem;
        text-transform: none;
        letter-spacing: 0.4px;
    }
    
    .sidebar-chat-messages {
        max-height: 250px;
        overflow-y: auto;
        padding-right: 4px;
        display: flex;
        flex-direction: column;
        gap: 12px;
        scrollbar-width: thin;
        scrollbar-color: var(--primary-blue) transparent;
    }
    
    .sidebar-chat-message.assistant {
        background: #0d1117 !important;
        color: #f0f6fc !important;
        border: 1px solid #444c56 !important;
        padding: 14px 20px !important;
        border-radius: 20px !important;
        font-size: 0.9rem !important;
        line-height: 1.5 !important;
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.5) !important;
        display: block !important;
        width: 100% !important;
        margin-bottom: 0.75rem !important;
        font-family: inherit !important;
    }

    .landing-chat-popup {
        background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-card) 100%);
        border: 1px solid var(--primary-blue);
        border-radius: 16px;
        padding: 2rem;
        margin-left: auto !important;
        margin-right: auto !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
        max-width: 800px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        gap: 0.75rem;
    }
        animation: fadeInUp 0.8s ease-out;
        box-shadow: var(--shadow-lg), 0 0 30px rgba(0, 119, 181, 0.1);
    }

    .landing-chat-popup-text {
        width: 100%;
    }

    .landing-chat-popup-title {
        color: var(--primary-light);
        font-weight: 700;
        margin-bottom: 0.25rem !important;
        font-size: 1.25rem;
    }
}

/* =============================================================================
   CROSS-BROWSER COMPATIBILITY FIXES
   ============================================================================= 
   Ensures consistent rendering across:
   - Chrome, Firefox, Safari, Edge
   - iOS Safari, Android Chrome
   - macOS Safari
   ============================================================================= */

/* 1. FLEXBOX CROSS-BROWSER PREFIXES */
.glass-card,
.metric-card,
.hero-gradient,
.sidebar-chat-container,
.landing-chat-popup {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
}

/* 2. BACKDROP-FILTER (Safari/iOS Fix) */
.glass-card {
    /* Standard */
    backdrop-filter: blur(10px);
    /* Safari/WebKit */
    -webkit-backdrop-filter: blur(10px);
    /* Fallback for unsupported browsers */
}

@supports not (backdrop-filter: blur(10px)) {
    .glass-card {
        background: rgba(22, 27, 34, 0.95) !important;
    }
}

/* 3. SMOOTH SCROLLING - Cross Browser */
html {
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch; /* iOS momentum scrolling */
}

/* 4. BORDER-RADIUS CONSISTENCY (Old Safari) */
.stButton > button,
.glass-card,
.metric-card,
.skill-tag-matched,
.skill-tag-missing,
.skill-tag-transferable,
.skill-tag-project,
.skill-tag-bonus {
    -webkit-border-radius: 8px;
    -moz-border-radius: 8px;
    border-radius: 8px;
}

/* 5. BOX-SIZING FIX (Universal) */
*, *::before, *::after {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

/* 6. TRANSFORM/TRANSITION PREFIXES */
.stButton > button:hover,
.glass-card:hover,
.metric-card:hover {
    -webkit-transform: translateY(-2px);
    -moz-transform: translateY(-2px);
    -ms-transform: translateY(-2px);
    transform: translateY(-2px);
    
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}

/* 7. GRADIENT TEXT (Cross-Browser Including Firefox) */
h1 {
    background: linear-gradient(90deg, var(--primary-light), var(--primary-blue), var(--primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    /* Firefox fallback */
    color: var(--primary-blue);
}

@supports (-moz-appearance:none) {
    h1 {
        background: none !important;
        color: var(--primary-blue) !important;
        -webkit-text-fill-color: var(--primary-blue) !important;
    }
}

/* 8. iOS SAFARI SPECIFIC FIXES */
@supports (-webkit-touch-callout: none) {
    /* iOS only */
    .stApp {
        /* Prevent unwanted zoom on input focus */
        touch-action: manipulation;
    }
    
    .stTextArea textarea,
    .stTextInput input {
        /* Prevent iOS zoom on focus */
        font-size: 16px !important;
    }
    
    /* Fix iOS button styling */
    .stButton > button {
        -webkit-appearance: none;
        appearance: none;
    }
    
    /* Fix position:fixed on iOS */
    section[data-testid="stSidebar"] {
        -webkit-overflow-scrolling: touch;
    }
}

/* 9. MOBILE TOUCH OPTIMIZATION */
@media (pointer: coarse) {
    /* Increase touch targets */
    .stButton > button {
        min-height: 48px !important;
        padding: 12px 24px !important;
    }
    
    .skill-tag-matched,
    .skill-tag-missing,
    .skill-tag-transferable,
    .skill-tag-project,
    .skill-tag-bonus {
        padding: 10px 18px !important;
        margin: 6px !important;
    }
    
    /* Disable hover effects on touch */
    .stButton > button:hover,
    .glass-card:hover,
    .metric-card:hover {
        transform: none !important;
        -webkit-transform: none !important;
    }
    
    /* Larger tap targets for links */
    a {
        padding: 8px 0;
    }
}

/* 10. SMALL SCREEN MOBILE FIX (iPhone SE, etc.) */
@media (max-width: 375px) {
    .stButton > button {
        padding: 10px 16px !important;
        font-size: 14px !important;
    }
    
    .glass-card,
    .metric-card {
        padding: 12px !important;
        margin: 8px 0 !important;
    }
    
    h1 {
        font-size: 1.5rem !important;
    }
    
    h2 {
        font-size: 1.25rem !important;
    }
    
    .hero-gradient {
        padding: 1rem !important;
    }
}

/* 11. TABLET LANDSCAPE FIX */
@media (min-width: 768px) and (max-width: 1024px) and (orientation: landscape) {
    section[data-testid="stSidebar"] {
        width: 280px !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 6px 10px !important;
        font-size: 0.8rem !important;
    }
}

/* 12. PRINT STYLES (For CV Export) */
@media print {
    .stApp {
        background: white !important;
    }
    
    .stButton,
    section[data-testid="stSidebar"],
    .stProgress,
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    .glass-card,
    .metric-card {
        box-shadow: none !important;
        border: 1px solid #ddd !important;
        page-break-inside: avoid;
    }
}

/* 13. HIGH CONTRAST MODE SUPPORT */
@media (prefers-contrast: high) {
    :root {
        --primary-blue: #0066cc;
        --text-primary: #ffffff;
        --text-secondary: #cccccc;
        --bg-dark: #000000;
        --bg-card: #1a1a1a;
        --border-color: #ffffff;
    }
    
    .skill-tag-matched,
    .skill-tag-missing,
    .skill-tag-transferable {
        border-width: 2px !important;
    }
}

/* 14. FORCED COLORS MODE (Windows High Contrast) */
@media (forced-colors: active) {
    .stButton > button {
        border: 2px solid ButtonText !important;
    }
    
    .glass-card,
    .metric-card {
        border: 1px solid CanvasText !important;
    }
}

/* 15. SAFARI ANIMATION BUG FIX */
@-webkit-keyframes fadeInUp {
    from {
        opacity: 0;
        -webkit-transform: translateY(20px);
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }
}

/* 16. CHROME SCROLLBAR STYLING */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-dark);
}

::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--primary-blue);
}

/* Firefox scrollbar */
* {
    scrollbar-width: thin;
    scrollbar-color: var(--border-color) var(--bg-dark);
}

/* 17. SAFE AREA INSETS (iPhone X and later notch) */
@supports (padding-top: env(safe-area-inset-top)) {
    .stApp {
        padding-top: env(safe-area-inset-top);
        padding-bottom: env(safe-area-inset-bottom);
        padding-left: env(safe-area-inset-left);
        padding-right: env(safe-area-inset-right);
    }
}

/* 18. DARK MODE FORCED BY STREAMLIT FIX */
[data-theme="dark"] .stApp,
.stApp[data-theme="dark"] {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%) !important;
}

/* 19. PREVENT LAYOUT SHIFT */
.stButton > button,
.stTextArea textarea,
.stTextInput input {
    contain: layout;
}

/* 20. FOCUS VISIBLE (Accessibility) */
.stButton > button:focus-visible,
.stTextArea textarea:focus-visible,
.stTextInput input:focus-visible {
    outline: 2px solid var(--primary-blue) !important;
    outline-offset: 2px !important;
}

/* Hide focus ring for mouse users */
.stButton > button:focus:not(:focus-visible),
.stTextArea textarea:focus:not(:focus-visible),
.stTextInput input:focus:not(:focus-visible) {
    outline: none !important;
}

/* =============================================================================
   AI ASSISTANT UI
   ============================================================================= */

.sidebar-chat-container {
    margin-top: 2rem;
    padding: 1.5rem;
    background: rgba(0, 119, 181, 0.08);
    border: 1px solid rgba(0, 119, 181, 0.4);
    border-radius: 16px;
    box-shadow: inset 0 0 25px rgba(0, 119, 181, 0.08);
    margin-bottom: 1.5rem;
}

.sidebar-chat-header {
    font-size: 1rem;
    font-weight: 800;
    color: #00C9A7 !important;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1rem;
    border-bottom: 1px solid rgba(0, 201, 167, 0.2);
    padding-bottom: 8px;
}

.sidebar-chat-message {
    background: #1c2128;
    color: #f0f6fc;
    border: 1px solid #444c56;
    padding: 16px 22px;
    border-radius: 18px;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-top: 1rem;
    box-shadow: var(--shadow-sm);
}

</style>
"""


# DEMO DATA REMOVED FOR PRODUCTION

