import os
import pypdf

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def dump_pages(pdf_path, start_page, end_page, out_name):
    reader = pypdf.PdfReader(pdf_path)
    with open(os.path.join(BASE_DIR, "data", "processed", out_name), "w", encoding="utf-8") as f:
        for i in range(start_page - 1, min(end_page, len(reader.pages))):
            f.write(f"\n==================== PAGE {i+1} ====================\n")
            f.write(reader.pages[i].extract_text() or "")
    print(f"Dumped pages {start_page} to {end_page} of {os.path.basename(pdf_path)}")

dump_pages(
    os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Individual 2025 - EPEC-AR.pdf"),
    25, 45, "indiv_2025_p25_45.txt"
)
dump_pages(
    os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Individual 2026 - EPEC-AR.pdf"),
    25, 45, "indiv_2026_p25_45.txt"
)
dump_pages(
    os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Com entre Rondas 2026 - EPEC-AR.pdf"),
    1, 30, "rondas_2026_p1_30.txt"
)
