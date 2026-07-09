# decisiones/ — ADRs de la plataforma

Registro de decisiones de arquitectura y alcance. Cada ADR cierra una fila del
tablero del doc 03 §9 (dimensiones D1–D6) o una decisión posterior. Formato: corto —
decisión, alternativas, fundamento, impacto, referencias.

**Convención de ubicación:** los ADRs viven acá (el set documental versionado es el
registro rector). Cuando la implementación de una decisión arranca en un repo de
código, ese repo puede llevar una copia o un puntero a este archivo — la verdad es
esta carpeta.

| ADR | Decisión | Cierra | Estado |
|---|---|---|---|
| [001](adr-001-estrategia-deteccion-nucleo.md) | E-IND núcleo (encuadre); E-DIR variante; experimento D1 cuantifica. *Ajuste 07-09: E-HYB-or/and corre siempre en Fase 2* | D1 (encuadre) | Aceptada — revisable solo por el experimento (doc 04 §8) |
| [002](adr-002-granularidad-patron-g0-g1demo.md) | G0 escena núcleo + G1 demostrativa (tracker portado al media-plane, sin métricas MOT) | D2 | Aceptada |
| [003](adr-003-bus-media-control-zeromq.md) | ZeroMQ PUB/SUB media→control; broker diferido; mitigaciones de pérdida | D3 | Aceptada |
| [004](adr-004-corrida-paraguas-experiment-id.md) | Manifiesto paraguas + `experiment_id`; runner CLI orquesta; webconsole cliente | D4 | Aceptada |
| [005](adr-005-distribucion-mqtt-repo-propio.md) | Distribución recortada, canal MQTT, **repo propio** con bus control→distribución | D5 | Aceptada |
| [006](adr-006-reporte-consolidado-aplicabilidad.md) | Reporte consolidado por experimento + estados de aplicabilidad + diccionario de métricas + relojes | D6 | Aceptada |
| [007](adr-007-semantica-corrida-1a1.md) | Corrida control-plane 1:1 con run del media-plane en EBE | doc 02 §9.4 | Aceptada |
| [008](adr-008-control-plane-servicio-minimo.md) | Control-plane como servicio mínimo; webconsole cliente de ambos planos | nueva (excepción al doc 10) | Aceptada |
| [009](adr-009-config-centralizada-webconsole.md) | Config experimental centralizada en experimental-setup; webconsole superficie de gestión primaria (+mejora UX); runner CLI como camino reproducible | nueva (doc 10 ítem 11) | Aceptada |
