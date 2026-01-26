import sys
import os

# Add project directory to path
sys.path.append(os.path.abspath(os.curdir))

from ml_utils import extract_skills_from_text, analyze_gap
import constants

def test_ner_extraction():
    print("--- Test 1: NER Extraction (Technical Skills) ---")
    test_text = "Experienced Senior Data Scientist with expertise in PyTorch, AWS Bedrock, and Snowflake database optimization. Skilled in MLOps workflows using MLflow."
    
    hard_skills, soft_skills = extract_skills_from_text(test_text)
    
    print(f"Text: {test_text}")
    print(f"Extracted Hard Skills: {hard_skills}")
    
    # Check for expected skills
    expected = {"pytorch", "snowflake", "mlflow", "aws"}
    found_expected = expected.intersection(hard_skills)
    
    if found_expected == expected:
        print("[OK] SUCCESS: All core technical skills extracted.")
    else:
        print(f"[WARN] PARTIAL: Missing {expected - hard_skills}")

def test_gap_analysis():
    print("\n--- Test 2: Gap Analysis (Inference Logic) ---")
    cv_text = "I have experience with Python and SQL."
    jd_text = "Required: Data Engineering skills, Spark, and ETL experience."
    
    results = analyze_gap(cv_text, jd_text)
    
    print(f"CV: {cv_text}")
    print(f"JD: {jd_text}")
    print(f"Match Percentage: {results['match_percentage']}%")
    print(f"Missing Hard Skills: {results['missing_hard']}")
    
    if results['match_percentage'] < 50:
        print("[OK] SUCCESS: Low match percentage correctly identified.")
    else:
        print("[FAIL] FAILURE: Match percentage too high.")

if __name__ == "__main__":
    try:
        test_ner_extraction()
        test_gap_analysis()
        print("\n[VERIFICATION COMPLETE]")
    except Exception as e:
        print(f"\n[FAIL] ERROR during verification: {e}")
