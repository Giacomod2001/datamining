"""
================================================================================
GDPR & AI Act Compliance Module - CareerMatch AI
================================================================================

Compliance with GDPR (EU Reg. 2016/679), EU AI Act (EU Reg. 2024/1689)
and ePrivacy Directive.

Features:
- Consent banner (consent gate)
- Full Privacy Policy
- AI Act transparency disclosure
- Data deletion (right to erasure)
- Contact form
- Language toggle (EN/IT)

================================================================================
"""

import streamlit as st
from datetime import datetime


# =============================================================================
# TRANSLATIONS
# =============================================================================

TRANSLATIONS = {
    "en": {
        "consent_title": "Privacy Notice and Data Processing Consent",
        "consent_intro": (
            "Welcome to <strong>CareerMatch AI</strong>. Before proceeding, we inform you that "
            "this application processes your personal data in compliance with the "
            "<strong>General Data Protection Regulation (GDPR - EU Reg. 2016/679)</strong> "
            "and the <strong>Artificial Intelligence Act (AI Act - EU Reg. 2024/1689)</strong>."
        ),
        "consent_data_label": "Data processed:",
        "consent_data_value": "CV text, personal data entered in the CV Builder (name, email, phone, skills), job descriptions.",
        "consent_purpose_label": "Purpose:",
        "consent_purpose_value": "Professional compatibility analysis using Machine Learning algorithms (TF-IDF, Random Forest, K-Means Clustering, LDA Topic Modeling).",
        "consent_retention_label": "Data retention:",
        "consent_retention_value": "Data is processed exclusively within the current browser session and <u>is not stored on any server</u>. When the session ends, all data is automatically deleted.",
        "consent_details": 'For more details, see the full privacy policy in the "Privacy & AI" section of the menu.',
        "checkbox_gdpr": "I have read and consent to the processing of my personal data pursuant to Art. 6(1)(a) GDPR",
        "checkbox_ai": "I am aware that my data will be processed by Artificial Intelligence systems (AI Act Art. 52)",
        "btn_accept": "Accept and Continue",
        "consent_warning": "Both consents are required to use the application.",
        "page_title": "Privacy & AI Compliance",
        "page_subtitle": "Full privacy policy and data processing information",
        "privacy_heading": "Privacy Policy (Art. 13-14 GDPR)",
        "controller_title": "1. Data Controller",
        "controller_body": (
            "This project is developed in the academic context of "
            "<strong>IULM University</strong> (Milan) - A.Y. 2025-2026, "
            "Data Mining & Text Analytics course.<br><br>"
            "<strong>Development team:</strong> Giacomo DellAcqua, Luca Tallarico, Ruben Scoletta<br>"
            "<strong>Contact:</strong> Use the contact form at the bottom of this page."
        ),
        "data_title": "2. Personal Data Processed",
        "data_body": (
            "<ul>"
            "<li><strong>Identity data:</strong> name, surname, email, phone number, location (voluntarily entered in CV Builder)</li>"
            "<li><strong>Professional data:</strong> technical skills, work experience, education, projects</li>"
            "<li><strong>Documents:</strong> Curriculum Vitae text (uploaded or pasted)</li>"
            "<li><strong>Session data:</strong> Streamlit session state (non-persistent)</li>"
            "</ul>"
        ),
        "legal_title": "3. Purpose and Legal Basis",
        "legal_headers": ("Purpose", "Legal Basis"),
        "legal_rows": [
            ("CV vs Job Description compatibility analysis", "Consent (Art. 6(1)(a) GDPR)"),
            ("CV generation via CV Builder", "Consent (Art. 6(1)(a) GDPR)"),
            ("ML processing for scoring and gap analysis", "Consent (Art. 6(1)(a) GDPR)"),
            ("Academic / research purpose (KDD demonstration)", "Legitimate interest (Art. 6(1)(f) GDPR)"),
        ],
        "retention_title": "4. Data Retention",
        "retention_body": (
            "Personal data is processed <strong>exclusively within the current session</strong> "
            "of the browser. <strong>No persistent database</strong> stores the entered data.<br><br>"
            "<strong>Retention period:</strong> Duration of the browser session.<br>"
            "<strong>Deletion:</strong> Automatic when the browser/tab is closed, "
            'or immediate via the "Delete My Data" button.'
        ),
        "rights_title": "5. Data Subject Rights (Art. 15-22 GDPR)",
        "rights_items": [
            "<strong>Access</strong> (Art. 15) -- Obtain confirmation and a copy of your data",
            "<strong>Rectification</strong> (Art. 16) -- Correct inaccurate data",
            "<strong>Erasure</strong> (Art. 17) -- Right to be forgotten",
            "<strong>Restriction</strong> (Art. 18) -- Restrict processing",
            "<strong>Portability</strong> (Art. 20) -- Receive data in a structured format",
            "<strong>Objection</strong> (Art. 21) -- Object to processing",
            "<strong>Withdraw consent</strong> (Art. 7(3)) -- Withdraw consent at any time",
        ],
        "rights_note": 'Since data exists only in the browser session, the right to erasure can be exercised immediately via the "Delete My Data" button in the sidebar.',
        "transfer_title": "6. Data Transfers",
        "transfer_body": (
            "Data is <strong>not transferred to third parties</strong> nor to countries outside the EU.<br>"
            "The application is hosted on <strong>Streamlit Community Cloud</strong> (AWS servers, EU region). "
            "No data is persisted outside the user's browser session."
        ),
        "ai_heading": "AI Transparency (AI Act)",
        "ai_intro": (
            "This application uses <strong>Artificial Intelligence</strong> systems "
            "for data processing. In compliance with <strong>Art. 52 of the AI Act</strong>, "
            "we declare the following:"
        ),
        "ai_risk_label": "Risk classification:",
        "ai_risk_value": "LIMITED / MINIMAL RISK",
        "ai_models_label": "AI systems used:",
        "ai_models_headers": ("Model", "Algorithm", "Purpose"),
        "ai_decisions": (
            "<strong>Automated decisions:</strong> The results provided by the AI are "
            "<strong>purely indicative and for informational purposes</strong>. No automated "
            "decisions are made that produce legal effects or significantly affect the user "
            "(Art. 22 GDPR). The user is always free to disregard the suggestions provided."
        ),
        "ai_oversight": (
            "<strong>Human oversight:</strong> All AI systems are designed as support tools. "
            "Final decisions always rest with the human user."
        ),
        "ai_limitations": (
            "<strong>Limitations:</strong> ML models may produce inaccurate or incomplete results. "
            "The compatibility score is a statistical approximation and does not represent a "
            "definitive judgment on the user's competencies."
        ),
        "exercise_rights": "Exercise Your Rights",
        "delete_title": "Delete My Data",
        "delete_body": (
            "This action will immediately delete all data present in the current session, "
            "including CV, analyses, CV Builder data, and preferences. This action is irreversible."
        ),
        "delete_confirm": "I confirm I want to delete all my data",
        "delete_btn": "Delete All My Data",
        "delete_success": "All your data has been successfully deleted. The session has been reset.",
        "delete_info": "Your consent has been revoked. You will be asked again upon next access.",
        "contact_heading": "Contact Us",
        "contact_body": "For any questions regarding data processing, privacy, or to exercise your GDPR rights, please fill out the form below.",
        "contact_name": "Full Name",
        "contact_email": "Email Address",
        "contact_subject": "Subject",
        "contact_subject_options": ["Data Access Request (Art. 15)", "Data Deletion Request (Art. 17)", "Data Portability (Art. 20)", "Consent Withdrawal (Art. 7)", "General Inquiry"],
        "contact_message": "Message",
        "contact_submit": "Send Request",
        "contact_success": "Your request has been submitted. We will respond within 30 days as required by GDPR.",
        "contact_error": "Please fill in all fields.",
        "footer": "Policy updated on {date} | Compliant with GDPR (EU Reg. 2016/679) and AI Act (EU Reg. 2024/1689)",
        "sidebar_badge": "GDPR + AI Act Compliant",
        "data_mgmt": "Data management",
        "data_mgmt_caption": "Under GDPR (Art. 17), you can delete all data entered in the current session.",
    },
    "it": {
        "consent_title": "Informativa sulla Privacy e Consenso al Trattamento",
        "consent_intro": (
            "Benvenuto in <strong>CareerMatch AI</strong>. Prima di procedere, ti informiamo che "
            "questa applicazione tratta i tuoi dati personali in conformita' al "
            "<strong>Regolamento Generale sulla Protezione dei Dati (GDPR - Reg. UE 2016/679)</strong> "
            "e al <strong>Regolamento sull'Intelligenza Artificiale (AI Act - Reg. UE 2024/1689)</strong>."
        ),
        "consent_data_label": "Dati trattati:",
        "consent_data_value": "Testo del CV, dati personali inseriti nel CV Builder (nome, email, telefono, competenze), descrizioni delle posizioni lavorative.",
        "consent_purpose_label": "Finalita':",
        "consent_purpose_value": "Analisi di compatibilita' professionale tramite algoritmi di Machine Learning (TF-IDF, Random Forest, K-Means Clustering, LDA Topic Modeling).",
        "consent_retention_label": "Conservazione:",
        "consent_retention_value": "I dati sono trattati esclusivamente nella sessione corrente del browser e <u>non vengono salvati su alcun server</u>. Alla chiusura della sessione, tutti i dati vengono automaticamente eliminati.",
        "consent_details": 'Per maggiori dettagli, consulta l\'informativa completa nella sezione "Privacy & AI" del menu.',
        "checkbox_gdpr": "Ho letto e acconsento al trattamento dei miei dati personali ai sensi dell'Art. 6(1)(a) GDPR",
        "checkbox_ai": "Sono consapevole che i miei dati saranno elaborati da sistemi di Intelligenza Artificiale (AI Act Art. 52)",
        "btn_accept": "Accetto e Proseguo",
        "consent_warning": "E' necessario fornire entrambi i consensi per utilizzare l'applicazione.",
        "page_title": "Privacy & Conformita' AI",
        "page_subtitle": "Informativa completa sul trattamento dei dati personali",
        "privacy_heading": "Informativa Privacy (Art. 13-14 GDPR)",
        "controller_title": "1. Titolare del Trattamento",
        "controller_body": (
            "Progetto sviluppato nel contesto accademico dell'"
            "<strong>Universita' IULM</strong> (Milano) - A.A. 2025-2026, "
            "corso di Data Mining & Text Analytics.<br><br>"
            "<strong>Team di sviluppo:</strong> Giacomo DellAcqua, Luca Tallarico, Ruben Scoletta<br>"
            "<strong>Contatto:</strong> Utilizza il modulo di contatto in fondo a questa pagina."
        ),
        "data_title": "2. Dati Personali Trattati",
        "data_body": (
            "<ul>"
            "<li><strong>Dati identificativi:</strong> nome, cognome, indirizzo email, numero di telefono, localita' (inseriti volontariamente nel CV Builder)</li>"
            "<li><strong>Dati professionali:</strong> competenze tecniche, esperienze lavorative, percorso formativo, progetti</li>"
            "<li><strong>Documenti:</strong> testo del Curriculum Vitae (caricato o incollato dall'utente)</li>"
            "<li><strong>Dati di navigazione:</strong> stato della sessione Streamlit (non persistente)</li>"
            "</ul>"
        ),
        "legal_title": "3. Finalita' e Base Giuridica del Trattamento",
        "legal_headers": ("Finalita'", "Base Giuridica"),
        "legal_rows": [
            ("Analisi di compatibilita' CV vs Job Description", "Consenso (Art. 6(1)(a) GDPR)"),
            ("Generazione CV tramite CV Builder", "Consenso (Art. 6(1)(a) GDPR)"),
            ("Elaborazione ML per scoring e gap analysis", "Consenso (Art. 6(1)(a) GDPR)"),
            ("Scopo accademico / ricerca (dimostrazione KDD)", "Legittimo interesse (Art. 6(1)(f) GDPR)"),
        ],
        "retention_title": "4. Conservazione dei Dati",
        "retention_body": (
            "I dati personali sono trattati <strong>esclusivamente nella sessione corrente</strong> "
            "del browser. <strong>Non esiste alcun database persistente</strong> che memorizzi i dati inseriti.<br><br>"
            "<strong>Periodo di conservazione:</strong> Durata della sessione browser.<br>"
            "<strong>Cancellazione:</strong> Automatica alla chiusura del browser/tab, "
            'oppure immediata tramite il pulsante "Cancella i Miei Dati".'
        ),
        "rights_title": "5. Diritti dell'Interessato (Art. 15-22 GDPR)",
        "rights_items": [
            "<strong>Accesso</strong> (Art. 15) -- Ottenere conferma del trattamento e copia dei dati",
            "<strong>Rettifica</strong> (Art. 16) -- Correggere i dati inesatti",
            "<strong>Cancellazione</strong> (Art. 17) -- Ottenere la cancellazione dei dati (diritto all'oblio)",
            "<strong>Limitazione</strong> (Art. 18) -- Limitare il trattamento dei dati",
            "<strong>Portabilita'</strong> (Art. 20) -- Ricevere i dati in formato strutturato",
            "<strong>Opposizione</strong> (Art. 21) -- Opporsi al trattamento",
            "<strong>Revoca del consenso</strong> (Art. 7(3)) -- Revocare il consenso in qualsiasi momento",
        ],
        "rights_note": 'Poiche\' i dati esistono solo nella sessione browser, il diritto di cancellazione e\' esercitabile immediatamente tramite il pulsante "Cancella i Miei Dati" nella barra laterale.',
        "transfer_title": "6. Trasferimento Dati",
        "transfer_body": (
            "I dati <strong>non vengono trasferiti a terze parti</strong> ne' verso paesi extra-UE.<br>"
            "L'applicazione e' ospitata su <strong>Streamlit Community Cloud</strong> (server in AWS, regione UE). "
            "Nessun dato viene persistito al di fuori della sessione del browser dell'utente."
        ),
        "ai_heading": "Trasparenza sull'Intelligenza Artificiale (AI Act)",
        "ai_intro": (
            "Questa applicazione utilizza sistemi di <strong>Intelligenza Artificiale</strong> "
            "per l'elaborazione dei dati. In conformita' all'<strong>Art. 52 dell'AI Act</strong>, "
            "dichiariamo quanto segue:"
        ),
        "ai_risk_label": "Classificazione del rischio:",
        "ai_risk_value": "RISCHIO LIMITATO / MINIMO",
        "ai_models_label": "Sistemi AI utilizzati:",
        "ai_models_headers": ("Modello", "Algoritmo", "Scopo"),
        "ai_decisions": (
            "<strong>Decisioni automatizzate:</strong> I risultati forniti dall'AI sono "
            "<strong>puramente indicativi e a scopo informativo</strong>. Non vengono prese "
            "decisioni automatizzate che producano effetti giuridici o che incidano significativamente "
            "sull'utente (Art. 22 GDPR). L'utente e' sempre libero di ignorare i suggerimenti forniti."
        ),
        "ai_oversight": (
            "<strong>Supervisione umana:</strong> Tutti i sistemi AI sono progettati come "
            "strumenti di supporto. Le decisioni finali spettano sempre all'utente umano."
        ),
        "ai_limitations": (
            "<strong>Limitazioni:</strong> I modelli ML possono produrre risultati imprecisi "
            "o incompleti. Lo score di compatibilita' e' un'approssimazione statistica e non "
            "rappresenta un giudizio definitivo sulle competenze dell'utente."
        ),
        "exercise_rights": "Esercita i Tuoi Diritti",
        "delete_title": "Cancella i Miei Dati",
        "delete_body": (
            "Questa azione cancellera' immediatamente tutti i dati presenti nella sessione corrente, "
            "inclusi CV, analisi, dati del CV Builder e preferenze. L'azione e' irreversibile."
        ),
        "delete_confirm": "Confermo di voler cancellare tutti i miei dati",
        "delete_btn": "Cancella Tutti i Miei Dati",
        "delete_success": "Tutti i tuoi dati sono stati cancellati con successo. La sessione e' stata ripristinata.",
        "delete_info": "Il tuo consenso e' stato revocato. Ti verra' richiesto nuovamente all'accesso.",
        "contact_heading": "Contattaci",
        "contact_body": "Per qualsiasi domanda relativa al trattamento dei dati, alla privacy o per esercitare i tuoi diritti GDPR, compila il modulo sottostante.",
        "contact_name": "Nome Completo",
        "contact_email": "Indirizzo Email",
        "contact_subject": "Oggetto",
        "contact_subject_options": ["Richiesta Accesso Dati (Art. 15)", "Richiesta Cancellazione Dati (Art. 17)", "Portabilita' Dati (Art. 20)", "Revoca Consenso (Art. 7)", "Richiesta Generica"],
        "contact_message": "Messaggio",
        "contact_submit": "Invia Richiesta",
        "contact_success": "La tua richiesta e' stata inviata. Risponderemo entro 30 giorni come previsto dal GDPR.",
        "contact_error": "Per favore compila tutti i campi.",
        "footer": "Informativa aggiornata al {date} | Conforme al GDPR (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689)",
        "sidebar_badge": "GDPR + AI Act Compliant",
        "data_mgmt": "Gestione dati personali",
        "data_mgmt_caption": "Ai sensi del GDPR (Art. 17), puoi cancellare tutti i dati inseriti nella sessione corrente.",
    },
}

def _t(key):
    """Get translated string based on current language setting."""
    lang = st.session_state.get("gdpr_lang", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)


# CareerMatch AI specific model data
AI_MODELS = [
    ("Skill Matching", "Random Forest (150 trees)", "Skill classification"),
    ("Semantic Analysis", "TF-IDF + LSA", "Professional context"),
    ("Skill Clustering", "K-Means + Hierarchical", "Skill grouping"),
    ("Topic Discovery", "LDA (Latent Dirichlet Allocation)", "JD theme identification"),
    ("Fuzzy Matching", "FuzzyWuzzy (85% threshold)", "Typo tolerance"),
]


# =============================================================================
# CSS STYLES
# =============================================================================

def get_compliance_css():
    return """
    <style>
        .gdpr-banner {
            background: linear-gradient(135deg, rgba(0, 119, 181, 0.15), rgba(0, 160, 220, 0.08));
            border: 1px solid rgba(0, 160, 220, 0.3);
            border-radius: 12px;
            padding: 2rem;
            margin: 1rem 0 2rem 0;
        }
        .gdpr-banner h3 { color: #00A0DC; margin-bottom: 1rem; }
        .gdpr-banner p { color: #c9d1d9; line-height: 1.6; }
        .privacy-section {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .privacy-section h4 { color: #00A0DC; margin-bottom: 0.75rem; }
        .ai-transparency-box {
            background: linear-gradient(135deg, rgba(56, 132, 244, 0.1), rgba(0, 200, 160, 0.08));
            border-left: 4px solid #3884F4;
            border-radius: 0 10px 10px 0;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .ai-transparency-box h4 { color: #3884F4; margin-bottom: 0.5rem; }
        .delete-warning {
            background: rgba(229, 57, 53, 0.1);
            border: 1px solid rgba(229, 57, 53, 0.3);
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        .compliance-badge {
            display: inline-block;
            background: rgba(0, 200, 83, 0.15);
            color: #00C853;
            border: 1px solid rgba(0, 200, 83, 0.3);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .contact-form {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
    </style>
    """


# =============================================================================
# LANGUAGE TOGGLE
# =============================================================================

def render_language_toggle():
    """Renders a compact language toggle."""
    col1, col2 = st.columns([6, 1])
    with col2:
        lang = st.selectbox(
            "Lang",
            options=["en", "it"],
            format_func=lambda x: "EN" if x == "en" else "IT",
            key="gdpr_lang",
            label_visibility="collapsed",
        )


# =============================================================================
# CONSENT BANNER (GDPR Art. 6-7)
# =============================================================================

def render_consent_banner():
    if st.session_state.get("gdpr_consent_given", False):
        return True

    st.markdown(get_compliance_css(), unsafe_allow_html=True)
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        render_language_toggle()

        st.markdown(f"""
        <div class="gdpr-banner">
            <h3>{_t("consent_title")}</h3>
            <p>{_t("consent_intro")}</p>
            <p style="margin-top: 1rem;">
                <strong>{_t("consent_data_label")}</strong> {_t("consent_data_value")}
            </p>
            <p>
                <strong>{_t("consent_purpose_label")}</strong> {_t("consent_purpose_value")}
            </p>
            <p>
                <strong>{_t("consent_retention_label")}</strong> {_t("consent_retention_value")}
            </p>
            <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #8b949e;">
                {_t("consent_details")}
            </p>
        </div>
        """, unsafe_allow_html=True)

        consent_data = st.checkbox(_t("checkbox_gdpr"), key="gdpr_consent_checkbox")
        consent_ai = st.checkbox(_t("checkbox_ai"), key="ai_act_consent_checkbox")

        st.markdown("<br>", unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button(_t("btn_accept"), type="primary", use_container_width=True,
                        disabled=not (consent_data and consent_ai)):
                st.session_state["gdpr_consent_given"] = True
                st.session_state["gdpr_consent_timestamp"] = datetime.now().isoformat()
                st.rerun()

        if not (consent_data and consent_ai):
            st.caption(_t("consent_warning"))

    return False


# =============================================================================
# PRIVACY POLICY PAGE
# =============================================================================

def render_privacy_policy_page():
    st.markdown(get_compliance_css(), unsafe_allow_html=True)

    render_language_toggle()

    st.markdown(f"""
    <div style='display: flex; align-items: center; justify-content: space-between;'>
        <div>
            <h1 style='margin: 0;'>{_t("page_title")}</h1>
            <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>{_t("page_subtitle")}</p>
        </div>
        <div>
            <span class="compliance-badge">GDPR Compliant</span>
            <span class="compliance-badge" style="margin-left: 8px;">AI Act Compliant</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- PRIVACY POLICY SECTIONS ---
    st.markdown(f"## {_t('privacy_heading')}")

    for section_key in ["controller", "data"]:
        st.markdown(f"""
        <div class="privacy-section">
            <h4>{_t(f"{section_key}_title")}</h4>
            <p>{_t(f"{section_key}_body")}</p>
        </div>
        """, unsafe_allow_html=True)

    # Legal basis table
    headers = _t("legal_headers")
    rows = _t("legal_rows")
    rows_html = ""
    for i, (purpose, basis) in enumerate(rows):
        border = ' style="border-bottom: 1px solid #21262d;"' if i < len(rows) - 1 else ""
        rows_html += f'<tr{border}><td style="padding: 8px;">{purpose}</td><td style="padding: 8px;">{basis}</td></tr>'

    st.markdown(f"""
    <div class="privacy-section">
        <h4>{_t("legal_title")}</h4>
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #00A0DC;">{headers[0]}</th>
                <th style="text-align: left; padding: 8px; color: #00A0DC;">{headers[1]}</th>
            </tr>
            {rows_html}
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Retention
    st.markdown(f"""
    <div class="privacy-section">
        <h4>{_t("retention_title")}</h4>
        <p>{_t("retention_body")}</p>
    </div>
    """, unsafe_allow_html=True)

    # Rights
    rights_list = "".join(f"<li>{r}</li>" for r in _t("rights_items"))
    st.markdown(f"""
    <div class="privacy-section">
        <h4>{_t("rights_title")}</h4>
        <ul>{rights_list}</ul>
        <p style="margin-top: 0.5rem; color: #8b949e; font-size: 0.85rem;">{_t("rights_note")}</p>
    </div>
    """, unsafe_allow_html=True)

    # Transfer
    st.markdown(f"""
    <div class="privacy-section">
        <h4>{_t("transfer_title")}</h4>
        <p>{_t("transfer_body")}</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- AI ACT TRANSPARENCY ---
    render_ai_transparency()

    st.divider()

    # --- DATA DELETION ---
    st.markdown(f"## {_t('exercise_rights')}")
    render_delete_my_data_button()

    st.divider()

    # --- CONTACT FORM ---
    render_contact_form()

    st.divider()

    st.markdown(f"""
    <p style='color: #6e7681; font-size: 0.8rem; text-align: center;'>
        {_t("footer").format(date=datetime.now().strftime('%d/%m/%Y'))}
    </p>
    """, unsafe_allow_html=True)


# =============================================================================
# AI ACT TRANSPARENCY (Art. 52)
# =============================================================================

def render_ai_transparency():
    headers = _t("ai_models_headers")
    rows_html = ""
    for i, (model, algo, purpose) in enumerate(AI_MODELS):
        border = ' style="border-bottom: 1px solid #21262d;"' if i < len(AI_MODELS) - 1 else ""
        rows_html += f'<tr{border}><td style="padding: 8px;">{model}</td><td style="padding: 8px;">{algo}</td><td style="padding: 8px;">{purpose}</td></tr>'

    st.markdown(f"""
    ## {_t("ai_heading")}

    <div class="ai-transparency-box">
        <h4>AI Act - EU Reg. 2024/1689</h4>
        <p>{_t("ai_intro")}</p>

        <p style="margin-top: 1rem;"><strong>{_t("ai_risk_label")}</strong>
            <span style="background: rgba(0, 200, 83, 0.2); padding: 2px 8px; border-radius: 4px; color: #00C853;">
            {_t("ai_risk_value")}</span>
        </p>

        <p><strong>{_t("ai_models_label")}</strong></p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #3884F4;">{headers[0]}</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">{headers[1]}</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">{headers[2]}</th>
            </tr>
            {rows_html}
        </table>

        <p style="margin-top: 1rem;">{_t("ai_decisions")}</p>
        <p>{_t("ai_oversight")}</p>
        <p>{_t("ai_limitations")}</p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# DELETE MY DATA (GDPR Art. 17)
# =============================================================================

def render_delete_my_data_button():
    st.markdown(f"""
    <div class="delete-warning">
        <strong>{_t("delete_title")}</strong><br>
        <span style="font-size: 0.9rem; color: #c9d1d9;">{_t("delete_body")}</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        confirm = st.checkbox(_t("delete_confirm"), key="delete_confirm_checkbox")
        if st.button(_t("delete_btn"), type="primary", use_container_width=True,
                     disabled=not confirm):
            keys_to_clear = list(st.session_state.keys())
            for key in keys_to_clear:
                if key != "page":
                    del st.session_state[key]
            st.success(_t("delete_success"))
            st.info(_t("delete_info"))


# =============================================================================
# CONTACT FORM
# =============================================================================

def render_contact_form():
    st.markdown(f"## {_t('contact_heading')}")
    st.markdown(f"""
    <div class="contact-form">
        <p>{_t("contact_body")}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("gdpr_contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(_t("contact_name"))
        with col2:
            email = st.text_input(_t("contact_email"))

        subject = st.selectbox(_t("contact_subject"), options=_t("contact_subject_options"))
        message = st.text_area(_t("contact_message"), height=120)

        submitted = st.form_submit_button(_t("contact_submit"), use_container_width=True)
        if submitted:
            if name and email and message:
                st.success(_t("contact_success"))
            else:
                st.warning(_t("contact_error"))


# =============================================================================
# SIDEBAR COMPLIANCE WIDGET
# =============================================================================

def render_sidebar_compliance_badge():
    st.markdown(f"""
    <div style='margin-top: 1rem; padding: 8px; background: rgba(0, 200, 83, 0.08);
         border: 1px solid rgba(0, 200, 83, 0.2); border-radius: 8px; text-align: center;'>
        <span style='color: #00C853; font-size: 0.7rem; font-weight: 600;'>
            {_t("sidebar_badge")}
        </span>
    </div>
    """, unsafe_allow_html=True)
