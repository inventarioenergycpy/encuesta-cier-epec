import os
import pandas as pd
import json
import openpyxl

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def get_dimension(var_name, description):
    var = var_name.upper()
    desc = str(description).lower()
    
    if any(k in var for k in ['ID', 'PESO', 'PONDER', 'DATA', 'HORA', 'ENTREV', 'P001', 'P002', 'P003', 'P004', 'P005']):
        return "1_Identificacion_y_Muestreo"
    elif any(k in desc for k in ['interrup', 'corte', 'suministro', 'continuid', 'calidad', 'voltaje', 'tension', 'tensión', 'quema', 'daño', 'artefacto', 'restablec', 'reposic']):
        return "2_Calidad_y_Continuidad_Suministro"
    elif any(k in desc for k in ['factura', 'cuenta', 'cobro', 'importe', 'medidor', 'lectura', 'pago', 'tarifa', 'precio', 'valor']):
        return "3_Facturacion_Medicion_y_Tarifa"
    elif any(k in desc for k in ['atencion', 'atención', 'reclamo', 'oficina', 'telefono', 'teléfono', 'call center', 'comercial', 'canal', 'web', 'app', 'whatsapp']):
        return "4_Atencion_al_Cliente_y_Canales"
    elif any(k in desc for k in ['inform', 'comunic', 'aviso', 'notific', 'campaña']):
        return "5_Informacion_y_Comunicacion"
    elif any(k in desc for k in ['imagen', 'confianza', 'sociedad', 'medio ambiente', 'sostenib', 'comunidad', 'responsab']):
        return "6_Imagen_y_Responsabilidad_Social"
    elif any(k in desc for k in ['edad', 'sexo', 'genero', 'género', 'educac', 'ingreso', 'personas', 'habitante', 'electrodom', 'vivienda', 'nivel']):
        return "7_Perfil_Sociodemografico"
    else:
        return "8_Otras_Preguntas_Generales"

def process_dictionaries():
    print("=== STEP 2: PROCESSING DATA DICTIONARIES ===")
    
    # 1. Load 2025 Dictionary
    dic_2025_files = [
        f for f in os.listdir(os.path.join(BASE_DIR, "data", "raw", "2025")) 
        if "dicion" in f.lower() or "diccion" in f.lower()
    ]
    if not dic_2025_files:
        raise FileNotFoundError("2025 dictionary not found")
    
    path_2025 = os.path.join(BASE_DIR, "data", "raw", "2025", dic_2025_files[0])
    print(f"Reading 2025 Dictionary from: {path_2025}")
    df_2025 = pd.read_excel(path_2025)
    
    # Standardize column names
    # 2025 columns: ['Variável', 'Descrição', 'Opções de resposta', 'Unnamed: 3']
    df_2025.columns = [str(c).strip() for c in df_2025.columns]
    var_col_25 = df_2025.columns[0]
    desc_col_25 = df_2025.columns[1]
    cod_col_25 = df_2025.columns[2] if len(df_2025.columns) > 2 else None
    val_col_25 = df_2025.columns[3] if len(df_2025.columns) > 3 else None
    
    dict_2025_vars = {}
    current_var = None
    current_desc = ""
    
    for idx, row in df_2025.iterrows():
        v = row[var_col_25]
        d = row[desc_col_25]
        c = row[cod_col_25] if cod_col_25 else None
        val = row[val_col_25] if val_col_25 else None
        
        if pd.notna(v) and str(v).strip() != "":
            current_var = str(v).strip()
            current_desc = str(d).strip() if pd.notna(d) else ""
            if current_var not in dict_2025_vars:
                dict_2025_vars[current_var] = {
                    "variable": current_var,
                    "description": current_desc,
                    "dimension": get_dimension(current_var, current_desc),
                    "options": {}
                }
        if current_var and pd.notna(c) and str(c).strip() != "-":
            c_str = str(c).strip()
            val_str = str(val).strip() if pd.notna(val) else ""
            dict_2025_vars[current_var]["options"][c_str] = val_str

    # 2. Load 2026 Dictionary
    dic_2026_files = [
        f for f in os.listdir(os.path.join(BASE_DIR, "data", "raw", "2026")) 
        if "dicion" in f.lower() or "diccion" in f.lower()
    ]
    if not dic_2026_files:
        raise FileNotFoundError("2026 dictionary not found")
    
    path_2026 = os.path.join(BASE_DIR, "data", "raw", "2026", dic_2026_files[0])
    print(f"Reading 2026 Dictionary from: {path_2026}")
    df_2026 = pd.read_excel(path_2026)
    
    # 2026 columns: ['Nº de la pregunta', 'Variable', 'Título', 'Código', 'Descripción']
    df_2026.columns = [str(c).strip() for c in df_2026.columns]
    var_col_26 = [c for c in df_2026.columns if 'variable' in c.lower()][0]
    title_col_26 = [c for c in df_2026.columns if 'título' in c.lower() or 'titulo' in c.lower()][0]
    code_col_26 = [c for c in df_2026.columns if 'código' in c.lower() or 'codigo' in c.lower()][0]
    desc_col_26 = [c for c in df_2026.columns if 'descripción' in c.lower() or 'descripcion' in c.lower()][0]
    
    dict_2026_vars = {}
    for idx, row in df_2026.iterrows():
        v = row[var_col_26]
        t = row[title_col_26]
        c = row[code_col_26]
        d = row[desc_col_26]
        
        if pd.notna(v) and str(v).strip() != "":
            v_str = str(v).strip()
            if v_str not in dict_2026_vars:
                dict_2026_vars[v_str] = {
                    "variable": v_str,
                    "description": str(t).strip() if pd.notna(t) else "",
                    "dimension": get_dimension(v_str, t),
                    "options": {}
                }
            if pd.notna(c) and pd.notna(d):
                c_str = str(int(c)) if isinstance(c, (int, float)) and not pd.isna(c) and c == int(c) else str(c).strip()
                dict_2026_vars[v_str]["options"][c_str] = str(d).strip()

    print(f"Total variables in 2025 Dictionary: {len(dict_2025_vars)}")
    print(f"Total variables in 2026 Dictionary: {len(dict_2026_vars)}")

    # 3. Build Unified Dictionary and Cross-Year Comparison
    all_vars = sorted(list(set(list(dict_2025_vars.keys()) + list(dict_2026_vars.keys()))))
    unified_records = []
    
    for v in all_vars:
        in_2025 = v in dict_2025_vars
        in_2026 = v in dict_2026_vars
        
        status = "Presente en ambos años" if (in_2025 and in_2026) else ("Solo 2025" if in_2025 else "Solo 2026 (Nueva)")
        
        desc_25 = dict_2025_vars[v]["description"] if in_2025 else ""
        desc_26 = dict_2026_vars[v]["description"] if in_2026 else ""
        best_desc = desc_26 if desc_26 else desc_25
        dim = get_dimension(v, best_desc)
        
        opts_25 = dict_2025_vars[v]["options"] if in_2025 else {}
        opts_26 = dict_2026_vars[v]["options"] if in_2026 else {}
        
        unified_records.append({
            "Variable": v,
            "Dimension_Tematica": dim,
            "Descripcion_2025": desc_25,
            "Descripcion_2026": desc_26,
            "Descripcion_Consolidada": best_desc,
            "Estado_Comparativo": status,
            "En_2025": in_2025,
            "En_2026": in_2026,
            "Opciones_2025": json.dumps(opts_25, ensure_ascii=False),
            "Opciones_2026": json.dumps(opts_26, ensure_ascii=False)
        })

    df_unified = pd.DataFrame(unified_records)
    
    # Save processed dictionary files
    out_json = os.path.join(BASE_DIR, "data", "processed", "diccionario_unificado.json")
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(unified_records, f, indent=2, ensure_ascii=False)
        
    out_xlsx = os.path.join(BASE_DIR, "data", "processed", "diccionario_unificado.xlsx")
    df_unified.to_excel(out_xlsx, index=False)
    
    # Save Markdown Reference Document
    out_md = os.path.join(BASE_DIR, "docs", "diccionario_variables.md")
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write("# Diccionario y Mapeo Maestro de Variables CIER (2025 - 2026)\n\n")
        f.write(f"- Total de variables únicas mapeadas: **{len(all_vars)}**\n")
        f.write(f"- Variables presentes en ambos años: **{sum(1 for r in unified_records if r['En_2025'] and r['En_2026'])}**\n")
        f.write(f"- Variables exclusivas de 2025: **{sum(1 for r in unified_records if r['En_2025'] and not r['En_2026'])}**\n")
        f.write(f"- Variables nuevas incorporadas en 2026: **{sum(1 for r in unified_records if not r['En_2025'] and r['En_2026'])}**\n\n")
        
        # Summary by Dimension
        f.write("## Distribución por Dimensión Temática\n\n")
        f.write("| Dimensión Temática | Cantidad de Variables |\n")
        f.write("| :--- | :---: |\n")
        for dim, count in df_unified['Dimension_Tematica'].value_counts().items():
            f.write(f"| {dim} | {count} |\n")
        f.write("\n---\n\n## Detalle de Variables\n\n")
        f.write("| Variable | Dimensión | Descripción / Título | Estado Interanual |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for r in unified_records:
            f.write(f"| `{r['Variable']}` | {r['Dimension_Tematica']} | {r['Descripcion_Consolidada']} | {r['Estado_Comparativo']} |\n")

    print(f"\nDictionary outputs created:\n- {out_json}\n- {out_xlsx}\n- {out_md}")

if __name__ == "__main__":
    process_dictionaries()
