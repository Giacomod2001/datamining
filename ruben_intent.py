"""
================================================================================
CareerMatch AI - Ruben Intent Classifier (M3)
================================================================================

Replaces the chain of `if any(kw in msg.lower() for kw in [...])` blocks in
ml_utils.get_chatbot_response with a small TF-IDF + cosine-similarity intent
classifier. Pure-Python, local, free, ~50ms after the first call.

Why this is better than keyword matching:
- Handles paraphrases ("how do I get a job?" -> job_search, even without the
  literal word "find").
- Multilingual without a separate vocabulary: we use character n-grams (3-5)
  so accents / inflections / declensions in IT, ES, FR, DE, PT are captured.
- Picks the *best* intent instead of the first matching keyword, which
  removes order-dependent bugs from the original chain.

Public API:
- classify_intent(message)          -> (intent, confidence) or (None, 0.0)
- get_intent_response(intent, lang) -> str or None
- CONFIDENCE_THRESHOLD              -> module-level constant
- INTENT_RESPONSES                  -> {intent: {lang: str}}

Caching: the underlying vectorizer + prototype matrix are built once via
streamlit.cache_resource (with a graceful no-op fallback when imported
outside a Streamlit context, e.g. in the pytest suite).
================================================================================
"""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =============================================================================
# CACHING SHIM
# =============================================================================
# We want @st.cache_resource in production (so the vectorizer is built once),
# but also tolerate the module being imported in a plain Python context
# (pytest, ad-hoc scripts) where Streamlit isn't running.

try:
    import streamlit as _st

    def _cache_resource(fn):
        return _st.cache_resource(show_spinner=False)(fn)
except Exception:  # pragma: no cover -- streamlit always installed in prod
    def _cache_resource(fn):
        cached = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cached:
                cached[key] = fn(*args, **kwargs)
            return cached[key]

        return wrapper


CONFIDENCE_THRESHOLD = 0.40
# Tuned empirically:
#   - real intent queries ("how do I prepare for an interview", "tips for cv")
#     score 0.5-1.0
#   - generic openers ("how does it work", "what is this", "how to") score 0.3-0.4,
#     so they fall back to page context instead of grabbing a wrong intent
#   - direct keywords ("hello", "thanks", "salary") score ~1.0


# =============================================================================
# INTENT PROTOTYPES (multilingual)
# =============================================================================
# Hand-curated short phrases per intent across EN, IT, ES, FR, DE, PT.
# The classifier learns to discriminate between intents based on these.

INTENT_PROTOTYPES: dict[str, list[str]] = {
    "greeting": [
        "hello", "hi there", "hey", "good morning", "good afternoon", "who are you",
        "ciao", "salve", "buongiorno", "buonasera", "chi sei",
        "hola", "buenos dias", "buenas tardes", "quien eres",
        "bonjour", "salut", "bonsoir", "qui es tu",
        "hallo", "guten tag", "guten morgen", "wer bist du",
        "ola", "oi", "bom dia", "boa tarde", "quem es",
    ],
    "thanks": [
        "thanks", "thank you", "thanks a lot", "thanks for the help", "appreciated",
        "grazie", "grazie mille", "ti ringrazio",
        "gracias", "muchas gracias",
        "merci", "merci beaucoup",
        "danke", "vielen dank",
        "obrigado", "obrigada", "muito obrigado",
    ],
    "interview": [
        "how do I prepare for an interview", "interview tips", "behavioral questions",
        "technical interview preparation", "I'm nervous about my interview",
        "what should I expect in an interview", "system design questions",
        "come prepararsi a un colloquio", "consigli per il colloquio", "colloquio tecnico",
        "domande comportamentali", "sono nervoso per il colloquio",
        "como preparar una entrevista", "consejos entrevista", "preguntas de comportamiento",
        "comment preparer un entretien", "conseils entretien", "questions comportementales",
        "wie bereite ich mich auf ein vorstellungsgesprach vor", "tipps vorstellungsgesprach",
        "como preparar uma entrevista", "dicas entrevista", "perguntas comportamentais",
    ],
    "data_science": [
        "data science career", "how to become a data scientist", "machine learning roles",
        "deep learning jobs", "ai engineer", "neural networks", "nlp engineer",
        "computer vision careers", "mlops",
        "carriera data science", "diventare data scientist", "ingegnere machine learning",
        "carrera data science", "ser cientifico de datos", "ingeniero machine learning",
        "carriere data science", "devenir data scientist", "ingenieur machine learning",
        "data science karriere", "data scientist werden", "ml ingenieur",
        "carreira data science", "ser cientista de dados", "engenheiro machine learning",
    ],
    "cloud": [
        "cloud data jobs", "aws career", "snowflake roles", "databricks", "azure data",
        "data engineering pipelines", "etl elt", "spark big data",
        "lavoro cloud data", "carriera aws", "ruoli snowflake", "pipeline dati",
        "trabajo cloud", "carrera aws", "ingenieria de datos",
        "emploi cloud", "carriere aws", "pipelines de donnees",
        "cloud data karriere", "aws karriere", "data engineering",
        "trabalho cloud", "carreira aws", "pipelines de dados",
    ],
    "salary": [
        "how much does a data scientist make", "salary range", "compensation",
        "what's the pay", "salary negotiation", "how to negotiate offer",
        "quanto guadagna un data scientist", "stipendio data analyst", "negoziare stipendio",
        "cuanto gana", "salario data scientist", "negociar salario",
        "combien gagne", "salaire data scientist", "negocier salaire",
        "wie viel verdient", "gehalt data scientist", "gehalt verhandeln",
        "quanto ganha", "salario data scientist", "negociar salario",
    ],
    "skills": [
        "what skills should I learn", "best courses for data", "certifications worth it",
        "how to improve my profile", "what to study to become data scientist",
        "cosa devo studiare", "quali skill servono", "corsi consigliati", "certificazioni utili",
        "que habilidades aprender", "mejores cursos", "certificaciones",
        "quelles competences apprendre", "meilleurs cours", "certifications",
        "welche fahigkeiten lernen", "beste kurse", "zertifizierungen",
        "que habilidades aprender", "melhores cursos", "certificacoes",
    ],
    "resume": [
        "how to write my cv", "resume tips", "ats friendly cv", "cv format",
        "what to put on my resume", "should I include this on my cv",
        "come scrivere il cv", "consigli per il curriculum", "formato cv", "cv ats",
        "como hacer cv", "formato cv", "consejos curriculum",
        "comment ecrire un cv", "conseils cv", "format cv",
        "wie schreibe ich einen lebenslauf", "lebenslauf tipps", "ats lebenslauf",
        "como escrever cv", "dicas curriculo", "formato curriculo",
    ],
    "career_change": [
        "i want to change career", "switch to data", "transition from another field",
        "moving from finance to tech", "break into data science",
        "cambiare carriera", "passare al data", "transizione carriera", "diventare data analyst",
        "cambiar de carrera", "transicion a data", "cambio profesional",
        "changer de carriere", "transition vers la data",
        "karriere wechseln", "umstieg in data",
        "mudar de carreira", "transicao para data",
    ],
    "remote": [
        "remote jobs", "work from home", "hybrid work", "remote first",
        "lavoro da remoto", "lavoro da casa", "smart working", "ibrido",
        "trabajo remoto", "teletrabajo", "hibrido",
        "teletravail", "travail a distance", "hybride",
        "remote arbeit", "homeoffice", "hybrid",
        "trabalho remoto", "trabalho de casa", "hibrido",
    ],
    "networking": [
        "linkedin networking", "how to network", "build connections", "referrals",
        "should I reach out", "networking message",
        "fare networking", "linkedin", "contatti professionali", "referral",
        "como hacer networking", "linkedin", "referidos",
        "comment reseauter", "reseautage linkedin", "parrainage",
        "wie netzwerken", "linkedin", "empfehlungen",
        "como fazer networking", "linkedin", "indicacoes",
    ],
    "cover_letter": [
        "cover letter help", "how to write cover letter", "motivation letter",
        "lettera motivazionale", "lettera di presentazione", "come scrivere lettera",
        "carta de presentacion", "carta motivacion",
        "lettre de motivation", "lettre presentation",
        "anschreiben", "motivationsschreiben",
        "carta de apresentacao", "carta motivacao",
    ],
    "job_search": [
        "find a job", "looking for work", "job hunting", "where to apply",
        "best job boards", "how do I land a job",
        "trovare lavoro", "cercare lavoro", "dove candidarsi", "bacheche di lavoro",
        "buscar trabajo", "donde postular", "portales de empleo",
        "trouver un emploi", "ou postuler", "sites emploi",
        "job suchen", "stellensuche", "wo bewerben",
        "procurar emprego", "onde candidatar", "sites emprego",
    ],
    "help": [
        "what can you do", "help me", "what services", "what are you for",
        "how can you help me", "what is this app",
        "cosa puoi fare", "aiuto", "cosa fai", "a cosa servi", "come puoi aiutarmi",
        "que puedes hacer", "ayuda", "como me ayudas",
        "que peux tu faire", "aide", "comment peux tu m aider",
        "was kannst du tun", "hilfe", "wie kannst du helfen",
        "o que voce pode fazer", "ajuda", "como pode me ajudar",
    ],
    "why": [
        "why sql", "why python", "why this approach", "explain why",
        "perche sql", "perche python", "spiega perche",
        "por que sql", "por que python", "explica por que",
        "pourquoi sql", "pourquoi python", "explique pourquoi",
        "warum sql", "warum python", "erklare warum",
        "por que sql", "por que python", "explique por que",
    ],
}


# =============================================================================
# CLASSIFIER
# =============================================================================

@_cache_resource
def _build_classifier():
    """Train the TF-IDF char-ngram classifier on the prototype phrases."""
    intents: list[str] = []
    texts: list[str] = []
    for intent, prototypes in INTENT_PROTOTYPES.items():
        for phrase in prototypes:
            intents.append(intent)
            texts.append(phrase.lower())

    vectorizer = TfidfVectorizer(
        analyzer="char_wb",       # character n-grams within word boundaries
        ngram_range=(3, 5),       # captures roots across languages
        min_df=1,
        sublinear_tf=True,
        norm="l2",
    )
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix, intents


# Greeting / thanks short-circuit. When the message opens with one of these
# tokens we don't need the classifier -- this matches the original behaviour
# where a "Hello, can you help me?" was treated as a greeting before falling
# into the help branch. Without it, TF-IDF gives more weight to the longer
# tail of the sentence and misclassifies. Lower-cased, no accents stripped:
# char_wb ngrams already absorb accented forms via "olá" / "ola" overlap.
_GREETING_PREFIXES = (
    "hello", "hi ", "hi,", "hi!", "hey", "good morning", "good afternoon",
    "ciao", "salve", "buongiorno", "buonasera",
    "hola", "buenos", "buenas",
    "bonjour", "salut", "bonsoir",
    "hallo", "guten ",
    "ola", "ola,", "ola!", "oi", "oi,", "oi!", "ola ", "olá", "bom dia", "boa tarde", "boa noite",
)

_THANKS_PREFIXES = (
    "thanks", "thank you", "grazie", "gracias", "merci", "danke", "obrigado", "obrigada",
)


def classify_intent(message: str) -> Tuple[Optional[str], float]:
    """
    Classify a free-form user message into one of INTENT_PROTOTYPES.

    Returns (intent_name, max_aggregate_similarity). When no intent reaches
    CONFIDENCE_THRESHOLD the caller is expected to fall back to a generic
    page-based response.
    """
    if not message or not message.strip():
        return None, 0.0

    msg_lower = message.lower().lstrip()
    if any(msg_lower.startswith(p) for p in _GREETING_PREFIXES):
        return "greeting", 1.0
    if any(msg_lower.startswith(p) for p in _THANKS_PREFIXES):
        return "thanks", 1.0

    vectorizer, matrix, intents = _build_classifier()
    query_vec = vectorizer.transform([message.lower()])
    sims = cosine_similarity(query_vec, matrix).ravel()  # shape: (n_prototypes,)

    # Aggregate similarities per intent. We use the *max* over an intent's
    # prototypes -- a single strong match should win, but multiple weak
    # matches shouldn't accumulate falsely.
    best_intent = None
    best_score = 0.0
    for intent in set(intents):
        idx = [i for i, x in enumerate(intents) if x == intent]
        score = float(np.max(sims[idx]))
        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent, best_score


# =============================================================================
# INTENT RESPONSES (multilingual)
# =============================================================================
# Each intent maps to a per-language response. Pulled from the legacy
# in-function dicts in ml_utils.get_chatbot_response so that file becomes
# significantly shorter after M3.

INTENT_RESPONSES: dict[str, dict[str, str]] = {
    "greeting": {
        "en": "Hello. I am Ruben, a professional career consultant. I am here to help you optimize your career strategy.",
        "it": "Ciao. Sono Ruben, un consulente di carriera professionale. Sono qui per aiutarti a ottimizzare la tua strategia lavorativa.",
        "es": "Hola. Soy Ruben, un consultor profesional. Estoy aqui para ayudarte a optimizar tu estrategia de carrera.",
        "fr": "Bonjour. Je suis Ruben, un consultant professionnel. Je suis ici pour optimiser votre strategie de carriere.",
        "de": "Hallo. Ich bin Ruben, ein professioneller Karriereberater. Ich bin hier, um Ihre Karrierestrategie zu optimieren.",
        "pt": "Ola. Sou Ruben, um consultor profissional. Estou aqui para otimizar sua estrategia de carreira.",
    },
    "thanks": {
        "en": "You're welcome! Let me know if you need anything else. I'm here to help with your career journey.",
        "it": "Prego! Fammi sapere se hai bisogno di altro. Sono qui per aiutarti nel tuo percorso di carriera.",
        "es": "De nada! Avisame si necesitas algo mas. Estoy aqui para ayudarte en tu carrera.",
        "fr": "Je vous en prie! N'hesitez pas si vous avez d'autres questions. Je suis la pour vous aider.",
        "de": "Gern geschehen! Lassen Sie mich wissen, wenn Sie weitere Hilfe benotigen.",
        "pt": "De nada! Me avise se precisar de mais alguma coisa.",
    },
    "interview": {
        "en": "For technical interviews (Data/ML), prepare for: 1) Live Coding (SQL/Python). 2) ML Case Studies (explain bias-variance trade-off). 3) System Design (scaling data pipelines). Use the STAR method for behavioral questions. Would you like specific tips for a particular role (e.g., Data Architect)?",
        "it": "Per i colloqui tecnici (Data/ML), preparati su: 1) Live Coding (SQL/Python). 2) ML Case Studies (spiega il bias-variance trade-off). 3) System Design (scalabilita delle pipeline dati). Usa il metodo STAR per le domande comportamentali. Vuoi consigli specifici per un ruolo (es. Data Architect)?",
        "es": "Para entrevistas tecnicas (Data/ML): 1) Live Coding (SQL/Python). 2) Casos de ML (sesgo-varianza). 3) Diseno de sistemas. Usa el metodo STAR. Quieres consejos para un rol especifico?",
        "fr": "Pour les entretiens techniques: 1) Live Coding (SQL/Python). 2) Cas d'etudes ML. 3) System Design. Utilisez la methode STAR. Voulez-vous des conseils pour un role specifique?",
        "de": "Fur technische Interviews: 1) Live Coding. 2) ML-Fallstudien. 3) Systemdesign. Verwenden Sie die STAR-Methode.",
        "pt": "Para entrevistas tecnicas: 1) Live Coding. 2) Casos de ML. 3) Design de sistemas. Use o metodo STAR.",
    },
    "data_science": {
        "en": "In Data Science/ML, mastery of the lifecycle is key: EDA -> Feature Eng -> Model Selection -> Evaluation (Precision/Recall/F1) -> Deployment. Mention experience with MLflow, DVC, or Airflow. Are you focusing on MLOps or Research?",
        "it": "In Data Science/ML, la padronanza del lifecycle e fondamentale: EDA -> Feature Eng -> Model Selection -> Evaluation (Precision/Recall/F1) -> Deployment. Menziona l'esperienza con MLflow, DVC o Airflow. Ti stai concentrando su MLOps o Research?",
        "es": "En Data Science/ML, domina el ciclo de vida: EDA, Ingenieria de Features, Seleccion de Modelo, Evaluacion y Deployment. Menciona MLflow o Airflow.",
        "fr": "En Data Science/ML: EDA, Feature Engineering, Selection de modele, Evaluation et Deployment. Mentionnez MLflow ou Airflow.",
        "de": "In Data Science/ML: EDA, Feature Engineering, Modellauswahl, Evaluierung und Deployment.",
        "pt": "Em Data Science/ML: EDA, Feature Engineering, Selecao de Modelo, Avaliacao e Deployment.",
    },
    "cloud": {
        "en": "For Cloud Data roles: 1) Focus on partitioning and clustering (Snowflake/Databricks). 2) Understand CI/CD for data (Terraform). 3) Know the difference between ETL and ELT. Mention cloud certifications if you have them. Need advice on a specific cloud provider?",
        "it": "Per ruoli Cloud Data: 1) Concentrati su partitioning e clustering (Snowflake/Databricks). 2) Comprendi la CI/CD per i dati (Terraform). 3) Conosci la differenza tra ETL ed ELT. Menziona le certificazioni cloud se le hai. Vuoi consigli su un provider specifico?",
        "es": "Para roles Cloud Data: 1) Enfocate en partitioning y clustering. 2) Entiende CI/CD (Terraform). 3) ETL vs ELT. Menciona certificaciones cloud.",
        "fr": "Pour les roles Cloud Data: 1) Partitioning et clustering. 2) CI/CD (Terraform). 3) ETL vs ELT.",
        "de": "Fur Cloud Data Rollen: 1) Partitionierung und Clustering. 2) CI/CD (Terraform). 3) ETL vs ELT.",
        "pt": "Para funcoes Cloud Data: 1) Partitioning e clustering. 2) CI/CD (Terraform). 3) ETL vs ELT.",
    },
    "salary": {
        "en": "Salary for Data roles varies significantly by location and seniority. For a Senior Data Scientist in EU, ranges often fall between €65k-€95k. In the US, it's $130k-$190k+. Always check 'levels.fyi' for the latest tech benchmarks. Ready to negotiate that offer?",
        "it": "Lo stipendio per i ruoli Data varia per location e seniority. Un Senior Data Scientist in Italia/EU varia spesso tra 50k-75k€, mentre all'estero (ES/DE/UK) e sensibilmente piu alto. Controlla 'levels.fyi' per benchmarks tech reali. Vuoi aiuto per negoziare?",
        "es": "El salario para roles Data varia segun ubicacion. Un Senior Data Scientist en la UE suele estar entre 60k€-90k€. En EE.UU. es de $130k-$190k+. Consulta 'levels.fyi'.",
        "fr": "Le salaire pour les roles Data varie par lieu. Un Senior Data Scientist en UE se situe entre 60k€-95k€. Consultez 'levels.fyi'.",
        "de": "Gehalter fur Data Rollen variieren. Ein Senior Data Scientist in der EU liegt oft zwischen 70k€-100k€.",
        "pt": "Salario para funcoes Data varia por local. Um Senior Data Scientist na UE esta entre 60k€-90k€.",
    },
    "skills": {
        "en": "To boost your career profile, I recommend: 1) Master Python/SQL (mandatory). 2) Learn a BI tool (Tableau/PowerBI). 3) Build 3 distinct projects (one Kaggle, one End-to-End, one Dashboard). 4) Get the AWS Cloud Practitioner or GCP Data Engineer cert. Which domain interests you most?",
        "it": "Per potenziare il profilo, consiglio: 1) Padroneggia Python/SQL (obbligatorio). 2) Impara uno strumento di BI (Tableau/PowerBI). 3) Costruisci 3 progetti distinti (uno Kaggle, uno End-to-End, una Dashboard). 4) Prendi una certificazione AWS o GCP. Quale dominio ti interessa di piu?",
        "es": "Para mejorar el perfil: 1) Domina Python/SQL. 2) Aprende una herramienta BI. 3) Crea 3 proyectos distintos. 4) Obten certificacion AWS o GCP.",
        "fr": "Pour booster votre profil: 1) Maitrisez Python/SQL. 2) Apprenez un outil BI. 3) Creez 3 projets. 4) Obtenez une certif AWS ou GCP.",
        "de": "Profil verbessern: 1) Python/SQL beherrschen. 2) BI-Tool lernen. 3) 3 Projekte erstellen. 4) AWS/GCP Zertifizierung.",
        "pt": "Para melhorar o perfil: 1) Domine Python/SQL. 2) Aprenda uma ferramenta BI. 3) Crie 3 projetos. 4) Certificacao AWS ou GCP.",
    },
    "resume": {
        "en": "For Data CVs: 1) Use the 'Reverse Chronological' format. 2) The 'Skill' section must be near the top. 3) Quantify! Use: 'Optimized SQL queries, reducing latency by 40%'. 4) Include a GitHub/Portfolio link. 5) Mention specific tech stacks (e.g., PyTorch, Spark, K8s). Would you like to check your CV for ATS compliance?",
        "it": "Per i CV Data: 1) Usa il formato 'Reverse Chronological'. 2) La sezione 'Skill' deve essere in alto. 3) Quantifica! Es: 'Ottimizzato query SQL riducendo la latenza del 40%'. 4) Includi GitHub/Portfolio. 5) Menziona stack specifici (es. PyTorch, Spark). Vuoi controllare la conformita ATS?",
        "es": "Para CV de Data: 1) Formato cronologico inverso. 2) Habilidades arriba. 3) Cuantifica logros (ej: reduje latencia 40%). 4) Enlace a GitHub. 5) Menciona stacks tecnicos.",
        "fr": "Pour un CV Data: 1) Format chronologique inverse. 2) Competences en haut. 3) Quantifiez (ex: reduction latence 40%). 4) Lien GitHub. 5) Stack technique.",
        "de": "Fur Data CVs: 1) Umgekehrt chronologisches Format. 2) Fahigkeiten oben. 3) Erfolge quantifizieren. 4) GitHub-Link.",
        "pt": "Para CVs de Data: 1) Formato cronologico inverso. 2) Habilidades no topo. 3) Quantifique conquistas. 4) Link do GitHub.",
    },
    "career_change": {
        "en": "Breaking into Data from another field? 1) Pivot to 'Data Analyst' first (it's the softest entry point). 2) Learn SQL -- it's the universal language. 3) Leverage your domain knowledge (e.g., Finance domain knowledge + SQL is a powerhouse). Are you switching from a non-tech background?",
        "it": "Entrare nel mondo Data da un altro settore? 1) Punta al ruolo di 'Data Analyst' come primo passo (e il punto d'ingresso piu accessibile). 2) Impara SQL: e il linguaggio universale dei dati. 3) Sfrutta la tua conoscenza di dominio (es. Finance + SQL = combinazione letale). Vieni da un background non-tech?",
        "es": "Entrar en Data desde otro campo? 1) Empieza como 'Data Analyst'. 2) Aprende SQL. 3) Usa tu conocimiento de dominio. Vienes de un campo no tecnico?",
        "fr": "Passer a la Data? 1) Visez 'Data Analyst' en premier. 2) Apprenez SQL. 3) Utilisez votre expertise metier.",
        "de": "In Data Bereich wechseln? 1) Zuerst 'Data Analyst' anstreben. 2) SQL lernen. 3) Fachwissen nutzen.",
        "pt": "Mudar para Data? 1) Foque em 'Data Analyst' primeiro. 2) Aprenda SQL. 3) Use seu conhecimento de dominio.",
    },
    "remote": {
        "en": "Remote work is the standard for Data roles. Tips: 1) Prove you can work with cloud-native tools (Databricks, Snowflake). 2) Highlight 'Async Communication' in your CV. 3) Look for 'Remote-First' companies (GitLab, Zapier, Shopify). Want to filter jobs by remote status in Career Discovery?",
        "it": "Il lavoro remoto e lo standard per i ruoli Data. Consigli: 1) Dimostra di saper usare tool cloud-native (Databricks, Snowflake). 2) Evidenzia la 'Comunicazione Asincrona' nel CV. 3) Cerca aziende 'Remote-First' (GitLab, Shopify). Vuoi filtrare per ruoli remoti in Career Discovery?",
        "es": "El trabajo remoto es estandar en Data. 1) Usa herramientas cloud. 2) Destaca comunicacion asincrona. 3) Busca empresas 'Remote-First'.",
        "fr": "Le teletravail est la norme en Data. 1) Outils cloud-native. 2) Communication asynchrone. 3) Entreprises 'Remote-First'.",
        "de": "Remote-Arbeit ist Standard in Data Rollen. Cloud-native Tools nutzen, asynchrone Kommunikation hervorheben.",
        "pt": "Trabalho remoto e o padrao em funcoes Data. 1) Ferramentas cloud-native. 2) Comunicacao assincrona. 3) Empresas 'Remote-First'.",
    },
    "networking": {
        "en": "For Data Scientists, LinkedIn networking is vital. Follow industry leaders (Cassie Kozyrkov, Andrew Ng). Engage with the #DataScience community. 40% of tech hires come from referrals -- don't just apply, talk to the hiring team first. Need a networking message template?",
        "it": "Per i Data Scientist, il networking su LinkedIn e vitale. Segui i leader del settore (Andrew Ng, ecc.). Partecipa alla community #DataScience. Il 40% delle assunzioni tech arriva da referral: non solo candidarti, parla prima con il team. Ti serve un template per il messaggio?",
        "es": "Networking en LinkedIn es vital. Sigue a lideres industriales. El 40% de contrataciones son por referidos. Quieres un mensaje tipo?",
        "fr": "Le reseautage LinkedIn est vital. Suivez les leaders. 40% des embauches tech via parrainage.",
        "de": "LinkedIn Networking ist wichtig. Folgen Sie Branchenfuhrern. 40% der Tech-Einstellungen durch Empfehlungen.",
        "pt": "Networking no LinkedIn e vital. Siga lideres da industria. 40% das contratacoes tech via indicacao.",
    },
    "cover_letter": {
        "en": "Data Cover Letters should be concise: 1) Paragraph 1: Why this specific dataset/problem interests you. 2) Paragraph 2: A concrete example of a project where you delivered value. 3) Paragraph 3: Cultural fit. Keep it under 250 words. Shall we analyze your draft in CV Evaluation?",
        "it": "Le lettere motivazionali per ruoli Data devono essere concise: 1) Paragrafo 1: Perche quel dataset/problema specifico ti interessa. 2) Paragrafo 2: Esempio concreto di un progetto di valore. 3) Paragrafo 3: Fit culturale. Resta sotto le 250 parole. Analizziamo la bozza in CV Evaluation?",
        "es": "Cartas de presentacion breves: 1) Por que te interesa este problema. 2) Ejemplo concreto de valor. 3) Fit cultural. Menos de 250 palabras.",
        "fr": "Lettres de motivation concises: 1) Pourquoi ce probleme vous interesse. 2) Exemple concret de valeur. Sous 250 mots.",
        "de": "Data Anschreiben kurz halten: 1) Warum dieses Problem? 2) Konkretes Beispiel. 3) Fit. Unter 250 Worter.",
        "pt": "Cartas de apresentacao concisas: 1) Por que este problema lhe interessa. 2) Exemplo concreto de valor. Menos de 250 palavras.",
    },
    "job_search": {
        "en": "The best Data jobs aren't just on LinkedIn. Check: 1) Otta (for high-growth startups). 2) Wellfound/AngelList. 3) Specific tech job boards (Hacker News Who's Hiring). 4) Use 'LinkedIn Boomerang' strategy: reach out to peers at the company first. Ready to scale your job hunt?",
        "it": "I migliori lavori Data non sono solo su LinkedIn. Controlla: 1) Otta (per startup high-growth). 2) Wellfound/AngelList. 3) Bacheche tech specifiche (Hacker News). 4) Strategia 'LinkedIn Boomerang': contatta prima i peer in azienda. Pronto ad accelerare?",
        "es": "Mejores trabajos de Data: 1) Otta. 2) Wellfound. 3) Hacker News. 4) Contacta primero con pares en la empresa.",
        "fr": "Meilleurs jobs Data: 1) Otta. 2) Wellfound. 3) Hacker News.",
        "de": "Beste Data Jobs: 1) Otta. 2) Wellfound. 3) Hacker News.",
        "pt": "Melhores empregos Data: 1) Otta. 2) Wellfound. 3) Hacker News.",
    },
    "help": {
        "en": "I am Ruben, your Technical Career Strategist. I specialize in Data Science, Cloud, and Engineering careers. Ask me about: 1) Niche tech stacks. 2) MLOps workflows. 3) Tech industry benchmarks. 4) Salary and negotiation in the Data space. 5) Portfolio building. How can I steer your technical career today?",
        "it": "Sono Ruben, il tuo Technical Career Strategist. Sono specializzato in carriere Data Science, Cloud ed Engineering. Chiedimi di: 1) Niche tech stacks. 2) Workflows MLOps. 3) Benchmark del settore tech. 4) Stipendio e negoziazione spazio Data. 5) Portfolio building. Come posso guidare la tua carriera tecnica oggi?",
        "es": "Soy Ruben, Technical Career Strategist. Especialista en Data Science y Cloud. Preguntame sobre tech stacks, MLOps, salarios y portfolio.",
        "fr": "Je suis Ruben, Technical Career Strategist. Specialiste Data Science et Cloud.",
        "de": "Ich bin Ruben, Technical Career Strategist. Spezialist fur Data Science und Cloud.",
        "pt": "Sou Ruben, Technical Career Strategist. Especialista em Data Science e Cloud.",
    },
    "why": {
        "en": "Technical career choices require deep context. Why focus on SQL? Because it's the 90% of data work. Why MLOps? Because models that don't deploy deliver zero value. Give me a specific topic and I'll explain the 'Data Logic' behind it.",
        "it": "Le scelte di carriera tecnica richiedono contesto. Perche focus su SQL? Perche e il 90% del lavoro sui dati. Perche MLOps? Perche i modelli che non scalano non valgono nulla. Dimmi un argomento e ti spieghero la 'Logica dei Dati' dietro di esso.",
        "es": "Elegir una carrera tecnica requiere contexto. Por que SQL? Es el 90% del trabajo. MLOps? Los modelos sin despliegue no valen nada.",
        "fr": "Les choix de carriere technique necessitent du contexte. Pourquoi SQL? C'est 90% du travail.",
        "de": "Technische Karrierewahl erfordert Kontext. Warum SQL? Es sind 90% der Arbeit.",
        "pt": "Escolhas de carreira tecnica exigem contexto. Por que SQL? E 90% do trabalho.",
    },
}


def get_intent_response(intent: str, lang: str) -> Optional[str]:
    """Return the canned response for an intent in the requested language."""
    resp_dict = INTENT_RESPONSES.get(intent)
    if not resp_dict:
        return None
    return resp_dict.get(lang) or resp_dict.get("en")


def fallback_response(message: str, lang: str) -> str:
    """Generic, tech-flavoured fallback when no intent passes the threshold."""
    snippet = (message or "")[:40]
    fallback = {
        "en": f"Interesting query about '{snippet}...'. As a Technical Strategist, I see this through the lens of data-driven careers. I can pivot to: technical interview hacks, cloud certification paths, or high-growth data roles. What's your priority?",
        "it": f"Domanda interessante su '{snippet}...'. Come Technical Strategist, la inquadro nella prospettiva delle carriere data-driven. Possiamo parlare di: interview hacks tecnici, percorsi cert cloud, o ruoli data ad alta crescita. Qual e la tua priorita?",
        "es": f"Consulta interesante sobre '{snippet}...'. Hablemos de hacks para entrevistas tecnicas, certificaciones cloud o roles de alta demanda.",
        "fr": f"Question interessante sur '{snippet}...'. Parlons de hacks d'entretien, certifs cloud ou roles a forte croissance.",
        "de": f"Interessante Frage zu '{snippet}...'. Reden wir uber technische Interviews, Cloud-Zertifizierungen oder gefragte Rollen.",
        "pt": f"Consulta interessante sobre '{snippet}...'. Falemos sobre entrevistas tecnicas, certificacoes cloud ou funcoes de alta demanda.",
    }
    return fallback.get(lang, fallback["en"])
