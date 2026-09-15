import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
pptx_txt = os.path.join(BASE_DIR, "data", "processed", "pptx_slides_2026.txt")

with open(pptx_txt, "r", encoding="utf-8") as f:
    text = f.read()

slides = text.split("--- SLIDE ")
print(f"Total slides: {len(slides)-1}")

# Search for slides containing company names and scores
for s in slides[1:]:
    s_num = s.split(" ---\n")[0]
    s_body = s
    
    if any(k in s_body.lower() for k in ["epec", "edenor", "codensa", "epm", "ande", "cre", "delapaz", "enel", "cnel", "eeq", "caess", "delsur"]):
        # Check if it has ISCAL or ranking
        if any(w in s_body.lower() for w in ["iscal", "se", "ic", "fe", "at", "im", "ranking", "77,", "78,", "65,", "63,"]):
            lines = [l.strip() for l in s_body.split("\n") if l.strip()]
            print(f"\n[SLIDE {s_num}]:")
            for l in lines[:15]:
                safe = l.encode('ascii', errors='replace').decode('ascii')
                print(f"   {safe}")
