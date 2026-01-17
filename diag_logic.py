
from ml_utils import analyze_gap
import json

cv_text = "I know Python and Tableau."
jd_text = "Requires Python, Programming, Power BI, and Java."
res = analyze_gap(cv_text, jd_text)

print(json.dumps(res, indent=2))
