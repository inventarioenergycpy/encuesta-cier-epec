import subprocess
import sys
import os

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
SCRIPTS = [
    "01_unzip_and_catalog.py",
    "02_build_dictionary.py",
    "03_process_microdata.py",
    "04_generate_summary.py"
]

def main():
    print("================================================================================")
    print("      PIPELINE DE PROCESAMIENTO - ENCUESTA CIER EPEC (2025 - 2026)             ")
    print("================================================================================\n")
    
    for s in SCRIPTS:
        script_path = os.path.join(BASE_DIR, "scripts", s)
        print(f"\n>>> Running: {s} ...")
        # Run script with PYTHONIOENCODING set to utf-8
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        res = subprocess.run([sys.executable, script_path], cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
        
        # Print output safely
        safe_stdout = res.stdout.encode('ascii', errors='replace').decode('ascii')
        print(safe_stdout)
        if res.stderr:
            safe_stderr = res.stderr.encode('ascii', errors='replace').decode('ascii')
            print("STDERR:", safe_stderr)
        if res.returncode != 0:
            print(f"FAILED with return code {res.returncode}")
            sys.exit(res.returncode)
            
    print("\n================================================================================")
    print("                 PIPELINE COMPLETADO EXITOSAMENTE                               ")
    print("================================================================================")

if __name__ == "__main__":
    main()
