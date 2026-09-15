import pypdf
import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
pdf_paises_26 = os.path.join(BASE_DIR, "data", "raw", "2026", "Inf Comp Paises 2026 - EPEC-AR.pdf")
pdf_paises_25 = os.path.join(BASE_DIR, "data", "raw", "2025", "Inf Comp Paises 2025 - EPEC-AR.pdf")

def dump_paises(pdf_path, out_name):
    reader = pypdf.PdfReader(pdf_path)
    with open(os.path.join(BASE_DIR, "data", "processed", out_name), "w", encoding="utf-8") as out:
        for i, page in enumerate(reader.pages):
            out.write(f"\n================ PAGE {i+1} ================\n")
            out.write(page.extract_text() or "")
    print(f"Dumped {len(reader.pages)} pages to {out_name}")

dump_paises(pdf_paises_26, "paises_2026.txt")
dump_paises(pdf_paises_25, "paises_2025.txt")
