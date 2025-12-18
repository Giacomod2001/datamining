from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        if hasattr(self, 'title_text'):
            self.cell(0, 10, self.title_text, 0, 1, 'C')
        self.set_font('Arial', '', 12)
        if hasattr(self, 'subtitle_text'):
            self.cell(0, 10, self.subtitle_text, 0, 1, 'C')
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

# 1. Generate Senior DE CV (High Match)
pdf = PDF()
pdf.title_text = 'MARIO ROSSI'
pdf.subtitle_text = 'Senior Data Engineer | mario.rossi@email.com'
pdf.add_page()

pdf.chapter_title('PROFESSIONAL SUMMARY')
pdf.chapter_body(
    "Senior Data Engineer with 5+ years of experience in designing and building scalable data pipelines. "
    "Expert in cloud technologies (AWS, GCP) and big data frameworks (Spark). "
)

pdf.chapter_title('TECHNICAL SKILLS')
pdf.chapter_body(
    "- Languages: Python, SQL, Java, Scala\n"
    "- Cloud: AWS (S3, Redshift, Glue), GCP (BigQuery, Dataflow)\n"
    "- Big Data: Apache Spark, Hadoop, Kafka, Airflow\n"
    "- Databases: PostgreSQL, MongoDB, Cassandra\n"
    "- Tools: Docker, Kubernetes, Terraform, Git"
)

pdf.chapter_title('EXPERIENCE')
pdf.chapter_body(
    "Senior Data Engineer | Tech Corp | 2020 - Present\n"
    "- Built real-time data ingestion pipelines using Kafka and Spark Streaming.\n"
    "- Optimized ETL processes reducing latency by 40%.\n"
    "- Managed Data Warehouse migration to Snowflake.\n\n"
    "Data Engineer | Data Solutions | 2017 - 2020\n"
    "- Developed Python ETL scripts for daily reporting.\n"
    "- Maintained Airflow DAGs for scheduling data jobs."
)

pdf.output('Demo_Candidate_CV.pdf', 'F')
print("Generated: Demo_Candidate_CV.pdf (High Match)")

# 2. Generate Junior DS CV (Low Match / Pivot)
pdf_ds = PDF()
pdf_ds.title_text = 'LUCA BIANCHI'
pdf_ds.subtitle_text = 'Junior Data Analyst | luca.bianchi@email.com'
pdf_ds.add_page()

pdf_ds.chapter_title('PROFESSIONAL SUMMARY')
pdf_ds.chapter_body(
    "Passionate Junior Data Analyst with a strong background in Statistics. "
    "Proficient in Python for data analysis and visualization. "
    "Looking for opportunities in Data Science."
)

pdf_ds.chapter_title('TECHNICAL SKILLS')
pdf_ds.chapter_body(
    "- Programming: Python (Pandas, NumPy, Scikit-learn), R\n"
    "- Visualization: Matplotlib, Seaborn, Tableau\n"
    "- Concepts: Statistical Analysis, Linear Regression, A/B Testing\n"
    "- Tools: Jupyter Notebook, Excel"
)

pdf_ds.chapter_title('EXPERIENCE')
pdf_ds.chapter_body(
    "Intern Data Analyst | Marketing Srl | 2023 - Present\n"
    "- Analyzed customer churn data using Python.\n"
    "- Created monthly reports using Excel and Tableau."
)

pdf_ds.output('Demo_Candidate_DS_CV.pdf', 'F')
print("Generated: Demo_Candidate_DS_CV.pdf (Low Match)")

# 3. Generate Job Description (Senior DE)
jd_text = """JOB TITLE: Senior Data Engineer

JOB SUMMARY:
We are looking for a Senior Data Engineer to join our data platform team. You will be responsible for building and maintaining our data infrastructure.

RESPONSIBILITIES:
- Design and implement scalable data pipelines.
- Manage cloud infrastructure on AWS.
- Optimize data warehouses (BigQuery/Redshift).
- Collaborate with Data Scientists to deploy ML models.

REQUIREMENTS:
- 4+ years of experience as a Data Engineer.
- Strong proficiency in Python and SQL.
- Experience with Big Data technologies: Spark, Airflow, Kafka.
- Hands-on experience with Cloud platforms (AWS or GCP).
- Knowledge of Containerization (Docker, Kubernetes).
- Familiarity with NoSQL databases.
"""

with open("Demo_Job_Offer.txt", "w") as f:
    f.write(jd_text)
print("Generated: Demo_Job_Offer.txt")
