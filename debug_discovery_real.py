
import ml_utils
from knowledge_base import JOB_ARCHETYPES_EXTENDED, INFERENCE_RULES

# Simulate User CV Text
cv_text = """
EDUCATION
Laurea in Ingegneria Energetica
Politecnico di Milano

SKILLS
AutoCAD, Matlab, English
"""

print("--- DEBUGGING DISCOVERY ---")

# 1. Test Extraction
hard, soft = ml_utils.extract_skills_from_text(cv_text)
print(f"Extracted Hard Skills: {hard}")

# 2. Test Inferred Skills via expand_skills_with_clusters
# Manually check what "Ingegneria Energetica" infers
if "Ingegneria Energetica" in INFERENCE_RULES:
    print(f"Direct Inference Rule found for 'Ingegneria Energetica': {INFERENCE_RULES['Ingegneria Energetica']}")
else:
    print("WARNING: 'Ingegneria Energetica' NOT in INFERENCE_RULES keys!")

# 3. Test expand function
expanded = ml_utils.expand_skills_with_clusters(hard)
print(f"Expanded Skills: {expanded}")

# 4. Run discovery
print("\n--- RUNNING DISCOVER_CAREERS ---")
# Reset JOB_ARCHETYPES in constants just in case (since we import it inside the function usually)
import constants
# Reload matching Logic
try:
    results = ml_utils.discover_careers(cv_text=cv_text)
    
    # Filter for Energy Engineer
    energy_res = [r for r in results if "Energy" in r['role']]
    for r in energy_res:
        print(f"\nRole: {r['role']}")
        print(f"Score: {r['score']:.1f}%")
        print(f"Matched: {r['skills_matched']}")
        print(f"Missing: {r['missing_skills']}")
        print(f"Raw Match %: {r['skill_match']:.1f}%")
except Exception as e:
    print(f"Error running discovery: {e}")
