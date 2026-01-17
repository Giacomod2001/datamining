
from knowledge_base import HARD_SKILLS, SKILL_CLUSTERS

keys_to_check = ["Tableau", "BI Tools", "Data Visualization", "Visualization", "Looker Studio", "Looker"]

print("=== HARD_SKILLS Entries ===")
for k in keys_to_check:
    print(f"'{k}': {HARD_SKILLS.get(k, 'NOT FOUND')}")

print("\n=== SKILL_CLUSTERS Entries ===")
for name, skills in SKILL_CLUSTERS.items():
    check = [k for k in keys_to_check if k in skills]
    if check:
        print(f"Cluster '{name}': {check}")
