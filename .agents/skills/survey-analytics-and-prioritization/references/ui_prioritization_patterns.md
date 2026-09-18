# Patrones de Diseño e Interfaz para Priorización y Presentación de Datos

Esta guía detalla los principios de diseño de interfaz, ergonomía visual e interactividad reactiva para tableros ejecutivos y analíticos de encuestas.

---

## 1. Arquitectura de Navegación por Menú Lateral (Sidebar)

Para dashboards con más de 5 áreas temáticas:
- **Estructura:** Menú lateral fijo a la izquierda (`width: 260px - 280px`) con scroll independiente.
- **Categorización:** Agrupar secciones por áreas temáticas (Resumen Ejecutivo, Análisis Estratégico, Datos y Diccionarios, Documentación).
- **Indicadores y Badges:** Incorporar badges con conteos de elementos o estados (`30`, `HD`, `N=1.250`).
- **Encabezado Contextual (Topbar):** Incluir migas de pan (*breadcrumbs*) que reflejen la sección activa y chips con macro KPIs clave (`ISG`, `IAC`, `ISCAL`, `% Detractores`).

---

## 2. Paginación Cognitiva en Bloques de 10 Puestos

En tablas o listados densos de clasificación (ej. 30 atributos):
- **Problema:** Desplegar 30 tarjetas extensas en una sola vista genera sobrecarga cognitiva y pérdida de contexto.
- **Solución:** Implementar barra de paginación por bloques de 10 puestos:
  - `Puestos 1 - 10 (Prioridades 1° a 10°)`
  - `Puestos 11 - 20 (Prioridades 11° a 20°)`
  - `Puestos 21 - 30 (Prioridades 21° a 30°)`
  - `Ver Todos (30)`
- **Filtros Adicionales:** Permitir filtrado complementario por cuadrante (Foco Urgente, Fortalezas Clave, etc.) y búsqueda rápida por texto.

---

## 3. Interactividad Bidireccional Gráfico de Dispersión (Chart.js) ↔ Microdatos

Al construir gráficos de dispersión (Scatter Plots) interactivos:
1. **Evento de Clic en Puntos (`onClick`):**
   - Detectar elementos seleccionados mediante `chart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true)`.
   - Permitir selección individual o selección múltiple (acumulativa).
2. **Resaltado y Atenuación al 50%:**
   - **Punto(s) Seleccionado(s):** Color cian de alto contraste (`#06b6d4`), tamaño incrementado (radio $12 - 14\text{ px}$) y borde blanco grueso ($2.5 - 3\text{ px}$).
   - **Puntos No Seleccionados:** Aplicar atenuación calibrada al **50% de opacidad** (`rgba(..., 0.5)` o color base atenuado). Esto mantiene visible la distribución global sin competir visualmente con la selección.
3. **Banner de Selección Activa y Scroll:**
   - Mostrar un banner con chips de los atributos actualmente seleccionados y botón de reset (`✖ Restablecer vista`).
   - Desplazar la vista suavemente (*smooth scroll*) hacia el bloque de microdatos y resaltar las filas correspondientes en las tablas.

---

## 4. Estilos de Alerta y Contraste (Perfil del Detractor)

Para tarjetas de riesgo, clientes críticos o alertas SLA:
- **Evitar:** Gradientes rojos brillantes con efectos de brillo reflectante (*glossy glassmorphism* con reflejos blancos que impiden la lectura).
- **Usar:** Fondos sólidos oscuros mate (`#240e11` o `hsl(350, 45%, 10%)`), borde de acento en rojo vivo (`#ef4444` o `#dc2626`) y tipografía en blanco nítido (`#f8fafc`).

---

## 5. Modal de Inspección Visual HD

- Proveer soporte de visor en pantalla completa (`modal-overlay` con `backdrop-filter: blur(8px)`) para gráficos complejos o recortes oficiales.
- Botones de control: Zoom in, Zoom out, Ajustar a pantalla y Cerrar (`Escape` key o clic fuera del modal).
