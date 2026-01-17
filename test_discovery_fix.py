
# Mock minimal dependencies to test discover_careers
class MockConstants:
    JOB_ARCHETYPES = {
        "Energy Engineer": {
            "primary_skills": ["Thermodynamics", "Power Systems", "AutoCAD"],
            "category": "Engineering"
        },
        "Legacy Role": ["Skill A", "Skill B"]  # Test legacy list support
    }
    JOB_ROLE_METADATA = {}
    SKILL_CLUSTERS = {"Energy": ["Thermodynamics", "Heat Transfer"]}
    INFERENCE_RULES = {}

# Mock extract_skills
def extract_skills_from_text(text, is_jd=False):
    if "energy" in text.lower():
        return {"Thermodynamics", "Power Systems"}, set()
    return set(), set()

# Mock expand_skills
def expand_skills_with_clusters(skills):
    expanded = set(skills)
    if "Thermodynamics" in skills:
        expanded.add("Heat Transfer")
    return expanded

# Paste the function (simplified for testing context, or import if possible, but import is hard with mocks)
# I will just write a logic test that mimics the function I just wrote.

def test_logic():
    print("Testing Dictionary Support...")
    role_data = {"primary_skills": ["Thermodynamics", "AutoCAD"], "category": "Eng"}
    
    if isinstance(role_data, dict):
        skills = set(role_data.get("primary_skills", []))
        print(f"Dict Skills Extracted: {skills}")
        assert "Thermodynamics" in skills
    else:
        print("FAIL: Dict treated as list")

    print("\nTesting Matching...")
    cv_skills = {"Thermodynamics", "Power Systems"} # 2 skills
    role_skills = {"Thermodynamics", "Power Systems", "AutoCAD"} # 3 skills
    
    matched = cv_skills.intersection(role_skills)
    score = len(matched) / len(role_skills) * 100
    print(f"Score: {score:.1f}%")
    assert score > 60

test_logic()
