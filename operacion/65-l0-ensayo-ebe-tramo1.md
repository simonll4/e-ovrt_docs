# 65 — L0 tramo 1: ensayo EBE pre-rodaje con el campeón (2026-07-23)

Primer tramo del L0 del plan maestro (doc 62 §6), ejecutado la misma noche del cierre S1/S2:
corrida EBE 1:1 real de dos planos con **`gdino-tiny-560`** (campeón S2, doc 64) contra la
EZVIZ RTSP, sin actores.

## Resultado: VERDE de punta a punta

- **Orden de disparo verificado**: `POST :8081/api/runs` (`mode: live`,
  `configs/live_ebe_cr01_cr02.yaml`) → `subscribed: true` en el estado ANTES de disparar
  media; después `POST :8080/api/runs` con `bus.enabled: true`.
- **Media** (`run_20260723_024636_dbe_grounding_dino_d4b938`): 30 procesadas / 60 drops
  (evicciones del ring `bounded_freshness` a 15 fps de cámara vs ~3,3 fps de pipeline —
  esperado), `fps_effective` 3.25 (mejor que los 2.8–3.0 del 800), g2a p50 312 ms / p95 414
  ms, **frame 0 g2a 711 ms sin cascada de drops** (el pre-flight `prepare_run` funciona en
  live; antes del fix el frame 0 costaba 3,3 s y 50 drops). Nota: g2a ~60 ms más alto que el
  bench person-only de doc 61 — el caption de 3 clases (person+helmet+vest) alarga la
  inferencia de GDINO; dato a tener para el rodaje (el prompt set real es de 3+ clases).
- **Control** (`control_live_cr01_cr02_20260723T024608Z_7e0673`): 30/30 unidades,
  **`bus_dropped_events: 0`**, `pattern_set_id: cr01_cr02_v2`, `degraded: false`, cierre 1:1
  por `run_finished`, ambos `succeeded`.
- **El camino de alertas se ejercitó entero**: 1 alerta CR-01 `high` emitida
  (`alerts.jsonl`/`.csv`, con `first_evidence_ms`). Escena nocturna sin actor: es una **falsa
  alerta sostenida** — el fenómeno exacto que FAR/hora medirá en fase C (sobre-marca a
  distancia, hallazgo A7). Como ensayo, prueba el circuito detección→episodio→confirmación→
  alerta con contenido real.

## Trampas operativas anotadas para el día del rodaje

1. **Lanzar cada servicio desde la raíz de su repo.** Esta corrida lanzó el media-plane desde
   el workspace y los artefactos cayeron en `projects/runs/` en vez de
   `e-ovrt_media-plane/runs/` (los paths del config resuelven contra CWD — trampa conocida,
   reconfirmada). El run de media de este ensayo quedó en `projects/runs/`.
2. El estado del control-plane usa la clave **`control_run_id`** (no `run_id`) y el terminal
   es `succeeded` — pollers ajenos a eso cuelgan (reconfirmado del dry-run).
3. Un run live del control-plane huérfano responde **409 con `active_run_id`** al reintentar:
   el reintento correcto es reusar ese run (ya está suscripto), no borrarlo.

## Pendiente para el tramo 2 de L0 (con el usuario presente)

- Ensayo mecánico de doble toma (grabar toma A desde la consola + toma B live) con tiempos de
  setup por escena.
- Claqueta de prueba (requiere una persona) → decidir si el stretch de la identidad
  `t_alert = TTFD + t_capture→alert` entra al rodaje.
- Checklist del doc 59 §7 recorrida completa con la config final (`gdino-tiny-560`).
