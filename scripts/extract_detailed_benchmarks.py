import os
import pypdf
import json

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def extract_detailed_benchmarks(pdf_path, year):
    reader = pypdf.PdfReader(pdf_path)
    print(f"\n================ EXTRACTING BENCHMARKS FROM {os.path.basename(pdf_path)} ({year}) ================")
    
    results = []
    # Pages 30 to 80 contain all the area benchmarks
    for page_idx in range(28, min(85, len(reader.pages))):
        text = reader.pages[page_idx].extract_text() or ""
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        
        # Check if page has benchmark comparisons
        if any(w in text.lower() for w in ["resultado cier", "benchmark", "distribuidora", "promedio", "idar", "idat", "iscal"]):
            header = lines[0] if lines else ""
            area_matches = [l for l in lines if any(k in l.upper() for k in ["SUMINISTRO", "FACTURA", "ATENCI", "IMAGEN", "INFORMACI", "RESPONSABILIDAD", "ALUMBRADO", "ISCAL", "IAC", "IIS", "ISG"])]
            
            results.append({
                "page": page_idx + 1,
                "header": header,
                "area_matches": area_matches[:3],
                "lines": lines
            })
            
    print(f"Extracted {len(results)} benchmark pages for {year}")
    return results

res26 = extract_detailed_benchmarks(os.path.join(BASE_DIR, "data", "raw", "2026", "Informe Individual 2026 - EPEC-AR.pdf"), 2026)
res25 = extract_detailed_benchmarks(os.path.join(BASE_DIR, "data", "raw", "2025", "Informe Individual 2025 - EPEC-AR.pdf"), 2025)

out_json = os.path.join(BASE_DIR, "data", "processed", "benchmarks_individual_extracted.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump({"2026": res26, "2025": res25}, f, indent=2, ensure_ascii=False)
print("Saved to", out_json)
