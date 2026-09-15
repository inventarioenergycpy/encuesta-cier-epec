import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def analyze_report(txt_path, year):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print(f"\n==================================================")
    print(f"REPORT: {os.path.basename(txt_path)} (Year {year})")
    print(f"==================================================")
    
    pages = content.split("--- PAGE ")
    print(f"Total pages: {len(pages)-1}")
    
    # Check for keywords
    for p in pages:
        if not p.strip(): continue
        p_num = p.split(" ---")[0]
        p_text = p
        
        # Look for pages discussing 500.000, Porte, Ranking, ISCAL, ABRADEE, etc.
        if any(k in p_text.lower() for k in ["500.000", "500 000", "más de 500", "mas de 500", "porte", "tamaño", "grupo"]):
            print(f"\n>>> MATCH IN PAGE {p_num}:")
            lines = [l.strip() for l in p_text.split("\n") if l.strip()]
            for l in lines[:20]:
                print(f"   {l}")

if __name__ == "__main__":
    analyze_report(os.path.join(BASE_DIR, "data", "processed", "informe_distrib_2025.txt"), 2025)
    analyze_report(os.path.join(BASE_DIR, "data", "processed", "informe_distrib_2026.txt"), 2026)
