import streamlit as st

# LinkedIn-inspired Color Palette
PRIMARY_COLOR = "#0077b5"       # LinkedIn Blue
BACKGROUND_COLOR = "#f3f2ef"    # LinkedIn Light Gray
TEXT_COLOR = "#191919"          # LinkedIn Black
SECONDARY_TEXT_COLOR = "#666666" # LinkedIn Secondary Text
CARD_BG_COLOR = "#ffffff"       # White Card Background
BORDER_COLOR = "#e0e0e0"        # Subtle Border

def inject_custom_css():
    """
    Injects global CSS to style the Streamlit app with a LinkedIn-like theme.
    """
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        /* Global Font & Background */
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: {TEXT_COLOR};
        }}
        
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}

        /* Cards */
        .linkedin-card {{
            background-color: {CARD_BG_COLOR};
            border-radius: 8px;
            border: 1px solid {BORDER_COLOR};
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08); /* Slight shadow for depth */
        }}

        /* Headers within cards */
        .linkedin-card h3 {{
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: {TEXT_COLOR};
        }}
        
        .linkedin-card p {{
            color: {SECONDARY_TEXT_COLOR};
            font-size: 0.95rem;
            line-height: 1.5;
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 24px;
            border: none;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: background-color 0.2s;
        }}
        
        .stButton > button:hover {{
            background-color: #005582;
            color: white;
            border: none;
        }}

        /* Text Areas & Inputs */
        .stTextArea textarea {{
            background-color: white;
            border: 1px solid {BORDER_COLOR};
            border-radius: 4px;
        }}
        
        .stTextArea textarea:focus {{
            border-color: {PRIMARY_COLOR};
            box-shadow: 0 0 0 1px {PRIMARY_COLOR};
        }}

        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: #ffffff;
            border-right: 1px solid {BORDER_COLOR};
        }}

        /* Expander */
        .streamlit-expanderHeader {{
            background-color: white;
            border-radius: 4px;
        }}
        
        /* Badges / Metrics logic can be handled via Markdown in app.py but basics here */
        code {{
            color: {TEXT_COLOR};
            background-color: #eef3f8 !important; /* Light blue tint background */
            border-radius: 4px;
            padding: 2px 6px;
            border: 1px solid #dce6f1;
        }}
        
    </style>
    """, unsafe_allow_html=True)
