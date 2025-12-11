import streamlit as st

# LinkedIn-inspired Color Palette
PRIMARY_COLOR = "#0077b5"       # LinkedIn Blue
BACKGROUND_COLOR = "#f3f2ef"    # LinkedIn Light Gray
TEXT_COLOR = "#191919"          # LinkedIn Black (Almost Black)
SECONDARY_TEXT_COLOR = "#666666" # LinkedIn Secondary Text
CARD_BG_COLOR = "#ffffff"       # White Card Background
BORDER_COLOR = "#d0d0d0"        # Slightly darker border for visibility

def inject_custom_css():
    """
    Injects global CSS to style the Streamlit app with a LinkedIn-like theme.
    Includes HIGH CONTRAST fixes.
    """
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        /* FORCE GLOBAL TEXT COLOR */
        html, body, [class*="css"], .stMarkdown, .stText, p, h1, h2, h3, h4 {{
            font-family: 'Inter', sans-serif !important;
            color: {TEXT_COLOR} !important;
        }}
        
        /* Main Background */
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}
        
        /* Cards */
        .linkedin-card {{
            background-color: {CARD_BG_COLOR};
            border-radius: 8px;
            border: 1px solid {BORDER_COLOR};
            padding: 24px; /* Increased padding */
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        }}

        /* Headers within cards */
        .linkedin-card h3 {{
            color: {TEXT_COLOR} !important;
            font-weight: 700 !important;
        }}
        
        .linkedin-card p {{
            color: {SECONDARY_TEXT_COLOR} !important;
            font-weight: 500 !important;
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
            border-radius: 24px;
            border: none;
            padding: 0.6rem 1.5rem;
            font-weight: 600;
        }}
        
        .stButton > button:hover {{
            background-color: #004182 !important; /* Darker Blue */
            color: white !important;
        }}

        /* Inputs (Text Area, File Uploader) FIX */
        .stTextArea textarea {{
            background-color: white !important;
            color: {TEXT_COLOR} !important; 
            border: 1px solid #8e8e8e !important; /* Visible border */
        }}
        
        .stTextArea textarea:focus {{
            border-color: {PRIMARY_COLOR} !important;
            box-shadow: 0 0 0 1px {PRIMARY_COLOR} !important;
        }}
        
        /* File Uploader */
        [data-testid="stFileUploader"] {{
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px dashed #8e8e8e;
        }}

        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: white !important;
            border-right: 1px solid {BORDER_COLOR};
        }}
        
        .sidebar-text {{
            color: {SECONDARY_TEXT_COLOR} !important;
            font-size: 0.9rem;
        }}

        /* Expander */
        .streamlit-expanderHeader {{
            background-color: white !important;
            color: {TEXT_COLOR} !important;
            font-weight: 600 !important;
            border: 1px solid {BORDER_COLOR};
        }}
        
        .streamlit-expanderContent {{
            background-color: white !important;
            color: {TEXT_COLOR} !important;
            border-top: none;
        }}
        
    </style>
    """, unsafe_allow_html=True)
