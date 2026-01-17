
import ml_utils
import constants
import importlib

# Force reload to get latest constants
importlib.reload(constants)
importlib.reload(ml_utils)

cv_text = """
Autorizzo l’uso dei miei dati personali – d.lgs 196/2003 & GDPR 679/2016
Matteo Politi
Vigevano (PV)
(+39) 3917176008
mapoliti2002@gmail.com
date of birth: 18/07/2002
PROFILE
Master’s student in Energy Engineering with strong quantitative and analytical skills, aiming for a career that
bridges the worlds of finance and energy.
• On going thesis in data-driven forecasting (Python, predictive models for the balancing Italian
market)
• Solid background in energy economics, thermodynamics, aerospace propulsion
• Strong interpersonal skills, proven resilience and effective time management (balancing a 3.5 hours
daily commute with full-time studies at Italy’s top technical university)
EDUCATION
 09/2024 – 07/2026 MSc in Energy Engineering Milano (MI)
Politecnico di Milano
• Balancing Market Quantitative Analysis (developing a predictive model on Python based on
ENTSO-E, TERNA, GME datasets for RES/demand variations to forecast BM’s volumes and
prices). Ongoing, but open to changes for possible collaborations in the trading field.
09/2021 - 07/2024 BSc in Aerospace Engineering Milano (MI)
Politecnico di Milano
• “Analysis and Design of the PW123AF Propulsion System” – cycle reconstruction, NASA CEA
combustion simulations, energy efficiency improvement
09/2016 - 06/2021 High school Diploma – Scientific Lyceum Vigevano (PV)
Liceo Scientifico Caramuel
• Awarded a merit scholarship from the Lombardy Region. Final grade: 100/100 cum
laude
PROJECTS
• Energy Conversion (optimization of the evaporation temperature of a Heat Recovery Steam Cycle
through Excel modeling);
• RES Scenario Modeling (group project simulating Algerian energy transition on Hypatia framework: the
group acted as external advisor for the local policy makers);
• Enterpreneurship: launched and managed a profitable online reselling business during my bachelor’s
years (vintage clothing and collectibles), developing negotiation and investment skills.
SKILLS

• Technical: Python (on going), MATLAB, Excel (advanced), Hypatia;
• Languages: Italian (native), English (C1 IELTS);
• Soft skills: Analytical mindset, stakeholder engagement, adaptability, leadership in group work.
INTERESTS
• Running and hiking | investing and personal finance | Enterpreneurship
"""

# Simulate a typical Energy Engineer JD
jd_text = """
Energy Engineer position.
We are looking for a candidate with a degree in Energy Engineering.
Required skills:
- Python and MATLAB for data analysis.
- Knowledge of Energy Markets and Trading.
- Experience with forecasting and predictive models.
- Thermodynamics and Energy Efficiency.
- Excel modeling.
"""

print("--- ANALYZING CV SKILLS ---")
cv_skills = ml_utils.extract_skills(cv_text)
print("Extracted CV Skills:", cv_skills)

print("\n--- ANALYZING JD SKILLS ---")
jd_skills = ml_utils.extract_skills(jd_text)
print("Extracted JD Skills:", jd_skills)

print("\n--- GAP ANALYSIS ---")
gap = ml_utils.analyze_gap(cv_text, jd_text)
print("Match Score:", gap['match_percentage'])
print("Matching Skills:", gap['matching_hard'])
print("Missing Skills:", gap['missing_hard'])
