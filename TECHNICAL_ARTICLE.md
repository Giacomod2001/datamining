# Inside CareerMatch AI: How We Built a Smart Job Matching Engine with NLP and Python

**By Giacomo Dell'Acqua & Team** | *Data Mining & Text Analytics Project @ IULM University*

In an era where Applicant Tracking Systems (ATS) filter out 75% of resumes before they even reach a human recruiter, understanding "machine logic" has become a crucial survival skill for job seekers.

For our University project, instead of just analyzing this problem, we decided to solve it. We built **CareerMatch AI**, an open-source tool that reverse-engineers the hiring process, giving candidates the extracted insights they need to optimize their applications.

Here is a deep dive into the technology stack, the Machine Learning pipeline, and the Natural Language Processing (NLP) logic that powers our application.

---

## 🤖 The Core Mission: Beyond Simple Keyword Matching

Most basic "resume checkers" perform a simple `Ctrl+F` for keywords. If a job asks for "Python" and you have "Python", it’s a match.
But hiring is more nuanced. Recruiters look for **context**, **soft skills**, and **implied capabilities**.

We designed CareerMatch AI to simulate this closer reading using a multi-stage NLP pipeline. The goal was to answer three questions for the user:

1. **How well do I fit this specific role?** (Matching)
2. **What am I missing?** (Gap Analysis)
3. **What else could I do?** (Career Discovery)

---

## ⚙️ The Architecture: Under the Hood

The application is built entirely in **Python**, leveraging the **Streamlit** framework for a responsive, interactive frontend. The backend processing relies on a robust stack of Data Science libraries:

* **Natural Language Processing:** `NLTK`, `TheFuzz`, `scikit-learn`
* **Vectorization & Modeling:** `TfidfVectorizer`, `CountVectorizer`
* **Data Structure:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Altair`

### 1. The Knowledge Base: Defining the "Ground Truth"

Before analyzing any text, we needed a reference model. We constructed a proprietary (but open) database of **230+ Job Archetypes** and **950+ "Killer Keywords"**.

* **Archetypes:** Pre-defined profiles (e.g., "Data Scientist", "SEO Specialist", "Energy Trader") that contain standard expected hard and soft skills.
* **Killer Keywords:** A curated dictionary of high-impact skills with mapped variations (e.g., *Machine Learning* ↔ *ML*, *Deep Learning*, *Neural Networks*).

### 2. The NLP Pipeline: From Text to Structued Data

When a user uploads a CV (PDF) and pastes a Job Description, the raw text goes through a rigorous preprocessing phase:

1. **Text Extraction:** `PyPDF2` strips content from PDFs, handling standard layouts.
2. **Normalization:** Text is lowercased, and special characters are cleaned. We preserve crucial acronyms (like "AWS", "SQL") that standard tokenizers might destroy.
3. **N-Gram & Fuzzy Extraction:**
    * We don't just look for exact matches. We use **N-Grams** (1-3 word sequences) to capture multi-word skills like "Project Management".
    * We employ **Fuzzy Matching** (via `TheFuzz`) to handle typos or variations (e.g., "Ms Excel" vs "Microsoft Excel"), reducing false negatives.
4. **Archetype Fallback:** If a Job Description is sparse (e.g., "Looking for a Data Analyst"), our system detects the intent and "injects" missing implied skills from our Archetype database to provide a fairer analysis.

### 3. The Matching Engine: Calculating the Score

We moved beyond simple keyword counts to a weighted similarity score. Our "Gap Analysis" engine (`analyze_gap` function) works by:

* Creating a set of **Required Skills** from the JD.
* Creating a set of **Present Skills** from the CV.
* Calculating the intersection (Matched Skills) and the difference (Missing Skills).
* **Semantic Scoring:** We use **Cosine Similarity** on TF-IDF vectors to compare the *entire* CV text against the JD text, capturing thematic alignment beyond just skill lists.

### 4. Career Compass: The Recommendation System

One of our most advanced features is the **Career Compass**. It doesn't just grade you; it guides you.

* It takes the user's extracted skill vector.
* It computes the **Jaccard Similarity** against all 230+ defined Job Archetypes.
* It ranks the top 3 roles that arguably fit the user's *current* capabilities, often revealing career paths they hadn't considered (e.g., a "Marketing Manager" being well-suited for a "Product Owner" role).

---

## 🔒 Privacy & Open Source Ethics

We believe career data is personal. Unlike many commercial platforms, CareerMatch AI is designed with **Privacy by Design**:

* **No Database:** We do not store user CVs. All processing happens in RAM and is wiped when the session ends.
* **No Training:** User data is never used to train our models.
* **Open Source:** The entire codebase is available on GitHub for transparency and inspection.

---

## 🚀 Try It Yourself

CareerMatch AI is live and continuously evolving. We invite Data Scientists, Recruiters, and Job Seekers to test it, break it, and contribute.

* **Live App:** [dataminingiulm.streamlit.app](https://dataminingiulm.streamlit.app)
* **GitHub Repository:** [github.com/Giacomod2001/datamining](https://github.com/Giacomod2001/datamining)

*Powered by Streamlit · Developed at IULM University*
