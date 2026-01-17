import sys
import os
sys.path.append(os.getcwd())
import ml_utils

def test_gap_analysis():
    # Simulate a CV with "English" and a JD requiring "Languages"
    cv_text = """
    John Doe
    john@example.com
    
    Skills:
    - Python
    - English (fluent)
    - Excel
    """
    
    jd_text = """
    We are looking for:
    - Languages (multilingual environment)
    - Python
    - Data Analysis
    """
    
    result = ml_utils.analyze_gap(cv_text, jd_text)
    
    print("=== GAP ANALYSIS TEST ===")
    print(f"CV Skills extracted: {sorted(result.get('matching_hard', set()) | result.get('extra_hard', set()))}")
    print(f"JD Skills required: {sorted(result.get('matching_hard', set()) | result.get('missing_hard', set()))}")
    print()
    print(f"Matched: {sorted(result.get('matching_hard', set()))}")
    print(f"Missing: {sorted(result.get('missing_hard', set()))}")
    print(f"Bonus: {sorted(result.get('extra_hard', set()))}")
    print()
    
    # Check if Languages is matched (should be, because CV has English)
    if 'Languages' in result.get('matching_hard', set()):
        print("✓ PASS: 'Languages' correctly matched (user has 'English')")
    elif 'Languages' in result.get('missing_hard', set()):
        print("✗ FAIL: 'Languages' still marked as Missing despite having 'English'")
    else:
        print("? WARNING: 'Languages' not found in any category")

if __name__ == "__main__":
    test_gap_analysis()
