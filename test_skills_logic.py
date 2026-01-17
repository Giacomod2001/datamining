
import unittest
from ml_utils import analyze_gap
from knowledge_base import SKILL_CLUSTERS, INFERENCE_RULES

class TestSkillGapLogic(unittest.TestCase):
    def test_direct_match(self):
        """Test Case 1: Direct Match (Green)"""
        # User has Python, JD needs Python
        cv_text = "I have experience with Python."
        jd_text = "Required: Python."
        
        result = analyze_gap(cv_text, jd_text)
        
        self.assertIn("Python", result["matching_hard"])
        self.assertNotIn("Python", result["missing_hard"])
        # Score calculation: 1 skill required, 1 matched direct = 1.0/1.0 = 100%
        self.assertAlmostEqual(result["match_percentage"], 100.0)

    def test_inferred_match(self):
        """Test Case 2: Inferred Match (Green) - Hierarchy"""
        # User has Python (Child), JD needs Programming (Parent)
        # Verify Rule exists: Python -> Programming
        
        cv_text = "I know Python."
        jd_text = "Must understand Programming concepts."
        
        result = analyze_gap(cv_text, jd_text)
        
        # Should match "Programming" because Python implies Programming
        self.assertIn("Programming", result["matching_hard"])
        self.assertNotIn("Programming", result["missing_hard"])
        self.assertAlmostEqual(result["match_percentage"], 100.0)

    def test_transferable_match(self):
        """Test Case 3: Transferable Match (Yellow) - Cluster"""
        # User has Looker Studio, JD needs Tableau
        # Both in "BI Tools" cluster
        
        cv_text = "Proficient in Looker Studio."
        jd_text = "Experience with Tableau is required."
        
        result = analyze_gap(cv_text, jd_text)
        
        # Tableau is technically "missing" as a direct skill, BUT handled as transferable
        # The current analyze_gap implementation puts it in 'transferable' dict, NOT 'matching_hard'
        # and excludes it from 'missing_hard'.
        
        self.assertNotIn("Tableau", result["matching_hard"]) 
        self.assertIn("Tableau", result["transferable"])
        self.assertNotIn("Tableau", result["missing_hard"])
        
        # Score: 1 required. Transferable = 0.5. Total 0.5/1.0 = 50%
        self.assertAlmostEqual(result["match_percentage"], 50.0)

    def test_missing_match(self):
        """Test Case 4: Missing (Red)"""
        cv_text = "I know Cooking."
        jd_text = "Required: Java."
        
        result = analyze_gap(cv_text, jd_text)
        
        self.assertIn("Java", result["missing_hard"])
        self.assertEqual(result["match_percentage"], 0.0)

    def test_mixed_scenario(self):
        """Test Case 5: Complex Scenario"""
        # CV: Python (Direct), Looker Studio (Transferable for Tableau), Cooking (Extra)
        # JD: Python, Tableau, Java (Missing)
        
        cv_text = "Skills: Python, Looker Studio, Cooking."
        jd_text = "Requirements: Python, Tableau, Java."
        
        result = analyze_gap(cv_text, jd_text)
        
        self.assertIn("Python", result["matching_hard"]) # 1.0
        self.assertIn("Tableau", result["transferable"]) # 0.5
        self.assertIn("Java", result["missing_hard"])    # 0.0
        
        # Score: (1.0 + 0.5 + 0.0) / 3 = 1.5/3 = 50%
        self.assertAlmostEqual(result["match_percentage"], 50.0)
        
    def test_score_cap(self):
        """Test Case 6: Score Capped at 100%"""
        # Edge case where logic might double count or something (though current logic sums / total_required)
        # If I have Python and JD needs Python.
        cv_text = "Python"
        jd_text = "Python"
        result = analyze_gap(cv_text, jd_text)
        self.assertLessEqual(result["match_percentage"], 100.0)

if __name__ == '__main__':
    unittest.main()
