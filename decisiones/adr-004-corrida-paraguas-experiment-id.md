# ADR-004 — Corrida experimental paraguas y `experiment_id`

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Dimensión que atiende:** D4 (doc 03 §5)
- **Decisor:** usuario, 2026-07-09 (confirma la recomendación del doc 02 §4.4)

## Decisión

- La corrida experimental se materializa como **manifiesto paraguas** en
  `e-ovrt_experimental-setup`, con un **`experiment_id`** que se propaga a los
  eventos y summaries de **ambos planos**. El manifiesto **referencia** las configs
  existentes de cada plano (no las fusiona ni inventa un schema monolítico).
- **Orquestación: runner CLI** en experimental-setup (~100 líneas): lee el
  manifiesto → dispara media-plane (HTTP, ya servicio) → dispara control-plane
  (HTTP, servicio mínimo según ADR-008) → espera → genera el reporte consolidado
  (ADR-006). La webconsole **agrupa y muestra** por experimento y puede disparar
  corridas como cliente de ambos servicios; no mantiene estado de orquestación
  propio.

> **Ampliado por ADR-009 (2026-07-09):** toda la configuración experimental se
> centraliza en experimental-setup y la webconsole pasa a ser la superficie de
> gestión primaria (editar configs, disparar, monitorear). El runner sigue siendo
> el camino reproducible para campañas; ambos usan las mismas APIs y configs.

## Alternativas consideradas

- **`RunConfig` monolítico** (Camino B literal, §17.3.6/Tabla 44): contradice la
  separación de repos ya adoptada.
- **Webconsole como orquestador de plataforma:** scope creep señalado por la
  auditoría (doc 07 D4.1); la lógica de orquestación queda en el runner,
  reutilizable sin UI.

## Fundamento

Cumple la promesa de trazabilidad de §17.3.11.1 ("reconstruir la alerta hasta la
configuración") con costo mínimo: el `RunSummary` del media-plane ya tiene el campo
`experiment_id`; falta propagarlo al control-plane y al disparo.

## Impacto

- Schema del manifiesto paraguas (spec experimental-setup, semanas 1–2).
- Campo `experiment_id` en eventos/summary del control-plane.
- Webconsole: agrupación por experimento.

## Referencias

Doc 02 §4.4, doc 03 §5, doc 07 D4, ADR-006, ADR-008.
