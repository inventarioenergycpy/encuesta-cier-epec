# Encuesta de Satisfacción CIER EPEC-AR (2025 - 2026)
### Estudio Comparativo Regional de Satisfacción de Clientes Residenciales y Benchmarking de Distribución Eléctrica

[![GitHub Pages](https://img.shields.io/badge/Live_Dashboard-GitHub_Pages-2ea44f?style=for-the-badge&logo=github)](https://inventarioenergycpy.github.io/encuesta-cier-epec/)
[![EPEC](https://img.shields.io/badge/Distribuidora-EPEC_C%C3%B3rdoba-005691?style=for-the-badge)](https://www.epec.com.ar)
[![CIER](https://img.shields.io/badge/Organismo-CIER_Regional-f39c12?style=for-the-badge)](https://www.cier.org)
[![Muestra](https://img.shields.io/badge/Muestra_Auditada-N%3D1.250-blue?style=for-the-badge)]()
[![SSOT](https://img.shields.io/badge/SSOT-100%25_Auditado-success?style=for-the-badge)]()

---

## 📌 Resumen Ejecutivo y Alcance

Este repositorio alberga el ecosistema completo de **análisis cuantitativo, microdatos auditados ($N=1.250$), modelos analíticos, documentación técnica (SSOT) y tablero interactivo de control de gestión** correspondiente a la **Encuesta de Satisfacción de Clientes Residenciales CIER** para la **Empresa Provincial de Energía de Córdoba (EPEC)**.

### Indicadores Clave Consolidados (2025 vs 2026):

* **Índice de Satisfacción General (ISG):** **`65.60 pts`** (+4.48 pts vs. 61.12 en 2025).
* **Índice de Aprobación del Cliente (IAC):** **`77.60 pts`** (+1.92 pts vs. 75.68 en 2025).
* **Calidad Percibida (ISCAL):** **`65.96 pts`** (+2.27 pts vs. 63.69 en 2025).
* **Índice de Excelencia (IECP - Promotores):** **`27.15%`** (+5.54% vs 2025).
* **Índice de Insatisfacción (IICP - Detractores):** **`15.19%`** (-2.47% vs 2025).

---

## 🚀 Arquitectura y Módulos del Tablero Local (`index.html`)

El tablero interactivo cuenta con una navegación moderna mediante un **Menú Lateral Izquierdo (Sidebar)** fijo con 8 paneles temáticos independientes:

1. **📊 Resumen Ejecutivo (`tab-overview`):** KPIs macro, radar comparativo multivariable CIER (4 series), ponderaciones de calidad del servicio y tarjetas de fortalezas/desafíos.
2. **📋 Resultados & Territorial (`tab-results`):** Desglose territorial completo (Total EPEC vs Córdoba Capital vs Interior vs Brecha territorial) y matriz de 66 indicadores canónicos con filtros por dimensión.
3. **🏢 Benchmark >500k & Países (`tab-benchmark`):** Posicionamiento competitivo frente a 13 grandes distribuidoras de América Latina y comparativa internacional por países miembros de CIER.
4. **🚩 Matriz de Mejora - Sección 16 (`tab-matriz`):**
   * **Recorte Oficial HD del Informe CIER (Pág. 94):** Imagen de alta resolución ($2428 \times 1512\text{ px}$) con visor modal de pantalla completa y zoom.
   * **Dispersión Interactiva (Chart.js):** Gráfico con coordenadas de Importancia vs Desempeño y **selección bidireccional de puntos** (atenuación al 50%).
   * **Cruce de Microdatos Paginado (10 puestos por vez):** Tarjetas con la pregunta de encuesta, barras de calificaciones (Negativo 1-4, Neutro 5-7, Positivo 8-10), nota media, causa raíz y acción recomendada.
   * **Tabla de Ranking de Prioridades (1ª a 30ª):** Buscador instantáneo y sincronización con el gráfico de dispersión.
5. **👥 Perfil del Detractor (`tab-detractores`):** Radiografía sociodemográfica (Edad 47.8 años, Ingresos $1.338.726, Educación 77.2%, Ubicación), 4 causas raíz de detracción y modelo de segmentación por tolerancia a cortes.
6. **📚 Diccionario de Datos (`tab-dictionary`):** Glosario de 66+ variables CIER, formulaciones de cálculo y escalas.
7. **🖼️ Guía de Gráficos (`tab-charts-guide`):** Catálogo de gráficos oficiales con recortes originales de informes PDF/PPT.
8. **🗄️ Catálogo & Respaldo SSOT (`tab-files`):** Checklist de auditoría de la Fuente Única de Verdad e inventario de archivos.

---

## 📁 Estructura del Repositorio

```
encuesta-cier-epec/
├── index.html                   # Tablero interactivo principal (HTML5 semántico)
├── style.css                    # Hoja de estilos con tema oscuro premium y diseño responsive
├── app.js                       # Controlador JavaScript modular (Chart.js, filtros, modales)
├── data_bundle.js               # Bundle de datos estructurados JSON inyectado en el cliente
├── README.md                    # Documentación principal del repositorio
├── assets/
│   └── img/
│       └── crops/               # Recortes oficiales HD de gráficos del informe CIER (Pág. 94, tablas)
├── docs/                        # Fuente Única de Verdad (SSOT) en Markdown
│   ├── matriz_acciones_mejora_prioridades.md
│   ├── resumen_cambios_y_actualizaciones_v2.md
│   ├── resumen_ejecutivo_indices.md
│   ├── comparativo_distribuidores_500k.md
│   ├── comparativo_regional_epec.md
│   ├── comparativo_paises_cier.md
│   ├── analisis_conglomerados_segmentos.md
│   ├── diccionario_variables.md
│   └── catalogo_archivos.md
├── data/
│   ├── processed/               # Datasets limpios (CSV y XLSX)
│   └── classified/              # Informes PDF, PPTX y bases de microdatos clasificadas
└── scripts/                     # Scripts de automatización, validación y testing
```

---

## 🛠️ Cómo Ejecutar y Editar el Proyecto

1. **Ejecución Local Inmediata:**
   * No requiere servidores ni dependencias pesadas: simplemente abra `index.html` en su navegador preferido (Edge, Chrome, Firefox).
2. **Sincronización y Actualizaciones:**
   * Las modificaciones en datos se reflejan editando `data_bundle.js` o ejecutando los scripts en `scripts/`.
   * La documentación SSOT en `docs/` se mantiene sincronizada con los microdatos auditados.

---

*© 2026 EPEC · Estudio Regional CIER de Satisfacción Residencial.*
