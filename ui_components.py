"""
================================================================================
CareerMatch AI - UI Components (ui_components.py)
================================================================================

Reusable Streamlit components introduced in M2 to:
- Drastically reduce inline `unsafe_allow_html` blocks across app.py
- Give us a single source of truth for headers, hero sections, metrics, cards
- Make the dark/light theme toggle and accessibility helpers consistent
- Keep `app.py` readable while we progressively migrate older pages

Usage:
    from ui_components import (
        hero, section_header, metric_row, link_card,
        skill_tag, theme_toggle, get_theme, footer,
    )

Anything here that emits HTML uses CSS classes defined in `styles.py`. If you
want to add a new visual primitive, add it here -- not as raw HTML in app.py.
================================================================================
"""

from __future__ import annotations

from typing import Iterable, Optional

import streamlit as st


# =============================================================================
# LAYOUT PRIMITIVES
# =============================================================================

def _md(html: str) -> None:
    """
    Emit raw HTML via st.markdown. We strip leading whitespace from every line
    because Streamlit's markdown engine treats 4+ leading spaces as a code
    block -- which silently breaks nested <div>s.
    """
    cleaned = "\n".join(line.lstrip() for line in html.strip().splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)


def hero(title: str, subtitle: Optional[str] = None, accent_gradient: bool = True) -> None:
    """
    Page hero with gradient title. Used by the landing page and major sub-pages.
    Pure-HTML emit -- no extra widgets, so it's safe to call multiple times.
    """
    title_style = "cm-hero-title cm-gradient-text" if accent_gradient else "cm-hero-title"
    subtitle_html = (
        f"<p class='cm-hero-subtitle'>{subtitle}</p>" if subtitle else ""
    )
    _md(f"""
    <header class="cm-hero" role="banner">
    <h1 class="{title_style}">{title}</h1>
    {subtitle_html}
    </header>
    """)


def section_header(title: str, subtitle: Optional[str] = None) -> None:
    """Smaller header for sub-pages. Always centered for visual consistency."""
    subtitle_html = (
        f"<p class='cm-section-subtitle'>{subtitle}</p>" if subtitle else ""
    )
    _md(f"""
    <section class="cm-section-header">
    <h1 class="cm-section-title">{title}</h1>
    {subtitle_html}
    </section>
    """)


def metric_row(items: Iterable[tuple[str, str]]) -> None:
    """
    Render a horizontal row of compact metrics, e.g. 950+ Keywords | 230+ Roles.

    Args:
        items: iterable of (value, label) tuples.
    """
    parts = [
        (
            f"<div class='cm-metric'>"
            f"<span class='cm-metric-value cm-gradient-text'>{value}</span>"
            f"<span class='cm-metric-label'>{label}</span>"
            f"</div>"
        )
        for value, label in items
    ]
    _md(f"<div class='cm-metric-row' role='list'>{''.join(parts)}</div>")


def link_card(title: str, body: str, button_label: str, page_key: str,
              btn_key: str, primary: bool = False) -> None:
    """
    A bordered card with title, body and a button that switches `st.session_state['page']`.
    Designed for the landing page grid.
    """
    btn_type = "primary" if primary else "secondary"
    with st.container(border=True):
        _md(f"""
        <div class="cm-card-content">
        <h3 class="cm-card-title">{title}</h3>
        <p class="cm-card-body">{body}</p>
        </div>
        """)
        if st.button(button_label, key=btn_key, use_container_width=True, type=btn_type):
            st.session_state["page"] = page_key
            st.rerun()


def skill_tag(text: str, kind: str = "matched") -> str:
    """
    Returns the HTML for a skill tag. Use as a string (does NOT call st.markdown
    itself, so the caller can compose many tags in one markdown block).

    `kind` is one of: matched, missing, transferable, project, bonus.
    """
    safe_kinds = {"matched", "missing", "transferable", "project", "bonus"}
    css_class = f"skill-tag-{kind if kind in safe_kinds else 'bonus'}"
    return f"<span class='{css_class}'>{text}</span>"


def render_skill_tags(skills: Iterable[str], kind: str = "matched") -> None:
    """Convenience: render an iterable of skills as a wrapping row of tags."""
    html = " ".join(skill_tag(s, kind) for s in skills)
    _md(f"<div class='cm-tag-row'>{html}</div>")


def footer(left_text: str, right_html: Optional[str] = None) -> None:
    """Unified app footer. `right_html` may contain feedback links etc."""
    right = right_html or ""
    _md(f"""
    <footer class="cm-footer">
    <span class="cm-footer-left">{left_text}</span>
    <span class="cm-footer-right">{right}</span>
    </footer>
    """)


# =============================================================================
# ACCESSIBILITY HELPERS
# =============================================================================

def skip_to_content_link(target_id: str = "main-content") -> None:
    """
    Adds an a11y "skip to content" anchor visible only on keyboard focus.
    Place this at the very top of the page (after navigation render).
    """
    _md(
        f'<a class="cm-skip-link" href="#{target_id}">Skip to main content</a>'
        f'<div id="{target_id}" tabindex="-1"></div>'
    )
