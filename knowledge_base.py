# =============================================================================
# EXTENDED KNOWLEDGE BASE v2.1 (REFACTORED)
# =============================================================================

# =============================================================================
# SECTION 1: JOB ARCHETYPES (CORRECTED & EXPANDED)
# =============================================================================

JOB_ARCHETYPES_EXTENDED = {
    # ========== TECHNOLOGY & DIGITAL ==========
    'Software Engineer': {
        'sector': 'Technology',
        'primary_skills': ['Algorithms', 'Git', 'Programming', 'System Design', 'Testing'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€35k-65k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Engineering Manager',
        'transition_from': ['Computer Science Degree', 'Bootcamp'],
    },
    
    'Frontend Developer': {
        'sector': 'Technology',
        'primary_skills': ['CSS', 'Git', 'HTML', 'JavaScript', 'React', 'UI Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail'],
        'market_demand': 'high',
        'salary_range': '€32k-58k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Frontend Architect',
    },
    
    'Backend Developer': {
        'sector': 'Technology',
        'primary_skills': ['Docker', 'Java', 'Microservices', 'Python', 'Redis', 'SQL', 'System Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Analytical Thinking'],
        'market_demand': 'high',
        'salary_range': '€35k-62k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Backend Architect',
    },
    
    'Full Stack Developer': {
        'sector': 'Technology',
        'primary_skills': ['DevOps', 'Git', 'JavaScript', 'Node.js', 'Python', 'React', 'SQL'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Multitasking'],
        'market_demand': 'very high',
        'salary_range': '€38k-68k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Tech Lead',
    },
    
    # ========== DATA & ANALYTICS ==========
    'Data Analyst': {
        'sector': 'Data',
        'primary_skills': ['Data Visualization', 'Excel', 'Python', 'SQL', 'Statistics'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€32k-55k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Analytics Manager',
    },
    
    'Data Scientist': {
        'sector': 'Data',
        'primary_skills': ['Deep Learning', 'Machine Learning', 'Python', 'SQL', 'Statistics'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€40k-70k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Head of Data Science',
    },
    
    'Data Engineer': {
        'sector': 'Data',
        'primary_skills': ['BigQuery', 'Cloud Computing', 'ETL', 'Python', 'SQL', 'Spark'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€42k-72k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Data Architect',
    },
    
    'Machine Learning Engineer': {
        'sector': 'Data',
        'primary_skills': ['Cloud Computing', 'MLOps', 'Machine Learning', 'Python', 'TensorFlow'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€45k-75k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> ML Research Scientist',
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
        'sector': 'Data',
        'primary_skills': ['CI/CD', 'DevOps', 'Docker', 'Kubernetes', 'Machine Learning', 'Python'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€45k-75k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Tech Lead',
    },
    
    'AI Business Analyst': {
        'sector': 'Data',
        'primary_skills': ['Artificial Intelligence', 'Business Analysis', 'Data Analysis', 'Python', 'Strategy'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Strategic Thinking'],
        'market_demand': 'emerging high',
        'salary_range': '€38k-62k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Junior -> Senior -> AI Consultant',
    },
    
    # ========== DESIGN & UX ==========
    'UX Designer': {
        'sector': 'Design',
        'primary_skills': ['Figma', 'Prototyping', 'UX Design', 'User Research', 'Wireframing'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Empathy', 'Creativity'],
        'market_demand': 'high',
        'salary_range': '€32k-58k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> UX Director',
    },
    
    'UI Designer': {
        'sector': 'Design',
        'primary_skills': ['Adobe Creative Suite', 'Figma', 'Typography', 'UI Design', 'Visual Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail', 'Creativity'],
        'market_demand': 'high',
        'salary_range': '€30k-55k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Design Director',
    },
    
    # ========== DEVOPS & INFRASTRUCTURE ==========
    'DevOps Engineer': {
        'sector': 'Technology',
        'primary_skills': ['CI/CD', 'Cloud Computing', 'DevOps', 'Docker', 'Kubernetes'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€42k-72k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Lead -> Architect',
    },
    
    'Cybersecurity Analyst': {
        'sector': 'Technology',
        'primary_skills': ['Compliance', 'Cybersecurity', 'Incident Response', 'Network Security', 'Risk Management'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Attention to Detail', 'Communication', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€38k-68k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Manager -> CISO',
    },
    
    'IT Support Specialist': {
        'sector': 'Technology',
        'primary_skills': ['Customer Service', 'Hardware', 'IT Support', 'Troubleshooting', 'Windows'],
        'soft_skills': ['Adaptability', 'Communication', 'Empathy', 'Problem Solving', 'Patience'],
        'market_demand': 'stable',
        'salary_range': '€24k-38k',
        'remote_friendly': False,
        'client_facing': True,
        'international': False,
        'career_path': 'Specialist -> Senior -> Manager',
    },
    
    'System Administrator': {
        'sector': 'Technology',
        'primary_skills': ['Cloud Computing', 'Linux', 'Networking', 'Scripting', 'Windows Server'],
        'soft_skills': ['Adaptability', 'Communication', 'Problem Solving', 'Attention to Detail'],
        'market_demand': 'stable',
        'salary_range': '€32k-55k',
        'remote_friendly': True,
        'client_facing': False,
        'international': False,
        'career_path': 'Junior -> Senior -> Infrastructure Manager',
    },
    
    # ========== PRODUCT & GROWTH ==========
    'Product Manager': {
        'sector': 'Product',
        'primary_skills': ['Agile', 'Data Analysis', 'Product Management', 'Roadmap', 'User Stories'],
        'soft_skills': ['Adaptability', 'Communication', 'Leadership', 'Problem Solving', 'Strategic Thinking', 'Team Management'],
        'market_demand': 'high',
        'salary_range': '€45k-85k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Junior -> PM -> Head of Product',
    },

    # ========== MARKETING & SALES ==========
    'Marketing Manager': {
        'sector': 'Marketing',
        'primary_skills': ['SEO', 'SEM', 'Content Strategy', 'Social Media Marketing', 'Google Analytics'],
        'soft_skills': ['Creativity', 'Communication', 'Strategic Thinking', 'Leadership'],
        'market_demand': 'high',
        'salary_range': '€35k-65k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Specialist -> Manager -> CMO',
    },

    'Account Executive': {
        'sector': 'Sales',
        'primary_skills': ['B2B Sales', 'CRM', 'Negotiation', 'Lead Generation', 'Sales Pitching'],
        'soft_skills': ['Interpersonal Skills', 'Persuasion', 'Resilience', 'Communication'],
        'market_demand': 'high',
        'salary_range': '€30k-60k + Bns',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'SDR -> AE -> Sales Manager',
    },

    # ========== FINANCE & ACCOUNTING ==========
    'Financial Analyst': {
        'sector': 'Finance',
        'primary_skills': ['Financial Modelling', 'Financial Reporting', 'Excel', 'SQL', 'Valuation'],
        'soft_skills': ['Analytical Thinking', 'Attention to Detail', 'Communication'],
        'market_demand': 'high',
        'salary_range': '€35k-60k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Junior -> Senior -> Finance Manager -> CFO',
    },
    'Accountant': {
        'sector': 'Finance',
        'primary_skills': ['Accounting Principles', 'Auditing', 'Excel', 'Taxation', 'Financial Statements'],
        'soft_skills': ['Attention to Detail', 'Integrity', 'Organization'],
        'market_demand': 'stable',
        'salary_range': '€30k-55k',
        'remote_friendly': True,
        'client_facing': True,
        'international': False,
        'career_path': 'Accountant -> Senior Accountant -> Accounting Manager',
    },

    # ========== HEALTHCARE & LIFE SCIENCES ==========
    'Clinical Research Associate': {
        'sector': 'Healthcare',
        'primary_skills': ['Clinical Trials', 'GCP', 'Data Management', 'Monitoring', 'Regulatory Affairs'],
        'soft_skills': ['Attention to Detail', 'Ethics', 'Communication'],
        'market_demand': 'high',
        'salary_range': '€35k-55k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'CRA -> Senior CRA -> Clinical Project Manager',
    },

    # ========== LEGAL & COMPLIANCE ==========
    'Legal Counsel': {
        'sector': 'Legal',
        'primary_skills': ['Contract Law', 'Corporate Law', 'Compliance', 'Legal Drafting', 'GDPR'],
        'soft_skills': ['Attention to Detail', 'Critical Thinking', 'Communication', 'Ethics'],
        'market_demand': 'stable',
        'salary_range': '€40k-85k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Junior -> Legal Counsel -> General Counsel',
    },

    # ========== ENERGY & SUSTAINABILITY ==========
    'Energy Engineer': {
        'sector': 'Energy',
        'primary_skills': ['Renewable Energy', 'Energy Auditing', 'Energy Efficiency', 'Sustainability', 'AutoCAD'],
        'soft_skills': ['Analytical Thinking', 'Problem Solving', 'Technical Writing'],
        'market_demand': 'high',
        'salary_range': '€35k-60k',
        'remote_friendly': False,
        'client_facing': False,
        'international': True,
        'career_path': 'Engineer -> Senior Engineer -> Energy Manager',
    },
    
    'Solutions Architect': {
        'sector': 'Technology',
        'primary_skills': ['AWS', 'Azure', 'Cloud Computing', 'Communication', 'Sales', 'System Design'],
        'soft_skills': ['Adaptability', 'Communication', 'Empathy', 'Negotiation', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€50k-90k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Architect -> Senior SA -> Enterprise Architect',
    },

    'Sustainability Manager': {
        'sector': 'Sustainability',
        'primary_skills': ['Sustainability', 'ESG Reporting', 'Carbon Footprint', 'LCA', 'Compliance', 'Stakeholder Management'],
        'soft_skills': ['Adaptability', 'Communication', 'Strategic Thinking', 'Influence', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€45k-80k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Specialist -> Manager -> Head of Sustainability',
    },

    'E-commerce Manager': {
        'sector': 'Marketing',
        'primary_skills': ['E-commerce', 'Digital Marketing', 'Analytics', 'Shopify', 'Inventory Management', 'CRO'],
        'soft_skills': ['Adaptability', 'Analytical Thinking', 'Communication', 'Leadership', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€35k-65k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'Specialist -> Manager -> Digital Director',
    },
    'Compliance Officer': {
        'sector': 'Legal',
        'primary_skills': ['Compliance', 'Risk Management', 'GDPR', 'Legal Tech', 'Reporting', 'Audit'],
        'soft_skills': ['Attention to Detail', 'Analytical Thinking', 'Communication', 'Ethics', 'Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€40k-70k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Analyst -> Officer -> Head of Compliance',
    },

    # ========== HEALTHTECH & CLINICAL DATA ==========
    'Clinical Data Manager': {
        'sector': 'Healthcare',
        'primary_skills': ['Clinical Data Management', 'Statistics', 'SQL', 'Clinical Research', 'HealthTech', 'EDC Systems'],
        'soft_skills': ['Attention to Detail', 'Analytical Thinking', 'Communication', 'Problem Solving', 'Adaptability'],
        'market_demand': 'medium-high',
        'salary_range': '€35k-60k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Manager -> Senior Manager -> Head of Data Management',
    },

    'Luxury Store Manager': {
        'sector': 'Fashion & Luxury',
        'primary_skills': ['Luxury Retail', 'Visual Merchandising', 'Clienteling', 'Team Management', 'Salesforce', 'P&L Management'],
        'soft_skills': ['Communication', 'Leadership', 'Emotional Intelligence', 'Adaptability'],
        'market_demand': 'high',
        'salary_range': '€50k-95k',
        'remote_friendly': False,
        'client_facing': True,
        'international': True,
        'career_path': 'Assistant -> Store Manager -> Regional Manager',
    },

    'Hotel General Manager': {
        'sector': 'Hospitality',
        'primary_skills': ['Hotel Management', 'Revenue Management', 'Guest Experience', 'Budgeting', 'Operations', 'PMS Software'],
        'soft_skills': ['Leadership', 'Problem Solving', 'Customer Focus', 'Adaptability'],
        'market_demand': 'medium-high',
        'salary_range': '€60k-120k+',
        'remote_friendly': False,
        'client_facing': True,
        'international': True,
        'career_path': 'Operations Manager -> GM -> Area Manager',
    },

    'Automotive Engineer': {
        'sector': 'Engineering',
        'primary_skills': ['Automotive Engineering', 'MATLAB', 'Simulation', 'Vehicle Dynamics', 'CAD', 'Powertrain'],
        'soft_skills': ['Analytical Thinking', 'Teamwork', 'Attention to Detail', 'Problem Solving'],
        'market_demand': 'very high',
        'salary_range': '€38k-75k',
        'remote_friendly': False,
        'client_facing': False,
        'international': True,
        'career_path': 'Engineer -> Lead Engineer -> Technical Director',
    },

    'Fintech Product Manager': {
        'sector': 'Finance',
        'primary_skills': ['Product Management', 'Open Banking', 'Agile', 'Compliance', 'Data Analysis', 'User Research'],
        'soft_skills': ['Adaptability', 'Strategic Thinking', 'Communication', 'Collaborative Skills'],
        'market_demand': 'very high',
        'salary_range': '€45k-85k',
        'remote_friendly': True,
        'client_facing': True,
        'international': True,
        'career_path': 'PM -> Senior PM -> Head of Product',
    },

    'Systems Engineer (Aerospace)': {
        'sector': 'Engineering',
        'primary_skills': ['Systems Engineering', 'Mission Design', 'Propulsion', 'Avionics', 'Aerodynamics'],
        'soft_skills': ['Critical Thinking', 'Communication', 'Teamwork', 'Systems Thinking'],
        'market_demand': 'high',
        'salary_range': '€40k-80k',
        'remote_friendly': False,
        'client_facing': False,
        'international': True,
        'career_path': 'Engineer -> Systems Engineer -> Project Manager',
    },

    'Space Systems Architect': {
        'sector': 'Engineering',
        'primary_skills': ['Systems Engineering', 'Mission Design', 'Satellite Ops', 'GNC', 'Space Mechanics'],
        'soft_skills': ['Visionary Thinking', 'Systems Thinking', 'Leadership', 'Complex Problem Solving'],
        'market_demand': 'high',
        'salary_range': '€55k-100k+',
        'remote_friendly': False,
        'client_facing': False,
        'international': True,
        'career_path': 'Senior Engineer -> Space Architect -> Mission Director',
    },

    'Quantum Algorithm Researcher': {
        'sector': 'Technology',
        'primary_skills': ['Quantum Computing', 'Quantum Algorithms', 'Physics', 'Mathematics', 'Python', 'Qiskit'],
        'soft_skills': ['Intellectual Curiosity', 'Analytical Thinking', 'Scientific Rigor'],
        'market_demand': 'emerging',
        'salary_range': '€45k-80k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Researcher -> Senior Researcher -> Quantum Architect',
    },

    'XR Developer': {
        'sector': 'Technology',
        'primary_skills': ['Spatial Computing', 'Unity 3D', 'Unreal Engine', 'C#', 'C++', 'Computer Vision'],
        'soft_skills': ['Creativity', 'Attention to Detail', 'User Empathy', 'Adaptability'],
        'market_demand': 'high',
        'salary_range': '€35k-65k',
        'remote_friendly': True,
        'client_facing': False,
        'international': True,
        'career_path': 'Developer -> Senior XR Developer -> XR Architect',
    },

    'AgTech Innovation Specialist': {
        'sector': 'Engineering',
        'primary_skills': ['Precision Farming', 'IoT', 'Data Analysis', 'Hydroponics', 'Sustainability', 'GIS'],
        'soft_skills': ['Resourcefulness', 'Communication', 'Strategic Thinking', 'Domain Curiosity'],
        'market_demand': 'medium-high',
        'salary_range': '€35k-60k',
        'remote_friendly': False,
        'client_facing': True,
        'international': True,
        'career_path': 'Specialist -> Innovation Manager -> CTO',
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
    
    # Sustainability
    "LCA": ["Sustainability", "Environmental Science"],
    "Carbon Footprint": ["Sustainability", "Reporting"],
    "ESG Reporting": ["Sustainability", "Reporting", "Compliance"],
    "Circular Economy": ["Sustainability", "Resource Management"],
    
    # E-commerce
    "Shopify": ["E-commerce", "Digital Presence"],
    "Magento": ["E-commerce", "Web Development"],
    "Amazon Marketplace": ["E-commerce", "Sales Channels"],
    "CRO": ["E-commerce", "Digital Marketing", "Analytics"],
    
    # Legal Tech
    "CLM": ["Legal Tech", "Contract Management"],
    "GDPR": ["Compliance", "Legal Tech", "Privacy"],
    "AML": ["Compliance", "Legal Tech", "Finance"],
    
    # HealthTech
    "HL7": ["HealthTech", "Data Standards"],
    "EHR": ["HealthTech", "Digital Health"],
    "CDM": ["HealthTech", "Clinical Research"],
    
    # Luxury & Fashion
    "Luxury Retail": ["Sales", "Luxury & Fashion"],
    "Visual Merchandising": ["Design", "Retail"],
    "Textile Knowledge": ["Fashion Design", "Materials Science"],
    "Haute Couture": ["Fashion Design", "Luxury & Fashion"],
    "Salesforce Clienteling": ["CRM", "Luxury Retail"],
    
    # Hospitality
    "Hotel Management": ["Hospitality", "Management"],
    "Revenue Management": ["Hospitality", "Finance", "Analytics"],
    "PMS Software": ["Hospitality", "Software"],
    "Guest Experience": ["Hospitality", "Customer Service"],
    
    # Automotive
    "Vehicle Dynamics": ["Automotive Engineering", "Physics"],
    "Powertrain": ["Automotive Engineering", "Mechanical Engineering"],
    "Aerodynamics Specialist": ["Aerospace", "Automotive", "Physics"],
    "CFD": ["Engineering", "Simulation"],
    
    # Fintech & Web3
    "Solidity": ["Blockchain", "Programming"],
    "Smart Contracts": ["Blockchain", "Legal Tech"],
    "Cryptography": ["Security", "Mathematics"],
    "Open Banking": ["Fintech", "Banking"],
    
    # Aerospace
    "Avionics": ["Aerospace", "Electronics"],
    "Propulsion": ["Aerospace", "Engineering"],
    "Orbital Mechanics": ["Aerospace", "Physics"],
    "Mission Design": ["Aerospace", "Systems Engineering"],
    
    # Global Frontier: NewSpace
    "GNC": ["Aerospace", "Physics", "Math"],
    "CubeSats": ["Aerospace", "Satellites"],
    "Satellite Ops": ["Aerospace", "Operations"],
    
    # Global Frontier: Quantum
    "Qiskit": ["Quantum Computing", "Python"],
    "Quantum Algorithms": ["Quantum Computing", "Mathematics", "Computer Science"],
    "Parallel Programming": ["HPC", "Computer Science"],
    
    # Global Frontier: Gaming/XR
    "Unreal Engine": ["Game Development", "Graphics", "C++"],
    "Unity 3D": ["Game Development", "XR", "C#"],
    "Spatial Computing": ["AR/VR", "User Experience"],
    
    # Global Frontier: AgTech
    "NDVI Analysis": ["AgTech", "Data Analysis", "GIS"],
    "Vertical Farming": ["AgTech", "Sustainability", "Engineering"],
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
    
    "Digital Marketing": ["Campaign Management", "Analytics", "Content Strategy", "SEO", "SEM", "Budgeting"],
    "SEO": ["Content Marketing", "Analytics", "Keyword Research"],
    "SEM": ["PPC", "Google Ads", "Analytics"],
    "Social Media Marketing": ["Content Creation", "Community Management", "Analytics"],
    
    "Project Management": ["Planning", "Risk Management", "Budgeting", "Team Coordination", "Pianificazione"],
    "Product Management": ["Market Research", "User Research", "Data Analysis", "Agile"],
    
    "Business Intelligence": ["Data Analysis", "Reporting", "Visualization", "SQL"],
    "Data Analysis": ["Excel", "SQL", "Statistics", "Reporting", "Visualization", "Critical Thinking"],
    "Analytics": ["Data Analysis", "Reporting", "Metrics", "KPI Management"],
    "Advanced Excel": ["Excel", "Spreadsheets", "Data Analysis", "VBA"],
    "Marketing Analytics": ["Google Analytics", "Excel", "Data Analysis", "SQL", "KPI Management"],
    "Performance Marketing": ["PPC", "SEM", "Google Ads", "Facebook Ads", "KPI Management", "Analytics", "Data Analysis", "Budgeting"],
    "KPI Management": ["Reporting", "Analytics", "Strategy", "Data Analysis"],
    
    "UX Design": ["User Research", "Prototyping", "Wireframing", "Usability Testing"],
    "UI Design": ["Visual Design", "Typography", "Color Theory", "Design Tools"],
    
    "Cybersecurity": ["Network Security", "Risk Management", "Compliance", "Incident Response"],
    "Network Security": ["Networking", "Firewall Management", "Security Protocols"],
    
    "Seniority": ["Leadership", "Project Management", "Team Management"],
    
    # Sustainability Implications
    "Sustainability Manager": ["Sustainability", "ESG Reporting", "Carbon Footprint", "LCA", "Compliance"],
    "ESG Analyst": ["Sustainability", "ESG Reporting", "Data Analysis", "Reporting"],
    
    # E-commerce Implications
    "E-commerce Manager": ["E-commerce", "Digital Marketing", "Analytics", "Inventory Management", "Shopify"],
    "Growth Hacker": ["Digital Marketing", "Analytics", "CRO", "Content Strategy"],
    
    # Legal Tech & Compliance
    "DPO": ["GDPR", "Privacy", "Compliance", "Risk Management"],
    "Compliance Officer": ["Compliance", "Risk Management", "Reporting", "Legal Tech"],
    
    # HealthTech
    "Informatics Specialist": ["HealthTech", "EHR", "Data Analysis", "HL7"],
    "Clinical Data Manager": ["HealthTech", "CDM", "Clinical Research", "Data Analysis"],
    
    # Luxury & Fashion Implications
    "Luxury Store Manager": ["Luxury Retail", "Visual Merchandising", "Team Management", "Salesforce", "Customer Experience"],
    "Merchandising Manager": ["Fashion Merchandising", "Data Analysis", "Textile Knowledge", "Inventory Management"],
    
    # Hospitality Implications
    "Hotel General Manager": ["Hotel Management", "Revenue Management", "Team Management", "Guest Experience", "Budgeting"],
    "Revenue Manager": ["Revenue Management", "Excel", "Data Analysis", "PMS Software", "Pricing Strategy"],
    
    # Automotive Implications
    "Automotive Engineer": ["Automotive Engineering", "MATLAB", "Simulation", "Vehicle Dynamics", "Powertrain"],
    "Aerodynamics Specialist": ["Aerodynamics", "CFD", "Physics", "Mathematics"],
    
    # Fintech Implications
    "Blockchain Developer": ["Blockchain", "Solidity", "Smart Contracts", "Cryptography", "Git"],
    "Fintech PM": ["Product Management", "Open Banking", "Agile", "Compliance", "Data Analysis"],
    
    # Aerospace Implications
    "Systems Engineer (Aerospace)": ["Systems Engineering", "Mission Design", "Propulsion", "Avionics", "Aerodynamics"],
    "Satellite Engineer": ["Orbital Mechanics", "Propulsion", "Systems Engineering", "Communication"],
    
    # Global Frontier Implications
    "Space Systems Architect": ["Space Systems", "Mission Design", "Satellite Ops", "Systems Engineering", "GNC"],
    "Quantum Researcher": ["Quantum Computing", "Quantum Algorithms", "Physics", "Mathematics", "Python"],
    "XR Developer": ["Spatial Computing", "Unity 3D", "Unreal Engine", "C#", "C++", "UI/UX Basics"],
    "AgTech Specialist": ["Precision Farming", "IoT", "Data Analysis", "Sustainability", "Hydroponics"],
    "Supply Chain Director": ["Logistics", "4PL Logistics", "Risk Management", "Business Strategy", "Analytics"],
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
    
    # Marketing Metrics (Performance Specific)
    "performance_metrics": {
        "name": "Performance Marketing Metrics",
        "skills": {"KPI", "ROI", "ROAS", "CPA", "CTR", "CPC", "Conversion Rate", "CAC", "LTV"},
        "transferability": "very high"
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
    "Copywriting": ["copywriting", "copy", "scrittura persuasiva"],
    "Branding": ["branding", "brand strategy", "posizionamento brand", "identità di marca"],
    "Campaign Management": ["campaign management", "gestione campagne", "digital campaigns", "performance marketing", "direct marketing", "media planning", "advertising"],
    "Performance Marketing": ["performance marketing", "paid ads", "media buying", "paid performance", "growth marketing", "conversion optimization", "advertising online", "campagne a performance"],
    "KPI Management": ["kpi management", "gestione kpi", "okr", "performance measurement", "kpi tracking", "misurazione performance", "key performance indicators"],
    
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
    "Planning": ["planning", "pianificazione", "pianificazione strategica", "strategic planning"],
    "Budgeting": ["budgeting", "budget management", "gestione budget", "budget", "p&l management"],
    "Leadership": ["leadership", "team leadership"],
    "Stakeholder Management": ["stakeholder management"],
    
    # ========== FINANCE & ACCOUNTING ==========
    "Accounting": ["accounting", "contabilità", "billing", "financial reporting", "marketing accounting", "fatturazione", "amministrazione"],
    "Financial Analysis": ["financial analysis", "analisi finanziaria", "financial reporting"],
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

    # ========== DATA & ANALYTICS (STANDARD) ==========
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

    # ========== ENGINEERING ==========
    "Engineering": ["engineering", "ingegneria", "technical", "tecnico"],
    "CAD": ["autocad", "solidworks", "catia", "nx", "ptc creo", "revit", "bim", "civil 3d", "microstation", "cad"],
    "Simulation": ["ansys", "abaqus", "comsol", "simulink", "matlab", "labview", "hysys", "aspen plus", "fluent", "cfd"],
    "Electronics": ["pcb design", "altium designer", "eagle", "proteus", "kicad", "spice", "vhdl", "verilog", "fpga", "arduino", "raspberry pi", "plc", "scada"],
    "Energy Engineering": ["energy engineering", "energy engineer", "ingegneria energetica", "energy manager"],
    "Thermodynamics": ["thermodynamics", "termodinamica"],
    "Power Systems": ["power systems", "sistemi elettrici", "grid", "smart grid"],
    "Energy Efficiency": ["energy efficiency", "efficienza energetica", "energy saving"],
    "Renewable Energy": ["renewable energy", "energie rinnovabili", "renewables", "solar energy", "wind energy", "photovoltaics", "pv"],
    "MATLAB": ["matlab", "simulink"],
    "AutoCAD": ["autocad"],

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

    # ========== SUSTAINABILITY & ESG (DETAILED) ==========
    "Sustainability": ["sustainability", "sostenibilità", "esg", "environmental social governance"],
    "LCA": ["life cycle assessment", "lca", "analisi del ciclo di vita"],
    "Carbon Footprint": ["carbon footprint", "impronta di carbonio", "carbon accounting", "emissioni co2"],
    "ESG Reporting": ["gri", "sasb", "tcfd", "esg report", "sustainability reporting"],
    "Circular Economy": ["circular economy", "economia circolare", "waste management"],

    # ========== E-COMMERCE & DIGITAL COMMERCE (DETAILED) ==========
    "E-commerce": ["e-commerce", "ecommerce", "online shop", "marketplace"],
    "Shopify": ["shopify"],
    "Magento": ["magento", "adobe commerce"],
    "Amazon Marketplace": ["amazon seller central", "fba", "amazon marketplace"],
    "Conversion Rate Optimization": ["cro", "conversion rate optimization", "a/b testing"],
    "Digital Payments": ["stripe", "paypal", "payments gateway"],

    # ========== LEGAL TECH & COMPLIANCE (DETAILED) ==========
    "Legal Tech": ["legal tech", "legal operations", "clm", "contract lifecycle management"],
    "GDPR": ["gdpr", "data privacy", "privacy by design", "dpo"],
    "Compliance": ["compliance", "regulatory compliance", "risk & compliance"],
    "Anti-Money Laundering": ["aml", "anti-money laundering", "kyc", "antiriciclaggio"],

    # ========== HEALTHTECH & CLINICAL DATA (DETAILED) ==========
    "HealthTech": ["healthtech", "digital health", "e-health"],
    "HL7": ["hl7", "fhira", "interoperability healthcare"],
    "Electronic Health Records": ["ehr", "emr", "cartella clinica elettronica"],
    "Clinical Data Management": ["clinical data management", "cdm", "clinical trials data"],

    # ========== LUXURY & FASHION (ITA-GLOBAL) ==========
    "Luxury Retail": ["luxury retail", "clienteling", "luxury store management", "alta moda", "high-end retail"],
    "Visual Merchandising": ["visual merchandising", "vetrinistica", "allestimento", "window display"],
    "Textile Knowledge": ["textiles", "tessuti", "materials knowledge", "haute couture", "sartorial"],
    "Fashion Merchandising": ["merchandising", "product selection", "assortment planning"],
    "Brand Heritage": ["brand heritage", "brand storytelling", "history of fashion"],

    # ========== HOSPITALITY & PREMIUM TOURISM (ITA-GLOBAL) ==========
    "Hotel Management": ["hotel management", "front office management", "hospitality operations", "direzione alberghiera"],
    "Revenue Management": ["revenue management", "yield management", "pricing strategy", "otas"],
    "PMS Software": ["opera pms", "prohotelier", "hotel software", "pms"],
    "Guest Experience": ["guest relation", "guest experience", "concierge", "customer satisfaction hospitality"],
    "Event Planning (Tourism)": ["mice", "meetings incentives conferences exhibitions", "event management"],

    # ========== AUTOMOTIVE & MOTOR VALLEY (ITA) ==========
    "Vehicle Dynamics": ["vehicle dynamics", "dinamica veicolo", "handing", "suspension tuning"],
    "Powertrain": ["powertrain", "motore", "engine mapping", "transmission systems", "e-powertrain"],
    "Automotive Engineering": ["automotive engineering", "ingegneria del veicolo", "car design technical"],
    "CFD (Automotive)": ["computational fluid dynamics", "cfd", "aerodinamica", "wind tunnel testing"],

    # ========== FINTECH & WEB3 ==========
    "Blockchain": ["blockchain", "distributed ledger", "web3", "smart contracts"],
    "Solidity": ["solidity", "ethereum", "evm"],
    "Cryptography": ["cryptography", "crittografia", "encryption"],
    "Open Banking": ["open banking", "psd2", "fintech apis"],
    "Algorithmic Trading": ["algo trading", "quantitative trading", "hft"],

    # ========== AEROSPACE & DEFENSE ==========
    "Aerodynamics": ["aerodynamics", "aerodinamica", "fluid dynamics aerospace"],
    "Avionics": ["avionics", "avionica", "flight control systems"],
    "Propulsion": ["propulsion", "propulsione", "jet engines", "rocket science"],
    "Orbital Mechanics": ["orbital mechanics", "astrodynamics", "satellite trajectories"],
    "Systems Engineering (Aerospace)": ["systems engineering", "mission design", "space systems"],

    # ========== NEWSPACE & SPACE EXPLORATION (GLOBAL FRONTIER) ==========
    "Satellite Operations": ["satellite ops", "ground station", "mission control", "telemetry", "tt&c"],
    "GNC": ["guidance navigation control", "gnc", "attitude control", "adcs", "orbit determination"],
    "CubeSats": ["cubesat", "nanosatellite", "smallsat", "space systems design"],
    "Space Mechanics": ["stk", "systems tool kit", "freeflyer", "gmat", "orbit analysis"],
    "Lunar Economy": ["lunar exploration", "isru", "moon base", "lunar logistics"],

    # ========== QUANTUM COMPUTING & HPC (GLOBAL FRONTIER) ==========
    "Quantum Algorithms": ["quantum algorithms", "shor's algorithm", "grover's algorithm", "vqe", "qaoa"],
    "Qiskit": ["qiskit", "ibm quantum"],
    "Cirq": ["cirq", "google quantum"],
    "Quantum Hardware": ["superconducting qubits", "ion traps", "topological qubits", "quantum error correction"],
    "Parallel Programming": ["cuda", "opencl", "mpi", "openmp", "high performance computing", "hpc"],

    # ========== ADVANCED LOGISTICS & SUPPLY CHAIN (GLOBAL FRONTIER) ==========
    "4PL Logistics": ["4pl", "fourth party logistics", "supply chain orchestration"],
    "Cold Chain": ["cold chain", "refrigerated logistics", "temperature controlled", "pharma logistics"],
    "Last-mile Optimization": ["last-mile", "routing algorithms", "delivery optimization", "micro-fulfillment"],
    "Supply Chain Resilience": ["risk management supply chain", "resilience planning", "supply chain visibility"],

    # ========== GAMING, AR/VR & METAVERSE (GLOBAL FRONTIER) ==========
    "Unreal Engine": ["unreal engine 5", "ue5", "blueprints", "niagara", "nanite"],
    "Unity 3D": ["unity", "unity3d", "c# gaming"],
    "Spatial Computing": ["ar", "vr", "augmented reality", "virtual reality", "mixed reality", "xr", "oculus", "hololens"],
    "Game Engine Design": ["game engine development", "rendering pipeline", "physics engine"],
    "Metaverse Architecture": ["digital twins", "virtual worlds", "3d environment design"],

    # ========== ADVANCED AGTECH (GLOBAL FRONTIER) ==========
    "Precision Farming": ["precision agriculture", "precision farming", "ndvi", "satellite imaging ag"],
    "Hydroponics": ["hydroponics", "aeroponics", "aquaponics", "vertical farming", "soilless culture"],
    "Drone Mapping": ["uav mapping", "drone photogrammetry", "ag-drones", "pix4d"],
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
# =============================================================================
# SECTION 3: SKILL CLUSTERS (EQUIVALENT TOOLS)
# =============================================================================

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

    # ========== DATA & ANALYTICS (STANDARD) ==========
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
INFERENCE_RULES = SKILL_HIERARCHY  # Alias for backward compatibility

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


# =============================================================================
# SECTION 6: LEARNING RESOURCES DATABASE
# =============================================================================
# Maps skills to learning resources with metadata for Learning Path Generator

LEARNING_RESOURCES = {
    # === PROGRAMMING ===
    "Python": [
        {"title": "Python for Everybody", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 25, "url": "https://www.coursera.org/specializations/python", "free": True},
        {"title": "Complete Python Bootcamp", "platform": "Udemy", "difficulty": "beginner", "duration_hours": 22, "url": "https://www.udemy.com/course/complete-python-bootcamp/", "free": False},
        {"title": "Python Tutorial", "platform": "freeCodeCamp", "difficulty": "beginner", "duration_hours": 4, "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "free": True},
    ],
    "JavaScript": [
        {"title": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "difficulty": "beginner", "duration_hours": 30, "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "free": True},
        {"title": "The Complete JavaScript Course", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 69, "url": "https://www.udemy.com/course/the-complete-javascript-course/", "free": False},
    ],
    "Java": [
        {"title": "Java Programming and Software Engineering", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 40, "url": "https://www.coursera.org/specializations/java-programming", "free": True},
    ],
    "SQL": [
        {"title": "SQL for Data Science", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 15, "url": "https://www.coursera.org/learn/sql-for-data-science", "free": True},
        {"title": "The Complete SQL Bootcamp", "platform": "Udemy", "difficulty": "beginner", "duration_hours": 9, "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/", "free": False},
        {"title": "SQLBolt Interactive Tutorial", "platform": "SQLBolt", "difficulty": "beginner", "duration_hours": 3, "url": "https://sqlbolt.com/", "free": True},
    ],
    
    # === WEB DEVELOPMENT ===
    "React": [
        {"title": "React - The Complete Guide", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 48, "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "free": False},
        {"title": "React Tutorial", "platform": "React Docs", "difficulty": "beginner", "duration_hours": 5, "url": "https://react.dev/learn", "free": True},
    ],
    "Node.js": [
        {"title": "Node.js, Express, MongoDB & More", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 42, "url": "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/", "free": False},
    ],
    "HTML": [
        {"title": "Responsive Web Design", "platform": "freeCodeCamp", "difficulty": "beginner", "duration_hours": 15, "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "free": True},
    ],
    "CSS": [
        {"title": "CSS - The Complete Guide", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 22, "url": "https://www.udemy.com/course/css-the-complete-guide-incl-flexbox-grid-sass/", "free": False},
    ],
    
    # === DATA SCIENCE & ML ===
    "Machine Learning": [
        {"title": "Machine Learning Specialization", "platform": "Coursera", "difficulty": "intermediate", "duration_hours": 60, "url": "https://www.coursera.org/specializations/machine-learning-introduction", "free": True},
        {"title": "Intro to Machine Learning", "platform": "Kaggle", "difficulty": "beginner", "duration_hours": 10, "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "free": True},
    ],
    "Deep Learning": [
        {"title": "Deep Learning Specialization", "platform": "Coursera", "difficulty": "advanced", "duration_hours": 80, "url": "https://www.coursera.org/specializations/deep-learning", "free": True},
        {"title": "Practical Deep Learning for Coders", "platform": "fast.ai", "difficulty": "intermediate", "duration_hours": 30, "url": "https://course.fast.ai/", "free": True},
    ],
    "Statistics": [
        {"title": "Statistics with Python", "platform": "Coursera", "difficulty": "intermediate", "duration_hours": 30, "url": "https://www.coursera.org/specializations/statistics-with-python", "free": True},
        {"title": "Khan Academy Statistics", "platform": "Khan Academy", "difficulty": "beginner", "duration_hours": 20, "url": "https://www.khanacademy.org/math/statistics-probability", "free": True},
    ],
    "Data Visualization": [
        {"title": "Data Visualization with Tableau", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 20, "url": "https://www.coursera.org/specializations/data-visualization", "free": True},
    ],
    "TensorFlow": [
        {"title": "TensorFlow Developer Certificate", "platform": "Coursera", "difficulty": "intermediate", "duration_hours": 50, "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice", "free": True},
    ],
    
    # === CLOUD & DEVOPS ===
    "AWS": [
        {"title": "AWS Certified Cloud Practitioner", "platform": "AWS", "difficulty": "beginner", "duration_hours": 20, "url": "https://aws.amazon.com/training/learn-about/cloud-practitioner/", "free": True},
        {"title": "AWS Solutions Architect", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 27, "url": "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/", "free": False},
    ],
    "Docker": [
        {"title": "Docker for Beginners", "platform": "YouTube", "difficulty": "beginner", "duration_hours": 4, "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo", "free": True},
        {"title": "Docker Mastery", "platform": "Udemy", "difficulty": "intermediate", "duration_hours": 20, "url": "https://www.udemy.com/course/docker-mastery/", "free": False},
    ],
    "Kubernetes": [
        {"title": "Kubernetes for the Absolute Beginners", "platform": "Udemy", "difficulty": "beginner", "duration_hours": 5, "url": "https://www.udemy.com/course/learn-kubernetes/", "free": False},
    ],
    "Git": [
        {"title": "Git and GitHub for Beginners", "platform": "freeCodeCamp", "difficulty": "beginner", "duration_hours": 1, "url": "https://www.youtube.com/watch?v=RGOj5yH7evk", "free": True},
    ],
    "CI/CD": [
        {"title": "CI/CD with GitHub Actions", "platform": "LinkedIn Learning", "difficulty": "intermediate", "duration_hours": 4, "url": "https://www.linkedin.com/learning/learning-github-actions-2", "free": False},
    ],
    
    # === DESIGN ===
    "Figma": [
        {"title": "Figma Tutorial for Beginners", "platform": "YouTube", "difficulty": "beginner", "duration_hours": 3, "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8", "free": True},
        {"title": "Figma UI UX Design Essentials", "platform": "Udemy", "difficulty": "beginner", "duration_hours": 12, "url": "https://www.udemy.com/course/figma-ux-ui-design-user-experience-tutorial-course/", "free": False},
    ],
    "UX Design": [
        {"title": "Google UX Design Certificate", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 150, "url": "https://www.coursera.org/professional-certificates/google-ux-design", "free": True},
    ],
    
    # === BUSINESS & MARKETING ===
    "Excel": [
        {"title": "Excel Skills for Business", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 24, "url": "https://www.coursera.org/specializations/excel", "free": True},
    ],
    "Power BI": [
        {"title": "Microsoft Power BI Data Analyst", "platform": "Microsoft Learn", "difficulty": "intermediate", "duration_hours": 30, "url": "https://learn.microsoft.com/en-us/training/courses/pl-300t00", "free": True},
    ],
    "Google Analytics": [
        {"title": "Google Analytics Certification", "platform": "Google Skillshop", "difficulty": "beginner", "duration_hours": 5, "url": "https://skillshop.withgoogle.com/", "free": True},
    ],
    "SEO": [
        {"title": "SEO Training Course", "platform": "HubSpot Academy", "difficulty": "beginner", "duration_hours": 4, "url": "https://academy.hubspot.com/courses/seo-training", "free": True},
    ],
    "Digital Marketing": [
        {"title": "Google Digital Marketing Certificate", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 80, "url": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce", "free": True},
    ],
    
    # === PROJECT MANAGEMENT ===
    "Agile": [
        {"title": "Agile with Atlassian Jira", "platform": "Coursera", "difficulty": "beginner", "duration_hours": 12, "url": "https://www.coursera.org/learn/agile-atlassian-jira", "free": True},
    ],
    "Product Management": [
        {"title": "Digital Product Management", "platform": "Coursera", "difficulty": "intermediate", "duration_hours": 25, "url": "https://www.coursera.org/specializations/uva-darden-digital-product-management", "free": True},
    ],
    "Scrum": [
        {"title": "Scrum Master Certification", "platform": "LinkedIn Learning", "difficulty": "intermediate", "duration_hours": 5, "url": "https://www.linkedin.com/learning/cert-prep-scrum-master", "free": False},
    ],
}


# =============================================================================
# SECTION 7: INTERVIEW QUESTIONS DATABASE
# =============================================================================
# Organized by role and question type for Interview Simulator

INTERVIEW_QUESTIONS = {
    # === BEHAVIORAL QUESTIONS (All Roles) ===
    "behavioral": [
        {"question": "Tell me about a time when you had to deal with a difficult colleague.", "category": "teamwork", "star_focus": "situation, task, action, result"},
        {"question": "Describe a project where you had to meet a tight deadline.", "category": "time_management", "star_focus": "situation, action, result"},
        {"question": "Give an example of when you showed leadership.", "category": "leadership", "star_focus": "situation, task, action, result"},
        {"question": "Tell me about a time you failed and what you learned.", "category": "growth", "star_focus": "situation, action, result, learning"},
        {"question": "Describe a situation where you had to adapt to change.", "category": "adaptability", "star_focus": "situation, action, result"},
        {"question": "How do you prioritize when you have multiple deadlines?", "category": "organization", "star_focus": "situation, method, result"},
        {"question": "Tell me about a time you solved a complex problem.", "category": "problem_solving", "star_focus": "situation, task, action, result"},
        {"question": "Describe a situation where you had to persuade someone.", "category": "communication", "star_focus": "situation, approach, result"},
    ],
    
    # === TECH ROLES ===
    "Software Engineer": [
        {"question": "Explain the difference between REST and GraphQL APIs.", "category": "technical", "expected_keywords": ["rest", "graphql", "endpoint", "query", "schema"]},
        {"question": "How would you design a URL shortening service?", "category": "system_design", "expected_keywords": ["hash", "database", "redirect", "scalability"]},
        {"question": "What is your approach to debugging a production issue?", "category": "problem_solving", "expected_keywords": ["logs", "reproduce", "isolate", "fix", "monitor"]},
        {"question": "Explain SOLID principles.", "category": "technical", "expected_keywords": ["single responsibility", "open closed", "liskov", "interface", "dependency"]},
    ],
    
    "Data Scientist": [
        {"question": "Explain the bias-variance tradeoff.", "category": "technical", "expected_keywords": ["bias", "variance", "overfitting", "underfitting", "complexity"]},
        {"question": "How do you handle missing data?", "category": "technical", "expected_keywords": ["imputation", "mean", "median", "mode", "drop", "model"]},
        {"question": "Walk me through a machine learning project you've worked on.", "category": "experience", "expected_keywords": ["data", "model", "training", "evaluation", "deployment"]},
        {"question": "What metrics would you use for a classification problem?", "category": "technical", "expected_keywords": ["accuracy", "precision", "recall", "f1", "auc", "roc"]},
    ],
    
    "Data Analyst": [
        {"question": "How would you explain a complex analysis to a non-technical stakeholder?", "category": "communication", "expected_keywords": ["visualize", "simple", "business impact", "story"]},
        {"question": "What's your process for investigating a data anomaly?", "category": "analytical", "expected_keywords": ["source", "validate", "compare", "hypothesis", "root cause"]},
        {"question": "Describe a time when your analysis influenced a business decision.", "category": "impact", "expected_keywords": ["insight", "recommendation", "decision", "result"]},
    ],
    
    "Product Manager": [
        {"question": "How do you prioritize features?", "category": "strategy", "expected_keywords": ["impact", "effort", "user", "business", "data", "stakeholder"]},
        {"question": "Describe your ideal product development process.", "category": "process", "expected_keywords": ["discovery", "design", "development", "testing", "launch", "iteration"]},
        {"question": "How do you measure product success?", "category": "metrics", "expected_keywords": ["kpi", "metrics", "user", "retention", "engagement", "revenue"]},
    ],
    
    "UX Designer": [
        {"question": "Walk me through your design process.", "category": "process", "expected_keywords": ["research", "user", "wireframe", "prototype", "test", "iterate"]},
        {"question": "How do you handle feedback that conflicts with your design?", "category": "collaboration", "expected_keywords": ["listen", "data", "user", "compromise", "advocate"]},
        {"question": "Describe a challenging usability problem you solved.", "category": "problem_solving", "expected_keywords": ["research", "user", "test", "solution", "improvement"]},
    ],
    
    # === HR QUESTIONS (All Roles) ===
    "hr": [
        {"question": "Why are you interested in this role?", "category": "motivation", "good_answer_includes": ["company mission", "role fit", "growth", "impact"]},
        {"question": "Where do you see yourself in 5 years?", "category": "career", "good_answer_includes": ["growth", "skills", "contribution", "leadership"]},
        {"question": "Why are you leaving your current job?", "category": "motivation", "good_answer_includes": ["growth", "challenge", "opportunity", "positive framing"]},
        {"question": "What are your salary expectations?", "category": "negotiation", "good_answer_includes": ["research", "range", "value", "flexibility"]},
        {"question": "What's your greatest strength?", "category": "self_awareness", "good_answer_includes": ["specific", "example", "relevance"]},
        {"question": "What's your greatest weakness?", "category": "self_awareness", "good_answer_includes": ["genuine", "improvement", "mitigation"]},
    ],
}


# =============================================================================
# SECTION 8: JOB MARKET TRENDS
# =============================================================================

SKILL_DEMAND_TRENDS = {
    "Python": {"demand": 95, "growth": "+15%", "sector": "Technology"},
    "JavaScript": {"demand": 92, "growth": "+10%", "sector": "Technology"},
    "SQL": {"demand": 90, "growth": "+8%", "sector": "Data"},
    "AWS": {"demand": 88, "growth": "+20%", "sector": "Cloud"},
    "Machine Learning": {"demand": 85, "growth": "+25%", "sector": "AI/ML"},
    "React": {"demand": 85, "growth": "+12%", "sector": "Web"},
    "Docker": {"demand": 82, "growth": "+18%", "sector": "DevOps"},
    "Kubernetes": {"demand": 78, "growth": "+22%", "sector": "DevOps"},
    "TypeScript": {"demand": 78, "growth": "+30%", "sector": "Web"},
    "Data Analysis": {"demand": 88, "growth": "+15%", "sector": "Data"},
    "Power BI": {"demand": 75, "growth": "+20%", "sector": "BI"},
    "Tableau": {"demand": 72, "growth": "+12%", "sector": "BI"},
    "Figma": {"demand": 70, "growth": "+25%", "sector": "Design"},
    "Agile": {"demand": 80, "growth": "+10%", "sector": "Management"},
    "Git": {"demand": 92, "growth": "+5%", "sector": "Development"},
    "Node.js": {"demand": 78, "growth": "+10%", "sector": "Web"},
    "Deep Learning": {"demand": 72, "growth": "+30%", "sector": "AI/ML"},
    "Cybersecurity": {"demand": 85, "growth": "+28%", "sector": "Security"},
    "CI/CD": {"demand": 80, "growth": "+15%", "sector": "DevOps"},
    "Product Management": {"demand": 82, "growth": "+12%", "sector": "Product"},
}


# =============================================================================
# SECTION 9: COMPANY PROFILES (For Company Research)
# =============================================================================

COMPANY_PROFILES = {
    "Google": {
        "sector": "Technology",
        "culture": ["Innovation", "Data-Driven", "Open Culture", "20% Time"],
        "values": ["Focus on the user", "Fast is better than slow", "Democracy on the web works", "Great just isn't good enough"],
        "interview_tips": ["Practice coding on whiteboard", "Show problem-solving process", "Ask clarifying questions", "Use STAR method for behavioral"],
        "common_questions": ["Design a parking lot system", "Tell me about a challenging project", "How would you improve Google Maps?"],
        "remote_policy": "Hybrid",
        "glassdoor_rating": 4.4,
    },
    "Microsoft": {
        "sector": "Technology",
        "culture": ["Growth Mindset", "Inclusion", "One Microsoft", "Customer Obsessed"],
        "values": ["Respect", "Integrity", "Accountability"],
        "interview_tips": ["Prepare for behavioral and technical", "Know Azure products", "Show growth mindset examples"],
        "common_questions": ["Why Microsoft?", "Describe a time you failed", "Design an elevator system"],
        "remote_policy": "Hybrid",
        "glassdoor_rating": 4.3,
    },
    "Amazon": {
        "sector": "Technology/E-commerce",
        "culture": ["Customer Obsession", "Ownership", "Bias for Action", "Leadership Principles"],
        "values": ["Customer Obsession", "Invent and Simplify", "Dive Deep", "Have Backbone; Disagree and Commit"],
        "interview_tips": ["Study Leadership Principles deeply", "Use STAR method", "Prepare data-driven examples", "Show ownership"],
        "common_questions": ["Tell me about a time you disagreed with your manager", "Describe a time you failed", "How do you prioritize?"],
        "remote_policy": "Office-first",
        "glassdoor_rating": 3.9,
    },
    "Meta": {
        "sector": "Technology/Social Media",
        "culture": ["Move Fast", "Be Bold", "Focus on Impact", "Be Open"],
        "values": ["Move fast", "Build awesome things", "Live in the future", "Be direct and respect your colleagues"],
        "interview_tips": ["Prepare for system design", "Practice coding problems", "Show passion for the mission"],
        "common_questions": ["Why Meta?", "Design Instagram stories", "Tell me about a complex bug you fixed"],
        "remote_policy": "Hybrid",
        "glassdoor_rating": 4.0,
    },
    "Apple": {
        "sector": "Technology/Hardware",
        "culture": ["Secrecy", "Design Excellence", "Innovation", "Attention to Detail"],
        "values": ["Accessibility", "Environment", "Privacy", "Supplier Responsibility"],
        "interview_tips": ["Show passion for Apple products", "Attention to detail is key", "Be ready for multiple rounds"],
        "common_questions": ["Why Apple?", "Describe your favorite Apple product", "How would you improve Siri?"],
        "remote_policy": "Office-first",
        "glassdoor_rating": 4.2,
    },
    "Netflix": {
        "sector": "Entertainment/Technology",
        "culture": ["Freedom & Responsibility", "No Rules Rules", "Radical Candor", "Keeper Test"],
        "values": ["Judgment", "Communication", "Curiosity", "Courage", "Passion", "Selflessness", "Innovation", "Inclusion", "Integrity", "Impact"],
        "interview_tips": ["Read the Culture Deck", "Show independent judgment", "Prepare for tough behavioral questions"],
        "common_questions": ["Give an example of taking an unpopular stance", "How do you handle ambiguity?", "Describe a time you gave difficult feedback"],
        "remote_policy": "Hybrid",
        "glassdoor_rating": 4.0,
    },
    "Spotify": {
        "sector": "Entertainment/Technology",
        "culture": ["Squad Model", "Autonomous Teams", "Data-Driven", "Be Real"],
        "values": ["Innovative", "Sincere", "Passionate", "Collaborative", "Playful"],
        "interview_tips": ["Know the squad/tribe model", "Show data-driven thinking", "Demonstrate collaboration skills"],
        "common_questions": ["How would you improve Spotify playlists?", "Tell me about working in autonomous teams"],
        "remote_policy": "Work from Anywhere",
        "glassdoor_rating": 4.1,
    },
}
