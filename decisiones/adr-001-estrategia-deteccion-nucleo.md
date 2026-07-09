# ADR-001 — Estrategia de detección del núcleo: E-IND (encuadre)

- **Fecha:** 2026-07-09
- **Estado:** Aceptada como encuadre — el cierre definitivo lo da el experimento D1
- **Dimensión que atiende:** D1 (doc 03 §2)
- **Decisor:** usuario, 2026-07-09 (confirma la recomendación del doc 02 §4.1)

## Decisión

Se **invierte la adopción de §17.3.9.2 del informe**: el núcleo validable usa
**E-IND** (evidencia positiva person/helmet/vest + inferencia espacial de ausencia
en el control-plane). **E-DIR** (prompts directos de ausencia/estado) pasa a
variante comparativa, y la tensión se convierte en el resultado R2.

Esto NO cierra el experimento D1: el protocolo pre-registrado del doc 04 corre
igual (por ADR-010: Fase 1 en el tramo plataforma apenas exista `edir_v1`;
Fases 2–3 en el tramo de evaluación) para cuantificar la brecha, darle a E-DIR la oportunidad justa
con sus propias formulaciones (Tabla 45) y detectar complementariedad E-HYB. Si el
resultado contradijera el encuadre (criterios doc 04 §8 mandan), este ADR se revisa.

**Ajuste 2026-07-09 (usuario): E-HYB sube a rama experimental de primera clase.**
Las fusiones simples **E-HYB-or y E-HYB-and se corren en la Fase 2 siempre** (no
solo si la Fase 1 muestra complementariedad — ese umbral pasa de condición de
ejecución a *predicción a contrastar*). Fundamento: el resultado híbrido agrega
valor propio a la tesis (R2: "¿la señal semántica corrobora a la heurística
espacial?") gane quien gane. Sin cambios en: los criterios de adopción como núcleo
(doc 04 §8.3 — E-HYB solo es núcleo si supera por ≥0.05 y se explica en un párrafo)
ni la exclusión de **E-HYB-vote** (E-13).

## Alternativas consideradas

- **E-DIR como núcleo** (lo que adopta §17.3.9.2): descartada como núcleo por la
  evidencia propia (Sprint 2: `bare_head` débil en los 5 modelos; doc 31: YOLOE
  ciego a `bare_head`) y la literatura de negación en VLMs (ARO, NegBench, VALSE).
- **Esperar al experimento sin encuadre:** descartada — los specs y el informe
  necesitan una estrategia declarada ya; el experimento ajusta, no bloquea
  (doc 03 §10).

## Fundamento

1. Es la única estrategia implementada y testeada (evaluador `spatial_absence`,
   fixture temporal P/R/F1 = 1.0; motor mejorado por la rama `mati`, doc 01 §12).
2. La evidencia es auditable (bbox + región + ausencia verificable) — encaja con la
   trazabilidad causal exigida por §17.3.9.3, contra el score opaco de E-DIR.
3. Los insumos de E-IND son las clases fuertes del benchmark propio (doc 04 §3.4).

## Impacto

- Redline a §17.3.9.2 del informe (agenda de doc 02 §4.8 / doc 08).
- Prompt set del núcleo = `eind_v1` (canonical_v2); `edir_v1` se crea solo para el
  experimento. Construcción, comparabilidad y mecánica de fusión E-HYB: **doc 12**.

## Referencias

Doc 02 §4.1, doc 04 (protocolo completo), doc 07 D1, doc 12 (bajada operativa de
prompts y fusión), doc 31.
