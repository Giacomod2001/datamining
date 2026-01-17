"""
Debug script to test skill extraction and matching
"""
import sys
sys.path.insert(0, r'C:\Users\giaco\.gemini\antigravity\scratch\datamining_git')

import ml_utils
import constants

# Test CV from demo
cv_text = """
GIACOMO DELLACQUA
Digital Marketing Data Analyst
Milan, Italy | dellacquagiacomo@gmail.com | +39 351 930 1321

PROFESSIONAL SUMMARY
Results-driven Digital Marketing Data Analyst with expertise in AI-powered business solutions and data-driven decision-making. 

TECHNICAL SKILLS
- Analytics: Google Analytics 4, Google Tag Manager, Looker Studio, Tableau
- Programming: Python, SQL, BigQuery, Machine Learning (scikit-learn)
- Marketing: Digital Marketing, Marketing Automation, CRM, Performance Marketing
- Business Analysis: Requirements gathering, process mapping, gap analysis
- Campaign Management: Multi-channel campaign planning and execution
- Excel: Advanced Excel, pivot tables, data analysis
- Statistics: Statistical analysis, A/B testing, hypothesis testing
- Leadership: Team coordination and project management

PROFESSIONAL EXPERIENCE
Digital Marketing Data Analyst Intern | Randstad Group Italia SPA | Nov 2025 – Present
- Implement and maintain online tracking ecosystems using Google Tag Manager
- Analyze website performance and user behavior using Google Analytics 4
- Design interactive dashboards with Google Looker Studio for stakeholder reporting
- Support paid performance campaigns and conduct A/B testing for optimization
"""

print("="*80)
print("SKILL EXTRACTION TEST")
print("="*80)

# Extract skills from CV
cv_hard, cv_soft = ml_utils.extract_skills_from_text(cv_text)

print(f"\n1. HARD SKILLS EXTRACTED ({len(cv_hard)}):")
for skill in sorted(cv_hard):
    print(f"   - {skill}")

print(f"\n2. SOFT SKILLS EXTRACTED ({len(cv_soft)}):")
for skill in sorted(cv_soft):
    print(f"   - {skill}")

# Test expansion
cv_norm = {s.lower() for s in cv_hard}
cv_expanded = ml_utils.expand_skills_with_clusters(cv_norm)

print(f"\n3. EXPANDED SKILLS ({len(cv_expanded)}):")
added_skills = cv_expanded - cv_norm
print(f"   Added {len(added_skills)} skills through expansion:")
for skill in sorted(added_skills):
    print(f"   + {skill}")

# Test Marketing Manager archetype
print("\n" + "="*80)
print("MARKETING MANAGER ARCHETYPE TEST")
print("="*80)

marketing_skills = constants.JOB_ARCHETYPES.get("Marketing Manager", set())
print(f"\n4. MARKETING MANAGER REQUIRED SKILLS ({len(marketing_skills)}):")
for skill in sorted(marketing_skills):
    print(f"   - {skill}")

# Expand marketing skills
marketing_norm = {s.lower() for s in marketing_skills}
marketing_expanded = ml_utils.expand_skills_with_clusters(marketing_norm)

print(f"\n5. MARKETING MANAGER EXPANDED SKILLS ({len(marketing_expanded)}):")
added_marketing = marketing_expanded - marketing_norm
print(f"   Added {len(added_marketing)} skills through expansion:")
for skill in sorted(added_marketing):
    print(f"   + {skill}")

# Calculate match
intersection = cv_expanded & marketing_expanded
union = cv_expanded | marketing_expanded
jaccard = len(intersection) / len(union) if union else 0

print(f"\n6. MATCHING ANALYSIS:")
print(f"   CV expanded: {len(cv_expanded)} skills")
print(f"   Role expanded: {len(marketing_expanded)} skills")
print(f"   Intersection: {len(intersection)} skills")
print(f"   Union: {len(union)} skills")
print(f"   Jaccard score: {jaccard:.2%}")

print(f"\n7. MATCHED SKILLS:")
for skill in sorted(intersection):
    print(f"   ✓ {skill}")

missing = marketing_expanded - cv_expanded
print(f"\n8. MISSING SKILLS ({len(missing)}):")
for skill in sorted(missing):
    print(f"   ✗ {skill}")

extra = cv_expanded - marketing_expanded  
print(f"\n9. BONUS SKILLS ({len(extra)}):")
for skill in sorted(extra):
    print(f"   + {skill}")
