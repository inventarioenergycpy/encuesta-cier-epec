import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for year, fname in [(2025, "paises_2025.txt"), (2026, "paises_2026.txt")]:
    txt_path = os.path.join(BASE_DIR, "data", "processed", fname)
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    pages = text.split("================ PAGE ")
    print(f"\n=======================================================")
    print(f"SEARCHING PAISES IN YEAR {year}")
    print(f"=======================================================")
    for p in pages[1:30]:
        lines = [l.strip() for l in p.split("\n") if l.strip()]
        p_num = lines[0].replace(" ================", "").strip()
        if any(w in p.lower() for w in ["argentina", "iscal", "iac", "ranking", "promedio", "brasil", "colombia", "paraguay", "bolivia", "peru", "ecuador", "costa rica", "el salvador", "uruguay"]):
            print(f"\n--- [Year {year} - Page {p_num}] ---")
            for l in lines[1:15]:
                safe = l.encode('ascii', errors='replace').decode('ascii')
                print(f"  {safe}")
