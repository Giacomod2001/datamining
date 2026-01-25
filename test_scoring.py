"""
================================================================================
Test Suite for DataMining Scoring Functions
================================================================================
Comprehensive tests for skill matching, percentages, and scoring logic.
"""

import sys
import os

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import modules
import ml_utils
import knowledge_base

def print_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_test(name, passed, details=""):
    status = "[PASS]" if passed else "[FAIL]"
    print(f"  {status}: {name}")
    if details and not passed:
        print(f"         Details: {details}")
    return passed

# =============================================================================
# TEST 1: calculate_match_score Function
# =============================================================================
def test_calculate_match_score():
    print_header("TEST 1: calculate_match_score()")
    
    tests_passed = 0
    total_tests = 0
    
    # Test basic calculation
    total_tests += 1
    result = ml_utils.calculate_match_score(5.0, 10)
    passed = result == 50.0
    if print_test("Basic calculation (5/10 = 50%)", passed, f"Got {result}"):
        tests_passed += 1
    
    # Test 100% cap
    total_tests += 1
    result = ml_utils.calculate_match_score(15.0, 10)
    passed = result == 100.0
    if print_test("100% cap (15/10 should be 100%)", passed, f"Got {result}"):
        tests_passed += 1
    
    # Test zero items
    total_tests += 1
    result = ml_utils.calculate_match_score(5.0, 0)
    passed = result == 0.0
    if print_test("Zero items returns 0%", passed, f"Got {result}"):
        tests_passed += 1
    
    # Test decimal rounding
    total_tests += 1
    result = ml_utils.calculate_match_score(3.0, 7)
    passed = result == 42.9  # Should be rounded to 1 decimal
    if print_test("Decimal rounding (3/7 = 42.9%)", passed, f"Got {result}"):
        tests_passed += 1
    
    # Test weighted score
    total_tests += 1
    # 2 direct (2.0) + 1 inferred (0.9) + 1 transferable (0.7) = 3.6 out of 4
    score_points = 2 * 1.0 + 1 * 0.9 + 1 * 0.7
    result = ml_utils.calculate_match_score(score_points, 4)
    passed = result == 90.0
    if print_test("Weighted score calculation", passed, f"Got {result}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 2: Skill Extraction
# =============================================================================
def test_skill_extraction():
    print_header("TEST 2: extract_skills_from_text()")
    
    tests_passed = 0
    total_tests = 0
    
    # Test basic skill extraction from CV text
    cv_text = """
    Experienced Python developer with 5 years of experience.
    Skills: Python, JavaScript, SQL, React, Data Analysis
    Used Docker and Kubernetes for deployment.
    Strong communication and leadership abilities.
    """
    
    hard, soft = ml_utils.extract_skills_from_text(cv_text)
    
    # Check hard skills
    total_tests += 1
    passed = "Python" in hard or "python" in {s.lower() for s in hard}
    if print_test("Detects 'Python' as hard skill", passed, f"Hard skills: {hard}"):
        tests_passed += 1
    
    total_tests += 1
    passed = "SQL" in hard or "sql" in {s.lower() for s in hard}
    if print_test("Detects 'SQL' as hard skill", passed, f"Hard skills: {hard}"):
        tests_passed += 1
    
    # Check soft skills
    total_tests += 1
    soft_lower = {s.lower() for s in soft}
    passed = "communication" in soft_lower or "leadership" in soft_lower
    if print_test("Detects soft skills (communication/leadership)", passed, f"Soft skills: {soft}"):
        tests_passed += 1
    
    # Test with JD mode
    jd_text = "Looking for a Data Analyst with Python, SQL, and Excel experience."
    jd_hard, jd_soft = ml_utils.extract_skills_from_text(jd_text, is_jd=True)
    
    total_tests += 1
    passed = len(jd_hard) >= 2
    if print_test("JD mode extracts skills correctly", passed, f"JD skills: {jd_hard}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 3: Gap Analysis
# =============================================================================
def test_gap_analysis():
    print_header("TEST 3: analyze_gap()")
    
    tests_passed = 0
    total_tests = 0
    
    # Test matching CV
    cv_text = """
    Full Stack Developer with expertise in:
    - Python, JavaScript, React, Node.js
    - SQL, PostgreSQL, MongoDB
    - Docker, AWS, CI/CD
    - Git, Agile methodologies
    """
    
    jd_text = """
    Requirements:
    - Python programming
    - JavaScript and React
    - SQL database experience
    - Docker knowledge preferred
    """
    
    result = ml_utils.analyze_gap(cv_text, jd_text)
    
    # Check result structure
    total_tests += 1
    passed = "match_percentage" in result
    if print_test("Returns match_percentage", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = "matching_hard" in result
    if print_test("Returns matching_hard list", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = "missing_hard" in result
    if print_test("Returns missing_hard list", passed):
        tests_passed += 1
    
    # Check percentage is within bounds
    total_tests += 1
    pct = result.get("match_percentage", -1)
    passed = 0 <= pct <= 100
    if print_test(f"match_percentage is valid (0-100): {pct}%", passed, f"Got {pct}"):
        tests_passed += 1
    
    # Check high match percentage for matching skills
    total_tests += 1
    passed = pct >= 50  # Should be high since CV matches JD well
    if print_test(f"Good CV should have >50% match: {pct}%", passed, f"Got {pct}"):
        tests_passed += 1
    
    print(f"\n  Matching skills: {result.get('matching_hard', [])}")
    print(f"  Missing skills:  {result.get('missing_hard', [])}")
    print(f"  Match percentage: {result.get('match_percentage', 0)}%")
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 4: Role-Based Analysis (Archetype Fallback)
# =============================================================================
def test_role_archetype():
    print_header("TEST 4: Role Archetype Matching")
    
    tests_passed = 0
    total_tests = 0
    
    cv_text = """
    Data Scientist with strong Python and ML skills.
    Experience with TensorFlow, Pandas, NumPy, Scikit-learn.
    SQL and database management.
    Data visualization with Matplotlib and Tableau.
    Statistical analysis and A/B testing.
    """
    
    # Test with role name as JD
    role_jd = "Data Scientist"
    result = ml_utils.analyze_gap(cv_text, role_jd)
    
    total_tests += 1
    pct = result.get("match_percentage", -1)
    passed = 0 <= pct <= 100
    if print_test(f"Role-based analysis returns valid %: {pct}", passed):
        tests_passed += 1
    
    total_tests += 1
    matched = result.get("matching_hard", [])
    passed = len(matched) >= 2
    if print_test(f"Finds matching skills for role: {len(matched)} skills", passed):
        tests_passed += 1
    
    # Test with archetype check
    total_tests += 1
    archetypes = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
    passed = "Data Scientist" in archetypes
    if print_test("Data Scientist exists in knowledge base", passed):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 5: Composite Scoring
# =============================================================================
def test_composite_scoring():
    print_header("TEST 5: Composite Role Scoring")
    
    tests_passed = 0
    total_tests = 0
    
    # Test _calculate_composite_role_score
    total_tests += 1
    result = ml_utils._calculate_composite_role_score(80.0, 70.0, 90.0)
    # 65% * 80 + 20% * 70 + 15% * 90 = 52 + 14 + 13.5 = 79.5
    expected = 79.5
    passed = result == expected
    if print_test(f"Composite score calculation: {result}", passed, f"Expected {expected}"):
        tests_passed += 1
    
    # Test with 100% inputs
    total_tests += 1
    result = ml_utils._calculate_composite_role_score(100.0, 100.0, 100.0)
    passed = result == 100.0
    if print_test("100% inputs = 100% output", passed, f"Got {result}"):
        tests_passed += 1
    
    # Test with 0% inputs
    total_tests += 1
    result = ml_utils._calculate_composite_role_score(0.0, 0.0, 0.0)
    passed = result == 0.0
    if print_test("0% inputs = 0% output", passed, f"Got {result}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 6: Seniority Detection
# =============================================================================
def test_seniority_detection():
    print_header("TEST 6: Seniority Detection")
    
    tests_passed = 0
    total_tests = 0
    
    # Test senior level detection
    senior_text = "Senior Software Engineer with 10 years experience. Tech Lead at Google."
    level, confidence = ml_utils.detect_seniority(senior_text)
    
    total_tests += 1
    passed = level in ["Senior Level", "Senior", "Mid-Senior"]
    if print_test(f"Detects senior level: {level}", passed, f"Confidence: {confidence}"):
        tests_passed += 1
    
    # Test junior level detection
    junior_text = "Junior developer, recent graduate. Entry-level position. Internship experience."
    level, confidence = ml_utils.detect_seniority(junior_text)
    
    total_tests += 1
    passed = level in ["Junior", "Entry Level", "Entry-Level"]
    if print_test(f"Detects junior level: {level}", passed, f"Confidence: {confidence}"):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 7: Knowledge Base Integrity
# =============================================================================
def test_knowledge_base():
    print_header("TEST 7: Knowledge Base Integrity")
    
    tests_passed = 0
    total_tests = 0
    
    # Check for essential attributes
    total_tests += 1
    passed = hasattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED")
    if print_test("JOB_ARCHETYPES_EXTENDED exists", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = hasattr(knowledge_base, "SKILL_CLUSTERS")
    if print_test("SKILL_CLUSTERS exists", passed):
        tests_passed += 1
    
    # Check archetype structure
    archetypes = getattr(knowledge_base, "JOB_ARCHETYPES_EXTENDED", {})
    
    total_tests += 1
    passed = len(archetypes) >= 5
    if print_test(f"Has {len(archetypes)} job archetypes (min 5)", passed):
        tests_passed += 1
    
    # Check each archetype has required fields
    total_tests += 1
    valid_archetypes = 0
    for name, data in archetypes.items():
        if isinstance(data, dict):
            has_skills = "primary_skills" in data or "hard_skills" in data
            has_soft = "soft_skills" in data
            if has_skills and has_soft:
                valid_archetypes += 1
    
    passed = valid_archetypes >= len(archetypes) * 0.8  # 80% must be valid
    if print_test(f"{valid_archetypes}/{len(archetypes)} archetypes have valid structure", passed):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# TEST 8: Portfolio Analysis (if project text provided)
# =============================================================================
def test_portfolio_analysis():
    print_header("TEST 8: Portfolio/Project Analysis")
    
    tests_passed = 0
    total_tests = 0
    
    cv_text = "Python developer with data science skills. SQL, Pandas, Machine Learning."
    jd_text = "Data Analyst - Requires Python, SQL, Tableau, Data Visualization"
    project_text = """
    GitHub Project: Data Dashboard
    Built using Python, Pandas, and Tableau for data visualization.
    Implemented SQL queries for data extraction.
    Created interactive dashboards for business insights.
    """
    
    result = ml_utils.analyze_gap_with_project(cv_text, jd_text, project_text)
    
    # Check project-specific fields
    total_tests += 1
    passed = "project_verified" in result
    if print_test("Returns project_verified", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = "portfolio_quality" in result
    if print_test("Returns portfolio_quality", passed):
        tests_passed += 1
    
    total_tests += 1
    pq = result.get("portfolio_quality", -1)
    passed = 0 <= pq <= 100
    if print_test(f"Portfolio quality is valid (0-100): {pq}", passed):
        tests_passed += 1
    
    total_tests += 1
    passed = "gap_projects" in result
    if print_test("Returns gap_projects suggestions", passed):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"

# =============================================================================
# MAIN TEST RUNNER
# =============================================================================
def run_all_tests():
    print("\n" + "=" * 70)
    print("       DATAMINING SCORING SYSTEM - COMPREHENSIVE TESTS")
    print("=" * 70)
    
    all_passed = True
    test_results = []
    
    # Run each test suite
    test_results.append(("calculate_match_score", test_calculate_match_score()))
    test_results.append(("skill_extraction", test_skill_extraction()))
    test_results.append(("gap_analysis", test_gap_analysis()))
    test_results.append(("role_archetype", test_role_archetype()))
    test_results.append(("composite_scoring", test_composite_scoring()))
    test_results.append(("seniority_detection", test_seniority_detection()))
    test_results.append(("knowledge_base", test_knowledge_base()))
    test_results.append(("portfolio_analysis", test_portfolio_analysis()))
    
    # Summary
    print_header("FINAL RESULTS")
    passed = sum(1 for _, p in test_results if p)
    total = len(test_results)
    
    for name, result in test_results:
        status = "[PASSED]" if result else "[FAILED]"
        print(f"  {status}: {name}")
    
    print(f"\n  TOTAL: {passed}/{total} test suites passed")
    
    if passed == total:
        print("\n  >>> ALL TESTS PASSED! Scoring system is working correctly.")
    else:
        print("\n  >>> Some tests failed. Please review the output above.")
    
    return passed == total

if __name__ == "__main__":
    run_all_tests()
