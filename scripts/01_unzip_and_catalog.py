import os
import zipfile
import shutil
import json
import pandas as pd

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
SOURCE_PATHS = {
    "2025": r"\\srvfs01\ProyectoTelemedicion\38 - Informes Protelem\26-Encuesta-CIER\2025",
    "2026": r"\\srvfs01\ProyectoTelemedicion\38 - Informes Protelem\26-Encuesta-CIER\2026"
}

CATEGORIES = {
    "1_Metodologia_Instrumentos": ["carta", "cuestionario", "clientes"],
    "2_Operacion_Campo_Muestreo": ["cronograma", "catastro", "entrenamiento", "entrevistador", "piloto", "plano", "calculo", "sorteo"],
    "3_Diccionarios_Metadatos": ["dicion", "diccion"],
    "4_Microdatos_Frecuencias": ["banco de datos", "bd epec", "frec", "planilla", "indices", "ndices"],
    "5_Informes_Presentaciones": ["informe", "inf comp", "analis", "conglomerad", "presentacion"]
}

def clean_text(text):
    text = text.lower()
    for char in ['á', 'à', 'ä', 'â', 'ã', 'ª']: text = text.replace(char, 'a')
    for char in ['é', 'è', 'ë', 'ê']: text = text.replace(char, 'e')
    for char in ['í', 'ì', 'ï', 'î']: text = text.replace(char, 'i')
    for char in ['ó', 'ò', 'ö', 'ô', 'º']: text = text.replace(char, 'o')
    for char in ['ú', 'ù', 'ü', 'û']: text = text.replace(char, 'u')
    for char in ['ñ']: text = text.replace(char, 'n')
    for char in ['?', '', '\ufffd']: text = text.replace(char, '')
    return text

def classify_file(filename):
    fname_clean = clean_text(filename)
    for cat, keywords in CATEGORIES.items():
        if any(clean_text(kw) in fname_clean for kw in keywords):
            return cat
    return "6_Otros"

def clean_extracted_name(raw_name):
    try:
        decoded = raw_name.encode('cp437').decode('utf-8')
    except Exception:
        try:
            decoded = raw_name.encode('cp437').decode('latin1')
        except Exception:
            decoded = raw_name
    return decoded

def run():
    print("=== STEP 1: INITIALIZING DIRECTORIES & CATALOGING ===")
    os.makedirs(os.path.join(BASE_DIR, "data", "raw"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "data", "classified"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "docs"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "scripts"), exist_ok=True)

    catalog = []

    for year, src_dir in SOURCE_PATHS.items():
        print(f"\nProcessing Year {year} from {src_dir}...")
        raw_year_dir = os.path.join(BASE_DIR, "data", "raw", year)
        os.makedirs(raw_year_dir, exist_ok=True)

        for zip_file in sorted(os.listdir(src_dir)):
            if not zip_file.lower().endswith('.zip'):
                continue
            
            src_zip_path = os.path.join(src_dir, zip_file)

            with zipfile.ZipFile(src_zip_path, 'r') as z:
                for zinfo in z.infolist():
                    internal_name = clean_extracted_name(zinfo.filename)
                    category = classify_file(internal_name)
                    
                    # Target directories
                    cat_dir = os.path.join(BASE_DIR, "data", "classified", year, category)
                    os.makedirs(cat_dir, exist_ok=True)
                    
                    target_file_path = os.path.join(cat_dir, internal_name)
                    
                    # Extract file content safely
                    content = z.read(zinfo.filename)
                    with open(target_file_path, 'wb') as out_f:
                        out_f.write(content)

                    # Also copy to raw folder
                    raw_target_path = os.path.join(raw_year_dir, internal_name)
                    with open(raw_target_path, 'wb') as raw_f:
                        raw_f.write(content)

                    mod_date = f"{zinfo.date_time[0]}-{zinfo.date_time[1]:02d}-{zinfo.date_time[2]:02d}"
                    catalog.append({
                        "year": int(year),
                        "zip_source": zip_file,
                        "file_name": internal_name,
                        "file_extension": os.path.splitext(internal_name)[1].lower(),
                        "category": category,
                        "size_kb": round(zinfo.file_size / 1024.0, 2),
                        "modified_date": mod_date,
                        "local_path": target_file_path.replace(BASE_DIR + "\\", "")
                    })
                    print(f"  [+] Categorized: [{category}] {internal_name} ({zinfo.file_size/1024:.1f} KB)")

    # Save catalog as JSON, CSV and Markdown
    json_path = os.path.join(BASE_DIR, "data", "processed", "catalogo_archivos.json")
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(catalog, jf, indent=2, ensure_ascii=False)

    df_cat = pd.DataFrame(catalog)
    csv_path = os.path.join(BASE_DIR, "data", "processed", "catalogo_archivos.csv")
    df_cat.to_csv(csv_path, index=False, encoding='utf-8-sig')

    md_path = os.path.join(BASE_DIR, "docs", "catalogo_archivos.md")
    with open(md_path, 'w', encoding='utf-8') as mf:
        mf.write("# Catálogo Oficial de Archivos de la Encuesta CIER (2025 - 2026)\n\n")
        mf.write(f"Total de archivos procesados y clasificados: **{len(catalog)}**\n\n")
        mf.write("| Año | Categoría | Nombre del Archivo | Formato | Tamaño | Fecha Original | Archivo ZIP Origen |\n")
        mf.write("| :---: | :--- | :--- | :---: | :---: | :---: | :--- |\n")
        for item in catalog:
            mf.write(f"| {item['year']} | {item['category']} | `{item['file_name']}` | {item['file_extension'].upper()} | {item['size_kb']} KB | {item['modified_date']} | `{item['zip_source']}` |\n")

    print(f"\nCatalog saved successfully at:\n- {json_path}\n- {csv_path}\n- {md_path}")

if __name__ == "__main__":
    run()
