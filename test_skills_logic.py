
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
        
        # With aggregated Visualization key, both Looker Studio and Tableau map to 'Visualization'
        # So it becomes a Direct Match (Green) for current logic (User requested "Match era meglio prima")
        self.assertIn("Visualization", result["matching_hard"])
        self.assertNotIn("Tableau", result["missing_hard"])
        
        # Score calculation: 100% match
        self.assertAlmostEqual(result["match_percentage"], 100.0)

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
        # Tableau -> Visualization (Green Direct Match due to aggregation)
        self.assertIn("Visualization", result["matching_hard"]) 
        self.assertIn("Java", result["missing_hard"])    # 0.0
        
        # Score calculation is complex due to Inference Rules (Python -> Programming, Tableau -> BI Tools, etc.)
        # We verify that we got a score involving the partial matches.
        # It should be at least (1.0 + 0.5) / Total > 0.
        self.assertGreater(result["match_percentage"], 30.0)
        # Verify it didn't just bomb to 0 or 100 unfairly
        self.assertLess(result["match_percentage"], 100.0)
        
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
