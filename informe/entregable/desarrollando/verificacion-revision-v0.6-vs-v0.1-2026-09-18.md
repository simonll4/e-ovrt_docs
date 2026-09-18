# Verificación mecánica: revisión v0.6 (2026-09-15) vs `E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`

Fuente revisión: `informe/entregable/desarrollando/revision-informe-final-v0.6-2026-09-15.md` (110 líneas).
Fuente v0.1: `informe/entregable/90-informe-final-2026-09-16-v0.1-texto-extraido.md` (la misma extracción, 4.152 líneas; los números de línea de abajo son de esa extracción sin el banner de 12 líneas: sumar 12).
Método: `grep`/`wc`/`python3` sobre el markdown extraído. Todo lo no verificable mecánicamente (redundancia de fondo, tono, "requiere lectura") se marca explícitamente.

## Tabla resumen

| # | Ítem de la revisión | Estado en v0.1 | Evidencia |
|---|---|---|---|
| 2.6a | Secciones 8, 9, 10 faltantes | RESUELTO | `## 9. Índice de Gráficos` (L483), `## 10. Índice de Tablas` (L499) existen; L73 `## Tabla de contenido` (sección 8, sin prefijo numérico en el heading pero con contenido). Ya no hay salto 7→11. |
| 2.6b | Numeración de figuras (Figura 1 vs Figura 4.1–4.6) | ABIERTO | Sin cambios: `Figura 1` (Gantt, L485/982) y `Figura 4.1`…`Figura 4.6` (L2431–3284), mismo esquema heredado. |
| 2.6c | Título 14 con mayúsculas en preposiciones | ABIERTO | L806: `## 14. Plan De Trabajo De Proyecto Integrador`, único heading con "De" mayúscula. |
| 2.6d | 14 tablas nunca mencionadas en el cuerpo (1,12,13,18,20,21,31,B.1–B.7) | ABIERTO (las 14) | Cada una tiene exactamente 2 apariciones de "Tabla N" en todo el doc: la entrada del índice y su propio caption `**Tabla N**`; cero menciones en prosa. Verificado 1‑a‑1 para las 14. |
| 2.3 | P-E1-05 y 07 faltantes en 16.7.3, sin nota | ABIERTO | L1657‑1671: aparecen 01,02,03,04,06,08; texto idéntico al citado por la revisión: "Los códigos se conservan para mantener la trazabilidad con las secciones posteriores" (L1660), sin explicar 05/07. |
| 3.2/3.3 conteos | "no constituye/equivale/implica/sustituye/reemplaza", "sin confundir", conectores, "identidad personal", "sólo/solo" | ABIERTO (persisten en magnitud similar o mayor) | no constituye 32 (rev. 29); no equivale 23 (21); no implica 14 (14); no sustituye 11 (10); no reemplaza 8 (9); sin confundir 7 (8); de modo que 57 (53); por ello 21 (21); identidad personal 12 (10); no se suman 6 (6, match exacto); sólo (tilde) 84 (match exacto con la revisión); solo (sin tilde) 12 (10); oraciones que empiezan "No " ≈71 (heurística, rev. 69). |
| 3.2 | "persistir/persiste antes de publicar" repetido | ABIERTO | Frase exacta ×2, variante "antes de publicar" (persistir/persiste) ×7 en total — mismo patrón disperso que describe la revisión. |
| 4 | AP@0.5 vs AP@0,5 vs AP50/mAP50 | ABIERTO | AP@0.5 ×2 (match exacto), AP@0,5 ×9 (match exacto), AP50 ×11 + mAP50 ×9 = 20 (rev. 22, ~igual). |
| 4 | fps vs FPS | ABIERTO | fps ×8 (rev. 7), FPS ×42 (rev. 35) — mezcla persiste, incluso mayor. |
| 4 | multiobjeto vs multi-objeto | ABIERTO | 25 vs 3 (rev. 23 vs 2); título 15.2.6 sigue con "multi-objeto" (L1221). |
| 4 | fine-tuning vs ajuste fino | ABIERTO | 28 vs 22 (rev. 13 vs 17) — mezcla persiste. |
| 4 | checkpoint vs punto de control | ABIERTO | 23 (match exacto con la revisión) vs 7 (rev. 4). |
| 4 | tracker vs seguidor | ABIERTO (sin cambio) | 19 vs 1 — match exacto con la revisión en ambos. |
| 4 | dataset vs conjunto de datos | ABIERTO | 22 vs 9 (rev. 27 vs 2) — mezcla persiste, proporción cambió. |
| 4 | modelo campeón vs perfil operativo | ABIERTO | "modelo campeón" ×2 (match exacto), "perfil operativo" ×16 — mismo patrón. |
| 4 | Escenario A/B vs DBE/EBE | ABIERTO (uso mixto, es sugerencia de estilo) | Escenario A ×4, Escenario B ×4, DBE ×31, EBE ×43. |
| 5.1 | DINO mal referenciado ("H. Zhang et al., 2022" = GLIPv2) | ABIERTO | L1022 repite literalmente "DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)"; único "Zhang, H." en la lista es GLIPv2 (L~4136); GLIPv2 nunca se nombra en el cuerpo (sólo aparece en Referencias). No existe entrada DINO (Zhang, Li, Liu…). |
| 5.1 | Axis Communications AB, s.f. sin entrada | ABIERTO | L2122 cita "Axis Communications AB, s. f." pero la lista sólo tiene "Axis Communications AB. (2015)" (L3882); mismo párrafo cita también "Axis Communications AB (2015)" en otros lados, o sea coexisten ambas formas. |
| 5.1 | Luxonis s.f.-a/-b sin entradas diferenciadas | ABIERTO | Cuerpo cita "Luxonis, s. f.-b" (L1327), "s. f.-a, s. f.-b" (L1752) y "Luxonis (s. f.)" sin sufijo (L3573); lista sólo tiene "Luxonis. (s. f.)" (L4006), sin -a/-b. |
| 5.1 | Agencia de Acceso… s.f.-a sin entrada | ABIERTO | Cuerpo (L1629) cita "s. f.-a"; lista (L3860) sólo "(s. f.)". |
| 5.1 | NVIDIA sufijos a,b,g,h (faltan c–f) | ABIERTO (mismo patrón, pero entradas sí existen) | Las 4 entradas a/b/g/h SÍ están en la lista (L4020,4030,4032,4034) — no es cita huérfana, pero el salto de letras (sin c–f) persiste igual que en la revisión. |
| 5.2 | 9 entradas de la lista no citadas en el cuerpo | ABIERTO (8/9 confirmados sin cita; GLIPv2 es el caso ya cubierto en DINO) | ISO 45001, IDEA-Research 2024b, Li S. et al. 2022 TET, Li X./Cho/Xiao 2022, Yao et al. 2022 DetCLIP, Zhou et al. 2022a CoCoOp, Zou X. 2023, Zou Z. 2023: las 8 siguen en la lista y NO aparecen citadas en el cuerpo (se buscaron sus términos clave: "45001", "Grounded-SAM-2"/"IDEA-Research, 2024b", "Tracking every thing", "Balancing Latency and Accuracy", "DetCLIP" sin v3/2024, "CoCoOp"/"2022a", "Generalized decoding"/"Zou, X", "Object Detection in 20 Years"/"Zou, Z" — cero resultados en el cuerpo). Zhang H. 2022 GLIPv2 = mismo caso que 5.1 (citada por error, nunca por su nombre). |
| 5.3 | Wang et al., 2025 sin inicial vs A. Wang et al., 2025 | PARCIAL (mejoró, no se unificó) | Sin inicial (real, tras excluir falsos positivos con lookbehind): 3 casos (L1858, 2122, 2178); "A. Wang et al., 2025" ×7. Revisión reportaba 10 vs 8 — bajó pero sigue mixto. |
| 5.3 | Zhang et al., 2022 sin inicial | PARCIAL (mejoró) | 1 caso real (L2122, en la misma oración que junta Axis s.f. + Wang sin inicial) vs revisión ×4; "H. Zhang"/"Y. Zhang" con inicial sí presentes. |
| 5.3 | Jiang et al., 2024 sin inicial | ABIERTO (sin cambio) | ×5, match exacto con la revisión. |
| 5.3 | Yao et al., 2024 sin inicial | ABIERTO (sin cambio) | ×4, match exacto con la revisión. |
| 5.3 | Li et al., 2023 sin inicial | RESUELTO | 0 casos reales sin inicial (los 3 candidatos eran falsos positivos de grep, todos son "S. Li et al., 2023"; revisión reportaba 4 vs 4). |
| 5.3 | Zhou et al., 2022 sin letra (vs 2022b) | ABIERTO (sin cambio) | 1 caso real bare "Zhou et al., 2022" (L1850) + 3 "Zhou et al., 2022b" — mismo patrón que la revisión describe (17.1.5.3). |
| 5.5(e) | Tamaño de la lista de Referencias / citas distintas en el cuerpo | Informativo (no es un ítem pass/fail) | Lista: 150 líneas no vacías tras `## Referencias` (≈150 entradas, 1 por línea). Estimación heurística de citas distintas en el cuerpo (regex "Apellido[, Inicial][ et al.], año", deduplicando por primer token+año): ~115 pares distintos sobre 330 coincidencias crudas — método aproximado, cotejar con lectura si se necesita precisión. |
| 6 | Hoja de Aceptación / Dedicatoria / Agradecimientos con placeholder | ABIERTO | L27, L31, L35: las tres siguen como `*[se completará más adelante]*`. |
| 6 | Resumen y Abstract con placeholder | RESUELTO | L45 (Resumen) y L48 (Abstract) están completamente redactados (párrafos con cifras: 47 clips, 32/15, F1 0,789→0,930, 26/323 FP, etc.), no hay placeholder. |
| 6 | `[[PENDIENTE: ...]]` en Anexo F | RESUELTO | No hay ninguna ocurrencia de "PENDIENTE"/"TODO"/"XXX"/"[[" en todo el documento. Anexo F (L3820‑3851) está redactado en extenso, con Tabla F.1 y notas sobre fecha de consulta de la lista de YouTube. |
| 6 | Secciones 8–10 (índices) ausentes | RESUELTO | Ver ítem 2.6a. |
| 6 | Tabla B.6 y 17.4.4 repiten los mismos parámetros | PARCIAL | La duplicación de contenido persiste (17.4.4 en prosa, Tabla B.6 en tabla) pero ahora la nota de Tabla B.6 remite explícitamente: "Configuraciones efectivas según la sección 17.4.4" (L3635) — implementa la sugerencia de remisión sin eliminar la redundancia. |
| 2.1 | Objetivo específico 5 (MOT/utilidad operativa no evaluados) | PARCIAL | Texto del objetivo sin cambios (L800, idéntico); 18.6 (L3476) reconoce parcialmente el límite ("el estado por persona de CR-02, la evaluación MOT y la validez operativa en obra real mantienen los límites ya expuestos") pero no cierra "ítem por ítem" como pide la revisión. |
| 2.1 | Etapa 5 del plan promete comparación con estado del arte no realizada | ABIERTO | L944 conserva "Análisis comparativo con resultados del estado del arte." en 14.2.5; no se halló en 18.1/17.5.7 una explicación de por qué no se hizo esa comparación (búsquedas de "no es comparable/no resulta comparable" no devuelven nada vinculado a esta etapa específica). |
| 2.1 | 14.4 redactado como ejecutado, se solapa con 17.2 | RESUELTO | L988‑1005: ahora dice explícitamente "Los gastos **previstos** para la realización del trabajo…" y cierra remitiendo a 17.2: "La evaluación económica completa del proyecto… se desarrolla en la sección 17.2." |
| 2.2 | Estatuto de distribución de alertas no unificado (alcance / capacidad opcional / módulo desacoplado) | ABIERTO | Persisten las 3 formulaciones sin unificar: intro L768 ("La plataforma incluye además…"), Tabla 32 L2362 ("Capacidad opcional"), L2682/2937 ("módulo desacoplado"). |
| 2.4 | Cronología de la referencia temporal (congelamiento, revisión ciega, corrección 5.313→5.308) sin ordenar | RESUELTO | L3213 declara "la referencia temporal fue humana y quedó congelada antes del reporte"; L3233 (nota Tabla) declara explícitamente la corrección posterior 5.313→5.308 y que "la medición no se repitió"; L3296 narra la revisión ciega (5 de 7 episodios descartados) en el propio cuerpo. Los tres elementos que la revisión pedía ordenar están ahora explícitos (no en un único párrafo consolidado, pero ya no hay salto silencioso). |
| 2.5 | Previsualización "habilitada por defecto" contradice DA-11/17.3.4.4, no registrada en limitaciones/18.6 | ABIERTO | L3140 reconoce inline la contradicción ("un valor que invierte la regla de habilitación explícita que el diseño fija") pero la lista de 8 limitaciones en 17.5.7 (L3364‑3369) y 18.6 (L3476‑3491) NO la incluyen — verificado leyendo ambos bloques completos. |
| 2.5 | Desviación construction_site_safety en banco+ajuste, no reflejada en Cierre | ABIERTO | L3472 (18.5) repite "CHV se excluyó para proteger la separación con el banco" sin mencionar que `construction_site_safety` sí se comparte entre ajuste y banco (la desviación en sí); tampoco aparece en la lista de 8 limitaciones de 17.5.7. |
| Extras | Conteo de tablas | Informativo | 73 captions `**Tabla N**` en el cuerpo (55 numeradas 1–55 + 18 en anexos A.1–F.1), y 73 entradas en el Índice de Tablas — coinciden exactamente. |
| Extras | Mapa de secciones 12–19 y anexos | Informativo | Ver listado completo más abajo con líneas. |
| Extras | Palabras por sección `## N.` | Informativo | Ver tabla más abajo; Desarrollo del producto (17) concentra ~45.144 palabras de un total aproximado de ~86k. |
| 3.1 (solapamientos de fondo), 3.3 (tono/estilo general), oraciones >60 palabras | requiere lectura | Heurística propia (split por oraciones excluyendo filas de tabla) da 27 oraciones >60 palabras vs 42 de la revisión — método distinto, no comparable de forma confiable sin revisión manual. |

## Detalle de apoyo

### Mapa de headings `## ` (nivel 2) y `### `/`#### ` relevantes

```
25   ## 2. Hoja de Aceptación del Trabajo Final
29   ## 3. Dedicatoria
33   ## 4. Agradecimientos
37   ## 5. Título del proyecto
41   ## 6. Abstract
51   ## 7. Palabras clave
73   ## Tabla de contenido        (sección 8, según la propia TOC interna)
483  ## 9. Índice de Gráficos
499  ## 10. Índice de Tablas
647  ## 11. Glosario, listado de símbolos y convenciones
730  ## 12. Introducción
784  ## 13. Objetivos del proyecto
806  ## 14. Plan De Trabajo De Proyecto Integrador
1006 ## 15. Estado del arte
1380 ## 16. Marco teórico
1681 ## 17. Desarrollo del producto
  1683   ### 17.1. Consolidación metodológica del protocolo experimental
  2222   ### 17.2. Costos asociados
  2320   ### 17.3. Diseño arquitectónico
  2927   ### 17.4. Implementación del prototipo experimental
  3205   ### 17.5. Evaluación y validación del prototipo
  3370   ### 17.6. Documentación técnica, repositorio y evidencias de cierre
3410 ## 18. Cierre del proyecto
  3412   ### 18.1. Respuesta a la hipótesis y alcance de la factibilidad
  3422   ### 18.2. Expresividad semántica, selección del perfil y extensibilidad
  3436   ### 18.3. Aporte temporal de la plataforma y cambio de régimen en obra real
  3450   ### 18.4. Funcionamiento en vivo y restricciones de oportunidad
  3462   ### 18.5. Interpretación de la rama de ajuste fino
  3476   ### 18.6. Balance de objetivos y líneas de continuidad
3492 ## 19. Anexos
  3496   ### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario
  3541   ### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales
  3653   ### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística
  3716   ### 19.4. Anexo D - Métricas, instrumentación y bitácora experimental
  3767   ### 19.5. Anexo E - Reproducibilidad y comprobación de la evidencia
  3820   ### 19.6. Anexo F - Procedencia, licencias y tratamiento del material
3852 ## Referencias
```

### Palabras aproximadas por sección de nivel 2

| Sección | Líneas | ~Palabras |
|---|---|---|
| 2. Hoja de Aceptación | 25-28 | 7 |
| 3. Dedicatoria | 29-32 | 7 |
| 4. Agradecimientos | 33-36 | 9 |
| 5. Título del proyecto | 37-40 | 20 |
| 6. Abstract | 41-50 | 468 |
| 7. Palabras clave | 51-72 | 49 |
| Tabla de contenido (8) | 73-482 | 1.839 |
| 9. Índice de Gráficos | 483-498 | 81 |
| 10. Índice de Tablas | 499-646 | 866 |
| 11. Glosario | 647-729 | 2.083 |
| 12. Introducción | 730-783 | 1.865 |
| 13. Objetivos | 784-805 | 359 |
| 14. Plan de Trabajo | 806-1005 | 1.290 |
| 15. Estado del arte | 1006-1379 | 10.444 |
| 16. Marco teórico | 1380-1680 | 8.179 |
| 17. Desarrollo del producto | 1681-3409 | 45.144 |
| 18. Cierre del proyecto | 3410-3491 | 2.983 |
| 19. Anexos | 3492-3851 | 6.505 |
| Referencias | 3852-4152 | 3.787 |

### Etiquetas de figuras (todas las que existen en el documento)

`Figura 1` (×4, incluye caption L982), `Figura 4.1`…`Figura 4.6` (×3 cada una, caption + 2 menciones en prosa cada una). No hay ninguna otra numeración de figura en el documento.

### Tablas nunca mencionadas en prosa (verificación 1 a 1)

Para cada una de las 14 tablas señaladas por la revisión, el patrón `Tabla N` (con límite de palabra, excluyendo a NN+dígito) aparece exactamente 2 veces en todo el archivo: la línea del Índice de Tablas y la línea `**Tabla N**` de su propio caption. Cero menciones adicionales en prosa para: 1, 12, 13, 18, 20, 21, 31, B.1, B.2, B.3, B.4, B.5, B.6, B.7.

### P-E1-05/07

Sección 16.7.3 (L1657-1671) enumera P-E1-01, 02, 03, 04, 06, 08 (misma lista que en v0.6). La única nota es la genérica "Los códigos se conservan para mantener la trazabilidad con las secciones posteriores" (L1659); no hay ninguna mención de qué eran 05/07 ni por qué se retiraron, en ningún punto del documento (`grep -n "P-E1-05\|P-E1-07"` no devuelve resultados).
