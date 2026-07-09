# ADR-007 — Semántica de corrida del control-plane en EBE: 1:1 con el run del media-plane

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** pregunta 4 del doc 02 §9 (no estaba en el tablero D1–D6)
- **Decisor:** usuario, 2026-07-09 (confirma la recomendación del doc 02)

## Decisión

En EBE, **una corrida del control-plane se corresponde 1:1 con un run del
media-plane**: nace cuando se dispara el run (suscripta al bus *antes*, ADR-003),
consume el stream y cierra al recibir `run_finished`/END, emitiendo su summary.
`control_run_id` referencia `media_run_id` (ya en los contratos) y ambos llevan el
`experiment_id` (ADR-004).

**Ventanas de evaluación propias del control-plane** (corridas que abarquen varios
runs de medios, o corridas continuas) quedan como **trabajo futuro declarado**.

## Fundamento

- Preserva la unidad experimental del informe: cada corrida es reproducible y
  comparable replay↔live con el mismo corte (test de paridad, ADR-003).
- Evita semánticas de agregación nuevas sin valor para R3/R4.
- Es la semántica que el runtime de replay ya tiene (corrida finita con resumen al
  agotar la fuente); el runtime live solo cambia la señal de fin.

## Referencias

Doc 02 §9.4, doc 03 §4 (inclinación D3), ADR-003, ADR-004.
