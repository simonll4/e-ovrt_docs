# 64 — Resultados S1/S2: selección de modelos (2026-07-23)

Ejecución de la Fase S del plan maestro (doc 62 §3). 20 corridas DBE (10 configuraciones ×
2 splits BENCH v2), 20/20 `succeeded`, criterio pre-registrado ANTES de correr (doc 62 §2.1:
mAP50 primario, desempate recall CR-01, agregado test+val ponderado). Crudos:
`datos/s1_matrix_results_2026-07-23.jsonl`; sub-splits limpios `datos/bench_obra_{test,val}.json`.

## Matriz completa (BENCH v2, 196 imgs)

| Configuración | mAP50 | recall CR-01 | vest AP | bare_head AP | inf p50 (ms) |
|---|---|---|---|---|---|
| **gdino-tiny-560** | **0.460** | 0.448 | 0.30 | 0.02–0.09 | **129** |
| gdino-base-560 | 0.453 | **0.541** | **0.51** | 0.01–0.03 | 146 |
| gdino-tiny (800) | 0.442 | 0.411 | 0.27 | 0.02–0.03 | 188 |
| yoloe-26x | 0.407 | 0.000 | 0.14 | 0.000 | 43 |
| gdino-base (800) | 0.401 | 0.514 | 0.43 | 0.01–0.03 | 213 |
| yoloe-26l | 0.378 | 0.000 | 0.13 | 0.000 | 34 |
| yoloe-26s | 0.370 | 0.049 | 0.23 | 0.000 | 27 |
| mm-gdino-base | 0.360 | 0.029 | 0.39 | 0.00 | 213 |
| yoloe-26m | 0.345 | 0.000 | 0.09 | 0.000 | 30 |
| mm-gdino-large | **0.017 (ROTO)** | — | 0.00 | 0.00 | 723 |

## Re-puntuación en `bench_obra` (147 imgs limpias, sin contaminación S0)

| Configuración | mAP50 obra | recall CR-01 obra | vest AP obra |
|---|---|---|---|
| **gdino-tiny-560** | **0.503** | 0.369 | 0.520 |
| gdino-tiny (800) | 0.502 | 0.323 | 0.456 |
| gdino-base-560 | 0.474 | **0.400** | **0.582** |
| yoloe-26x | 0.405 | 0.000 | 0.182 |

*(Recall obra corregido 2026-07-23: la primera versión de esta tabla traía valores deflactados
~2× por un bug de protocolo — `tools/evaluate` no restringe el `person_gt` a las imágenes del
run por default (`restrict_gt_to_detections=False`), así que el denominador eran los 111
violadores de AMBOS splits contra detecciones de uno solo. Corregido con denominadores obra
reales: 30 violadores test + 35 val = 65. El CLI queda arreglado para que restrinja por
default.)*

## Hallazgos

1. **CAMPEÓN GLOBAL: `gdino-tiny-560`** — 1º en mAP en los DOS marcos (completo 0.460, obra
   0.503; el empate técnico con tiny-800 en obra lo resuelve el desempate pre-registrado:
   recall CR-01 0.369 vs 0.323), y encima **32% más rápido** que el 800 (129 vs 188 ms DBE;
   −24% live, doc 61). La decisión no depende del marco: robusta a la contaminación.
2. **La resolución 560 mejora a AMBOS GDINO** (tiny 0.442→0.460, base 0.401→0.453; y en obra
   idem). Tercer dato consistente tras doc 61 (BENCH test) y el live. Con objetos chicos
   (helmet mediana 0,4% del área) el letterbox 560 no pierde y el modelo gana.
3. **La contaminación S0 inflaba el recall CR-01 moderadamente** (tiny-560: 0.448 completo →
   0.369 obra, −18%; el 41% de los violadores del `person_gt` —46 de 111— estaba en imágenes
   contaminadas, pero los modelos los detectaban en proporción similar). Y deprimía vest
   (0.30→0.52 al limpiar). **El instrumento limpio cambia los números absolutos, no el
   campeón** — exactamente la salvedad prevista en doc 63. *(La afirmación original "~2×" de
   este hallazgo era un artefacto del bug de protocolo anotado bajo la tabla obra.)*
4. **`gdino-base-560` = especialista en DOS EJES, con rol acotado** (vest AP 0.582 y recall
   CR-01 **0.400** en `bench_obra`, ambos los mejores): pasa a Fase T como candidato
   secundario — si el banco temporal pondera CR-02, puede disputar.
   > ✎ **Dos correcciones a este hallazgo (2026-08-10).** (1) **El número**: decía recall
   > CR-01 **0.292**, que era el valor **deflactado por el bug de denominador** anotado bajo
   > la tabla obra; el valor corregido de esa misma tabla es **0.400** (y en el marco BENCH v2
   > completo es 0.541). El 0.292 no correspondía a ninguna tabla vigente. (2) **La etiqueta**:
   > decía *"especialista CR-02/vest"* y en §B5 más abajo *"especialista CR-02/`bare_head`"* —
   > la segunda **mezcla los ejes**, porque `bare_head` es evidencia de **CR-01**, no de CR-02.
   > Etiqueta canónica, ya vigente en `results/bench_imagenes/index.md` y en AF-5:
   > **especialista en `bare_head` (evidencia de CR-01) y en `vest` (CR-02)**.
   > **Salvedad que hay que decir al citarlo:** la ventaja en `bare_head` **no se ve en la
   > tabla BENCH v2 de este doc** (base 0.01–0.03 vs tiny 0.02–0.09, base es PEOR); aparece
   > con el n grande de `bench_v3`/`shel5k` — **AP `bare_head` 0,399 vs 0,133** y **recall
   > CR-01 0,599 vs 0,308 (n=5.313)**. Lo robusto es el recall de la condición y el AP de
   > `vest`; **nunca escribir "el mejor en `bare_head`" citando solo este doc.**
5. **Familia MM-GDINO DESCARTADA entera con evidencia**: large reproduce el bug de bboxes
   degeneradas de Sprint 2 (sanity-check 2–3 degeneradas, mAP 0.003–0.027, 723 ms) y base es
   mediocre (0.360) sin ventaja en nada.
6. **Campeón YOLOE: 26x** (0.407/0.405) — pero vest 0.18, bare_head 0.000, recall CR-01
   0.000: **zero-shot no ve EPP**. Confirma su rol de réplica rápida/gate (doc 12 §3) y
   cuantifica el otro lado del trade: 43 ms vs 129 ms, a costo de no poder evaluar CR-01/CR-02.
7. `bare_head` sigue débil en obra limpia (≤0.09 quitando GT sub-pixel): el problema es real,
   no solo del GT. La estrategia E-DIR (Fase D) y la sobre-marca a distancia (A7/FAR) siguen
   siendo el camino de análisis.

## Decisiones S2 (enmienda formal a doc 58 §C Etapa A y doc 12 §3)

- **Fase T y P corren con `gdino-tiny-560` (primario) y `gdino-base-560` (secundario CR-02).**
- **Fase L (live) corre con `gdino-tiny-560`** — validado en BENCH (este doc) y en live
  (doc 61). YOLOE-26m queda como referencia de piso de latencia si hace falta.
  > ✎ **2026-08-10 — lo que efectivamente corrió en vivo fue `yoloe-26x`, no `26m`**
  > (doc 71 §2.3 y §7). El cambio **fortalece** el descarte en vez de debilitarlo: se llevó a
  > vivo la **mejor talla** de YOLOE por calidad (el campeón YOLOE del hallazgo 6 de este
  > mismo doc), no la más rápida, y aun así dio **0/3 alertas confiables** con verdad de
  > campo. La línea de arriba quedó como la única mención a `26m` en el doc; el resto ya
  > hablaba de `26x`.
- **Ninguna variante 800 px se lleva al banco temporal (video).** ✎ **Declarado
  explícitamente el 2026-08-10** — hasta hoy era inferencia del lector. La causa es
  **dominancia medida, no omisión**: 560 iguala o mejora el mAP con **−24% de latencia**
  (D-61.4 y hallazgo 2 de este doc), así que llevar 800 a los clips habría gastado GPU para
  medir una configuración dominada, y habría roto la variable única de las campañas
  (todas comparten modelo/resolución contra T1). **Trabajo futuro con causa:** doc 103 §7.4
  lista "800 px" entre las mitigaciones **no medidas** para el colapso de `vest` a
  distancia — si ese frente se retoma, la resolución es la palanca a medir, y hoy **no**
  figura en la enumeración de "palancas agotadas" del clip bench, a propósito.
- MM-GDINO fuera del resto del plan. YOLOE-26x se reporta como contraste, no compite en T/P.
- Reporte de cierre (Q1): números del marco `bench_obra` con n=147 y la contaminación
  declarada (doc 63); el BENCH completo solo como apéndice.

## Confirmación B5 (2026-07-23, `bench_v3`, n=6.477 — ver doc 66 §B5)

Los 3 campeones se re-corrieron sobre `bench_v3` (bench_obra + chv + shel5k, 44× más
imágenes que solo `bench_obra`). **El campeón se sostiene idéntico:**

| Modelo | mAP50 (n=6.477) | recall CR-01 (n=5.313) |
|---|---|---|
| **gdino-tiny-560** | **0.551** (1º, igual que doc 64 original) | 0.308 |
| gdino-base-560 | 0.525 | **0.599** (1º, brecha AHORA clara) |
| yoloe-26x | 0.442 | 0.000 |

**gdino-tiny-560 gana mAP50 en bench_obra solo (147) Y en bench_v3 (6.477) — robusto a la
fuente.** El hallazgo de `gdino-base-560` como especialista en **`bare_head` (evidencia de
CR-01) y en `vest` (CR-02)** — ✎ 2026-08-10: *decía "especialista CR-02/bare_head", etiqueta
que mezclaba los ejes* —, que en
`bench_obra` era casi empate (0.400 vs 0.369, n=65), **se separa con claridad** al sumar el
n grande de SHEL5K (0.599 vs 0.308, n=5.313): no era ruido de denominador chico, es un efecto
real. Decisión S2 sin cambios; el hallazgo del especialista queda más fuerte para el reporte
de cierre. Ver `datasets/registry/bench_v3.md` para la composición y salvedades del bench.
