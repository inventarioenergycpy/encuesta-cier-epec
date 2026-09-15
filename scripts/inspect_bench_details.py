import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

for fname in ["indiv_2025_p25_45.txt", "indiv_2026_p25_45.txt"]:
    fpath = os.path.join(BASE_DIR, "data", "processed", fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"\n=======================================================")
    print(f"FILE: {fname}")
    print(f"=======================================================")
    pages = text.split("==================== PAGE ")
    for p in pages[1:]:
        lines = p.split("\n")
        p_num = lines[0].replace(" ====================", "").strip()
        p_body = "\n".join(lines[1:])
        
        # Look for pages with benchmark values
        if any(w in p_body.lower() for w in ["iscal", "benchmark", "promedio", "suministro", "factura", "atención", "atencion", "imagen"]):
            print(f"\n--- PAGE {p_num} ---")
            for l in lines[1:25]:
                try:
                    safe = l.encode('ascii', errors='replace').decode('ascii')
                    if safe.strip():
                        print(f"  {safe.strip()}")
                except Exception:
                    pass
