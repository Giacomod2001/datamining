
from knowledge_base import HARD_SKILLS

print("Searching for keys with 'tableau' in variations...")
for skill, variations in HARD_SKILLS.items():
    if any("tableau" in v.lower() for v in variations):
        print(f"Key: '{skill}' -> Variations: {variations}")

print("\nSearching for keys with 'visualization' in variations...")
for skill, variations in HARD_SKILLS.items():
    if any("visualization" in v.lower() for v in variations):
        print(f"Key: '{skill}' -> Variations: {variations}")
