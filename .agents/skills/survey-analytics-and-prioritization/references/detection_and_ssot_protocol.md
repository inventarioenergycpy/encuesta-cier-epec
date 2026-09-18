# Protocolo de Detección de Fuentes, Extracción HD y Reconciliación SSOT

Este protocolo estandariza la ingesta y auditoría de datos provenientes de encuestas de satisfacción, informes ejecutivos en PDF/PPTX y bases de datos tabulares (Excel/CSV/SPSS).

---

## 1. Detección de Fuentes y Catálogo

Al iniciar el análisis de un estudio de satisfacción:
1. **Inventariar Activos Crudos (`data/raw/`):**
   - Catalogar informes en PDF (ejecutivos, regionales, por conglomerados, comparativos internacionales).
   - Localizar presentaciones ejecutivas (PPTX) y cuadernos de preguntas/cuestionarios.
   - Identificar bases de datos de microdatos (`BD.xlsx`, `.csv`, `.sav`) y diccionarios de variables.
2. **Construir Diccionario Unificado de Variables:**
   - Extraer código de variable (ej: `P13_1`, `P24_4`), tipo de escala (Likert 1-10, dicotómica 1/2, categórica), etiquetas literales de pregunta y rangos válidos.
   - Estandarizar mapeo interanual ($t$ vs. $t-1$).

---

## 2. Extracción de Recortes Gráficos en Alta Definición (PyMuPDF)

Para preservar la fidelidad gráfica de matrices complejas y gráficos vectoriales publicados en informes oficiales:
- Utilizar `PyMuPDF` (`fitz`) con matriz de escala $\ge 2.0x$ (equivalente a $300 - 450\text{ DPI}$).
- Calcular `Rect(x0, y0, x1, y1)` sobre la página en coordenadas de puntos.
- Guardar en formato PNG con compresión sin pérdidas.

```python
import fitz

def extract_crop_hd(pdf_path, page_num, rect_coords, output_path, zoom=2.5):
    doc = fitz.open(pdf_path)
    page = doc[page_num - 1]
    mat = fitz.Matrix(zoom, zoom)
    clip_rect = fitz.Rect(*rect_coords)
    pix = page.get_pixmap(matrix=mat, clip=clip_rect, alpha=False)
    pix.save(output_path)
    print(f"Recorte guardado exitosamente: {output_path} ({pix.width}x{pix.height}px)")
```

---

## 3. Protocolo de Reconciliación SSOT (Single Source of Truth)

Para evitar inconsistencias estadísticas:
1. **Auditoría Cruzada:**
   - Contrastar los totales agregados de los informes PDF (ej. nota media ponderada o índice general) contra el cálculo directo sobre los microdatos individuales ($N=1.250$).
2. **Tratamiento de No Sabe / No Contesta (NS/NC):**
   - Identificar códigos de omisión (ej: `99`, `999`, `null`, blancos) y documentar si las medias oficiales se calculan sobre la base total ($N$) o sobre la base efectiva que experimentó el servicio ($n_{efectivo}$).
3. **Validación de Frecuencias:**
   - Verificar que la suma de porcentajes segmentados (% Negativas 1-4 + % Neutras 5-7 + % Positivas 8-10) sume exactamente $100.0\%$.
