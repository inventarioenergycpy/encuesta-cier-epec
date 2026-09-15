import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year in [2025, 2026]:
    txt_path = os.path.join(BASE_DIR, "data", "processed", f"pptx_slides_{year}.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    slides = content.split("--- SLIDE ")
    print(f"\n=======================================================")
    print(f"SEARCHING PPTX SLIDES FOR YEAR {year} ({len(slides)-1} total slides)")
    print(f"=======================================================")
    
    matches = []
    for s in slides[1:]:
        s_num = s.split(" ---\n")[0]
        s_text = s
        
        # Check for benchmark, 500k, or ranking slides
        if any(w in s_text.lower() for w in ["más de 500", "mas de 500", "> 500", "500 mil", "benchmark", "ranking", "posici"]):
            if "iscal" in s_text.lower() or "suministro" in s_text.lower() or "factura" in s_text.lower() or "atenci" in s_text.lower() or "imagen" in s_text.lower() or "general" in s_text.lower():
                matches.append((s_num, s_text))
                
    print(f"Found {len(matches)} matching slides for year {year}")
    for s_num, s_text in matches[:10]:
        lines = [l.strip() for l in s_text.split("\n") if l.strip()]
        print(f"\n[Slide {s_num}]:")
        for l in lines[:10]:
            safe = l.encode('ascii', errors='replace').decode('ascii')
            print(f"   {safe}")
