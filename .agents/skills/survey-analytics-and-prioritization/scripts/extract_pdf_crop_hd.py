#!/usr/bin/env python3
"""
Script utilitario para extraer recortes gráficos en alta definición de páginas PDF usando PyMuPDF (fitz).
Permite capturar matrices de prioridad, tablas oficiales y gráficos con resolución optimizada para dashboards web.
"""

import sys
import argparse
import fitz  # PyMuPDF

def extract_crop(pdf_path, page_number, coords, output_path, zoom=2.5):
    """
    Extrae un recorte de la página PDF especificada.
    
    :param pdf_path: Ruta al archivo PDF.
    :param page_number: Número de página (1-indexed).
    :param coords: Tupla (x0, y0, x1, y1) en puntos de página PDF.
    :param output_path: Ruta de salida del archivo PNG.
    :param zoom: Factor de escala de resolución (2.5 = ~300 DPI).
    """
    try:
        doc = fitz.open(pdf_path)
        if page_number < 1 or page_number > len(doc):
            print(f"Error: La página {page_number} está fuera de rango (1-{len(doc)}).", file=sys.stderr)
            return False
            
        page = doc[page_number - 1]
        mat = fitz.Matrix(zoom, zoom)
        
        if coords:
            clip_rect = fitz.Rect(coords[0], coords[1], coords[2], coords[3])
        else:
            clip_rect = page.rect
            
        pix = page.get_pixmap(matrix=mat, clip=clip_rect, alpha=False)
        pix.save(output_path)
        print(f"[OK] Recorte HD guardado en: {output_path} ({pix.width}x{pix.height} px)")
        return True
    except Exception as e:
        print(f"Error extrayendo recorte: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Extraer recortes en HD desde archivos PDF.")
    parser.add_argument("pdf", help="Ruta al archivo PDF")
    parser.add_argument("page", type=int, help="Número de página (1-indexed)")
    parser.add_argument("output", help="Ruta de salida de la imagen PNG")
    parser.add_argument("--coords", nargs=4, type=float, metavar=('X0', 'Y0', 'X1', 'Y1'),
                        help="Coordenadas de recorte (x0, y0, x1, y1)")
    parser.add_argument("--zoom", type=float, default=2.5, help="Factor de ampliación (default: 2.5)")
    
    args = parser.parse_args()
    coords = tuple(args.coords) if args.coords else None
    
    success = extract_crop(args.pdf, args.page, coords, args.output, args.zoom)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
