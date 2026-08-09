# 111 — El lote de internet queda CERRADO: 13 de 14 con GT (banco 47)

**Fecha:** 2026-08-09. **Insumo:** las dos últimas tandas de CVAT (7 clips + `v02_c01`),
más dos decisiones del usuario. **Salida:** el estrato B completo y congelado del lado
del material — **no queda ninguna anotación pendiente** — y la **gen. 3 CORRIDA**: los
resultados finales del estrato B están en §6.

Este doc es el que citan los `clip.yaml` de la tanda ("GT HUMANO 2026-08-09, doc 111")
y el registry §1.1.

---

## 1. Qué entró

**Tanda 1 (7 clips):** `v01_c01`, `v01_c02`, `v03_c01`, `v04_c03`, `v05_c01`,
`v07_c01`, `v09_c01`. **Tanda 2:** `v02_c01`. Todos exports **task-level**, alineados
frame-perfecto con su `info.json`, verificados byte a byte contra el banco al archivar
(`_archived/anotaciones-2026-08-09/`).

| clip | duración | GT | nota |
|---|---|---|---|
| `v01_c01` | 37,2 s | 1 ep CR-01 `31.567 → 37.200 ms` | **CENSURADO** (A1: exige llegar a 45,6 s) — no aporta recall |
| `v01_c02` | 32,8 s | 1 ep CR-01 `0 → 15.633 ms` | **evaluable**; onset en t=0 ⇒ TTFD artefacto |
| `v02_c01` | 48,9 s | negativo | sin un solo `false` en 7 tracks; ni sub-umbral |
| `v03_c01` | 22,0 s | negativo | |
| `v04_c03` | 32,1 s | negativo | **el único negativo NOCTURNO del banco** — eje nocturno a n=3 |
| `v05_c01` | 78,5 s | negativo | el negativo más largo tras el soak; 17 tracks |
| `v07_c01` | 26,9 s | negativo | |
| `v09_c01` | 45,2 s | negativo | |

**Curación: 6 de 8 acertaron** (los dos que erró eran justamente los positivos, ambos
`P5`→`P1`). Acumulado del lote: **7 de 13** — la mitad. Los positivos audité con la caja
dibujada sobre el frame (regla F-94.1): el de `v01_c02` es plausible a la vista (cabeza
descubierta, compañero con casco al lado como contraste); el de `v01_c01` queda **marcado
para revisión** en su `clip.yaml` (sujeto dentro del edificio, a contraluz — misma
familia que `v03_c02`).

**Banco: 39 → 47 clips** (`manifest.yaml` sha256 `299ccc19…`), reportable, freeze
189/189. Composición: A 34 · B 13 · **40 episodios** (CR-01 32 / CR-02 8) · negativos 13
· soak 1 (`v06_c01`, 0,1027 h) · tiempo negativo total **0,2544 h**.

## 2. El caso testigo: el re-export de `v03_c02` — y la política que fijó

En la tanda 1 vino también `v03_c02`, **que ya estaba en el banco con 4 correcciones
firmadas** (orden del usuario, doc 110). El export llegó — como corresponde — **sin esas
correcciones**: CVAT nunca se tocó, porque la corrección se hizo del lado del repo.
Integrarlo a ciegas habría revertido una decisión firmada y devuelto al banco un episodio
CR-01 falso de 4.000 ms exactos, **en silencio**.

**Decisiones del usuario (2026-08-09):**
1. **Queda la versión corregida.**
2. **Las anotaciones del repo son la fuente de verdad** — no el estado de CVAT.

De ahí salieron tres piezas:
- **Política escrita** en `registry/clip_bench.md` §2.2 (tabla de qué ruta manda; y la
  aclaración de que esto **va a volver a pasar y es lo esperable**: todo clip con
  correcciones firmadas se re-exporta sin ellas).
- **Guard ejecutable**: `apply_attribute_corrections.py --check` — no escribe nada, sale
  1 si alguna corrección firmada no está aplicada. Verde sobre `v03_c02` (4) y `v06_c01`
  (1); detecta el revert sobre el export crudo archivado. +3 tests (suite 307).
- **Caso testigo conservado** en `_archived/anotaciones-2026-08-09/LEEME.md` con el
  comando para reproducir la detección.

## 3. `v08_c01`: exclusión declarada, nunca silenciosa

**Decisión del usuario:** no se anota. El lote cierra en **13/14**. Registrado como
**cobertura no ejecutada con causa** (doc 57 §7.6), no como pendiente:

- `datasets-videos/v08_c01.clip.yaml` lleva el bloque `excluded: true` con causa, firma
  (`excluded_by: simonll4`) y fecha, más el banner y las instrucciones por si alguna vez
  se anota.
- Registrado también en el bloque de comentarios del `manifest.yaml` y en el registry
  §1.1. Su `.mp4` y su pre-anotación quedan en disco; sin GT humano no es promovible y
  ninguna campaña lo toca.

## 4. La revisión de punta a punta previa a la gen. 3 (este mismo día)

Antes de correr nada, batería completa — y encontró **una** desalineación real:

- **`gt/v06_c01.json` no era re-derivable bit a bit** desde los artefactos del banco:
  al re-derivar, el bloque `annotation.attribute_corrections` difería. Causa: el
  rationale del `clip.yaml` se editó el 08-09 (nota de fuente-de-verdad) **después** de
  derivar el GT, y `assemble_clip_gt` embebe el bloque `annotation` en el GT. Episodios,
  sub-umbral y `negative` eran idénticos — cero impacto métrico. **Realineado**:
  re-derivado y re-promovido; el manifest volvió al mismo sha (`299ccc19…`).
- Todo lo demás verde: validadores en ambos modos, freeze 189/189, **los 13 GT del
  estrato B re-derivan idénticos** desde el banco, lab ≡ banco byte a byte, guard
  `--check` verde en los 2 clips con correcciones, el evaluador del control-plane carga
  los 13 GT (5 episodios), runner y `gen3.sh` compilan, pattern sets y catálogo del
  modelo presentes, pesos en disco, GPU libre, 891 GB de disco.
- **Auditoría de organización** (`datos/109-verificar-organizacion.py`, reejecutable):
  las 6 reglas del doc 109 se cumplen — estratos en su lugar, campaña citable vs
  evidencia exploratoria, fuente de verdad, integridad lab↔banco, exclusiones
  declaradas, banco verificable.

**Lección chica que deja la desalineación:** editar el `clip.yaml` de un clip ya
promovido exige re-derivar su GT aunque el cambio sea un comentario dentro de
`annotation` — el GT lo embebe. El chequeo de re-derivación de la batería lo caza.

## 5. Estado final y qué sigue

| | |
|---|---|
| Material | **CERRADO** — 47 clips `gt_ready` (34 rodaje + 13 internet), piloto ×4 en `_retired/` para Nivel A, `v08_c01` excluido con causa |
| Corridas | ✅ **HECHAS** — gen. 3 corrida el 2026-08-09 (72 min GPU, 13 clips, exit 0). Resultados en §6 |
| Propagación | ✅ hecha: `generations: gen 3` en los dos `campaign.yaml`, secciones de `results/clip_bench/index.md` y `results/bench_nivel_a/index.md` reescritas, registry §2.1 y L1 al día, banners de corrección en 108/109 |

Pendientes que no bloquean: revisión visual de `v01_c01` (marcada en su yaml), URL por
video (usuario), y las decisiones de encuadre del informe.

---

## 6. LA CORRIDA gen. 3 — resultados finales del estrato B (2026-08-09, 06:0X–07:2X)

`110-estrato-b-gen3.sh` corrió completo, exit 0. **72 min de GPU** para los 13 clips en
una sola sesión (`v06_c01` se llevó 30). Preflight verde, servicios levantados por el
propio script, las 8 etapas sin intervención.

### 6.1 Nivel B

| | I1 `scene` | I2 `subject` |
|---|---|---|
| recall (4 eps evaluables de 5) | 0,750 | **1,000** |
| precision | **0,375** | 0,111 |
| **F1** | **0,500** | 0,200 |
| matched / missed / FP | 3 / 1 / 5 | 4 / 0 / 32 |
| t_alert · SDR · TTFD | 4.767 ms · 0,890 · 16,5 ms | 5.800 ms · idem · idem |
| FP sobre los 9 negativos | 21 | 304 |
| **FAR/hora** (soak 0,1027 h) | **29,2** | **1.850,8** |

Por escenario: **P6 (`v04_c02`) es el único caso limpio de todo el estrato** — recall
1,000 y **0 FP en ambas granularidades**. P1 (3 clips): `scene` 0,500 con 5 FP,
`subject` 1,000 con 32 FP. P5 (9 negativos): 21 vs 304 FP.

> **F-111.1 — con el lote completo, `scene` le gana a `subject` y la brecha se agranda.**
> F1 0,500 vs 0,200 (en la gen. 2, con 4 clips, era 0,571 vs 0,400). `subject` compra el
> episodio que falta —recall 0,750 → 1,000— pagando **6× más FP en positivos y 14× más
> en negativos**. En el rodaje G1 dominaba con F1 0,930; en obra real no guionada, no.
> Consolida F-108.1 desde el agregado del lote entero: **no hay una granularidad mejor;
> hay una correcta para cada régimen de densidad.**

**Determinismo re-confirmado (F-109.1):** los 4 clips que ya se habían inferido en la
gen. 2 dieron detecciones **idénticas** (572 / 840 / 11.087 / 1.771 frames).

### 6.2 Nivel A (17 clips: 13 estrato B + 4 piloto)

Agregado **CR-01 F1 0,039** (P 0,021 / R 0,371) y **CR-02 F1 0,020** (P 0,010 / R 0,271),
contra 0,408–0,479 del bench de imágenes. **El derrumbe es de precision; el recall se
sostiene.** Mejores celdas: `video15_clip01` CR-02 F1 **0,381** (0% unknown — material
plenamente juzgable), `v01_c02` CR-01 **0,317**, `v01_c01` CR-01 **recall 0,846**.

### 6.3 ⚠️ Un BUG de métrica encontrado al revisar las cifras — y corregido

Los FAR/hora que imprimió la corrida (204,6 escena / 2.961,3 sujeto) no cerraban: el
agregador contaba **los FP de los 9 clips negativos** y los dividía por **las horas del
único clip soak**. Dos bases distintas en la misma fracción.

```python
# antes (aggregate_clip_campaign.py:119)
"far_per_hour": _safe(neg_fp, soak_ms / 3_600_000.0)   # neg_fp = TODOS los negativos
```

Con 1 soak y 1 negativo corto (gen. 2) la distorsión era 1,2× y pasó desapercibida; con
9 negativos infla **7×**. **Corregido**: numerador y denominador salen del mismo
conjunto, y se expone `far_per_hour_all_negatives` como base informativa. Test de
regresión que falla con el código viejo (suite 308).

| | publicado antes | **correcto** | informativo (todos los negativos) |
|---|---|---|---|
| `scene` | ~~48,7~~ / ~~204,6~~ | **29,2** | 96,1 |
| `subject` | ~~2.045,6~~ / ~~2.961,3~~ | **1.850,8** | 1.390,5 |

> **F-111.2 — el FAR/hora corregido es idéntico en gen. 2 y gen. 3**, porque depende
> solo del clip soak, que es determinista. Es una propiedad deseable: la métrica no se
> mueve al agregar clips cortos. **Las cifras de FAR de las gen. 1/2 que circularon
> (48,7 y 2.045,6) eran incorrectas** — corregidas en el índice, el registry y con
> banner en los docs 108 y 109, que conservan su texto original por trazabilidad.

**D-90.1 sigue precisada, no derogada:** con 0,1027 h y la regla de 3 harían falta 3,0 h
para sostener la cota "≤1 FA/hora". Lo que cambió es que ya no se declara la métrica no
medible: se reporta el valor y **se dice que refuta la operabilidad**.

### 6.4 Artefactos y propagación

`results/clip_bench/{i1,i2}_…_internet/` (`metrics.json` gen. 3 · `metrics.gen2.json`
preservado · `campaign.yaml` con `generations: 1/2/3` · `evals/` · `provenance.json`) ·
`results/bench_nivel_a/na1_gdinotiny560_v2short_video/metrics.json` (17 clips) ·
evidencia cruda en `datos/110-estrato-b-gen3/`.

Propagado: sección del estrato B de `results/clip_bench/index.md` reescrita entera,
índice de Nivel A reescrito, registry §2.1 y bloque L1 al día, banners de corrección en
108/109.
