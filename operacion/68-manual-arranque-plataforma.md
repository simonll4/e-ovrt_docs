# 68 — Manual de arranque de la plataforma (live / EBE)

**Fecha:** 2026-07-24. **Propósito:** checklist operativo para levantar la plataforma
completa y dejar lista una corrida en vivo, de cámara a evaluación de alertas.
Fuentes: docs 37 (bus/live), 38 (servicio control-plane), 67 (EBE verificado).

## 0. Precondiciones

- Disco: ≥ 20 GB libres en el destino de grabación/runs.
- **Cada servicio se levanta desde la raíz de su propio repo** (si no, los `runs/`
  quedan fuera de lugar).
- Modelo campeón para live: `grounding-dino/gdino-tiny-560` (doc 64).
- Prompt set congelado: `cr01_cr02_v2_short` (frozen, sha256 en el YAML).
- Pattern set: **`cr01_cr02_v2` siempre, nunca `v1`** (v1 desalinea umbrales con
  `derive_clip_gt` → falsos `missed`, F-DR9).

## 1. Arranque de servicios (en este orden)

```bash
# 1) media-plane (:8080) — el modelo carga UNA vez al startup
cd ~/projects/e-ovrt_media-plane
EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve
make smoke        # /healthz + /readyz deben responder ok/ready

# 2) control-plane (:8081) — sin modelo, readyz siempre ready
cd ~/projects/e-ovrt_control-plane
.venv/bin/eovrt-control serve --port 8081

# 3) webconsole — BFF (:8090) y frontend (:5173)
cd ~/projects/e-ovrt_experimental-setup/webconsole/backend
.venv/bin/uvicorn eovrt_webconsole.app:create_app --factory --port 8090
cd ../frontend && npm run dev
```

Tras cambios de frontend: Ctrl+Shift+R en el navegador. Entrar por `/`
(deep-links directos dan 404 en dev).

## 2. Cámaras

| Cámara | IP | Nota |
|---|---|---|
| RTSP DVR (EZVIZ) | 192.168.1.5 | tope real ~15 fps |
| OAK-D Pro PoE | 192.168.1.50 | preset `fps: 30` → ~13 fps reales; tarda ~9 s en conectar |

- `ping` a ambas antes de arrancar.
- Presets en `e-ovrt_experimental-setup/cameras/*.yaml` (gitignorado: credenciales
  RTSP en claro). El `{plugin, config}` del preset mapea 1:1 al bloque `ingest`.
- Encuadre: usar el preview de la consola (`/cameras`). Preview y run son
  mutuamente excluyentes (409 `preview_active` / `run_active`).

## 3. Lanzar la corrida live (EBE) — orden NO negociable

Desde la consola (`/experiments`, manifiesto con `runs.control.mode: live`) o a mano:

1. **Control-plane PRIMERO**: `POST :8081/api/runs` con
   `{"mode": "live", "config": {…, input.type: bus}}`. El 201 implica que el
   `BusSource` ya está suscripto (construirlo ES suscribirse). Config de
   referencia: `e-ovrt_control-plane/configs/live_ebe_cr01_cr02.yaml`.
2. **Confirmar suscripción**: `GET :8081/api/runs/current` → `subscribed: true`.
   Si no, abortar sin tocar el media-plane (PUB/SUB descarta en silencio lo
   publicado antes del SUBSCRIBE).
3. **Media-plane DESPUÉS**: `POST :8080/api/runs` con `bus: {enabled: true}`,
   `ingest` del preset de cámara, `prompts` = `cr01_cr02_v2_short`, y
   `ingest.config.source_id = <clip_id>` (contrato con el GT).
4. **Cierre 1:1**: al frenar el run de media (`POST :8080/api/runs/{id}/stop` o
   fin de fuente), emite `run.lifecycle.v1/run_finished` y el control cierra solo
   (fallback: polling o `idle_timeout_s: 300`).

**Antes de desarmar la escena**: verificar en el `summary.json` del control
`bus_dropped_events == 0` y que la alerta esperada se emitió.

## 4. Artefactos

- Media: `e-ovrt_media-plane/runs/<id>/` — `detections.jsonl` (verdad del bus),
  `metrics.jsonl`, `summary.json`, `dropped_units.jsonl`.
- Control: `e-ovrt_control-plane/runs/<id>/` — `alerts.jsonl`, `alerts.csv`,
  `pattern_events.jsonl`, `pattern_progress.jsonl`, `effective_config.yaml`,
  `summary.json` (`media_run_id`, `scenario: EBE`, `bus_dropped_events`, `degraded`).

## 5. Evaluación de alertas (offline, tras la corrida)

```bash
cd ~/projects/e-ovrt_control-plane
.venv/bin/eovrt-control evaluate-alerts \
    runs/<control_run>/alerts.jsonl <ground_truth.json> \
    -o temporal_evaluation.json \
    --detections ../e-ovrt_media-plane/runs/<media_run>/detections.jsonl \
    --patterns configs/patterns/cr01_cr02_v2.yaml
```

- `--detections`/`--patterns` habilitan SDR y TTFD; sin ellos solo P/R/FAR-hora.
- `--patterns` recibe el **YAML de patrones**, nunca `pattern_events.jsonl`.
- GT v2 = episodios en ms de `derive_clip_gt` (video-gt-lab); el matching casa
  por `source_id == clip_id`. Estado actual del banco: `gt_preliminary`.

## 6. Trampas conocidas (todas ya mordieron)

1. Invertir el orden de los POST pierde eventos iniciales sin error visible.
2. Pattern set v1 → falsos `missed` silenciosos. Siempre v2.
3. Nunca cerrar un socket ZeroMQ desde otro hilo con `recv_multipart` en vuelo
   (SIGABRT); usar `request_stop()`.
4. Servicios levantados fuera de la raíz de su repo → artefactos perdidos.
5. `--patterns` con el JSONL de eventos revienta la evaluación.
6. OAK-D viene de fábrica con IP estática 169.254.1.222 (no DHCP).
