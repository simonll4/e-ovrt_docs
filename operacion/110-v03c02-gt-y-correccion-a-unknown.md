# 110 — `v03_c02`: el positivo más frágil que el banco casi tuvo, y la primera corrección hacia `unknown`

**Fecha:** 2026-08-07, noche. **Insumo:** el equipo anotó `v03_c02` en CVAT (task 13) y
el usuario, tras revisar el video, pidió corregir un sujeto: *"en el frame 492 aparece
person 3, hay que ajustarle `has_vest=true` y `has_helmet=unknown` en todos los frames"*.
**Salida:** banco **39 clips**, `v03_c02` **negativo**, y un hallazgo sobre el propio GT.

**Estado: el material está listo; las corridas NO se ejecutaron** (decisión de
secuenciación del usuario). Todo lo que falta corre con un comando — §4.

---

## 1. Integración

Export **task-level** (task 13, `<size>` 3147 = `n_frames` del `info.json`, alineado
exacto), 4 tracks `person`. `split_cvat_project.py` **no** se aplica: sería el error
simétrico del doc 102 §1.1. Cadena estándar más el paso de corrección:

`corrected/` → **`apply_attribute_corrections`** → `derive_clip_gt` (4000/7000) →
`validate` (0 errores) → `promote_clip` (`gt_ready` derivado, no impuesto) →
`build_clip_bench` → `sha256sum -c` (**157 OK / 0 FAILED**).

| | |
|---|---|
| sha256 del export CRUDO | `4aff825e0ba07634…` (copia intacta fuera del repo, en el drop del usuario) |
| sha256 del XML corregido | `06bfe6a49e665de3…` (el que promovió al banco y firma `provenance.xml_sha256`) |
| `manifest.yaml` | `4437eb6d…` → **`c1791c9b…`** (38 → 39 filas; ninguna fila previa cambió) |

## 2. La corrección, y por qué era necesaria

**El export crudo dejaba 1 episodio CR-01 de `16.400 → 20.400 ms`.** Duración:
**4.000 ms EXACTOS** contra un `confirm_after_ms` de 4.000 ms. Lo sostenía un solo
track.

**Identificación del sujeto.** El anotador lo nombró por el número de la UI de CVAT
("person 3"), que **no viaja en el XML**. El ancla que sí viaja es el frame de
aparición: de los 4 tracks, **uno solo aparece en el frame 492** (track `id=0`,
frames 492–706, 202 cajas, hueco de `outside` en 659–671). Sin ambigüedad.

**Auditoría visual antes de tocar nada** (regla F-94.1 — no afirmar sobre una clase sin
mirarla). Frames 492, 618 y 690 extraídos con la caja del track dibujada:

- el sujeto es el **operador sentado en la cabina de la excavadora**, filmado a través
  del vidrio, con el marco de la cabina cruzándole la cabeza;
- **chaleco naranja fluorescente, claramente visible** en el tramo despejado ⇒ el
  `has_vest: false` de las 202 cajas era **error de anotación**;
- **la cabeza no es observable en ningún frame** (marco + reflejo + su propio brazo) ⇒
  el `has_helmet` venía partido en conjeturas: `false` en 190 cajas y `true` en 12
  (frames 612–623). Las dos son conjeturas, con signo opuesto.

**Cuatro entradas de `attribute_corrections`, no dos.** El guard de `previous_value`
exige que el valor declarado coincida **caja por caja**, y `has_helmet` venía en tres
tramos (`false` 492–611 / `true` 612–623 / `false` 624–706). Eso obliga a firmar cada
tramo por separado — y está bien que obligue: cada conjetura queda con su propia firma
y su propio rationale. Total: **404 cajas modificadas** (202 de `vest` + 202 de
`helmet`), **idempotente verificado** (segunda pasada: 0 cambios, sha256 estable).

## 3. Resultado y efecto en el banco

**`v03_c02` es NEGATIVO**: 0 episodios, **3 eventos sub-umbral** — CR-02 de 800 ms
(`21.500 → 22.300`, del track 1) y CR-01 + CR-02 de 33 ms en `t=0`, de un track residual
de una sola caja visible (33×58 px pegada al borde superior, resto de la
pre-anotación). Ninguno debe alertar. Los tracks residuales **no se tocaron**: son datos
del anotador, no producen episodios, y borrarlos sin firma sería exactamente lo que la
ceremonia de correcciones existe para evitar. Si el equipo quiere limpiarlos, se limpian
en CVAT y se re-exporta.

| banco | antes (38) | ahora (**39**) |
|---|---|---|
| Bloque B (obra real) | 4 | **5** |
| Escenario P5 | 4 | **5** |
| Positivos / negativos / soak | 32 / 6 / 1 | 32 / **7** / 1 |
| Episodios | 38 (CR-01 30 · CR-02 8) | **38, sin cambios** |
| Duración total | 1.548.403 ms | **1.653.303 ms** (27:33) |
| Duración negativa | 0,1548 h | **0,1840 h** |
| Denominador FAR/hora | 0,1027 h | **0,1027 h, sin cambios** |

**No es soak.** 104.900 ms < 5 min (doc 57 §3.2 G1), así que engorda el tiempo negativo
*informativo* pero **no el denominador de FAR/hora**. Su rol es **control de falsos
positivos sobre obra real**: cualquier alerta de una campaña sobre este clip es un FP con
causa auditable.

### Hallazgos

**F-110.1 — el banco casi incorpora un positivo que no debía existir.** Un episodio de
4.000 ms contra un umbral de 4.000 ms, sostenido **íntegramente por atributos no
observables**: un frame menos de conjetura y no existía; un `true` de más en el tramo
612–623 y tampoco. Sacarlo **endurece** el banco. Regla que queda: **un episodio cuya
duración iguala el umbral de confirmación se audita visualmente antes de entrar al
banco** — la aritmética lo admite y el material no lo sostiene.

**F-110.2 — primera corrección firmada hacia `unknown`.** `attribute_corrections` nació
(doc 108 §6) para arreglar un `false` que debía ser `true`. Acá hace el trabajo
epistémicamente **opuesto**: borrar una conjetura y dejar constancia de que el estado no
es determinable. Es la misma ceremonia para las dos direcciones, y debe seguir siéndolo:
*la incertidumbre no fabrica una violación, y tampoco fabrica un cumplimiento.*

**F-110.3 — la curación sigue perdiendo contra el GT humano: 1 de 5.** De los 5 clips
del estrato B, sólo `v10_c01` confirmó su escenario curado sin intervención; 2 lo
contradicen de plano (`v04_c01` P8→P1, `v04_c02` P5→P6) y 2 vuelven a P5 **sólo después
de una corrección firmada** (`v06_c01`, `v03_c02`). La etiqueta `scenario` de este lote
no es un dato hasta que hay GT.

**F-110.4 — el número de objeto de CVAT no es una identidad.** "person 3" no viaja en el
XML; el frame de aparición sí. Cuando el anotador nombra un sujeto por el número de la
UI, se resuelve por frame de aparición y **se anotan los dos** en el `clip.yaml`, que es
lo que hace auditable la corrección meses después.

## 4. Lo que falta correr — un comando

```bash
bash docs/operacion/datos/110-estrato-b-gen3.sh
```

Hace la campaña **gen. 3** del estrato B de punta a punta y sin intervención: deriva la
lista de clips **del manifest del banco** (bloque B en `gt_ready`), preflight (validate +
freeze, falla cerrado), levanta los servicios, **I1 scene** (inferencia fresca de los 5
en UNA sesión), **verificación de determinismo** contra la gen. 2 del doc 109, **I2
subject** (reusa las cajas), agregación a `metrics.json` de las dos campañas (la gen. 2
queda al lado como `metrics.gen2.json`) y **Nivel A** del estrato B + consolidado con el
piloto (9 clips).

**Costo:** ~53 min de GPU. `v06_c01` se lleva 33 (11.087 frames) y `v03_c02` ~10 (3.147
frames a los ~5,0 fps medidos en la gen. 2). El resto son minutos.

**Por qué re-corre los 5 y no sólo el nuevo:** una campaña citable tiene UNA procedencia
(un hardware, una sesión, un prompt set congelado). Mezclar la inferencia de hoy con la
de ayer en la misma tabla es el desorden que el doc 109 §1 vino a arreglar. Para una
mirada rápida y NO citable: `CLIPS=v03_c02 bash …/110-estrato-b-gen3.sh`.

> **Secuenciación recomendada:** quedan **9 clips del lote sin anotar** y el script toma
> la lista del manifest, así que **conviene correr la gen. 3 una sola vez, cuando el lote
> esté completo**. Correrla por cada clip que llega cuesta ~1 h de GPU por vez y obliga a
> re-tocar los mismos 4 índices. `v03_c02` ya está en el banco: no se pierde nada
> esperando, y el banco es la fuente de verdad, no las campañas.

**Validación out-of-sample que este clip habilita** (pendiente desde el doc 107): la
celda combinada `gate` + `min_subject_confidence 0,50` + persistencia **no se corrió a
propósito** para no sobre-ajustar in-sample. Los clips nuevos son la muestra fuera de
calibración: se mide con los umbrales **ya fijados**, sin re-barrer.

## 5. Lo que hay que escribir a mano después de correr

1. `campaign.yaml` de I1 e I2: entrada `generations:` **gen 3** (fecha, 5 clips, manifest
   sha `c1791c9b…`) y actualizar `gt_bank` / `gt_note`.
2. `results/clip_bench/index.md` y `results/index.md`: filas de I1/I2.
3. `registry/clip_bench.md` §2.1: **quitar el aviso** de "`v03_c02` en ninguna campaña".
4. Este doc: pegar cifras y cerrar §4.

## 6. Estado de los artefactos

| artefacto | ruta |
|---|---|
| ficha con la corrección firmada | `datasets-videos/v03_c02.clip.yaml` |
| XML corregido (staging) | `datasets-videos/corrected/v03_c02.xml` |
| GT `clip_gt.v2` | `datasets-videos/gt/v03_c02.json` |
| banco | `datasets/processed/clip_bench/{meta,preann,annotations,gt}/v03_c02.*` |
| export crudo de CVAT | `~/projects/v03_c02/annotations.xml` (fuera de los repos; el corregido es el que manda) |
| runner de la campaña | `docs/operacion/datos/110-estrato-b-gen3.sh` |

**Sin commitear** (regla de la casa: los commits los pide el usuario).
