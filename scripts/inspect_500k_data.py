import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year in [2025, 2026]:
    txt_path = os.path.join(BASE_DIR, "data", "processed", f"distrib_analysis_{year}.txt")
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    print(f"\n====================== YEAR {year} SEARCH ======================")
    # Look for pages with company list, or tables of >500.000
    for match in re.finditer(r"------------------ PAGE (\d+) ------------------", text):
        page_num = match.group(1)
        start_idx = match.start()
        next_match = re.search(r"------------------ PAGE \d+ ------------------", text[start_idx+1:])
        end_idx = (start_idx + 1 + next_match.start()) if next_match else len(text)
        page_content = text[start_idx:end_idx]
        
        if "500" in page_content or "distribuidoras participantes" in page_content.lower() or "empresas participantes" in page_content.lower() or "iscal" in page_content.lower():
            # Check lines
            for line in page_content.split("\n")[:25]:
                if any(w in line.lower() for w in ["500", "epec", "iscal", "participante", "porte", "promedio", "ranking", "tabla"]):
                    print(f"[P.{page_num}] {line.strip()}")
