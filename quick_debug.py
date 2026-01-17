from ml_utils import extract_skills_from_text, analyze_gap
import constants

print("KB Visualization Keys:", [k for k in constants.HARD_SKILLS.keys() if "Visualization" in k])
print("KB Tableau Keys:", [k for k in constants.HARD_SKILLS.keys() if "Tableau" in k])

cv_text = "Experienced in Looker Studio and creating dashboards."
jd_text = "Must have experience with Tableau and Data Visualization."

hard, soft = extract_skills_from_text(cv_text)
print(f"CV Extracted: {hard}")

hard_jd, soft_jd = extract_skills_from_text(jd_text, is_jd=True)
print(f"JD Extracted: {hard_jd}")

gap = analyze_gap(cv_text, jd_text)
print("Gap Analysis Result:")
print(f"Match %: {gap['match_percentage']}")
print(f"Matching: {gap['matching_hard']}")
print(f"Transferable: {gap.get('transferable')}")
print(f"Missing: {gap['missing_hard']}")
