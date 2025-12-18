
from fpdf import FPDF

# ==========================================
# 1. OPTIMIZED JOB DESCRIPTION (Text File)
# ==========================================
# Strategy:
# - Match: Python, SQL, Git.
# - Transferable: AWS (Employee has Azure/GCP).
# - Gap: Power BI (Employee has nothing visually similar in clusters? Wait, BI Tools cluster has Power BI. If employee has nothing, it's a Gap).
# - Portfolio: System Design (Project Based).

jd_text = """
JOB TITLE: Senior Data Engineer
LOCATION: Rome, Italy (Remote)

ABOUT US:
We are "TechCorp Srl", a leading tech company looking for a talented Senior Data Engineer to join our Innovation Hub. 
You will lead high-impact projects involving Cloud Computing and Big Data.

RESPONSIBILITIES:
- Design and deploy scalable pipelines on AWS (Amazon Web Services).
- Create interactive dashboards for stakeholders using Power BI.
- Communicate complex technical results to non-technical business leaders.
- Handle massive datasets.
- Design scalable architecture (System Design).

REQUIREMENTS:
- Hard Skills: Python, SQL, AWS, Power BI, System Design, Git.
- Soft Skills: Leadership, Communication, Problem Solving.
- Experience: 5+ years in Data Science or related fields.
"""

# ==========================================
# 2. OPTIMIZED CV (PDF File)
# ==========================================
# Strategy:
# - Entities: Marco Rossi, TechCorp Srl, Politecnico di Milano.
# - Skills: Python, SQL, Azure, GCP, Git, Machine Learning, Deep Learning, Pandas, NumPy.
# - NOT Included: Power BI (So it shows as Missing), AWS (So it shows as Transferable via Azure).

cv_text = """
MARCO ROSSI
Location: Milano, Italy
Email: marco.rossi@email.com | Phone: +39 333 1234567

PROFILE
Passionate Data Engineer with 4 years of experience.
Specialized in Cloud Architecture and Backend Development.

EXPERIENCE
Data Engineer | TechCorp Srl (Torino, Italy)
Jan 2021 - Present
- Developed ETL pipelines using Python (Pandas) and SQL.
- Migrated on-premise infrastructure to Microsoft Azure and Google Cloud Platform (GCP).
- Optimized queries for faster reporting.
- Collaborated with cross-functional teams.

EDUCATION
Master of Science in Computer Engineering
Politecnico di Milano | 2018 - 2020

SKILLS
- Technical: Python, SQL, Azure, GCP, Git, Machine Learning, Deep Learning, Pandas, NumPy, Flask.
- Soft Skills: Problem Solving, Teamwork, Creativity.
- Languages: Italian (Native), English (Upper Intermediate).
"""

def create_pdf(filename, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Curriculum Vitae", 0, 1, "C")
    pdf.ln(10)
    
    # Body
    pdf.set_font("Arial", "", 12)
    # Handle simple encoding
    content_latin = content.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 7, content_latin)
    
    pdf.output(filename)
    print(f"Generated {filename}")

if __name__ == "__main__":
    # Create Text File
    with open("Demo_Job_Offer.txt", "w") as f:
        f.write(jd_text)
    print("Generated Demo_Job_Offer.txt")
    
    # Create PDF File
    create_pdf("Demo_Candidate_CV.pdf", cv_text)
