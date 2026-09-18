# Reglas de Análisis de Encuestas, Matrices de Prioridad y Presentación de Datos

Al trabajar en proyectos de análisis de encuestas de satisfacción, estudios de clientes (CIER, CSAT, NPS) o tableros de control analíticos:

## 1. Detección y Fidelidad de Datos (SSOT)
- **Reconciliación Cruzada:** Auditar siempre las métricas de informes ejecutivos (PDF/PPTX) contra los microdatos primarios ($N$). En caso de discrepancias por omisión de NS/NC, documentar explícitamente la base de cálculo ($N$ total vs. $n_{efectivo}$).
- **Captura Gráfica HD:** Para matrices complejas o gráficos oficiales, utilizar recortes de alta definición con PyMuPDF (`fitz`) a $\ge 300\text{ DPI}$ en lugar de reproducciones aproximadas sin respaldo.

## 2. Metodología de Matrices de Prioridad
- **Cuadrantes Estratégicos:** En análisis de Importancia vs. Desempeño (IPA / CIER), calcular la media teórica de importancia ($100\% / K$) y el corte de satisfacción global para clasificar rigurosamente en:
  1. *Foco Urgente / Prioridad Máxima* (Alta Importancia / Bajo Desempeño)
  2. *Fortalezas Clave* (Alta Importancia / Alto Desempeño)
  3. *Ventajas Secundarias* (Baja Importancia / Alto Desempeño)
  4. *Baja Prioridad / Monitoreo* (Baja Importancia / Bajo Desempeño)
- **Desglose de Microdatos:** Proporcionar siempre para cada atributo evaluado: % Negativas (1-4), % Neutras (5-7), % Positivas (8-10), Nota Media / 10 y diagnóstico de causas raíz operativas.

## 3. Ergonomía Visual y Priorización de Interfaz
- **Paginación Cognitiva:** Segmentar listados extensos en bloques de 10 puestos (`Puestos 1-10`, `11-20`, `21-30`, `Ver Todos`) para prevenir sobrecarga cognitiva.
- **Interactividad Bidireccional:** Vincular gráficos de dispersión (Scatter Plots) con las tarjetas y tablas de microdatos con selección interactiva.
- **Atenuación al 50%:** Resaltar elementos seleccionados en color de contraste (cian brillante) y aplicar un 50% de atenuación/opacidad a los elementos no seleccionados para mantener el contexto global sin saturación visual.
- **Contraste en Tarjetas Críticas:** En tarjetas de riesgo o perfiles de clientes detractores, emplear fondos oscuros mate sólidos (ej. `#240e11` con borde `#ef4444`) sin reflejos brillantes (*non-glare*).
- **Modales de Auditoría HD:** Incorporar visores a pantalla completa con soporte de zoom para permitir la verificación visual directa de las fuentes originales.
