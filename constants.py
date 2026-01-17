"""
================================================================================
CareerMatch AI - Knowledge Base (constants.py)
================================================================================

Universal skill database covering all major industries and career paths.
Suitable for graduates from any Italian university degree program.

================================================================================
"""

from knowledge_base import (
    ML_MODELS, 
    INFERENCE_RULES, 
    SKILL_CLUSTERS, 
    PROJECT_BASED_SKILLS, 
    SENIORITY_KEYWORDS, 
    HARD_SKILLS, 
    SOFT_SKILLS, 
    NON_SKILL_PATTERNS, 
    CAREER_CATEGORIES, 
    JOB_ARCHETYPES_EXTENDED
)

# =============================================================================
# JOB ARCHETYPES (IMPORTED FROM KNOWLEDGE BASE V2.0)
# =============================================================================
# Backward Compatibility Layer
# The application expects JOB_ARCHETYPES to be Dict[str, Set[str]]
# knowledge_base.JOB_ARCHETYPES_EXTENDED is Dict[str, Dict] (V2 Metadata)

JOB_ARCHETYPES = {}
JOB_ROLE_METADATA = {}

# Helper to infer category from role name
def _infer_category(role_name):
    """Infer category from role name keywords"""
    name_lower = role_name.lower()
    if any(kw in name_lower for kw in ['data', 'analyst', 'scientist', 'engineer', 'developer', 'tech']):
        return "Technology"
    elif any(kw in name_lower for kw in ['marketing', 'content', 'social', 'seo', 'campaign']):
        return "Marketing"
    elif any(kw in name_lower for kw in ['sales', 'business development', 'account']):
        return "Sales"
    elif any(kw in name_lower for kw in ['finance', 'accountant', 'auditor']):
        return "Finance"
    elif any(kw in name_lower for kw in ['hr', 'recruiter', 'talent']):
        return "Human Resources"
    elif any(kw in name_lower for kw in ['product', 'project manager']):
        return "Product & Operations"  
    elif any(kw in name_lower for kw in ['design', 'ux', 'ui']):
        return "Design"
    else:
        return "Other"

for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    if isinstance(metadata, dict) and "primary_skills" in metadata:
        # Create a set of primary skills for JOB_ARCHETYPES
        skills_set = set(metadata["primary_skills"])
        JOB_ARCHETYPES[role] = skills_set
        
        # Create metadata dict for JOB_ROLE_METADATA (used by discover_careers)
        # Infer category from role name since JOB_ARCHETYPES_EXTENDED doesn't have it
        JOB_ROLE_METADATA[role] = {
            "category": _infer_category(role),
            "client_facing": metadata.get("client_facing"),
            "remote_friendly": metadata.get("remote_friendly"),
            "international": metadata.get("international"),
            "dynamic": metadata.get("dynamic"),
            "creative": metadata.get("creative"),
        }
    else:
        # Fallback for any non-dict entries
        JOB_ARCHETYPES[role] = set(metadata) if not isinstance(metadata, set) else metadata
        JOB_ROLE_METADATA[role] = {"category": _infer_category(role)}
