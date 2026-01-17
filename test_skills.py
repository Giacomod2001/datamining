import sys
import os
sys.path.append(os.getcwd())
import ml_utils
import knowledge_base

def test_specific_skills():
    print("=== TESTING SPECIFIC SKILLS ===\n")
    
    # Test if these skills are defined in HARD_SKILLS
    hard_skills = getattr(knowledge_base, "HARD_SKILLS", {})
    soft_skills = getattr(knowledge_base, "SOFT_SKILLS", {})
    
    test_skills = ["Analytics", "Business Analysis", "Campaign Management", "Excel", "Statistics", "Leadership"]
    
    for skill in test_skills:
        print(f"\n--- {skill} ---")
        
        # Check if it's a key in HARD_SKILLS
        if skill in hard_skills:
            print(f"[OK] Found as HARD_SKILL key")
            print(f"  Variations: {hard_skills[skill][:5]}...")  # Show first 5
        elif skill in soft_skills:
            print(f"[OK] Found as SOFT_SKILL key")
            print(f"  Variations: {soft_skills[skill][:5]}...")
        else:
            # Check if it's a variation
            found_in = None
            for key, variations in hard_skills.items():
                if skill.lower() in [v.lower() for v in variations]:
                    found_in = key
                    print(f"[OK] Found as variation of HARD_SKILL '{key}'")
                    break
            
            if not found_in:
                for key, variations in soft_skills.items():
                    if skill.lower() in [v.lower() for v in variations]:
                        found_in = key
                        print(f"[OK] Found as variation of SOFT_SKILL '{key}'")
                        break
            
            if not found_in:
                print(f"[FAIL] NOT FOUND in knowledge base")
    
    print("\n\n=== TESTING EXPANSION LOGIC ===\n")
    
    # Test expansion
    test_cv_skills = {"analytics", "excel", "campaign management", "leadership"}
    expanded = ml_utils.expand_skills_with_clusters(test_cv_skills)
    
    print(f"Input: {test_cv_skills}")
    print(f"Expanded: {expanded}")
    print(f"\nAdded by expansion: {expanded - test_cv_skills}")

if __name__ == "__main__":
    test_specific_skills()
