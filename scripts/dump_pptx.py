import zipfile
import xml.etree.ElementTree as ET
import os

BASE_DIR = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\encuesta_cier"
pptx_path = os.path.join(BASE_DIR, "data", "raw", "2026", "Presentacion analitica 2026_v12.09.pptx")

def extract_pptx_slides(pptx_file):
    print("Opening PPTX:", pptx_file)
    with zipfile.ZipFile(pptx_file, 'r') as z:
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        # Sort slides by number
        slide_files.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
        print(f"Total slides found: {len(slide_files)}")
        
        out_txt = os.path.join(BASE_DIR, "data", "processed", "pptx_slides_2026.txt")
        with open(out_txt, 'w', encoding='utf-8') as out:
            for sname in slide_files:
                s_num = sname.replace('ppt/slides/slide', '').replace('.xml', '')
                xml_content = z.read(sname)
                tree = ET.fromstring(xml_content)
                texts = []
                for elem in tree.iter():
                    if elem.tag.endswith('}t') and elem.text:
                        texts.append(elem.text)
                slide_text = " ".join(texts)
                out.write(f"\n--- SLIDE {s_num} ---\n{slide_text}\n")
        print("PPTX text dump saved to", out_txt)

if os.path.exists(pptx_path):
    extract_pptx_slides(pptx_path)
