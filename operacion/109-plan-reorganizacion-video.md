# 109 — Plan de reorganización del dataset de video, runs y evaluaciones

**Fecha:** 2026-08-07. **Qué es:** el diseño de cómo queda organizado el material de
video y qué corridas producen los resultados citables, después de que el estrato B
creciera por goteo durante dos días (docs 102→108). **Estado: APROBADO Y EJECUTADO —
resultados en §9.**

**Por qué hace falta:** el material y los hallazgos están bien, pero los
**artefactos** quedaron fragmentados: campañas corridas con un subconjunto de los
clips, un artefacto de Nivel A calculado contra un GT que después se corrigió, tres
JSONs de Nivel A que deberían ser uno, y secciones de índice con capas de ✎ sobre ✎.
Nada de eso invalida conclusiones — pero hace que "los resultados" no se puedan citar
de un solo lugar, que era el pedido.

---

## 1. Diagnóstico: qué está desordenado (verificado, 2026-08-07)

| # | problema | evidencia |
|---|---|---|
| 1 | **Campañas I1/I2 corridas con 3 clips**; `v04_c02` quedó afuera | `results/clip_bench/i{1,2}_*/evals/` tienen 3 evals |
| 2 | **`campaign.yaml` de I1/I2 describen un GT que ya no existe** ("2 positivos; v06 CR-02") | corrección de `v06_c01` (doc 108 §6) |
| 3 | **`105-nivel-a-estrato-b.json` es STALE** — se puntuó con el XML de `v06` pre-corrección (394 cajas cambiaron de `false`→`true`) | sus cifras de CR-02 en `v06` son falsas |
| 4 | **Nivel A disperso en 3 JSONs sueltos** en `datos/`, sin estructura de campaña | `105-nivel-a-{piloto,estrato-b}.json` + `108-nivel-a-v04c02.json` |
| 5 | **Corridas de `v04_c02` sueltas** (`108-v04c02/`), no son campaña | mezcla de sesiones |
| 6 | **Sección "estrato B" del índice ilegible** por parches sucesivos | 3 rondas de ✎ |
| 7 | **~1,1 GB de `control_runs` exploratorios** sin comprimir | `103-gate-sim` 432M, `107-barrido-knobs` 295M, `104-barrido-gate` 137M, `102-i2` 129M, `104-i4` 121M |

**Lo que NO está desordenado y no se toca:** el banco (38 clips, `gt_ready`,
validadores en 0 errores, freeze 153 OK) y las campañas del rodaje (T1…R6,
congeladas contra el freeze `cef5082e`, ninguna tocada por nada de esto).

## 2. Diseño: el eje organizador

**Tres estratos de material × dos niveles de medición**, y separación estricta entre
**campaña citable** y **evidencia exploratoria**.

### 2.1 Material (ya es correcto — se formaliza, no se mueve)

| estrato | clips | ubicación | qué admite |
|---|---|---|---|
| **A — rodaje** (guionado) | 34 | banco | Nivel B (campañas congeladas) |
| **B — internet** (obra real) | **5 con GT** + 9 sin GT declarados | banco | Nivel B · **FAR/hora** · Nivel A |
| **Piloto** (12 s, 2026-07-18) | 4 | `_retired/piloto_2026-07-18/`, ejecutables | **solo Nivel A** — censura A1 no depende del archivo |

Composición del estrato B tras la corrección: `v04_c01` (P1, nocturno) ·
`v04_c02` (P6, nocturno, 2 episodios) · `v06_c01` (**P5 negativo, el único SOAK**) ·
`v10_c01` (P5 negativo).

> ✎ **2026-08-07, noche (doc 110): entró `v03_c02`** — banco **39 clips**, estrato B
> **5 con GT** (9 del lote sin anotar). Es **negativo** (P5, diurno, 104,9 s) tras una
> corrección firmada de atributos, así que **no cambia ningún episodio ni el denominador
> de FAR/hora**; suma tiempo negativo (0,1548 → 0,1840 h) y control de FP. **Las
> campañas de este doc (gen. 2, `manifest.yaml` `4437eb6d…`) NO lo incluyen**: la gen. 3
> con los 5 clips está lista para correr en un comando (doc 110 §4) y la recomendación es
> **correrla una sola vez, cuando el lote esté completo**.

### 2.2 Regla de separación (lo que arregla el desorden de fondo)

| clase | dónde vive | criterio |
|---|---|---|
| **Campaña citable** | `results/{clip_bench,bench_nivel_a}/<id>/` con `campaign.yaml` + `metrics.json` + `evals/` + `provenance.json` | una combinación declarada, **todos** los clips del estrato, GT vigente |
| **Evidencia exploratoria** | `docs/operacion/datos/<doc>-*/` | barridos, simulaciones, controles; **nunca** se cita como resultado |

Los barridos de los docs 104/107 son **exploratorios por definición** (calibración
in-sample declarada, y el doc 108 §3 refutó su mejor palanca fuera de muestra). Se
quedan donde están; lo único que cambia es que se comprimen (§5).

## 3. Nivel B del estrato B — reconstrucción completa

**Decisión: re-ejecutar de cero, no parchear.** Motivo: hoy las cifras de I1/I2 salen
de dos sesiones de inferencia distintas, con `v04_c02` afuera y un `campaign.yaml`
que describe otro GT. Parchear deja una procedencia que nadie va a poder reconstruir
en la defensa.

| campaña | id | granularidad | análoga a | costo |
|---|---|---|---|---|
| **I1** | `i1_gdinotiny560_v2short_scene_internet` | `scene` | T1 | **GPU, ~45 min** (v06 domina) |
| **I2** | `i2_gdinotiny560_v2short_subject_internet` | `subject` | G1 | CPU, ~1 min |

- **Se conservan los ids `i1`/`i2`** — los docs 103–108 los citan; renombrar rompería
  links por una ganancia cosmética. La historia de alcance se declara **dentro** del
  `campaign.yaml` (gen. 1 = 3 clips pre-corrección · gen. 2 = 4 clips, GT vigente),
  que es donde un lector la busca.
- **Los 4 clips en una sola sesión de inferencia** ⇒ una procedencia, un hardware,
  un `prompt_set_frozen_sha256`.
- **De yapa: verificación de reproducibilidad.** Re-inferir `v04_c01`/`v06_c01`/
  `v10_c01` permite comparar detección a detección contra la corrida de anteayer.
  Si difieren, es un hallazgo (no-determinismo del pipeline) que hay que saber.

## 4. Nivel A — una campaña consolidada

Hoy son 3 JSONs sueltos y uno está stale. **Se reemplazan por una sola campaña** sobre
**los 8 clips con GT humano de video** (4 del estrato B + 4 del piloto), con el XML
corregido y el mismo punto de operación desplegado:

```
results/bench_nivel_a/na1_gdinotiny560_v2short_video/
    campaign.yaml · metrics.json · por_clip.json
```

Los 3 JSONs viejos quedan **supersedidos con nota** (no se borran: son la evidencia de
los docs 105/108 tal como se escribieron).

**Lo que esto arregla, además del orden:** el número de `v06_c01` a Nivel A hoy es
**falso** (GT pre-corrección). Es la única cifra publicada de la jornada que está mal.

## 5. Higiene de artefactos

Comprimir los `control_runs` exploratorios a `.tar.gz`, **siguiendo el precedente ya
establecido en el repo** (`81-campana-rodaje-dbe-control-runs.tar.gz`,
`85-d1-edir-control-runs.tar.gz`, etc.): ~1,1 GB → estimado <150 MB. **No se borra
nada**: los `eval_*.json` y `resumen.json` (que son lo que los docs citan) quedan
sueltos y legibles.

## 6. Ejecución propuesta

| paso | qué | costo | reversible |
|---|---|---|---|
| 1 | Campaña I1 (scene, 4 clips, inferencia fresca) | GPU ~45 min | sí |
| 2 | Campaña I2 (subject sobre las detecciones de 1) | ~1 min | sí |
| 3 | Verificación de reproducibilidad vs corrida anterior | ~1 min | — |
| 4 | Campaña Nivel A consolidada (8 clips) | ~2 min | sí |
| 5 | Reescribir de una pieza: sección estrato B del índice de `clip_bench`, sección de video del índice de `bench_nivel_a`, registry | — | sí |
| 6 | Comprimir `control_runs` exploratorios | ~5 min | sí (son regenerables) |

**Total: ~1 h, casi todo desatendido.** El servidor del media-plane ya está levantado
con el modelo campeón.

## 7. Lo que NO se re-ejecuta (y por qué)

- **Campañas del rodaje (T1…R6):** congeladas contra el freeze `cef5082e`. Nada de
  esta jornada las tocó — el manifest solo creció.
- **Barridos de los docs 104/107** (gate, knobs, `base-560`): son caracterización de
  mecanismo sobre **detecciones**, que no cambiaron con la corrección del GT. Sus
  banners ya declaran que los conteos absolutos son pre-corrección. Re-correrlos
  costaría GPU y no cambiaría ninguna conclusión.
- **Piloto a Nivel B:** censurado por A1 con o sin video.

## 8. Riesgos declarados

1. **Las cifras publicadas de I1/I2 van a cambiar** (por `v04_c02` y por la
   corrección). Es el objetivo, pero implica actualizar los docs 103–108 que las
   citan. Se hace con nota, no borrando.
2. **`n` sigue siendo chico**: 3 episodios evaluables en 4 clips. La reorganización
   no compra poder estadístico — compra trazabilidad.
3. **La verificación de reproducibilidad puede fallar** (si el pipeline no es
   determinista frame a frame). Sería un hallazgo nuevo y habría que reportarlo.

---

## 9. EJECUCIÓN — resultados (2026-08-07, 20:03–20:47)

Los 6 pasos de §6 ejecutados. **43 min de GPU** (inferencia fresca de los 4 clips) +
CPU. Todo verificado al cierre: `validate_clip_gt` 0 errores, freeze OK, suites verdes
(datasets 304, control-plane 312), verificador de índices verde.

### 9.1 F-109.1 — el pipeline DBE es determinista, verificado

La re-inferencia de los 3 clips ya corridos el 08-06 dio **detecciones idénticas**:

| clip | detecciones | de las cuales `vest` | |
|---|---|---|---|
| `v04_c01` | 6.820 = 6.820 | 1.713 = 1.713 | ✔ |
| `v06_c01` | 284.189 = 284.189 | 55.572 = 55.572 | ✔ |
| `v10_c01` | 21.001 = 21.001 | 3.376 = 3.376 | ✔ |

No estaba verificado hasta hoy. Vale para toda re-corrida futura: **si un número
cambia, cambió una entrada, no el azar.**

### 9.2 Nivel B del estrato B — gen. 2 (4 clips, GT vigente)

| | I1 `scene` | I2 `subject` |
|---|---|---|
| recall (3 eps) | 0,667 | **1,000** |
| precision | **0,500** | 0,250 |
| **F1** | **0,571** | 0,400 |
| t_alert | **5.533 ms** | 6.700 ms |
| FP negativos · FAR/hora | 5 · **48,7** | 210 · **2.045,6** |

> ✎ **2026-08-09 — las cifras de FAR/hora de este doc quedaron corregidas.** El
> agregador calculaba `far_per_hour` con el numerador de todos los negativos y el
> denominador de solo los soak. Los valores correctos son **29,2** (escena) y
> **1.850,8** (sujeto). Detalle: doc 111 §6.

**Cambio de conclusión respecto de la gen. 1** (que tenía 3 clips y el GT sin
corregir): el estrato B **ya no es uniformemente catastrófico**. Con `v04_c02` dentro,
`scene` alcanza F1 0,571 — y **le gana a `subject`**, que compra recall pagando el
doble de precision. Eso refuerza F-108.1 desde el agregado: **no hay una granularidad
mejor, hay una correcta para cada densidad.** En el rodaje G1 dominaba; en este
estrato, no.

### 9.3 Nivel A consolidado — y la cifra que estaba mal

`na1_gdinotiny560_v2short_video`: 8 clips, agregado CR-01 F1 **0,034** / CR-02
**0,023**, contra 0,408–0,479 del bench de imágenes. El derrumbe es **de precision**
(el recall se sostiene en ~0,27).

**El artefacto stale, cuantificado.** `105-nivel-a-estrato-b.json` se había puntuado
con el XML de `v06_c01` anterior a la corrección firmada:

| `v06_c01` CR-02 | STALE | vigente |
|---|---|---|
| violadores en el GT | **37** | **10** |
| recall | 0,108 | **0,300** |

Contaba 27 person-frames como violaciones que no lo eran. Era **la única cifra
publicada de la jornada que estaba incorrecta**, no solo desactualizada.

### 9.4 Higiene y archivado

- **`control_runs`/`tracked` exploratorios comprimidos**: 1.160 MB → **394 MB**
  (−66%), sin perder ningún `eval_*.json`. Precedente del repo respetado.
- **Archivado a `_archived/`** (con README que explica cada carpeta y qué NO está
  ahí): las dos bandejas de entrada de CVAT ya procesadas —`v04_c02` verificada por
  sha256 contra el banco antes de mover— y los artefactos de la **era piloto 18-07**
  (manifiesto `video16_clip10_gt/` + 3 configs de replay). Comprobado que ningún doc
  vigente los cita y que la suite del control-plane sigue en 312 verdes.
- **Supersedidos marcados sin borrar** en `datos/109-SUPERSEDIDOS.md`.

### 9.5 Qué quedó como fuente única

| pregunta | dónde se responde |
|---|---|
| Composición del material de video | `registry/clip_bench.md` §1 y §1.1 |
| Nivel B del estrato B | `results/clip_bench/index.md` §Estrato B |
| Nivel A de todo el video | `results/bench_nivel_a/index.md` §Nivel A sobre clips |
| Qué artefacto reemplazó a cuál | `datos/109-SUPERSEDIDOS.md` |
| Qué está archivado y por qué | `_archived/README.md` |

### 9.6 Lo que sigue abierto

1. **Los docs 103–108 citan cifras de la gen. 1.** Llevan banner de corrección donde
   correspondía, pero sus tablas conservan los números viejos **a propósito**: son el
   registro de lo que se midió cuando se midió. La fuente vigente son los índices.
2. `n = 3 episodios` en 4 clips. La reorganización compró trazabilidad, no poder
   estadístico.
3. Sin cambios: URL por video, y las decisiones de encuadre para el informe.
