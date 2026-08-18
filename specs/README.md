# specs/ — Specs de Etapa 4 por módulo

Los specs se escriben **sin alternativas** (regla del doc 03 §9): cada uno parte de
los ADRs de `decisiones/` y solo describe la implementación elegida. Corresponden a
la lista del doc 02 §8, ajustada por los ADRs 001 (E-HYB firme), 002 (G1 demo),
005 (repo propio), 008 (servicio mínimo), 009 (config centralizada) y 011
(cooldown → política de notificación en distribución). Numeración: serie 40.

**Orden de ejecución (ADR-010, 2026-07-09; precisión del mismo día): plataforma
primero — 40 → 41 → 42 → 44 → 43; el 45 (distribución) no bloquea al 43 y corre
tras el 44 en paralelo. El 43 (clip bench) queda escrito y congelado: su
disparador es el cierre del 44 (corridas/configs trazables + runner + reporte).
El material crudo del dataset de videos ya está en proceso de armado, en
paralelo al tramo plataforma.**

## Cola

| # | Spec | Repo dueño | Insumos decididos | Estado |
|---|---|---|---|---|
| 40 | **Plataforma / Etapa 4 (integrador)** — mapa contrato-preliminar↔artefacto real; bus (envelope, topics, END); `experiment_id`; criterio de relojes; diccionario de métricas con estados de aplicabilidad + **`t_capture→alert`/`t_compute-budget`** (la cadena frame→evento medible sin GT, §5.2 — criterio de cierre del tramo plataforma) | transversal (vive acá) | ADR-003/004/006/007 | **Escrito** → [40-plataforma-etapa4-integrador.md](40-plataforma-etapa4-integrador.md) |
| 41 | **control-plane** — G0 (clave `(pattern, source)` + regeneración de fixture/GT); runtime live (`MediaEventSource` jsonl/memory/bus); **servicio mínimo** (POST corrida con config por payload/referencia / GET estado / GET config efectiva); evaluador `direct_evidence` + fusión E-HYB or/and según doc 12 (gating por persona, marca de corroboración, factor de ventana de confirmación); publisher de alertas al bus de distribución; `experiment_id` en eventos; TTFA; alineación pattern set al informe (severidades/ventanas, doc 08 §2.1) | `e-ovrt_control-plane` | ADR-001/002/003/007/008/009 | **Escrito** → [41-control-plane.md](41-control-plane.md) |
| 42 | **media-plane** — `BusPublishingArtifactWriter` (ZeroMQ + secuencia + END); **tracker liviano portado de labs** (`track_id` opcional aditivo en `media.detection.v1`); propagación `experiment_id`; verificación de config por payload en `POST /api/runs` (catálogos por id se conservan) | `e-ovrt_media-plane` | ADR-002/003/004/009 | **Escrito** → [42-media-plane.md](42-media-plane.md) |
| 43 | **datasets — clip bench** — selección/grabación escenificada (H2), formato GT temporal escena-condición (+identidad mínima solo en los 2–3 clips de la demo G1), doble anotación 20%+kappa, 8–15 clips | `e-ovrt_datasets` | ADR-002/010; doc 07 H2/H8 | **Escrito; se ejecuta al cierre del spec 44 (ADR-010)** → [43-clip-bench-gt-temporal.md](43-clip-bench-gt-temporal.md) |
| 44 | **experimental-setup** — **config experimental centralizada** (estructura por experimento: manifiestos, run configs de ambos planos, pattern/prompt/tuning sets); manifiesto paraguas + runner CLI (HTTP a ambos servicios); generador de reporte consolidado; prompt sets `eind_v1`/`edir_v1` construidos según doc 12 §2 (Tabla C.1, ejes, revisión del usuario antes de congelar); **webconsole como superficie de gestión primaria**: CRUD de configs, disparo en ambos planos, vista de alertas, agrupación por experimento, **rediseño UI/UX (navegación por experimento)** | `e-ovrt_experimental-setup` | ADR-001/004/006/008/**009** | **Escrito** → [44-experimental-setup.md](44-experimental-setup.md) |
| 45 | **distribución** — repo nuevo (`e-ovrt_alert-distribution`): bus control→distribución, `NotificationEnvelope`, ledger, canal MQTT, retry mínimo. ✎ 2026-08-18: **+§9 servicio HTTP** (`serve` en `:8082`, ADR-019, aditivo — CLI y subproceso intactos), implementado y verificado | repo nuevo | ADR-005 · ADR-019 | **Escrito** → [45-distribucion-alertas.md](45-distribucion-alertas.md) |

## Reglas

1. Un spec no repite el análisis: **cita el ADR** y va directo a contratos,
   módulos, configs y criterios de terminado (evidencia en corrida, doc 02 §2.6).
2. Cambios de contrato siempre **aditivos** (campos opcionales) — regla que ya
   siguen ambos planos.
3. Cada spec cierra con su lista de verificación de terminado y las métricas que
   habilita (mapeadas al diccionario del spec 40).
