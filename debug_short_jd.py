import ml_utils
from knowledge_base import JOB_ARCHETYPES_EXTENDED

text = "energy engeneer" # User typo included
hard, soft = ml_utils.extract_skills_from_text(text, is_jd=True)

print(f"Text: '{text}'")
print(f"Extracted Hard: {hard}")
print(f"Extracted Soft: {soft}")

# Check if it matches any archetype lazily
print("\n--- Archetype check ---")
for role in JOB_ARCHETYPES_EXTENDED.keys():
    if "energy" in role.lower():
        print(f"Found related role: {role}")
