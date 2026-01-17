
from ml_utils import analyze_gap
from knowledge_base import SKILL_CLUSTERS, INFERENCE_RULES

def test_matching_logic():
    print("=== Testing Structured Matching Logic ===\n")

    # TEST 1: Direct Match (Green)
    # CV has "Python", JD wants "Python"
    print("Test 1: Direct Match (PV: Python -> JD: Python)")
    res1 = analyze_gap("Skilled in Python.", "Requires Python.")
    assert "Python" in res1["matching_hard"], "Direct match logic failed"
    print("PASS: Python matched directly (Green)")

    # TEST 2: Inferred Match (Green)
    # CV has "Python", JD wants "Programming"
    # Rule: Python -> Programming
    print("\nTest 2: Inferred Match (PV: Python -> JD: Programming)")
    res2 = analyze_gap("Skilled in Python.", "Requires Programming.")
    assert "Programming" in res1["matching_hard"] or "programming" in [s.lower() for s in res2["matching_hard"]], f"Inferred match failed. Matched: {res2['matching_hard']}"
    print("PASS: Programming matched via inference (Green)")

    # TEST 3: Transferable Match (Yellow)
    # CV has "Tableau", JD wants "Power BI"
    # Cluster: BI Tools {Tableau, Power BI...}
    print("\nTest 3: Transferable Match (PV: Tableau -> JD: Power BI)")
    res3 = analyze_gap("Experienced with Tableau.", "Must know Power BI.")
    assert "Power BI" in res3["transferable"], f"Transferable match failed. Transferable: {res3['transferable']}"
    print(f"PASS: Power BI identified as transferable from {res3['transferable']['Power BI']} (Yellow)")

    # TEST 4: Missing (Red)
    # CV has "Cooking", JD wants "Java"
    print("\nTest 4: Missing Skill (PV: Cooking -> JD: Java)")
    res4 = analyze_gap("Expert in Cooking.", "Requires Java.")
    assert "Java" in res4["missing_hard"], "Missing logic failed"
    print("PASS: Java correctly marked missing (Red)")

    # TEST 5: Scoring
    # JD: Python (Direct), Programming (Inferred), Power BI (Transferable), Java (Missing)
    # Points: 1.0 (Python) + 1.0 (Programming) + 0.5 (Power BI) + 0.0 (Java) = 2.5 / 4 = 62.5%
    print("\nTest 5: Scoring Calculation")
    cv_text = "I know Python and Tableau."
    jd_text = "Requires Python, Programming, Power BI, and Java."
    res5 = analyze_gap(cv_text, jd_text)
    
    expected_score = 62.5
    print(f"Score: {res5['match_percentage']}% (Expected ~{expected_score}%)")
    assert abs(res5['match_percentage'] - expected_score) < 1.0, f"Scoring incorrect. Got {res5['match_percentage']}"
    print("PASS: Score calculation is correct.")

if __name__ == "__main__":
    try:
        test_matching_logic()
        print("\n=== ALL TESTS PASSED ===")
    except AssertionError as e:
        print(f"\nFAILED: {e}")
    except Exception as e:
        print(f"\nERROR: {e}")
