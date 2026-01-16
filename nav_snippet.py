def render_navigation():
    """
    Renders the global sidebar navigation menu.
    """
    with st.sidebar:
        # Branding
        st.markdown("""
        <div style='text-align: center; padding: 0.5rem 0;'>
            <h2 style='font-size: 1.5rem; margin: 0;'>CareerMatch AI</h2>
            <p style='color: #00A0DC; font-size: 0.8rem; font-weight: 600; margin: 0;'>CAREER ASSISTANT</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        
        # Navigation
        current_page = st.session_state.get("page", "Landing")
        
        nav_map = {
            "Home": "Landing",
            "CV Analysis": "CV Evaluation",
            "CV Builder": "CV Builder",
            "Career Discovery": "Career Discovery",
            "Dev Console": "Debugger"
        }
        
        # Determine index
        options = list(nav_map.keys())
        # Find which option maps to current_page
        default_idx = 0
        for i, (label, target) in enumerate(nav_map.items()):
            if target == current_page:
                default_idx = i
                break
        
        selected = st.radio("Navigation", options, index=default_idx, label_visibility="collapsed")
        
        target_page = nav_map[selected]
        if target_page != current_page:
            st.session_state["page"] = target_page
            st.rerun()
            
        st.divider()
        
        # Demo Controls
        if st.toggle("Demo Mode", value=st.session_state.get("demo_mode", False)):
             if not st.session_state.get("demo_mode", False):
                 st.session_state["demo_mode"] = True
                 # Auto-load demo data if switching ON
                 st.session_state["cv_text"] = styles.get_demo_cv()
                 st.session_state["jd_text"] = styles.get_demo_jd()
                 st.session_state["proj_text"] = styles.get_demo_project()
                 st.session_state["show_project_toggle"] = True
                 st.session_state["show_cover_letter"] = True
                 st.rerun()
             st.session_state["demo_mode"] = True
        else:
             st.session_state["demo_mode"] = False
             
        st.caption("v2.1 | Local Mode")
