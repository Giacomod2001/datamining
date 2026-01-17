
from ml_utils import analyze_gap
import json

cv_text = """
Master’s student in Energy Engineering with strong quantitative and analytical skills.
Thesis in data-driven forecasting (Python, predictive models).
MATLAB, Excel (advanced), Hypatia.
Vigevano (PV). Politecnico di Milano.
"""

# Case 1: Just the title
print("--- Case 1: Just 'energy engineer' ---")
res1 = analyze_gap(cv_text, "energy engineer")
print(f"Match: {res1['match_percentage']}%")
print(f"Matched: {res1['matching_hard']}")
print(f"Missing: {res1['missing_hard']}")
print(f"Transferable: {res1['transferable'].keys()}")
print("-" * 30)

# Case 2: Full JD
print("\n--- Case 2: Actual Energy Engineering description ---")
jd_text = "Looking for an Energy Engineer expert in Thermodynamics, Power Systems and Python."
res2 = analyze_gap(cv_text, jd_text)
print(f"Match: {res2['match_percentage']}%")
print(f"Matched: {res2['matching_hard']}")
print(f"Missing: {res2['missing_hard']}")
print("-" * 30)
