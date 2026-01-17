import sys
import os

# Add local path to sys to import modules
sys.path.append(os.getcwd())

from ml_utils import analyze_gap
from knowledge_base import SKILL_CLUSTERS, INFERENCE_RULES

def test_matching_logic():
    print("Testing Matching Logic...")
    
    # Test 1: Direct Match
    # User: Python, JD: Python
    cv_text_1 = "I have experience with Python."
    jd_text_1 = "Check for Python skills."
    
    result_1 = analyze_gap(cv_text_1, jd_text_1)
    print("\n--- Test 1: Direct Match (Python vs Python) ---")
    print(f"Matched Hard: {result_1['matching_hard']}")
    print(f"Transferable: {result_1['transferable']}")
    print(f"Missing: {result_1['missing_hard']}")
    print(f"Score: {result_1['match_percentage']}%")
    
    # Test 2: Inferred Match (Hierarchy)
    # User: Python (Child), JD: Programming (Parent)
    cv_text_2 = "I have experience with Python."
    jd_text_2 = "Must know Programming."
    
    result_2 = analyze_gap(cv_text_2, jd_text_2)
    print("\n--- Test 2: Inferred Match (Python -> Programming) ---")
    print(f"Matched Hard: {result_2['matching_hard']}")
    print(f"Transferable: {result_2['transferable']}")
    print(f"Missing: {result_2['missing_hard']}")
    print(f"Score: {result_2['match_percentage']}%")

    # Test 3: Transferable Match (Cluster)
    # User: Looker Studio, JD: Tableau
    cv_text_3 = "I use Looker Studio for reports."
    jd_text_3 = "Experience with Tableau is required."
    
    result_3 = analyze_gap(cv_text_3, jd_text_3)
    print("\n--- Test 3: Transferable Match (Looker Studio -> Tableau) ---")
    print(f"Matched Hard: {result_3['matching_hard']}")
    # Transferable should have { 'Tableau': ['Looker Studio'] }
    print(f"Transferable: {result_3['transferable']}") 
    print(f"Missing: {result_3['missing_hard']}")
    print(f"Score: {result_3['match_percentage']}%")

    # Test 4: Missing
    # User: Python, JD: Cooking
    cv_text_4 = "Python developer."
    jd_text_4 = "Must know Cooking."
    
    result_4 = analyze_gap(cv_text_4, jd_text_4)
    print("\n--- Test 4: Missing (Python vs Cooking) ---")
    print(f"Matched Hard: {result_4['matching_hard']}")
    print(f"Transferable: {result_4['transferable']}")
    print(f"Missing: {result_4['missing_hard']}")
    print(f"Score: {result_4['match_percentage']}%")

if __name__ == "__main__":
    test_matching_logic()
