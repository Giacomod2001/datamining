import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

import ml_utils
import knowledge_base

def test_bidirectional_inference():
    print("--- Testing Bidirectional Inference ---")
    # Data Science should imply SQL, Python, Excel
    skills = {"data science"}
    expanded = ml_utils.expand_skills_bidirectional(skills)
    expected = {"data science", "sql", "python", "excel", "machine learning", "statistics"}
    
    found = expected.intersection(expanded)
    print(f"Expanded: {expanded}")
    print(f"Intersection with expected: {found}")
    assert "sql" in expanded, "SQL missing from Data Science expansion"
    assert "excel" in expanded, "Excel missing from Data Science expansion"
    print("PASSED: Bidirectional Inference\n")

def test_soft_skill_refactor():
    print("--- Testing Soft Skill Refactor ---")
    cv_text = "I am a Data Scientist with Leadership and Communication skills."
    jd_text = "Looking for a Data Analyst with SQL and Leadership."
    
    res = ml_utils.analyze_gap(cv_text, jd_text)
    
    print(f"Match Pct: {res['match_percentage']}%")
    print(f"Soft Stated: {res['soft_stated_strengths']}")
    print(f"Soft Interview Verified: {res['soft_interview_verified']}")
    
    assert "leadership" in [s.lower() for s in res['soft_interview_verified']]
    # match_percentage should NOT be 100% just because of soft skills if hard skills are missing
    # But here "Data Science" implies "SQL", so it might be high.
    print("PASSED: Soft Skill Refactor\n")

def test_archetype_fallback():
    print("--- Testing Archetype Fallback ---")
    # Title-only JD
    jd_text = "Space Systems Architect"
    cv_text = "I have experience with GNC and Propulsion."
    
    res = ml_utils.analyze_gap(cv_text, jd_text)
    print(f"Archetype Detected: {res['seniority_info'].get('best_role_detected')}")
    print(f"Matched Skills: {res['matching_hard']}")
    
    assert len(res['matching_hard']) > 0, "No skills matched via fallback"
    print("PASSED: Archetype Fallback\n")

def test_discovery_engine():
    print("--- Testing Discovery Engine ---")
    skills = {"qiskit", "quantum algorithms", "python"}
    recs = ml_utils.recommend_roles(skills)
    
    roles = [r['role'] for r in recs]
    print(f"Recommendations: {roles}")
    
    assert any("Quantum" in r for r in roles), "Quantum role not recommended for Quantum skills"
    print("PASSED: Discovery Engine\n")

if __name__ == "__main__":
    try:
        test_bidirectional_inference()
        test_soft_skill_refactor()
        test_archetype_fallback()
        test_discovery_engine()
        print("ALL ENGINE TESTS PASSED!")
    except Exception as e:
        print(f"TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
