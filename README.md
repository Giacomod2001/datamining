# Job Seeker Helper

## Panoramica

**Job Seeker Helper** è un sistema di analisi automatizzata per la valutazione della compatibilità tra profilo professionale e requisiti lavorativi. Il software implementa algoritmi di text mining per estrarre e confrontare competenze tecniche da documenti testuali, fornendo metriche quantitative di corrispondenza.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Descrizione del Progetto

Il presente applicativo costituisce uno strumento di supporto decisionale per candidati professionali nella fase di job matching. Tramite l'utilizzo di tecniche di Natural Language Processing basate su espressioni regolari, il sistema esegue:

- Estrazione automatica di competenze tecniche da annunci di lavoro
- Parsing delle competenze presenti nel curriculum vitae del candidato
- Calcolo dell'indice di compatibilità percentuale
- Generazione di report analitici sulle competenze possedute e carenti

## Architettura Funzionale

### Componenti Principali

Il sistema è strutturato secondo i seguenti moduli:

1. **Modulo di Estrazione**: Implementazione di pattern matching tramite regex per l'identificazione di oltre 150 keyword tecniche organizzate per categoria (linguaggi di programmazione, framework, strumenti, metodologie)

2. **Modulo di Analisi**: Algoritmo di confronto insiemistico per la determinazione delle competenze in comune e delle lacune formative

3. **Modulo di Presentazione**: Interfaccia utente sviluppata con framework Streamlit per la visualizzazione dei risultati analitici

### Categorie di Competenze Rilevate

Il database interno comprende le seguenti macro-categorie:

- Linguaggi di programmazione (Python, Java, JavaScript, C++, ecc.)
- Framework frontend e backend (React, Angular, Django, Spring, ecc.)
- Sistemi di gestione database (SQL, MongoDB, PostgreSQL, Oracle, ecc.)
- Piattaforme cloud e DevOps (AWS, Azure, Docker, Kubernetes, ecc.)
- Data Science e Machine Learning (TensorFlow, PyTorch, Pandas, ecc.)
- Metodologie di sviluppo (Agile, Scrum, DevOps, TDD, ecc.)
- Soft skills e competenze manageriali

## Requisiti di Sistema

### Prerequisiti

- Python versione 3.8 o superiore
- Package manager pip

### Dipendenze

Le dipendenze del progetto sono specificate nel file `requirements.txt`:

```
streamlit>=1.28.0
```

## Procedura di Installazione

1. Clonare il repository dal sistema di versionamento:

```bash
git clone https://github.com/your-username/job-seeker-helper.git
cd job-seeker-helper
```

2. Installare le dipendenze necessarie:

```bash
pip install -r requirements.txt
```

3. Avviare l'applicazione:

```bash
streamlit run app.py
```

4. Accedere all'interfaccia web attraverso il browser al seguente indirizzo: `http://localhost:8501`

## Modalità d'Uso

### Workflow Operativo

1. **Input Annuncio**: Inserire il testo completo dell'annuncio di lavoro nell'area di testo dedicata
2. **Input Curriculum**: Inserire il curriculum vitae o l'elenco delle competenze possedute nell'apposita sezione
3. **Esecuzione Analisi**: Avviare il processo di matching tramite il pulsante "Analizza Match"
4. **Interpretazione Output**: Consultare i risultati analitici visualizzati

### Componenti dell'Output

Il sistema restituisce le seguenti informazioni:

- **Indice di Compatibilità**: Percentuale di corrispondenza tra requisiti e competenze possedute
- **Progress Indicator**: Rappresentazione grafica del livello di match
- **Valutazione Qualitativa**: Classificazione del profilo (Basso/Medio/Alto)
- **Analisi Dettagliata**: Elenco suddiviso delle competenze possedute e mancanti

## Interpretazione dei Risultati

| Range Percentuale | Classificazione | Interpretazione |
|-------------------|-----------------|------------------|
| 0% - 39% | Match Basso | Discrepanza significativa tra profilo e requisiti. Potenziale profilo junior o requisiti non allineati |
| 40% - 75% | Match Medio | Corrispondenza parziale. Presenza di competenze base con necessità di integrazione |
| 76% - 100% | Match Alto | Elevata compatibilità. Profilo in linea con i requisiti della posizione |

## Stack Tecnologico

- **Backend**: Python 3.8+
- **Framework UI**: Streamlit
- **Text Processing**: Modulo `re` (Regular Expressions) standard library Python
- **Type Hinting**: Typing module per type safety

## Struttura del Repository

```
job-seeker-helper/
├── app.py              # Applicazione principale Streamlit
├── requirements.txt    # Dipendenze Python
├── README.md          # Documentazione tecnica
├── LICENSE            # Termini di licenza MIT
└── .gitignore         # Configurazione Git
```

## Sviluppi Futuri

La roadmap di evoluzione del progetto prevede:

- Estensione del database keyword con categorie settoriali specifiche
- Implementazione funzionalità di export in formato PDF
- Supporto per localizzazione multilingua
- Integrazione con API di piattaforme di recruiting (LinkedIn API, Indeed API)
- Implementazione di algoritmi di Machine Learning per matching avanzato

## Contributi

Il progetto accetta contribuzioni secondo le seguenti modalità:

- Segnalazione di bug tramite issue tracker
- Proposte di enhancement e nuove funzionalità
- Pull request con miglioramenti del codice

Si raccomanda di seguire le best practices di sviluppo Python (PEP 8) e di includere documentazione appropriata.

## Autori e Crediti

Il progetto è stato sviluppato da:

- **Luca Tallarico**
- **Ruben Scoletta**
- **Giacomo Dellacqua**

## Licenza

Il software è distribuito sotto licenza MIT. Per i termini completi della licenza, consultare il file [LICENSE](LICENSE).

---

© 2025 - Job Seeker Helper Project
