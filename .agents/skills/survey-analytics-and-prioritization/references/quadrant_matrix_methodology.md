# Metodología de Matriz de Acciones de Mejora y Cuadrantes de Prioridad (CIER / IPA)

Esta guía documenta la construcción matemática y metodológica de la **Matriz de Importancia vs. Desempeño (IPA)** según los estándares de la Comisión de Integración Energética Regional (CIER).

---

## 1. Fundamentos del Análisis de Importancia vs. Desempeño (IPA)

La matriz cruza dos dimensiones analíticas clave para cada uno de los atributos de servicio evaluados:
1. **Importancia Relativa ($X$):** Ponderación derivada de coeficientes de regresión múltiple o análisis de correlación parcial con el Índice de Satisfacción General (ISG). En estudios con 30 atributos, el promedio teórico de importancia es:
   $$\bar{I} = \frac{100\%}{30} = 3.33\%$$
2. **Desempeño / Satisfacción ($Y$):** Nota media de satisfacción escalada a base 100 o media ponderada obtenida de la encuesta residencial. La media global del sistema (ej: $64.8\text{ pts}$) actúa como umbral divisorio horizontal.

---

## 2. Definición de los 4 Cuadrantes Estratégicos

```text
         Alto Desempeño (≥ 64.8 pts)
                     ▲
   CUADRANTE III     │     CUADRANTE II
Ventajas Secundarias │   Fortalezas Clave
   (Mantener Efic.)  │  (Palancas de Marca)
                     │
◄────────────────────┼────────────────────► Alta Importancia (≥ 3.33%)
   CUADRANTE IV      │     CUADRANTE I
  Baja Prioridad     │     Foco Urgente
   (Monitoreo)       │  (Prioridad Máxima)
                     │
                     ▼
         Bajo Desempeño (< 64.8 pts)
```

### Cuadrante I: Foco Urgente / Prioridad Máxima (Alta Importancia / Bajo Desempeño)
- **Diagnóstico:** Atributos con alta incidencia en la satisfacción general donde la empresa presenta calificaciones deficitarias.
- **Acción:** Asignación inmediata de CAPEX/OPEX, planes de choque operativos y reducción de tiempos de respuesta.

### Cuadrante II: Fortalezas Clave (Alta Importancia / Alto Desempeño)
- **Diagnóstico:** Pilares de valor fundamentales donde la empresa lidera y el cliente valora fuertemente.
- **Acción:** Preservar estándares de calidad, comunicación proactiva y blindaje operativo.

### Cuadrante III: Ventajas Secundarias (Baja Importancia / Alto Desempeño)
- **Diagnóstico:** Servicios complementarios bien calificados pero con bajo impacto marginal en la satisfacción global.
- **Acción:** Optimización de costos, digitalización y mantenimiento sin sobreinversión.

### Cuadrante IV: Baja Prioridad (Baja Importancia / Bajo Desempeño)
- **Diagnóstico:** Puntos débiles secundarios que no mueven significativamente el índice general.
- **Acción:** Monitoreo periódico y mejoras de bajo costo asociadas a rutinas estándar.

---

## 3. Cruce de Microdatos y Diagnóstico de Causa Raíz

Para cada atributo del ranking, calcular obligatoriamente:
- **Distribución de Notas:**
  - `% Negativas (1-4)`: Clientes insatisfechos o en fricción.
  - `% Neutras (5-7)`: Clientes pasivos o indiferentes.
  - `% Positivas (8-10)`: Promotores y clientes plenamente satisfechos.
  - `Nota Media / 10`: Esperanza matemática de la calificación.
- **Causa Raíz Operativa:** Vinculación directa con datos duros del servicio (frecuencia de cortes, canales telefónicos ocupados, claridad en cargos de facturas, fluctuaciones de tensión).
- **Acción Recomendada:** Plan táctico específico con responsables operacionales.
