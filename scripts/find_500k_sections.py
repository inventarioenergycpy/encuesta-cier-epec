import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
dump_path = os.path.join(BASE_DIR, "data", "processed", "benchmark_dump.txt")

with open(dump_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for mentions of 500.000, >500 mil, etc.
sections = text.split("=======================================================")
for s in sections:
    if not s.strip(): continue
    lines = s.strip().split("\n")
    report_title = lines[0] if lines else "Unknown"
    
    # Find pages in this report
    pages = s.split("--- [Page ")
    for p in pages[1:]:
        p_num = p.split("] ---")[0]
        p_text = p
        if "500" in p_text or "> 500" in p_text or "más de 500" in p_text.lower():
            p_lines = [l.strip() for l in p_text.split("\n") if l.strip()]
            print(f"\n[{report_title}] Page {p_num}:")
            for l in p_lines[:15]:
                try:
                    safe_l = l.encode('ascii', errors='replace').decode('ascii')
                    print(f"   {safe_l}")
                except Exception:
                    pass
