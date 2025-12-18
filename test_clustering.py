import ml_utils
import os
import pandas as pd

# Mock Data
skills = [
    "Python", "SQL", "Java", "C++",           # Tech
    "Communication", "Leadership", "Teamwork", # Soft
    "Docker", "Kubernetes", "AWS"             # DevOps
]

print("Testing perform_skill_clustering...")
df_viz, dendro_path, clusters = ml_utils.perform_skill_clustering(skills)

if df_viz is not None:
    print("✅ DataFrame created.")
    print(df_viz.head())
else:
    print("❌ DataFrame is None.")

if dendro_path and os.path.exists(dendro_path):
    print(f"✅ Dendrogram saved at {dendro_path}")
else:
    print("❌ Dendrogram not found.")

if clusters:
    print("✅ Clusters assigned:")
    print(clusters)
else:
    print("❌ No clusters returned.")
