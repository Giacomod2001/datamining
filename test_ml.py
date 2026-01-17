import ml_utils
import constants
import knowledge_base

cv = "I have experience with Python and SQL. I am a Data Analyst."
jd = "Looking for a Data Scientist with Python, SQL and Machine Learning."

res = ml_utils.analyze_gap(cv, jd)
print(f"Match: {res['match_percentage']}%")
print(f"Matched: {res['matching_hard']}")
print(f"Missing: {res['missing_hard']}")
print(f"Transferable: {res['transferable']}")
