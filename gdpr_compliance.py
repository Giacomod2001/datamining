"""
================================================================================
GDPR & AI Act Compliance Module - CareerMatch AI
================================================================================

Compliance with:
- GDPR (EU Reg. 2016/679)
- EU AI Act (EU Reg. 2024/1689)
- ePrivacy Directive (2002/58/EC)

Public entry points used by app.py:
- render_consent_banner()        -> bool  (consent gate)
- render_sidebar_compliance_badge()       (sidebar widget)
- render_privacy_policy_page()            (full policy page)

Features:
- 6-language support (EN, IT, ES, FR, DE, PT) -- aligned with Ruben assistant
- Consent banner with timestamp logging (accountability, Art. 7 GDPR)
- Full Privacy Policy with Data Processors (Art. 28) and DPIA summary (Art. 35)
- AI Act transparency disclosure (Art. 50-52)
- Right to erasure (Art. 17) -- one-click data wipe
- Working contact form (mailto deeplink + GitHub Issues + JSON export)
================================================================================
"""

from __future__ import annotations

import hashlib
import json
import urllib.parse
from datetime import datetime, timezone

import streamlit as st


# =============================================================================
# CONFIG
# =============================================================================

CONTACT_EMAIL = "dellacquagiacomo@gmail.com"
GITHUB_ISSUES_URL = "https://github.com/Giacomod2001/datamining/issues/new"
POLICY_VERSION = "3.3"
POLICY_DATE = "2026-06-07"

SUPPORTED_LANGUAGES = [
    ("en", "EN"),
    ("it", "IT"),
    ("es", "ES"),
    ("fr", "FR"),
    ("de", "DE"),
    ("pt", "PT"),
]

# AI systems disclosed under AI Act Art. 50/52.
# Tuple: (component_name, algorithm, purpose, provider/location)
AI_MODELS = [
    ("Skill Matching",      "Random Forest (150 trees)",          "Skill classification",        "scikit-learn / local"),
    ("Semantic Analysis",   "TF-IDF + LSA",                       "Professional context",        "scikit-learn / local"),
    ("Skill Clustering",    "K-Means + Hierarchical",             "Skill grouping",              "scikit-learn / local"),
    ("Topic Discovery",     "LDA (Latent Dirichlet Allocation)",  "JD theme identification",     "scikit-learn / local"),
    ("Fuzzy Matching",      "TheFuzz (Levenshtein, threshold 85)","Typo tolerance",              "TheFuzz / local"),
    ("Career Assistant",    "Rule-based intent matching",          "Guidance & navigation",       "Local (no LLM, no external API)"),
]


# =============================================================================
# TRANSLATIONS - 6 LANGUAGES
# =============================================================================
# Note: kept compact; full HTML inside strings is intentional (rendered via
# st.markdown(..., unsafe_allow_html=True)).

TRANSLATIONS: dict[str, dict] = {
    # -------------------------------------------------------------------------
    # ENGLISH
    # -------------------------------------------------------------------------
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
        "consent_purpose_value": "Professional compatibility analysis via classic Machine Learning algorithms (TF-IDF, Random Forest, K-Means, LDA) -- no external LLM provider is contacted.",
        "consent_retention_label": "Data retention:",
        "consent_retention_value": "Data is processed exclusively within the current browser session and <u>is not stored on any server</u>. When the session ends, all data is automatically deleted.",
        "consent_details": 'For more details, see the full privacy policy in the "Privacy & AI" section of the menu.',
        "checkbox_gdpr": "I have read and consent to the processing of my personal data pursuant to Art. 6(1)(a) GDPR",
        "checkbox_ai": "I am aware that my data will be processed by AI systems running locally (AI Act Art. 50)",
        "btn_accept": "Accept and Continue",
        "btn_decline": "Decline and Exit",
        "consent_warning": "Both consents are required to use the application.",
        "consent_declined_title": "Consent not provided",
        "consent_declined_body": "Without GDPR and AI Act consents the application cannot operate. You may close this tab.",
        "page_title": "Privacy & AI Compliance",
        "page_subtitle": "Full privacy policy and data processing information",
        "privacy_heading": "Privacy Policy (Art. 13-14 GDPR)",
        "controller_title": "1. Data Controller",
        "controller_body": (
            "This project is developed in the academic context of "
            "<strong>IULM University</strong> (Milan) -- A.Y. 2025-2026, "
            "Data Mining & Text Analytics course (Prof. Alessandro Bruno).<br><br>"
            "<strong>Development team:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Contact:</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a> "
            "(joint contact point for the development team)"
        ),
        "data_title": "2. Personal Data Processed",
        "data_body": (
            "<ul>"
            "<li><strong>Identity data:</strong> name, surname, email, phone number, location (voluntarily entered in CV Builder)</li>"
            "<li><strong>Professional data:</strong> technical skills, work experience, education, projects</li>"
            "<li><strong>Documents:</strong> Curriculum Vitae text (uploaded or pasted)</li>"
            "<li><strong>Session data:</strong> Streamlit session state (non-persistent), consent timestamp (hashed)</li>"
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
            "<strong>Lodge a complaint</strong> (Art. 77) -- File a complaint with the supervisory authority (Garante per la protezione dei dati personali, www.garanteprivacy.it)",
        ],
        "rights_note": 'Since data exists only in the browser session, the right to erasure can be exercised immediately via the "Delete My Data" button in the sidebar.',
        "processors_title": "6. Data Processors (Art. 28 GDPR)",
        "processors_body": (
            "<p>The application is hosted on a third-party infrastructure that acts as a "
            "<strong>data processor</strong>:</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- application hosting, AWS EU region. "
            "Adequacy decision / SCCs apply for any incidental US transfer.</li>"
            "<li><strong>GitHub Inc.</strong> -- source code hosting only (no user data). Subject to "
            "EU-US Data Privacy Framework.</li>"
            "</ul>"
            "<p>No external LLM provider (OpenAI, Anthropic, Google, etc.) is contacted: all ML processing "
            "happens in-process within the hosting environment.</p>"
        ),
        "transfer_title": "7. International Data Transfers",
        "transfer_body": (
            "Data is <strong>not transferred</strong> outside the user's browser session.<br>"
            "The hosting provider (Streamlit Community Cloud) runs on AWS infrastructure in the EU region. "
            "Should incidental transfers occur for operational purposes, they rely on adequacy decisions "
            "(EU-US DPF) and Standard Contractual Clauses (SCCs)."
        ),
        "dpia_title": "8. DPIA Summary (Art. 35 GDPR)",
        "dpia_body": (
            "<p>A simplified Data Protection Impact Assessment has been conducted given the "
            "use of AI systems on personal data:</p>"
            "<ul>"
            "<li><strong>Risk classification:</strong> Low. No special categories of data are processed; "
            "no profiling with legal effects; no large-scale monitoring.</li>"
            "<li><strong>Mitigations:</strong> session-only retention, no persistent database, no third-party LLM, "
            "human oversight on all outputs, transparent scoring rationale via Dev Console.</li>"
            "<li><strong>Residual risk:</strong> incorrect skill inference -- mitigated by explicit user review "
            "and the disclaimer that scores are indicative.</li>"
            "</ul>"
        ),
        "ai_heading": "AI Transparency (AI Act)",
        "ai_intro": (
            "This application uses <strong>Artificial Intelligence</strong> systems "
            "for data processing. In compliance with <strong>Art. 50-52 of the AI Act</strong>, "
            "we declare the following:"
        ),
        "ai_risk_label": "Risk classification:",
        "ai_risk_value": "LIMITED / MINIMAL RISK",
        "ai_models_label": "AI systems used:",
        "ai_models_headers": ("Component", "Algorithm", "Purpose", "Provider / Location"),
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
        "ai_no_llm": (
            "<strong>No external LLM:</strong> This application does <u>not</u> send your data to OpenAI, "
            "Anthropic, Google or any other LLM provider. All AI runs locally on the hosting server."
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
        "contact_body": "For any questions regarding data processing, privacy, or to exercise your GDPR rights, use one of the channels below.",
        "contact_name": "Full Name",
        "contact_email": "Email Address",
        "contact_subject": "Subject",
        "contact_subject_options": ["Data Access Request (Art. 15)", "Data Deletion Request (Art. 17)", "Data Portability (Art. 20)", "Consent Withdrawal (Art. 7)", "General Inquiry"],
        "contact_message": "Message",
        "contact_submit_email": "Open in Email Client",
        "contact_submit_github": "Open a GitHub Issue",
        "contact_download_json": "Download Request as JSON",
        "contact_success": "Your request has been prepared. Use one of the buttons above to submit it. We will respond within 30 days as required by GDPR.",
        "contact_error": "Please fill in all fields before generating the request.",
        "footer": "Policy v{version} updated on {date} | Compliant with GDPR (EU Reg. 2016/679) and AI Act (EU Reg. 2024/1689)",
        "sidebar_badge": "GDPR + AI Act Compliant",
        "data_mgmt": "Data management",
        "data_mgmt_caption": "Under GDPR (Art. 17), you can delete all data entered in the current session.",
        "consent_record_title": "Your consent record",
        "consent_record_caption": "Stored locally for accountability (Art. 7 GDPR). Not transmitted anywhere.",
    },

    # -------------------------------------------------------------------------
    # ITALIAN
    # -------------------------------------------------------------------------
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
        "consent_purpose_value": "Analisi di compatibilita' professionale tramite algoritmi classici di Machine Learning (TF-IDF, Random Forest, K-Means, LDA) -- nessun provider LLM esterno viene contattato.",
        "consent_retention_label": "Conservazione:",
        "consent_retention_value": "I dati sono trattati esclusivamente nella sessione corrente del browser e <u>non vengono salvati su alcun server</u>. Alla chiusura della sessione, tutti i dati vengono automaticamente eliminati.",
        "consent_details": 'Per maggiori dettagli, consulta l\'informativa completa nella sezione "Privacy & AI" del menu.',
        "checkbox_gdpr": "Ho letto e acconsento al trattamento dei miei dati personali ai sensi dell'Art. 6(1)(a) GDPR",
        "checkbox_ai": "Sono consapevole che i miei dati saranno elaborati da sistemi di Intelligenza Artificiale eseguiti localmente (AI Act Art. 50)",
        "btn_accept": "Accetto e Proseguo",
        "btn_decline": "Rifiuto ed Esco",
        "consent_warning": "E' necessario fornire entrambi i consensi per utilizzare l'applicazione.",
        "consent_declined_title": "Consenso non fornito",
        "consent_declined_body": "Senza i consensi GDPR e AI Act l'applicazione non puo' essere utilizzata. Puoi chiudere questa scheda.",
        "page_title": "Privacy & Conformita' AI",
        "page_subtitle": "Informativa completa sul trattamento dei dati personali",
        "privacy_heading": "Informativa Privacy (Art. 13-14 GDPR)",
        "controller_title": "1. Titolare del Trattamento",
        "controller_body": (
            "Progetto sviluppato nel contesto accademico dell'"
            "<strong>Universita' IULM</strong> (Milano) -- A.A. 2025-2026, "
            "corso di Data Mining & Text Analytics (Prof. Alessandro Bruno).<br><br>"
            "<strong>Team di sviluppo:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Contatto:</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a> "
            "(punto di contatto del team)"
        ),
        "data_title": "2. Dati Personali Trattati",
        "data_body": (
            "<ul>"
            "<li><strong>Dati identificativi:</strong> nome, cognome, indirizzo email, numero di telefono, localita' (inseriti volontariamente nel CV Builder)</li>"
            "<li><strong>Dati professionali:</strong> competenze tecniche, esperienze lavorative, percorso formativo, progetti</li>"
            "<li><strong>Documenti:</strong> testo del Curriculum Vitae (caricato o incollato dall'utente)</li>"
            "<li><strong>Dati di sessione:</strong> stato della sessione Streamlit (non persistente), timestamp del consenso (in hash)</li>"
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
            "<strong>Reclamo</strong> (Art. 77) -- Presentare reclamo all'autorita' di controllo (Garante per la protezione dei dati personali, www.garanteprivacy.it)",
        ],
        "rights_note": 'Poiche\' i dati esistono solo nella sessione browser, il diritto di cancellazione e\' esercitabile immediatamente tramite il pulsante "Cancella i Miei Dati" nella barra laterale.',
        "processors_title": "6. Responsabili del Trattamento (Art. 28 GDPR)",
        "processors_body": (
            "<p>L'applicazione e' ospitata su infrastruttura di terzi che agisce come "
            "<strong>responsabile del trattamento</strong>:</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- hosting applicativo, regione AWS UE. "
            "Trasferimenti accidentali coperti da decisione di adeguatezza / SCC.</li>"
            "<li><strong>GitHub Inc.</strong> -- solo hosting del codice sorgente (nessun dato utente). "
            "Soggetto al Framework EU-US Data Privacy.</li>"
            "</ul>"
            "<p>Nessun provider LLM esterno (OpenAI, Anthropic, Google, ecc.) viene contattato: "
            "tutta l'elaborazione ML avviene in-process nell'ambiente di hosting.</p>"
        ),
        "transfer_title": "7. Trasferimento Dati Internazionale",
        "transfer_body": (
            "I dati <strong>non vengono trasferiti</strong> al di fuori della sessione browser dell'utente.<br>"
            "L'hosting provider (Streamlit Community Cloud) opera su infrastruttura AWS in regione UE. "
            "Eventuali trasferimenti accidentali si basano su decisioni di adeguatezza (EU-US DPF) e "
            "Standard Contractual Clauses (SCC)."
        ),
        "dpia_title": "8. Sintesi DPIA (Art. 35 GDPR)",
        "dpia_body": (
            "<p>E' stata effettuata una valutazione d'impatto semplificata data la "
            "presenza di sistemi AI che trattano dati personali:</p>"
            "<ul>"
            "<li><strong>Classificazione del rischio:</strong> Basso. Nessuna categoria particolare di dati; "
            "nessuna profilazione con effetti giuridici; nessun monitoraggio su larga scala.</li>"
            "<li><strong>Misure di mitigazione:</strong> conservazione solo a sessione, nessun database persistente, "
            "nessun LLM di terzi, supervisione umana su tutti gli output, spiegabilita' dello score via Dev Console.</li>"
            "<li><strong>Rischio residuo:</strong> inferenza errata delle skill -- mitigato dalla revisione esplicita "
            "dell'utente e dal disclaimer di indicativita' dello score.</li>"
            "</ul>"
        ),
        "ai_heading": "Trasparenza sull'Intelligenza Artificiale (AI Act)",
        "ai_intro": (
            "Questa applicazione utilizza sistemi di <strong>Intelligenza Artificiale</strong> "
            "per l'elaborazione dei dati. In conformita' agli <strong>Artt. 50-52 dell'AI Act</strong>, "
            "dichiariamo quanto segue:"
        ),
        "ai_risk_label": "Classificazione del rischio:",
        "ai_risk_value": "RISCHIO LIMITATO / MINIMO",
        "ai_models_label": "Sistemi AI utilizzati:",
        "ai_models_headers": ("Componente", "Algoritmo", "Scopo", "Provider / Sede"),
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
        "ai_no_llm": (
            "<strong>Nessun LLM esterno:</strong> Questa applicazione <u>non</u> invia i tuoi dati a OpenAI, "
            "Anthropic, Google o altri provider di LLM. Tutta l'AI viene eseguita localmente sul server di hosting."
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
        "contact_body": "Per qualsiasi domanda relativa al trattamento dei dati, alla privacy o per esercitare i tuoi diritti GDPR, utilizza uno dei canali sottostanti.",
        "contact_name": "Nome Completo",
        "contact_email": "Indirizzo Email",
        "contact_subject": "Oggetto",
        "contact_subject_options": ["Richiesta Accesso Dati (Art. 15)", "Richiesta Cancellazione Dati (Art. 17)", "Portabilita' Dati (Art. 20)", "Revoca Consenso (Art. 7)", "Richiesta Generica"],
        "contact_message": "Messaggio",
        "contact_submit_email": "Apri nel Client Email",
        "contact_submit_github": "Apri una GitHub Issue",
        "contact_download_json": "Scarica la Richiesta in JSON",
        "contact_success": "La tua richiesta e' pronta. Usa uno dei pulsanti qui sopra per inviarla. Risponderemo entro 30 giorni come previsto dal GDPR.",
        "contact_error": "Per favore compila tutti i campi prima di generare la richiesta.",
        "footer": "Informativa v{version} aggiornata al {date} | Conforme al GDPR (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689)",
        "sidebar_badge": "GDPR + AI Act Conforme",
        "data_mgmt": "Gestione dati personali",
        "data_mgmt_caption": "Ai sensi del GDPR (Art. 17), puoi cancellare tutti i dati inseriti nella sessione corrente.",
        "consent_record_title": "Registrazione del tuo consenso",
        "consent_record_caption": "Conservata localmente per accountability (Art. 7 GDPR). Non trasmessa altrove.",
    },

    # -------------------------------------------------------------------------
    # SPANISH
    # -------------------------------------------------------------------------
    "es": {
        "consent_title": "Aviso de Privacidad y Consentimiento de Tratamiento",
        "consent_intro": (
            "Bienvenido a <strong>CareerMatch AI</strong>. Antes de continuar, le informamos que "
            "esta aplicacion trata sus datos personales conforme al "
            "<strong>Reglamento General de Proteccion de Datos (RGPD - Reg. UE 2016/679)</strong> "
            "y a la <strong>Ley de Inteligencia Artificial (AI Act - Reg. UE 2024/1689)</strong>."
        ),
        "consent_data_label": "Datos tratados:",
        "consent_data_value": "Texto del CV, datos personales en el CV Builder (nombre, email, telefono, habilidades), descripciones de puestos.",
        "consent_purpose_label": "Finalidad:",
        "consent_purpose_value": "Analisis de compatibilidad profesional mediante algoritmos clasicos de Machine Learning (TF-IDF, Random Forest, K-Means, LDA) -- no se contacta ningun proveedor de LLM externo.",
        "consent_retention_label": "Conservacion:",
        "consent_retention_value": "Los datos se tratan exclusivamente en la sesion actual del navegador y <u>no se almacenan en ningun servidor</u>. Al finalizar la sesion, todos los datos se eliminan automaticamente.",
        "consent_details": 'Para mas detalles, consulta la politica completa en la seccion "Privacy & AI" del menu.',
        "checkbox_gdpr": "He leido y consiento el tratamiento de mis datos personales conforme al Art. 6(1)(a) RGPD",
        "checkbox_ai": "Soy consciente de que mis datos seran tratados por sistemas de IA ejecutados localmente (AI Act Art. 50)",
        "btn_accept": "Acepto y Continuo",
        "btn_decline": "Rechazo y Salgo",
        "consent_warning": "Ambos consentimientos son necesarios para usar la aplicacion.",
        "consent_declined_title": "Consentimiento no proporcionado",
        "consent_declined_body": "Sin los consentimientos RGPD y AI Act la aplicacion no puede funcionar. Puede cerrar esta pestana.",
        "page_title": "Privacidad y Conformidad IA",
        "page_subtitle": "Politica completa de tratamiento de datos personales",
        "privacy_heading": "Politica de Privacidad (Art. 13-14 RGPD)",
        "controller_title": "1. Responsable del Tratamiento",
        "controller_body": (
            "Proyecto desarrollado en el contexto academico de la "
            "<strong>Universidad IULM</strong> (Milan) -- A.A. 2025-2026, "
            "curso de Data Mining & Text Analytics (Prof. Alessandro Bruno).<br><br>"
            "<strong>Equipo de desarrollo:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Contacto:</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a>"
        ),
        "data_title": "2. Datos Personales Tratados",
        "data_body": (
            "<ul>"
            "<li><strong>Datos identificativos:</strong> nombre, apellido, email, telefono, ubicacion (introducidos voluntariamente en CV Builder)</li>"
            "<li><strong>Datos profesionales:</strong> habilidades tecnicas, experiencia, formacion, proyectos</li>"
            "<li><strong>Documentos:</strong> texto del Curriculum Vitae (subido o pegado)</li>"
            "<li><strong>Datos de sesion:</strong> estado de la sesion Streamlit (no persistente), timestamp de consentimiento (en hash)</li>"
            "</ul>"
        ),
        "legal_title": "3. Finalidad y Base Juridica",
        "legal_headers": ("Finalidad", "Base Juridica"),
        "legal_rows": [
            ("Analisis CV vs descripcion del puesto", "Consentimiento (Art. 6(1)(a) RGPD)"),
            ("Generacion de CV via CV Builder", "Consentimiento (Art. 6(1)(a) RGPD)"),
            ("Procesamiento ML para scoring y gap analysis", "Consentimiento (Art. 6(1)(a) RGPD)"),
            ("Finalidad academica / investigacion (demostracion KDD)", "Interes legitimo (Art. 6(1)(f) RGPD)"),
        ],
        "retention_title": "4. Conservacion de los Datos",
        "retention_body": (
            "Los datos se tratan <strong>exclusivamente en la sesion actual</strong> del navegador. "
            "<strong>Ninguna base de datos persistente</strong> almacena los datos introducidos.<br><br>"
            "<strong>Periodo de conservacion:</strong> Duracion de la sesion del navegador.<br>"
            'Eliminacion automatica al cerrar el navegador o inmediata via el boton "Eliminar mis datos".'
        ),
        "rights_title": "5. Derechos del Interesado (Art. 15-22 RGPD)",
        "rights_items": [
            "<strong>Acceso</strong> (Art. 15) -- Obtener confirmacion y copia de tus datos",
            "<strong>Rectificacion</strong> (Art. 16) -- Corregir datos inexactos",
            "<strong>Supresion</strong> (Art. 17) -- Derecho al olvido",
            "<strong>Limitacion</strong> (Art. 18) -- Limitar el tratamiento",
            "<strong>Portabilidad</strong> (Art. 20) -- Recibir los datos en formato estructurado",
            "<strong>Oposicion</strong> (Art. 21) -- Oponerse al tratamiento",
            "<strong>Retirada del consentimiento</strong> (Art. 7(3)) -- Retirar el consentimiento en cualquier momento",
            "<strong>Reclamacion</strong> (Art. 77) -- Presentar reclamacion ante la autoridad de control (AEPD, www.aepd.es)",
        ],
        "rights_note": 'Como los datos existen solo en la sesion del navegador, el derecho de supresion puede ejercerse inmediatamente via el boton "Eliminar mis datos" en la barra lateral.',
        "processors_title": "6. Encargados del Tratamiento (Art. 28 RGPD)",
        "processors_body": (
            "<p>La aplicacion se aloja en infraestructura de terceros que actua como "
            "<strong>encargado del tratamiento</strong>:</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- hosting de la app, region AWS UE.</li>"
            "<li><strong>GitHub Inc.</strong> -- solo hosting del codigo fuente (sin datos de usuario).</li>"
            "</ul>"
            "<p>No se contacta ningun proveedor externo de LLM: todo el procesamiento de IA ocurre localmente.</p>"
        ),
        "transfer_title": "7. Transferencias Internacionales",
        "transfer_body": (
            "Los datos <strong>no se transfieren</strong> fuera de la sesion del navegador.<br>"
            "El proveedor de hosting opera en AWS region UE. Eventuales transferencias incidentales se "
            "basan en decisiones de adecuacion (EU-US DPF) y Clausulas Contractuales Tipo (CCT)."
        ),
        "dpia_title": "8. Resumen DPIA (Art. 35 RGPD)",
        "dpia_body": (
            "<p>Se ha realizado una evaluacion de impacto simplificada dada la presencia de sistemas IA:</p>"
            "<ul>"
            "<li><strong>Riesgo:</strong> Bajo. Sin categorias especiales de datos; sin perfilado con efectos "
            "juridicos; sin monitorizacion a gran escala.</li>"
            "<li><strong>Mitigaciones:</strong> conservacion solo de sesion, sin BD persistente, sin LLM de terceros, "
            "supervision humana sobre todas las salidas, explicabilidad via Dev Console.</li>"
            "<li><strong>Riesgo residual:</strong> inferencia erronea de habilidades -- mitigada por la revision del usuario.</li>"
            "</ul>"
        ),
        "ai_heading": "Transparencia sobre Inteligencia Artificial (AI Act)",
        "ai_intro": (
            "Esta aplicacion utiliza sistemas de <strong>Inteligencia Artificial</strong> para procesar datos. "
            "Conforme a los <strong>Arts. 50-52 del AI Act</strong>, declaramos:"
        ),
        "ai_risk_label": "Clasificacion de riesgo:",
        "ai_risk_value": "RIESGO LIMITADO / MINIMO",
        "ai_models_label": "Sistemas IA utilizados:",
        "ai_models_headers": ("Componente", "Algoritmo", "Finalidad", "Proveedor / Ubicacion"),
        "ai_decisions": (
            "<strong>Decisiones automatizadas:</strong> Los resultados son <strong>puramente indicativos</strong>. "
            "No se toman decisiones automatizadas con efectos juridicos sobre el usuario (Art. 22 RGPD)."
        ),
        "ai_oversight": (
            "<strong>Supervision humana:</strong> Todos los sistemas IA son herramientas de apoyo. "
            "Las decisiones finales corresponden al usuario."
        ),
        "ai_limitations": (
            "<strong>Limitaciones:</strong> Los modelos ML pueden producir resultados imprecisos. "
            "El score de compatibilidad es una aproximacion estadistica."
        ),
        "ai_no_llm": (
            "<strong>Sin LLM externo:</strong> Esta aplicacion <u>no</u> envia tus datos a OpenAI, "
            "Anthropic, Google ni a otros proveedores de LLM."
        ),
        "exercise_rights": "Ejerce tus Derechos",
        "delete_title": "Eliminar mis Datos",
        "delete_body": (
            "Esta accion eliminara inmediatamente todos los datos de la sesion actual. Accion irreversible."
        ),
        "delete_confirm": "Confirmo que deseo eliminar todos mis datos",
        "delete_btn": "Eliminar Todos mis Datos",
        "delete_success": "Todos tus datos se eliminaron correctamente. La sesion se ha restablecido.",
        "delete_info": "Tu consentimiento fue revocado. Se solicitara nuevamente en el proximo acceso.",
        "contact_heading": "Contactanos",
        "contact_body": "Para cualquier pregunta sobre el tratamiento de datos o tus derechos RGPD, utiliza uno de los canales siguientes.",
        "contact_name": "Nombre Completo",
        "contact_email": "Email",
        "contact_subject": "Asunto",
        "contact_subject_options": ["Solicitud de Acceso (Art. 15)", "Solicitud de Supresion (Art. 17)", "Portabilidad (Art. 20)", "Retirada de Consentimiento (Art. 7)", "Consulta General"],
        "contact_message": "Mensaje",
        "contact_submit_email": "Abrir en el cliente de email",
        "contact_submit_github": "Abrir un GitHub Issue",
        "contact_download_json": "Descargar la solicitud en JSON",
        "contact_success": "Tu solicitud esta lista. Usa uno de los botones de arriba para enviarla. Responderemos en 30 dias como exige el RGPD.",
        "contact_error": "Por favor, completa todos los campos antes de generar la solicitud.",
        "footer": "Politica v{version} actualizada el {date} | Conforme con RGPD (Reg. UE 2016/679) y AI Act (Reg. UE 2024/1689)",
        "sidebar_badge": "RGPD + AI Act Conforme",
        "data_mgmt": "Gestion de datos personales",
        "data_mgmt_caption": "Segun el RGPD (Art. 17), puedes eliminar todos los datos introducidos en la sesion.",
        "consent_record_title": "Registro de tu consentimiento",
        "consent_record_caption": "Conservado localmente para accountability (Art. 7 RGPD). No transmitido.",
    },

    # -------------------------------------------------------------------------
    # FRENCH
    # -------------------------------------------------------------------------
    "fr": {
        "consent_title": "Avis de Confidentialite et Consentement au Traitement",
        "consent_intro": (
            "Bienvenue sur <strong>CareerMatch AI</strong>. Avant de continuer, nous vous informons que "
            "cette application traite vos donnees personnelles conformement au "
            "<strong>Reglement General sur la Protection des Donnees (RGPD - Reg. UE 2016/679)</strong> "
            "et au <strong>Reglement sur l'Intelligence Artificielle (AI Act - Reg. UE 2024/1689)</strong>."
        ),
        "consent_data_label": "Donnees traitees :",
        "consent_data_value": "Texte du CV, donnees personnelles dans le CV Builder (nom, email, telephone, competences), descriptions de postes.",
        "consent_purpose_label": "Finalite :",
        "consent_purpose_value": "Analyse de compatibilite professionnelle via algorithmes classiques de Machine Learning (TF-IDF, Random Forest, K-Means, LDA) -- aucun fournisseur LLM externe n'est contacte.",
        "consent_retention_label": "Conservation :",
        "consent_retention_value": "Les donnees sont traitees exclusivement dans la session actuelle du navigateur et <u>ne sont pas stockees sur aucun serveur</u>. A la fin de la session, toutes les donnees sont automatiquement supprimees.",
        "consent_details": 'Pour plus de details, consultez la politique complete dans la section "Privacy & AI" du menu.',
        "checkbox_gdpr": "J'ai lu et je consens au traitement de mes donnees personnelles conformement a l'Art. 6(1)(a) RGPD",
        "checkbox_ai": "Je suis conscient que mes donnees seront traitees par des systemes d'IA executes localement (AI Act Art. 50)",
        "btn_accept": "J'accepte et je continue",
        "btn_decline": "Je refuse et je sors",
        "consent_warning": "Les deux consentements sont necessaires pour utiliser l'application.",
        "consent_declined_title": "Consentement non fourni",
        "consent_declined_body": "Sans les consentements RGPD et AI Act, l'application ne peut pas fonctionner. Vous pouvez fermer cet onglet.",
        "page_title": "Confidentialite et Conformite IA",
        "page_subtitle": "Politique complete de traitement des donnees personnelles",
        "privacy_heading": "Politique de Confidentialite (Art. 13-14 RGPD)",
        "controller_title": "1. Responsable du Traitement",
        "controller_body": (
            "Projet developpe dans le contexte academique de l'"
            "<strong>Universite IULM</strong> (Milan) -- A.A. 2025-2026, "
            "cours de Data Mining & Text Analytics (Prof. Alessandro Bruno).<br><br>"
            "<strong>Equipe de developpement :</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Contact :</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a>"
        ),
        "data_title": "2. Donnees Personnelles Traitees",
        "data_body": (
            "<ul>"
            "<li><strong>Donnees d'identification :</strong> nom, prenom, email, telephone, localisation (saisis volontairement dans CV Builder)</li>"
            "<li><strong>Donnees professionnelles :</strong> competences techniques, experience, formation, projets</li>"
            "<li><strong>Documents :</strong> texte du Curriculum Vitae (charge ou colle)</li>"
            "<li><strong>Donnees de session :</strong> etat de la session Streamlit (non persistant), horodatage du consentement (hashe)</li>"
            "</ul>"
        ),
        "legal_title": "3. Finalite et Base Juridique",
        "legal_headers": ("Finalite", "Base Juridique"),
        "legal_rows": [
            ("Analyse CV vs description de poste", "Consentement (Art. 6(1)(a) RGPD)"),
            ("Generation de CV via CV Builder", "Consentement (Art. 6(1)(a) RGPD)"),
            ("Traitement ML pour scoring et gap analysis", "Consentement (Art. 6(1)(a) RGPD)"),
            ("Objectif academique / recherche (demonstration KDD)", "Interet legitime (Art. 6(1)(f) RGPD)"),
        ],
        "retention_title": "4. Conservation des Donnees",
        "retention_body": (
            "Les donnees sont traitees <strong>exclusivement dans la session actuelle</strong> du navigateur. "
            "<strong>Aucune base de donnees persistante</strong> ne stocke les donnees saisies.<br><br>"
            "<strong>Periode de conservation :</strong> Duree de la session navigateur.<br>"
            'Suppression automatique a la fermeture du navigateur ou immediate via le bouton "Supprimer mes donnees".'
        ),
        "rights_title": "5. Droits de la Personne Concernee (Art. 15-22 RGPD)",
        "rights_items": [
            "<strong>Acces</strong> (Art. 15) -- Obtenir confirmation et copie de vos donnees",
            "<strong>Rectification</strong> (Art. 16) -- Corriger les donnees inexactes",
            "<strong>Effacement</strong> (Art. 17) -- Droit a l'oubli",
            "<strong>Limitation</strong> (Art. 18) -- Limiter le traitement",
            "<strong>Portabilite</strong> (Art. 20) -- Recevoir les donnees dans un format structure",
            "<strong>Opposition</strong> (Art. 21) -- S'opposer au traitement",
            "<strong>Retrait du consentement</strong> (Art. 7(3)) -- Retirer le consentement a tout moment",
            "<strong>Reclamation</strong> (Art. 77) -- Deposer une reclamation aupres de l'autorite de controle (CNIL, www.cnil.fr)",
        ],
        "rights_note": 'Les donnees n\'existant que dans la session du navigateur, le droit d\'effacement peut etre exerce immediatement via le bouton "Supprimer mes donnees" dans la barre laterale.',
        "processors_title": "6. Sous-traitants (Art. 28 RGPD)",
        "processors_body": (
            "<p>L'application est hebergee sur une infrastructure tierce agissant comme "
            "<strong>sous-traitant</strong> :</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- hebergement, region AWS UE.</li>"
            "<li><strong>GitHub Inc.</strong> -- hebergement du code source uniquement (pas de donnees utilisateur).</li>"
            "</ul>"
            "<p>Aucun fournisseur LLM externe n'est contacte : tout le traitement IA s'effectue localement.</p>"
        ),
        "transfer_title": "7. Transferts Internationaux",
        "transfer_body": (
            "Les donnees <strong>ne sont pas transferees</strong> hors de la session du navigateur.<br>"
            "L'hebergeur opere sur l'infrastructure AWS region UE. Les transferts incidents reposent sur "
            "des decisions d'adequation (EU-US DPF) et des Clauses Contractuelles Types (CCT)."
        ),
        "dpia_title": "8. Resume DPIA (Art. 35 RGPD)",
        "dpia_body": (
            "<p>Une evaluation d'impact simplifiee a ete realisee :</p>"
            "<ul>"
            "<li><strong>Risque :</strong> Faible. Aucune categorie particuliere de donnees ; "
            "aucun profilage a effets juridiques ; aucune surveillance a grande echelle.</li>"
            "<li><strong>Mitigations :</strong> conservation par session uniquement, pas de BDD persistante, "
            "pas de LLM tiers, supervision humaine, explicabilite via Dev Console.</li>"
            "<li><strong>Risque residuel :</strong> inference erronee des competences -- attenuee par la revision de l'utilisateur.</li>"
            "</ul>"
        ),
        "ai_heading": "Transparence sur l'Intelligence Artificielle (AI Act)",
        "ai_intro": (
            "Cette application utilise des systemes d'<strong>Intelligence Artificielle</strong>. "
            "Conformement aux <strong>Arts. 50-52 de l'AI Act</strong>, nous declarons :"
        ),
        "ai_risk_label": "Classification du risque :",
        "ai_risk_value": "RISQUE LIMITE / MINIMAL",
        "ai_models_label": "Systemes IA utilises :",
        "ai_models_headers": ("Composant", "Algorithme", "Finalite", "Fournisseur / Localisation"),
        "ai_decisions": (
            "<strong>Decisions automatisees :</strong> Les resultats sont <strong>purement indicatifs</strong>. "
            "Aucune decision automatisee a effets juridiques (Art. 22 RGPD)."
        ),
        "ai_oversight": (
            "<strong>Supervision humaine :</strong> Tous les systemes IA sont des outils de soutien. "
            "Les decisions finales appartiennent a l'utilisateur."
        ),
        "ai_limitations": (
            "<strong>Limites :</strong> Les modeles ML peuvent produire des resultats imprecis. "
            "Le score est une approximation statistique."
        ),
        "ai_no_llm": (
            "<strong>Aucun LLM externe :</strong> Cette application <u>n'envoie pas</u> vos donnees a "
            "OpenAI, Anthropic, Google ni a aucun autre fournisseur de LLM."
        ),
        "exercise_rights": "Exercez vos Droits",
        "delete_title": "Supprimer mes Donnees",
        "delete_body": "Cette action supprimera immediatement toutes les donnees de la session actuelle. Action irreversible.",
        "delete_confirm": "Je confirme vouloir supprimer toutes mes donnees",
        "delete_btn": "Supprimer toutes mes donnees",
        "delete_success": "Toutes vos donnees ont ete supprimees. La session a ete reinitialisee.",
        "delete_info": "Votre consentement a ete revoque. Il sera redemande au prochain acces.",
        "contact_heading": "Contactez-nous",
        "contact_body": "Pour toute question sur le traitement des donnees ou vos droits RGPD, utilisez l'un des canaux ci-dessous.",
        "contact_name": "Nom Complet",
        "contact_email": "Email",
        "contact_subject": "Objet",
        "contact_subject_options": ["Demande d'acces (Art. 15)", "Demande de suppression (Art. 17)", "Portabilite (Art. 20)", "Retrait du consentement (Art. 7)", "Demande generale"],
        "contact_message": "Message",
        "contact_submit_email": "Ouvrir dans le client email",
        "contact_submit_github": "Ouvrir un GitHub Issue",
        "contact_download_json": "Telecharger la demande en JSON",
        "contact_success": "Votre demande est prete. Utilisez l'un des boutons ci-dessus. Reponse sous 30 jours (RGPD).",
        "contact_error": "Veuillez remplir tous les champs avant de generer la demande.",
        "footer": "Politique v{version} mise a jour le {date} | Conforme RGPD (Reg. UE 2016/679) et AI Act (Reg. UE 2024/1689)",
        "sidebar_badge": "RGPD + AI Act Conforme",
        "data_mgmt": "Gestion des donnees personnelles",
        "data_mgmt_caption": "Selon le RGPD (Art. 17), vous pouvez supprimer toutes les donnees saisies dans la session.",
        "consent_record_title": "Enregistrement de votre consentement",
        "consent_record_caption": "Stocke localement pour responsabilite (Art. 7 RGPD). Non transmis.",
    },

    # -------------------------------------------------------------------------
    # GERMAN
    # -------------------------------------------------------------------------
    "de": {
        "consent_title": "Datenschutzhinweis und Einwilligung zur Datenverarbeitung",
        "consent_intro": (
            "Willkommen bei <strong>CareerMatch AI</strong>. Bevor Sie fortfahren, informieren wir Sie, dass "
            "diese Anwendung Ihre personenbezogenen Daten gemass der "
            "<strong>Datenschutz-Grundverordnung (DSGVO - EU-Verordnung 2016/679)</strong> "
            "und dem <strong>KI-Gesetz (AI Act - EU-Verordnung 2024/1689)</strong> verarbeitet."
        ),
        "consent_data_label": "Verarbeitete Daten:",
        "consent_data_value": "CV-Text, persoenliche Daten im CV Builder (Name, E-Mail, Telefon, Faehigkeiten), Stellenbeschreibungen.",
        "consent_purpose_label": "Zweck:",
        "consent_purpose_value": "Berufliche Kompatibilitaetsanalyse mit klassischen Machine-Learning-Algorithmen (TF-IDF, Random Forest, K-Means, LDA) -- kein externer LLM-Anbieter wird kontaktiert.",
        "consent_retention_label": "Aufbewahrung:",
        "consent_retention_value": "Die Daten werden ausschliesslich in der aktuellen Browser-Sitzung verarbeitet und <u>nicht auf einem Server gespeichert</u>. Beim Schliessen der Sitzung werden alle Daten automatisch geloescht.",
        "consent_details": 'Weitere Details finden Sie in der vollstaendigen Richtlinie im Menue "Privacy & AI".',
        "checkbox_gdpr": "Ich habe die Verarbeitung meiner personenbezogenen Daten gemass Art. 6(1)(a) DSGVO gelesen und stimme zu",
        "checkbox_ai": "Ich bin mir bewusst, dass meine Daten von lokal ausgefuehrten KI-Systemen verarbeitet werden (AI Act Art. 50)",
        "btn_accept": "Akzeptieren und Fortfahren",
        "btn_decline": "Ablehnen und Beenden",
        "consent_warning": "Beide Einwilligungen sind erforderlich, um die Anwendung zu nutzen.",
        "consent_declined_title": "Einwilligung nicht erteilt",
        "consent_declined_body": "Ohne DSGVO- und AI-Act-Einwilligungen kann die Anwendung nicht arbeiten. Sie koennen diesen Tab schliessen.",
        "page_title": "Datenschutz & KI-Konformitaet",
        "page_subtitle": "Vollstaendige Datenschutzrichtlinie",
        "privacy_heading": "Datenschutzrichtlinie (Art. 13-14 DSGVO)",
        "controller_title": "1. Verantwortlicher",
        "controller_body": (
            "Projekt entwickelt im akademischen Kontext der "
            "<strong>IULM-Universitaet</strong> (Mailand) -- Studienjahr 2025-2026, "
            "Kurs Data Mining & Text Analytics (Prof. Alessandro Bruno).<br><br>"
            "<strong>Entwicklungsteam:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Kontakt:</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a>"
        ),
        "data_title": "2. Verarbeitete Daten",
        "data_body": (
            "<ul>"
            "<li><strong>Identifikationsdaten:</strong> Name, Nachname, E-Mail, Telefon, Ort (freiwillig im CV Builder eingegeben)</li>"
            "<li><strong>Berufliche Daten:</strong> Faehigkeiten, Erfahrung, Bildung, Projekte</li>"
            "<li><strong>Dokumente:</strong> Lebenslauf-Text (hochgeladen oder eingefuegt)</li>"
            "<li><strong>Sitzungsdaten:</strong> Streamlit-Session-State (nicht persistent), Einwilligungs-Zeitstempel (gehashed)</li>"
            "</ul>"
        ),
        "legal_title": "3. Zweck und Rechtsgrundlage",
        "legal_headers": ("Zweck", "Rechtsgrundlage"),
        "legal_rows": [
            ("CV-vs-Stellenbeschreibungs-Analyse", "Einwilligung (Art. 6(1)(a) DSGVO)"),
            ("CV-Erstellung via CV Builder", "Einwilligung (Art. 6(1)(a) DSGVO)"),
            ("ML-Verarbeitung fuer Scoring und Gap-Analyse", "Einwilligung (Art. 6(1)(a) DSGVO)"),
            ("Akademischer Zweck / Forschung (KDD-Demonstration)", "Berechtigtes Interesse (Art. 6(1)(f) DSGVO)"),
        ],
        "retention_title": "4. Datenaufbewahrung",
        "retention_body": (
            "Daten werden <strong>ausschliesslich in der aktuellen Sitzung</strong> verarbeitet. "
            "<strong>Keine persistente Datenbank.</strong><br><br>"
            "<strong>Aufbewahrungsdauer:</strong> Dauer der Browser-Sitzung.<br>"
            'Automatische Loeschung beim Schliessen oder sofortige Loeschung via "Meine Daten loeschen".'
        ),
        "rights_title": "5. Rechte der betroffenen Person (Art. 15-22 DSGVO)",
        "rights_items": [
            "<strong>Auskunft</strong> (Art. 15) -- Bestaetigung und Kopie der Daten",
            "<strong>Berichtigung</strong> (Art. 16) -- Korrektur unrichtiger Daten",
            "<strong>Loeschung</strong> (Art. 17) -- Recht auf Vergessenwerden",
            "<strong>Einschraenkung</strong> (Art. 18) -- Einschraenkung der Verarbeitung",
            "<strong>Datenuebertragbarkeit</strong> (Art. 20)",
            "<strong>Widerspruch</strong> (Art. 21)",
            "<strong>Widerruf der Einwilligung</strong> (Art. 7(3))",
            "<strong>Beschwerde</strong> (Art. 77) -- bei der Aufsichtsbehoerde (BfDI / Landes-LDA)",
        ],
        "rights_note": 'Da Daten nur in der Browser-Sitzung existieren, kann das Recht auf Loeschung sofort via "Meine Daten loeschen" in der Sidebar ausgeuebt werden.',
        "processors_title": "6. Auftragsverarbeiter (Art. 28 DSGVO)",
        "processors_body": (
            "<p>Die Anwendung wird auf einer Drittinfrastruktur gehostet, die als <strong>Auftragsverarbeiter</strong> handelt:</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- App-Hosting, AWS EU-Region.</li>"
            "<li><strong>GitHub Inc.</strong> -- nur Quellcode-Hosting (keine Nutzerdaten).</li>"
            "</ul>"
            "<p>Es wird kein externer LLM-Anbieter kontaktiert.</p>"
        ),
        "transfer_title": "7. Internationale Datenuebertragungen",
        "transfer_body": (
            "Daten werden <strong>nicht ausserhalb</strong> der Browser-Sitzung uebertragen.<br>"
            "Der Hosting-Anbieter laeuft auf AWS EU. Etwaige Uebertragungen stuetzen sich auf "
            "Angemessenheitsbeschluesse (EU-US DPF) und Standardvertragsklauseln (SCC)."
        ),
        "dpia_title": "8. DSFA-Zusammenfassung (Art. 35 DSGVO)",
        "dpia_body": (
            "<p>Eine vereinfachte Datenschutz-Folgenabschaetzung wurde durchgefuehrt:</p>"
            "<ul>"
            "<li><strong>Risiko:</strong> Gering. Keine besonderen Datenkategorien; kein Profiling mit Rechtsfolgen.</li>"
            "<li><strong>Massnahmen:</strong> sitzungsgebundene Speicherung, kein persistenter Speicher, "
            "kein Dritt-LLM, menschliche Aufsicht, Erklaerbarkeit via Dev Console.</li>"
            "<li><strong>Restrisiko:</strong> falsche Skill-Inferenz -- gemildert durch Nutzerueberpruefung.</li>"
            "</ul>"
        ),
        "ai_heading": "KI-Transparenz (AI Act)",
        "ai_intro": (
            "Diese Anwendung nutzt <strong>KI-Systeme</strong>. Gemaess <strong>Art. 50-52 AI Act</strong> erklaeren wir:"
        ),
        "ai_risk_label": "Risikoeinstufung:",
        "ai_risk_value": "BEGRENZTES / MINIMALES RISIKO",
        "ai_models_label": "Verwendete KI-Systeme:",
        "ai_models_headers": ("Komponente", "Algorithmus", "Zweck", "Anbieter / Ort"),
        "ai_decisions": (
            "<strong>Automatisierte Entscheidungen:</strong> Die Ergebnisse sind <strong>rein indikativ</strong>. "
            "Es werden keine automatisierten Entscheidungen mit Rechtswirkung getroffen (Art. 22 DSGVO)."
        ),
        "ai_oversight": (
            "<strong>Menschliche Aufsicht:</strong> Alle KI-Systeme sind Unterstuetzungswerkzeuge. "
            "Endentscheidungen liegen beim Nutzer."
        ),
        "ai_limitations": (
            "<strong>Einschraenkungen:</strong> ML-Modelle koennen ungenaue Ergebnisse liefern. "
            "Der Score ist eine statistische Annaeherung."
        ),
        "ai_no_llm": (
            "<strong>Kein externes LLM:</strong> Diese Anwendung sendet <u>keine</u> Daten an OpenAI, "
            "Anthropic, Google oder andere LLM-Anbieter."
        ),
        "exercise_rights": "Rechte ausueben",
        "delete_title": "Meine Daten loeschen",
        "delete_body": "Diese Aktion loescht sofort alle Daten der aktuellen Sitzung. Unwiderruflich.",
        "delete_confirm": "Ich bestaetige, dass ich alle meine Daten loeschen moechte",
        "delete_btn": "Alle meine Daten loeschen",
        "delete_success": "Alle Daten wurden geloescht. Die Sitzung wurde zurueckgesetzt.",
        "delete_info": "Ihre Einwilligung wurde widerrufen. Sie wird beim naechsten Zugriff erneut abgefragt.",
        "contact_heading": "Kontakt",
        "contact_body": "Fuer Fragen zur Datenverarbeitung oder Ihren DSGVO-Rechten nutzen Sie einen der unten stehenden Kanaele.",
        "contact_name": "Vollstaendiger Name",
        "contact_email": "E-Mail-Adresse",
        "contact_subject": "Betreff",
        "contact_subject_options": ["Auskunftsanfrage (Art. 15)", "Loeschungsanfrage (Art. 17)", "Datenuebertragbarkeit (Art. 20)", "Widerruf der Einwilligung (Art. 7)", "Allgemeine Anfrage"],
        "contact_message": "Nachricht",
        "contact_submit_email": "Im E-Mail-Client oeffnen",
        "contact_submit_github": "GitHub Issue oeffnen",
        "contact_download_json": "Anfrage als JSON herunterladen",
        "contact_success": "Ihre Anfrage ist bereit. Verwenden Sie eine der Schaltflaechen oben. Antwort innerhalb von 30 Tagen (DSGVO).",
        "contact_error": "Bitte fuellen Sie alle Felder aus, bevor Sie die Anfrage erstellen.",
        "footer": "Richtlinie v{version} aktualisiert am {date} | Konform mit DSGVO (EU-VO 2016/679) und AI Act (EU-VO 2024/1689)",
        "sidebar_badge": "DSGVO + AI Act Konform",
        "data_mgmt": "Verwaltung persoenlicher Daten",
        "data_mgmt_caption": "Gemaess DSGVO (Art. 17) koennen Sie alle Daten dieser Sitzung loeschen.",
        "consent_record_title": "Ihre Einwilligungs-Aufzeichnung",
        "consent_record_caption": "Lokal gespeichert zur Rechenschaftspflicht (Art. 7 DSGVO). Nicht uebertragen.",
    },

    # -------------------------------------------------------------------------
    # PORTUGUESE
    # -------------------------------------------------------------------------
    "pt": {
        "consent_title": "Aviso de Privacidade e Consentimento de Tratamento",
        "consent_intro": (
            "Bem-vindo ao <strong>CareerMatch AI</strong>. Antes de continuar, informamos que "
            "esta aplicacao trata os seus dados pessoais em conformidade com o "
            "<strong>Regulamento Geral de Protecao de Dados (RGPD - Reg. UE 2016/679)</strong> "
            "e com a <strong>Lei sobre Inteligencia Artificial (AI Act - Reg. UE 2024/1689)</strong>."
        ),
        "consent_data_label": "Dados tratados:",
        "consent_data_value": "Texto do CV, dados pessoais no CV Builder (nome, email, telefone, competencias), descricoes de vagas.",
        "consent_purpose_label": "Finalidade:",
        "consent_purpose_value": "Analise de compatibilidade profissional via algoritmos classicos de Machine Learning (TF-IDF, Random Forest, K-Means, LDA) -- nenhum fornecedor de LLM externo e contactado.",
        "consent_retention_label": "Conservacao:",
        "consent_retention_value": "Os dados sao tratados exclusivamente na sessao atual do navegador e <u>nao sao guardados em nenhum servidor</u>. Ao terminar a sessao, todos os dados sao automaticamente apagados.",
        "consent_details": 'Para mais detalhes, consulte a politica completa na seccao "Privacy & AI" do menu.',
        "checkbox_gdpr": "Li e consinto o tratamento dos meus dados pessoais nos termos do Art. 6(1)(a) RGPD",
        "checkbox_ai": "Estou consciente de que os meus dados serao tratados por sistemas de IA executados localmente (AI Act Art. 50)",
        "btn_accept": "Aceito e Continuo",
        "btn_decline": "Recuso e Saio",
        "consent_warning": "Sao necessarios ambos os consentimentos para usar a aplicacao.",
        "consent_declined_title": "Consentimento nao fornecido",
        "consent_declined_body": "Sem os consentimentos RGPD e AI Act a aplicacao nao pode funcionar. Pode fechar este separador.",
        "page_title": "Privacidade e Conformidade IA",
        "page_subtitle": "Politica completa de tratamento de dados pessoais",
        "privacy_heading": "Politica de Privacidade (Art. 13-14 RGPD)",
        "controller_title": "1. Responsavel pelo Tratamento",
        "controller_body": (
            "Projeto desenvolvido no contexto academico da "
            "<strong>Universidade IULM</strong> (Milao) -- A.A. 2025-2026, "
            "curso de Data Mining & Text Analytics (Prof. Alessandro Bruno).<br><br>"
            "<strong>Equipa de desenvolvimento:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>"
            f"<strong>Contacto:</strong> <a href='mailto:{CONTACT_EMAIL}' style='color:#00A0DC;'>{CONTACT_EMAIL}</a>"
        ),
        "data_title": "2. Dados Pessoais Tratados",
        "data_body": (
            "<ul>"
            "<li><strong>Dados identificativos:</strong> nome, apelido, email, telefone, localizacao (voluntarios)</li>"
            "<li><strong>Dados profissionais:</strong> competencias tecnicas, experiencia, formacao, projetos</li>"
            "<li><strong>Documentos:</strong> texto do CV (carregado ou colado)</li>"
            "<li><strong>Dados de sessao:</strong> estado da sessao Streamlit (nao persistente), timestamp do consentimento (hashed)</li>"
            "</ul>"
        ),
        "legal_title": "3. Finalidade e Base Juridica",
        "legal_headers": ("Finalidade", "Base Juridica"),
        "legal_rows": [
            ("Analise CV vs Descricao de Vaga", "Consentimento (Art. 6(1)(a) RGPD)"),
            ("Geracao de CV via CV Builder", "Consentimento (Art. 6(1)(a) RGPD)"),
            ("Processamento ML para scoring e gap analysis", "Consentimento (Art. 6(1)(a) RGPD)"),
            ("Finalidade academica / investigacao", "Interesse legitimo (Art. 6(1)(f) RGPD)"),
        ],
        "retention_title": "4. Conservacao dos Dados",
        "retention_body": (
            "Os dados sao tratados <strong>exclusivamente na sessao atual</strong> do navegador. "
            "<strong>Nenhuma base de dados persistente.</strong><br><br>"
            "<strong>Periodo de conservacao:</strong> Duracao da sessao.<br>"
            'Eliminacao automatica ao fechar o navegador ou imediata via "Apagar os meus dados".'
        ),
        "rights_title": "5. Direitos do Titular (Art. 15-22 RGPD)",
        "rights_items": [
            "<strong>Acesso</strong> (Art. 15)",
            "<strong>Retificacao</strong> (Art. 16)",
            "<strong>Apagamento</strong> (Art. 17) -- direito ao esquecimento",
            "<strong>Limitacao</strong> (Art. 18)",
            "<strong>Portabilidade</strong> (Art. 20)",
            "<strong>Oposicao</strong> (Art. 21)",
            "<strong>Retirada do consentimento</strong> (Art. 7(3))",
            "<strong>Reclamacao</strong> (Art. 77) -- autoridade de controlo (CNPD, www.cnpd.pt)",
        ],
        "rights_note": 'Como os dados existem apenas na sessao, o direito ao apagamento pode ser exercido imediatamente via "Apagar os meus dados" na sidebar.',
        "processors_title": "6. Subcontratantes (Art. 28 RGPD)",
        "processors_body": (
            "<p>A aplicacao e alojada em infraestrutura de terceiros como <strong>subcontratante</strong>:</p>"
            "<ul>"
            "<li><strong>Streamlit Community Cloud</strong> (Snowflake Inc.) -- alojamento, regiao AWS UE.</li>"
            "<li><strong>GitHub Inc.</strong> -- alojamento do codigo (sem dados de utilizador).</li>"
            "</ul>"
            "<p>Nenhum fornecedor externo de LLM e contactado.</p>"
        ),
        "transfer_title": "7. Transferencias Internacionais",
        "transfer_body": (
            "Os dados <strong>nao sao transferidos</strong> para fora da sessao do navegador.<br>"
            "O fornecedor de alojamento opera em AWS regiao UE. Transferencias incidentais baseiam-se em "
            "decisoes de adequacao (EU-US DPF) e CCT."
        ),
        "dpia_title": "8. Resumo da AIPD (Art. 35 RGPD)",
        "dpia_body": (
            "<p>Foi realizada uma avaliacao de impacto simplificada:</p>"
            "<ul>"
            "<li><strong>Risco:</strong> Baixo. Sem categorias especiais de dados; sem profiling com efeitos juridicos.</li>"
            "<li><strong>Mitigacoes:</strong> retencao apenas em sessao, sem BD persistente, sem LLM de terceiros, "
            "supervisao humana, explicabilidade via Dev Console.</li>"
            "<li><strong>Risco residual:</strong> inferencia errada de competencias -- mitigada por revisao do utilizador.</li>"
            "</ul>"
        ),
        "ai_heading": "Transparencia sobre Inteligencia Artificial (AI Act)",
        "ai_intro": (
            "Esta aplicacao utiliza sistemas de <strong>Inteligencia Artificial</strong>. "
            "Em conformidade com os <strong>Arts. 50-52 do AI Act</strong>, declaramos:"
        ),
        "ai_risk_label": "Classificacao de risco:",
        "ai_risk_value": "RISCO LIMITADO / MINIMO",
        "ai_models_label": "Sistemas IA utilizados:",
        "ai_models_headers": ("Componente", "Algoritmo", "Finalidade", "Fornecedor / Localizacao"),
        "ai_decisions": (
            "<strong>Decisoes automatizadas:</strong> Os resultados sao <strong>meramente indicativos</strong>. "
            "Nao se tomam decisoes automatizadas com efeitos juridicos (Art. 22 RGPD)."
        ),
        "ai_oversight": (
            "<strong>Supervisao humana:</strong> Todos os sistemas IA sao ferramentas de apoio. "
            "As decisoes finais cabem ao utilizador."
        ),
        "ai_limitations": (
            "<strong>Limitacoes:</strong> Os modelos ML podem produzir resultados imprecisos. "
            "O score e uma aproximacao estatistica."
        ),
        "ai_no_llm": (
            "<strong>Sem LLM externo:</strong> Esta aplicacao <u>nao</u> envia os seus dados a OpenAI, "
            "Anthropic, Google ou outros fornecedores de LLM."
        ),
        "exercise_rights": "Exerca os seus Direitos",
        "delete_title": "Apagar os meus Dados",
        "delete_body": "Esta acao apagara imediatamente todos os dados da sessao atual. Irreversivel.",
        "delete_confirm": "Confirmo que pretendo apagar todos os meus dados",
        "delete_btn": "Apagar todos os meus dados",
        "delete_success": "Todos os seus dados foram apagados. A sessao foi reiniciada.",
        "delete_info": "O seu consentimento foi revogado. Sera pedido novamente no proximo acesso.",
        "contact_heading": "Contacte-nos",
        "contact_body": "Para qualquer questao sobre tratamento de dados ou os seus direitos RGPD, utilize um dos canais abaixo.",
        "contact_name": "Nome Completo",
        "contact_email": "Email",
        "contact_subject": "Assunto",
        "contact_subject_options": ["Pedido de Acesso (Art. 15)", "Pedido de Apagamento (Art. 17)", "Portabilidade (Art. 20)", "Retirada de Consentimento (Art. 7)", "Pedido Geral"],
        "contact_message": "Mensagem",
        "contact_submit_email": "Abrir no cliente de email",
        "contact_submit_github": "Abrir um GitHub Issue",
        "contact_download_json": "Descarregar pedido em JSON",
        "contact_success": "O seu pedido esta pronto. Use um dos botoes acima. Resposta em 30 dias (RGPD).",
        "contact_error": "Preencha todos os campos antes de gerar o pedido.",
        "footer": "Politica v{version} atualizada em {date} | Conforme RGPD (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689)",
        "sidebar_badge": "RGPD + AI Act Conforme",
        "data_mgmt": "Gestao de dados pessoais",
        "data_mgmt_caption": "Nos termos do RGPD (Art. 17), pode apagar todos os dados desta sessao.",
        "consent_record_title": "Registo do seu consentimento",
        "consent_record_caption": "Guardado localmente para accountability (Art. 7 RGPD). Nao transmitido.",
    },
}


# =============================================================================
# HELPERS
# =============================================================================

def _t(key: str):
    """Get translated string based on current language setting."""
    lang = st.session_state.get("gdpr_lang", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, TRANSLATIONS["en"].get(key, key))


def _now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _consent_fingerprint() -> str:
    """
    Returns a short hash that lets us identify a consent record without storing
    any actual personal data. Combines timestamp + a session salt so two
    different users get different fingerprints. Purely local.
    """
    salt = st.session_state.get("gdpr_session_salt")
    if not salt:
        salt = hashlib.sha256(_now_utc_iso().encode()).hexdigest()[:16]
        st.session_state["gdpr_session_salt"] = salt
    payload = f"{salt}|{POLICY_VERSION}".encode()
    return hashlib.sha256(payload).hexdigest()[:12]


def _record_consent(consent_data: bool, consent_ai: bool) -> dict:
    record = {
        "timestamp_utc": _now_utc_iso(),
        "policy_version": POLICY_VERSION,
        "language": st.session_state.get("gdpr_lang", "en"),
        "consent_data_processing": bool(consent_data),
        "consent_ai_act": bool(consent_ai),
        "fingerprint": _consent_fingerprint(),
    }
    st.session_state["gdpr_consent_record"] = record
    return record


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
        .privacy-section a { color: #00A0DC; }
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
        .contact-channel {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .consent-record-pre {
            background: #0d1117;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 0.75rem 1rem;
            font-size: 0.78rem;
            color: #c9d1d9;
            overflow-x: auto;
        }
    </style>
    """


# =============================================================================
# LANGUAGE TOGGLE
# =============================================================================

def render_language_toggle():
    """Renders a compact 6-language toggle aligned with Ruben assistant."""
    col1, col2 = st.columns([6, 1])
    with col2:
        st.selectbox(
            "Lang",
            options=[code for code, _ in SUPPORTED_LANGUAGES],
            format_func=lambda x: dict(SUPPORTED_LANGUAGES).get(x, x.upper()),
            key="gdpr_lang",
            label_visibility="collapsed",
        )


# =============================================================================
# CONSENT BANNER (GDPR Art. 6-7, AI Act Art. 50)
# =============================================================================

def render_consent_banner() -> bool:
    """
    Blocking consent gate. Returns True if both GDPR and AI Act consents
    are stored in session_state, False otherwise.
    """
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

        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button(
                _t("btn_accept"),
                type="primary",
                use_container_width=True,
                disabled=not (consent_data and consent_ai),
            ):
                st.session_state["gdpr_consent_given"] = True
                _record_consent(consent_data, consent_ai)
                st.rerun()
        with btn_col2:
            if st.button(_t("btn_decline"), use_container_width=True):
                st.session_state["gdpr_consent_declined"] = True
                st.rerun()

        if not (consent_data and consent_ai):
            st.caption(_t("consent_warning"))

        if st.session_state.get("gdpr_consent_declined"):
            st.warning(f"**{_t('consent_declined_title')}** -- {_t('consent_declined_body')}")

    return False


# =============================================================================
# PRIVACY POLICY PAGE
# =============================================================================

def render_privacy_policy_page():
    st.markdown(get_compliance_css(), unsafe_allow_html=True)

    render_language_toggle()

    st.markdown(f"""
    <div style='display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;'>
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

    for section_key in ("controller", "data"):
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

    # Sections that are pure HTML body
    for section_key in ("retention",):
        st.markdown(f"""
        <div class="privacy-section">
            <h4>{_t(f"{section_key}_title")}</h4>
            <p>{_t(f"{section_key}_body")}</p>
        </div>
        """, unsafe_allow_html=True)

    # Rights list
    rights_list = "".join(f"<li>{r}</li>" for r in _t("rights_items"))
    st.markdown(f"""
    <div class="privacy-section">
        <h4>{_t("rights_title")}</h4>
        <ul>{rights_list}</ul>
        <p style="margin-top: 0.5rem; color: #8b949e; font-size: 0.85rem;">{_t("rights_note")}</p>
    </div>
    """, unsafe_allow_html=True)

    # Processors, Transfer, DPIA (new sections)
    for section_key in ("processors", "transfer", "dpia"):
        st.markdown(f"""
        <div class="privacy-section">
            <h4>{_t(f"{section_key}_title")}</h4>
            {_t(f"{section_key}_body")}
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # --- AI ACT TRANSPARENCY ---
    render_ai_transparency()

    st.divider()

    # --- CONSENT RECORD (accountability) ---
    record = st.session_state.get("gdpr_consent_record")
    if record:
        st.markdown(f"### {_t('consent_record_title')}")
        st.caption(_t("consent_record_caption"))
        st.markdown(
            f"<pre class='consent-record-pre'>{json.dumps(record, indent=2)}</pre>",
            unsafe_allow_html=True,
        )

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
        {_t("footer").format(version=POLICY_VERSION, date=POLICY_DATE)}
    </p>
    """, unsafe_allow_html=True)


# =============================================================================
# AI ACT TRANSPARENCY (Art. 50-52)
# =============================================================================

def render_ai_transparency():
    headers = _t("ai_models_headers")
    # AI_MODELS now has 4 fields: component, algo, purpose, provider
    rows_html = ""
    for i, row in enumerate(AI_MODELS):
        # tolerate older 3-tuple format if someone overrides AI_MODELS
        if len(row) == 3:
            component, algo, purpose = row
            provider = "Local"
        else:
            component, algo, purpose, provider = row
        border = ' style="border-bottom: 1px solid #21262d;"' if i < len(AI_MODELS) - 1 else ""
        rows_html += (
            f'<tr{border}>'
            f'<td style="padding: 8px;">{component}</td>'
            f'<td style="padding: 8px;">{algo}</td>'
            f'<td style="padding: 8px;">{purpose}</td>'
            f'<td style="padding: 8px;">{provider}</td>'
            f'</tr>'
        )

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
                <th style="text-align: left; padding: 8px; color: #3884F4;">{headers[3]}</th>
            </tr>
            {rows_html}
        </table>

        <p style="margin-top: 1rem;">{_t("ai_decisions")}</p>
        <p>{_t("ai_oversight")}</p>
        <p>{_t("ai_limitations")}</p>
        <p style="margin-top: 0.75rem; padding: 0.5rem 0.75rem; background: rgba(0,200,83,0.08); border-left: 3px solid #00C853; border-radius: 4px;">{_t("ai_no_llm")}</p>
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
        if st.button(
            _t("delete_btn"),
            type="primary",
            use_container_width=True,
            disabled=not confirm,
        ):
            keys_to_clear = list(st.session_state.keys())
            for key in keys_to_clear:
                if key != "page":
                    del st.session_state[key]
            st.success(_t("delete_success"))
            st.info(_t("delete_info"))


# =============================================================================
# CONTACT FORM - now actually actionable
# =============================================================================

def _build_email_link(name: str, email: str, subject: str, message: str) -> str:
    body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n\n"
        f"---\n"
        f"Sent via CareerMatch AI Privacy form -- policy v{POLICY_VERSION}"
    )
    params = urllib.parse.urlencode({
        "subject": f"[CareerMatch AI - GDPR] {subject}",
        "body": body,
    }, quote_via=urllib.parse.quote)
    return f"mailto:{CONTACT_EMAIL}?{params}"


def _build_github_issue_link(name: str, subject: str, message: str) -> str:
    body = (
        f"**Type**: GDPR / Privacy request\n"
        f"**Subject**: {subject}\n"
        f"**From** (optional name): {name}\n\n"
        f"### Request\n\n{message}\n\n"
        f"---\n_Submitted via Privacy & AI page._"
    )
    params = urllib.parse.urlencode({
        "title": f"[Privacy] {subject}",
        "body": body,
        "labels": "privacy,gdpr",
    }, quote_via=urllib.parse.quote)
    return f"{GITHUB_ISSUES_URL}?{params}"


def render_contact_form():
    st.markdown(f"## {_t('contact_heading')}")
    st.markdown(f"""
    <div class="contact-channel">
        <p>{_t("contact_body")}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("gdpr_contact_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(_t("contact_name"))
        with col2:
            email = st.text_input(_t("contact_email"))

        subject = st.selectbox(_t("contact_subject"), options=_t("contact_subject_options"))
        message = st.text_area(_t("contact_message"), height=120)

        submitted = st.form_submit_button(_t("contact_submit_email"), use_container_width=True, type="primary")

    if submitted:
        if not (name and email and message):
            st.warning(_t("contact_error"))
            return

        st.success(_t("contact_success"))

        email_link = _build_email_link(name, email, subject, message)
        gh_link = _build_github_issue_link(name, subject, message)

        json_payload = json.dumps({
            "submitted_at_utc": _now_utc_iso(),
            "policy_version": POLICY_VERSION,
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }, indent=2, ensure_ascii=False)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.link_button(_t("contact_submit_email"), email_link, use_container_width=True)
        with c2:
            st.link_button(_t("contact_submit_github"), gh_link, use_container_width=True)
        with c3:
            st.download_button(
                _t("contact_download_json"),
                data=json_payload,
                file_name=f"careermatch_gdpr_request_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True,
            )


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
