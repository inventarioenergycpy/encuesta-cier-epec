import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
rondas_path = os.path.join(BASE_DIR, "data", "processed", "rondas_2026_p1_30.txt")

with open(rondas_path, "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("==================== PAGE ")
for p in pages[1:]:
    lines = p.split("\n")
    p_num = lines[0].replace(" ====================", "").strip()
    print(f"\n--- RONDAS PAGE {p_num} ---")
    for l in lines[1:20]:
        try:
            safe = l.encode('ascii', errors='replace').decode('ascii')
            if safe.strip():
                print(f"  {safe.strip()}")
        except Exception:
            pass
