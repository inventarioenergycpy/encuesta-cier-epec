import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year in [2025, 2026]:
    txt_path = os.path.join(BASE_DIR, "data", "processed", f"distrib_full_pages_{year}.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pages = content.split("================ PAGE ")
    print(f"\n================================================================================")
    print(f"SEARCHING PARTICIPANTS AND RANKINGS IN YEAR {year}")
    print(f"================================================================================")
    
    for p in pages[1:]:
        lines = p.split("\n")
        p_num = lines[0].replace(" ================", "").strip()
        p_text = "\n".join(lines[1:])
        
        if any(w in p_text.lower() for w in ["participantes", "empresas participantes", "distribuidoras participantes", "ranking", "tabla"]):
            print(f"\n--- [Year {year} - Page {p_num}] ---")
            for l in lines[1:30]:
                try:
                    safe = l.encode('ascii', errors='replace').decode('ascii')
                    if safe.strip():
                        print(f"  {safe.strip()}")
                except Exception:
                    pass
