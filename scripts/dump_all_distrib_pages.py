import os
import pypdf

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year, fname in [(2025, "Informe Comp entre Distrib 2025 - EPEC-AR.pdf"), (2026, "Informe Comp entre Distrib 2026 - EPEC-AR.pdf")]:
    pdf_path = os.path.join(BASE_DIR, "data", "raw", str(year), fname)
    reader = pypdf.PdfReader(pdf_path)
    out_txt = os.path.join(BASE_DIR, "data", "processed", f"distrib_full_pages_{year}.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            f.write(f"\n================ PAGE {i+1} ================\n")
            f.write(text.strip() + "\n")
    print(f"Dumped {len(reader.pages)} pages for {year}")
