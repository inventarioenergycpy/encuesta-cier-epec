import os
import re

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def extract_benchmarks_from_distrib_pages():
    for year in [2025, 2026]:
        txt_path = os.path.join(BASE_DIR, "data", "processed", f"distrib_full_pages_{year}.txt")
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pages = content.split("================ PAGE ")
        print(f"\n=======================================================")
        print(f"EXTRACTING BENCHMARKS FROM YEAR {year}")
        print(f"=======================================================")
        
        extracted_indicators = []
        for p in pages[1:]:
            lines = [l.strip() for l in p.split("\n") if l.strip()]
            p_num = lines[0].replace(" ================", "").strip()
            
            # Find title / area / indicator name
            header_lines = lines[1:6]
            # Check numbers / distribution
            text_block = "\n".join(lines)
            
            # Find numbers with decimals like 78.5, 83.2, 65.4 etc.
            numbers = re.findall(r"\b\d{1,2}[\.,]\d{1,2}\b", text_block)
            
            print(f"[P.{p_num}] Header: {' | '.join(header_lines[:3])}")
            if numbers:
                print(f"      Numbers found: {numbers[:10]}")

extract_benchmarks_from_distrib_pages()
