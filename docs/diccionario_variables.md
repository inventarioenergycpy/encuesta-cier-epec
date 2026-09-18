# 📚 Diccionario Unificado de Variables CIER (EPEC 2025 - 2026)

Este documento describe formalmente las variables, preguntas y escalas utilizadas en los relevamientos CIER para EPEC en las rondas 2025 y 2026.

## 1. Homogeneización de Variables Clave entre Rondas

| Variable Conceptual | Código 2025 | Código 2026 | Tipo de Variable | Rango / Valores | Descripción Técnica |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Edad del encuestado** | `P035` | `P036` | Numérica (años) | 18 a 74 años | Edad cronológica cumplida del titular o decisor del hogar |
| **Nivel Educativo / Escolaridad** | `P036` | `P037` | Categórica ordinal | 1 a 11 | 1: Prim. inc., 4: Sec. comp., 6: Téc. comp., 8: Univ. comp., 9: Posgrado |
| **Ingreso Familiar (Franjas)** | `P037` | `P038` | Categórica ordinal | 1 a 22 | Deciles y franjas socioeconómicas armonizadas |
| **Ingreso Familiar Numérico ($)** | `P237` | `P283` | Numérica continua | Monto en ARS | Ingreso monetario total mensual neto de todos los miembros del hogar |
| **Satisfacción General (ISG)** | `P164` | `P238` | Escala 1 a 10 | 1 a 10 (1-2 Muy insat, 9-10 Muy sat) | Evaluación global del servicio eléctrico recibido |
| **Net Promoter Score (NPS)** | `P165` | `P239` | Escala 0 a 10 | 0 a 10 (0-6 Detractor, 7-8 Neutro, 9-10 Promotor) | Probabilidad de recomendación de la empresa a familiares/amigos |
| **Precio de la Factura (Percepción)** | `P163` | `P234` | Escala 1 a 10 | 1 = Muy Barato a 10 = Muy Caro | Evaluación del nivel tarifario percibido |
| **Duración de Cortes de Energía** | `P030` | `P030` / `P252` | Numérica (minutos) | 0 a 999 min | Duración total acumulada en minutos sin servicio en últimos meses |
| **Municipio de Residencia** | `P005` | `P005` | Categórica nominal | Códigos 960001 a 960095 | Localidad geográfica de la provincia de Córdoba |
| **Zona / Regional Operativa** | `region` | `REGIONAL_ID` | Categórica nominal | 9601 (Capital) a 9605 (Sur) | Agrupamiento territorial de delegaciones de EPEC |

## 2. Catálogo de Preguntas y Opciones del Cuestionario CIER 2026

| Pregunta | Variable | Título / Dimensión | Código | Opción de Respuesta |
| :--- | :---: | :--- | :---: | :--- |
| P001 | `P001` | País | 1.0 | ARGENTINA (AR) |
| P001 | `P001` | País | 2.0 | BOLIVIA (BO) |
| P001 | `P001` | País | 6.0 | COSTA RICA (CR) |
| P001 | `P001` | País | 7.0 | REPÚBLICA DOMINICANA (DO) |
| P001 | `P001` | País | 8.0 | ECUADOR (EC) |
| P001 | `P001` | País | 9.0 | GUATEMALA (GT) |
| P001 | `P001` | País | 12.0 | PERÚ (PE) |
| P001 | `P001` | País | 13.0 | PARAGUAY (PY) |
| P001 | `P001` | País | 14.0 | EL SALVADOR (SV) |
| P001 | `P001` | País | 15.0 | URUGUAY (UY) |
| P002 | `P002` | Distribuidora | 1.0 | distribuidora |
| P003 | `P003` | Tipo de muestra | 1.0 | Muestra |
| P003 | `P003` | Tipo de muestra | 2.0 | Expansión |
| P004 | `P004` | Prepago | 1.0 | Sí |
| P004 | `P004` | Prepago | 2.0 | No |
| P005 | `P005` | Municipio | 1.0 | NOMBRE DEL MUNICIPIO |
| P017 | `P017` | Medio de recibimiento de la factura | 1.0 | Impresa en su casa |
| P017 | `P017` | Medio de recibimiento de la factura | 2.0 | Correo electrónico o en el sitio web |
| P017 | `P017` | Medio de recibimiento de la factura | 3.0 | Correo electrónico e impresa |
| P017 | `P017` | Medio de recibimiento de la factura | 4.0 | App de la distribuidora o página web |
| P017 | `P017` | Medio de recibimiento de la factura | 5.0 | No recibe la factura/ paga en un punto de pago |
| P017 | `P017` | Medio de recibimiento de la factura | 6.0 | No recibe factura/ cliente prepago |
| P017 | `P017` | Medio de recibimiento de la factura | 7.0 | NS/ NR |
| P018 | `P018` | Presentó la factura | 1.0 | Presentó |
| P018 | `P018` | Presentó la factura | 2.0 | No presentó |
| P023 | `P023` | Consumo (en kWh/ mes) | -77.0 | Dato no disponible en la factura |
| P025 | `P025` | Solicitud de informaciones de la factura | 1.0 | Sí |
| P025 | `P025` | Solicitud de informaciones de la factura | 2.0 | No |
| P028 | `P028` | Valor de la factura de energía | -99.0 | No respondió |
| P028 | `P028` | Valor de la factura de energía | -88.0 | No Sabe |
| P030 | `P030` | Consumo (en kWh/ mes) | -99.0 | No respondió |
| P030 | `P030` | Consumo (en kWh/ mes) | -88.0 | No Sabe |
| P032 | `P032` | Valor de la recarga en el último mes | -99.0 | No respondió |
| P032 | `P032` | Valor de la recarga en el último mes | -88.0 | No Sabe |
| P034 | `P034` | Consumo (en kWh/ mes) | -99.0 | No respondió |
| P034 | `P034` | Consumo (en kWh/ mes) | -88.0 | No Sabe |
| P036 | `P036` | Edad | -99.0 | No respondió |
| P037 | `P037` | Escolaridad | 1.0 | Primaria incompleta |
| P037 | `P037` | Escolaridad | 2.0 | Primaria completa |
| P037 | `P037` | Escolaridad | 3.0 | Secundaria incompleta |
| P037 | `P037` | Escolaridad | 4.0 | Secundaria completa |
| P037 | `P037` | Escolaridad | 5.0 | Técnico incompleto |
| P037 | `P037` | Escolaridad | 6.0 | Técnico completo |
| P037 | `P037` | Escolaridad | 7.0 | Universidad incompleta |
| P037 | `P037` | Escolaridad | 8.0 | Universidad completa |
| P037 | `P037` | Escolaridad | 9.0 | Posgrado |
| P037 | `P037` | Escolaridad | 10.0 | No Respondió |
| P037 | `P037` | Escolaridad | 11.0 | Analfabeto/ Ninguna escolaridad |
| P038 | `P038` | Rango del ingreso familiar | 1.0 | @FRANJA_INGRESO_1@ |
| P038 | `P038` | Rango del ingreso familiar | 2.0 | @FRANJA_INGRESO_2@ |
| P038 | `P038` | Rango del ingreso familiar | 3.0 | @FRANJA_INGRESO_3@ |
| P038 | `P038` | Rango del ingreso familiar | 4.0 | @FRANJA_INGRESO_4@ |
| P038 | `P038` | Rango del ingreso familiar | 5.0 | @FRANJA_INGRESO_5@ |
| P038 | `P038` | Rango del ingreso familiar | 6.0 | @FRANJA_INGRESO_6@ |
| P038 | `P038` | Rango del ingreso familiar | 7.0 | @FRANJA_INGRESO_7@ |
| P038 | `P038` | Rango del ingreso familiar | 8.0 | @FRANJA_INGRESO_8@ |
| P038 | `P038` | Rango del ingreso familiar | 9.0 | @FRANJA_INGRESO_9@ |
| P038 | `P038` | Rango del ingreso familiar | 10.0 | @FRANJA_INGRESO_10@ |
| P038 | `P038` | Rango del ingreso familiar | 11.0 | @FRANJA_INGRESO_11@ |
| P038 | `P038` | Rango del ingreso familiar | 12.0 | @FRANJA_INGRESO_12@ |
| P038 | `P038` | Rango del ingreso familiar | 13.0 | @FRANJA_INGRESO_13@ |
| P038 | `P038` | Rango del ingreso familiar | 14.0 | @FRANJA_INGRESO_14@ |
| P038 | `P038` | Rango del ingreso familiar | 15.0 | @FRANJA_INGRESO_15@ |
| P038 | `P038` | Rango del ingreso familiar | 16.0 | @FRANJA_INGRESO_16@ |
| P038 | `P038` | Rango del ingreso familiar | 17.0 | @FRANJA_INGRESO_17@ |
| P038 | `P038` | Rango del ingreso familiar | 18.0 | @FRANJA_INGRESO_18@ |
| P038 | `P038` | Rango del ingreso familiar | 19.0 | @FRANJA_INGRESO_19@ |
| P038 | `P038` | Rango del ingreso familiar | 20.0 | @FRANJA_INGRESO_20@ |
| P038 | `P038` | Rango del ingreso familiar | 21.0 | No sabe |
| P038 | `P038` | Rango del ingreso familiar | 22.0 | No Respondió |
| P039 | `P039` | Evaluación de la calidad de los servicios | 1.0 | Muy mala |
| P039 | `P039` | Evaluación de la calidad de los servicios | 2.0 | Muy mala |
| P039 | `P039` | Evaluación de la calidad de los servicios | 3.0 | Mala |
| P039 | `P039` | Evaluación de la calidad de los servicios | 4.0 | Mala |
| P039 | `P039` | Evaluación de la calidad de los servicios | 5.0 | Regular |
| P039 | `P039` | Evaluación de la calidad de los servicios | 6.0 | Regular |
| P039 | `P039` | Evaluación de la calidad de los servicios | 7.0 | Buena |
| P039 | `P039` | Evaluación de la calidad de los servicios | 8.0 | Buena |
| P039 | `P039` | Evaluación de la calidad de los servicios | 9.0 | Muy buena |
| P039 | `P039` | Evaluación de la calidad de los servicios | 10.0 | Muy buena |
| P039 | `P039` | Evaluación de la calidad de los servicios | 11.0 | NS |
| P039 | `P039` | Evaluación de la calidad de los servicios | 12.0 | NR |
| P048 | `P048` | Tipo de cuestionario | 1.0 | Importancia |
| P048 | `P048` | Tipo de cuestionario | 2.0 | Satisfacción |
| G050 | `P050` | 1º puesto | 1.0 | Sin interrupción |
| G050 | `P050` | 1º puesto | 2.0 | Sin variación de voltaje |
| G050 | `P050` | 1º puesto | 3.0 | Rapidez en la reanudación de la energía cuando falta |
| G050 | `P051` | 2º puesto | 1.0 | Sin interrupción |
| G050 | `P051` | 2º puesto | 2.0 | Sin variación de voltaje |
| G050 | `P051` | 2º puesto | 3.0 | Rapidez en la reanudación de la energía cuando falta |
| G050 | `P052` | 3º puesto | 1.0 | Sin interrupción |
| G050 | `P052` | 3º puesto | 2.0 | Sin variación de voltaje |
| G050 | `P052` | 3º puesto | 3.0 | Rapidez en la reanudación de la energía cuando falta |
| G053 | `P053` | Sin interrupción | 1.0 | Muy baja importancia |
| G053 | `P053` | Sin interrupción | 2.0 | Muy baja importancia |
| G053 | `P053` | Sin interrupción | 3.0 | Baja importancia |
| G053 | `P053` | Sin interrupción | 4.0 | Baja importancia |
| G053 | `P053` | Sin interrupción | 5.0 | Importancia Mediana |
| G053 | `P053` | Sin interrupción | 6.0 | Importancia Mediana |
| G053 | `P053` | Sin interrupción | 7.0 | Alta importancia |
| G053 | `P053` | Sin interrupción | 8.0 | Alta importancia |
| G053 | `P053` | Sin interrupción | 9.0 | Muy alta importancia |
| G053 | `P053` | Sin interrupción | 10.0 | Muy alta importancia |
| G053 | `P053` | Sin interrupción | 11.0 | NS |
| G053 | `P053` | Sin interrupción | 12.0 | NR |
| G053 | `P054` | Sin variación de voltaje | 1.0 | Muy baja importancia |
| G053 | `P054` | Sin variación de voltaje | 2.0 | Muy baja importancia |
| G053 | `P054` | Sin variación de voltaje | 3.0 | Baja importancia |
| G053 | `P054` | Sin variación de voltaje | 4.0 | Baja importancia |
| G053 | `P054` | Sin variación de voltaje | 5.0 | Importancia Mediana |
| G053 | `P054` | Sin variación de voltaje | 6.0 | Importancia Mediana |
| G053 | `P054` | Sin variación de voltaje | 7.0 | Alta importancia |
| G053 | `P054` | Sin variación de voltaje | 8.0 | Alta importancia |
| G053 | `P054` | Sin variación de voltaje | 9.0 | Muy alta importancia |
| G053 | `P054` | Sin variación de voltaje | 10.0 | Muy alta importancia |
| G053 | `P054` | Sin variación de voltaje | 11.0 | NS |
| G053 | `P054` | Sin variación de voltaje | 12.0 | NR |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 1.0 | Muy baja importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 2.0 | Muy baja importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 3.0 | Baja importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 4.0 | Baja importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 5.0 | Importancia Mediana |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 6.0 | Importancia Mediana |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 7.0 | Alta importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 8.0 | Alta importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 9.0 | Muy alta importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 10.0 | Muy alta importancia |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 11.0 | NS |
| G053 | `P055` | Rapidez en la reanudación de la energía cuando falta | 12.0 | NR |
| G056 | `P056` | 1º puesto | 1.0 | Notificación de interrupción |
| G056 | `P056` | 1º puesto | 2.0 | Uso eficiente |
| G056 | `P056` | 1º puesto | 3.0 | Riesgos y peligros |
| G056 | `P056` | 1º puesto | 4.0 | Derechos y deberes |
| G056 | `P056` | 1º puesto | 5.0 | Medición del consumo de energía |
| G056 | `P057` | 2º puesto | 1.0 | Notificación de interrupción |
| G056 | `P057` | 2º puesto | 2.0 | Uso eficiente |
| G056 | `P057` | 2º puesto | 3.0 | Riesgos y peligros |
| G056 | `P057` | 2º puesto | 4.0 | Derechos y deberes |
| G056 | `P057` | 2º puesto | 5.0 | Medición del consumo de energía |
| G056 | `P058` | 3º puesto | 1.0 | Notificación de interrupción |
| G056 | `P058` | 3º puesto | 2.0 | Uso eficiente |
| G056 | `P058` | 3º puesto | 3.0 | Riesgos y peligros |
| G056 | `P058` | 3º puesto | 4.0 | Derechos y deberes |
| G056 | `P058` | 3º puesto | 5.0 | Medición del consumo de energía |
| G056 | `P059` | 4º puesto | 1.0 | Notificación de interrupción |
| G056 | `P059` | 4º puesto | 2.0 | Uso eficiente |
| G056 | `P059` | 4º puesto | 3.0 | Riesgos y peligros |
| G056 | `P059` | 4º puesto | 4.0 | Derechos y deberes |
| G056 | `P059` | 4º puesto | 5.0 | Medición del consumo de energía |
| G056 | `P060` | 5º puesto | 1.0 | Notificación de interrupción |
| G056 | `P060` | 5º puesto | 2.0 | Uso eficiente |
| G056 | `P060` | 5º puesto | 3.0 | Riesgos y peligros |
| G056 | `P060` | 5º puesto | 4.0 | Derechos y deberes |
| G056 | `P060` | 5º puesto | 5.0 | Medición del consumo de energía |
| G061 | `P061` | Notificación de interrupción | 1.0 | Muy baja importancia |
| G061 | `P061` | Notificación de interrupción | 2.0 | Muy baja importancia |
| G061 | `P061` | Notificación de interrupción | 3.0 | Baja importancia |
| G061 | `P061` | Notificación de interrupción | 4.0 | Baja importancia |
| G061 | `P061` | Notificación de interrupción | 5.0 | Importancia Mediana |
| G061 | `P061` | Notificación de interrupción | 6.0 | Importancia Mediana |
| G061 | `P061` | Notificación de interrupción | 7.0 | Alta importancia |
| G061 | `P061` | Notificación de interrupción | 8.0 | Alta importancia |
| G061 | `P061` | Notificación de interrupción | 9.0 | Muy alta importancia |
| G061 | `P061` | Notificación de interrupción | 10.0 | Muy alta importancia |
| G061 | `P061` | Notificación de interrupción | 11.0 | NS |
| G061 | `P061` | Notificación de interrupción | 12.0 | NR |
| G061 | `P062` | Uso eficiente | 1.0 | Muy baja importancia |
| G061 | `P062` | Uso eficiente | 2.0 | Muy baja importancia |
| G061 | `P062` | Uso eficiente | 3.0 | Baja importancia |
| G061 | `P062` | Uso eficiente | 4.0 | Baja importancia |
| G061 | `P062` | Uso eficiente | 5.0 | Importancia Mediana |
| G061 | `P062` | Uso eficiente | 6.0 | Importancia Mediana |
| G061 | `P062` | Uso eficiente | 7.0 | Alta importancia |
| G061 | `P062` | Uso eficiente | 8.0 | Alta importancia |
| G061 | `P062` | Uso eficiente | 9.0 | Muy alta importancia |
| G061 | `P062` | Uso eficiente | 10.0 | Muy alta importancia |
| G061 | `P062` | Uso eficiente | 11.0 | NS |
| G061 | `P062` | Uso eficiente | 12.0 | NR |
| G061 | `P063` | Riesgos y peligros | 1.0 | Muy baja importancia |
| G061 | `P063` | Riesgos y peligros | 2.0 | Muy baja importancia |
| G061 | `P063` | Riesgos y peligros | 3.0 | Baja importancia |
| G061 | `P063` | Riesgos y peligros | 4.0 | Baja importancia |
| G061 | `P063` | Riesgos y peligros | 5.0 | Importancia Mediana |
| G061 | `P063` | Riesgos y peligros | 6.0 | Importancia Mediana |
| G061 | `P063` | Riesgos y peligros | 7.0 | Alta importancia |
| G061 | `P063` | Riesgos y peligros | 8.0 | Alta importancia |
| G061 | `P063` | Riesgos y peligros | 9.0 | Muy alta importancia |
| G061 | `P063` | Riesgos y peligros | 10.0 | Muy alta importancia |
| G061 | `P063` | Riesgos y peligros | 11.0 | NS |
| G061 | `P063` | Riesgos y peligros | 12.0 | NR |
| G061 | `P064` | Derechos y deberes | 1.0 | Muy baja importancia |
| G061 | `P064` | Derechos y deberes | 2.0 | Muy baja importancia |
| G061 | `P064` | Derechos y deberes | 3.0 | Baja importancia |
| G061 | `P064` | Derechos y deberes | 4.0 | Baja importancia |
| G061 | `P064` | Derechos y deberes | 5.0 | Importancia Mediana |
| G061 | `P064` | Derechos y deberes | 6.0 | Importancia Mediana |
| G061 | `P064` | Derechos y deberes | 7.0 | Alta importancia |
| G061 | `P064` | Derechos y deberes | 8.0 | Alta importancia |
| G061 | `P064` | Derechos y deberes | 9.0 | Muy alta importancia |
| G061 | `P064` | Derechos y deberes | 10.0 | Muy alta importancia |
| G061 | `P064` | Derechos y deberes | 11.0 | NS |
| G061 | `P064` | Derechos y deberes | 12.0 | NR |
| G061 | `P065` | Medición del consumo de energía | 1.0 | Muy baja importancia |
| G061 | `P065` | Medición del consumo de energía | 2.0 | Muy baja importancia |
| G061 | `P065` | Medición del consumo de energía | 3.0 | Baja importancia |
| G061 | `P065` | Medición del consumo de energía | 4.0 | Baja importancia |
| G061 | `P065` | Medición del consumo de energía | 5.0 | Importancia Mediana |
| G061 | `P065` | Medición del consumo de energía | 6.0 | Importancia Mediana |
| G061 | `P065` | Medición del consumo de energía | 7.0 | Alta importancia |
| G061 | `P065` | Medición del consumo de energía | 8.0 | Alta importancia |
| G061 | `P065` | Medición del consumo de energía | 9.0 | Muy alta importancia |
| G061 | `P065` | Medición del consumo de energía | 10.0 | Muy alta importancia |
| G061 | `P065` | Medición del consumo de energía | 11.0 | NS |
| G061 | `P065` | Medición del consumo de energía | 12.0 | NR |
| G066 | `P066` | 1º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P066` | 1º puesto | 2.0 | Factura sin errores |
| G066 | `P066` | 1º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P066` | 1º puesto | 4.0 | Locales para el pago |
| G066 | `P066` | 1º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P066` | 1º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G066 | `P067` | 2º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P067` | 2º puesto | 2.0 | Factura sin errores |
| G066 | `P067` | 2º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P067` | 2º puesto | 4.0 | Locales para el pago |
| G066 | `P067` | 2º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P067` | 2º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G066 | `P068` | 3º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P068` | 3º puesto | 2.0 | Factura sin errores |
| G066 | `P068` | 3º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P068` | 3º puesto | 4.0 | Locales para el pago |
| G066 | `P068` | 3º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P068` | 3º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G066 | `P069` | 4º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P069` | 4º puesto | 2.0 | Factura sin errores |
| G066 | `P069` | 4º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P069` | 4º puesto | 4.0 | Locales para el pago |
| G066 | `P069` | 4º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P069` | 4º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G066 | `P070` | 5º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P070` | 5º puesto | 2.0 | Factura sin errores |
| G066 | `P070` | 5º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P070` | 5º puesto | 4.0 | Locales para el pago |
| G066 | `P070` | 5º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P070` | 5º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G066 | `P071` | 6º puesto | 1.0 | Plazo entre la recepción y el vencimiento |
| G066 | `P071` | 6º puesto | 2.0 | Factura sin errores |
| G066 | `P071` | 6º puesto | 3.0 | Facilidad de comprensión |
| G066 | `P071` | 6º puesto | 4.0 | Locales para el pago |
| G066 | `P071` | 6º puesto | 5.0 | Fechas para el vencimiento |
| G066 | `P071` | 6º puesto | 6.0 | Disponibilidad de canales de pago digitales |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 1.0 | Muy baja importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 2.0 | Muy baja importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 3.0 | Baja importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 4.0 | Baja importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 5.0 | Importancia Mediana |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 6.0 | Importancia Mediana |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 7.0 | Alta importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 8.0 | Alta importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 9.0 | Muy alta importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 10.0 | Muy alta importancia |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 11.0 | NS |
| G072 | `P072` | Plazo entre la recepción y el vencimiento | 12.0 | NR |
| G072 | `P073` | Factura sin errores | 1.0 | Muy baja importancia |
| G072 | `P073` | Factura sin errores | 2.0 | Muy baja importancia |
| G072 | `P073` | Factura sin errores | 3.0 | Baja importancia |
| G072 | `P073` | Factura sin errores | 4.0 | Baja importancia |
| G072 | `P073` | Factura sin errores | 5.0 | Importancia Mediana |
| G072 | `P073` | Factura sin errores | 6.0 | Importancia Mediana |
| G072 | `P073` | Factura sin errores | 7.0 | Alta importancia |
| G072 | `P073` | Factura sin errores | 8.0 | Alta importancia |
| G072 | `P073` | Factura sin errores | 9.0 | Muy alta importancia |
| G072 | `P073` | Factura sin errores | 10.0 | Muy alta importancia |
| G072 | `P073` | Factura sin errores | 11.0 | NS |
| G072 | `P073` | Factura sin errores | 12.0 | NR |
| G072 | `P074` | Facilidad de comprensión | 1.0 | Muy baja importancia |
| G072 | `P074` | Facilidad de comprensión | 2.0 | Muy baja importancia |
| G072 | `P074` | Facilidad de comprensión | 3.0 | Baja importancia |
| G072 | `P074` | Facilidad de comprensión | 4.0 | Baja importancia |
| G072 | `P074` | Facilidad de comprensión | 5.0 | Importancia Mediana |
| G072 | `P074` | Facilidad de comprensión | 6.0 | Importancia Mediana |
| G072 | `P074` | Facilidad de comprensión | 7.0 | Alta importancia |
| G072 | `P074` | Facilidad de comprensión | 8.0 | Alta importancia |
| G072 | `P074` | Facilidad de comprensión | 9.0 | Muy alta importancia |
| G072 | `P074` | Facilidad de comprensión | 10.0 | Muy alta importancia |
| G072 | `P074` | Facilidad de comprensión | 11.0 | NS |
| G072 | `P074` | Facilidad de comprensión | 12.0 | NR |
| G072 | `P075` | Locales para el pago | 1.0 | Muy baja importancia |
| G072 | `P075` | Locales para el pago | 2.0 | Muy baja importancia |
| G072 | `P075` | Locales para el pago | 3.0 | Baja importancia |
| G072 | `P075` | Locales para el pago | 4.0 | Baja importancia |
| G072 | `P075` | Locales para el pago | 5.0 | Importancia Mediana |
| G072 | `P075` | Locales para el pago | 6.0 | Importancia Mediana |
| G072 | `P075` | Locales para el pago | 7.0 | Alta importancia |
| G072 | `P075` | Locales para el pago | 8.0 | Alta importancia |
| G072 | `P075` | Locales para el pago | 9.0 | Muy alta importancia |
| G072 | `P075` | Locales para el pago | 10.0 | Muy alta importancia |
| G072 | `P075` | Locales para el pago | 11.0 | NS |
| G072 | `P075` | Locales para el pago | 12.0 | NR |
| G072 | `P076` | Fechas para el vencimiento | 1.0 | Muy baja importancia |
| G072 | `P076` | Fechas para el vencimiento | 2.0 | Muy baja importancia |
| G072 | `P076` | Fechas para el vencimiento | 3.0 | Baja importancia |
| G072 | `P076` | Fechas para el vencimiento | 4.0 | Baja importancia |
| G072 | `P076` | Fechas para el vencimiento | 5.0 | Importancia Mediana |
| G072 | `P076` | Fechas para el vencimiento | 6.0 | Importancia Mediana |
| G072 | `P076` | Fechas para el vencimiento | 7.0 | Alta importancia |
| G072 | `P076` | Fechas para el vencimiento | 8.0 | Alta importancia |
| G072 | `P076` | Fechas para el vencimiento | 9.0 | Muy alta importancia |
| G072 | `P076` | Fechas para el vencimiento | 10.0 | Muy alta importancia |
| G072 | `P076` | Fechas para el vencimiento | 11.0 | NS |
| G072 | `P076` | Fechas para el vencimiento | 12.0 | NR |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 1.0 | Muy baja importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 2.0 | Muy baja importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 3.0 | Baja importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 4.0 | Baja importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 5.0 | Importancia Mediana |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 6.0 | Importancia Mediana |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 7.0 | Alta importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 8.0 | Alta importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 9.0 | Muy alta importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 10.0 | Muy alta importancia |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 11.0 | NS |
| G072 | `P077` | Disponibilidad de canales de pago digitales | 12.0 | NR |
| G078 | `P078` | 1º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P078` | 1º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P078` | 1º puesto | 3.0 | Duración de la atención |
| G078 | `P078` | 1º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P078` | 1º puesto | 5.0 | Claridad en la información |
| G078 | `P078` | 1º puesto | 6.0 | Calidad de la atención |
| G078 | `P078` | 1º puesto | 7.0 | Plazo informado |
| G078 | `P078` | 1º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P078` | 1º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P078` | 1º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P079` | 2º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P079` | 2º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P079` | 2º puesto | 3.0 | Duración de la atención |
| G078 | `P079` | 2º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P079` | 2º puesto | 5.0 | Claridad en la información |
| G078 | `P079` | 2º puesto | 6.0 | Calidad de la atención |
| G078 | `P079` | 2º puesto | 7.0 | Plazo informado |
| G078 | `P079` | 2º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P079` | 2º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P079` | 2º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P080` | 3º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P080` | 3º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P080` | 3º puesto | 3.0 | Duración de la atención |
| G078 | `P080` | 3º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P080` | 3º puesto | 5.0 | Claridad en la información |
| G078 | `P080` | 3º puesto | 6.0 | Calidad de la atención |
| G078 | `P080` | 3º puesto | 7.0 | Plazo informado |
| G078 | `P080` | 3º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P080` | 3º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P080` | 3º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P081` | 4º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P081` | 4º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P081` | 4º puesto | 3.0 | Duración de la atención |
| G078 | `P081` | 4º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P081` | 4º puesto | 5.0 | Claridad en la información |
| G078 | `P081` | 4º puesto | 6.0 | Calidad de la atención |
| G078 | `P081` | 4º puesto | 7.0 | Plazo informado |
| G078 | `P081` | 4º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P081` | 4º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P081` | 4º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P082` | 5º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P082` | 5º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P082` | 5º puesto | 3.0 | Duración de la atención |
| G078 | `P082` | 5º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P082` | 5º puesto | 5.0 | Claridad en la información |
| G078 | `P082` | 5º puesto | 6.0 | Calidad de la atención |
| G078 | `P082` | 5º puesto | 7.0 | Plazo informado |
| G078 | `P082` | 5º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P082` | 5º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P082` | 5º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P083` | 6º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P083` | 6º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P083` | 6º puesto | 3.0 | Duración de la atención |
| G078 | `P083` | 6º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P083` | 6º puesto | 5.0 | Claridad en la información |
| G078 | `P083` | 6º puesto | 6.0 | Calidad de la atención |
| G078 | `P083` | 6º puesto | 7.0 | Plazo informado |
| G078 | `P083` | 6º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P083` | 6º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P083` | 6º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P084` | 7º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P084` | 7º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P084` | 7º puesto | 3.0 | Duración de la atención |
| G078 | `P084` | 7º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P084` | 7º puesto | 5.0 | Claridad en la información |
| G078 | `P084` | 7º puesto | 6.0 | Calidad de la atención |
| G078 | `P084` | 7º puesto | 7.0 | Plazo informado |
| G078 | `P084` | 7º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P084` | 7º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P084` | 7º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P085` | 8º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P085` | 8º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P085` | 8º puesto | 3.0 | Duración de la atención |
| G078 | `P085` | 8º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P085` | 8º puesto | 5.0 | Claridad en la información |
| G078 | `P085` | 8º puesto | 6.0 | Calidad de la atención |
| G078 | `P085` | 8º puesto | 7.0 | Plazo informado |
| G078 | `P085` | 8º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P085` | 8º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P085` | 8º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P086` | 9º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P086` | 9º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P086` | 9º puesto | 3.0 | Duración de la atención |
| G078 | `P086` | 9º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P086` | 9º puesto | 5.0 | Claridad en la información |
| G078 | `P086` | 9º puesto | 6.0 | Calidad de la atención |
| G078 | `P086` | 9º puesto | 7.0 | Plazo informado |
| G078 | `P086` | 9º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P086` | 9º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P086` | 9º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G078 | `P087` | 10º puesto | 1.0 | Facilidad para contactarse |
| G078 | `P087` | 10º puesto | 2.0 | Tiempo de espera hasta ser atendido |
| G078 | `P087` | 10º puesto | 3.0 | Duración de la atención |
| G078 | `P087` | 10º puesto | 4.0 | Conocimiento sobre el tema |
| G078 | `P087` | 10º puesto | 5.0 | Claridad en la información |
| G078 | `P087` | 10º puesto | 6.0 | Calidad de la atención |
| G078 | `P087` | 10º puesto | 7.0 | Plazo informado |
| G078 | `P087` | 10º puesto | 8.0 | Solución definitiva del problema |
| G078 | `P087` | 10º puesto | 9.0 | Cumplimiento del plazo |
| G078 | `P087` | 10º puesto | 10.0 | Autonomía/ flexibilidad del empleado |
| G088 | `P088` | Facilidad para contactarse | 1.0 | Muy baja importancia |
| G088 | `P088` | Facilidad para contactarse | 2.0 | Muy baja importancia |
| G088 | `P088` | Facilidad para contactarse | 3.0 | Baja importancia |
| G088 | `P088` | Facilidad para contactarse | 4.0 | Baja importancia |
| G088 | `P088` | Facilidad para contactarse | 5.0 | Importancia Mediana |
| G088 | `P088` | Facilidad para contactarse | 6.0 | Importancia Mediana |
| G088 | `P088` | Facilidad para contactarse | 7.0 | Alta importancia |
| G088 | `P088` | Facilidad para contactarse | 8.0 | Alta importancia |
| G088 | `P088` | Facilidad para contactarse | 9.0 | Muy alta importancia |
| G088 | `P088` | Facilidad para contactarse | 10.0 | Muy alta importancia |
| G088 | `P088` | Facilidad para contactarse | 11.0 | NS |
| G088 | `P088` | Facilidad para contactarse | 12.0 | NR |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 1.0 | Muy baja importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 2.0 | Muy baja importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 3.0 | Baja importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 4.0 | Baja importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 5.0 | Importancia Mediana |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 6.0 | Importancia Mediana |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 7.0 | Alta importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 8.0 | Alta importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 9.0 | Muy alta importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 10.0 | Muy alta importancia |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 11.0 | NS |
| G088 | `P089` | Tiempo de espera hasta ser atendido | 12.0 | NR |
| G088 | `P090` | Duración del tiempo de la atención | 1.0 | Muy baja importancia |
| G088 | `P090` | Duración del tiempo de la atención | 2.0 | Muy baja importancia |
| G088 | `P090` | Duración del tiempo de la atención | 3.0 | Baja importancia |
| G088 | `P090` | Duración del tiempo de la atención | 4.0 | Baja importancia |
| G088 | `P090` | Duración del tiempo de la atención | 5.0 | Importancia Mediana |
| G088 | `P090` | Duración del tiempo de la atención | 6.0 | Importancia Mediana |
| G088 | `P090` | Duración del tiempo de la atención | 7.0 | Alta importancia |
| G088 | `P090` | Duración del tiempo de la atención | 8.0 | Alta importancia |
| G088 | `P090` | Duración del tiempo de la atención | 9.0 | Muy alta importancia |
| G088 | `P090` | Duración del tiempo de la atención | 10.0 | Muy alta importancia |
| G088 | `P090` | Duración del tiempo de la atención | 11.0 | NS |
| G088 | `P090` | Duración del tiempo de la atención | 12.0 | NR |
| G088 | `P091` | Conocimiento sobre el tema | 1.0 | Muy baja importancia |
| G088 | `P091` | Conocimiento sobre el tema | 2.0 | Muy baja importancia |
| G088 | `P091` | Conocimiento sobre el tema | 3.0 | Baja importancia |
| G088 | `P091` | Conocimiento sobre el tema | 4.0 | Baja importancia |
| G088 | `P091` | Conocimiento sobre el tema | 5.0 | Importancia Mediana |
| G088 | `P091` | Conocimiento sobre el tema | 6.0 | Importancia Mediana |
| G088 | `P091` | Conocimiento sobre el tema | 7.0 | Alta importancia |
| G088 | `P091` | Conocimiento sobre el tema | 8.0 | Alta importancia |
| G088 | `P091` | Conocimiento sobre el tema | 9.0 | Muy alta importancia |
| G088 | `P091` | Conocimiento sobre el tema | 10.0 | Muy alta importancia |
| G088 | `P091` | Conocimiento sobre el tema | 11.0 | NS |
| G088 | `P091` | Conocimiento sobre el tema | 12.0 | NR |
| G088 | `P092` | Claridad en la información | 1.0 | Muy baja importancia |
| G088 | `P092` | Claridad en la información | 2.0 | Muy baja importancia |
| G088 | `P092` | Claridad en la información | 3.0 | Baja importancia |
| G088 | `P092` | Claridad en la información | 4.0 | Baja importancia |
| G088 | `P092` | Claridad en la información | 5.0 | Importancia Mediana |
| G088 | `P092` | Claridad en la información | 6.0 | Importancia Mediana |
| G088 | `P092` | Claridad en la información | 7.0 | Alta importancia |
| G088 | `P092` | Claridad en la información | 8.0 | Alta importancia |
| G088 | `P092` | Claridad en la información | 9.0 | Muy alta importancia |
| G088 | `P092` | Claridad en la información | 10.0 | Muy alta importancia |
| G088 | `P092` | Claridad en la información | 11.0 | NS |
| G088 | `P092` | Claridad en la información | 12.0 | NR |
| G088 | `P093` | Calidad de la atención | 1.0 | Muy baja importancia |
| G088 | `P093` | Calidad de la atención | 2.0 | Muy baja importancia |
| G088 | `P093` | Calidad de la atención | 3.0 | Baja importancia |
| G088 | `P093` | Calidad de la atención | 4.0 | Baja importancia |
| G088 | `P093` | Calidad de la atención | 5.0 | Importancia Mediana |
| G088 | `P093` | Calidad de la atención | 6.0 | Importancia Mediana |
| G088 | `P093` | Calidad de la atención | 7.0 | Alta importancia |
| G088 | `P093` | Calidad de la atención | 8.0 | Alta importancia |
| G088 | `P093` | Calidad de la atención | 9.0 | Muy alta importancia |
| G088 | `P093` | Calidad de la atención | 10.0 | Muy alta importancia |
| G088 | `P093` | Calidad de la atención | 11.0 | NS |
| G088 | `P093` | Calidad de la atención | 12.0 | NR |
| G088 | `P094` | Plazo informado | 1.0 | Muy baja importancia |
| G088 | `P094` | Plazo informado | 2.0 | Muy baja importancia |
| G088 | `P094` | Plazo informado | 3.0 | Baja importancia |
| G088 | `P094` | Plazo informado | 4.0 | Baja importancia |
| G088 | `P094` | Plazo informado | 5.0 | Importancia Mediana |
| G088 | `P094` | Plazo informado | 6.0 | Importancia Mediana |
| G088 | `P094` | Plazo informado | 7.0 | Alta importancia |
| G088 | `P094` | Plazo informado | 8.0 | Alta importancia |
| G088 | `P094` | Plazo informado | 9.0 | Muy alta importancia |
| G088 | `P094` | Plazo informado | 10.0 | Muy alta importancia |
| G088 | `P094` | Plazo informado | 11.0 | NS |
| G088 | `P094` | Plazo informado | 12.0 | NR |
| G088 | `P095` | Solución definitiva del problema | 1.0 | Muy baja importancia |
| G088 | `P095` | Solución definitiva del problema | 2.0 | Muy baja importancia |
| G088 | `P095` | Solución definitiva del problema | 3.0 | Baja importancia |
| G088 | `P095` | Solución definitiva del problema | 4.0 | Baja importancia |
| G088 | `P095` | Solución definitiva del problema | 5.0 | Importancia Mediana |
| G088 | `P095` | Solución definitiva del problema | 6.0 | Importancia Mediana |
| G088 | `P095` | Solución definitiva del problema | 7.0 | Alta importancia |
| G088 | `P095` | Solución definitiva del problema | 8.0 | Alta importancia |
| G088 | `P095` | Solución definitiva del problema | 9.0 | Muy alta importancia |
| G088 | `P095` | Solución definitiva del problema | 10.0 | Muy alta importancia |
| G088 | `P095` | Solución definitiva del problema | 11.0 | NS |
| G088 | `P095` | Solución definitiva del problema | 12.0 | NR |
| G088 | `P096` | Cumplimiento del plazo | 1.0 | Muy baja importancia |
| G088 | `P096` | Cumplimiento del plazo | 2.0 | Muy baja importancia |
| G088 | `P096` | Cumplimiento del plazo | 3.0 | Baja importancia |
| G088 | `P096` | Cumplimiento del plazo | 4.0 | Baja importancia |
| G088 | `P096` | Cumplimiento del plazo | 5.0 | Importancia Mediana |
| G088 | `P096` | Cumplimiento del plazo | 6.0 | Importancia Mediana |
| G088 | `P096` | Cumplimiento del plazo | 7.0 | Alta importancia |
| G088 | `P096` | Cumplimiento del plazo | 8.0 | Alta importancia |
| G088 | `P096` | Cumplimiento del plazo | 9.0 | Muy alta importancia |
| G088 | `P096` | Cumplimiento del plazo | 10.0 | Muy alta importancia |
| G088 | `P096` | Cumplimiento del plazo | 11.0 | NS |
| G088 | `P096` | Cumplimiento del plazo | 12.0 | NR |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 1.0 | Muy baja importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 2.0 | Muy baja importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 3.0 | Baja importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 4.0 | Baja importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 5.0 | Importancia Mediana |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 6.0 | Importancia Mediana |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 7.0 | Alta importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 8.0 | Alta importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 9.0 | Muy alta importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 10.0 | Muy alta importancia |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 11.0 | NS |
| G088 | `P097` | Autonomía/ flexibilidad del empleado | 12.0 | NR |
| G098 | `P098` | 1º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P098` | 1º puesto | 2.0 | Correcta con los clientes |
| G098 | `P098` | 1º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P098` | 1º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P098` | 1º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P098` | 1º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P098` | 1º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P098` | 1º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P098` | 1º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P099` | 2º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P099` | 2º puesto | 2.0 | Correcta con los clientes |
| G098 | `P099` | 2º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P099` | 2º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P099` | 2º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P099` | 2º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P099` | 2º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P099` | 2º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P099` | 2º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P100` | 3º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P100` | 3º puesto | 2.0 | Correcta con los clientes |
| G098 | `P100` | 3º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P100` | 3º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P100` | 3º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P100` | 3º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P100` | 3º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P100` | 3º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P100` | 3º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P101` | 4º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P101` | 4º puesto | 2.0 | Correcta con los clientes |
| G098 | `P101` | 4º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P101` | 4º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P101` | 4º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P101` | 4º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P101` | 4º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P101` | 4º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P101` | 4º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P102` | 5º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P102` | 5º puesto | 2.0 | Correcta con los clientes |
| G098 | `P102` | 5º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P102` | 5º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P102` | 5º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P102` | 5º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P102` | 5º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P102` | 5º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P102` | 5º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P103` | 6º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P103` | 6º puesto | 2.0 | Correcta con los clientes |
| G098 | `P103` | 6º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P103` | 6º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P103` | 6º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P103` | 6º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P103` | 6º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P103` | 6º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P103` | 6º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P104` | 7º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P104` | 7º puesto | 2.0 | Correcta con los clientes |
| G098 | `P104` | 7º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P104` | 7º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P104` | 7º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P104` | 7º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P104` | 7º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P104` | 7º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P104` | 7º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P105` | 8º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P105` | 8º puesto | 2.0 | Correcta con los clientes |
| G098 | `P105` | 8º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P105` | 8º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P105` | 8º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P105` | 8º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P105` | 8º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P105` | 8º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P105` | 8º puesto | 9.0 | Preparada para situaciones de emergencia |
| G098 | `P106` | 9º puesto | 1.0 | Respeta los derechos de los clientes |
| G098 | `P106` | 9º puesto | 2.0 | Correcta con los clientes |
| G098 | `P106` | 9º puesto | 3.0 | Invierte para proveer energía con calidad |
| G098 | `P106` | 9º puesto | 4.0 | Informa a sus clientes con respecto a su actuación |
| G098 | `P106` | 9º puesto | 5.0 | Se ocupa de evitar hurtos de energía |
| G098 | `P106` | 9º puesto | 6.0 | Ofrece atención sin discriminación |
| G098 | `P106` | 9º puesto | 7.0 | Dispuesta a negociar con sus clientes (flexible) |
| G098 | `P106` | 9º puesto | 8.0 | Se ocupa del medio ambiente |
| G098 | `P106` | 9º puesto | 9.0 | Preparada para situaciones de emergencia |
| G107 | `P107` | Respeta los derechos de los clientes | 1.0 | Muy baja importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 2.0 | Muy baja importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 3.0 | Baja importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 4.0 | Baja importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 5.0 | Importancia Mediana |
| G107 | `P107` | Respeta los derechos de los clientes | 6.0 | Importancia Mediana |
| G107 | `P107` | Respeta los derechos de los clientes | 7.0 | Alta importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 8.0 | Alta importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 9.0 | Muy alta importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 10.0 | Muy alta importancia |
| G107 | `P107` | Respeta los derechos de los clientes | 11.0 | NS |
| G107 | `P107` | Respeta los derechos de los clientes | 12.0 | NR |
| G107 | `P108` | Correcta con los clientes | 1.0 | Muy baja importancia |
| G107 | `P108` | Correcta con los clientes | 2.0 | Muy baja importancia |
| G107 | `P108` | Correcta con los clientes | 3.0 | Baja importancia |
| G107 | `P108` | Correcta con los clientes | 4.0 | Baja importancia |
| G107 | `P108` | Correcta con los clientes | 5.0 | Importancia Mediana |
| G107 | `P108` | Correcta con los clientes | 6.0 | Importancia Mediana |
| G107 | `P108` | Correcta con los clientes | 7.0 | Alta importancia |
| G107 | `P108` | Correcta con los clientes | 8.0 | Alta importancia |
| G107 | `P108` | Correcta con los clientes | 9.0 | Muy alta importancia |
| G107 | `P108` | Correcta con los clientes | 10.0 | Muy alta importancia |
| G107 | `P108` | Correcta con los clientes | 11.0 | NS |
| G107 | `P108` | Correcta con los clientes | 12.0 | NR |
| G107 | `P109` | Invierte para proveer energía con calidad | 1.0 | Muy baja importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 2.0 | Muy baja importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 3.0 | Baja importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 4.0 | Baja importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 5.0 | Importancia Mediana |
| G107 | `P109` | Invierte para proveer energía con calidad | 6.0 | Importancia Mediana |
| G107 | `P109` | Invierte para proveer energía con calidad | 7.0 | Alta importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 8.0 | Alta importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 9.0 | Muy alta importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 10.0 | Muy alta importancia |
| G107 | `P109` | Invierte para proveer energía con calidad | 11.0 | NS |
| G107 | `P109` | Invierte para proveer energía con calidad | 12.0 | NR |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 1.0 | Muy baja importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 2.0 | Muy baja importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 3.0 | Baja importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 4.0 | Baja importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 5.0 | Importancia Mediana |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 6.0 | Importancia Mediana |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 7.0 | Alta importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 8.0 | Alta importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 9.0 | Muy alta importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 10.0 | Muy alta importancia |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 11.0 | NS |
| G107 | `P110` | Informa a sus clientes con respecto a su actuación | 12.0 | NR |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 1.0 | Muy baja importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 2.0 | Muy baja importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 3.0 | Baja importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 4.0 | Baja importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 5.0 | Importancia Mediana |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 6.0 | Importancia Mediana |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 7.0 | Alta importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 8.0 | Alta importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 9.0 | Muy alta importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 10.0 | Muy alta importancia |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 11.0 | NS |
| G107 | `P111` | Se ocupa de evitar hurtos de energía | 12.0 | NR |
| G107 | `P112` | Ofrece atención sin discriminación | 1.0 | Muy baja importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 2.0 | Muy baja importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 3.0 | Baja importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 4.0 | Baja importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 5.0 | Importancia Mediana |
| G107 | `P112` | Ofrece atención sin discriminación | 6.0 | Importancia Mediana |
| G107 | `P112` | Ofrece atención sin discriminación | 7.0 | Alta importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 8.0 | Alta importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 9.0 | Muy alta importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 10.0 | Muy alta importancia |
| G107 | `P112` | Ofrece atención sin discriminación | 11.0 | NS |
| G107 | `P112` | Ofrece atención sin discriminación | 12.0 | NR |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 1.0 | Muy baja importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 2.0 | Muy baja importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 3.0 | Baja importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 4.0 | Baja importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 5.0 | Importancia Mediana |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 6.0 | Importancia Mediana |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 7.0 | Alta importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 8.0 | Alta importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 9.0 | Muy alta importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 10.0 | Muy alta importancia |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 11.0 | NS |
| G107 | `P113` | Dispuesta a negociar con sus clientes (flexible) | 12.0 | NR |
| G107 | `P114` | Se ocupa del medio ambiente | 1.0 | Muy baja importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 2.0 | Muy baja importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 3.0 | Baja importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 4.0 | Baja importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 5.0 | Importancia Mediana |
| G107 | `P114` | Se ocupa del medio ambiente | 6.0 | Importancia Mediana |
| G107 | `P114` | Se ocupa del medio ambiente | 7.0 | Alta importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 8.0 | Alta importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 9.0 | Muy alta importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 10.0 | Muy alta importancia |
| G107 | `P114` | Se ocupa del medio ambiente | 11.0 | NS |
| G107 | `P114` | Se ocupa del medio ambiente | 12.0 | NR |
| G107 | `P115` | Preparada para situaciones de emergencia | 1.0 | Muy baja importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 2.0 | Muy baja importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 3.0 | Baja importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 4.0 | Baja importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 5.0 | Importancia Mediana |
| G107 | `P115` | Preparada para situaciones de emergencia | 6.0 | Importancia Mediana |
| G107 | `P115` | Preparada para situaciones de emergencia | 7.0 | Alta importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 8.0 | Alta importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 9.0 | Muy alta importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 10.0 | Muy alta importancia |
| G107 | `P115` | Preparada para situaciones de emergencia | 11.0 | NS |
| G107 | `P115` | Preparada para situaciones de emergencia | 12.0 | NR |
| G116 | `P116` | 1º puesto | 1.0 | Suministro de energía |
| G116 | `P116` | 1º puesto | 2.0 | Información y comunicación |
| G116 | `P116` | 1º puesto | 3.0 | Factura de energía |
| G116 | `P116` | 1º puesto | 4.0 | Atención al cliente |
| G116 | `P116` | 1º puesto | 5.0 | Imagen |
| G116 | `P117` | 2º puesto | 1.0 | Suministro de energía |
| G116 | `P117` | 2º puesto | 2.0 | Información y comunicación |
| G116 | `P117` | 2º puesto | 3.0 | Factura de energía |
| G116 | `P117` | 2º puesto | 4.0 | Atención al cliente |
| G116 | `P117` | 2º puesto | 5.0 | Imagen |
| G116 | `P118` | 3º puesto | 1.0 | Suministro de energía |
| G116 | `P118` | 3º puesto | 2.0 | Información y comunicación |
| G116 | `P118` | 3º puesto | 3.0 | Factura de energía |
| G116 | `P118` | 3º puesto | 4.0 | Atención al cliente |
| G116 | `P118` | 3º puesto | 5.0 | Imagen |
| G116 | `P119` | 4º puesto | 1.0 | Suministro de energía |
| G116 | `P119` | 4º puesto | 2.0 | Información y comunicación |
| G116 | `P119` | 4º puesto | 3.0 | Factura de energía |
| G116 | `P119` | 4º puesto | 4.0 | Atención al cliente |
| G116 | `P119` | 4º puesto | 5.0 | Imagen |
| G116 | `P120` | 5º puesto | 1.0 | Suministro de energía |
| G116 | `P120` | 5º puesto | 2.0 | Información y comunicación |
| G116 | `P120` | 5º puesto | 3.0 | Factura de energía |
| G116 | `P120` | 5º puesto | 4.0 | Atención al cliente |
| G116 | `P120` | 5º puesto | 5.0 | Imagen |
| G121 | `P121` | Suministro de energía | 1.0 | Muy baja importancia |
| G121 | `P121` | Suministro de energía | 2.0 | Muy baja importancia |
| G121 | `P121` | Suministro de energía | 3.0 | Baja importancia |
| G121 | `P121` | Suministro de energía | 4.0 | Baja importancia |
| G121 | `P121` | Suministro de energía | 5.0 | Importancia Mediana |
| G121 | `P121` | Suministro de energía | 6.0 | Importancia Mediana |
| G121 | `P121` | Suministro de energía | 7.0 | Alta importancia |
| G121 | `P121` | Suministro de energía | 8.0 | Alta importancia |
| G121 | `P121` | Suministro de energía | 9.0 | Muy alta importancia |
| G121 | `P121` | Suministro de energía | 10.0 | Muy alta importancia |
| G121 | `P121` | Suministro de energía | 11.0 | NS |
| G121 | `P121` | Suministro de energía | 12.0 | NR |
| G121 | `P122` | Información y comunicación con el cliente | 1.0 | Muy baja importancia |
| G121 | `P122` | Información y comunicación con el cliente | 2.0 | Muy baja importancia |
| G121 | `P122` | Información y comunicación con el cliente | 3.0 | Baja importancia |
| G121 | `P122` | Información y comunicación con el cliente | 4.0 | Baja importancia |
| G121 | `P122` | Información y comunicación con el cliente | 5.0 | Importancia Mediana |
| G121 | `P122` | Información y comunicación con el cliente | 6.0 | Importancia Mediana |
| G121 | `P122` | Información y comunicación con el cliente | 7.0 | Alta importancia |
| G121 | `P122` | Información y comunicación con el cliente | 8.0 | Alta importancia |
| G121 | `P122` | Información y comunicación con el cliente | 9.0 | Muy alta importancia |
| G121 | `P122` | Información y comunicación con el cliente | 10.0 | Muy alta importancia |
| G121 | `P122` | Información y comunicación con el cliente | 11.0 | NS |
| G121 | `P122` | Información y comunicación con el cliente | 12.0 | NR |
| G121 | `P123` | Factura de energía | 1.0 | Muy baja importancia |
| G121 | `P123` | Factura de energía | 2.0 | Muy baja importancia |
| G121 | `P123` | Factura de energía | 3.0 | Baja importancia |
| G121 | `P123` | Factura de energía | 4.0 | Baja importancia |
| G121 | `P123` | Factura de energía | 5.0 | Importancia Mediana |
| G121 | `P123` | Factura de energía | 6.0 | Importancia Mediana |
| G121 | `P123` | Factura de energía | 7.0 | Alta importancia |
| G121 | `P123` | Factura de energía | 8.0 | Alta importancia |
| G121 | `P123` | Factura de energía | 9.0 | Muy alta importancia |
| G121 | `P123` | Factura de energía | 10.0 | Muy alta importancia |
| G121 | `P123` | Factura de energía | 11.0 | NS |
| G121 | `P123` | Factura de energía | 12.0 | NR |
| G121 | `P124` | Atención al cliente | 1.0 | Muy baja importancia |
| G121 | `P124` | Atención al cliente | 2.0 | Muy baja importancia |
| G121 | `P124` | Atención al cliente | 3.0 | Baja importancia |
| G121 | `P124` | Atención al cliente | 4.0 | Baja importancia |
| G121 | `P124` | Atención al cliente | 5.0 | Importancia Mediana |
| G121 | `P124` | Atención al cliente | 6.0 | Importancia Mediana |
| G121 | `P124` | Atención al cliente | 7.0 | Alta importancia |
| G121 | `P124` | Atención al cliente | 8.0 | Alta importancia |
| G121 | `P124` | Atención al cliente | 9.0 | Muy alta importancia |
| G121 | `P124` | Atención al cliente | 10.0 | Muy alta importancia |
| G121 | `P124` | Atención al cliente | 11.0 | NS |
| G121 | `P124` | Atención al cliente | 12.0 | NR |
| G121 | `P125` | Imagen de la empresa | 1.0 | Muy baja importancia |
| G121 | `P125` | Imagen de la empresa | 2.0 | Muy baja importancia |
| G121 | `P125` | Imagen de la empresa | 3.0 | Baja importancia |
| G121 | `P125` | Imagen de la empresa | 4.0 | Baja importancia |
| G121 | `P125` | Imagen de la empresa | 5.0 | Importancia Mediana |
| G121 | `P125` | Imagen de la empresa | 6.0 | Importancia Mediana |
| G121 | `P125` | Imagen de la empresa | 7.0 | Alta importancia |
| G121 | `P125` | Imagen de la empresa | 8.0 | Alta importancia |
| G121 | `P125` | Imagen de la empresa | 9.0 | Muy alta importancia |
| G121 | `P125` | Imagen de la empresa | 10.0 | Muy alta importancia |
| G121 | `P125` | Imagen de la empresa | 11.0 | NS |
| G121 | `P125` | Imagen de la empresa | 12.0 | NR |
| G129 | `P129` | Sin interrupción | 1.0 | Muy insatisfecho |
| G129 | `P129` | Sin interrupción | 2.0 | Muy insatisfecho |
| G129 | `P129` | Sin interrupción | 3.0 | Insatisfecho |
| G129 | `P129` | Sin interrupción | 4.0 | Insatisfecho |
| G129 | `P129` | Sin interrupción | 5.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P129` | Sin interrupción | 6.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P129` | Sin interrupción | 7.0 | Satisfecho |
| G129 | `P129` | Sin interrupción | 8.0 | Satisfecho |
| G129 | `P129` | Sin interrupción | 9.0 | Muy satisfecho |
| G129 | `P129` | Sin interrupción | 10.0 | Muy satisfecho |
| G129 | `P129` | Sin interrupción | 11.0 | NS |
| G129 | `P129` | Sin interrupción | 12.0 | NR |
| G129 | `P130` | Sin variación de voltaje | 1.0 | Muy insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 2.0 | Muy insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 3.0 | Insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 4.0 | Insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 5.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 6.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P130` | Sin variación de voltaje | 7.0 | Satisfecho |
| G129 | `P130` | Sin variación de voltaje | 8.0 | Satisfecho |
| G129 | `P130` | Sin variación de voltaje | 9.0 | Muy satisfecho |
| G129 | `P130` | Sin variación de voltaje | 10.0 | Muy satisfecho |
| G129 | `P130` | Sin variación de voltaje | 11.0 | NS |
| G129 | `P130` | Sin variación de voltaje | 12.0 | NR |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 1.0 | Muy insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 2.0 | Muy insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 3.0 | Insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 4.0 | Insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 5.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 6.0 | Ni satisfecho, Ni insatisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 7.0 | Satisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 8.0 | Satisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 9.0 | Muy satisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 10.0 | Muy satisfecho |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 11.0 | NS |
| G129 | `P131` | Rapidez en la reanudación de la energía cuando falta | 12.0 | NR |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 1.0 | Extremamente frecuentes |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 2.0 | Muy frecuentes |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 3.0 | Frecuentes |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 4.0 | Poco frecuente |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 5.0 | Muy poco frecuentes |
| P132 | `P132` | Percepción sobre la frecuencia de los cortes | 6.0 | No sabe |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 1.0 | Siempre |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 2.0 | Casi siempre |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 3.0 | A veces |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 4.0 | Casi nunca |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 5.0 | Nunca |
| P133 | `P133` | Percepción sobre la frecuencia de bajones/ parpadeos | 6.0 | No sabe |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 1.0 | Muy lento |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 2.0 | Lento |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 3.0 | Aceptable |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 4.0 | Rápido |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 5.0 | Muy rápido |
| P134 | `P134` | Percepción sobre la rapidez de la reposición del servicio | 6.0 | No sabe |
| P135 | `P135` | ¿Hubo interrupción en el suministro de energía en el último mes? | 1.0 | Sí, hubo interrupción |
| P135 | `P135` | ¿Hubo interrupción en el suministro de energía en el último mes? | 2.0 | No hubo interrupción |
| P135 | `P135` | ¿Hubo interrupción en el suministro de energía en el último mes? | 3.0 | No sabe |
| P136 | `P136` | Número de interrupciones en el domicilio en el último mes | -99.0 | No se recuerda |
| P136 | `P136` | Número de interrupciones en el domicilio en el último mes | -88.0 | No sabe |
| G137 | `P140` | No sabe | 1.0 | Mencionó |
| G137 | `P140` | No sabe | 2.0 | No mencionó |
| G137 | `P141` | No se recuerda | 1.0 | Mencionó |
| G137 | `P141` | No se recuerda | 2.0 | No mencionó |
| P142 | `P142` | Confirmación de la duración de las interrupciones | 1.0 | Correcto |
| P142 | `P142` | Confirmación de la duración de las interrupciones | 2.0 | No, corregir |
| G143 | `P143` | Notificación de interrupción | 1.0 | Muy insatisfecho |
| G143 | `P143` | Notificación de interrupción | 2.0 | Muy insatisfecho |
| G143 | `P143` | Notificación de interrupción | 3.0 | Insatisfecho |
| G143 | `P143` | Notificación de interrupción | 4.0 | Insatisfecho |
| G143 | `P143` | Notificación de interrupción | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P143` | Notificación de interrupción | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P143` | Notificación de interrupción | 7.0 | Satisfecho |
| G143 | `P143` | Notificación de interrupción | 8.0 | Satisfecho |
| G143 | `P143` | Notificación de interrupción | 9.0 | Muy satisfecho |
| G143 | `P143` | Notificación de interrupción | 10.0 | Muy satisfecho |
| G143 | `P143` | Notificación de interrupción | 11.0 | NS |
| G143 | `P143` | Notificación de interrupción | 12.0 | NR |
| G143 | `P144` | Uso eficiente | 1.0 | Muy insatisfecho |
| G143 | `P144` | Uso eficiente | 2.0 | Muy insatisfecho |
| G143 | `P144` | Uso eficiente | 3.0 | Insatisfecho |
| G143 | `P144` | Uso eficiente | 4.0 | Insatisfecho |
| G143 | `P144` | Uso eficiente | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P144` | Uso eficiente | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P144` | Uso eficiente | 7.0 | Satisfecho |
| G143 | `P144` | Uso eficiente | 8.0 | Satisfecho |
| G143 | `P144` | Uso eficiente | 9.0 | Muy satisfecho |
| G143 | `P144` | Uso eficiente | 10.0 | Muy satisfecho |
| G143 | `P144` | Uso eficiente | 11.0 | NS |
| G143 | `P144` | Uso eficiente | 12.0 | NR |
| G143 | `P145` | Riesgos y peligros | 1.0 | Muy insatisfecho |
| G143 | `P145` | Riesgos y peligros | 2.0 | Muy insatisfecho |
| G143 | `P145` | Riesgos y peligros | 3.0 | Insatisfecho |
| G143 | `P145` | Riesgos y peligros | 4.0 | Insatisfecho |
| G143 | `P145` | Riesgos y peligros | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P145` | Riesgos y peligros | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P145` | Riesgos y peligros | 7.0 | Satisfecho |
| G143 | `P145` | Riesgos y peligros | 8.0 | Satisfecho |
| G143 | `P145` | Riesgos y peligros | 9.0 | Muy satisfecho |
| G143 | `P145` | Riesgos y peligros | 10.0 | Muy satisfecho |
| G143 | `P145` | Riesgos y peligros | 11.0 | NS |
| G143 | `P145` | Riesgos y peligros | 12.0 | NR |
| G143 | `P146` | Derechos y deberes | 1.0 | Muy insatisfecho |
| G143 | `P146` | Derechos y deberes | 2.0 | Muy insatisfecho |
| G143 | `P146` | Derechos y deberes | 3.0 | Insatisfecho |
| G143 | `P146` | Derechos y deberes | 4.0 | Insatisfecho |
| G143 | `P146` | Derechos y deberes | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P146` | Derechos y deberes | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P146` | Derechos y deberes | 7.0 | Satisfecho |
| G143 | `P146` | Derechos y deberes | 8.0 | Satisfecho |
| G143 | `P146` | Derechos y deberes | 9.0 | Muy satisfecho |
| G143 | `P146` | Derechos y deberes | 10.0 | Muy satisfecho |
| G143 | `P146` | Derechos y deberes | 11.0 | NS |
| G143 | `P146` | Derechos y deberes | 12.0 | NR |
| G143 | `P147` | Medición del consumo de energía | 1.0 | Muy insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 2.0 | Muy insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 3.0 | Insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 4.0 | Insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P147` | Medición del consumo de energía | 7.0 | Satisfecho |
| G143 | `P147` | Medición del consumo de energía | 8.0 | Satisfecho |
| G143 | `P147` | Medición del consumo de energía | 9.0 | Muy satisfecho |
| G143 | `P147` | Medición del consumo de energía | 10.0 | Muy satisfecho |
| G143 | `P147` | Medición del consumo de energía | 11.0 | NS |
| G143 | `P147` | Medición del consumo de energía | 12.0 | NR |
| G143 | `P148` | Comunicación por diferentes medios | 1.0 | Muy insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 2.0 | Muy insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 3.0 | Insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 4.0 | Insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 7.0 | Satisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 8.0 | Satisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 9.0 | Muy satisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 10.0 | Muy satisfecho |
| G143 | `P148` | Comunicación por diferentes medios | 11.0 | NS |
| G143 | `P148` | Comunicación por diferentes medios | 12.0 | NR |
| G143 | `P149` | Facilidad de comprensión de la información dada | 1.0 | Muy insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 2.0 | Muy insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 3.0 | Insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 4.0 | Insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 5.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 6.0 | Ni satisfecho, Ni insatisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 7.0 | Satisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 8.0 | Satisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 9.0 | Muy satisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 10.0 | Muy satisfecho |
| G143 | `P149` | Facilidad de comprensión de la información dada | 11.0 | NS |
| G143 | `P149` | Facilidad de comprensión de la información dada | 12.0 | NR |
| P150 | `P150` | Conocimiento previo del corte programado | 1.0 | Nunca |
| P150 | `P150` | Conocimiento previo del corte programado | 2.0 | Casi nunca |
| P150 | `P150` | Conocimiento previo del corte programado | 3.0 | A veces |
| P150 | `P150` | Conocimiento previo del corte programado | 4.0 | Casi siempre |
| P150 | `P150` | Conocimiento previo del corte programado | 5.0 | Siempre |
| P150 | `P150` | Conocimiento previo del corte programado | 6.0 | No sabe |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 1.0 | Muy mala |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 2.0 | Mala |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 3.0 | Regular |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 4.0 | Buena |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 5.0 | Muy buena |
| P151 | `P151` | Evaluación de la orientación sobre el uso eficiente | 6.0 | No sabe |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 1.0 | Muy lento |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 2.0 | Lento |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 3.0 | Aceptable |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 4.0 | Rápido |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 5.0 | Muy rápido |
| P152 | `P152` | Evaluación de la orientación sobre riesgos y peligros | 6.0 | No sabe |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 1.0 | Muy mala |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 2.0 | Mala |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 3.0 | Regular |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 4.0 | Buena |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 5.0 | Muy buena |
| P153 | `P153` | Evaluación de la orientación sobre derechos y deberes | 6.0 | No sabe |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 1.0 | Muy insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 2.0 | Muy insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 3.0 | Insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 4.0 | Insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 7.0 | Satisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 8.0 | Satisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 9.0 | Muy satisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 10.0 | Muy satisfecho |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 11.0 | NS |
| G154 | `P154` | Plazo entre la recepción y el vencimiento | 12.0 | NR |
| G154 | `P155` | Factura sin errores | 1.0 | Muy insatisfecho |
| G154 | `P155` | Factura sin errores | 2.0 | Muy insatisfecho |
| G154 | `P155` | Factura sin errores | 3.0 | Insatisfecho |
| G154 | `P155` | Factura sin errores | 4.0 | Insatisfecho |
| G154 | `P155` | Factura sin errores | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P155` | Factura sin errores | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P155` | Factura sin errores | 7.0 | Satisfecho |
| G154 | `P155` | Factura sin errores | 8.0 | Satisfecho |
| G154 | `P155` | Factura sin errores | 9.0 | Muy satisfecho |
| G154 | `P155` | Factura sin errores | 10.0 | Muy satisfecho |
| G154 | `P155` | Factura sin errores | 11.0 | NS |
| G154 | `P155` | Factura sin errores | 12.0 | NR |
| G154 | `P156` | Facilidad de comprensión | 1.0 | Muy insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 2.0 | Muy insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 3.0 | Insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 4.0 | Insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P156` | Facilidad de comprensión | 7.0 | Satisfecho |
| G154 | `P156` | Facilidad de comprensión | 8.0 | Satisfecho |
| G154 | `P156` | Facilidad de comprensión | 9.0 | Muy satisfecho |
| G154 | `P156` | Facilidad de comprensión | 10.0 | Muy satisfecho |
| G154 | `P156` | Facilidad de comprensión | 11.0 | NS |
| G154 | `P156` | Facilidad de comprensión | 12.0 | NR |
| G154 | `P157` | Locales para el pago | 1.0 | Muy insatisfecho |
| G154 | `P157` | Locales para el pago | 2.0 | Muy insatisfecho |
| G154 | `P157` | Locales para el pago | 3.0 | Insatisfecho |
| G154 | `P157` | Locales para el pago | 4.0 | Insatisfecho |
| G154 | `P157` | Locales para el pago | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P157` | Locales para el pago | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P157` | Locales para el pago | 7.0 | Satisfecho |
| G154 | `P157` | Locales para el pago | 8.0 | Satisfecho |
| G154 | `P157` | Locales para el pago | 9.0 | Muy satisfecho |
| G154 | `P157` | Locales para el pago | 10.0 | Muy satisfecho |
| G154 | `P157` | Locales para el pago | 11.0 | NS |
| G154 | `P157` | Locales para el pago | 12.0 | NR |
| G154 | `P158` | Fechas para el vencimiento | 1.0 | Muy insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 2.0 | Muy insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 3.0 | Insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 4.0 | Insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P158` | Fechas para el vencimiento | 7.0 | Satisfecho |
| G154 | `P158` | Fechas para el vencimiento | 8.0 | Satisfecho |
| G154 | `P158` | Fechas para el vencimiento | 9.0 | Muy satisfecho |
| G154 | `P158` | Fechas para el vencimiento | 10.0 | Muy satisfecho |
| G154 | `P158` | Fechas para el vencimiento | 11.0 | NS |
| G154 | `P158` | Fechas para el vencimiento | 12.0 | NR |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 1.0 | Muy insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 2.0 | Muy insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 3.0 | Insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 4.0 | Insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 7.0 | Satisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 8.0 | Satisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 9.0 | Muy satisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 10.0 | Muy satisfecho |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 11.0 | NS |
| G154 | `P159` | Disponibilidad de canales de pago digitales | 12.0 | NR |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 1.0 | Muy insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 2.0 | Muy insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 3.0 | Insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 4.0 | Insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 7.0 | Satisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 8.0 | Satisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 9.0 | Muy satisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 10.0 | Muy satisfecho |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 11.0 | NS |
| G154 | `P160` | Aviso de facturas atrasadas o deudas | 12.0 | NR |
| G154 | `P161` | Aviso de corte por falta de pago | 1.0 | Muy insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 2.0 | Muy insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 3.0 | Insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 4.0 | Insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 5.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 6.0 | Ni satisfecho, Ni insatisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 7.0 | Satisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 8.0 | Satisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 9.0 | Muy satisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 10.0 | Muy satisfecho |
| G154 | `P161` | Aviso de corte por falta de pago | 11.0 | NS |
| G154 | `P161` | Aviso de corte por falta de pago | 12.0 | NR |
| P162 | `P162` | Entrega oportuna de la factura | 1.0 | Nunca |
| P162 | `P162` | Entrega oportuna de la factura | 2.0 | Casi nunca |
| P162 | `P162` | Entrega oportuna de la factura | 3.0 | A veces |
| P162 | `P162` | Entrega oportuna de la factura | 4.0 | Casi siempre |
| P162 | `P162` | Entrega oportuna de la factura | 5.0 | Siempre |
| P162 | `P162` | Entrega oportuna de la factura | 6.0 | No sabe |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 1.0 | Siempre |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 2.0 | Casi siempre |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 3.0 | A veces |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 4.0 | Casi nunca |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 5.0 | Nunca |
| P163 | `P163` | Frecuencia con que la factura tiene errores | 6.0 | No sabe |
| P164 | `P164` | Cantidad de locales y medios para el pago | 1.0 | Muy escasos |
| P164 | `P164` | Cantidad de locales y medios para el pago | 2.0 | Escasos |
| P164 | `P164` | Cantidad de locales y medios para el pago | 3.0 | Aceptables |
| P164 | `P164` | Cantidad de locales y medios para el pago | 4.0 | Satisfactorios |
| P164 | `P164` | Cantidad de locales y medios para el pago | 5.0 | Muy satisfactorios |
| P164 | `P164` | Cantidad de locales y medios para el pago | 6.0 | No sabe |
| P165 | `P165` | Plazo para cancelar la factura | 1.0 | Muy escaso |
| P165 | `P165` | Plazo para cancelar la factura | 2.0 | Escaso |
| P165 | `P165` | Plazo para cancelar la factura | 3.0 | Aceptable |
| P165 | `P165` | Plazo para cancelar la factura | 4.0 | Satisfactorio |
| P165 | `P165` | Plazo para cancelar la factura | 5.0 | Muy satisfactorio |
| P165 | `P165` | Plazo para cancelar la factura | 6.0 | No sabe |
| P167 | `P167` | Cómo recibe la factura | -99.0 | No respondió |
| P167 | `P167` | Cómo recibe la factura | -88.0 | No Sabe |
| P167 | `P167` | Cómo recibe la factura | 1.0 | Correo electrónico |
| P167 | `P167` | Cómo recibe la factura | 2.0 | Factura impresa |
| P167 | `P167` | Cómo recibe la factura | 3.0 | Ambos medios |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | -99.0 | No respondió |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | -88.0 | No Sabe |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | 1.0 | Sí, cambiaría |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | 2.0 | Sí, pero necesitaría ayuda |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | 3.0 | Tal vez/ necesita más información |
| P169 | `P169` | Disposición para recibir la factura únicamente de forma electrónica | 4.0 | No, prefiere la impresa |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 1.0 | Muy insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 2.0 | Muy insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 3.0 | Insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 4.0 | Insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 7.0 | Satisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 8.0 | Satisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 9.0 | Muy satisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 10.0 | Muy satisfecho |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 11.0 | NS |
| G170 | `P170` | Tiempo de anticipación entre e SMS y el corte de la luz | 12.0 | NR |
| G170 | `P171` | Disponibilidad de puntos de recarga | 1.0 | Muy insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 2.0 | Muy insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 3.0 | Insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 4.0 | Insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 7.0 | Satisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 8.0 | Satisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 9.0 | Muy satisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 10.0 | Muy satisfecho |
| G170 | `P171` | Disponibilidad de puntos de recarga | 11.0 | NS |
| G170 | `P171` | Disponibilidad de puntos de recarga | 12.0 | NR |
| G170 | `P172` | Rapidez de la llegada del SMS | 1.0 | Muy insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 2.0 | Muy insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 3.0 | Insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 4.0 | Insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 7.0 | Satisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 8.0 | Satisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 9.0 | Muy satisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 10.0 | Muy satisfecho |
| G170 | `P172` | Rapidez de la llegada del SMS | 11.0 | NS |
| G170 | `P172` | Rapidez de la llegada del SMS | 12.0 | NR |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 1.0 | Muy insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 2.0 | Muy insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 3.0 | Insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 4.0 | Insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 7.0 | Satisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 8.0 | Satisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 9.0 | Muy satisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 10.0 | Muy satisfecho |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 11.0 | NS |
| G170 | `P173` | Claridad del SMS con su consumo en kWh | 12.0 | NR |
| G170 | `P174` | Disponibilidad del sistema | 1.0 | Muy insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 2.0 | Muy insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 3.0 | Insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 4.0 | Insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P174` | Disponibilidad del sistema | 7.0 | Satisfecho |
| G170 | `P174` | Disponibilidad del sistema | 8.0 | Satisfecho |
| G170 | `P174` | Disponibilidad del sistema | 9.0 | Muy satisfecho |
| G170 | `P174` | Disponibilidad del sistema | 10.0 | Muy satisfecho |
| G170 | `P174` | Disponibilidad del sistema | 11.0 | NS |
| G170 | `P174` | Disponibilidad del sistema | 12.0 | NR |
| G170 | `P175` | Rapidez en la recarga | 1.0 | Muy insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 2.0 | Muy insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 3.0 | Insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 4.0 | Insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P175` | Rapidez en la recarga | 7.0 | Satisfecho |
| G170 | `P175` | Rapidez en la recarga | 8.0 | Satisfecho |
| G170 | `P175` | Rapidez en la recarga | 9.0 | Muy satisfecho |
| G170 | `P175` | Rapidez en la recarga | 10.0 | Muy satisfecho |
| G170 | `P175` | Rapidez en la recarga | 11.0 | NS |
| G170 | `P175` | Rapidez en la recarga | 12.0 | NR |
| G170 | `P176` | Recarga sin errores | 1.0 | Muy insatisfecho |
| G170 | `P176` | Recarga sin errores | 2.0 | Muy insatisfecho |
| G170 | `P176` | Recarga sin errores | 3.0 | Insatisfecho |
| G170 | `P176` | Recarga sin errores | 4.0 | Insatisfecho |
| G170 | `P176` | Recarga sin errores | 5.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P176` | Recarga sin errores | 6.0 | Ni satisfecho, Ni insatisfecho |
| G170 | `P176` | Recarga sin errores | 7.0 | Satisfecho |
| G170 | `P176` | Recarga sin errores | 8.0 | Satisfecho |
| G170 | `P176` | Recarga sin errores | 9.0 | Muy satisfecho |
| G170 | `P176` | Recarga sin errores | 10.0 | Muy satisfecho |
| G170 | `P176` | Recarga sin errores | 11.0 | NS |
| G170 | `P176` | Recarga sin errores | 12.0 | NR |
| G177 | `P177` | Facilidad para contactarse | 1.0 | Muy insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 2.0 | Muy insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 3.0 | Insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 4.0 | Insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P177` | Facilidad para contactarse | 7.0 | Satisfecho |
| G177 | `P177` | Facilidad para contactarse | 8.0 | Satisfecho |
| G177 | `P177` | Facilidad para contactarse | 9.0 | Muy satisfecho |
| G177 | `P177` | Facilidad para contactarse | 10.0 | Muy satisfecho |
| G177 | `P177` | Facilidad para contactarse | 11.0 | NS |
| G177 | `P177` | Facilidad para contactarse | 12.0 | NR |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 1.0 | Muy insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 2.0 | Muy insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 3.0 | Insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 4.0 | Insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 7.0 | Satisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 8.0 | Satisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 9.0 | Muy satisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 10.0 | Muy satisfecho |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 11.0 | NS |
| G177 | `P178` | Tiempo de espera hasta ser atendido | 12.0 | NR |
| G177 | `P179` | Duración del tiempo de la atención | 1.0 | Muy insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 2.0 | Muy insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 3.0 | Insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 4.0 | Insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 7.0 | Satisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 8.0 | Satisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 9.0 | Muy satisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 10.0 | Muy satisfecho |
| G177 | `P179` | Duración del tiempo de la atención | 11.0 | NS |
| G177 | `P179` | Duración del tiempo de la atención | 12.0 | NR |
| G177 | `P180` | Conocimiento sobre el tema | 1.0 | Muy insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 2.0 | Muy insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 3.0 | Insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 4.0 | Insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 7.0 | Satisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 8.0 | Satisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 9.0 | Muy satisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 10.0 | Muy satisfecho |
| G177 | `P180` | Conocimiento sobre el tema | 11.0 | NS |
| G177 | `P180` | Conocimiento sobre el tema | 12.0 | NR |
| G177 | `P181` | Claridad en la información | 1.0 | Muy insatisfecho |
| G177 | `P181` | Claridad en la información | 2.0 | Muy insatisfecho |
| G177 | `P181` | Claridad en la información | 3.0 | Insatisfecho |
| G177 | `P181` | Claridad en la información | 4.0 | Insatisfecho |
| G177 | `P181` | Claridad en la información | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P181` | Claridad en la información | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P181` | Claridad en la información | 7.0 | Satisfecho |
| G177 | `P181` | Claridad en la información | 8.0 | Satisfecho |
| G177 | `P181` | Claridad en la información | 9.0 | Muy satisfecho |
| G177 | `P181` | Claridad en la información | 10.0 | Muy satisfecho |
| G177 | `P181` | Claridad en la información | 11.0 | NS |
| G177 | `P181` | Claridad en la información | 12.0 | NR |
| G177 | `P182` | Calidad de la atención | 1.0 | Muy insatisfecho |
| G177 | `P182` | Calidad de la atención | 2.0 | Muy insatisfecho |
| G177 | `P182` | Calidad de la atención | 3.0 | Insatisfecho |
| G177 | `P182` | Calidad de la atención | 4.0 | Insatisfecho |
| G177 | `P182` | Calidad de la atención | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P182` | Calidad de la atención | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P182` | Calidad de la atención | 7.0 | Satisfecho |
| G177 | `P182` | Calidad de la atención | 8.0 | Satisfecho |
| G177 | `P182` | Calidad de la atención | 9.0 | Muy satisfecho |
| G177 | `P182` | Calidad de la atención | 10.0 | Muy satisfecho |
| G177 | `P182` | Calidad de la atención | 11.0 | NS |
| G177 | `P182` | Calidad de la atención | 12.0 | NR |
| G177 | `P183` | Plazo informado | 1.0 | Muy insatisfecho |
| G177 | `P183` | Plazo informado | 2.0 | Muy insatisfecho |
| G177 | `P183` | Plazo informado | 3.0 | Insatisfecho |
| G177 | `P183` | Plazo informado | 4.0 | Insatisfecho |
| G177 | `P183` | Plazo informado | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P183` | Plazo informado | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P183` | Plazo informado | 7.0 | Satisfecho |
| G177 | `P183` | Plazo informado | 8.0 | Satisfecho |
| G177 | `P183` | Plazo informado | 9.0 | Muy satisfecho |
| G177 | `P183` | Plazo informado | 10.0 | Muy satisfecho |
| G177 | `P183` | Plazo informado | 11.0 | NS |
| G177 | `P183` | Plazo informado | 12.0 | NR |
| G177 | `P184` | Solución definitiva del problema | 1.0 | Muy insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 2.0 | Muy insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 3.0 | Insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 4.0 | Insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P184` | Solución definitiva del problema | 7.0 | Satisfecho |
| G177 | `P184` | Solución definitiva del problema | 8.0 | Satisfecho |
| G177 | `P184` | Solución definitiva del problema | 9.0 | Muy satisfecho |
| G177 | `P184` | Solución definitiva del problema | 10.0 | Muy satisfecho |
| G177 | `P184` | Solución definitiva del problema | 11.0 | NS |
| G177 | `P184` | Solución definitiva del problema | 12.0 | NR |
| G177 | `P185` | Cumplimiento del plazo | 1.0 | Muy insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 2.0 | Muy insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 3.0 | Insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 4.0 | Insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P185` | Cumplimiento del plazo | 7.0 | Satisfecho |
| G177 | `P185` | Cumplimiento del plazo | 8.0 | Satisfecho |
| G177 | `P185` | Cumplimiento del plazo | 9.0 | Muy satisfecho |
| G177 | `P185` | Cumplimiento del plazo | 10.0 | Muy satisfecho |
| G177 | `P185` | Cumplimiento del plazo | 11.0 | NS |
| G177 | `P185` | Cumplimiento del plazo | 12.0 | NR |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 1.0 | Muy insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 2.0 | Muy insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 3.0 | Insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 4.0 | Insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 5.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 6.0 | Ni satisfecho, Ni insatisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 7.0 | Satisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 8.0 | Satisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 9.0 | Muy satisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 10.0 | Muy satisfecho |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 11.0 | NS |
| G177 | `P186` | Autonomía/ flexibilidad del empleado | 12.0 | NR |
| P187 | `P187` | Facilidad de contacto con la empresa | 1.0 | Muy mala |
| P187 | `P187` | Facilidad de contacto con la empresa | 2.0 | Mala |
| P187 | `P187` | Facilidad de contacto con la empresa | 3.0 | Regular |
| P187 | `P187` | Facilidad de contacto con la empresa | 4.0 | Buena |
| P187 | `P187` | Facilidad de contacto con la empresa | 5.0 | Muy buena |
| P187 | `P187` | Facilidad de contacto con la empresa | 6.0 | No sabe |
| P188 | `P188` | Tiempo de espera para ser atendido | 1.0 | Muy largo |
| P188 | `P188` | Tiempo de espera para ser atendido | 2.0 | Largo |
| P188 | `P188` | Tiempo de espera para ser atendido | 3.0 | Aceptable |
| P188 | `P188` | Tiempo de espera para ser atendido | 4.0 | Satisfactorio |
| P188 | `P188` | Tiempo de espera para ser atendido | 5.0 | Muy satisfactorio |
| P188 | `P188` | Tiempo de espera para ser atendido | 6.0 | No sabe |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 1.0 | Muy largo |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 2.0 | Largo |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 3.0 | Aceptable |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 4.0 | Satisfactorio |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 5.0 | Muy satisfactorio |
| P189 | `P189` | Tiempo dedicado para atender su reclamo | 6.0 | No sabe |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 1.0 | Muy malo |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 2.0 | Malo |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 3.0 | Regular |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 4.0 | Bueno |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 5.0 | Muy bueno |
| P190 | `P190` | Conocimientos de los funcionarios sobre el tema | 6.0 | No sabe |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 1.0 | Muy malas |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 2.0 | Malas |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 3.0 | Regulares |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 4.0 | Buenas |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 5.0 | Muy buenas |
| P191 | `P191` | Calidad de la información/ acciones proporcionadas | 6.0 | No sabe |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 1.0 | Muy malas |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 2.0 | Malas |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 3.0 | Regulares |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 4.0 | Buenas |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 5.0 | Muy buenas |
| P192 | `P192` | Trato, respeto y cordialidad prestada por el personal | 6.0 | No sabe |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 1.0 | Muy largo |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 2.0 | Largo |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 3.0 | Aceptable |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 4.0 | Satisfactorio |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 5.0 | Muy satisfactorio |
| P193 | `P193` | Tiempo total para solventar las solicitudes | 6.0 | No sabe |
| P194 | `P194` | Solución definitiva de los problemas | 1.0 | Nunca |
| P194 | `P194` | Solución definitiva de los problemas | 2.0 | Casi nunca |
| P194 | `P194` | Solución definitiva de los problemas | 3.0 | A veces |
| P194 | `P194` | Solución definitiva de los problemas | 4.0 | Casi siempre |
| P194 | `P194` | Solución definitiva de los problemas | 5.0 | Siempre |
| P194 | `P194` | Solución definitiva de los problemas | 6.0 | No sabe |
| P195 | `P195` | Cumplimiento de los plazos | 1.0 | Nunca |
| P195 | `P195` | Cumplimiento de los plazos | 2.0 | Casi nunca |
| P195 | `P195` | Cumplimiento de los plazos | 3.0 | A veces |
| P195 | `P195` | Cumplimiento de los plazos | 4.0 | Casi siempre |
| P195 | `P195` | Cumplimiento de los plazos | 5.0 | Siempre |
| P195 | `P195` | Cumplimiento de los plazos | 6.0 | No sabe |
| G196 | `P196` | Respeta los derechos de los clientes | 1.0 | Muy insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 2.0 | Muy insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 3.0 | Insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 4.0 | Insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 7.0 | Satisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 8.0 | Satisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 9.0 | Muy satisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 10.0 | Muy satisfecho |
| G196 | `P196` | Respeta los derechos de los clientes | 11.0 | NS |
| G196 | `P196` | Respeta los derechos de los clientes | 12.0 | NR |
| G196 | `P197` | Correcta con los clientes | 1.0 | Muy insatisfecho |
| G196 | `P197` | Correcta con los clientes | 2.0 | Muy insatisfecho |
| G196 | `P197` | Correcta con los clientes | 3.0 | Insatisfecho |
| G196 | `P197` | Correcta con los clientes | 4.0 | Insatisfecho |
| G196 | `P197` | Correcta con los clientes | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P197` | Correcta con los clientes | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P197` | Correcta con los clientes | 7.0 | Satisfecho |
| G196 | `P197` | Correcta con los clientes | 8.0 | Satisfecho |
| G196 | `P197` | Correcta con los clientes | 9.0 | Muy satisfecho |
| G196 | `P197` | Correcta con los clientes | 10.0 | Muy satisfecho |
| G196 | `P197` | Correcta con los clientes | 11.0 | NS |
| G196 | `P197` | Correcta con los clientes | 12.0 | NR |
| G196 | `P198` | Invierte para proveer energía con calidad | 1.0 | Muy insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 2.0 | Muy insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 3.0 | Insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 4.0 | Insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 7.0 | Satisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 8.0 | Satisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 9.0 | Muy satisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 10.0 | Muy satisfecho |
| G196 | `P198` | Invierte para proveer energía con calidad | 11.0 | NS |
| G196 | `P198` | Invierte para proveer energía con calidad | 12.0 | NR |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 1.0 | Muy insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 2.0 | Muy insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 3.0 | Insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 4.0 | Insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 7.0 | Satisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 8.0 | Satisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 9.0 | Muy satisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 10.0 | Muy satisfecho |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 11.0 | NS |
| G196 | `P199` | Informa a sus clientes con respecto a su actuación | 12.0 | NR |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 1.0 | Muy insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 2.0 | Muy insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 3.0 | Insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 4.0 | Insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 7.0 | Satisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 8.0 | Satisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 9.0 | Muy satisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 10.0 | Muy satisfecho |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 11.0 | NS |
| G196 | `P200` | Se ocupa de evitar hurtos de energía | 12.0 | NR |
| G196 | `P201` | Ofrece atención sin discriminación | 1.0 | Muy insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 2.0 | Muy insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 3.0 | Insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 4.0 | Insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 7.0 | Satisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 8.0 | Satisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 9.0 | Muy satisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 10.0 | Muy satisfecho |
| G196 | `P201` | Ofrece atención sin discriminación | 11.0 | NS |
| G196 | `P201` | Ofrece atención sin discriminación | 12.0 | NR |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 1.0 | Muy insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 2.0 | Muy insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 3.0 | Insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 4.0 | Insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 7.0 | Satisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 8.0 | Satisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 9.0 | Muy satisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 10.0 | Muy satisfecho |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 11.0 | NS |
| G196 | `P202` | Dispuesta a negociar con sus clientes (flexible) | 12.0 | NR |
| G196 | `P203` | Se ocupa del medio ambiente | 1.0 | Muy insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 2.0 | Muy insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 3.0 | Insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 4.0 | Insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 7.0 | Satisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 8.0 | Satisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 9.0 | Muy satisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 10.0 | Muy satisfecho |
| G196 | `P203` | Se ocupa del medio ambiente | 11.0 | NS |
| G196 | `P203` | Se ocupa del medio ambiente | 12.0 | NR |
| G196 | `P204` | Preparada para situaciones de emergencia | 1.0 | Muy insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 2.0 | Muy insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 3.0 | Insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 4.0 | Insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 7.0 | Satisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 8.0 | Satisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 9.0 | Muy satisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 10.0 | Muy satisfecho |
| G196 | `P204` | Preparada para situaciones de emergencia | 11.0 | NS |
| G196 | `P204` | Preparada para situaciones de emergencia | 12.0 | NR |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 1.0 | Muy insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 2.0 | Muy insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 3.0 | Insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 4.0 | Insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 7.0 | Satisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 8.0 | Satisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 9.0 | Muy satisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 10.0 | Muy satisfecho |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 11.0 | NS |
| G196 | `P205` | Enfoca en las necesidades de sus clientes | 12.0 | NR |
| G196 | `P206` | Invierte en modernización e innovación | 1.0 | Muy insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 2.0 | Muy insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 3.0 | Insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 4.0 | Insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 5.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 6.0 | Ni satisfecho, Ni insatisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 7.0 | Satisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 8.0 | Satisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 9.0 | Muy satisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 10.0 | Muy satisfecho |
| G196 | `P206` | Invierte en modernización e innovación | 11.0 | NS |
| G196 | `P206` | Invierte en modernización e innovación | 12.0 | NR |
| G207 | `P207` | Promoción de programas sociales | 1.0 | Muy insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 2.0 | Muy insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 3.0 | Insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 4.0 | Insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P207` | Promoción de programas sociales | 7.0 | Satisfecho |
| G207 | `P207` | Promoción de programas sociales | 8.0 | Satisfecho |
| G207 | `P207` | Promoción de programas sociales | 9.0 | Muy satisfecho |
| G207 | `P207` | Promoción de programas sociales | 10.0 | Muy satisfecho |
| G207 | `P207` | Promoción de programas sociales | 11.0 | NS |
| G207 | `P207` | Promoción de programas sociales | 12.0 | NR |
| G207 | `P208` | Promoción de acciones culturales | 1.0 | Muy insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 2.0 | Muy insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 3.0 | Insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 4.0 | Insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P208` | Promoción de acciones culturales | 7.0 | Satisfecho |
| G207 | `P208` | Promoción de acciones culturales | 8.0 | Satisfecho |
| G207 | `P208` | Promoción de acciones culturales | 9.0 | Muy satisfecho |
| G207 | `P208` | Promoción de acciones culturales | 10.0 | Muy satisfecho |
| G207 | `P208` | Promoción de acciones culturales | 11.0 | NS |
| G207 | `P208` | Promoción de acciones culturales | 12.0 | NR |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 1.0 | Muy insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 2.0 | Muy insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 3.0 | Insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 4.0 | Insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 7.0 | Satisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 8.0 | Satisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 9.0 | Muy satisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 10.0 | Muy satisfecho |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 11.0 | NS |
| G207 | `P209` | Se ocupa de la prevención de accidentes | 12.0 | NR |
| G207 | `P210` | Lleva energía a regiones no atendidas | 1.0 | Muy insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 2.0 | Muy insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 3.0 | Insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 4.0 | Insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 7.0 | Satisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 8.0 | Satisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 9.0 | Muy satisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 10.0 | Muy satisfecho |
| G207 | `P210` | Lleva energía a regiones no atendidas | 11.0 | NS |
| G207 | `P210` | Lleva energía a regiones no atendidas | 12.0 | NR |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 1.0 | Muy insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 2.0 | Muy insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 3.0 | Insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 4.0 | Insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 7.0 | Satisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 8.0 | Satisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 9.0 | Muy satisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 10.0 | Muy satisfecho |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 11.0 | NS |
| G207 | `P211` | Contribuye para el desarrollo econ. de la ciudad | 12.0 | NR |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 1.0 | Muy insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 2.0 | Muy insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 3.0 | Insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 4.0 | Insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 7.0 | Satisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 8.0 | Satisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 9.0 | Muy satisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 10.0 | Muy satisfecho |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 11.0 | NS |
| G207 | `P212` | Facilita el acceso de ciudadanos con neces. espec. | 12.0 | NR |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 1.0 | Muy insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 2.0 | Muy insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 3.0 | Insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 4.0 | Insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 5.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 6.0 | Ni satisfecho, Ni insatisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 7.0 | Satisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 8.0 | Satisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 9.0 | Muy satisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 10.0 | Muy satisfecho |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 11.0 | NS |
| G207 | `P213` | Honesta/ cumple con sus obligaciones | 12.0 | NR |
| P214 | `P214` | Participó en programa social/ cultural ofrecido por la distribuidora | 1.0 | Sí |
| P214 | `P214` | Participó en programa social/ cultural ofrecido por la distribuidora | 2.0 | No |
| P214 | `P214` | Participó en programa social/ cultural ofrecido por la distribuidora | 3.0 | NS |
| P214 | `P214` | Participó en programa social/ cultural ofrecido por la distribuidora | 4.0 | NR |
| P215 | `P215` | Garantiza igualdad de oportunidades y trato entre mujeres y hombres | 1.0 | Sí |
| P215 | `P215` | Garantiza igualdad de oportunidades y trato entre mujeres y hombres | 2.0 | No |
| P215 | `P215` | Garantiza igualdad de oportunidades y trato entre mujeres y hombres | 3.0 | NS |
| P215 | `P215` | Garantiza igualdad de oportunidades y trato entre mujeres y hombres | 4.0 | NR |
| P216 | `P216` | Beneficiarios de programas sociales relacionados a la energía | 1.0 | Sí |
| P216 | `P216` | Beneficiarios de programas sociales relacionados a la energía | 2.0 | No |
| P216 | `P216` | Beneficiarios de programas sociales relacionados a la energía | 3.0 | NS |
| P216 | `P216` | Beneficiarios de programas sociales relacionados a la energía | 4.0 | NR |
| P217 | `P217` | Servicio de energía afectado por conflictos sociales | 1.0 | Sí |
| P217 | `P217` | Servicio de energía afectado por conflictos sociales | 2.0 | No |
| P217 | `P217` | Servicio de energía afectado por conflictos sociales | 3.0 | NS |
| P217 | `P217` | Servicio de energía afectado por conflictos sociales | 4.0 | NR |
| P218 | `P218` | Tenencia de auto en el hogar | 1.0 | No tiene y no va a comprar |
| P218 | `P218` | Tenencia de auto en el hogar | 2.0 | No tiene y va a comprar uno a combustión |
| P218 | `P218` | Tenencia de auto en el hogar | 3.0 | No tiene y va a comprar uno eléctrico |
| P218 | `P218` | Tenencia de auto en el hogar | 4.0 | Tiene uno a combustión y no va a cambiarlo |
| P218 | `P218` | Tenencia de auto en el hogar | 5.0 | Tiene uno a combustión y va a cambiarlo por otro |
| P218 | `P218` | Tenencia de auto en el hogar | 6.0 | Tiene uno a combustión y va cambiarlo por eléctrico |
| P218 | `P218` | Tenencia de auto en el hogar | 7.0 | Tiene auto eléctrico |
| P218 | `P218` | Tenencia de auto en el hogar | 8.0 | Tiene auto híbrido (combustión y eléctrico) |
| P218 | `P218` | Tenencia de auto en el hogar | 9.0 | Ninguna de las opciones |
| G219 | `P219` | Alto costo del vehículo | 1.0 | Mencionó |
| G219 | `P219` | Alto costo del vehículo | 2.0 | No mencionó |
| G219 | `P220` | Recorre pocos km al mes | 1.0 | Mencionó |
| G219 | `P220` | Recorre pocos km al mes | 2.0 | No mencionó |
| G219 | `P221` | No puede cargarlo en su domicilio | 1.0 | Mencionó |
| G219 | `P221` | No puede cargarlo en su domicilio | 2.0 | No mencionó |
| G219 | `P222` | Alto costo de la energía eléctrica | 1.0 | Mencionó |
| G219 | `P222` | Alto costo de la energía eléctrica | 2.0 | No mencionó |
| G219 | `P223` | No hay cargadores públicos cerca | 1.0 | Mencionó |
| G219 | `P223` | No hay cargadores públicos cerca | 2.0 | No mencionó |
| G219 | `P224` | Recorre muchos km y teme quedarse sin carga | 1.0 | Mencionó |
| G219 | `P224` | Recorre muchos km y teme quedarse sin carga | 2.0 | No mencionó |
| G219 | `P226` | NS | 1.0 | Mencionó |
| G219 | `P226` | NS | 2.0 | No mencionó |
| G219 | `P227` | NR | 1.0 | Mencionó |
| G219 | `P227` | NR | 2.0 | No mencionó |
| P228 | `P228` | Satisfacción intermedia | 1.0 | Muy insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 2.0 | Muy insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 3.0 | Insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 4.0 | Insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 5.0 | Ni satisfecho, Ni insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 6.0 | Ni satisfecho, Ni insatisfecho |
| P228 | `P228` | Satisfacción intermedia | 7.0 | Satisfecho |
| P228 | `P228` | Satisfacción intermedia | 8.0 | Satisfecho |
| P228 | `P228` | Satisfacción intermedia | 9.0 | Muy satisfecho |
| P228 | `P228` | Satisfacción intermedia | 10.0 | Muy satisfecho |
| P228 | `P228` | Satisfacción intermedia | 11.0 | NS |
| P228 | `P228` | Satisfacción intermedia | 12.0 | NR |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 1.0 | Empeorando mucho |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 2.0 | Empeorando mucho |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 3.0 | Empeorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 4.0 | Empeorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 5.0 | Ni mejorando, Ni empeorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 6.0 | Ni mejorando, Ni empeorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 7.0 | Mejorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 8.0 | Mejorando |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 9.0 | Mejorando mucho |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 10.0 | Mejorando mucho |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 11.0 | NS |
| P232 | `P232` | Percepción sobre la trayectoria de los servicios | 12.0 | NR |
| P234 | `P234` | Precio de la factura | 1.0 | Muy caro/ muy costoso |
| P234 | `P234` | Precio de la factura | 2.0 | Muy caro/ muy costoso |
| P234 | `P234` | Precio de la factura | 3.0 | Caro/ costoso |
| P234 | `P234` | Precio de la factura | 4.0 | Caro/ costoso |
| P234 | `P234` | Precio de la factura | 5.0 | Ni caro/ costoso, Ni barato/ económico |
| P234 | `P234` | Precio de la factura | 6.0 | Ni caro/ costoso, Ni barato/ económico |
| P234 | `P234` | Precio de la factura | 7.0 | Barato/ económico |
| P234 | `P234` | Precio de la factura | 8.0 | Barato/ económico |
| P234 | `P234` | Precio de la factura | 9.0 | Muy barato/ muy económico |
| P234 | `P234` | Precio de la factura | 10.0 | Muy barato/ muy económico |
| P234 | `P234` | Precio de la factura | 11.0 | NS |
| P234 | `P234` | Precio de la factura | 12.0 | NR |
| P235 | `P235` | Percepción de justicia del precio de la energía | -99.0 | NR |
| P235 | `P235` | Percepción de justicia del precio de la energía | -88.0 | NS |
| P235 | `P235` | Percepción de justicia del precio de la energía | 1.0 | Es justo |
| P235 | `P235` | Percepción de justicia del precio de la energía | 2.0 | No es justo |
| P237 | `P237` | Precio comparado a la calidad del suministro | 1.0 | Muy caro |
| P237 | `P237` | Precio comparado a la calidad del suministro | 2.0 | Muy caro |
| P237 | `P237` | Precio comparado a la calidad del suministro | 3.0 | Caro |
| P237 | `P237` | Precio comparado a la calidad del suministro | 4.0 | Caro |
| P237 | `P237` | Precio comparado a la calidad del suministro | 5.0 | Ni caro, ni barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 6.0 | Ni caro, ni barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 7.0 | Barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 8.0 | Barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 9.0 | Muy barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 10.0 | Muy barato |
| P237 | `P237` | Precio comparado a la calidad del suministro | 11.0 | NS |
| P237 | `P237` | Precio comparado a la calidad del suministro | 12.0 | NR |
| P238 | `P238` | Satisfacción general | 1.0 | Muy insatisfecho |
| P238 | `P238` | Satisfacción general | 2.0 | Muy insatisfecho |
| P238 | `P238` | Satisfacción general | 3.0 | Insatisfecho |
| P238 | `P238` | Satisfacción general | 4.0 | Insatisfecho |
| P238 | `P238` | Satisfacción general | 5.0 | Ni satisfecho, Ni insatisfecho |
| P238 | `P238` | Satisfacción general | 6.0 | Ni satisfecho, Ni insatisfecho |
| P238 | `P238` | Satisfacción general | 7.0 | Satisfecho |
| P238 | `P238` | Satisfacción general | 8.0 | Satisfecho |
| P238 | `P238` | Satisfacción general | 9.0 | Muy satisfecho |
| P238 | `P238` | Satisfacción general | 10.0 | Muy satisfecho |
| P238 | `P238` | Satisfacción general | 11.0 | NS |
| P238 | `P238` | Satisfacción general | 12.0 | NR |
| P239 | `P239` | NPS - Net Promoter Score | 0.0 | Nada probable |
| P239 | `P239` | NPS - Net Promoter Score | 1.0 | 1 |
| P239 | `P239` | NPS - Net Promoter Score | 2.0 | 2 |
| P239 | `P239` | NPS - Net Promoter Score | 3.0 | 3 |
| P239 | `P239` | NPS - Net Promoter Score | 4.0 | 4 |
| P239 | `P239` | NPS - Net Promoter Score | 5.0 | 5 |
| P239 | `P239` | NPS - Net Promoter Score | 6.0 | 6 |
| P239 | `P239` | NPS - Net Promoter Score | 7.0 | 7 |
| P239 | `P239` | NPS - Net Promoter Score | 8.0 | 8 |
| P239 | `P239` | NPS - Net Promoter Score | 9.0 | 9 |
| P239 | `P239` | NPS - Net Promoter Score | 10.0 | Muy probable |
| P239 | `P239` | NPS - Net Promoter Score | 11.0 | NS |
| P239 | `P239` | NPS - Net Promoter Score | 12.0 | NR |
| P240 | `P240` | Contacto con la distribuidora | 1.0 | Sí, hizo contacto |
| P240 | `P240` | Contacto con la distribuidora | 2.0 | No hizo contacto |
| P241 | `P241` | Otros contactos además de pago de la factura | 1.0 | Sí, tuvo otros contactos |
| P241 | `P241` | Otros contactos además de pago de la factura | 2.0 | No tuvo otros contactos |
| G242 | `P242` | Para pagar la factura de energía | 1.0 | Sí |
| G242 | `P242` | Para pagar la factura de energía | 2.0 | No |
| G242 | `P243` | Falta de energía | 1.0 | Sí |
| G242 | `P243` | Falta de energía | 2.0 | No |
| G242 | `P244` | Copia de la factura | 1.0 | Sí |
| G242 | `P244` | Copia de la factura | 2.0 | No |
| G242 | `P245` | Realizar cambios en el catastro | 1.0 | Sí |
| G242 | `P245` | Realizar cambios en el catastro | 2.0 | No |
| G242 | `P246` | Negociar facturas en retraso | 1.0 | Sí |
| G242 | `P246` | Negociar facturas en retraso | 2.0 | No |
| G242 | `P247` | Accidente/ mal funcionamiento de la red | 1.0 | Sí |
| G242 | `P247` | Accidente/ mal funcionamiento de la red | 2.0 | No |
| G242 | `P248` | Reclamo (Alumbrado Público) | 1.0 | Sí |
| G242 | `P248` | Reclamo (Alumbrado Público) | 2.0 | No |
| G242 | `P249` | Información sobre puntos de pago | 1.0 | Sí |
| G242 | `P249` | Información sobre puntos de pago | 2.0 | No |
| G242 | `P250` | Problema con la factura | 1.0 | Sí |
| G242 | `P250` | Problema con la factura | 2.0 | No |
| G242 | `P251` | Cobro indebido | 1.0 | Sí |
| G242 | `P251` | Cobro indebido | 2.0 | No |
| G242 | `P252` | Corte de energía | 1.0 | Sí |
| G242 | `P252` | Corte de energía | 2.0 | No |
| G242 | `P253` | Daño en aparato electrónico | 1.0 | Sí |
| G242 | `P253` | Daño en aparato electrónico | 2.0 | No |
| G242 | `P254` | Consultar interrupciones programadas | 1.0 | Sí |
| G242 | `P254` | Consultar interrupciones programadas | 2.0 | No |
| G242 | `P255` | Solicitar información | 1.0 | Sí |
| G242 | `P255` | Solicitar información | 2.0 | No |
| G242 | `P256` | Realización de servicio | 1.0 | Sí |
| G242 | `P256` | Realización de servicio | 2.0 | No |
| G242 | `P257` | Acompañar pedido | 1.0 | Sí |
| G242 | `P257` | Acompañar pedido | 2.0 | No |
| G242 | `P258` | Reclamo (retraso en el servicio) | 1.0 | Sí |
| G242 | `P258` | Reclamo (retraso en el servicio) | 2.0 | No |
| G242 | `P259` | Reclamo (servicio mal realizado) | 1.0 | Sí |
| G242 | `P259` | Reclamo (servicio mal realizado) | 2.0 | No |
| G242 | `P261` | No sabe | 1.0 | Sí |
| G242 | `P261` | No sabe | 2.0 | No |
| G242 | `P262` | No respondió | 1.0 | Sí |
| G242 | `P262` | No respondió | 2.0 | No |
| P263 | `P263` | Solución en el primer contacto | 1.0 | Primer contacto |
| P263 | `P263` | Solución en el primer contacto | 2.0 | Más de un contacto |
| P263 | `P263` | Solución en el primer contacto | 3.0 | Algunos al primer contacto, otros con más de un contacto |
| P263 | `P263` | Solución en el primer contacto | 4.0 | NS |
| P264 | `P264` | Facilidad para relacionarse | 1.0 | Muy difícil |
| P264 | `P264` | Facilidad para relacionarse | 2.0 | Difícil |
| P264 | `P264` | Facilidad para relacionarse | 3.0 | Ni fácil ni difícil |
| P264 | `P264` | Facilidad para relacionarse | 4.0 | Fácil |
| P264 | `P264` | Facilidad para relacionarse | 5.0 | Muy fácil |
| P264 | `P264` | Facilidad para relacionarse | 6.0 | NS/ NR |
| P267 | `P267` | Satisfacción con canales digitales | 1.0 | Muy insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 2.0 | Muy insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 3.0 | Insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 4.0 | Insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 5.0 | Ni satisfecho, Ni insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 6.0 | Ni satisfecho, Ni insatisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 7.0 | Satisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 8.0 | Satisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 9.0 | Muy satisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 10.0 | Muy satisfecho |
| P267 | `P267` | Satisfacción con canales digitales | 11.0 | NS |
| P267 | `P267` | Satisfacción con canales digitales | 12.0 | NR |
| P272 | `P272` | Mencionó canal digital | 1.0 | Sí |
| P272 | `P272` | Mencionó canal digital | 2.0 | No |
| G274 | `P274` | Disponible en todo el municipio | 1.0 | Muy insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 2.0 | Muy insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 3.0 | Insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 4.0 | Insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 5.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 6.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P274` | Disponible en todo el municipio | 7.0 | Satisfecho |
| G274 | `P274` | Disponible en todo el municipio | 8.0 | Satisfecho |
| G274 | `P274` | Disponible en todo el municipio | 9.0 | Muy satisfecho |
| G274 | `P274` | Disponible en todo el municipio | 10.0 | Muy satisfecho |
| G274 | `P274` | Disponible en todo el municipio | 11.0 | NS |
| G274 | `P274` | Disponible en todo el municipio | 12.0 | NR |
| G274 | `P275` | Calidad del alumbrado público | 1.0 | Muy insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 2.0 | Muy insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 3.0 | Insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 4.0 | Insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 5.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 6.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P275` | Calidad del alumbrado público | 7.0 | Satisfecho |
| G274 | `P275` | Calidad del alumbrado público | 8.0 | Satisfecho |
| G274 | `P275` | Calidad del alumbrado público | 9.0 | Muy satisfecho |
| G274 | `P275` | Calidad del alumbrado público | 10.0 | Muy satisfecho |
| G274 | `P275` | Calidad del alumbrado público | 11.0 | NS |
| G274 | `P275` | Calidad del alumbrado público | 12.0 | NR |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 1.0 | Muy insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 2.0 | Muy insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 3.0 | Insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 4.0 | Insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 5.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 6.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 7.0 | Satisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 8.0 | Satisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 9.0 | Muy satisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 10.0 | Muy satisfecho |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 11.0 | NS |
| G274 | `P276` | Mantenimiento del alumbrado público en calles, avenidas | 12.0 | NR |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 1.0 | Muy insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 2.0 | Muy insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 3.0 | Insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 4.0 | Insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 5.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 6.0 | Ni satisfecho, Ni insatisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 7.0 | Satisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 8.0 | Satisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 9.0 | Muy satisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 10.0 | Muy satisfecho |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 11.0 | NS |
| G274 | `P277` | Mantenimiento del alumbrado público en plazas, parques, etc | 12.0 | NR |
| P278 | `P278` | Número de luminarias de alumbrado público | 1.0 | Muy escasas |
| P278 | `P278` | Número de luminarias de alumbrado público | 2.0 | Escasas |
| P278 | `P278` | Número de luminarias de alumbrado público | 3.0 | Aceptables |
| P278 | `P278` | Número de luminarias de alumbrado público | 4.0 | Satisfactorias |
| P278 | `P278` | Número de luminarias de alumbrado público | 5.0 | Muy satisfactorias |
| P278 | `P278` | Número de luminarias de alumbrado público | 6.0 | No sabe |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 1.0 | Muy lento |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 2.0 | Lento |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 3.0 | Aceptable |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 4.0 | Rápido |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 5.0 | Muy rápido |
| P279 | `P279` | Tiempo entre solicitud de revisión del AP hasta la resolución | 6.0 | No sabe |
| P280 | `P280` | Percepción sobre el servicio de AP | 1.0 | Muy insatisfactorio |
| P280 | `P280` | Percepción sobre el servicio de AP | 2.0 | Insatisfactorio |
| P280 | `P280` | Percepción sobre el servicio de AP | 3.0 | Aceptable |
| P280 | `P280` | Percepción sobre el servicio de AP | 4.0 | Satisfactorio |
| P280 | `P280` | Percepción sobre el servicio de AP | 5.0 | Muy satisfactorio |
| P280 | `P280` | Percepción sobre el servicio de AP | 6.0 | No sabe |
| P281 | `P281` | Responsable por el alumbrado público | 1.0 | La municipalidad |
| P281 | `P281` | Responsable por el alumbrado público | 2.0 | La distribuidora |
| P281 | `P281` | Responsable por el alumbrado público | 3.0 | Otro |
| P281 | `P281` | Responsable por el alumbrado público | 4.0 | No respondió/ No sabe |
| P282 | `P282` | Número de personas que viven en el domicilio | -99.0 | No respondió |
| P283 | `P283` | Ingreso familiar | -99.0 | No respondió |
| P283 | `P283` | Ingreso familiar | -88.0 | No Sabe |
| P284 | `P284` | Confirmación del ingreso familiar | 1.0 | @FRANJA_INGRESO_1@ |
| P284 | `P284` | Confirmación del ingreso familiar | 2.0 | @FRANJA_INGRESO_2@ |
| P284 | `P284` | Confirmación del ingreso familiar | 3.0 | @FRANJA_INGRESO_3@ |
| P284 | `P284` | Confirmación del ingreso familiar | 4.0 | @FRANJA_INGRESO_4@ |
| P284 | `P284` | Confirmación del ingreso familiar | 5.0 | @FRANJA_INGRESO_5@ |
| P284 | `P284` | Confirmación del ingreso familiar | 6.0 | @FRANJA_INGRESO_6@ |
| P284 | `P284` | Confirmación del ingreso familiar | 7.0 | @FRANJA_INGRESO_7@ |
| P284 | `P284` | Confirmación del ingreso familiar | 8.0 | @FRANJA_INGRESO_8@ |
| P284 | `P284` | Confirmación del ingreso familiar | 9.0 | @FRANJA_INGRESO_9@ |
| P284 | `P284` | Confirmación del ingreso familiar | 10.0 | @FRANJA_INGRESO_10@ |
| P284 | `P284` | Confirmación del ingreso familiar | 11.0 | @FRANJA_INGRESO_11@ |
| P284 | `P284` | Confirmación del ingreso familiar | 12.0 | @FRANJA_INGRESO_12@ |
| P284 | `P284` | Confirmación del ingreso familiar | 13.0 | @FRANJA_INGRESO_13@ |
| P284 | `P284` | Confirmación del ingreso familiar | 14.0 | @FRANJA_INGRESO_14@ |
| P284 | `P284` | Confirmación del ingreso familiar | 15.0 | @FRANJA_INGRESO_15@ |
| P284 | `P284` | Confirmación del ingreso familiar | 16.0 | @FRANJA_INGRESO_16@ |
| P284 | `P284` | Confirmación del ingreso familiar | 17.0 | @FRANJA_INGRESO_17@ |
| P284 | `P284` | Confirmación del ingreso familiar | 18.0 | @FRANJA_INGRESO_18@ |
| P284 | `P284` | Confirmación del ingreso familiar | 19.0 | @FRANJA_INGRESO_19@ |
| P284 | `P284` | Confirmación del ingreso familiar | 20.0 | @FRANJA_INGRESO_20@ |
| P284 | `P284` | Confirmación del ingreso familiar | 21.0 | No sabe |
| P284 | `P284` | Confirmación del ingreso familiar | 22.0 | No Respondió |
| P285 | `P285` | Género | 1.0 | Masculino |
| P285 | `P285` | Género | 2.0 | Femenino |
| P286 | `P286` | Ocupación | 1.0 | Jubilado/ pensionado |
| P286 | `P286` | Ocupación | 2.0 | Autónomo |
| P286 | `P286` | Ocupación | 3.0 | Desempleado |
| P286 | `P286` | Ocupación | 4.0 | Ama de casa |
| P286 | `P286` | Ocupación | 5.0 | Empleado de hogar diario o mensual |
| P286 | `P286` | Ocupación | 6.0 | Empleado de empresa privada |
| P286 | `P286` | Ocupación | 7.0 | Empresario |
| P286 | `P286` | Ocupación | 8.0 | Emprendedor/ microempresario |
| P286 | `P286` | Ocupación | 9.0 | Estudiante/ becario |
| P286 | `P286` | Ocupación | 10.0 | Funcionario público |
| P286 | `P286` | Ocupación | 11.0 | Militar/ Fuerza Pública |
| P286 | `P286` | Ocupación | 12.0 | Servicios religiosos o asistenciales |
| P286 | `P286` | Ocupación | 13.0 | Profesional independiente |
| P286 | `P286` | Ocupación | 14.0 | Propietario rural |
| P286 | `P286` | Ocupación | 15.0 | Trabajador rural |
| P286 | `P286` | Ocupación | 16.0 | Otra actividad |
| P286 | `P286` | Ocupación | 17.0 | No respondió |
| G303 | `P303` | 1º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P303` | 1º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P303` | 1º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P303` | 1º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P303` | 1º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P303` | 1º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P303` | 1º puesto | 7.0 | Recarga sin errores |
| G303 | `P304` | 2º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P304` | 2º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P304` | 2º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P304` | 2º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P304` | 2º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P304` | 2º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P304` | 2º puesto | 7.0 | Recarga sin errores |
| G303 | `P305` | 3º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P305` | 3º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P305` | 3º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P305` | 3º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P305` | 3º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P305` | 3º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P305` | 3º puesto | 7.0 | Recarga sin errores |
| G303 | `P306` | 4º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P306` | 4º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P306` | 4º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P306` | 4º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P306` | 4º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P306` | 4º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P306` | 4º puesto | 7.0 | Recarga sin errores |
| G303 | `P307` | 5º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P307` | 5º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P307` | 5º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P307` | 5º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P307` | 5º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P307` | 5º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P307` | 5º puesto | 7.0 | Recarga sin errores |
| G303 | `P308` | 6º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P308` | 6º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P308` | 6º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P308` | 6º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P308` | 6º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P308` | 6º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P308` | 6º puesto | 7.0 | Recarga sin errores |
| G303 | `P309` | 7º puesto | 1.0 | Tiempo de anticipación entre e SMS y el corte de la luz |
| G303 | `P309` | 7º puesto | 2.0 | Disponibilidad de puntos de recarga |
| G303 | `P309` | 7º puesto | 3.0 | Rapidez de la llegada del SMS |
| G303 | `P309` | 7º puesto | 4.0 | Claridad del SMS con su consumo en kWh |
| G303 | `P309` | 7º puesto | 5.0 | Disponibilidad del sistema |
| G303 | `P309` | 7º puesto | 6.0 | Rapidez en la recarga |
| G303 | `P309` | 7º puesto | 7.0 | Recarga sin errores |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 1.0 | Muy baja importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 2.0 | Muy baja importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 3.0 | Baja importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 4.0 | Baja importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 5.0 | Importancia Mediana |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 6.0 | Importancia Mediana |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 7.0 | Alta importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 8.0 | Alta importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 9.0 | Muy alta importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 10.0 | Muy alta importancia |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 11.0 | NS |
| G310 | `P310` | Tiempo de anticipación entre e SMS y el corte de la luz | 12.0 | NR |
| G310 | `P311` | Disponibilidad de puntos de recarga | 1.0 | Muy baja importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 2.0 | Muy baja importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 3.0 | Baja importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 4.0 | Baja importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 5.0 | Importancia Mediana |
| G310 | `P311` | Disponibilidad de puntos de recarga | 6.0 | Importancia Mediana |
| G310 | `P311` | Disponibilidad de puntos de recarga | 7.0 | Alta importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 8.0 | Alta importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 9.0 | Muy alta importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 10.0 | Muy alta importancia |
| G310 | `P311` | Disponibilidad de puntos de recarga | 11.0 | NS |
| G310 | `P311` | Disponibilidad de puntos de recarga | 12.0 | NR |
| G310 | `P312` | Rapidez de la llegada del SMS | 1.0 | Muy baja importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 2.0 | Muy baja importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 3.0 | Baja importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 4.0 | Baja importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 5.0 | Importancia Mediana |
| G310 | `P312` | Rapidez de la llegada del SMS | 6.0 | Importancia Mediana |
| G310 | `P312` | Rapidez de la llegada del SMS | 7.0 | Alta importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 8.0 | Alta importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 9.0 | Muy alta importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 10.0 | Muy alta importancia |
| G310 | `P312` | Rapidez de la llegada del SMS | 11.0 | NS |
| G310 | `P312` | Rapidez de la llegada del SMS | 12.0 | NR |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 1.0 | Muy baja importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 2.0 | Muy baja importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 3.0 | Baja importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 4.0 | Baja importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 5.0 | Importancia Mediana |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 6.0 | Importancia Mediana |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 7.0 | Alta importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 8.0 | Alta importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 9.0 | Muy alta importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 10.0 | Muy alta importancia |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 11.0 | NS |
| G310 | `P313` | Claridad del SMS con su consumo en kWh | 12.0 | NR |
| G310 | `P314` | Disponibilidad del sistema | 1.0 | Muy baja importancia |
| G310 | `P314` | Disponibilidad del sistema | 2.0 | Muy baja importancia |
| G310 | `P314` | Disponibilidad del sistema | 3.0 | Baja importancia |
| G310 | `P314` | Disponibilidad del sistema | 4.0 | Baja importancia |
| G310 | `P314` | Disponibilidad del sistema | 5.0 | Importancia Mediana |
| G310 | `P314` | Disponibilidad del sistema | 6.0 | Importancia Mediana |
| G310 | `P314` | Disponibilidad del sistema | 7.0 | Alta importancia |
| G310 | `P314` | Disponibilidad del sistema | 8.0 | Alta importancia |
| G310 | `P314` | Disponibilidad del sistema | 9.0 | Muy alta importancia |
| G310 | `P314` | Disponibilidad del sistema | 10.0 | Muy alta importancia |
| G310 | `P314` | Disponibilidad del sistema | 11.0 | NS |
| G310 | `P314` | Disponibilidad del sistema | 12.0 | NR |
| G310 | `P315` | Rapidez en la recarga | 1.0 | Muy baja importancia |
| G310 | `P315` | Rapidez en la recarga | 2.0 | Muy baja importancia |
| G310 | `P315` | Rapidez en la recarga | 3.0 | Baja importancia |
| G310 | `P315` | Rapidez en la recarga | 4.0 | Baja importancia |
| G310 | `P315` | Rapidez en la recarga | 5.0 | Importancia Mediana |
| G310 | `P315` | Rapidez en la recarga | 6.0 | Importancia Mediana |
| G310 | `P315` | Rapidez en la recarga | 7.0 | Alta importancia |
| G310 | `P315` | Rapidez en la recarga | 8.0 | Alta importancia |
| G310 | `P315` | Rapidez en la recarga | 9.0 | Muy alta importancia |
| G310 | `P315` | Rapidez en la recarga | 10.0 | Muy alta importancia |
| G310 | `P315` | Rapidez en la recarga | 11.0 | NS |
| G310 | `P315` | Rapidez en la recarga | 12.0 | NR |
| G310 | `P316` | Recarga sin errores | 1.0 | Muy baja importancia |
| G310 | `P316` | Recarga sin errores | 2.0 | Muy baja importancia |
| G310 | `P316` | Recarga sin errores | 3.0 | Baja importancia |
| G310 | `P316` | Recarga sin errores | 4.0 | Baja importancia |
| G310 | `P316` | Recarga sin errores | 5.0 | Importancia Mediana |
| G310 | `P316` | Recarga sin errores | 6.0 | Importancia Mediana |
| G310 | `P316` | Recarga sin errores | 7.0 | Alta importancia |
| G310 | `P316` | Recarga sin errores | 8.0 | Alta importancia |
| G310 | `P316` | Recarga sin errores | 9.0 | Muy alta importancia |
| G310 | `P316` | Recarga sin errores | 10.0 | Muy alta importancia |
| G310 | `P316` | Recarga sin errores | 11.0 | NS |
| G310 | `P316` | Recarga sin errores | 12.0 | NR |