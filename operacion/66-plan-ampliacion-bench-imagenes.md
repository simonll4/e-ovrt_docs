# 66 — Plan de ampliación del bench de imágenes (2026-07-23)

Responde al déficit señalado en el análisis realista post-S2: `bench_obra` es honesto pero
chico (147 imgs; vest n=79, bare_head n=61, violadores CR-01 n=65 ⇒ IC de ±0.12 en recall).
Objetivo: **n≥300 por clase y ≥2 fuentes**, sin sacrificar la honestidad ganada en S0.

## Precondición metodológica (antes de tocar datos): congelar prompts

Regla anti-fuga: **ningún dato que entre al bench puede usarse para calibrar prompts** (sería
overfitting del "modelo" — acá el prompt ES parte del modelo). El set `cr01_cr02_bench_v2`
está fijo desde Sprint 2 y S1 corrió con él; se declara **congelado para evaluación de
bench** antes de incorporar imágenes nuevas. Las corridas de calibración del carril 2 de la
estrategia de prompts usan EXCLUSIVAMENTE material que no esté en ningún bench (p.ej. DEMO
split o el train de CHV no promovido).

## B1 — Promover CSS-train: **DESCARTADO tras auditoría (2026-07-23)**

La auditoría S0 previa a promover (18 imgs con GT dibujado + verificación objetiva) mostró
que **el train split de CSS está 100% aumentado por el export de Roboflow**: collages mosaic
2×2, parches cutout negros y variantes en escala de grises horneadas en los archivos, con
selfies COVID dentro de los collages. Verificación objetiva: densidad 14,4 anotaciones/img
vs 3,8 en test/val (≈4× = collage 2×2 en casi todo el split). La política del repo
(`class_mapping.yaml`: "no data augmentation sobre BENCH/DEMO") lo prohíbe y no hay forma
confiable de recuperar los originales del export. **Los conteos prometedores del plan
original (NO-Hardhat 2318, etc.) eran anotaciones de derivados aumentados.** El principio
auditar-antes-de-promover evitó contaminar el bench por segunda vez.

## ~~B1 (plan original, invalidado)~~ Promover CSS-train curado

`construction_site_safety/train`: 2.603 imgs con GT completo: Person 9.691, Hardhat 3.362,
**NO-Hardhat 2.318** (→ bare_head + `has_helmet=false`), Safety Vest 3.156, **NO-Safety Vest
3.957** (→ `has_vest=false`, habilita atributos CR-02 que el bench actual casi no tiene).

1. Aplicar la curación S0 (mismas 12 reglas de prefijo + área mínima, script extendido) —
   esperar ~25% de exclusión como en test/val.
2. Auditoría visual muestral (~30 imgs con GT dibujado) ANTES de promover: el train split
   nunca fue mirado a ojo.
3. **Dedup perceptual contra test/val** (política ya declarada en class_mapping.yaml): los
   splits Roboflow salen de los mismos videos ⇒ near-duplicates entre train y test/val
   inflarían el n sin agregar información. Reportar cuántos se excluyen.
4. Convertir con `convert_datasets.py` (ya soporta CSS) + `build_person_gt.py` para extender
   el GT persona-nivel (violadores CR-01 y CR-02 nuevos).
5. Salida: `bench_obra_ext_css` con estrato declarado `fuente=css_train`.

Advertencia declarada: sigue siendo LA MISMA fuente Roboflow — sube n y precisión de los IC,
NO independencia. La independencia la aportan B2/B4.

## B2 — CHV a rol BENCH (segunda fuente, académica) — **AUDITADO APTO (2026-07-23)**

Auditoría visual (12 imgs con GT dibujado): obra e industrial real, cajas prolijas y ceñidas
(cascos/chalecos/personas), sin augmentations (densidad 5 labels/img, mediana). Salvedades a
declarar: algunas imágenes de stock con watermark y 1–2 de estudio con fondo blanco; dominio
mixto obra/aula-industrial (consistente con el scoring original "parcial"). Entra como
estrato propio.

CHV (ZijianWang, PPE_detection, 1.330 imgs, YOLO): person + helmet(4 colores) + vest. Está
en rol TRAIN, pero **no entrenamos**: reasignarlo a BENCH es legítimo si (a) los prompts ya
están congelados (precondición) y (b) se excluye del carril de calibración.

1. Auditoría S0 muestral (dominio "parcial" según scoring: verificar cuánto es obra real).
2. Sin negativos explícitos ⇒ **aporta AP de person/helmet/vest, NO CR-01/CR-02** (el
   contrato v2 prohíbe derivar bare_head por resta — se respeta).
3. Chequeo de solape contra ppe-dataset rechazado (comparten stems `ppe_XXXX`) y contra CSS.
4. Salida: estrato `fuente=chv` para AP por clase con n independiente.

## B3 — ppe_siabar: decisión post-auditoría (prioridad baja)

1.612 imgs person/helmet/vest, pero el scoring lo marca `dominio_obra_civil: no`. Auditar 20
imgs: si el dominio es genérico-industrial, NO entra al bench de obra (puede servir como
robustez out-of-domain declarada, que es otra pregunta). No gastar más de 30 min.

## B4 — Fuente externa nueva: adoptar SHEL5K (investigación 2026-07-23 cerrada)

Se investigaron 8 candidatos académicos con los criterios de entrada (GT de person + dominio
obra + licencia citable + descarga viva; links y licencias verificados uno a uno):

- **ADOPTAR: SHEL5K** (Otgonbold et al., *Sensors* 2022; Mendeley Data `9rcv8mm682` v4,
  **CC BY 4.0**, descarga directa sin registro, VOC XML). 5.000 imgs / 75.578 labels en 6
  clases que mapean nativo: `person_with_helmet ∪ person_no_helmet` → person (¡con atributo
  has_helmet gratis!), `helmet` → helmet, **`head` → bare_head SIN derivación** — GT nativo
  de nuestra clase más débil, la que más necesita n. No trae vest. Costo: hereda un
  subconjunto no-obra (aulas) del Kaggle original ⇒ **auditoría de dominio S0 obligatoria**
  antes de promover (mismas herramientas de mosaicos).
- **Opcional 2º: CHVG** (Ferdous & Ahsan, *PeerJ CS* 2022; figshare, **CC BY 4.0**, 1.699
  imgs): el único con los 4 conceptos (person body / hardhat / vest / head) en obra real —
  PERO es la extensión de nuestro CHV: exige dedup imagen-a-imagen contra los splits v2 y el
  remanente puede quedar chico. Entra solo si tras dedup aporta n material.
- **Reserva: SH17** (CC BY-NC-SA, 8k imgs, 4 clases, ya tenemos script de descarga legacy) —
  volumen y vest, pero dominio "foto de stock Pexels": no como núcleo del bench.
- **Descartados con evidencia**: SODA (link oficial 404, solo Baidu, sin licencia — una pena:
  el mejor dominio), GDUT-HWD (sin clase person; Baidu-only), SHWD (su "person" son cabezas
  y mezcla aulas — mismo patrón que el ppe-dataset rechazado), Pictor-v3 (sin licencia, 774
  imgs útiles), SFCHD (sin licencia declarada; safety-clothing ≠ vest — reconsiderar si los
  autores licencian: dominio CCTV industrial excelente).

Registro completo del informe: agregarlo a `datasets/registry/` al ejecutar B4.

### B4 ejecutado (2026-07-23): SHEL5K descargado y AUDITADO APTO con salvedades

Descarga verificada desde el endpoint oficial de Mendeley (`public-api/zip/9rcv8mm682/download/4`,
zip 1,23 GiB íntegro conservado): 5.000 PNG + 5.000 XML VOC, correspondencia 1:1 perfecta.
Conteos reales: helmet 19.252, head_with_helmet 16.048, person_with_helmet 14.767,
**head 6.120 (= bare_head nativo)**, person_no_helmet 5.248, face 14.135, + 8 labels `person`
sueltos (ruido de anotación, se ignoran en el mapping).

**Auditoría S0 (18 imgs con GT + 300 verificadas estadísticamente): dominio obra/industrial
real** (túneles, andamios, excavadoras, líneas eléctricas, aplanadoras) — **sin aulas en la
muestra** (la herencia SCUT-HEAD era de SHWD, no de esta base). Salvedades a declarar como
estrato: (a) **resolución 416×416** en todo el dataset (base Roboflow preprocesada — estrato
de baja resolución, objetos chicos gruesos); (b) **mirror-padding horneado en ~2–10%** de las
imágenes, con GT anotado también sobre las franjas espejadas (detector estricto: 7/300;
visualmente algo más); (c) watermarks de portales de noticias chinos en una fracción.

**Mapping canónico decidido**: `person` = person_with_helmet ∪ person_no_helmet (con
`has_helmet` gratis por la clase compuesta), `helmet` = helmet, `bare_head` = head;
`face`/`head_with_helmet`/los 8 `person` sueltos se descartan. Próximo paso: entrada
`shel5k` en `configs()` de `convert_datasets.py` (TDD) + estrato en bench_v3 (B5).

## B5 — Conversión + re-puntuación + consolidación: COMPLETO (2026-07-23)

**Hecho, con TDD (suite datasets 125 passed):**

1. **Mapping SHEL5K corregido en el conversor** — la entrada previa (de junio) tenía dos
   errores que la auditoría del B4 destapó: mapeaba `head_with_helmet→helmet` (verificado:
   97% de solape con una caja `helmet` separada — habría duplicado ~16k cajas de GT) y no
   mapeaba `head` en absoluto por una lectura conservadora del guard D9. Verificación empírica
   sobre 400 XML: las cajas `head` están 82% contenidas en `person_no_helmet` y solo 2% en
   `person_with_helmet` (existe `head_with_helmet` aparte) — es la anotación EXPLÍCITA de
   cabeza descubierta del paper, no una derivación por resta. El guard `assert_no_derived_bare_head`
   ganó una exención tipada `bare_head_explicit_sources` (documentada, exige verificación
   empírica citada) sin debilitar la regla general.
2. **Conversión `canonical_v2` ejecutada**: SHEL5K (5.000 imgs: person 20.023, helmet 19.252,
   **bare_head 6.120**) y CHV (1.330: person 3.887, helmet 3.538, **vest 1.784**).
3. **`person_gt_shel5k.json` generado** (script nuevo con TDD,
   `datasets/scripts/bench/build_person_gt_shel5k.py`): 20.015 personas con `has_helmet`
   directo de las clases compuestas → **5.248 violadores CR-01** (vs 65 en bench_obra).
   `has_vest` deliberadamente ausente — SHEL5K no lo anota; fabricarlo en `false` inventaría
   violadores CR-02 que no existen en el dataset.
4. **COCOs por estrato fusionados** (`bench_stratum_{shel5k,chv}.json`, ids remapeados,
   basenames verificados únicos).

**Re-puntuación completa (3/3 modelos candidatos × 2 estratos nuevos + re-lectura corregida
del estrato `bench_obra`):**

| Modelo | Estrato | person | helmet | vest | bare_head | recall CR-01 |
|---|---|---|---|---|---|---|
| gdino-tiny-560 | shel5k (n=5000) | 0.770 | 0.707 | — | **0.133** | 0.308 |
| gdino-tiny-560 | chv (n=1330) | 0.862 | 0.886 | **0.553** | — | — |
| gdino-base-560 | shel5k (n=5000) | 0.693 | 0.415 | — | **0.399** | **0.602** |
| gdino-base-560 | chv (n=1330) | 0.783 | 0.453 | **0.576** | — | — |
| yoloe-26x | shel5k (n=5000) | 0.785 | 0.715 | — | 0.000 | 0.000 |
| yoloe-26x | chv (n=1330) | 0.785 | 0.888 | 0.243 | — | — |

(`—` = clase sin GT en ese estrato: vest no existe en SHEL5K, bare_head no existe en CHV;
recall CR-01 en CHV sale `None` por falta de `person_gt` propio, esperado.)

**Trampa cazada al consolidar: el `eval_perception.json` de las corridas `bench_obra` de S1**
tenía el recall CR-01 con el bug de denominador (el fix del CLI, doc 64, llegó después de
esas corridas puntuales) — **0.415/0.471** en vez de los valores correctos ya validados a
mano en doc 64 (test 7/30=0.2333, val 17/35=0.4857 para tiny-560; análogo para base-560).
Causa de fondo: el mecanismo `restrict_gt_to_detections` del CLI restringe el `person_gt` a
los basenames del `detections.jsonl` del run — pero esas corridas de S1 procesaron el
`bench_v2_test` SIN curar (82 imgs), no el `bench_obra_test` curado (62 imgs), así que el
restrict conserva violadores de las 20 imágenes fuera de dominio que la curación excluye. El
AP por clase (que sí restringe por el `--bench-coco` pasado) no se ve afectado — solo el
recall CR-01. Se usaron los valores manualmente verificados de doc 64 para el agregado.

## `bench_v3` ensamblado y congelado

Script nuevo con TDD (`datasets/scripts/curate/build_bench_v3.py`, 6 tests):
fusiona los 4 COCOs curados (`bench_obra_test` + `bench_obra_val` + `chv` + `shel5k`) con ids
globales únicos, cada imagen con su campo `stratum`. Salida:
`processed/coco/bench/curated/bench_v3.json` (**6.477 imgs, 55.165 anotaciones**) +
`bench_v3_manifest.json` (conteos por estrato, sha256 de cada fuente y del bench fusionado —
congelamiento verificable). Integridad verificada: 0 colisiones de id, 0 basenames duplicados
entre estratos. Registro humano: `datasets/registry/bench_v3.md`.

Agregado ponderado por n_gt/n_violadores real (`datasets/scripts/curate/bench_v3_report.py`,
4 tests — ignora clases ausentes en un estrato en vez de contarlas como cero):

| Modelo | mAP50 (n=6.477) | recall CR-01 (n=5.313) |
|---|---|---|
| **gdino-tiny-560** | **0.551** | 0.308 |
| gdino-base-560 | 0.525 | **0.599** |
| yoloe-26x | 0.442 | 0.000 |

**Resultado: el campeón se sostiene idéntico** (`gdino-tiny-560`, 1º en mAP50 tanto en
`bench_obra` solo —147 imgs— como en `bench_v3` —6.477—, robusto a la fuente). El hallazgo de
`gdino-base-560` como especialista CR-02/bare_head, casi empatado en `bench_obra` (0.400 vs
0.369, n=65), **se separa con claridad** al sumar el n grande de SHEL5K (0.599 vs 0.308,
n=5.313): no era ruido de denominador chico, es un efecto real que ahora tiene respaldo
estadístico sólido para el reporte de cierre. Detalle y decisión formal en doc 64 (sección
"Confirmación B5").

Crudos: `datos/b5_rescore_partial_2026-07-23.jsonl` (6 registros: los 3 modelos × 2 estratos,
pese al nombre "partial" del archivo — quedó así por continuidad con la corrida de anoche).

## Esfuerzo real vs estimado

Estimado originalmente: B1 medio día + B2 2-3h + B4 1 día + B5 ~1h GPU. Real: B1 se descartó
en la propia auditoría (30 min), B2/B4/B5 se completaron en una sesión partida en dos noches
(la descarga de SHEL5K y el cómputo GPU fueron la parte lenta, no el análisis). Bench de
imágenes pasó de 147 imgs / 1 fuente a **6.477 imgs / 3 fuentes independientes** — el IC del
recall CR-01 baja de ±0.12 (n=65) a ~±0.014 (n=5.313). El rodaje no se tocó ni se retrasó.
