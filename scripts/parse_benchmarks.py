import json
import re
import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
json_path = os.path.join(BASE_DIR, "data", "processed", "benchmarks_individual_extracted.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for year in ["2025", "2026"]:
    print(f"\n==================================================================")
    print(f"BENCHMARK VALUES EXTRACTED FOR YEAR {year}")
    print(f"==================================================================")
    
    pages = data[year]
    for p in pages:
        p_num = p["page"]
        lines = p["lines"]
        
        # Check if page contains benchmark / cier / epec comparisons
        full_text = " ".join(lines)
        if "benchmark" in full_text.lower() or "resultado cier" in full_text.lower():
            # Find numbers with decimals
            print(f"\n[Page {p_num}] {lines[0] if lines else ''}")
            for l in lines[:20]:
                if any(k in l.lower() for k in ["epec", "cier", "benchmark", "idar", "idat", "iscal", "iac", "iis", "isg", "suministro", "factura", "atención", "imagen", "información"]):
                    safe = l.encode('ascii', errors='replace').decode('ascii')
                    print(f"   {safe}")
