import os
import pypdf

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def extract_pdf_sections(pdf_path, out_txt):
    reader = pypdf.PdfReader(pdf_path)
    with open(out_txt, 'w', encoding='utf-8') as f:
        for idx, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            f.write(f"\n--- PAGE {idx+1} ---\n")
            f.write(text)
    print(f"Extracted {len(reader.pages)} pages to {out_txt}")

out25 = os.path.join(BASE_DIR, "data", "processed", "informe_distrib_2025.txt")
out26 = os.path.join(BASE_DIR, "data", "processed", "informe_distrib_2026.txt")

extract_pdf_sections(os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Comp entre Distrib 2025 - EPEC-AR.pdf"), out25)
extract_pdf_sections(os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Comp entre Distrib 2026 - EPEC-AR.pdf"), out26)
