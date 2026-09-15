import os
import pandas as pd
import json

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

def process_microdata():
    print("=== STEP 3: PROCESSING MICRODATA DATASETS ===")
    
    # 1. Load 2025 EPEC dataset
    p2025 = os.path.join(BASE_DIR, "data", "raw", "2025", "[xlsx] BD EPEC-AR.xlsx")
    print(f"Loading 2025 EPEC Microdata: {p2025}")
    df_2025 = pd.read_excel(p2025)
    df_2025.columns = [str(c).strip().upper() for c in df_2025.columns]
    df_2025['ANIO_ENCUESTA'] = 2025
    df_2025['EMPRESA'] = "EPEC"
    df_2025['PAIS'] = "ARGENTINA"
    print(f"  2025 records: {len(df_2025)} rows, {len(df_2025.columns)} columns")

    # 2. Load 2026 EPEC dataset
    p2026 = os.path.join(BASE_DIR, "data", "raw", "2026", "[xlsx] BD EPEC-AR.xlsx")
    print(f"Loading 2026 EPEC Microdata: {p2026}")
    df_2026 = pd.read_excel(p2026)
    df_2026.columns = [str(c).strip().upper() for c in df_2026.columns]
    df_2026['ANIO_ENCUESTA'] = 2026
    df_2026['EMPRESA'] = "EPEC"
    df_2026['PAIS'] = "ARGENTINA"
    print(f"  2026 records: {len(df_2026)} rows, {len(df_2026.columns)} columns")

    # 3. Concatenate and align columns
    print("Merging 2025 and 2026 datasets...")
    common_cols = sorted(list(set(df_2025.columns).intersection(set(df_2026.columns))))
    all_cols = ['ANIO_ENCUESTA', 'EMPRESA', 'PAIS', 'ID'] + [c for c in sorted(list(set(df_2025.columns).union(set(df_2026.columns)))) if c not in ['ANIO_ENCUESTA', 'EMPRESA', 'PAIS', 'ID']]
    
    df_combined = pd.concat([df_2025, df_2026], ignore_index=True)
    # Reorder columns
    df_combined = df_combined[[c for c in all_cols if c in df_combined.columns]]

    print(f"Combined Dataset: {len(df_combined)} rows, {len(df_combined.columns)} total columns")
    print(f"Common variables across both years: {len(common_cols)}")

    # 4. Save outputs
    # Parquet
    out_parquet = os.path.join(BASE_DIR, "data", "processed", "microdata_epec_2025_2026.parquet")
    df_parquet = df_combined.copy()
    for col in df_parquet.columns:
        if df_parquet[col].dtype == 'object':
            df_parquet[col] = df_parquet[col].astype(str)
    try:
        df_parquet.to_parquet(out_parquet, index=False)
        print(f"Saved Parquet: {out_parquet}")
    except Exception as e:
        print(f"Note on parquet export: {e}")

    # CSV (Combined and by year)
    out_csv_all = os.path.join(BASE_DIR, "data", "processed", "microdata_epec_2025_2026.csv")
    df_combined.to_csv(out_csv_all, index=False, encoding='utf-8-sig')
    print(f"Saved CSV: {out_csv_all}")

    # Excel (Combined and separate sheets)
    out_xlsx = os.path.join(BASE_DIR, "data", "processed", "microdata_epec_2025_2026.xlsx")
    with pd.ExcelWriter(out_xlsx, engine='openpyxl') as writer:
        df_combined.to_excel(writer, sheet_name='EPEC_2025_2026', index=False)
        df_2025.to_excel(writer, sheet_name='EPEC_2025', index=False)
        df_2026.to_excel(writer, sheet_name='EPEC_2026', index=False)
    print(f"Saved Excel: {out_xlsx}")

    # SQLite Database (optional fallback)
    try:
        import sqlite3
        db_path = os.path.join(BASE_DIR, "data", "processed", "base_analitica.sqlite")
        conn = sqlite3.connect(db_path)
        df_sql = df_combined.copy()
        df_sql.columns = [c.replace(' ', '_').replace('-', '_').replace('.', '_') for c in df_sql.columns]
        df_sql.to_sql('microdatos_cier', conn, if_exists='replace', index=False)
        conn.close()
        print(f"Saved SQLite Database: {db_path}")
    except Exception as ex:
        print(f"SQLite export skipped ({ex}). Data is fully available in Parquet, Excel, and CSV.")

if __name__ == "__main__":
    process_microdata()
