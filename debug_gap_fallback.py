
from knowledge_base import JOB_ARCHETYPES_EXTENDED
import ml_utils

print("--- DEBUGGING GAP ANALYSIS FALLBACK ---")
print(f"Total Archetypes: {len(JOB_ARCHETYPES_EXTENDED)}")
print(f"Keys: {list(JOB_ARCHETYPES_EXTENDED.keys())}")

key = "Energy Engineering"
if key in JOB_ARCHETYPES_EXTENDED:
    print(f"SUCCESS: '{key}' found in KB.")
    print(f"Data: {JOB_ARCHETYPES_EXTENDED[key]}")
else:
    print(f"FAILURE: '{key}' NOT found in KB.")
    # Check close matches
    import difflib
    print(f"Close matches: {difflib.get_close_matches(key, JOB_ARCHETYPES_EXTENDED.keys())}")

# Test analyze_gap fallback simulation
query = "energy engineering"
print(f"\nSimulating Fallback for query: '{query}'")

# Copy-paste logic from ml_utils.py (simplified) to test
import difflib
titles = list(JOB_ARCHETYPES_EXTENDED.keys())
matches = difflib.get_close_matches(query, titles, n=1, cutoff=0.6)
if not matches:
    matches = [t for t in titles if query.lower() in t.lower()]

print(f"Matches found: {matches}")

if matches:
    best_role = matches[0]
    print(f"Selected Role: {best_role}")
    archetype_data = JOB_ARCHETYPES_EXTENDED[best_role]
    
    arch_hard = set()
    if "primary_skills" in archetype_data:
        arch_hard.update(archetype_data["primary_skills"])
    if "hard_skills" in archetype_data:
        arch_hard.update(archetype_data["hard_skills"])
        print(f"Found 'hard_skills': {archetype_data['hard_skills']}")
    
    print(f"Final Loaded Skills: {arch_hard}")
else:
    print("NO MATCHES FOUND IN FALLBACK LOGIC")

# Now run the REAL function
print("\n--- REAL FUNCTION CALL ---")
res = ml_utils.analyze_gap(cv_text="Thermodynamics, AutoCAD", job_text="energy engineering")
print(f"Match %: {res['match_percentage']}")
print(f"Missing: {res['missing_hard']}")
print(f"Matched: {res['matching_hard']}")
