# Verificación end-to-end: video real y RTSP real (no simulado)

- **Fecha:** 2026-07-10
- **Por qué existe este doc:** todo lo verificado en el doc 34 (gate F1=1.0, ADR-012
  confirmado, invariante 137→77) corrió sobre un fixture sintético de 12 líneas y un
  `detections.jsonl` **precomputado**. Ningún modelo se había cargado, ni un frame de
  video ni de cámara había pasado por el motor nuevo. Este doc cierra esa brecha: es la
  primera corrida de la sesión con **inferencia real** (GDINO-tiny en GPU) y la primera
  contra una **cámara RTSP real**.

## 1. Qué se ejecutó

Se levantó el media-plane como servicio real (`uvicorn`, `EOVRT_MODEL_REF=grounding-dino/gdino-tiny`,
`cuda:0`) y se dispararon dos corridas por `POST /api/runs`, encadenadas después al motor
nuevo del control-plane vía replay.

### 1.1 Video real (`data/samples/videos/recorte-1.mp4`)

- Ingesta: `video_file` sobre el archivo real (15 MB, en disco).
- Modelo: GDINO-tiny, `cuda:0`, cargado al arranque del servicio (no `mock`).
- Resultado (`run_20260710_011320_dbe_grounding_dino_4be2cc`): **733 frames, 0 fallos**,
  15.959 detecciones (8.002 personas, 5.919 cascos, 2.038 chalecos), 179 s en GPU,
  4,09 fps efectivos, `gpu_memory_peak_mb: 1745`.
- Coincidió en frames y duración con una corrida anterior sobre el mismo video
  (`run_20260704_210226_dbe_grounding_dino_7febb7`, desde entonces podada del disco) —
  misma fuente, resultado consistente.

**Aliasing de `det_NNN`, medido sobre esta corrida fresca:** `det_000001` recorre
**1831 px** de un frame de ~1920 px de ancho. No es un artefacto de una corrida vieja: se
reproduce con inferencia nueva. Es la medición, no el argumento, de por qué G0 hace falta.

> **Nota (2026-07-10):** las dos corridas de esta seccion
> (`run_20260710_011320` y `run_20260710_011715`) **sobreviven** en disco; son la evidencia
> mas fresca del proyecto. Corridas mas viejas del media-plane fueron podadas.

### 1.2 Replay del video real por el motor G0

Config: `configs/verify_video_g0_fresh.yaml`, pattern set `cr01_cr02_v2_probe.yaml`
(bandas de `v2`: confirm 4 s / 7 s — spec 41 §7, sin calibrar).

| | |
|---|---|
| `units_processed` | 733 |
| `errors_count` | 0 |
| `alerts_count` | 2 |
| CR-01 | confirma en **t=4000 ms** exacto, clave `CR-01:recorte-1.mp4` |
| CR-02 | confirma en **t=7000 ms** exacto, clave `CR-02:recorte-1.mp4` |
| `degraded` | `False` |
| `pattern_evaluation` | `{state: computed, causes: []}` |

La clave de estado es estable y constante durante los 733 frames — nunca depende de
`det_NNN`. Coincide exactamente con la corrida sobre el `detections.jsonl` precomputado
de otra sesión previa (doc 34 §2, misma fuente): la implementación es determinista frente
al mismo input, generado por inferencia real o no.

### 1.3 Cámara RTSP real (`192.168.1.5:554`)

- La cámara estuvo apagada al inicio de la sesión (`no route to host`); el usuario la
  reconectó y el puerto 554 respondió.
- Ingesta: `rtsp` contra la URL real (credenciales en `configs/runs/local/rtsp_camera.env`,
  no versionadas). `run.max_units: 15` como tope de seguridad.
- Resultado (`run_20260710_011715_dbe_grounding_dino_fc965b`): **succeeded, 0 fallos**,
  3 unidades procesadas (de 15 pedidas — la fuente cortó antes; no es un error de
  contrato, `errors_count: 0`), `source_type: video_frame`, detecciones reales
  (persona + chaleco).
- **`timestamp_ms` es reloj de pared real** (epoch ms, ~2026-07-10 01:17 UTC) — confirma
  `source_clock: wallclock` para RTSP tal como documenta la spec 42 §5, no una
  simulación de timestamps.

### 1.4 Replay de la corrida RTSP por el motor G0

Config: `configs/verify_rtsp_g0_fresh.yaml`. `units_processed: 3, errors_count: 0,
alerts_count: 0` — correcto: la ventana capturada (3,19 s) es menor que el umbral de
confirmación de CR-01 (4000 ms), así que la condición queda en `candidate`, no confirma.
No es una falla: es la histéresis operando como se espera con una ventana corta.

## 2. Qué queda demostrado que antes no lo estaba

- El motor G0 corre sobre **inferencia real**, no solo sobre fixtures ni sobre JSONL
  precomputado de sesiones anteriores.
- El aliasing de `det_NNN` que motiva G0 se **midió**, no se asumió, sobre una corrida
  fresca.
- La cadena **cámara RTSP real → GDINO real → motor G0** funciona sin errores de
  contrato, con reloj de pared real.
- El camino DBE (archivo) y el camino "en vivo por archivo intermedio" (RTSP → JSONL →
  replay) están verificados. El camino **EBE real** (bus ZeroMQ, servicio del
  control-plane consumiendo en vivo) **sigue sin existir** — es el plan 2, no este.

## 3. Lo que esto NO prueba

- No valida el modo `granularity: subject` con datos reales: sigue sin existir un
  productor de `track_id` (doc 34 §4.1, sin cambios).
- No es una corrida de calibración: `cr01_cr02_v2_probe.yaml` usa las bandas
  declaradas por la spec 41 §7 pero no está calibrado; los números de confirmación
  (4000/7000 ms exactos) son deterministas dado el input, no una validación de que
  esos umbrales sean los correctos para producción.
- La corrida RTSP fue de 3 frames en ~3 s: no valida estabilidad de la reconexión ni
  comportamiento sostenido en vivo (eso es instrumentación y runtime live, plan 2).
- El servicio del media-plane se levantó y se apagó manualmente en esta sesión; no
  hay corrida de tipo `live` desde el control-plane consumiéndolo por bus — ese
  camino no existe todavía.

## 4. Evidencia

Corridas en `e-ovrt_media-plane/runs/run_20260710_011320_dbe_grounding_dino_4be2cc/` y
`run_20260710_011715_dbe_grounding_dino_fc965b/`; replays en
`e-ovrt_control-plane/runs/verify_video_g0_fresh_20260710/` y
`verify_rtsp_g0_fresh_20260710/`. Configs en `e-ovrt_control-plane/configs/verify_*.yaml`
y `patterns/cr01_cr02_v2_probe.yaml` (explícitamente marcado como probe, no el pattern
set `v2` oficial de la spec 41 §7, que requiere calibración).
