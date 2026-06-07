"""
================================================================================
CareerMatch AI - Sample data for first-visit demo
================================================================================

Pre-filled text so visitors can land on a page and immediately click
"Analyze" without typing. The samples are intentionally generic --
short, realistic, and aimed at the most common path (Data Analyst -> Data
Scientist). The user can edit or clear them at any time; once edited, the
prefill never overwrites their input again (see `prefill_once`).
================================================================================
"""

from __future__ import annotations

import streamlit as st


# =============================================================================
# HELPER
# =============================================================================

def prefill_once(key: str, value: str) -> None:
    """
    Set `st.session_state[key] = value` only if the key is not yet present.

    Streamlit reads the existing session value when rendering the widget, so
    the field appears pre-filled on first visit. User edits live in the same
    session_state slot, so subsequent visits to the same page keep the user's
    text instead of clobbering it.
    """
    if key not in st.session_state:
        st.session_state[key] = value


# =============================================================================
# SAMPLE TEXTS
# =============================================================================

SAMPLE_DISCOVERY_QUERY = (
    "I'm a recent graduate in economics with strong Excel and SQL skills. "
    "I'd like a remote-friendly job with international clients, ideally "
    "in fintech or consulting. I enjoy data, problem-solving and a fast pace."
)

SAMPLE_CV = """Jane Doe
Milan, Italy | jane.doe@example.com | +39 333 1234567

PROFESSIONAL SUMMARY
Data Analyst with 2+ years of experience turning raw data into business
insights. Strong SQL and Python skills, comfortable building dashboards
in Tableau and Power BI. Eager to grow into a Data Scientist role.

EXPERIENCE
Data Analyst -- Acme Retail, Milan (2023 - present)
- Built weekly KPI dashboards in Tableau used by 40+ store managers.
- Reduced ad-hoc reporting requests by 60% via a self-serve Power BI hub.
- Automated ETL pipelines in Python + Airflow, cutting refresh time from
  4h to 25min.

Junior Analyst -- Beta Insights, Milan (2022 - 2023)
- Analyzed customer churn for a SaaS client; recommendations reduced
  churn 12% in one quarter.
- Wrote SQL queries against a 50M-row Snowflake warehouse.

EDUCATION
MSc in Business Analytics -- Bocconi University (2020 - 2022)
BSc in Economics -- University of Bologna (2017 - 2020)

TECHNICAL SKILLS
- Languages: Python (pandas, scikit-learn), SQL, R
- BI: Tableau, Power BI, Looker
- Cloud / Data: Snowflake, BigQuery, dbt, Airflow
- Other: Git, Jira, A/B testing

LANGUAGES
- Italian (native), English (C1)
"""

SAMPLE_JD = """Data Scientist -- Remote (EU)

About the role
We are looking for a Data Scientist to join our Growth team. You will
own the customer-segmentation roadmap, design experiments, and turn
findings into production-ready models.

Responsibilities
- Build, validate and ship machine-learning models (classification,
  clustering, uplift) using Python and scikit-learn.
- Design and analyze A/B tests; communicate results to product and
  marketing stakeholders.
- Partner with data engineering to maintain feature pipelines (Airflow,
  dbt, Snowflake).
- Mentor junior analysts and contribute to internal best-practice docs.

Requirements
- 3+ years building ML models in a production environment.
- Strong Python (pandas, NumPy, scikit-learn) and advanced SQL.
- Solid statistics: hypothesis testing, regression, causal inference basics.
- Experience with cloud data warehouses (Snowflake / BigQuery / Redshift).
- Excellent communication; able to translate technical findings for
  non-technical audiences.

Nice to have
- Experience with deep-learning frameworks (PyTorch / TensorFlow).
- Familiarity with MLOps tools (MLflow, Vertex AI, SageMaker).
- Prior fintech or SaaS experience.

We offer
- Fully remote within EU time zones.
- Annual learning budget, conference attendance.
- Stock options.
"""

SAMPLE_COVER_LETTER = """Dear Hiring Team,

I'm excited to apply for the Data Scientist position on the Growth team.
Over the past two years as a Data Analyst at Acme Retail, I have moved
from ad-hoc reporting to building production-grade pipelines and
dashboards used daily by 40+ stakeholders.

I am ready to take the next step into modelling work: I have completed
the Coursera ML Specialization, shipped a small churn-prediction project
in Python + scikit-learn, and designed an A/B test framework that
reduced ad-hoc requests by 60%.

I would love to bring this combination of business curiosity and
hands-on engineering to your Growth team.

Best regards,
Jane Doe
"""

SAMPLE_INTERVIEW_ANSWER = (
    "In my previous role at Acme Retail I led the migration of weekly KPI "
    "reporting from Excel to a Tableau dashboard. I started by interviewing "
    "five store managers to understand which KPIs they actually used, then "
    "designed the schema in Snowflake and built the dashboards in Tableau. "
    "Within two months adoption was at 90% of stores and ad-hoc reporting "
    "requests dropped 60%, freeing up roughly one analyst-day per week."
)
