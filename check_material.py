
import PyPDF2
import os

pdf_dir = "/Users/lucatallarico/Desktop/datamining/Materiale_corso"
files_to_check = [
    "Lecture_06 Text Classification.pdf",
    "Lecture_02_Clustering_Techniques.pdf",
    "Lecture_04. Text Mining_1.pdf"
]

keywords = ["centroid", "rocchio", "nearest mean", "prototype", "vector space", "cosine"]

print(f"Scanning for keywords: {keywords}\n")

for filename in files_to_check:
    path = os.path.join(pdf_dir, filename)
    try:
        reader = PyPDF2.PdfReader(path)
        print(f"--- {filename} ---")
        found = False
        for i, page in enumerate(reader.pages):
            text = page.extract_text().lower()
            for kw in keywords:
                if kw in text:
                    print(f"Found '{kw}' on page {i+1}")
                    found = True
        if not found:
            print("No keywords found.")
        print("\n")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
