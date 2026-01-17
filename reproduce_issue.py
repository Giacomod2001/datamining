
import sys
import os
sys.path.append(os.getcwd())
import ml_utils
import knowledge_base

def reproduce_issue():
    # Setup
    user_skills = {"english"}  # User has specific skill
    required_skills = ["Languages"] # Job requires category key
    
    # Current behavior in discover_careers logic (simplified)
    cv_norm = {s.lower() for s in user_skills}
    role_norm = {s.lower() for s in required_skills}
    
    # 1. Expand with Actual ML Utils Logic
    cv_expanded = ml_utils.expand_skills_with_clusters(cv_norm)
            
    # Check match
    matched = cv_expanded & role_norm
    missing = role_norm - cv_expanded
    
    print(f"User Skills: {user_skills}")
    print(f"Required: {required_skills}")
    print(f"Expanded: {cv_expanded}")
    print(f"Matched: {matched}")
    print(f"Missing: {missing}")
    
    if "languages" in missing:
        print("FAIL: 'English' did not trigger 'Languages' match.")
    else:
        print("PASS: 'English' triggered 'Languages' match.")

if __name__ == "__main__":
    reproduce_issue()
