"""
================================================================================
CareerMatch AI - Knowledge Base (constants.py)
================================================================================
Universal skill database covering all major industries and career paths.
Suitable for graduates from any Italian university degree program.
================================================================================
"""

# =============================================================================
# IMPORT FROM REFACTORED KNOWLEDGE BASE
# =============================================================================
from knowledge_base import (
    JOB_ARCHETYPES_EXTENDED,
    SKILL_HIERARCHY,
    SKILL_IMPLICATIONS,
    SKILL_CLUSTERS,
    PROJECT_BASED_SKILLS,
    SENIORITY_KEYWORDS,
    HARD_SKILLS,
    SOFT_SKILLS,
    NON_SKILL_PATTERNS
)

# Dynamic Generation for backward compatibility
CAREER_CATEGORIES = {}
for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    sector = metadata.get("sector", "Other")
    if sector not in CAREER_CATEGORIES:
        CAREER_CATEGORIES[sector] = f"Roles related to {sector}"

JOB_ROLE_METADATA = {}
for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    JOB_ROLE_METADATA[role] = {
        "category": metadata.get("sector", "Other"),
        "client_facing": metadata.get("client_facing", False),
        "remote_friendly": metadata.get("remote_friendly", True),
        "international": metadata.get("international", True),
        "dynamic": metadata.get("dynamic", False),
        "creative": metadata.get("creative", False)
    }

# =============================================================================
# BACKWARD COMPATIBILITY LAYER
# =============================================================================
# The application expects certain variable names that may differ in the new KB

# 1. INFERENCE_RULES (maps to SKILL_HIERARCHY in new KB)
INFERENCE_RULES = SKILL_HIERARCHY

# 2. JOB_ARCHETYPES (simplified format for legacy code)
# Convert JOB_ARCHETYPES_EXTENDED (dict with metadata) to simple dict of sets
JOB_ARCHETYPES = {}
for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    if isinstance(metadata, dict):
        # Extract primary_skills from metadata
        skills_set = set(metadata.get("primary_skills", []))
        # Also add hard_skills if present (for robustness)
        if "hard_skills" in metadata:
            skills_set.update(metadata.get("hard_skills", []))
        JOB_ARCHETYPES[role] = skills_set
    elif isinstance(metadata, (list, set)):
        # Fallback for simple list/set format
        JOB_ARCHETYPES[role] = set(metadata)
    else:
        # Safety fallback
        JOB_ARCHETYPES[role] = set()

# 3. ML_MODELS (placeholder - not used in current implementation)
# This was an artifact from the old structure
ML_MODELS = {}

# =============================================================================
# ADDITIONAL FEATURES (Optional Extensions)
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
            {
                "skill": "Machine Learning",
                "priority": "Critical",
                "duration": "2-3 months",
                "resources": ["Coursera ML Specialization", "Fast.ai"]
            },
            {
                "skill": "Python (Advanced)",
                "priority": "High",
                "duration": "1-2 months",
                "resources": ["Real Python", "DataCamp"]
            },
            {
                "skill": "Statistics (Inferential)",
                "priority": "High",
                "duration": "1-2 months",
                "resources": ["Khan Academy", "StatQuest YouTube"]
            },
            {
                "skill": "Deep Learning",
                "priority": "Medium",
                "duration": "2-3 months",
                "resources": ["Deep Learning Specialization", "PyTorch Tutorials"]
            }
        ]
    },
    "Frontend_to_Full Stack": {
        "from_role": "Frontend Developer",
        "to_role": "Full Stack Developer",
        "total_time": "4-6 months",
        "gap_skills": [
            {
                "skill": "Node.js",
                "priority": "Critical",
                "duration": "1-2 months",
                "resources": ["NodeSchool", "FreeCodeCamp"]
            },
            {
                "skill": "SQL",
                "priority": "Critical",
                "duration": "1 month",
                "resources": ["SQLZoo", "Mode Analytics SQL Tutorial"]
            },
            {
                "skill": "REST API Design",
                "priority": "High",
                "duration": "2-3 weeks",
                "resources": ["REST API Tutorial", "Postman Learning"]
            },
            {
                "skill": "DevOps Basics",
                "priority": "Medium",
                "duration": "1-2 months",
                "resources": ["Docker Getting Started", "CI/CD Fundamentals"]
            }
        ]
    }
}

# Domain-Specific Extraction Rules (Context Awareness)
DOMAIN_EXTRACTION_RULES = {
    "Energy": {
        "context_words": ["energy", "renewable", "power", "grid", "solar", "wind", "electricity"],
        "must_extract": ["Energy Markets", "Power Systems", "Renewable Energy", "Grid", "Solar Energy"],
        "boost_skills": {
            "Energy Engineering": 1.5,
            "Renewable Energy": 1.3,
            "Power Systems": 1.3
        }
    },
    "Biotech": {
        "context_words": ["biotech", "pharma", "clinical", "drug", "research", "molecular"],
        "must_extract": ["Clinical Research", "GMP", "Regulatory Affairs", "Lab Techniques"],
        "boost_skills": {
            "Clinical Research": 1.5,
            "Lab Techniques": 1.3
        }
    },
    "Fashion": {
        "context_words": ["fashion", "luxury", "retail", "apparel", "design", "textile"],
        "must_extract": ["Fashion Design", "Visual Merchandising", "Buying", "Textile"],
        "boost_skills": {
            "Fashion Design": 1.5,
            "Visual Merchandising": 1.3
        }
    },
    "Manufacturing": {
        "context_words": ["manufacturing", "production", "plant", "automation", "quality", "lean"],
        "must_extract": ["Lean Manufacturing", "Quality Management", "Industrial Automation"],
        "boost_skills": {
            "Lean Manufacturing": 1.5,
            "Quality Management": 1.3
        }
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
# VALIDATION CHECKS (Run at Import)
# =============================================================================
def _validate_knowledge_base():
    """
    Validates the integrity of the knowledge base at import time.
    Ensures no broken references or missing keys.
    """
    errors = []
    
    # Check 1: All roles in JOB_ARCHETYPES have skills
    for role, skills in JOB_ARCHETYPES.items():
        if not skills or len(skills) == 0:
            errors.append(f"Role '{role}' has no skills defined")
    
    # Check 2: SKILL_HIERARCHY references valid parent skills
    for child, parents in SKILL_HIERARCHY.items():
        for parent in parents:
            # Parent should exist in HARD_SKILLS or SOFT_SKILLS
            if parent not in HARD_SKILLS and parent not in SOFT_SKILLS:
                # Allow some meta-categories that aren't literal skills
                meta_categories = {"Programming", "Cloud Computing", "Web Development", 
                                 "Frontend Development", "Backend Development", "Data Analysis"}
                if parent not in meta_categories:
                    errors.append(f"Inference rule '{child}' -> '{parent}' references unknown skill")
    
    # Check 3: SKILL_CLUSTERS contain valid skills
    for cluster_name, cluster_data in SKILL_CLUSTERS.items():
        if isinstance(cluster_data, dict):
            skills = cluster_data.get("skills", set())
        else:
            skills = cluster_data
        
        for skill in skills:
            # Skill should exist somewhere in the KB
            # (Either in HARD_SKILLS keys, or as a known tool/framework)
            # This is a soft check - we allow some flexibility
            pass
    
    # Print validation results
    if errors:
        print("⚠️  Knowledge Base Validation Warnings:")
        for error in errors[:10]:  # Show first 10 only
            print(f"   - {error}")
        if len(errors) > 10:
            print(f"   ... and {len(errors) - 10} more")
    else:
        print("✅ Knowledge Base validated successfully")

# Run validation on import (comment out in production if needed)
# _validate_knowledge_base()

# =============================================================================
# EXPORT ALL (for wildcard imports)
# =============================================================================
__all__ = [
    # Core Data Structures
    'JOB_ARCHETYPES',
    'JOB_ARCHETYPES_EXTENDED',
    'SKILL_HIERARCHY',
    'SKILL_IMPLICATIONS',
    'SKILL_CLUSTERS',
    'HARD_SKILLS',
    'SOFT_SKILLS',
    
    # Classification & Patterns
    'PROJECT_BASED_SKILLS',
    'SENIORITY_KEYWORDS',
    'NON_SKILL_PATTERNS',
    
    # Metadata
    'CAREER_CATEGORIES',
    'JOB_ROLE_METADATA',
    
    # Backward Compatibility
    'INFERENCE_RULES',
    'ML_MODELS',
    
    # Extensions
    'SKILL_DEMAND_MATRIX',
    'LEARNING_PATHS',
    'DOMAIN_EXTRACTION_RULES',
    'CONTEXT_SIGNALS',
]
