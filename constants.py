# SKILL GROUPS DATABASE
SKILL_GROUPS = {
    # Programming Languages
    "Python": ["python", "py", "python3", "django", "flask", "fastapi", "pandas", "numpy"],
    "Java": ["java", "spring", "spring boot", "maven", "gradle", "jvm"],
    "JavaScript": ["javascript", "js", "node", "nodejs", "typescript", "ts", "es6"],
    "C++": ["c++", "cpp", "c plus plus"],
    "C#": ["c#", "csharp", "c sharp", ".net", "dotnet", "asp.net"],
    "Go": ["go", "golang"],
    "Rust": ["rust", "rustlang"],
    "R": ["r language", "r programming", "rstudio", "tidyverse"],
    
    # Data Science & ML
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural network", "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn"],
    "Data Science": ["data science", "data scientist", "data analysis", "analytics", "statistical analysis"],
    "Computer Vision": ["computer vision", "cv", "image processing", "opencv", "yolo", "object detection", "image recognition"],
    "NLP": ["nlp", "natural language processing", "text mining", "sentiment analysis", "transformers", "bert", "gpt"],
    "Deep Learning": ["deep learning", "neural network", "cnn", "rnn", "lstm", "transformer"],
    
    # Databases
    "SQL": ["sql", "mysql", "postgresql", "postgres", "sqlite", "oracle", "sql server", "tsql", "plsql"],
    "MongoDB": ["mongodb", "mongo", "nosql"],
    "Redis": ["redis", "caching"],
    "BigQuery": ["bigquery", "big query", "bq"],
    
    # Cloud
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda", "dynamodb", "sagemaker", "cloudformation"],
    "GCP": ["gcp", "google cloud", "google cloud platform", "vertex ai", "cloud functions", "cloud run"],
    "Azure": ["azure", "microsoft azure", "azure devops", "azure ml"],
    "Cloud Computing": ["cloud", "cloud computing", "serverless", "iaas", "paas", "saas"],
    
    # DevOps
    "Docker": ["docker", "container", "containerization", "dockerfile"],
    "Kubernetes": ["kubernetes", "k8s", "helm", "kubectl", "container orchestration"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "continuous deployment", "jenkins", "github actions", "gitlab ci"],
    "Terraform": ["terraform", "infrastructure as code", "iac"],
    
    # Frontend
    "React": ["react", "reactjs", "react.js", "redux", "next.js", "nextjs"],
    "Vue": ["vue", "vuejs", "vue.js", "nuxt"],
    "Angular": ["angular", "angularjs"],
    "HTML/CSS": ["html", "css", "html5", "css3", "sass", "scss", "tailwind", "bootstrap"],
    
    # BI & Visualization
    "Tableau": ["tableau", "tableau desktop", "tableau server"],
    "Power BI": ["power bi", "powerbi", "dax"],
    "Looker": ["looker", "looker studio", "data studio"],
    "Excel": ["excel", "spreadsheet", "vlookup", "pivot table", "macros", "vba"],
    
    # Soft Skills
    "Agile": ["agile", "scrum", "kanban", "sprint", "jira"],
    "Leadership": ["leadership", "team lead", "management", "mentoring"],
    "Communication": ["communication", "presentation", "stakeholder", "collaboration"],
    "Problem Solving": ["problem solving", "analytical", "critical thinking"],
    
    # Testing
    "Testing": ["testing", "unit test", "pytest", "jest", "selenium", "qa", "quality assurance"],
    "Git": ["git", "github", "gitlab", "version control", "bitbucket"],
}

# LEARNING RESOURCES DATABASE (Skill-Specific!)
LEARNING_RESOURCES = {
    "Python": {
        "level": "Medium",
        "time": "2-3 months",
        "courses": ["Python for Everybody (Coursera)", "Complete Python Bootcamp (Udemy)", "Official Python Docs"],
        "practice": "Build a data dashboard with Pandas + Streamlit. Create a web scraper. Automate daily tasks.",
        "cert": "PCAP (Python Institute)",
        "project": "Personal Finance Tracker - Pandas for data, Matplotlib for viz, SQLite for storage"
    },
    "Java": {
        "level": "Medium-High",
        "time": "3-4 months",
        "courses": ["Java MOOC (University of Helsinki)", "Oracle Java Tutorials"],
        "practice": "Build REST API with Spring Boot. Implement CRUD with database.",
        "cert": "Oracle Certified Associate",
        "project": "Employee Management System - Spring Boot + MySQL + REST API"
    },
    "JavaScript": {
        "level": "Medium",
        "time": "2-3 months",
        "courses": ["freeCodeCamp JavaScript", "JavaScript.info"],
        "practice": "Build interactive portfolio. Create weather app using API. Add animations.",
        "cert": "Portfolio projects over certs",
        "project": "Real-Time Chat App - WebSockets for messaging, deploy on Netlify"
    },
    "Machine Learning": {
        "level": "High",
        "time": "4-6 months",
        "courses": ["Andrew Ng's ML Course (Coursera)", "Fast.ai Practical Deep Learning"],
        "practice": "Kaggle competitions (Titanic). Movie recommender. Image classifier.",
        "cert": "Google ML Engineer Certificate",
        "project": "Housing Price Predictor - scikit-learn, feature engineering, Flask API"
    },
    "Data Science": {
        "level": "Medium-High",
        "time": "3-5 months",
        "courses": ["IBM Data Science Professional", "DataCamp Data Scientist Track"],
        "practice": "Analyze public datasets. Create Plotly visualizations. Write technical blog.",
        "cert": "IBM Data Science Certificate",
        "project": "Customer Churn Analysis - EDA with Pandas, predictive model, Streamlit dashboard"
    },
    "SQL": {
        "level": "Low-Medium",
        "time": "3-6 weeks",
        "courses": ["Mode SQL Tutorial", "SQLBolt (Interactive)", "Codecademy Learn SQL"],
        "practice": "Complex JOINs on sample databases. Optimize queries with indexes. Create views.",
        "cert": "Practice > Certifications",
        "project": "E-commerce Analytics DB - Star schema design, KPI queries, stored procedures"
    },
    "AWS": {
        "level": "Medium-High",
        "time": "2-3 months",
        "courses": ["AWS Cloud Practitioner (Free)", "A Cloud Guru"],
        "practice": "Deploy to S3 + CloudFront. Set up EC2. Create Lambda function (free tier).",
        "cert": "AWS Certified Cloud Practitioner",
        "project": "Serverless Image Resizer - S3, Lambda, API Gateway, DynamoDB"
    },
    "GCP": {
        "level": "Medium-High",
        "time": "2-3 months",
        "courses": ["Google Cloud Skills Boost", "Coursera GCP Specialization"],
        "practice": "Deploy to Cloud Run. Use BigQuery for analytics. Set up Cloud Functions.",
        "cert": "Google Cloud Associate Engineer",
        "project": "Data Pipeline - Cloud Functions, BigQuery, Looker Studio dashboard"
    },
    "Docker": {
        "level": "Medium",
        "time": "2-3 weeks",
        "courses": ["Docker Official Guide", "Docker Mastery (Udemy)"],
        "practice": "Dockerize your apps. Use docker-compose for multi-container. Push to Docker Hub.",
        "cert": "Hands-on experience",
        "project": "Microservices Blog - Frontend + Backend + DB containers with docker-compose"
    },
    "React": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["React Official Docs", "Scrimba Learn React"],
        "practice": "Build 5 apps: todo, weather, quiz, cart, blog. Master hooks (useState, useEffect).",
        "cert": "Portfolio projects",
        "project": "Job Board Dashboard - API fetch, search/filter, React Router, deploy to Vercel"
    },
    "Computer Vision": {
        "level": "High",
        "time": "3-5 months",
        "courses": ["CS231n Stanford (YouTube)", "PyImageSearch tutorials"],
        "practice": "Object detection with YOLO. Image classification with CNN. OCR projects.",
        "cert": "Portfolio > Certifications",
        "project": "Document Scanner - OpenCV preprocessing, text extraction, deploy as web app"
    },
    "NLP": {
        "level": "High",
        "time": "3-4 months",
        "courses": ["NLP Specialization (deeplearning.ai)", "Hugging Face Course"],
        "practice": "Sentiment analyzer. Intent chatbot. Fine-tune BERT on custom data.",
        "cert": "Portfolio projects",
        "project": "Job Description Analyzer - spaCy NER, TF-IDF matching, skill trend visualization"
    },
    "Tableau": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["Tableau Desktop Specialist Path", "Tableau Public Gallery"],
        "practice": "5 viz types: bar, line, map, scatter, heatmap. Build dashboard stories.",
        "cert": "Tableau Desktop Specialist",
        "project": "COVID Tracker - Live data, choropleth map, time series, publish to Tableau Public"
    },
    "Power BI": {
        "level": "Medium",
        "time": "1-2 months",
        "courses": ["Microsoft Power BI Training (Free)", "Enterprise DNA YouTube"],
        "practice": "Connect real data sources. Build interactive dashboards. Publish to Service.",
        "cert": "Microsoft Data Analyst Associate",
        "project": "Sales Dashboard - Star schema, KPI cards, time intelligence, map visual"
    },
    "Excel": {
        "level": "Low-Medium",
        "time": "2-3 weeks",
        "courses": ["Excel Essential Training (LinkedIn)", "Chandoo.org"],
        "practice": "Pivot tables and charts. VLOOKUP, INDEX-MATCH. Macros for automation.",
        "cert": "Microsoft Office Specialist Excel",
        "project": "Budget Manager - Category tracking, formulas, conditional formatting, macro buttons"
    },
    "Git": {
        "level": "Low",
        "time": "1-2 weeks",
        "courses": ["Git Official Tutorial", "Learn Git Branching (Game)"],
        "practice": "Daily Git usage. Feature branches. Resolve merge conflicts. Open source PRs.",
        "cert": "Not needed - practical skill",
        "project": "Practice: 3 feature branches, meaningful commits, rebasing, squashing"
    },
    "Kubernetes": {
        "level": "High",
        "time": "2-3 months",
        "courses": ["Kubernetes for Beginners (Udemy)", "Official K8s Docs"],
        "practice": "Local Minikube cluster. Deployments, services, ingress. Rolling updates.",
        "cert": "CKA (Certified K8s Admin)",
        "project": "Scalable API - 3 replicas, LoadBalancer, health checks, auto-scaling, Prometheus"
    },
    "Agile": {
        "level": "Low-Medium",
        "time": "2-4 weeks",
        "courses": ["Scrum.org Learning Path", "Agile Foundations (LinkedIn)"],
        "practice": "Apply Agile to personal projects. Trello sprints. Daily notes. Retros.",
        "cert": "PSM I (Professional Scrum Master)",
        "project": "Run 2-week sprints on your next project with user stories and velocity tracking"
    },
    "Testing": {
        "level": "Low-Medium",
        "time": "1-2 months",
        "courses": ["Test Automation University (Free)", "Software Testing Fundamentals"],
        "practice": "Unit tests for Python/JS. pytest or Jest. 80%+ coverage. GitHub Actions CI.",
        "cert": "ISTQB Foundation Level",
        "project": "Test To-Do API - Unit, integration, mocked tests, 90% coverage, CI on every PR"
    },
}

# Default for unmapped skills
DEFAULT_RESOURCE = {
    "level": "Varies",
    "time": "1-3 months",
    "courses": ["Search Coursera, Udemy, YouTube"],
    "practice": "Start with official docs. Build 2-3 small projects. Join communities.",
    "cert": "Check for industry certifications",
    "project": "Find a real problem, break into milestones, build incrementally, share on GitHub"
}
