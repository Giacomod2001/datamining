"""
================================================================================
CareerMatch AI - Visual Design System (styles.py)
================================================================================

KDD Step 7 -- Knowledge Presentation.

Public API used elsewhere in the app:
- get_premium_css(theme="dark") -> str  (call once at app start; pass current
  theme to switch between dark and light without reloading)

The module exposes a single function so that `app.py` can re-inject the
correct CSS on every rerun depending on `ui_components.get_theme()`. This
keeps theme switching free of JavaScript hacks while still being instant.

================================================================================
LAYERS:
    1. Tokens           -- CSS custom properties (theme-aware)
    2. Base             -- typography, scrollbars, app background
    3. Components       -- cm-hero, cm-metric, cm-card-*, cm-section-*, cm-tag-row
    4. Streamlit hooks  -- overrides on st.button, st.tabs, st.expander, etc.
    5. Skill tags       -- legacy classes preserved (skill-tag-*)
    6. Sidebar + chat   -- Ruben assistant container
    7. Accessibility    -- focus rings, reduced motion, high contrast, print
    8. Responsive       -- mobile / tablet / iPhone SE breakpoints
================================================================================
"""

from __future__ import annotations


# =============================================================================
# THEME TOKENS
# =============================================================================
# Two compact dictionaries: one per theme. The rest of the CSS only references
# CSS custom properties so the bulk of the stylesheet is theme-agnostic.

_DARK_TOKENS = {
    # surfaces
    "bg-base":      "#0d1117",
    "bg-surface":   "#161b22",
    "bg-elevated":  "#21262d",
    "bg-gradient":  "linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%)",
    # text
    "text-primary":   "#f0f6fc",
    "text-secondary": "#8b949e",
    "text-muted":     "#6e7681",
    # borders
    "border":          "#30363d",
    "border-strong":   "#444c56",
    # brand
    "brand":         "#0077B5",
    "brand-dark":    "#004471",
    "brand-light":   "#00A0DC",
    "accent-green":  "#00C853",
    "accent-amber":  "#FFB300",
    "accent-red":    "#E53935",
    "accent-teal":   "#00C9A7",
    # focus ring (WCAG AA, ~3:1 against dark surface)
    "focus-ring":    "rgba(0, 160, 220, 0.65)",
    # shadows
    "shadow-sm":  "0 1px 3px rgba(0,0,0,0.35)",
    "shadow-md":  "0 4px 8px rgba(0,0,0,0.45)",
    "shadow-lg":  "0 10px 24px rgba(0,0,0,0.55)",
    # tags (matched / missing / transferable / project / bonus)
    "tag-matched-bg":         "linear-gradient(135deg, #1e4620 0%, #155724 100%)",
    "tag-matched-color":      "#75f083",
    "tag-matched-border":     "#2d5a30",
    "tag-missing-bg":         "linear-gradient(135deg, #5c1f23 0%, #842029 100%)",
    "tag-missing-color":      "#ff8a8a",
    "tag-missing-border":     "#8a3035",
    "tag-transferable-bg":    "linear-gradient(135deg, #5c4813 0%, #856404 100%)",
    "tag-transferable-color": "#ffd666",
    "tag-transferable-border":"#7a5f10",
    "tag-project-bg":         "linear-gradient(135deg, #0a3d62 0%, #084298 100%)",
    "tag-project-color":      "#7ec8ff",
    "tag-project-border":     "#0d5aa7",
    "tag-bonus-bg":           "linear-gradient(135deg, #2d333b 0%, #41464b 100%)",
    "tag-bonus-color":        "#b1b8c0",
    "tag-bonus-border":       "#484f58",
}

def _render_tokens(tokens: dict[str, str]) -> str:
    """Emit a CSS :root block from a token dict."""
    body = "\n    ".join(f"--cm-{k}: {v};" for k, v in tokens.items())
    return f":root {{\n    {body}\n}}"


# =============================================================================
# PUBLIC API
# =============================================================================

def get_premium_css(theme: str = "dark") -> str:
    """
    Return the complete CSS bundle.

    The `theme` parameter is accepted for backward compatibility but ignored:
    the project ships dark only. Reintroducing light mode would require
    restoring _LIGHT_TOKENS and the sidebar toggle.
    """
    tokens = _DARK_TOKENS
    return f"""
<style>
/* =============================================================================
   1. THEME TOKENS (dark)
   ============================================================================= */
{_render_tokens(tokens)}

/* =============================================================================
   2. BASE
   ============================================================================= */
.stApp {{
    background: var(--cm-bg-gradient);
    color: var(--cm-text-primary);
}}

#MainMenu, footer {{ visibility: hidden; }}

h1, h2, h3, h4, h5, h6 {{
    font-weight: 600;
    margin-top: 1.25rem;
    margin-bottom: 0.75rem;
    color: var(--cm-text-primary);
}}

p, span, label, div, li {{ color: var(--cm-text-primary); }}

/* Brand gradient title used by h1 and .cm-gradient-text */
h1, .cm-gradient-text {{
    background: linear-gradient(90deg, var(--cm-brand-light), var(--cm-brand), var(--cm-brand-dark));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: var(--cm-brand);  /* Firefox fallback */
}}

hr {{
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--cm-border), var(--cm-brand), var(--cm-border), transparent);
    margin: 2rem 0;
}}

/* =============================================================================
   3. COMPONENT CLASSES (used by ui_components.py)
   ============================================================================= */

.cm-hero {{
    text-align: center;
    padding: 2.5rem 1rem 1rem;
    width: 100%;
}}

.cm-hero-title {{
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    line-height: 1.1;
}}

.cm-hero-subtitle {{
    font-size: clamp(0.95rem, 1.5vw, 1.1rem);
    color: var(--cm-text-secondary);
    margin: 0;
}}

.cm-section-header {{
    text-align: center;
    margin-bottom: 1.5rem;
}}

.cm-section-title {{
    margin: 0;
    padding: 0;
    font-size: clamp(1.75rem, 3vw, 2.25rem);
}}

.cm-section-subtitle {{
    color: var(--cm-text-secondary);
    margin: 0.25rem 0 0 0;
    font-size: 0.95rem;
}}

.cm-metric-row {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 2.5rem;
    margin-bottom: 1.5rem;
    padding: 0 1rem;
}}

.cm-metric {{
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
}}

.cm-metric-value {{
    font-size: clamp(1.6rem, 2.5vw, 2rem);
    font-weight: 700;
    margin: 0;
}}

.cm-metric-label {{
    color: var(--cm-text-secondary);
    font-size: 1.05rem;
}}

.cm-card-content {{
    text-align: center;
}}

.cm-card-title {{
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
    color: var(--cm-text-primary);
}}

.cm-card-body {{
    color: var(--cm-text-secondary);
    font-size: 0.9rem;
    line-height: 1.45;
    min-height: 3.5rem;
    margin: 0 0 1rem 0;
}}

.cm-tag-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 0.5rem 0;
}}

.cm-footer {{
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
    color: var(--cm-text-muted);
    font-size: 0.85rem;
    padding: 1rem 0;
}}

.cm-skip-link {{
    position: absolute;
    left: -9999px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
}}
.cm-skip-link:focus {{
    position: fixed;
    top: 0.5rem;
    left: 0.5rem;
    width: auto;
    height: auto;
    padding: 0.5rem 1rem;
    background: var(--cm-bg-elevated);
    color: var(--cm-text-primary);
    border: 2px solid var(--cm-brand-light);
    border-radius: 6px;
    z-index: 10000;
}}

/* =============================================================================
   4. STREAMLIT WIDGET OVERRIDES
   ============================================================================= */

/* Buttons (primary = gradient, secondary = outlined surface) */
.stButton > button {{
    background: linear-gradient(135deg, var(--cm-brand) 0%, var(--cm-brand-dark) 100%);
    color: #ffffff;
    border: none;
    padding: 0.7rem 1.2rem;
    border-radius: 8px;
    font-weight: 600;
    width: 100%;
    min-height: 2.75rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.2s ease;
    box-shadow: var(--cm-shadow-sm);
}}
.stButton > button:hover {{
    transform: translateY(-1px);
    box-shadow: var(--cm-shadow-md);
    background: linear-gradient(135deg, var(--cm-brand-light) 0%, var(--cm-brand) 100%);
}}
.stButton > button:active {{ transform: translateY(0); }}
.stButton > button:disabled {{
    background: var(--cm-bg-elevated);
    color: var(--cm-text-muted);
    cursor: not-allowed;
    box-shadow: none;
}}

/* Secondary buttons (kind="secondary"): surface bg, brand border + text */
.stButton > button[kind="secondary"] {{
    background: var(--cm-bg-surface);
    color: var(--cm-brand);
    border: 1.5px solid var(--cm-brand);
    box-shadow: none;
}}
.stButton > button[kind="secondary"]:hover {{
    background: color-mix(in srgb, var(--cm-brand) 12%, var(--cm-bg-surface));
    color: var(--cm-brand);
    box-shadow: var(--cm-shadow-sm);
}}

/* Bordered container (st.container(border=True)) */
[data-testid="stVerticalBlockBordered"] {{
    background: color-mix(in srgb, var(--cm-bg-surface) 70%, transparent);
    border: 1px solid var(--cm-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.25rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}
[data-testid="stVerticalBlockBordered"]:hover {{
    border-color: var(--cm-brand);
    box-shadow: 0 0 12px color-mix(in srgb, var(--cm-brand) 25%, transparent);
}}

/* Inputs */
.stTextArea textarea,
.stTextInput input,
.stNumberInput input,
.stDateInput input {{
    background: var(--cm-bg-elevated);
    border: 1px solid var(--cm-border);
    border-radius: 8px;
    color: var(--cm-text-primary);
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
}}
.stTextArea textarea:focus,
.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus {{
    border-color: var(--cm-brand);
    box-shadow: 0 0 0 3px var(--cm-focus-ring);
    outline: none;
}}

/* File uploader */
.stFileUploader {{
    background: var(--cm-bg-elevated);
    border: 2px dashed var(--cm-border);
    border-radius: 12px;
    padding: 1rem;
    transition: border-color 0.2s ease, background 0.2s ease;
}}
.stFileUploader:hover {{
    border-color: var(--cm-brand);
    background: color-mix(in srgb, var(--cm-brand) 8%, var(--cm-bg-elevated));
}}

/* Expander */
.streamlit-expanderHeader,
[data-testid="stExpander"] details summary {{
    background: var(--cm-bg-elevated);
    border-radius: 8px;
    border: 1px solid var(--cm-border);
    transition: border-color 0.15s ease, background 0.15s ease;
}}
.streamlit-expanderHeader:hover,
[data-testid="stExpander"] details summary:hover {{
    border-color: var(--cm-brand);
    background: color-mix(in srgb, var(--cm-brand) 6%, var(--cm-bg-elevated));
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 4px;
    background: var(--cm-bg-elevated);
    padding: 6px;
    border-radius: 12px;
    flex-wrap: wrap;
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 8px;
    padding: 8px 12px;
    transition: background 0.15s ease;
    font-size: 0.9rem;
    color: var(--cm-text-primary);
}}
.stTabs [data-baseweb="tab"]:hover {{
    background: color-mix(in srgb, var(--cm-brand) 12%, transparent);
}}
.stTabs [aria-selected="true"] {{
    background: var(--cm-brand);
    color: #ffffff;
}}

/* Progress */
.stProgress > div > div {{
    background: linear-gradient(90deg, var(--cm-brand), var(--cm-brand-light), var(--cm-accent-green));
    border-radius: 10px;
}}

/* Metrics widget */
[data-testid="stMetricValue"] {{
    font-size: 2.25rem;
    font-weight: 700;
    background: linear-gradient(90deg, var(--cm-brand-light), var(--cm-brand));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: var(--cm-brand);
}}

/* Alerts */
.stAlert {{
    border-radius: 12px;
    border-left-width: 4px;
}}

/* =============================================================================
   5. SKILL TAGS (legacy class names preserved)
   ============================================================================= */
.skill-tag-matched, .skill-tag-missing, .skill-tag-transferable,
.skill-tag-project, .skill-tag-bonus {{
    display: inline-block;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 4px;
    border-style: solid;
    border-width: 1px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}}
.skill-tag-matched:hover, .skill-tag-missing:hover, .skill-tag-transferable:hover,
.skill-tag-project:hover, .skill-tag-bonus:hover {{
    transform: translateY(-1px);
    box-shadow: var(--cm-shadow-sm);
}}

.skill-tag-matched {{
    background: var(--cm-tag-matched-bg);
    color: var(--cm-tag-matched-color);
    border-color: var(--cm-tag-matched-border);
}}
.skill-tag-missing {{
    background: var(--cm-tag-missing-bg);
    color: var(--cm-tag-missing-color);
    border-color: var(--cm-tag-missing-border);
}}
.skill-tag-transferable {{
    background: var(--cm-tag-transferable-bg);
    color: var(--cm-tag-transferable-color);
    border-color: var(--cm-tag-transferable-border);
}}
.skill-tag-project {{
    background: var(--cm-tag-project-bg);
    color: var(--cm-tag-project-color);
    border-color: var(--cm-tag-project-border);
}}
.skill-tag-bonus {{
    background: var(--cm-tag-bonus-bg);
    color: var(--cm-tag-bonus-color);
    border-color: var(--cm-tag-bonus-border);
}}

/* =============================================================================
   6. SIDEBAR + RUBEN CHAT
   ============================================================================= */
section[data-testid="stSidebar"] {{
    background: var(--cm-bg-surface);
    border-right: 1px solid var(--cm-border);
}}
section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {{
    color: var(--cm-brand-light);
    -webkit-text-fill-color: var(--cm-brand-light);
}}

.sidebar-chat-container {{
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    padding: 1.25rem;
    background: color-mix(in srgb, var(--cm-brand) 8%, transparent);
    border: 1px solid color-mix(in srgb, var(--cm-brand) 35%, transparent);
    border-radius: 14px;
    box-shadow: inset 0 0 18px color-mix(in srgb, var(--cm-brand) 8%, transparent);
}}

.sidebar-chat-header {{
    font-size: 0.95rem;
    font-weight: 800;
    color: var(--cm-accent-teal);
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid color-mix(in srgb, var(--cm-accent-teal) 25%, transparent);
    padding-bottom: 6px;
}}

.sidebar-chat-message {{
    background: var(--cm-bg-elevated);
    color: var(--cm-text-primary);
    border: 1px solid var(--cm-border-strong);
    padding: 14px 18px;
    border-radius: 16px;
    font-size: 0.92rem;
    line-height: 1.55;
    margin-top: 0.75rem;
    box-shadow: var(--cm-shadow-sm);
}}

.landing-chat-popup {{
    background: linear-gradient(135deg, var(--cm-bg-elevated) 0%, var(--cm-bg-surface) 100%);
    border: 1px solid var(--cm-brand);
    border-radius: 16px;
    padding: 1.75rem;
    margin: 1.5rem auto;
    max-width: 800px;
    text-align: center;
    box-shadow: var(--cm-shadow-md);
}}

.landing-chat-popup-title {{
    color: var(--cm-brand-light);
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    font-size: 1.25rem;
}}

/* =============================================================================
   7. ACCESSIBILITY
   ============================================================================= */

/* Keyboard focus rings (WCAG 2.1 AA) */
.stButton > button:focus-visible,
.stTextArea textarea:focus-visible,
.stTextInput input:focus-visible,
.stSelectbox div[data-baseweb="select"]:focus-within,
.stCheckbox label:focus-within,
.stRadio label:focus-within,
a:focus-visible,
[role="button"]:focus-visible {{
    outline: 3px solid var(--cm-focus-ring);
    outline-offset: 2px;
    border-radius: 6px;
}}
/* Hide focus ring for mouse-only interactions */
.stButton > button:focus:not(:focus-visible),
.stTextArea textarea:focus:not(:focus-visible),
.stTextInput input:focus:not(:focus-visible) {{
    outline: none;
}}

/* Reduced motion users */
@media (prefers-reduced-motion: reduce) {{
    *, *::before, *::after {{
        animation-duration: 0.001ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.001ms !important;
        scroll-behavior: auto !important;
    }}
}}

/* High contrast */
@media (prefers-contrast: more) {{
    .stButton > button {{ border: 2px solid var(--cm-text-primary); }}
    .skill-tag-matched, .skill-tag-missing, .skill-tag-transferable,
    .skill-tag-project, .skill-tag-bonus {{ border-width: 2px; }}
}}

/* Windows forced colors */
@media (forced-colors: active) {{
    .stButton > button {{ border: 2px solid ButtonText; }}
    [data-testid="stVerticalBlockBordered"] {{ border: 1px solid CanvasText; }}
}}

/* =============================================================================
   8. RESPONSIVE
   ============================================================================= */

@media (max-width: 768px) {{
    .stButton > button {{ width: 100%; min-height: 3rem; }}
    .cm-metric-row {{ gap: 1rem; }}
    .cm-hero {{ padding: 1.5rem 0.75rem 0.75rem; }}
}}

@media (max-width: 480px) {{
    .stButton > button {{ padding: 0.6rem 1rem; font-size: 0.95rem; }}
    [data-testid="stVerticalBlockBordered"] {{ padding: 1rem; }}
    .cm-metric {{ flex-direction: column; align-items: center; gap: 0; }}
    .cm-metric-label {{ font-size: 0.9rem; }}
}}

/* Touch devices (coarse pointer) */
@media (pointer: coarse) {{
    .stButton > button {{ min-height: 48px; padding: 12px 24px; }}
    .skill-tag-matched, .skill-tag-missing, .skill-tag-transferable,
    .skill-tag-project, .skill-tag-bonus {{ padding: 10px 16px; margin: 5px; }}
    .stButton > button:hover, [data-testid="stVerticalBlockBordered"]:hover {{
        transform: none;
    }}
}}

/* iOS Safari: prevent zoom on focus */
@supports (-webkit-touch-callout: none) {{
    .stTextArea textarea, .stTextInput input {{ font-size: 16px; }}
    .stButton > button {{ -webkit-appearance: none; appearance: none; }}
}}

/* Safe area for notched devices */
@supports (padding-top: env(safe-area-inset-top)) {{
    .stApp {{
        padding-top: env(safe-area-inset-top);
        padding-bottom: env(safe-area-inset-bottom);
        padding-left: env(safe-area-inset-left);
        padding-right: env(safe-area-inset-right);
    }}
}}

/* Print (CV export friendly) */
@media print {{
    .stApp {{ background: white !important; color: black !important; }}
    section[data-testid="stSidebar"], .stButton,
    .stProgress, [data-testid="collapsedControl"] {{ display: none !important; }}
    [data-testid="stVerticalBlockBordered"] {{
        box-shadow: none !important;
        border: 1px solid #ddd !important;
        page-break-inside: avoid;
    }}
}}

/* =============================================================================
   9. ANIMATIONS (kept compact)
   ============================================================================= */
@keyframes cm-fade-in-up {{
    from {{ opacity: 0; transform: translateY(14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
.fade-in {{ animation: cm-fade-in-up 0.45s ease-out both; }}

@keyframes cm-pulse {{
    0%, 100% {{ opacity: 1; }}
    50%       {{ opacity: 0.7; }}
}}
.pulse {{ animation: cm-pulse 2s ease-in-out infinite; }}

@keyframes cm-shimmer {{
    0%   {{ background-position: -200% 0; }}
    100% {{ background-position: 200% 0; }}
}}
.skeleton {{
    background: linear-gradient(90deg, var(--cm-bg-elevated) 25%, var(--cm-bg-surface) 50%, var(--cm-bg-elevated) 75%);
    background-size: 200% 100%;
    animation: cm-shimmer 1.5s infinite;
    border-radius: 4px;
}}

/* =============================================================================
   10. SCROLLBARS
   ============================================================================= */
::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: var(--cm-bg-base); }}
::-webkit-scrollbar-thumb {{ background: var(--cm-border); border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--cm-brand); }}
* {{ scrollbar-width: thin; scrollbar-color: var(--cm-border) var(--cm-bg-base); }}

/* =============================================================================
   11. SIDEBAR DETAIL POLISH (M2.1)
   ============================================================================= */

/* Vertical breathing room between sidebar widget groups */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"]
  > [data-testid="stElementContainer"] {{
    margin-bottom: 0.5rem;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] {{
    margin-top: 0.75rem;
}}

/* Version stamp under the theme toggle */
.cm-sidebar-version {{
    margin-top: 0.5rem;
    margin-bottom: 0.25rem;
    color: var(--cm-text-muted);
    font-size: 0.78rem;
    text-align: center;
    letter-spacing: 0.04em;
}}

/* Expander in the sidebar -- legible on both themes */
section[data-testid="stSidebar"] [data-testid="stExpander"] details {{
    background: var(--cm-bg-elevated);
    border: 1px solid var(--cm-border);
    border-radius: 10px;
    padding: 0.25rem 0.5rem;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] details summary {{
    color: var(--cm-text-primary);
    font-weight: 600;
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] details summary:hover {{
    color: var(--cm-brand);
}}
section[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stCaptionContainer"],
section[data-testid="stSidebar"] [data-testid="stExpander"] p {{
    color: var(--cm-text-secondary);
}}

/* Ruben chat input: theme-aware, comfortable size */
.sidebar-chat-container + div .stTextInput input,
section[data-testid="stSidebar"] .stTextInput input {{
    background: var(--cm-bg-elevated);
    color: var(--cm-text-primary);
    border: 1px solid var(--cm-border);
}}
.sidebar-chat-container + div .stTextInput input::placeholder,
section[data-testid="stSidebar"] .stTextInput input::placeholder {{
    color: var(--cm-text-muted);
}}

/* =============================================================================
   12. BOX SIZING + BASE FIXES
   ============================================================================= */
*, *::before, *::after {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; -webkit-overflow-scrolling: touch; }}
</style>
"""
