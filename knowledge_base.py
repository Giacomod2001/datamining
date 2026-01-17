# =============================================================================
# EXTENDED KNOWLEDGE BASE v2.1 (REFACTORED)
# =============================================================================

# =============================================================================
# SECTION 1: JOB ARCHETYPES (CORRECTED & EXPANDED)
# =============================================================================

JOB_ARCHETYPES_EXTENDED = {
    # ========== SOFTWARE ENGINEERING ==========
    'Software Engineer': {
        'primary_skills': ['Algorithms', 'Git', 'Programming', 'System Design', 'Testing'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€35k-65k',
        'career_path': 'Junior Software Engineer -> Senior Software Engineer -> Lead Software Engineer -> Engineering Manager',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Startups', 'Consulting', 'Banks'],
        'transition_from': ['Computer Science Degree', 'Bootcamp', 'Self-taught'],
        'prerequisite_skills': ['Programming fundamentals', 'Data structures'],
        'learning_time': '6-12 months proficiency'
    },
    
    'Frontend Developer': {
        'primary_skills': ['CSS', 'Git', 'HTML', 'JavaScript', 'React', 'UI Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail'],
        'market_demand': 'high',
        'salary_range_italy': '€32k-58k',
        'career_path': 'Junior Frontend Developer -> Senior Frontend Developer -> Lead Frontend Developer -> Frontend Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Startups', 'Digital Agencies', 'E-commerce'],
        'transition_from': ['Web Design', 'Computer Science', 'Bootcamp'],
        'prerequisite_skills': ['HTML/CSS basics', 'JavaScript fundamentals'],
        'learning_time': '6-12 months proficiency'
    },
    
    'Backend Developer': {
        'primary_skills': ['Docker', 'Java', 'Microservices', 'Python', 'Redis', 'SQL', 'System Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Analytical Thinking'],
        'market_demand': 'high',
        'salary_range_italy': '€35k-62k',
        'career_path': 'Junior Backend Developer -> Senior Backend Developer -> Lead Backend Developer -> Backend Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Startups', 'Consulting', 'Fintech'],
        'transition_from': ['Computer Science Degree', 'Software Engineering'],
        'prerequisite_skills': ['Programming', 'Database basics'],
        'learning_time': '6-12 months proficiency'
    },
    
    'Full Stack Developer': {
        'primary_skills': ['DevOps', 'Git', 'JavaScript', 'Node.js', 'Python', 'React', 'SQL'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Multitasking'],
        'market_demand': 'very high',
        'salary_range_italy': '€38k-68k',
        'career_path': 'Junior Full Stack Developer -> Senior Full Stack Developer -> Lead Full Stack Developer -> Tech Lead',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Startups', 'Tech Companies', 'Scale-ups', 'Consulting'],
        'transition_from': ['Frontend/Backend', 'Computer Science'],
        'prerequisite_skills': ['Full web stack understanding'],
        'learning_time': '12-18 months proficiency'
    },
    
    # ========== DATA & ANALYTICS ==========
    'Data Analyst': {
        'primary_skills': ['Data Visualization', 'Excel', 'Python', 'SQL', 'Statistics'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€32k-55k',
        'career_path': 'Junior Data Analyst -> Senior Data Analyst -> Lead Data Analyst -> Analytics Manager',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Corporates', 'Startups', 'Consulting', 'E-commerce'],
        'transition_from': ['Business', 'Economics', 'Engineering'],
        'prerequisite_skills': ['Excel', 'Basic statistics'],
        'learning_time': '3-6 months proficiency'
    },
    
    'Data Scientist': {
        'primary_skills': ['Deep Learning', 'Machine Learning', 'Python', 'SQL', 'Statistics'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€40k-70k',
        'career_path': 'Junior Data Scientist -> Senior Data Scientist -> Lead Data Scientist -> Head of Data Science',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Consulting', 'Research', 'Finance'],
        'transition_from': ['STEM Degree', 'Data Analyst', 'Research'],
        'prerequisite_skills': ['Statistics', 'Programming', 'ML basics'],
        'learning_time': '12-18 months proficiency'
    },
    
    'Data Engineer': {
        'primary_skills': ['BigQuery', 'Cloud Computing', 'ETL', 'Python', 'SQL', 'Spark'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€42k-72k',
        'career_path': 'Junior Data Engineer -> Senior Data Engineer -> Lead Data Engineer -> Data Platform Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Data-driven companies', 'Consulting'],
        'transition_from': ['Software Engineering', 'Database Admin'],
        'prerequisite_skills': ['SQL', 'Programming', 'ETL concepts'],
        'learning_time': '6-12 months proficiency'
    },
    
    'Business Intelligence Analyst': {
        'primary_skills': ['Data Modelling', 'Power BI', 'Reporting', 'SQL', 'Tableau'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€35k-58k',
        'career_path': 'Junior BI Analyst -> Senior BI Analyst -> Lead BI Analyst -> BI Manager',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Corporates', 'Consulting', 'Retail', 'Manufacturing'],
        'transition_from': ['Data Analyst', 'Business Analyst'],
        'prerequisite_skills': ['SQL', 'BI tools', 'Business acumen'],
        'learning_time': '6-9 months proficiency'
    },
    
    'Machine Learning Engineer': {
        'primary_skills': ['Cloud Computing', 'MLOps', 'Machine Learning', 'Python', 'TensorFlow'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€45k-75k',
        'career_path': 'Junior ML Engineer -> Senior ML Engineer -> Lead ML Engineer -> ML Research Scientist',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Research Labs', 'Automotive', 'Healthcare'],
        'transition_from': ['Data Science', 'Software Engineering', 'PhD'],
        'prerequisite_skills': ['ML fundamentals', 'Python', 'Math'],
        'learning_time': '12-18 months proficiency'
    },
    
    'Analytics Engineer': {
        'primary_skills': ['BigQuery', 'Data Modeling', 'Git', 'Python', 'SQL', 'Snowflake', 'dbt'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€40k-65k',
        'career_path': 'Junior Analytics Engineer -> Senior Analytics Engineer -> Lead Analytics Engineer -> Analytics Platform Lead',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Data Teams', 'Scale-ups'],
        'transition_from': ['Data Analyst', 'Data Engineer'],
        'prerequisite_skills': ['SQL', 'Python', 'dbt'],
        'learning_time': '6-12 months proficiency'
    },
    
    'MLOps Engineer': {
        'primary_skills': ['CI/CD', 'DevOps', 'Docker', 'Kubernetes', 'Machine Learning', 'Python'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€45k-75k',
        'career_path': 'Junior MLOps Engineer -> Senior MLOps Engineer -> Lead MLOps Engineer -> ML Platform Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'AI Startups', 'Research', 'Cloud Providers'],
        'transition_from': ['DevOps', 'Data Engineering', 'ML Engineering'],
        'prerequisite_skills': ['DevOps', 'ML basics', 'Cloud'],
        'learning_time': '9-15 months proficiency'
    },
    
    'AI Business Analyst': {
        'primary_skills': ['Artificial Intelligence', 'Business Analysis', 'Data Analysis', 'Python', 'Strategy'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Strategic Thinking'],
        'market_demand': 'emerging high',
        'salary_range_italy': '€38k-62k',
        'career_path': 'Junior AI Business Analyst -> Senior AI Business Analyst -> Lead AI Strategy Consultant',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Consulting', 'Tech Companies', 'Innovation Labs'],
        'transition_from': ['Business Analyst', 'Data Analyst'],
        'prerequisite_skills': ['Business analysis', 'AI literacy'],
        'learning_time': '6-12 months proficiency'
    },
    
    # ========== DESIGN & UX ==========
    'UX Designer': {
        'primary_skills': ['Figma', 'Prototyping', 'UX Design', 'User Research', 'Wireframing'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Empathy', 'Creativity'],
        'market_demand': 'high',
        'salary_range_italy': '€32k-58k',
        'career_path': 'Junior UX Designer -> Senior UX Designer -> Lead UX Designer -> UX Director',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Agencies', 'Startups', 'Consulting'],
        'transition_from': ['Graphic Design', 'Psychology', 'HCI'],
        'prerequisite_skills': ['Design thinking', 'User research basics'],
        'learning_time': '6-12 months proficiency'
    },
    
    'UI Designer': {
        'primary_skills': ['Adobe Creative Suite', 'Figma', 'Typography', 'UI Design', 'Visual Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail', 'Creativity'],
        'market_demand': 'high',
        'salary_range_italy': '€30k-55k',
        'career_path': 'Junior UI Designer -> Senior UI Designer -> Lead UI Designer -> Design Director',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Agencies', 'Startups', 'E-commerce'],
        'transition_from': ['Graphic Design', 'Visual Arts'],
        'prerequisite_skills': ['Design tools', 'Visual design principles'],
        'learning_time': '6-9 months proficiency'
    },
    
    # ========== DEVOPS & INFRASTRUCTURE ==========
    'DevOps Engineer': {
        'primary_skills': ['CI/CD', 'Cloud Computing', 'DevOps', 'Docker', 'Kubernetes'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€42k-72k',
        'career_path': 'Junior DevOps Engineer -> Senior DevOps Engineer -> Lead DevOps Engineer -> DevOps Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Startups', 'Cloud Providers', 'Consulting'],
        'transition_from': ['System Admin', 'Software Engineering'],
        'prerequisite_skills': ['Linux', 'Scripting', 'Cloud basics'],
        'learning_time': '9-15 months proficiency'
    },
    
    'Cybersecurity Analyst': {
        'primary_skills': ['Compliance', 'Cybersecurity', 'Incident Response', 'Network Security', 'Risk Management'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range_italy': '€38k-68k',
        'career_path': 'Junior Cybersecurity Analyst -> Senior Cybersecurity Analyst -> Cybersecurity Manager -> CISO',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Banks', 'Corporates', 'Consulting', 'Government'],
        'transition_from': ['IT Support', 'Network Admin', 'Computer Science'],
        'prerequisite_skills': ['Networking', 'Security basics', 'Linux'],
        'learning_time': '12-18 months proficiency'
    },
    
    'IT Support Specialist': {
        'primary_skills': ['Customer Service', 'Hardware', 'IT Support', 'Troubleshooting', 'Windows'],
        'soft_skills': ['Adaptability', 'Communication', 'Empathy', 'Problem Solving', 'Patience'],
        'market_demand': 'stable',
        'salary_range_italy': '€24k-38k',
        'career_path': 'IT Support Specialist -> Senior IT Support -> IT Support Manager -> IT Operations Manager',
        'geographic_focus': ['Italy', 'Hybrid'],
        'remote_friendly': False,
        'typical_employer': ['Corporates', 'MSPs', 'Schools', 'Healthcare'],
        'transition_from': ['Entry Level', 'IT Certifications'],
        'prerequisite_skills': ['Windows', 'Basic networking'],
        'learning_time': '3-6 months proficiency'
    },
    
    'System Administrator': {
        'primary_skills': ['Cloud Computing', 'Linux', 'Networking', 'Scripting', 'Windows Server'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail'],
        'market_demand': 'stable',
        'salary_range_italy': '€32k-55k',
        'career_path': 'Junior System Administrator -> Senior System Administrator -> Infrastructure Manager',
        'geographic_focus': ['Italy', 'Hybrid'],
        'remote_friendly': True,
        'typical_employer': ['Corporates', 'MSPs', 'Government', 'Education'],
        'transition_from': ['IT Support', 'Network Admin'],
        'prerequisite_skills': ['Linux/Windows', 'Networking', 'Scripting'],
        'learning_time': '6-12 months proficiency'
    },
    
    # ========== PRODUCT & GROWTH ==========
    'Product Manager': {
        'primary_skills': ['Agile', 'Data Analysis', 'Product Management', 'Roadmap', 'User Stories'],
        'soft_skills': ['Adaptability', 'Communication', 'Leadership', 'Problem Solving', 'Strategic Thinking', 'Team Management'],
        'market_demand': 'high',
        'salary_range_italy': '€45k-85k',
        'career_path': 'Associate PM -> Product Manager -> Senior PM -> Group PM -> VP Product',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'Startups', 'Scale-ups', 'Corporates'],
        'transition_from': ['Business Analyst', 'Engineering', 'Consulting'],
        'prerequisite_skills': ['Product thinking', 'Data literacy'],
        'learning_time': 'Continuous specialization'
    },
    
    'Technical Product Manager': {
        'primary_skills': ['APIs', 'Agile', 'Data Analysis', 'Product Management', 'System Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Leadership', 'Problem Solving', 'Strategic Thinking', 'Team Management'],
        'market_demand': 'high',
        'salary_range_italy': '€50k-90k',
        'career_path': 'Technical PM -> Senior Technical PM -> Principal PM -> Director of Product',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Tech Companies', 'SaaS', 'Platform Companies'],
        'transition_from': ['Software Engineering', 'Product Manager'],
        'prerequisite_skills': ['Technical background', 'Product skills'],
        'learning_time': 'Continuous specialization'
    },
    
    'Growth Engineer': {
        'primary_skills': ['A/B Testing', 'Automation', 'Data Analysis', 'JavaScript', 'Marketing', 'Python'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€40k-68k',
        'career_path': 'Junior Growth Engineer -> Senior Growth Engineer -> Lead Growth Engineer -> Head of Growth',
        'geographic_focus': ['Italy', 'Remote', 'EU', 'US'],
        'remote_friendly': True,
        'typical_employer': ['Startups', 'Scale-ups', 'SaaS Companies'],
        'transition_from': ['Software Engineering', 'Marketing', 'Data'],
        'prerequisite_skills': ['Programming', 'Analytics', 'Marketing basics'],
        'learning_time': '6-12 months proficiency'
    },
    
    # ========== SOLUTIONS & ARCHITECTURE ==========
    'Solutions Architect': {
        'primary_skills': ['AWS', 'Azure', 'Cloud Computing', 'Communication', 'Sales', 'System Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Empathy', 'Negotiation', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range_italy': '€50k-90k',
        'career_path': 'Solutions Architect -> Senior SA -> Principal SA -> Enterprise Architect',
        'geographic_focus': ['Italy', 'Remote', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Cloud Providers', 'Consulting', 'System Integrators'],
        'transition_from': ['Software Engineering', 'Infrastructure'],
        'prerequisite_skills': ['Cloud platforms', 'Architecture patterns'],
        'learning_time': 'Continuous specialization'
    },
    
    # ========== MARKETING ==========
    'Marketing Manager': {
        'primary_skills': ['Analytics', 'Budgeting', 'Campaign Management', 'Leadership', 'Marketing Strategy'],
        'soft_skills': ['Adaptability', 'Communication', 'Leadership', 'Problem Solving', 'Strategic Thinking', 'Team Management'],
        'market_demand': 'high',
        'salary_range_italy': '€40k-70k',
        'career_path': 'Marketing Specialist -> Marketing Manager -> Senior Marketing Manager -> CMO',
        'geographic_focus': ['Italy', 'Hybrid', 'EU'],
        'remote_friendly': True,
        'typical_employer': ['Corporates', 'Agencies', 'Startups', 'E-commerce'],
        'transition_from': ['Marketing Specialist', 'Communications', 'Business'],
        'prerequisite_skills': ['Marketing fundamentals', 'Digital marketing'],
        'learning_time': 'Continuous specialization'
    },
    
    # ========== ENERGY & SPECIALIZED ENGINEERING ==========
    'Energy Trader': {
        'primary_skills': ['Energy Markets', 'Python', 'Financial Modeling', 'Risk Management', 'Power Systems', 'Trading Strategies', 'Commodities', 'Derivatives', 'Hedging'],
        'soft_skills': ['Stress Management', 'Decision-Making', 'Negotiation', 'Analytical Thinking'],
        'market_demand': 'emerging high',
        'salary_range_italy': '€50k-120k',
        'career_path': 'Analyst → Junior Trader → Senior Trader → Trading Manager → Head of Trading',
        'geographic_focus': ['Italy', 'EU Energy Hubs'],
        'remote_friendly': False,
        'typical_employer': ['Enel', 'Terna', 'Eni', 'Trading Desks', 'Energy Brokers'],
        'transition_from': ['Finance', 'Engineering', 'Data Science'],
        'prerequisite_skills': ['Finance basics', 'Energy Market knowledge'],
        'learning_time': '6-12 months onboarding'
    },
    
    'Manufacturing Data Scientist': {
        'primary_skills': ['Python', 'Machine Learning', 'Time Series Forecasting', 'Manufacturing Domain', 'Data Engineering', 'IIoT', 'Predictive Maintenance', 'Computer Vision', 'Edge Computing'],
        'soft_skills': ['Problem-solving', 'Domain curiosity', 'Communication'],
        'market_demand': 'very high',
        'salary_range_italy': '€45k-75k',
        'career_path': 'Data Analyst → ML Engineer → Principal Data Scientist → Director of Data Science',
        'geographic_focus': ['Lombardy', 'Emilia-Romagna', 'Veneto'],
        'remote_friendly': True,
        'typical_employer': ['Manufacturing companies', 'Industry 4.0 startups', 'Consultancies'],
        'transition_from': ['Data Science', 'Engineering', 'Operations'],
        'prerequisite_skills': ['ML fundamentals', 'Python'],
        'learning_time': '3-6 months domain learning'
    },
}

# =============================================================================
# SECTION 2: INFERENCE SYSTEM (REFACTORED)
# =============================================================================

# 2.1 CHILD → PARENT INFERENCES (Hierarchical "If you know X, you know Y")
# Logic: Having the child skill implies having the parent skill
# Example: "React" → "Frontend Development" means if you know React, you know Frontend Dev
SKILL_HIERARCHY = {
    # Programming Languages → General Programming
    "Python": ["Programming", "Scripting"],
    "Java": ["Programming", "Object Oriented Programming"],
    "JavaScript": ["Programming", "Frontend Development"],
    "TypeScript": ["Programming", "JavaScript", "Frontend Development"],
    "C++": ["Programming", "Object Oriented Programming"],
    "C#": ["Programming", "Object Oriented Programming"],
    "Go": ["Programming", "Backend Development"],
    "Rust": ["Programming", "Systems Programming"],
    "Ruby": ["Programming", "Scripting"],
    "PHP": ["Programming", "Web Development"],
    "Swift": ["Programming", "Mobile Development"],
    "Kotlin": ["Programming", "Mobile Development"],
    
    # Frontend Frameworks → Frontend Development
    "React": ["JavaScript", "Frontend Development", "UI Development"],
    "Angular": ["JavaScript", "TypeScript", "Frontend Development"],
    "Vue.js": ["JavaScript", "Frontend Development"],
    "Svelte": ["JavaScript", "Frontend Development"],
    "Next.js": ["React", "JavaScript", "Frontend Development", "Full Stack"],
    
    # Backend Frameworks → Backend Development
    "Django": ["Python", "Backend Development", "Web Development"],
    "Flask": ["Python", "Backend Development", "Web Development"],
    "FastAPI": ["Python", "Backend Development", "API Development"],
    "Spring Boot": ["Java", "Backend Development", "Enterprise Development"],
    "Node.js": ["JavaScript", "Backend Development", "Web Development"],
    "Express.js": ["Node.js", "JavaScript", "Backend Development"],
    
    # Cloud Platforms → Cloud Computing
    "AWS": ["Cloud Computing", "Infrastructure"],
    "Azure": ["Cloud Computing", "Infrastructure"],
    "GCP": ["Cloud Computing", "Infrastructure", "Google Cloud"],
    "Google Cloud": ["Cloud Computing", "Infrastructure"],
    
    # DevOps Tools → DevOps
    "Docker": ["Containerization", "DevOps"],
    "Kubernetes": ["Containerization", "Orchestration", "DevOps", "Cloud Native"],
    "Terraform": ["Infrastructure as Code", "DevOps", "Cloud Computing"],
    "Ansible": ["Configuration Management", "DevOps", "Automation"],
    "Jenkins": ["CI/CD", "DevOps", "Automation"],
    "GitLab CI": ["CI/CD", "DevOps", "Git"],
    "GitHub Actions": ["CI/CD", "DevOps", "Git"],
    
    # Version Control
    "Git": ["Version Control"],
    "GitHub": ["Version Control", "Git", "Collaboration"],
    "GitLab": ["Version Control", "Git", "CI/CD"],
    
    # Databases → Database Management
    "SQL": ["Database Management", "Data Querying"],
    "MySQL": ["Database Management", "SQL", "Relational Databases"],
    "PostgreSQL": ["Database Management", "SQL", "Relational Databases"],
    "MongoDB": ["Database Management", "NoSQL"],
    "Redis": ["Database Management", "NoSQL", "Caching"],
    "Cassandra": ["Database Management", "NoSQL", "Distributed Systems"],
    
    # Data Science & ML
    "Pandas": ["Python", "Data Analysis", "Data Manipulation"],
    "NumPy": ["Python", "Data Analysis", "Scientific Computing"],
    "Scikit-learn": ["Python", "Machine Learning", "Data Science"],
    "TensorFlow": ["Deep Learning", "Machine Learning", "AI"],
    "PyTorch": ["Deep Learning", "Machine Learning", "AI"],
    "Keras": ["Deep Learning", "Machine Learning", "TensorFlow"],
    
    # BI & Visualization Tools
    "Tableau": ["Data Visualization", "BI Tools", "Analytics"],
    "Power BI": ["Data Visualization", "BI Tools", "Analytics"],
    "Looker": ["Data Visualization", "BI Tools", "Analytics"],
    "Looker Studio": ["Data Visualization", "BI Tools", "Google Analytics"],
    
    # Spreadsheets
    "Excel": ["Spreadsheets", "Data Analysis", "Business Analysis"],
    "Google Sheets": ["Spreadsheets", "Data Analysis"],
    
    # Digital Marketing Tools
    "Google Ads": ["SEM", "PPC", "Digital Marketing"],
    "Facebook Ads": ["Social Media Marketing", "Digital Marketing", "PPC"],
    "Google Analytics": ["Web Analytics", "Digital Marketing", "Data Analysis"],
    "GA4": ["Web Analytics", "Google Analytics", "Digital Marketing"],
    "SEO": ["Digital Marketing", "Content Marketing"],
    
    # Project Management
    "Jira": ["Project Management", "Agile"],
    "Trello": ["Project Management", "Kanban"],
    "Asana": ["Project Management", "Task Management"],
    "Scrum": ["Agile", "Project Management"],
    "Kanban": ["Agile", "Project Management"],
    
    # Design Tools
    "Figma": ["UI Design", "Design Tools", "Prototyping"],
    "Sketch": ["UI Design", "Design Tools"],
    "Adobe XD": ["UI Design", "Design Tools", "Prototyping"],
    "Photoshop": ["Photo Editing", "Graphic Design"],
    "Illustrator": ["Vector Graphics", "Graphic Design"],
    
    # Financial & Business
    "Budgeting": ["Financial Management", "Business Management"],
    "Financial Modeling": ["Financial Analysis", "Excel"],
    
    # CRM
    "Salesforce": ["CRM", "Sales Management"],
    "HubSpot": ["CRM", "Marketing Automation"],
    
    # Energy & Engineering (User Requested)
    "Energy Engineering": ["Thermodynamics", "Power Systems", "Energy Efficiency"],
    "Renewable Energy": ["Solar Energy", "Wind Energy", "Sustainability"],
    "Photovoltaics": ["Solar Energy", "Renewable Energy"],
    "PV": ["Solar Energy", "Photovoltaics"],
    "Matlab": ["Programming", "Simulink", "Engineering Software"],
    "PVSyst": ["Solar Energy", "Energy Modeling"],
    "AutoCAD": ["CAD", "Technical Drawing", "Design Software"],
    
    # Languages
    "English": ["Languages", "Communication"],
    "Italian": ["Languages", "Communication"],
    "French": ["Languages", "Communication"],
    "German": ["Languages", "Communication"],
    "Spanish": ["Languages", "Communication"],
}

# 2.2 PARENT → CHILD IMPLICATIONS (Skills that imply knowledge of related skills)
# Logic: If you master the parent, you likely know the children
# Example: "Data Science" implies ["Python", "Statistics", "SQL"]
SKILL_IMPLICATIONS = {
    # High-level domains imply foundational skills
    "Data Science": ["Machine Learning", "Statistics", "Data Analysis", "Programming", "Python", "SQL"],
    "Machine Learning": ["Statistics", "Data Analysis", "Modeling", "Python", "Mathematics"],
    "Deep Learning": ["Machine Learning", "Neural Networks", "Statistics", "Python"],
    "Artificial Intelligence": ["Machine Learning", "Programming", "Algorithms"],
    
    "Full Stack Development": ["Frontend Development", "Backend Development", "Database Management", "API Development"],
    "Backend Development": ["Database Management", "API Development", "Server Management"],
    "Frontend Development": ["HTML", "CSS", "JavaScript", "UI/UX Basics"],
    
    "DevOps": ["CI/CD", "Cloud Computing", "Containerization", "Scripting", "Automation"],
    "Cloud Computing": ["Networking", "Security Basics", "Infrastructure"],
    
    "Digital Marketing": ["Campaign Management", "Analytics", "Content Strategy", "SEO", "SEM"],
    "SEO": ["Content Marketing", "Analytics", "Keyword Research"],
    "SEM": ["PPC", "Google Ads", "Analytics"],
    "Social Media Marketing": ["Content Creation", "Community Management", "Analytics"],
    
    "Project Management": ["Planning", "Risk Management", "Budgeting", "Team Coordination"],
    "Product Management": ["Market Research", "User Research", "Data Analysis", "Agile"],
    
    "Business Intelligence": ["Data Analysis", "Reporting", "Visualization", "SQL"],
    "Data Analysis": ["Excel", "Statistics", "Critical Thinking"],
    "Analytics": ["Data Analysis", "Reporting", "Metrics"],
    
    "UX Design": ["User Research", "Prototyping", "Wireframing", "Usability Testing"],
    "UI Design": ["Visual Design", "Typography", "Color Theory", "Design Tools"],
    
    "Cybersecurity": ["Network Security", "Risk Management", "Compliance", "Incident Response"],
    "Network Security": ["Networking", "Firewall Management", "Security Protocols"],
}

# 2.3 SKILL CLUSTERS (Transferable/Equivalent Skills)
# Logic: Skills in the same cluster are highly transferable
# Example: If you know Tableau, you can quickly learn Power BI
SKILL_CLUSTERS = {
    # BI & Visualization Tools (High Transferability)
    "bi_tools": {
        "name": "Business Intelligence Tools",
        "skills": {"Tableau", "Power BI", "Looker", "Looker Studio", "QlikView", "Qlik Sense", "Data Studio", "Metabase"},
        "transferability": "high"
    },
    
    # Cloud Platforms (Conceptual Transferability)
    "cloud_platforms": {
        "name": "Cloud Platforms",
        "skills": {"AWS", "Azure", "GCP", "Google Cloud", "IBM Cloud", "Oracle Cloud", "Cloud Computing"},
        "transferability": "medium-high"
    },
    
    # Relational Databases
    "sql_databases": {
        "name": "SQL Databases",
        "skills": {"MySQL", "PostgreSQL", "SQL Server", "Oracle Database", "MariaDB", "SQLite", "SQL"},
        "transferability": "high"
    },
    
    # NoSQL Databases
    "nosql_databases": {
        "name": "NoSQL Databases",
        "skills": {"MongoDB", "Cassandra", "Redis", "DynamoDB", "Couchbase", "Neo4j"},
        "transferability": "medium"
    },
    
    # Python Web Frameworks
    "python_frameworks": {
        "name": "Python Web Frameworks",
        "skills": {"Django", "Flask", "FastAPI", "Pyramid", "Tornado"},
        "transferability": "high"
    },
    
    # JavaScript Frontend Frameworks
    "frontend_frameworks": {
        "name": "Frontend Frameworks",
        "skills": {"React", "Vue", "Angular", "Svelte", "Ember", "Next.js", "Nuxt.js"},
        "transferability": "high"
    },
    
    # Containerization & Orchestration
    "containerization": {
        "name": "Containerization",
        "skills": {"Docker", "Podman", "LXC", "Kubernetes", "OpenShift", "Docker Swarm"},
        "transferability": "high"
    },
    
    # IaC Tools
    "iac_tools": {
        "name": "Infrastructure as Code",
        "skills": {"Terraform", "Ansible", "CloudFormation", "Pulumi", "Chef", "Puppet"},
        "transferability": "medium-high"
    },
    
    # CI/CD Tools
    "cicd_tools": {
        "name": "CI/CD Tools",
        "skills": {"Jenkins", "GitLab CI", "GitHub Actions", "CircleCI", "Travis CI", "Azure DevOps"},
        "transferability": "high"
    },
    
    # Web Analytics
    "web_analytics": {
        "name": "Web Analytics",
        "skills": {"Google Analytics", "GA4", "Adobe Analytics", "Mixpanel", "Matomo", "Amplitude"},
        "transferability": "high"
    },
    
    # CRM Systems
    "crm_systems": {
        "name": "CRM Systems",
        "skills": {"Salesforce", "HubSpot", "Zoho CRM", "Microsoft Dynamics", "Pipedrive", "SugarCRM"},
        "transferability": "medium-high"
    },
    
    # Office/Productivity
    "spreadsheets": {
        "name": "Spreadsheets",
        "skills": {"Excel", "Google Sheets", "Numbers", "LibreOffice Calc"},
        "transferability": "very high"
    },
    
    "presentation_tools": {
        "name": "Presentation Tools",
        "skills": {"PowerPoint", "Keynote", "Google Slides", "Prezi", "Canva"},
        "transferability": "very high"
    },
    
    # Project Management Tools
    "pm_tools": {
        "name": "Project Management Tools",
        "skills": {"Jira", "Asana", "Trello", "Monday.com", "ClickUp", "Basecamp", "Notion"},
        "transferability": "very high"
    },
    
    # Design Tools - Vector Graphics
    "vector_graphics": {
        "name": "Vector Graphics",
        "skills": {"Illustrator", "CorelDRAW", "Inkscape", "Affinity Designer"},
        "transferability": "high"
    },
    
    # Design Tools - Photo Editing
    "photo_editing": {
        "name": "Photo Editing",
        "skills": {"Photoshop", "Lightroom", "GIMP", "Affinity Photo", "Capture One"},
        "transferability": "high"
    },
    
    # Design Tools - UI/UX
    "ui_design_tools": {
        "name": "UI Design Tools",
        "skills": {"Figma", "Sketch", "Adobe XD", "InVision", "Framer", "Penpot"},
        "transferability": "very high"
    },
    
    # Digital Advertising
    "digital_ads": {
        "name": "Digital Advertising",
        "skills": {"Google Ads", "Facebook Ads", "LinkedIn Ads", "Bing Ads", "Twitter Ads", "PPC", "SEM"},
        "transferability": "high"
    },
    
    # Social Media Platforms
    "social_media": {
        "name": "Social Media",
        "skills": {"Instagram", "Facebook", "LinkedIn", "TikTok", "Twitter", "YouTube", "Pinterest"},
        "transferability": "high"
    },
    
    # Programming Languages (Same Paradigm)
    "oop_languages": {
        "name": "Object-Oriented Languages",
        "skills": {"Java", "C++", "C#", "Python", "Ruby", "Swift", "Kotlin"},
        "transferability": "medium-high"
    },
    
    "functional_languages": {
        "name": "Functional Languages",
        "skills": {"Haskell", "Scala", "Clojure", "Erlang", "F#", "Elixir"},
        "transferability": "medium"
    },
    
    # ML/DL Frameworks
    "ml_frameworks": {
        "name": "Machine Learning Frameworks",
        "skills": {"TensorFlow", "PyTorch", "Keras", "scikit-learn", "XGBoost", "LightGBM"},
        "transferability": "medium-high"
    },
    
    # Data Processing
    "big_data_tools": {
        "name": "Big Data Tools",
        "skills": {"Spark", "Hadoop", "Hive", "Flink", "Kafka", "Databricks"},
        "transferability": "medium"
    },
    
    # Data Warehouses
    "data_warehouses": {
        "name": "Data Warehouses",
        "skills": {"Snowflake", "BigQuery", "Redshift", "Databricks", "Synapse"},
        "transferability": "high"
    },
}

# =============================================================================
# SECTION 3: SKILL CLASSIFICATION
# =============================================================================

# 3.1 Project-Based Skills (Learned through practice)
PROJECT_BASED_SKILLS = {
    # Technical
    "Programming", "Web Development", "App Development", "Software Development",
    "Machine Learning", "Data Science", "Data Analysis", "Data Engineering",
    "Cloud Computing", "DevOps", "Cybersecurity",
    
    # Creative
    "Graphic Design", "UI Design", "UX Design", "Video Production", "Photography",
    "Writing", "Copywriting", "Content Creation", "Animation",
    
    # Research
    "Research", "Academic Research", "Market Research", "User Research",
    
    # Business
    "Business Development", "Entrepreneurship", "Consulting", "Product Management",
    "Project Management", "Business Analysis",
}

# 3.2 Seniority Keywords
SENIORITY_KEYWORDS = {
    "Entry Level": [
        "entry level", "junior", "intern", "internship", "trainee", 
        "graduate", "associate", "stage", "tirocinio", "student", 
        "studente", "laureando", "neo-laureato", "apprentice", "beginner"
    ],
    "Mid Level": [
        "mid level", "mid-level", "experienced", "specialist", 
        "analyst", "consultant", "manager", "gestione", "professional"
    ],
    "Senior Level": [
        "senior", "lead", "principal", "head of", "director", 
        "vp", "executive", "chief", "partner", "founder", "expert",
        "staff", "distinguished"
    ],
}

# =============================================================================
# SECTION 4: HARD SKILLS (CONSOLIDATED & CLEAN)
# =============================================================================

HARD_SKILLS = {
    # ========== PROGRAMMING & TECHNOLOGY ==========
    "Programming": ["programming", "coding", "sviluppo software", "programmazione", "software development"],
    "Python": ["python", "py"],
    "JavaScript": ["javascript", "js", "ecmascript", "es6", "es2015"],
    "TypeScript": ["typescript", "ts"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "C#": ["c#", "csharp"],
    "Go": ["golang", "go"],
    "Rust": ["rust"],
    "Ruby": ["ruby"],
    "PHP": ["php"],
    "Swift": ["swift"],
    "Kotlin": ["kotlin"],
    "SQL": ["sql", "t-sql", "pl/sql"],
    
    # Frontend
    "Frontend Development": ["frontend", "front-end", "ui development"],
    "HTML": ["html", "html5"],
    "CSS": ["css", "css3", "scss", "sass", "less"],
    "React": ["react", "reactjs", "react.js"],
    "Angular": ["angular", "angularjs"],
    "Vue": ["vue", "vuejs", "vue.js"],
    "Next.js": ["nextjs", "next.js"],
    "State Management": ["redux", "mobx", "zustand", "recoil", "pinia", "context api"],
    "Responsive Design": ["responsive", "mobile-first", "adaptive design"],
    
    # Backend
    "Backend Development": ["backend", "back-end", "server-side"],
    "Node.js": ["nodejs", "node.js", "node"],
    "Django": ["django"],
    "Flask": ["flask"],
    "FastAPI": ["fastapi"],
    "Spring": ["spring", "spring boot"],
    "Microservices": ["microservices", "micro-services", "service-oriented architecture"],
    "API Development": ["rest", "restful", "graphql", "grpc", "api"],
    "Serverless": ["serverless", "lambda", "cloud functions", "faas"],
    
    # DevOps & Cloud
    "DevOps": ["devops", "sre", "site reliability"],
    "Cloud Computing": ["cloud", "cloud computing"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "GCP": ["gcp", "google cloud platform", "google cloud"],
    "Docker": ["docker", "containerization"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Terraform": ["terraform", "iac", "infrastructure as code"],
    "Ansible": ["ansible"],
    "Jenkins": ["jenkins"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "continuous deployment"],
    "GitLab CI": ["gitlab ci", "gitlab"],
    "GitHub Actions": ["github actions"],
    
    # Databases
    "Database Management": ["database", "db", "database management"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo"],
    "Redis": ["redis"],
    "Elasticsearch": ["elasticsearch", "elastic"],
    
    # Version Control
    "Git": ["git"],
    "GitHub": ["github"],
    
    # ========== DATA & ANALYTICS ==========
    "Data Analysis": ["data analysis", "analisi dati", "data analytics"],
    "Data Science": ["data science", "data scientist"],
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning", "neural networks"],
    "Artificial Intelligence": ["artificial intelligence", "ai"],
    "Statistics": ["statistics", "statistica", "statistical analysis"],
    "Data Visualization": ["data visualization", "data viz", "visualizzazione dati"],
    "Excel": ["excel", "microsoft excel", "spreadsheet"],
    "Python (Data)": ["pandas", "numpy", "scipy"],
    "R": ["r", "r programming"],
    "Tableau": ["tableau"],
    "Power BI": ["power bi", "powerbi"],
    "Looker": ["looker"],
    "SQL (Analytics)": ["sql", "query", "data querying"],
    "BigQuery": ["bigquery"],
    "Snowflake": ["snowflake"],
    "Spark": ["apache spark", "pyspark"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "dbt": ["dbt", "data build tool"],
    "ETL": ["etl", "elt", "data pipeline"],
    "Data Modeling": ["data modeling", "data modelling"],
    
    # ========== MARKETING & DIGITAL ==========
    "Digital Marketing": ["digital marketing", "marketing digitale"],
    "SEO": ["seo", "search engine optimization"],
    "SEM": ["sem", "search engine marketing"],
    "PPC": ["ppc", "pay per click"],
    "Google Ads": ["google ads", "adwords"],
    "Facebook Ads": ["facebook ads", "meta ads"],
    "Social Media Marketing": ["social media marketing", "smm"],
    "Content Marketing": ["content marketing"],
    "Email Marketing": ["email marketing"],
    "Marketing Analytics": ["marketing analytics"],
    "Google Analytics": ["google analytics", "ga4"],
    "Copywriting": ["copywriting", "copy"],
    "Branding": ["branding", "brand strategy"],
    "Campaign Management": ["campaign management", "gestione campagne"],
    
    # ========== DESIGN ==========
    "UI Design": ["ui design", "user interface"],
    "UX Design": ["ux design", "user experience"],
    "Graphic Design": ["graphic design", "design grafico"],
    "Figma": ["figma"],
    "Sketch": ["sketch"],
    "Adobe XD": ["adobe xd", "xd"],
    "Photoshop": ["photoshop", "ps"],
    "Illustrator": ["illustrator", "ai"],
    "Prototyping": ["prototyping", "prototipazione"],
    "Wireframing": ["wireframing"],
    "User Research": ["user research", "ux research"],
    
    # ========== BUSINESS & MANAGEMENT ==========
    "Project Management": ["project management", "gestione progetti"],
    "Product Management": ["product management"],
    "Business Analysis": ["business analysis", "analisi business"],
    "Agile": ["agile", "scrum", "kanban"],
    "Scrum": ["scrum"],
    "Kanban": ["kanban"],
    "Jira": ["jira"],
    "Confluence": ["confluence"],
    "Strategy": ["strategy", "strategia", "strategic planning"],
    "Budgeting": ["budgeting", "budget management"],
    "Leadership": ["leadership", "team leadership"],
    "Stakeholder Management": ["stakeholder management"],
    
    # ========== FINANCE & ACCOUNTING ==========
    "Accounting": ["accounting", "contabilità"],
    "Financial Analysis": ["financial analysis", "analisi finanziaria"],
    "Financial Modeling": ["financial modeling", "modelli finanziari"],
    "Taxation": ["taxation", "fiscalità", "tax"],
    "Auditing": ["auditing", "audit", "revisione"],
    "Risk Management": ["risk management", "gestione rischio"],
    
    # ========== ENGINEERING ==========
    "Mechanical Engineering": ["mechanical engineering", "ingegneria meccanica"],
    "Electrical Engineering": ["electrical engineering", "ingegneria elettrica"],
    "Civil Engineering": ["civil engineering", "ingegneria civile"],
    "CAD": ["autocad", "solidworks", "catia", "cad"],
    "AutoCAD": ["autocad"],
    "SolidWorks": ["solidworks"],
    "Simulation": ["ansys", "abaqus", "comsol", "fem", "fea"],
    "PLC": ["plc", "siemens", "allen bradley"],
    "SCADA": ["scada"],
    
    # Comp & Ben (Killer Keywords)
    "Compensation": ["salary benchmarking", "job grading", "hay method", "mercer", "towers watson", "executive compensation"],
    "Benefits": ["benefits administration", "welfare plans", "pension schemes", "health insurance", "total rewards"],

    # ========== SUPPLY CHAIN & LOGISTICS (DETAILED) ==========
    "Supply Chain": ["supply chain management", "scm"],
    "Planning (Killer Keywords)": ["demand planning", "s&op", "sales and operations planning", "mrp ii", "inventory optimization", "safety stock analysis"],
    "Procurement (Killer Keywords)": ["strategic sourcing", "category management", "rfq/rfp management", "supplier relationship management", "srm", "contract negotiation"],
    "Logistics (Killer Keywords)": ["freight forwarding", "incoterms 2020", "last mile delivery", "fleet telematics", "reverse logistics", "wms configuration"],

    # ========== DATA & ANALTYICS (STANDARD) ==========
    "Excel": ["excel", "microsoft excel", "advanced excel", "excel advanced", "vba", "pivot table", "vlookup", "xlookup", "fogli di calcolo", "spreadsheet"],
    "Reporting": ["reporting", "reportistica", "business reporting", "data reporting", "generazione report", "reports", "dashboarding"],
    "Statistics": ["statistics", "statistica", "statistical analysis", "analisi statistica", "probabilità", "inferenza statistica"],
    "Data Analysis": ["data analysis", "pandas", "numpy", "power query", "analytics", "analisi dati", "analisi dei dati"],
    "Artificial Intelligence": ["artificial intelligence", "ai", "machine intelligence", "computational intelligence", "cognitive computing", "generative ai", "llm", "large language models"],
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural networks", "predictive modeling", "tensorflow", "pytorch", "scikit-learn", "xgboost", "automl"],
    "Visualization": ["power bi", "looker", "qlik", "domo", "google data studio", "looker studio", "google looker studio", "data visualization", "tableau", "tableau desktop", "tableau server", "tableau prep", "tableau public"],
    "Big Data": ["hadoop", "spark", "hive", "databricks", "snowflake", "redshift", "bigquery"],
    "Google Analytics": ["google analytics", "ga4", "google analytics 4", "universal analytics", "web analytics"],

    # ========== FASHION & LUXURY (DETAILED) ==========
    "Fashion Design": ["fashion design", "stilista", "fashion sketching", "moodboard", "modellistica", "draping"],
    "Textile Knowledge": ["textile", "tessuti", "merciologia tessile", "fabric knowledge", "yarns", "filati", "leather"],
    "Pattern Making": ["pattern making", "modellista", "cartamodello", "lectra", "gerber", "clo3d", "cad fashion"],
    "Visual Merchandising": ["visual merchandising", "vetrinista", "store layout", "display design", "in-store experience"],
    "Luxury Retail": ["luxury retail", "vendita assistita", "luxury sales", "clienteling", "vic", "very important client"],
    "Buying": ["buying", "buyer", "acquisti moda", "budgeting", "assortment planning", "oted"],
    "Merchandising": ["merchandising", "allocator", "stock management", "sales analysis", "open to buy"],

    # ========== FOOD & BEVERAGE & ARGITECH (DETAILED) ==========
    "Food Safety": ["haccp", "iso 22000", "brc", "ifs", "sicurezza alimentare", "food defense"],
    "Food Technology": ["food technology", "tecnologie alimentari", "processo produttivo", "scienza degli alimenti", "shelf life"],
    "Enology": ["enology", "enologia", "winemaking", "vinificazione", "sommelier", "degustazione", "cantina"],
    "Agronomy": ["agronomy", "agronomia", "coltivazioni", "crop management", "precision agriculture", "agritech"],
    "F&B Management": ["food & beverage", "f&b", "food cost", "menu engineering", "gestione sala", "ristorazione"],

    # ========== MANUFACTURING 4.0 (DETAILED) ==========
    "CNC Machining": ["cnc", "macchine utensili", "tornitura", "fresatura", "fanuc", "siemens sinumerik", "heidenhain"],
    "Industrial Automation": ["automazione industriale", "plc", "scada", "hmi", "robotics", "kuka", "abb", "yaskawa"],
    "Lean Manufacturing": ["lean manufacturing", "kaizen", "5s", "tpm", "smed", "continuous improvement", "toyota production system"],
    "Maintenance Management": ["manutenzione", "maintenance", "gmaw", "tig", "mig", "saldatura", "elettromeccanica"],
    "Quality Management": ["quality management", "sistema qualità", "iso 9001", "iatf 16949", "audit", "non conformity"],

    # ========== DESIGN & ARCHITECTURE (DETAILED) ==========
    "Interior Design": ["interior design", "architettura d'interni", "arredamento", "space planning", "homestaging"],
    "BIM & CAD": ["bim", "revit", "archicad", "autocad", "2d drawing", "technical drawing", "disegno tecnico"],
    "3D Modeling & Rendering": ["3d modeling", "rendering", "sketchup", "rhino", "3ds max", "v-ray", "corona renderer", "lumion"],
    "Restoration": ["restoration", "restauro", "conservazione", "beni culturali", "history of architecture"],

    # ========== BANKING & INSURANCE (DETAILED) ==========
    "Wealth Management": ["wealth management", "gestione patrimoni", "private banking", "portafogli", "asset allocation"],
    "Banking Compliance": ["compliance bancaria", "mifid", "antiriciclaggio", "aml", "kyc", "basel"],
    "Credit Analysis": ["analisi del credito", "credit risk", "rischio di credito", "fidi", "istruttoria"],
    "Insurance Products": ["assicurazioni", "polizze", "ramo danni", "ramo vita", "insurance underwriting", "claims"],

    # ========== ENGINEERING DEEP DIVE (DETAILED) ==========
    "Engineering": {
        "CAD": ["autocad", "solidworks", "catia", "nx", "ptc creo", "revit", "bim", "civil 3d", "microstation"],
        "Simulation": ["ansys", "abaqus", "comsol", "simulink", "matlab", "labview", "hysys", "aspen plus", "fluent", "cfd"],
        "Electronics": ["pcb design", "altium designer", "eagle", "proteus", "kicad", "spice", "vhdl", "verilog", "fpga", "arduino", "raspberry pi", "plc", "scada"],
        "Energy Engineering": ["energy engineering", "ingegneria energetica", "renewable energy", "solar energy", "photovoltaics", "wind energy", "energy efficiency", "thermodynamics", "power systems"],
    },
    "Electrical Engineering": ["electrical engineering", "elettrotecnica", "schema elettrico", "medium voltage", "high voltage", "cabine"],
    "Embedded Systems": ["embedded c", "microcontrollers", "stm32", "pic", "fpga", "vhdl", "verilog", "rtos", "firmware"],
    "Civil Engineering": ["ingegneria civile", "strutture", "calcolo strutturale", "direzione lavori", "computo metrico", "primus"],
    "BIM": ["bim", "revit", "navisworks", "archicad", "tekla", "building information modeling"],
    "Energy & Renewables": ["rinnovabili", "fotovoltaico", "eolico", "efficienza energetica", "energy manager", "pvsyst", "high voltage"],

    # ========== BIOTECH, PHARMA & SCIENCE (DETAILED) ==========
    "Clinical Research": ["clinical trials", "studi clinici", "good clinical practice", "clinical research associate", "cra clinical", "ich-gcp"],
    "Regulatory Affairs": ["regulatory affairs", "aifa", "ema", "fda", "dossier", "market access"],
    "Quality Assurance (Pharma)": ["gmp", "good manufacturing practice", "glp", "capa", "change control", "data integrity"],
    "Lab Techniques": ["pcr", "elisa", "westem blot", "hplc", "cell culture", "biologia molecolare", "chromatography"],
    "R&D (Science)": ["ricerca e sviluppo", "r&d", "protocolli", "sperimentazione", "formulazione"],

    # ========== LANGUAGES & TRANSLATION (DETAILED) ==========
    "Translation": ["translation", "traduzione", "trados", "memoq", "post-editing", "mtpe", "localization"],
    "Interpreting": ["interpreting", "interpretariato", "simultanea", "consecutiva", "chuchotage"],
    "Teaching": ["teaching", "insegnamento", "didattica", "docenza", "esl", "tefl"],

    # ========== ECONOMICS & FINANCE (DETAILED) ==========
    "Auditing": ["audit", "revisione legale", "internal audit", "big 4", "isa", "controllo di gestione"],
    "Taxation": ["tax", "fiscalità", "dichiarazione redditi", "transfer pricing", "iva", "vat"],
    "Economics": ["econometrics", "stata", "eviews", "macroeconomics", "economic policy", "antitrust"],

    # ========== ENERGY MARKETS & TRADING (LEGACY MERGED) ==========
    "Energy Markets": ["energy markets", "power markets", "electricity markets", "mercato elettrico"],
    "Energy Trading": ["energy trading", "power trading", "commodity trading"],
    "Financial Modeling (Energy)": ["financial modeling", "price forecasting", "risk modeling"],
    "Power Systems Analysis": ["power systems", "grid analysis", "load forecasting"],
    "Trading Strategies": ["trading strategies", "hedging", "derivatives"],
    
    # ========== OTHER (LEGACY MERGED) ==========
    "Customer Service": ["customer service", "servizio clienti"],
    "Sales": ["sales", "vendita"],
    "CRM": ["salesforce", "hubspot", "crm"],

}

# =============================================================================
# SECTION 5: SOFT SKILLS
# =============================================================================

SOFT_SKILLS = {
    # Communication
    "Communication": ["communication", "comunicazione", "verbal communication"],
    "Written Communication": ["written communication", "comunicazione scritta"],
    "Presentation Skills": ["presentation", "public speaking"],
    "Active Listening": ["active listening", "ascolto attivo"],
    
    # Teamwork & Leadership
    "Teamwork": ["teamwork", "lavoro di squadra", "collaboration"],
    "Leadership": ["leadership", "guida team", "people management"],
    "Mentoring": ["mentoring", "coaching"],
    "Conflict Resolution": ["conflict resolution", "risoluzione conflitti"],
    
    # Analytical & Problem Solving
    "Problem Solving": ["problem solving", "risoluzione problemi"],
    "Critical Thinking": ["critical thinking", "pensiero critico"],
    "Decision Making": ["decision making", "processo decisionale"],
    "Analytical Thinking": ["analytical", "analitico", "analytical thinking"],
    
    # Personal Effectiveness
    "Time Management": ["time management", "gestione tempo"],
    "Organization": ["organization", "organizzazione"],
    "Prioritization": ["prioritization", "priorità"],
    "Attention to Detail": ["attention to detail", "attenzione dettagli", "precision"],
    "Self-Motivation": ["self-motivation", "proattività", "initiative"],
    
    # Adaptability
    "Adaptability": ["adaptability", "adattabilità", "flexibility"],
    "Resilience": ["resilience", "resilienza"],
    "Learning Agility": ["learning agility", "quick learner"],
    
    # Creativity & Innovation
    "Creativity": ["creativity", "creatività", "creative thinking"],
    "Innovation": ["innovation", "innovazione"],
    "Strategic Thinking": ["strategic thinking", "pensiero strategico"],
    
    # Interpersonal
    "Interpersonal Skills": ["interpersonal", "relazionale"],
    "Empathy": ["empathy", "empatia", "emotional intelligence"],
    "Customer Focus": ["customer focus", "orientamento cliente"],
    "Negotiation": ["negotiation", "negoziazione"],
}

# =============================================================================
# SECTION 6: NON-SKILL PATTERNS
# =============================================================================

NON_SKILL_PATTERNS = {
    "section_headers": [
        r"benefic[i]?|benefits|cosa (?:ti )?offriamo|what we offer|perks",
        r"condizioni|conditions|termini|terms",
        r"chi siamo|about us|la nostra azienda|our company",
    ],
    
    "salary": [
        r"[€$£]\s*[\d.,]+(?:k|K)?",
        r"(?:RAL|salary|stipendio)[\s:]*[\d€$£.,]+",
    ],
    
    "hours": [
        r"\d+\s*(?:ore|hours?)(?:\s*/\s*(?:settimana|week))?",
        r"(?:full-time|part-time)",
    ],
    
    "duration": [
        r"\d+\s*(?:mesi|months?|anni|years?)",
    ],
    
    "benefits": [
        r"(?:ferie|vacation|holidays?)",
        r"(?:assicurazione|insurance)",
        r"(?:smart working|remote work)",
        r"(?:buoni pasto|meal vouchers?)",
    ],
    
    "contract": [
        r"(?:contratto|contract)\s+(?:determinato|indeterminato|permanent|fixed)",
    ],
    
    "eligibility": [
        r"(?:età|age)[\s:]*\d+",
        r"(?:laurea|degree|bachelor|master)",
    ],
}

# =============================================================================
# SECTION 7: CAREER CATEGORIES & JOB METADATA
# =============================================================================

CAREER_CATEGORIES = {
    "Technology": "Software, data, IT, cybersecurity, and digital infrastructure",
    "Marketing": "Digital marketing, branding, communications, and growth",
    "Business": "Management, consulting, operations, and strategy",
    "Finance": "Accounting, financial analysis, investment, and risk",
    "Design": "UX/UI, graphic design, creative direction, and content",
    "Engineering": "Mechanical, electrical, industrial, and process engineering",
    "Data": "Data science, analytics, ML, and data engineering",
    "Product": "Product management, product design, and innovation",
    "Sales": "B2B/B2C sales, account management, and business development",
    "Energy": "Renewable energy, energy trading, and power systems",
}

JOB_ROLE_METADATA = {
    # Technology
    "Software Engineer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Frontend Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Backend Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Full Stack Developer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "DevOps Engineer": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Cybersecurity Analyst": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": True, "creative": False},
    "System Administrator": {"category": "Technology", "client_facing": False, "remote_friendly": True, "international": False, "dynamic": False, "creative": False},
    
    # Data
    "Data Analyst": {"category": "Data", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "Data Scientist": {"category": "Data", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Data Engineer": {"category": "Data", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    "ML Engineer": {"category": "Data", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    "Analytics Engineer": {"category": "Data", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": False},
    
    # Design
    "UX Designer": {"category": "Design", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "UI Designer": {"category": "Design", "client_facing": False, "remote_friendly": True, "international": True, "dynamic": False, "creative": True},
    
    # Product
    "Product Manager": {"category": "Product", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    "Technical Product Manager": {"category": "Product", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # Marketing
    "Marketing Manager": {"category": "Marketing", "client_facing": True, "remote_friendly": True, "international": True, "dynamic": True, "creative": True},
    
    # Energy
    "Energy Trader": {"category": "Energy", "client_facing": True, "remote_friendly": False, "international": True, "dynamic": True, "creative": False},
    "Energy Engineer": {"category": "Energy", "client_facing": False, "remote_friendly": False, "international": True, "dynamic": False, "creative": True},
}

ML_MODELS = {
    "Authorization": ["oauth", "jwt", "sso", "saml", "openid connect", "auth0", "okta"],
    
    # ========== LANGUAGES & TRANSLATION (DETAILED) ==========
    "Languages": ["english", "italian", "french", "german", "spanish", "chinese", "japanese", "inglese", "italiano", "francese", "tedesco", "spagnolo", "cinese", "giapponese", "lingue estere"],
    
    # Translation (Killer Keywords)
    "Translation Tech": ["cat tools", "trados studio", "memoq", "memsource", "wordfast", "terminology management"],
    "Specialized Translation": ["legal translation", "biomedical translation", "patent translation", "technical translation", "financial translation"],
    "Localization": ["localization", "l10n", "internationalization", "i18n", "software localization", "game localization", "transcreation"],
    "Post-Editing": ["mtpe", "machine translation post-editing", "neural machine translation"],

    # Interpreting (Killer Keywords)
    "Interpreting Modes": ["simultaneous interpreting", "consecutive interpreting", "chuchotage", "liaison interpreting"],
    "Remote Interpreting": ["rsi", "remote simultaneous interpreting", "kudo", "interpretfy", "zoom interpretation"],
    
    # ========== HUMAN RESOURCES (DETAILED) ==========
    # Talent Acquisition (Killer Keywords)
    "Sourcing": ["boolean search", "x-ray search", "github sourcing", "stackoverflow sourcing", "talent mapping"],
    "Recruitment Marketing": ["employer branding", "career page optimization", "recruitment analytics", "candidate experience"],
    "Assessment": ["psychometric testing", "assessment centers", "behavioral interviewing", "star method", "coding challenges"],
    
    # Comp & Ben (Killer Keywords)
    "Compensation": ["salary benchmarking", "job grading", "hay method", "mercer", "towers watson", "executive compensation"],
    "Benefits": ["benefits administration", "welfare plans", "pension schemes", "health insurance", "total rewards"],

    # ========== SUPPLY CHAIN & LOGISTICS (DETAILED) ==========
    "Supply Chain": ["supply chain management", "scm"],
    "Planning (Killer Keywords)": ["demand planning", "s&op", "sales and operations planning", "mrp ii", "inventory optimization", "safety stock analysis"],
    "Procurement (Killer Keywords)": ["strategic sourcing", "category management", "rfq/rfp management", "supplier relationship management", "srm", "contract negotiation"],
    "Logistics (Killer Keywords)": ["freight forwarding", "incoterms 2020", "last mile delivery", "fleet telematics", "reverse logistics", "wms configuration"],

    # ========== DATA & ANALTYICS (STANDARD) ==========
    "Excel": ["excel", "microsoft excel", "advanced excel", "excel advanced", "vba", "pivot table", "vlookup", "xlookup", "fogli di calcolo", "spreadsheet"],
    "Reporting": ["reporting", "reportistica", "business reporting", "data reporting", "generazione report", "reports", "dashboarding"],
    "Statistics": ["statistics", "statistica", "statistical analysis", "analisi statistica", "probabilità", "inferenza statistica"],
    "Data Analysis": ["data analysis", "pandas", "numpy", "power query", "analytics", "analisi dati", "analisi dei dati"],
    "Artificial Intelligence": ["artificial intelligence", "ai", "machine intelligence", "computational intelligence", "cognitive computing", "generative ai", "llm", "large language models"],
    "Machine Learning": ["machine learning", "ml", "deep learning", "neural networks", "predictive modeling", "tensorflow", "pytorch", "scikit-learn", "xgboost", "automl"],
    "Visualization": ["power bi", "looker", "qlik", "domo", "google data studio", "looker studio", "google looker studio", "data visualization"],
    "Tableau": ["tableau", "tableau desktop", "tableau server", "tableau prep", "tableau public"],
    "Big Data": ["hadoop", "spark", "hive", "databricks", "snowflake", "redshift", "bigquery"],
    "Google Analytics": ["google analytics", "ga4", "google analytics 4", "universal analytics", "web analytics"],
}

# =============================================================================
# BACKWARD COMPATIBILITY LAYER
# =============================================================================
# The application expects JOB_ARCHETYPES to be Dict[str, Set[str]]
# whereas JOB_ARCHETYPES_EXTENDED is Dict[str, Dict] (V2 Metadata)

JOB_ARCHETYPES = {}

for role, metadata in JOB_ARCHETYPES_EXTENDED.items():
    if isinstance(metadata, dict):
        if 'primary_skills' in metadata:
            JOB_ARCHETYPES[role] = set(metadata['primary_skills'])
        elif 'hard_skills' in metadata:
            JOB_ARCHETYPES[role] = set(metadata['hard_skills'])
        else:
            JOB_ARCHETYPES[role] = set()
    else:
        # Fallback for any non-dict entries
        JOB_ARCHETYPES[role] = set(metadata) if not isinstance(metadata, set) else metadata

