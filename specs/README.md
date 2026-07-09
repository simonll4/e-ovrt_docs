# specs/ — Specs de Etapa 4 por módulo

Los specs se escriben **sin alternativas** (regla del doc 03 §9): cada uno parte de
los ADRs de `decisiones/` y solo describe la implementación elegida. Corresponden a
la lista del doc 02 §8, ajustada por los ADRs 001 (E-HYB firme), 002 (G1 demo),
005 (repo propio), 008 (servicio mínimo) y 009 (config centralizada). Numeración:
serie 40.

## Cola (orden de escritura = orden de dependencia)

| # | Spec | Repo dueño | Insumos decididos | Estado |
|---|---|---|---|---|
| 40 | **Plataforma / Etapa 4 (integrador)** — mapa contrato-preliminar↔artefacto real; bus (envelope, topics, END); `experiment_id`; criterio de relojes; diccionario de métricas con estados de aplicabilidad | transversal (vive acá) | ADR-003/004/006/007 | Pendiente |
| 41 | **control-plane** — G0 (clave `(pattern, source)` + regeneración de fixture/GT); runtime live (`MediaEventSource` jsonl/memory/bus); **servicio mínimo** (POST corrida con config por payload/referencia / GET estado / GET config efectiva); evaluador `direct_evidence` + fusión E-HYB or/and según doc 12 (gating por persona, marca de corroboración, factor de ventana de confirmación); publisher de alertas al bus de distribución; `experiment_id` en eventos; TTFA; alineación pattern set al informe (severidades/ventanas, doc 08 §2.1) | `e-ovrt_control-plane` | ADR-001/002/003/007/008/009 | Pendiente |
| 42 | **media-plane** — `BusPublishingArtifactWriter` (ZeroMQ + secuencia + END); **tracker liviano portado de labs** (`track_id` opcional aditivo en `media.detection.v1`); propagación `experiment_id`; verificación de config por payload en `POST /api/runs` (catálogos por id se conservan) | `e-ovrt_media-plane` | ADR-002/003/004/009 | Pendiente |
| 43 | **datasets — clip bench** — selección/grabación escenificada (H2), formato GT temporal escena-condición (+identidad mínima solo en los 2–3 clips de la demo G1), doble anotación 20%+kappa, 8–15 clips | `e-ovrt_datasets` | ADR-002; doc 07 H2/H8 | Pendiente — **mayor lead time, primero** |
| 44 | **experimental-setup** — **config experimental centralizada** (estructura por experimento: manifiestos, run configs de ambos planos, pattern/prompt/tuning sets); manifiesto paraguas + runner CLI (HTTP a ambos servicios); generador de reporte consolidado; prompt sets `eind_v1`/`edir_v1` construidos según doc 12 §2 (Tabla C.1, ejes, revisión del usuario antes de congelar); **webconsole como superficie de gestión primaria**: CRUD de configs, disparo en ambos planos, vista de alertas, agrupación por experimento, **rediseño UI/UX (navegación por experimento)** | `e-ovrt_experimental-setup` | ADR-001/004/006/008/**009** | Pendiente |
| 45 | **distribución** — repo nuevo (`e-ovrt_alert-distribution`): bus control→distribución, `NotificationEnvelope`, ledger, canal MQTT, retry mínimo | repo nuevo | ADR-005 | Pendiente |

## Reglas

1. Un spec no repite el análisis: **cita el ADR** y va directo a contratos,
   módulos, configs y criterios de terminado (evidencia en corrida, doc 02 §2.6).
2. Cambios de contrato siempre **aditivos** (campos opcionales) — regla que ya
   siguen ambos planos.
3. Cada spec cierra con su lista de verificación de terminado y las métricas que
   habilita (mapeadas al diccionario del spec 40).
