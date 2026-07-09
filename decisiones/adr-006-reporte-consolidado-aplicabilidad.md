# ADR-006 — Reporte consolidado y aplicabilidad de métricas

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Dimensión que atiende:** D6 (doc 03 §7)
- **Decisor:** usuario, 2026-07-09 (adopta el Camino B — §17.3.13 del informe)

## Decisión

- **Reporte consolidado por `experiment_id`**: un script (en experimental-setup)
  junta los summaries/evals de ambos planos y emite `report.json` + `report.md`.
  No es un servicio ni una base de datos (contención doc 07 D6).
- Cada métrica lleva **estado de aplicabilidad literal**:
  `computed | applicable_not_computed | not_applicable | not_interpretable` +
  `cause` (taxonomía §17.3.13.3). Las métricas MOT figuran `not_applicable`
  (E-10), no se omiten.
- **Diccionario de métricas** (1 página): nombre, fórmula, evento t0, evento t1,
  unidad, condición de aplicación — mapeado a señales ya instrumentadas
  (`timestamp_ms`, transiciones, alertas). Incluye TTFD, t_alert-system,
  t_alert-notification, SDR, G2A.
- **Criterio de relojes para EBE two-node** (hueco del informe, doc 02 §4.6):
  latencias por tramo intra-nodo + latencia end-to-end medida en un solo reloj
  (recepción), o sincronización declarada (chrony/NTP) con error estimado.

## Fundamento

Es la decisión más barata y rentable del set (doc 07 D6): materializa lo más
defendible del diseño de Etapa 3 y cierra la trazabilidad de ADR-004.

## Impacto

Generador de reporte en experimental-setup (semanas 1–4); campos de estado en las
evaluaciones existentes (`evaluate_bench.py`, `evaluate-alerts`).

## Referencias

Doc 02 §4.6, doc 03 §7, doc 07 D6, doc 08 §2 (nombres/umbrales del informe).
