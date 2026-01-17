import difflib

titles = ["Energy Trader", "Renewable Energy Engineer", "Data Scientist", "Software Engineer"]
query = "energy engeneer"

matches = difflib.get_close_matches(query, titles, n=1, cutoff=0.5)
print(f"Difflib Result: {matches}")

# Containment check (Reverse: Is query in Title? No. Is title in query? No.)
# What about token overlap?
query_tokens = set(query.lower().split())
best_role = None
max_overlap = 0

for t in titles:
    t_tokens = set(t.lower().split())
    overlap = len(query_tokens.intersection(t_tokens))
    if overlap > max_overlap:
        max_overlap = overlap
        best_role = t

print(f"Token Overlap Best: {best_role} (Overlap: {max_overlap})")
