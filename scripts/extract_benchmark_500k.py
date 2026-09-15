import os
import pypdf
import json

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def extract_all_text(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    pages = []
    for i, p in enumerate(reader.pages):
        pages.append((i+1, p.extract_text() or ""))
    return pages

# Let's inspect pages from both 2025 and 2026 reports
reports = {
    "2025_distrib": os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Comp entre Distrib 2025 - EPEC-AR.pdf"),
    "2026_distrib": os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Comp entre Distrib 2026 - EPEC-AR.pdf"),
    "2026_rondas": os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Com entre Rondas 2026 - EPEC-AR.pdf"),
    "2025_individual": os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Individual 2025 - EPEC-AR.pdf"),
    "2026_individual": os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Individual 2026 - EPEC-AR.pdf"),
}

with open(os.path.join(BASE_DIR, "data", "processed", "benchmark_dump.txt"), "w", encoding="utf-8") as out:
    for name, path in reports.items():
        if os.path.exists(path):
            out.write(f"\n=======================================================\n")
            out.write(f"REPORT: {name} ({os.path.basename(path)})\n")
            out.write(f"=======================================================\n")
            pages = extract_all_text(path)
            for num, text in pages:
                # Check for benchmarks, 500, ranking, ISCAL
                if any(w in text.lower() for w in ["500", "porte", "ranking", "promedio", "posici", "cuadro", "tabla", "comparativ"]):
                    out.write(f"\n--- [Page {num}] ---\n")
                    out.write(text.strip() + "\n")

print("Benchmark dump completed!")
