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
    JOB_ROLE_METADATA,
    JOB_ARCHETYPES_EXTENDED
)

# =============================================================================
# JOB ARCHETYPES (IMPORTED FROM KNOWLEDGE BASE V2.0)
# =============================================================================
# Backward Compatibility Layer
# The application expects JOB_ARCHETYPES to be Dict[str, Set[str]]
# knowledge_base.JOB_ARCHETYPES_EXTENDED is Dict[str, Dict] (V2 Metadata)

JOB_ARCHETYPES = {}

for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    if isinstance(metadata, dict) and "primary_skills" in metadata:
        # Create a set of primary skills for JOB_ARCHETYPES
        skills_set = set(metadata["primary_skills"])
        JOB_ARCHETYPES[role] = skills_set
    else:
        # Fallback for any non-dict entries
        JOB_ARCHETYPES[role] = set(metadata) if not isinstance(metadata, set) else metadata
