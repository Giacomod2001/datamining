
from ml_utils import extract_skills_from_text, analyze_gap

cv_text = "Proficient in Looker Studio."
jd_text = "Experience with Tableau is required."

cv_hard, cv_soft = extract_skills_from_text(cv_text)
job_hard, job_soft = extract_skills_from_text(jd_text, is_jd=True)

print(f"CV Hard: {cv_hard}")
print(f"JD Hard: {job_hard}")

result = analyze_gap(cv_text, jd_text)
print(f"Match Result: {result}")
