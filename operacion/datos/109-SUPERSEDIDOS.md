# Artefactos supersedidos por la reorganización del 2026-08-07 (doc 109)

**Ninguno se borró.** Son la evidencia de los docs que los citan, tal como se
escribieron. Lo que este archivo hace es decir **cuál es la fuente vigente**, para que
nadie los use como cifra actual.

**Regla:** si un doc cita un número, el número vive donde el doc dice. Si querés **la
cifra vigente**, mirá la campaña de la columna derecha.

| artefacto | qué era | estado | fuente vigente |
|---|---|---|---|
| `105-nivel-a-estrato-b.json` | Nivel A de v04_c01/v06_c01/v10_c01 | 🔴 **STALE — cifras de `v06_c01` FALSAS** | `results/bench_nivel_a/na1_gdinotiny560_v2short_video/` |
| `105-nivel-a-piloto.json` | Nivel A de los 4 clips piloto | ⚪ supersedido (consolidado) | ídem |
| `108-nivel-a-v04c02.json` | Nivel A de v04_c02 | ⚪ supersedido (consolidado) | ídem |
| `102-i1-internet-scene-clips/` | campaña I1 **gen. 1** (3 clips) | ⚪ supersedida | `results/clip_bench/i1_…_internet/` (gen. 2) |
| `102-i2-internet-subject-clips/` | campaña I2 **gen. 1** (3 clips) | ⚪ supersedida | `results/clip_bench/i2_…_internet/` (gen. 2) |
| `108-v04c02/` | corridas sueltas de v04_c02 | ⚪ absorbidas | ídem (v04_c02 es parte de la gen. 2) |

## El único que estaba MAL, no solo viejo

**`105-nivel-a-estrato-b.json`** se calculó el 2026-08-06 con el XML de `v06_c01`
**anterior** a la corrección firmada del doc 108 §6 (394 cajas del track 110 pasaron de
`has_vest: false` a `true`). Sus métricas de CR-02 para ese clip cuentan como
violaciones 26 person-frames que **no lo eran**. No es "una versión anterior": es un
número incorrecto, y por eso lleva 🔴.

Los demás son correctos para el alcance con el que se corrieron; simplemente ese
alcance creció.

## Lo que NO está supersedido (y se sigue citando tal cual)

- **Barridos de los docs 104 y 107** (`103-gate-sim/`, `104-barrido-gate/`,
  `107-barrido-knobs/`, `104-i3/i4-base-*`): miden **mecanismo sobre detecciones**, y
  las detecciones no cambiaron con la corrección del GT. Sus docs llevan banner
  aclarando que los conteos absolutos son pre-corrección.
- **Campañas del rodaje** (T1…R6): congeladas contra el freeze `cef5082e`, intactas.

## Nota de formato

Los subdirectorios `control_runs/` y `tracked/` de estas carpetas se comprimieron a
`.tar.gz` (1.160 MB → 394 MB), siguiendo el precedente del repo
(`81-campana-rodaje-dbe-control-runs.tar.gz`). Los `eval_*.json` y `resumen.json` —que
es lo que los docs citan— quedaron sueltos y legibles.
