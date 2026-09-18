# Mapa de equivalencia de §17.1 — de la numeración anterior a la v1.15 (final)

> **Para qué existe.** El ciclo de reestructuración del 2026-09-01 al 09-03 llevó §17.1 de **109 a
> 37 títulos**. Todas las actas, ajustes y decisiones anteriores (`ajustes/02`, las actas de los
> pases 1 a 6, `90g`, el kit, `operacion/*`) citan la numeración vieja, que en la mayoría de los
> casos **ya no existe**. Esta es la tabla de traducción. **No se edita el material histórico**
> (regla del repo): se lee con este mapa al lado.
>
> Documento vigente: `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.15.docx`
> · texto extraído: [`../90f-etapa2-texto-extraido.md`](../../archivado/90f-etapa2-texto-extraido.md).

## 1. Estructura final (v1.15) — 37 títulos

| # | Sección | Tablas propias |
|---|---|---|
| 17.1 | Consolidación metodológica del protocolo experimental | — |
| 17.1.1 | Función y alcance de la consolidación metodológica | — |
| 17.1.2 | Alcance experimental consolidado del prototipo → **.1** Catálogo de condiciones de riesgo y alcance de validación | — |
| 17.1.3 | Diseño metodológico general y lógica de escenarios → **.1** Patrón de riesgo como unidad de análisis · **.2** Cadena operativa mínima y motor de patrones · **.3** Escenarios de evaluación · **.4** Decisiones estructurales | 16 |
| 17.1.4 | Entorno experimental, infraestructura y escenarios → **.1** Infraestructura y roles de ejecución · **.2** Escenarios de evaluación | 17 |
| 17.1.5 | Condiciones de riesgo, patrones y protocolo de prompts → **.1** Catálogo y evaluabilidad · **.2** Patrones y criterios de activación · **.3** Diseño de prompts OVD · **.4** Protocolo de evaluación y congelamiento | 20, 21 |
| 17.1.6 | Estrategia de datos, benchmarks y partición → **.1** Alcance y criterios · **.2** Fuentes de gestión directa, cobertura y brechas · **.3** Asignación de roles y partición · **.4** Benchmarks de referencia para seguimiento · **.5** Licencias, ética y logística | 22–27 |
| 17.1.7 | Framework de métricas, viabilidad operativa y presupuesto → **.1** Propósito, alcance y principio de aplicabilidad · **.2** Niveles de evaluación y jerarquía de evidencia · **.3** Métricas adoptadas y reglas de lectura · **.4** Comparación línea base vs variante ajustada · **.5** Presupuesto temporal y referencias por severidad · **.6** Instrumentación, aplicabilidad y reporte | 28, 29, 30 |
| 17.1.8 | Protocolo experimental integrado *(sin subsecciones)* | 33 |
| 17.1.9 | Estrategia de adaptación al dominio *(sin subsecciones)* | 34 |
| 17.1.10 | Supuestos, riesgos de validez y consideraciones ético-legales *(sin subsecciones)* | 35 |
| 17.1.11 | Conclusiones parciales de la consolidación metodológica *(sin subsecciones)* | — |
| Anexo C | Prompts, datos, datasets, benchmarks y logística | C.1, C.2, C.3 |
| Anexo D | Métricas, instrumentación y bitácora experimental | D.1, D.2, D.3 |

## 2. Traducción de la numeración vieja

| Numeración anterior (v1.8 y previas) | Hoy | Nota |
|---|---|---|
| 17.1.2.1 … 17.1.2.4 | **17.1.2.1** | fusionadas por GPT en la v1.9 |
| 17.1.4.1 … 17.1.4.3 | **17.1.4.1** | infraestructura y roles |
| 17.1.4.4, 17.1.4.4.1, **17.1.4.4.2** | **17.1.4.2** | escenarios DBE/EBE; acá vive ahora la cita a la **Tabla C.2** |
| 17.1.5.1 … 17.1.5.1.x | **17.1.5.1** | catálogo y evaluabilidad |
| 17.1.5.2, 17.1.5.3.x | **17.1.5.2** | patrones, severidad, persistencia, histéresis |
| 17.1.5.4, **17.1.5.4.2**, 17.1.5.4.3 | **17.1.5.3** | diseño de prompts; **acá nacen E-DIR / E-IND / E-HYB** (D-E2-2) |
| **17.1.5.4.4**, 17.1.5.4.5, 17.1.5.5 | **17.1.5.4** | protocolo de cinco fases y congelamiento; cita a la **Tabla C.1** |
| 17.1.6.1.1, 17.1.6.1.2, 17.1.6.1.3 | **17.1.6.1** | alcance, categorías y criterios C1–C7 |
| **17.1.6.2.1**, .2.2, .2.3, .2.5, .2.6, .2.8 | **17.1.6.2** | fuentes retenidas y descartadas, cobertura, brechas |
| 17.1.6.2.4, **17.1.6.2.7** | **17.1.6.3** | roles, partición, rango 500–2.000 |
| 17.1.6.3, .3.1, .3.2 | **17.1.6.4** | MOT17 y OVT-B |
| 17.1.6.4, .4.1, **17.1.6.4.2**, 17.1.6.5 | **17.1.6.5** | licencias, ética y logística |
| 17.1.7.1, **17.1.7.1.1**, 17.1.7.3.2, 17.1.7.3.3 | **17.1.7.1** | propósito, estados, **niveles de compromiso** y factibilidad |
| 17.1.7.2 *(alcance evaluativo)*, **17.1.7.3.1** | **17.1.7.2** | niveles de evidencia y Tabla 28 |
| **17.1.7.4.1**, **17.1.7.4.2**, .4.3, 17.1.7.5.x, **17.1.7.8.3** | **17.1.7.3** | métricas adoptadas y reglas de lectura |
| 17.1.7.6 | **17.1.7.4** | comparación zero-shot vs ajustada |
| 17.1.7.7, .7.1 … **17.1.7.7.5** | **17.1.7.5** | presupuesto temporal, Tablas 29 y 30 |
| 17.1.7.8, .8.1, .8.2, **17.1.7.8.4**, **17.1.7.9** | **17.1.7.6** | instrumentación, aplicabilidad y reporte |
| 17.1.8.1 | **17.1.8** | |
| 17.1.9.1, 17.1.9.2 | **17.1.9** | |
| 17.1.10.1, 17.1.10.2 | **17.1.10** | **las salvaguardas se citan como "sección 17.1.10"** |
| 17.1.11.1, **17.1.11.2** | **17.1.11** | |
| 17.1.7.7.6 | *(no existe)* | nunca llegó a la v1.8 |

## 3. Tablas — estado y pendiente de renumeración

**Vigentes (22):** 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35 · C.1, C.2, C.3 ·
D.1, D.2, D.3. Cada una citada **exactamente una vez** desde el desarrollo (regla E2-47), incluida
la C.2, que estaba huérfana hasta la v1.15.

**Huecos abiertos:** **18 y 19** (eliminadas en la rama de GPT sin renumerar) y **31 y 32**
(jerarquía de métricas y umbrales, disueltas en la v1.11 y la v1.14). Se resuelven **en el pase de
integración al maestro**, junto con la numeración global del informe. Propuesta registrada: correr
20→18 … 30→28 y 33→29, 34→30, 35→31, o bien renumerar el capítulo entero de una vez.

**Equivalencias de tablas que citan las actas viejas:** Tabla 18 y Tabla 19 (escenarios y recaudos
ético-legales) ya no existen; su contenido vive en la Tabla 17 y en §17.1.10. La Tabla 31
(jerarquía de métricas) fue reemplazada por la **Tabla 28**; la Tabla 32 (umbrales por severidad)
es hoy la **Tabla 30**.

## 4. Residuales para la integración

1. **Numeración de tablas** (huecos 18/19 y 31/32) y su efecto sobre el índice de tablas del maestro.
2. **Referencias nuevas al listado global:** *Milan, A., Leal-Taixé, L., Reid, I., Roth, S., y
   Schindler, K. (2016). MOT16: A benchmark for multi-object tracking. arXiv:1603.00831* ·
   *Liang, H., y Han, R. (2024). OVT-B: A new large-scale benchmark for open-vocabulary
   multi-object tracking. arXiv:2410.17534*.
3. **Anexos C y D → §19.3 y §19.4** del maestro (D-P3-8).
4. **"baseline" vs "línea base":** la prosa unificó a *línea base*; sobreviven celdas de las Tablas
   16, 33 y 34 con *baseline*. Unificar al integrar.
5. **"Fuente: elaboración propia."** sobrevive sólo en la nota de la Tabla 21 (§17.1.5.2). Ninguna
   otra tabla del capítulo la lleva.
6. **Presupuesto de latencia:** §17.1 declara 35–250 ms para el tramo previo a la acumulación,
   mientras que el instrumento del doc 39, el inventario de métricas y `results/realtime` verifican
   G2A contra 50–250 ms. §17.4 y §17.5 deben mapear una cifra a la otra al reportar.
7. **Un comentario abierto** del colega en §17.1.6 ("validar la lista de pendientes y los
   datasets"), que la v1.15 responde con los datos del registro. Lo cierra el usuario.
