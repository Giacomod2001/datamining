"""
================================================================================
Deep Test: Inference Rules, Job Archetypes, and Dev Console
================================================================================
Verifica approfondita delle regole di inferenza e degli archetipi.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ml_utils
import knowledge_base
import constants

def print_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_test(name, passed, details=""):
    status = "[PASS]" if passed else "[FAIL]"
    print(f"  {status}: {name}")
    if details:
        print(f"         {details}")
    return passed

# =============================================================================
# TEST 1: SKILL_HIERARCHY / INFERENCE_RULES Structure
# =============================================================================
def test_skill_hierarchy():
    print_header("TEST 1: SKILL_HIERARCHY / INFERENCE_RULES")
    
    tests_passed = 0
    total_tests = 0
    
    # Check SKILL_HIERARCHY exists
    total_tests += 1
    sh = getattr(knowledge_base, "SKILL_HIERARCHY", {})
    passed = len(sh) > 0
    if print_test(f"SKILL_HIERARCHY has {len(sh)} entries", passed):
        tests_passed += 1
    
    # Check INFERENCE_RULES is alias
    total_tests += 1
    ir = getattr(knowledge_base, "INFERENCE_RULES", {})
    passed = ir == sh
    if print_test("INFERENCE_RULES is alias for SKILL_HIERARCHY", passed):
        tests_passed += 1
    
    # Check structure: each entry should have parents
    total_tests += 1
    valid_entries = 0
    for child, parents in sh.items():
        if isinstance(parents, (list, tuple, set)) and len(parents) > 0:
            valid_entries += 1
    passed = valid_entries >= len(sh) * 0.9
    if print_test(f"{valid_entries}/{len(sh)} entries have valid parent structure", passed):
        tests_passed += 1
    
    # Sample some inference rules
    print("\n  Sample Inference Rules:")
    for i, (child, parents) in enumerate(list(sh.items())[:5]):
        parent_str = ", ".join(parents) if isinstance(parents, (list, tuple)) else str(parents)
        print(f"    {child} -> {parent_str}")
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 2: Bidirectional Skill Expansion
# =============================================================================
def test_skill_expansion():
    print_header("TEST 2: expand_skills_bidirectional()")
    
    tests_passed = 0
    total_tests = 0
    
    # Test with Python skill
    total_tests += 1
    result = ml_utils.expand_skills_bidirectional({"python"})
    passed = len(result) > 1  # Should expand to related skills
    if print_test(f"'python' expands to {len(result)} skills", passed, f"Skills: {list(result)[:8]}..."):
        tests_passed += 1
    
    # Test with React
    total_tests += 1
    result = ml_utils.expand_skills_bidirectional({"react"})
    passed = len(result) > 1
    if print_test(f"'react' expands to {len(result)} skills", passed, f"Skills: {list(result)[:8]}..."):
        tests_passed += 1
    
    # Test with SQL
    total_tests += 1
    result = ml_utils.expand_skills_bidirectional({"sql"})
    passed = len(result) >= 1
    if print_test(f"'sql' expands to {len(result)} skills", passed, f"Skills: {list(result)[:8]}..."):
        tests_passed += 1
    
    # Test multiple skills
    total_tests += 1
    result = ml_utils.expand_skills_bidirectional({"python", "machine learning", "tensorflow"})
    passed = len(result) >= 3
    if print_test(f"Multiple skills expand to {len(result)}", passed):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 3: Job Archetypes Deep Validation
# =============================================================================
def test_job_archetypes_deep():
    print_header("TEST 3: Job Archetypes Deep Validation")
    
    tests_passed = 0
    total_tests = 0
    
    archetypes = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
    
    # Check key archetypes exist
    key_roles = ["Data Scientist", "Software Engineer", "Marketing Manager", "Financial Analyst", "Frontend Developer"]
    
    for role in key_roles:
        total_tests += 1
        passed = role in archetypes
        if print_test(f"'{role}' archetype exists", passed):
            tests_passed += 1
    
    # Check each archetype has required fields
    total_tests += 1
    required_fields = {"primary_skills", "soft_skills", "sector"}
    complete = 0
    for name, data in archetypes.items():
        if isinstance(data, dict):
            has_skills = "primary_skills" in data or "hard_skills" in data
            has_soft = "soft_skills" in data
            has_sector = "sector" in data
            if has_skills and has_soft and has_sector:
                complete += 1
    passed = complete >= len(archetypes) * 0.8
    if print_test(f"{complete}/{len(archetypes)} archetypes are complete", passed):
        tests_passed += 1
    
    # Check Data Scientist structure in detail
    total_tests += 1
    ds = archetypes.get("Data Scientist", {})
    ds_skills = ds.get("primary_skills", [])
    expected = ["Python", "Machine Learning", "Statistics"]
    found = sum(1 for e in expected if any(e.lower() in s.lower() for s in ds_skills))
    passed = found >= 2
    if print_test(f"Data Scientist has core skills ({found}/3)", passed, f"Skills: {ds_skills}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 4: SKILL_CLUSTERS Validation
# =============================================================================
def test_skill_clusters():
    print_header("TEST 4: SKILL_CLUSTERS Validation")
    
    tests_passed = 0
    total_tests = 0
    
    clusters = getattr(knowledge_base, "SKILL_CLUSTERS", {})
    
    # Check clusters exist
    total_tests += 1
    passed = len(clusters) > 0
    if print_test(f"SKILL_CLUSTERS has {len(clusters)} clusters", passed):
        tests_passed += 1
    
    # Check cluster structure
    total_tests += 1
    valid = 0
    for cluster_id, data in clusters.items():
        if isinstance(data, dict):
            if "skills" in data and len(data.get("skills", [])) > 0:
                valid += 1
        elif isinstance(data, (list, tuple)) and len(data) > 0:
            valid += 1
    passed = valid >= len(clusters) * 0.8
    if print_test(f"{valid}/{len(clusters)} clusters have valid skills", passed):
        tests_passed += 1
    
    # Show sample clusters
    print("\n  Sample Skill Clusters:")
    for i, (cid, data) in enumerate(list(clusters.items())[:5]):
        if isinstance(data, dict):
            skills = list(data.get("skills", []))[:4]
        else:
            skills = list(data)[:4]
        print(f"    {cid}: {skills}")
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 5: Role Recommendation System
# =============================================================================
def test_recommend_roles():
    print_header("TEST 5: Role Recommendation System")
    
    tests_passed = 0
    total_tests = 0
    
    # Test with Python/ML skills
    cv_skills = {"Python", "Machine Learning", "TensorFlow", "SQL", "Data Analysis"}
    cv_text = "Data Scientist with 5 years experience in Python, Machine Learning, and TensorFlow."
    
    recs = ml_utils.recommend_roles(cv_skills=cv_skills, cv_text=cv_text)
    
    total_tests += 1
    passed = len(recs) > 0
    if print_test(f"Returns {len(recs)} role recommendations", passed):
        tests_passed += 1
    
    # Check recommendation structure
    total_tests += 1
    if recs:
        rec = recs[0]
        has_role = "role" in rec
        has_score = "score" in rec
        passed = has_role and has_score
        if print_test("Recommendations have 'role' and 'score' fields", passed):
            tests_passed += 1
    else:
        print_test("Recommendations have 'role' and 'score' fields", False, "No recommendations")
    
    # Check scores are valid percentages
    total_tests += 1
    valid_scores = all(0 <= r.get("score", -1) <= 100 for r in recs[:5])
    if print_test("All scores are valid percentages (0-100)", valid_scores):
        tests_passed += 1
    
    # Show top recommendations
    print("\n  Top Role Recommendations:")
    for rec in recs[:5]:
        print(f"    {rec.get('role', 'Unknown')}: {rec.get('score', 0):.1f}%")
    
    # Check Data Scientist is in top 3
    total_tests += 1
    top_roles = [r.get("role", "") for r in recs[:5]]
    passed = any("Data" in r for r in top_roles)
    if print_test("Data-related role is in top 5 for ML skills", passed, f"Top: {top_roles}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 6: Inference Rules in Action (Gap Analysis)
# =============================================================================
def test_inference_in_gap():
    print_header("TEST 6: Inference Rules in Gap Analysis")
    
    tests_passed = 0
    total_tests = 0
    
    # CV with React (should infer Frontend/JavaScript)
    cv_text = "Frontend Developer: React, TypeScript, CSS, HTML"
    jd_text = "Looking for Frontend Developer with JavaScript and UI skills"
    
    result = ml_utils.analyze_gap(cv_text, jd_text)
    
    # Check if inference worked (React should match JavaScript requirement)
    total_tests += 1
    matched = result.get("matching_hard", [])
    matched_lower = [s.lower() for s in matched]
    # Should find JavaScript or Frontend through React inference
    passed = any("javascript" in s or "frontend" in s or "react" in s for s in matched_lower)
    if print_test("Inference finds React/JavaScript connection", passed, f"Matched: {matched}"):
        tests_passed += 1
    
    # Check match percentage reflects inference
    total_tests += 1
    pct = result.get("match_percentage", 0)
    passed = pct > 0
    if print_test(f"Match percentage: {pct}% (should be > 0)", passed):
        tests_passed += 1
    
    # Test with TensorFlow (should infer ML/Python)
    cv2 = "ML Engineer: TensorFlow, PyTorch, NumPy, Pandas"
    jd2 = "Machine Learning Engineer with Python and Deep Learning"
    
    result2 = ml_utils.analyze_gap(cv2, jd2)
    
    total_tests += 1
    matched2 = result2.get("matching_hard", [])
    pct2 = result2.get("match_percentage", 0)
    passed = pct2 > 50  # Should be high match
    if print_test(f"TensorFlow -> ML inference works ({pct2}%)", passed, f"Matched: {matched2}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 7: Dev Console Data Integrity
# =============================================================================
def test_dev_console_data():
    print_header("TEST 7: Dev Console Data Integrity")
    
    tests_passed = 0
    total_tests = 0
    
    # Simulate what the Dev Console would display
    
    # 1. Knowledge Base Stats
    archetypes = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
    clusters = getattr(knowledge_base, "SKILL_CLUSTERS", {})
    hierarchy = getattr(knowledge_base, "SKILL_HIERARCHY", {})
    
    total_tests += 1
    passed = len(archetypes) >= 30
    if print_test(f"Job Archetypes count: {len(archetypes)} (min 30)", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = len(clusters) >= 5
    if print_test(f"Skill Clusters count: {len(clusters)} (min 5)", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = len(hierarchy) >= 50
    if print_test(f"Inference Rules count: {len(hierarchy)} (min 50)", passed):
        tests_passed += 1
    
    # 2. Count total unique skills
    all_skills = set()
    for name, data in archetypes.items():
        if isinstance(data, dict):
            all_skills.update(data.get("primary_skills", []))
            all_skills.update(data.get("soft_skills", []))
    
    total_tests += 1
    passed = len(all_skills) >= 50
    if print_test(f"Unique skills in KB: {len(all_skills)} (min 50)", passed):
        tests_passed += 1
    
    # 3. Sectors coverage
    sectors = set()
    for name, data in archetypes.items():
        if isinstance(data, dict):
            sectors.add(data.get("sector", "Unknown"))
    
    total_tests += 1
    passed = len(sectors) >= 5
    if print_test(f"Industry sectors: {len(sectors)} (min 5)", passed, f"Sectors: {sectors}"):
        tests_passed += 1
    
    print("\n  Dev Console Summary:")
    print(f"    - Archetypes: {len(archetypes)}")
    print(f"    - Clusters: {len(clusters)}")
    print(f"    - Inference Rules: {len(hierarchy)}")
    print(f"    - Unique Skills: {len(all_skills)}")
    print(f"    - Sectors: {sectors}")
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# MAIN
# =============================================================================
def run_all_deep_tests():
    print("\n" + "=" * 70)
    print("    DEEP TESTS: INFERENCE RULES, ARCHETYPES, DEV CONSOLE")
    print("=" * 70)
    
    results = []
    results.append(("skill_hierarchy", test_skill_hierarchy()))
    results.append(("skill_expansion", test_skill_expansion()))
    results.append(("job_archetypes_deep", test_job_archetypes_deep()))
    results.append(("skill_clusters", test_skill_clusters()))
    results.append(("recommend_roles", test_recommend_roles()))
    results.append(("inference_in_gap", test_inference_in_gap()))
    results.append(("dev_console_data", test_dev_console_data()))
    
    print_header("FINAL RESULTS")
    passed = sum(1 for _, p in results if p)
    
    for name, result in results:
        status = "[PASSED]" if result else "[FAILED]"
        print(f"  {status}: {name}")
    
    print(f"\n  TOTAL: {passed}/{len(results)} test suites passed")
    
    if passed == len(results):
        print("\n  >>> ALL DEEP TESTS PASSED!")
    else:
        print("\n  >>> Some tests failed.")
    
    return passed == len(results)

if __name__ == "__main__":
    run_all_deep_tests()
