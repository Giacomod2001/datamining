"""
================================================================================
GDPR & AI Act Compliance Module - CareerMatch AI
================================================================================

Modulo per la conformità al GDPR (Reg. UE 2016/679), EU AI Act (Reg. UE 2024/1689)
e Direttiva ePrivacy.

Funzionalità:
- Banner di consenso (consent gate)
- Informativa Privacy completa
- Trasparenza AI Act
- Cancellazione dati (diritto all'oblio)

================================================================================
"""

import streamlit as st
from datetime import datetime


# =============================================================================
# CSS STYLES FOR COMPLIANCE UI
# =============================================================================

def get_compliance_css():
    """Returns CSS for compliance UI elements."""
    return """
    <style>
        .gdpr-banner {
            background: linear-gradient(135deg, rgba(0, 119, 181, 0.15), rgba(0, 160, 220, 0.08));
            border: 1px solid rgba(0, 160, 220, 0.3);
            border-radius: 12px;
            padding: 2rem;
            margin: 1rem 0 2rem 0;
        }
        .gdpr-banner h3 {
            color: #00A0DC;
            margin-bottom: 1rem;
        }
        .gdpr-banner p {
            color: #c9d1d9;
            line-height: 1.6;
        }
        .privacy-section {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .privacy-section h4 {
            color: #00A0DC;
            margin-bottom: 0.75rem;
        }
        .ai-transparency-box {
            background: linear-gradient(135deg, rgba(56, 132, 244, 0.1), rgba(0, 200, 160, 0.08));
            border-left: 4px solid #3884F4;
            border-radius: 0 10px 10px 0;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .ai-transparency-box h4 {
            color: #3884F4;
            margin-bottom: 0.5rem;
        }
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
    </style>
    """


# =============================================================================
# CONSENT BANNER (GDPR Art. 6-7)
# =============================================================================

def render_consent_banner():
    """
    Renders a GDPR consent banner that blocks the app until accepted.
    
    Returns:
        bool: True if consent has been given, False otherwise.
    """
    if st.session_state.get("gdpr_consent_given", False):
        return True
    
    st.markdown(get_compliance_css(), unsafe_allow_html=True)
    
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    
    # Center the banner
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div class="gdpr-banner">
            <h3>🔒 Informativa sulla Privacy e Consenso al Trattamento</h3>
            <p>
                Benvenuto in <strong>CareerMatch AI</strong>. Prima di procedere, ti informiamo che 
                questa applicazione tratta i tuoi dati personali in conformità al 
                <strong>Regolamento Generale sulla Protezione dei Dati (GDPR - Reg. UE 2016/679)</strong>
                e al <strong>Regolamento sull'Intelligenza Artificiale (AI Act - Reg. UE 2024/1689)</strong>.
            </p>
            <p style="margin-top: 1rem;">
                <strong>Dati trattati:</strong> Testo del CV, dati personali inseriti nel CV Builder 
                (nome, email, telefono, competenze), descrizioni delle posizioni lavorative.
            </p>
            <p>
                <strong>Finalità:</strong> Analisi di compatibilità professionale tramite algoritmi 
                di Machine Learning (TF-IDF, Random Forest, K-Means Clustering, LDA Topic Modeling).
            </p>
            <p>
                <strong>Conservazione:</strong> I dati sono trattati esclusivamente nella sessione 
                corrente del browser e <u>non vengono salvati su alcun server</u>. Alla chiusura 
                della sessione, tutti i dati vengono automaticamente eliminati.
            </p>
            <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #8b949e;">
                Per maggiori dettagli, consulta l'informativa completa nella sezione "Privacy & AI" del menu.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Consent checkboxes
        consent_data = st.checkbox(
            "✅ Ho letto e acconsento al trattamento dei miei dati personali ai sensi dell'Art. 6(1)(a) GDPR",
            key="gdpr_consent_checkbox"
        )
        consent_ai = st.checkbox(
            "✅ Sono consapevole che i miei dati saranno elaborati da sistemi di Intelligenza Artificiale (AI Act Art. 52)",
            key="ai_act_consent_checkbox"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("Accetto e Proseguo", type="primary", use_container_width=True, 
                        disabled=not (consent_data and consent_ai)):
                st.session_state["gdpr_consent_given"] = True
                st.session_state["gdpr_consent_timestamp"] = datetime.now().isoformat()
                st.rerun()
        
        if not (consent_data and consent_ai):
            st.caption("⚠️ È necessario fornire entrambi i consensi per utilizzare l'applicazione.")
    
    return False


# =============================================================================
# PRIVACY POLICY PAGE (GDPR Art. 13-14)
# =============================================================================

def render_privacy_policy_page():
    """Renders a complete GDPR-compliant privacy policy in Italian."""
    
    st.markdown(get_compliance_css(), unsafe_allow_html=True)
    
    st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between;'>
        <div>
            <h1 style='margin: 0;'>Privacy & Conformità AI</h1>
            <p style='color: #8b949e; margin: 0.25rem 0 0 0;'>Informativa completa sul trattamento dei dati personali</p>
        </div>
        <div>
            <span class="compliance-badge">GDPR Compliant</span>
            <span class="compliance-badge" style="margin-left: 8px;">AI Act Compliant</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- INFORMATIVA PRIVACY ---
    
    st.markdown("## 📋 Informativa Privacy (Art. 13-14 GDPR)")
    
    st.markdown("""
    <div class="privacy-section">
        <h4>1. Titolare del Trattamento</h4>
        <p>
            Il presente progetto è sviluppato nel contesto accademico dell'<strong>Università IULM</strong> 
            (Milano) – A.A. 2025-2026, corso di Data Mining & Text Analytics.<br><br>
            <strong>Team di sviluppo:</strong> Giacomo Dell'Acqua, Luca Tallarico, Ruben Scoletta<br>
            <strong>Contatto:</strong> Per esercitare i propri diritti, inviare comunicazione tramite 
            i canali istituzionali dell'Università IULM.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-section">
        <h4>2. Dati Personali Trattati</h4>
        <p>L'applicazione può trattare le seguenti categorie di dati:</p>
        <ul>
            <li><strong>Dati identificativi:</strong> nome, cognome, indirizzo email, numero di telefono, 
                località (inseriti volontariamente nel CV Builder)</li>
            <li><strong>Dati professionali:</strong> competenze tecniche, esperienze lavorative, 
                percorso formativo, progetti</li>
            <li><strong>Documenti:</strong> testo del Curriculum Vitae (caricato o incollato dall'utente)</li>
            <li><strong>Dati di navigazione:</strong> stato della sessione Streamlit (non persistente)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-section">
        <h4>3. Finalità e Base Giuridica del Trattamento</h4>
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #00A0DC;">Finalità</th>
                <th style="text-align: left; padding: 8px; color: #00A0DC;">Base Giuridica</th>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Analisi di compatibilità CV vs Job Description</td>
                <td style="padding: 8px;">Consenso (Art. 6(1)(a) GDPR)</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Generazione CV tramite CV Builder</td>
                <td style="padding: 8px;">Consenso (Art. 6(1)(a) GDPR)</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Elaborazione ML per scoring e gap analysis</td>
                <td style="padding: 8px;">Consenso (Art. 6(1)(a) GDPR)</td>
            </tr>
            <tr>
                <td style="padding: 8px;">Scopo accademico / ricerca (dimostrazione KDD)</td>
                <td style="padding: 8px;">Legittimo interesse (Art. 6(1)(f) GDPR)</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-section">
        <h4>4. Conservazione dei Dati</h4>
        <p>
            I dati personali sono trattati <strong>esclusivamente nella sessione corrente</strong> 
            del browser. <strong>Non esiste alcun database persistente</strong> che memorizzi i dati inseriti.<br><br>
            ⏱️ <strong>Periodo di conservazione:</strong> Durata della sessione browser.<br>
            🗑️ <strong>Cancellazione:</strong> Automatica alla chiusura del browser/tab, 
            oppure immediata tramite il pulsante "Cancella i Miei Dati".
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-section">
        <h4>5. Diritti dell'Interessato (Art. 15-22 GDPR)</h4>
        <p>L'utente ha diritto a:</p>
        <ul>
            <li><strong>Accesso</strong> (Art. 15) — Ottenere conferma del trattamento e copia dei dati</li>
            <li><strong>Rettifica</strong> (Art. 16) — Correggere i dati inesatti</li>
            <li><strong>Cancellazione</strong> (Art. 17) — Ottenere la cancellazione dei dati ("diritto all'oblio")</li>
            <li><strong>Limitazione</strong> (Art. 18) — Limitare il trattamento dei dati</li>
            <li><strong>Portabilità</strong> (Art. 20) — Ricevere i dati in formato strutturato</li>
            <li><strong>Opposizione</strong> (Art. 21) — Opporsi al trattamento</li>
            <li><strong>Revoca del consenso</strong> (Art. 7(3)) — Revocare il consenso in qualsiasi momento</li>
        </ul>
        <p style="margin-top: 0.5rem; color: #8b949e; font-size: 0.85rem;">
            Poiché i dati esistono solo nella sessione browser, il diritto di cancellazione è esercitabile 
            immediatamente tramite il pulsante "Cancella i Miei Dati" nella barra laterale.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-section">
        <h4>6. Trasferimento Dati</h4>
        <p>
            I dati <strong>non vengono trasferiti a terze parti</strong> né verso paesi extra-UE.<br>
            L'applicazione è ospitata su <strong>Streamlit Community Cloud</strong> (server in AWS, regione UE).
            Nessun dato viene persistito al di fuori della sessione del browser dell'utente.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- AI ACT TRANSPARENCY ---
    render_ai_transparency("careermatch")
    
    st.divider()
    
    # --- DATA DELETION ---
    st.markdown("## 🗑️ Esercita i Tuoi Diritti")
    render_delete_my_data_button()
    
    st.divider()
    
    st.markdown(f"""
    <p style='color: #6e7681; font-size: 0.8rem; text-align: center;'>
        Informativa aggiornata al {datetime.now().strftime('%d/%m/%Y')} | 
        Conforme al GDPR (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689)
    </p>
    """, unsafe_allow_html=True)


# =============================================================================
# AI ACT TRANSPARENCY (Art. 52)
# =============================================================================

def render_ai_transparency(project_type="careermatch"):
    """
    Renders AI Act transparency disclosure.
    
    Args:
        project_type: "careermatch", "studenti", or "jobseeker"
    """
    
    if project_type == "careermatch":
        ai_models_html = """
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #3884F4;">Modello</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Algoritmo</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Scopo</th>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Skill Matching</td>
                <td style="padding: 8px;">Random Forest (150 alberi)</td>
                <td style="padding: 8px;">Classificazione competenze</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Analisi Semantica</td>
                <td style="padding: 8px;">TF-IDF + LSA</td>
                <td style="padding: 8px;">Contesto professionale</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Skill Clustering</td>
                <td style="padding: 8px;">K-Means + Hierarchical</td>
                <td style="padding: 8px;">Raggruppamento competenze</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Topic Discovery</td>
                <td style="padding: 8px;">LDA (Latent Dirichlet Allocation)</td>
                <td style="padding: 8px;">Identificazione temi JD</td>
            </tr>
            <tr>
                <td style="padding: 8px;">Fuzzy Matching</td>
                <td style="padding: 8px;">FuzzyWuzzy (85% soglia)</td>
                <td style="padding: 8px;">Tolleranza errori ortografici</td>
            </tr>
        </table>
        """
    elif project_type == "studenti":
        ai_models_html = """
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #3884F4;">Modello</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Algoritmo</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Scopo</th>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Churn Prediction</td>
                <td style="padding: 8px;">Random Forest (BigQuery ML)</td>
                <td style="padding: 8px;">Previsione abbandono studenti</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Behavioral Clustering</td>
                <td style="padding: 8px;">K-Means (K=4)</td>
                <td style="padding: 8px;">Segmentazione comportamentale</td>
            </tr>
            <tr>
                <td style="padding: 8px;">Satisfaction Prediction</td>
                <td style="padding: 8px;">Boosted Tree (BigQuery ML)</td>
                <td style="padding: 8px;">Previsione soddisfazione</td>
            </tr>
        </table>
        """
    elif project_type == "jobseeker":
        ai_models_html = """
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
            <tr style="border-bottom: 1px solid #30363d;">
                <th style="text-align: left; padding: 8px; color: #3884F4;">Modello</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Algoritmo</th>
                <th style="text-align: left; padding: 8px; color: #3884F4;">Scopo</th>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Skill Classification</td>
                <td style="padding: 8px;">Random Forest + TF-IDF</td>
                <td style="padding: 8px;">Classificazione competenze</td>
            </tr>
            <tr style="border-bottom: 1px solid #21262d;">
                <td style="padding: 8px;">Inference Engine</td>
                <td style="padding: 8px;">Hierarchical Rule-Based</td>
                <td style="padding: 8px;">Deduzione competenze implicite</td>
            </tr>
            <tr>
                <td style="padding: 8px;">Fuzzy Matching</td>
                <td style="padding: 8px;">FuzzyWuzzy</td>
                <td style="padding: 8px;">Tolleranza errori di digitazione</td>
            </tr>
        </table>
        """
    else:
        ai_models_html = "<p>Informazioni sui modelli non disponibili.</p>"
    
    st.markdown(f"""
    ## 🤖 Trasparenza sull'Intelligenza Artificiale (AI Act)
    
    <div class="ai-transparency-box">
        <h4>Dichiarazione ai sensi del Regolamento UE 2024/1689 (AI Act)</h4>
        <p>
            Questa applicazione utilizza sistemi di <strong>Intelligenza Artificiale</strong> 
            per l'elaborazione dei dati. In conformità all'<strong>Art. 52 dell'AI Act</strong>, 
            dichiariamo quanto segue:
        </p>
        
        <p style="margin-top: 1rem;"><strong>📊 Classificazione del rischio:</strong> 
            <span style="background: rgba(0, 200, 83, 0.2); padding: 2px 8px; border-radius: 4px; color: #00C853;">
            RISCHIO LIMITATO / MINIMO</span>
        </p>
        
        <p><strong>🎯 Sistemi AI utilizzati:</strong></p>
        {ai_models_html}
        
        <p style="margin-top: 1rem;">
            <strong>⚖️ Decisioni automatizzate:</strong> I risultati forniti dall'AI sono 
            <strong>puramente indicativi e a scopo informativo</strong>. Non vengono prese 
            decisioni automatizzate che producano effetti giuridici o che incidano significativamente 
            sull'utente (Art. 22 GDPR). L'utente è sempre libero di ignorare i suggerimenti forniti.
        </p>
        
        <p>
            <strong>👤 Supervisione umana:</strong> Tutti i sistemi AI sono progettati come 
            strumenti di supporto. Le decisioni finali spettano sempre all'utente umano.
        </p>
        
        <p>
            <strong>📈 Limitazioni:</strong> I modelli ML possono produrre risultati imprecisi 
            o incompleti. Lo score di compatibilità è un'approssimazione statistica e non 
            rappresenta un giudizio definitivo sulle competenze dell'utente.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# DELETE MY DATA (GDPR Art. 17 - Right to Erasure)
# =============================================================================

def render_delete_my_data_button():
    """Renders a 'Delete My Data' button that clears all session state."""
    
    st.markdown("""
    <div class="delete-warning">
        <strong>🗑️ Cancella i Miei Dati</strong><br>
        <span style="font-size: 0.9rem; color: #c9d1d9;">
            Questa azione cancellerà immediatamente tutti i dati presenti nella sessione corrente, 
            inclusi CV, analisi, dati del CV Builder e preferenze. L'azione è irreversibile.
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        confirm = st.checkbox("Confermo di voler cancellare tutti i miei dati", key="delete_confirm_checkbox")
        
        if st.button("🗑️ Cancella Tutti i Miei Dati", type="primary", use_container_width=True,
                     disabled=not confirm):
            # Preserve only the page state to avoid crashes
            keys_to_clear = list(st.session_state.keys())
            for key in keys_to_clear:
                if key != "page":
                    del st.session_state[key]
            
            st.success("✅ Tutti i tuoi dati sono stati cancellati con successo. La sessione è stata ripristinata.")
            st.info("ℹ️ Il tuo consenso è stato revocato. Ti verrà richiesto nuovamente all'accesso.")
            st.balloons()


# =============================================================================
# SIDEBAR COMPLIANCE WIDGET
# =============================================================================

def render_sidebar_compliance_badge():
    """Renders a small compliance badge in the sidebar."""
    st.markdown("""
    <div style='margin-top: 1rem; padding: 8px; background: rgba(0, 200, 83, 0.08); 
         border: 1px solid rgba(0, 200, 83, 0.2); border-radius: 8px; text-align: center;'>
        <span style='color: #00C853; font-size: 0.7rem; font-weight: 600;'>
            🔒 GDPR · AI Act Compliant
        </span>
    </div>
    """, unsafe_allow_html=True)
