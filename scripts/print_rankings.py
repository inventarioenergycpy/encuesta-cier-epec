import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year, max_p in [(2025, 56), (2026, 61)]:
    txt_path = os.path.join(BASE_DIR, "data", "processed", f"distrib_full_pages_{year}.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
    pages = content.split("================ PAGE ")
    print(f"\n=========================================================================")
    print(f"PAGES 5, 6, 7 AND LAST PAGES FOR YEAR {year}")
    print(f"=========================================================================")
    for p in pages:
        if not p.strip(): continue
        lines = p.split("\n")
        p_num = int(lines[0].replace(" ================", "").strip())
        if p_num in [5, 6, 7, max_p-3, max_p-2, max_p-1, max_p]:
            print(f"\n--- [Page {p_num}] ---")
            for l in lines[1:]:
                safe = l.encode('ascii', errors='replace').decode('ascii').strip()
                if safe:
                    print(f"  {safe}")
