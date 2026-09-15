import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def analyze_and_dump():
    for year in [2025, 2026]:
        txt_path = os.path.join(BASE_DIR, "data", "processed", f"informe_distrib_{year}.txt")
        out_summary = os.path.join(BASE_DIR, "data", "processed", f"distrib_analysis_{year}.txt")
        
        with open(txt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pages = content.split("--- PAGE ")
        
        with open(out_summary, 'w', encoding='utf-8') as out:
            out.write(f"===========================================================\n")
            out.write(f"DISTRIBUTOR REPORT ANALYSIS - YEAR {year}\n")
            out.write(f"===========================================================\n\n")
            
            for p in pages:
                if not p.strip(): continue
                lines = p.split("\n")
                p_num = lines[0].replace(" ---", "").strip()
                p_text = "\n".join(lines[1:])
                
                # Check for keywords
                kws = ["500", "porte", "ranking", "iscal", "epec", "grupo", "participantes", "empresas", "tabla", "comparativo"]
                if any(kw in p_text.lower() for kw in kws):
                    out.write(f"\n------------------ PAGE {p_num} ------------------\n")
                    out.write(p_text.strip() + "\n")
                    
    print("Analysis dumped successfully!")

if __name__ == "__main__":
    analyze_and_dump()
