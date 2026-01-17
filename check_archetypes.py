from knowledge_base import JOB_ARCHETYPES_EXTENDED

key = "Renewable Energy Engineer"
if key in JOB_ARCHETYPES_EXTENDED:
    print(f"SUCCESS: {key} found in JOB_ARCHETYPES_EXTENDED")
    print(f"Skills: {JOB_ARCHETYPES_EXTENDED[key].get('hard_skills', [])}")
else:
    print(f"FAILURE: {key} NOT found in JOB_ARCHETYPES_EXTENDED")
    print("Available keys similar to 'Energy':")
    for k in JOB_ARCHETYPES_EXTENDED.keys():
        if "energy" in k.lower():
            print(f" - {k}")
