import os
import pandas as pd

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def sanitize_str(val):
    if pd.isna(val) or val is None:
        return ""
    s = str(val).strip()
    return s.replace('🆕', '[NUEVO]')

def extract_general_indices():
    raw_files = os.listdir(os.path.join(BASE_DIR, "data", "raw", "2026"))
    idx_files = [os.path.join(BASE_DIR, "data", "raw", "2026", f) for f in raw_files if "planilla" in f.lower() and f.endswith(".xlsx")]
    if not idx_files:
        return pd.DataFrame()
        
    xl = pd.ExcelFile(idx_files[0])
    sheet_gen = [s for s in xl.sheet_names if s.strip().upper() == 'GENERAL'][0]
    df_gen = xl.parse(sheet_gen)
    
    records = []
    current_area = "Índices Globales"
    
    for r in range(6, len(df_gen)):
        row = df_gen.iloc[r].tolist()
        sigla = sanitize_str(row[1]) if len(row) > 1 else ""
        tipo = sanitize_str(row[2]) if len(row) > 2 else ""
        desc_res = sanitize_str(row[4]) if len(row) > 4 else ""
        desc_comp = sanitize_str(row[5]) if len(row) > 5 else ""
        val_2025 = row[6] if len(row) > 6 else None
        val_2026 = row[7] if len(row) > 7 else None
        diff = row[8] if len(row) > 8 else None
        iaop = row[9] if len(row) > 9 else None
        
        if r > 86:
            break
            
        if pd.notna(val_2025) and pd.notna(val_2026) and isinstance(val_2025, (int, float)) and isinstance(val_2026, (int, float)):
            # Skip header row if it contains year numbers 2025 and 2026
            if val_2025 == 2025 and val_2026 == 2026:
                continue
                
            if tipo == 'IDAR':
                current_area = desc_res if desc_res else desc_comp
                
            records.append({
                "Area_Dimension": current_area,
                "Sigla": sigla,
                "Tipo_Indice": tipo,
                "Atributo_Indicador": desc_res if desc_res else desc_comp,
                "Indice_2025": round(float(val_2025), 2),
                "Indice_2026": round(float(val_2026), 2),
                "Diferencia_Puntos": round(float(diff), 2) if isinstance(diff, (int, float)) else round(float(val_2026)-float(val_2025), 2),
                "Variacion_IAOP_Pct": f"{round(float(iaop)*100, 2)}%" if isinstance(iaop, (int, float)) else f"{round(((float(val_2026)-float(val_2025))/float(val_2025))*100, 2)}%"
            })
            
    return pd.DataFrame(records)

def extract_satisfaction_details():
    raw_files = os.listdir(os.path.join(BASE_DIR, "data", "raw", "2026"))
    idx_files = [os.path.join(BASE_DIR, "data", "raw", "2026", f) for f in raw_files if "planilla" in f.lower() and f.endswith(".xlsx")]
    if not idx_files:
        return pd.DataFrame()
        
    xl = pd.ExcelFile(idx_files[0])
    sheet_sat = [s for s in xl.sheet_names if 'satisfac' in s.lower()][0]
    df_sat = xl.parse(sheet_sat)
    
    records = []
    current_area = "Índices Globales"
    
    for r in range(6, len(df_sat)):
        row = df_sat.iloc[r].tolist()
        sigla = sanitize_str(row[1]) if len(row) > 1 else ""
        tipo = sanitize_str(row[2]) if len(row) > 2 else ""
        desc_res = sanitize_str(row[3]) if len(row) > 3 else ""
        desc_comp = sanitize_str(row[4]) if len(row) > 4 else ""
        avg_score = row[19] if len(row) > 19 else None
        index_val = row[20] if len(row) > 20 else None
        
        if r > 86:
            break
            
        if pd.notna(avg_score) and isinstance(avg_score, (int, float)):
            if tipo == 'IDAR':
                current_area = desc_res if desc_res else desc_comp
            records.append({
                "Area_Dimension": current_area,
                "Sigla": sigla,
                "Tipo_Indice": tipo,
                "Atributo_Evaluado": desc_res if desc_res else desc_comp,
                "Nota_Promedio_1_10": round(float(avg_score), 2),
                "Indice_Satisfaccion_100": round(float(index_val), 2) if isinstance(index_val, (int, float)) else None
            })
            
    return pd.DataFrame(records)

def run():
    print("=== STEP 4: GENERATING ANALYTICAL SUMMARIES ===")
    
    df_gen = extract_general_indices()
    df_sat = extract_satisfaction_details()
    
    print(f"Extracted {len(df_gen)} indicators for General Comparison (2025 vs 2026)")
    print(f"Extracted {len(df_sat)} indicators for Satisfaction Detail (2026)")

    # Save to Excel
    out_xlsx = os.path.join(BASE_DIR, "data", "processed", "resumen_indices_satisfaccion.xlsx")
    with pd.ExcelWriter(out_xlsx, engine='openpyxl') as writer:
        if not df_gen.empty:
            df_gen.to_excel(writer, sheet_name='Comparativo_2025_2026', index=False)
        if not df_sat.empty:
            df_sat.to_excel(writer, sheet_name='Satisfaccion_2026', index=False)
    print(f"Saved Indices Summary Excel: {out_xlsx}")
    
    # Save to CSV
    if not df_gen.empty:
        df_gen.to_csv(os.path.join(BASE_DIR, "data", "processed", "indices_comparativo_2025_2026.csv"), index=False, encoding='utf-8-sig')
    if not df_sat.empty:
        df_sat.to_csv(os.path.join(BASE_DIR, "data", "processed", "indices_satisfaccion_2026.csv"), index=False, encoding='utf-8-sig')

    # Generate Markdown Summary
    out_md = os.path.join(BASE_DIR, "docs", "resumen_ejecutivo_indices.md")
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write("# Resumen Ejecutivo de Índices de Satisfacción CIER (EPEC 2025 - 2026)\n\n")
        f.write("Este informe consolida las principales métricas e indicadores de satisfacción del consumidor residencial de EPEC obtenidos en el estudio comparativo CIER.\n\n")
        
        if not df_gen.empty:
            f.write("## 1. Comparativa General de Indicadores e Índices (2025 vs. 2026)\n\n")
            f.write("| Dimensión / Área | Sigla | Tipo | Indicador / Atributo | Índice 2025 | Índice 2026 | Dif. Puntos | Var. Relativa (IAOP) |\n")
            f.write("| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |\n")
            for idx, r in df_gen.iterrows():
                f.write(f"| {r['Area_Dimension']} | `{r['Sigla']}` | {r['Tipo_Indice']} | {r['Atributo_Indicador']} | **{r['Indice_2025']}** | **{r['Indice_2026']}** | {r['Diferencia_Puntos']:+0.2f} | {r['Variacion_IAOP_Pct']} |\n")
                
        if not df_sat.empty:
            f.write("\n---\n\n## 2. Detalle de Satisfacción y Notas Promedio por Atributo (2026)\n\n")
            f.write("| Dimensión / Área | Sigla | Tipo | Atributo Evaluado | Nota Promedio (1 a 10) | Índice de Satisfacción (0 a 100) |\n")
            f.write("| :--- | :---: | :---: | :--- | :---: | :---: |\n")
            for idx, r in df_sat.iterrows():
                f.write(f"| {r['Area_Dimension']} | `{r['Sigla']}` | {r['Tipo_Indice']} | {r['Atributo_Evaluado']} | **{r['Nota_Promedio_1_10']}** | **{r['Indice_Satisfaccion_100']}** |\n")

    print(f"Saved Markdown Summary: {out_md}")

if __name__ == "__main__":
    run()
