
import os

# Define the content to append to knowledge_base.py
# extracted from the current constants.py
extra_content = """
# =============================================================================
# EXTENSIONS & MARKET INTELLIGENCE (MIGRATED FROM CONSTANTS.PY)
# =============================================================================

# Skill Demand Matrix (Market Intelligence)
SKILL_DEMAND_MATRIX = {
    "high_demand": [
        ("Python", "🔥 High demand in Data & AI"),
        ("Cloud Computing", "☁️ Growing 25% YoY"),
        ("Machine Learning", "🤖 AI boom driving demand"),
        ("React", "⚛️ Top frontend framework"),
        ("DevOps", "🚀 Critical for modern teams"),
        ("Cybersecurity", "🔒 Increasing threats = more jobs"),
        ("Data Analysis", "📊 Every company needs analysts"),
        ("SQL", "💾 Universal database skill"),
    ],
    "emerging": [
        ("MLOps", "Bridging ML and Operations"),
        ("Kubernetes", "Container orchestration standard"),
        ("Terraform", "Infrastructure as Code leader"),
        ("dbt", "Modern data transformation"),
        ("Snowflake", "Cloud data warehouse boom"),
    ]
}

# Learning Paths (Skill Development Roadmaps)
LEARNING_PATHS = {
    "Data Analytics_to_Data Science": {
        "from_role": "Data Analyst",
        "to_role": "Data Scientist",
        "total_time": "6-9 months",
        "gap_skills": [
            {"skill": "Machine Learning", "priority": "Critical", "duration": "2-3 months", "resources": ["Coursera ML Specialization", "Fast.ai"]},
            {"skill": "Python (Advanced)", "priority": "High", "duration": "1-2 months", "resources": ["Real Python", "DataCamp"]},
            {"skill": "Statistics (Inferential)", "priority": "High", "duration": "1-2 months", "resources": ["Khan Academy", "StatQuest YouTube"]},
            {"skill": "Deep Learning", "priority": "Medium", "duration": "2-3 months", "resources": ["Deep Learning Specialization", "PyTorch Tutorials"]}
        ]
    },
    "Frontend_to_Full Stack": {
        "from_role": "Frontend Developer",
        "to_role": "Full Stack Developer",
        "total_time": "4-6 months",
        "gap_skills": [
            {"skill": "Node.js", "priority": "Critical", "duration": "1-2 months", "resources": ["NodeSchool", "FreeCodeCamp"]},
            {"skill": "SQL", "priority": "Critical", "duration": "1 month", "resources": ["SQLZoo", "Mode Analytics SQL Tutorial"]},
            {"skill": "REST API Design", "priority": "High", "duration": "2-3 weeks", "resources": ["REST API Tutorial", "Postman Learning"]},
            {"skill": "DevOps Basics", "priority": "Medium", "duration": "1-2 months", "resources": ["Docker Getting Started", "CI/CD Fundamentals"]}
        ]
    }
}

# Domain-Specific Extraction Rules (Context Awareness)
DOMAIN_EXTRACTION_RULES = {
    "Energy": {
        "context_words": ["energy", "renewable", "power", "grid", "solar", "wind", "electricity"],
        "must_extract": ["Energy Markets", "Power Systems", "Renewable Energy", "Grid", "Solar Energy"],
        "boost_skills": {"Energy Engineering": 1.5, "Renewable Energy": 1.3, "Power Systems": 1.3}
    },
    "Biotech": {
        "context_words": ["biotech", "pharma", "clinical", "drug", "research", "molecular"],
        "must_extract": ["Clinical Research", "GMP", "Regulatory Affairs", "Lab Techniques"],
        "boost_skills": {"Clinical Research": 1.5, "Lab Techniques": 1.3}
    },
    "Fashion": {
        "context_words": ["fashion", "luxury", "retail", "apparel", "design", "textile"],
        "must_extract": ["Fashion Design", "Visual Merchandising", "Buying", "Textile"],
        "boost_skills": {"Fashion Design": 1.5, "Visual Merchandising": 1.3}
    },
    "Manufacturing": {
        "context_words": ["manufacturing", "production", "plant", "automation", "quality", "lean"],
        "must_extract": ["Lean Manufacturing", "Quality Management", "Industrial Automation"],
        "boost_skills": {"Lean Manufacturing": 1.5, "Quality Management": 1.3}
    }
}

# Context Signals (Seniority, Work Style)
CONTEXT_SIGNALS = {
    "seniority_from_jd": {
        "entry": ["junior", "entry level", "graduate", "intern", "trainee", "0-2 years"],
        "mid": ["mid-level", "experienced", "3-5 years", "specialist"],
        "senior": ["senior", "lead", "principal", "5+ years", "expert"],
        "executive": ["director", "vp", "head of", "chief", "executive", "c-level"]
    },
    "work_style": {
        "remote": ["remote", "work from home", "distributed", "anywhere"],
        "hybrid": ["hybrid", "flexible", "office/remote"],
        "onsite": ["onsite", "in-office", "on-premise", "physical presence"]
    }
}

# =============================================================================
# BACKWARD COMPATIBILITY & FIXES
# =============================================================================
# Ensure INFERENCE_RULES alias
INFERENCE_RULES = globals().get('SKILL_HIERARCHY', {})

# Re-generate JOB_ARCHETYPES with robust logic
if 'JOB_ARCHETYPES_EXTENDED' in globals():
    JOB_ARCHETYPES = {}
    for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
        if isinstance(metadata, dict):
            skills_set = set(metadata.get("primary_skills", []))
            if "hard_skills" in metadata:
                skills_set.update(metadata.get("hard_skills", []))
            JOB_ARCHETYPES[role] = skills_set
        elif isinstance(metadata, (list, set)):
            JOB_ARCHETYPES[role] = set(metadata)
        else:
            JOB_ARCHETYPES[role] = set()

# Placeholder for obsolete structures
ML_MODELS = {}
"""

kb_path = "knowledge_base.py"
with open(kb_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the start of the backward compatibility layer to replace it
start_line = -1
for i, line in enumerate(lines):
    if "BACKWARD COMPATIBILITY LAYER" in line:
        start_line = i - 1
        break

if start_line != -1:
    new_content = "".join(lines[:start_line]) + extra_content
else:
    new_content = "".join(lines) + extra_content

with open(kb_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully unified knowledge_base.py")
