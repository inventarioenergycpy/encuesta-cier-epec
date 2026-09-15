import os
import pypdf
import pandas as pd

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def search_pdf(pdf_path, keywords):
    print(f"\n================ SEARCHING IN: {os.path.basename(pdf_path)} ================")
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    matches = []
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if any(kw.lower() in text.lower() for kw in keywords):
            matches.append((idx + 1, text))
            
    print(f"Found {len(matches)} matching pages.")
    for page_num, text in matches[:5]:
        print(f"\n--- Page {page_num} Preview ---")
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for l in lines[:15]:
            print(f"  {l}")

if __name__ == "__main__":
    pdf_2025_dist = os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Comp entre Distrib 2025 - EPEC-AR.pdf")
    pdf_2026_dist = os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Comp entre Distrib 2026 - EPEC-AR.pdf")
    pdf_2026_rondas = os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Com entre Rondas 2026 - EPEC-AR.pdf")
    
    for p in [pdf_2025_dist, pdf_2026_dist, pdf_2026_rondas]:
        if os.path.exists(p):
            search_pdf(p, ["500", "porte", "grupo", "distribuidoras", "ranking", "iscal"])
