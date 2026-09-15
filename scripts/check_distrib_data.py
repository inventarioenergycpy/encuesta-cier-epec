import pandas as pd
import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"

# Check Banco de Datos 2025
bd_2025_path = os.path.join(BASE_DIR, "data", "raw", "2025", "Banco de Datos.xlsx")
if os.path.exists(bd_2025_path):
    df_bd = pd.read_excel(bd_2025_path)
    print("=== BANCO DE DATOS 2025 ===")
    print("Shape:", df_bd.shape)
    if 'P002' in df_bd.columns:
        print("P002 (Distribuidora) values count:\n", df_bd['P002'].value_counts())
    if 'P001' in df_bd.columns:
        print("P001 (Pais) values count:\n", df_bd['P001'].value_counts())

# Check Planilla de Indices 2026
idx_2026_files = [f for f in os.listdir(os.path.join(BASE_DIR, "data", "raw", "2026")) if "planilla" in f.lower() and f.endswith(".xlsx")]
if idx_2026_files:
    idx_path = os.path.join(BASE_DIR, "data", "raw", "2026", idx_2026_files[0])
    xl = pd.ExcelFile(idx_path)
    print("\n=== PLANILLA DE INDICES 2026 SHEETS ===")
    print(xl.sheet_names)
