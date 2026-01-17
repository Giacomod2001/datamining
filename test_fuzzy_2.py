import difflib

titles = ["Energy Trader", "Renewable Energy Engineer", "Software Engineer"]
query = "energy engineering"

print(f"Query: '{query}'")
match_engineer = difflib.get_close_matches(query, ["Energy Engineer"], n=1, cutoff=0.6)
print(f"Match against 'Energy Engineer' (Simulated): {match_engineer}")

match_renewable = difflib.get_close_matches(query, ["Renewable Energy Engineer"], n=1, cutoff=0.6)
print(f"Match against 'Renewable Energy Engineer': {match_renewable}")

# Test simple containment logic used in app
containment = [t for t in titles if query.lower() in t.lower()]
print(f"Containment check: {containment}")
