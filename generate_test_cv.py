from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'MARCO ROSSI', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Junior Data Analyst | marco.rossi@email.com', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# SUMMARY
pdf.chapter_title('PROFESSIONAL SUMMARY')
pdf.chapter_body(
    "Passionate Junior Data Analyst with a strong background in Statistics and Mathematics. "
    "Proficient in Python for data analysis and visualization. "
    "Looking for opportunities to apply statistical modeling and machine learning to business problems. "
    "Eager to learn and grow in a dynamic environment."
)

# SKILLS (Intentionally skewed to DS, missing DE tools)
pdf.chapter_title('TECHNICAL SKILLS')
pdf.chapter_body(
    "- Programming: Python (Pandas, NumPy, Scikit-learn), R\n"
    "- Visualization: Matplotlib, Seaborn, Tableau\n"
    "- Concepts: Statistical Analysis, Linear Regression, Hypothesis Testing, A/B Testing\n"
    "- Tools: Jupyter Notebook, Excel (Pivot Tables, VLOOKUP)\n"
    "- Languages: Italian (Native), English (B2)"
)

# EXPERIENCE
pdf.chapter_title('WORK EXPERIENCE')
pdf.chapter_body(
    "Intern Data Analyst | Marketing Solutions Srl | Milan | 2023 - Present\n"
    "- Analyzed customer churn data using Python and Pandas.\n"
    "- Created monthly reports using Excel and Tableau.\n"
    "- Conducted A/B testing on email marketing campaigns.\n"
    "- Assisted in cleaning datasets for predictive modeling."
)

# EDUCATION
pdf.chapter_title('EDUCATION')
pdf.chapter_body(
    "Bachelor's Degree in Statistics | University of Bologna | 2020 - 2023\n"
    "- Thesis: 'Predictive Modeling for Retail Sales'\n"
    "- Grade: 110/110"
)

# PROJECT
pdf.chapter_title('PROJECTS')
pdf.chapter_body(
    "Customer Segmentation Analysis\n"
    "- Used K-Means clustering to segment customers based on purchasing behavior.\n"
    "- Visualized results using Seaborn to identify key market segments."
)

pdf.output('Demo_Candidate_DS_CV.pdf', 'F')
print("PDF Generated Successfully: Demo_Candidate_DS_CV.pdf")
