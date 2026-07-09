# ADR-003 — Bus media→control: ZeroMQ PUB/SUB, broker diferido

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Dimensión que atiende:** D3 (doc 03 §4)
- **Decisor:** usuario, 2026-07-09 (confirma la recomendación de docs 03/05)

## Decisión

- **DBE:** el acople por archivo (`detections.jsonl` → replay) es conforme al
  diseño (DA-03: el repositorio es la fuente de verdad) y se mantiene.
- **EBE:** bus **ZeroMQ PUB/SUB + msgpack** con envelope versionado, reutilizando
  el patrón `transport/` del two-node. Publicador junto al
  `EventEmittingArtifactWriter` (media-plane); consumidor `BusSource`/
  `MediaEventSource` (control-plane). Señal `run_finished`/END para cierre 1:1
  (ADR-007).
- **Broker (Kafka/RabbitMQ/NATS): fuera de alcance** (E-05). Queda el seam
  documentado (`BrokerSource`/`BrokerPublisher`, doc 06 §17).

## Mitigaciones de pérdida (obligatorias, doc 07 H6)

1. El control-plane se suscribe **antes** de disparar el run (slow joiner).
2. Contador de secuencia por evento → drops detectados y reportados como métrica
   de **corrida degradada** (taxonomía §17.3.13.3).
3. El JSONL sigue siendo la verdad: toda corrida live es re-evaluable offline; la
   comparación live-vs-replay se reporta como resultado de robustez.

## Alternativas consideradas

- **Broker desde ya:** durabilidad/replay que el log ya provee, al costo de un
  servicio pesado en la ruta crítica sobre WSL — contradice DA-01/DA-02/DA-03.
- **MQTT también para este tramo:** pondría un broker en la ruta crítica de video;
  los dos tramos tienen requisitos opuestos (doc 07 D3.2) — media→control es
  interno y de alta tasa; alertas→consumidores es externo y de baja tasa.

## Referencias

Doc 03 §4, doc 05 (diseño completo), doc 07 D3/H6, doc 10 E-05.
