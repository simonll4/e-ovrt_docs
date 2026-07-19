# 97 — Brief de redacción del informe final

- **Fecha:** 2026-07-18
- **Propósito:** las reglas de redacción para escribir/reescribir el informe (el
  `.docx`/Google Docs) a partir de este set documental. Pensado como instrucción
  operativa para el asistente (LLM) que ayude a redactar en el Project de claude.ai.
- **Complementa:** doc 13 (glosario y jerarquía de verdad), doc 93 (los redlines a
  resolver), doc 94 (el texto modelo), doc 92 (las cifras canónicas).

---

## 1. Registro y estilo

- **Registro formal impersonal**, tiempo presente para el diseño ("el plano de control
  evalúa…") y pretérito para lo ejecutado ("la corrida produjo…"). Sin voseo, sin
  primera persona singular. Primera persona plural solo donde el resto del informe ya
  la usa.
- **El modelo de estilo es el doc 94** (`94-secciones-nuevas-etapa3.md`): así se
  escribe una sección nueva. El doc 90/96 muestran el estilo del documento existente
  al que hay que integrarse.
- Terminología: usar **exactamente** los términos del glosario (doc 13) y de la §17.1.
  No introducir sinónimos nuevos para conceptos ya nombrados (p. ej. no alternar
  "plano de medios" / "media-plane" dentro de una misma sección: seguir la convención
  de la sección del informe donde se escribe; el informe usa los nombres en español
  con el nombre técnico entre paréntesis en la primera mención).
- Los nombres de artefactos, campos y contratos van en `monoespaciado` y **no se
  traducen** (`detections.jsonl`, `confirm_after_ms`, `media.detection.v1`).
- No usar viñetas donde el informe usa prosa; el capítulo 17 es mayormente prosa con
  tablas numeradas.

## 2. Jerarquía de fuentes al redactar

1. **Cifras y contratos:** SOLO del doc 92 (tabla canónica, con ruta:línea) o del
   doc 56 §9. Si un número no está ahí, **no existe** para el informe (regla del
   doc 95: ninguna cifra estrella sin artefacto).
2. **Estado de la plataforma:** doc 56. Nunca del cuerpo de docs 32/36/50 ni de
   fragmentos sin banner.
3. **Decisiones y sus porqués:** ADR-001…014 + doc 10 (alcance/exclusiones). Las
   decisiones **no se re-litigan** en el informe: se declaran con su justificación.
4. **Protocolo y definiciones metodológicas:** §17.1 (doc 96b). El informe nuevo debe
   ser consistente con ella; si la implementación se desvió del protocolo, la
   desviación **se declara** (los casos conocidos ya están relevados en docs 91/93).
5. **Qué escribir:** el doc 93 es el tablero — 24 redlines (R-01…R-24) con "dice hoy /
   debe decir / evidencia". El doc 94 ya trae texto redactado listo para adaptar.

## 3. Reglas de honestidad experimental (no negociables)

- **GT preliminar:** mientras el clip bench tenga GT `gt_preliminary`, sus métricas se
  presentan como *verificación de la mecánica de evaluación*, nunca como resultado.
  Fórmula tipo: "sobre un GT preliminar pendiente de adjudicación humana, la
  plataforma produjo…".
- **Lo no hecho se registra, no se esconde:** tracker sin productor de `track_id`
  (modo sujeto inerte), distribución MQTT (spec 45) no implementada, D1 sin correr
  (bloqueada por el acta `edir_v1`), EBE-desde-clip sin ancla de sincronización,
  pasada humana CVAT pendiente. El registro honesto ya está redactado en doc 91 §7 y
  doc 94 (sección "registro de lo no implementado").
- **Estados de aplicabilidad:** cuando una métrica no aplica, el informe usa el
  lenguaje del ADR-006/013 ("se declara `not_applicable/non_temporal_source`"), no
  frases vagas ("no se pudo medir").
- **La tesis no es "OVD detecta mejor"** (doc 09). Toda comparación con modelos
  cerrados se encuadra en extensibilidad y costo de adaptación, no en supremacía de
  detección. Ante números flojos de detección: el argumento es la *plataforma que los
  mide y los mejora sin re-entrenar*.
- **`re_alerts` no son falsos positivos**; el doc 52 fija la semántica.

## 4. Mecánica de trabajo en el Project

- El `.docx` **no se edita desde el repo**: los redlines se resuelven en Google Docs.
  El chat produce texto listo para pegar + la casilla del redline que salda.
- Al redactar una sección: (1) identificar el redline del doc 93 que la cubre, (2)
  levantar la evidencia del doc 92/56, (3) partir del texto del doc 94 si existe,
  (4) devolver el texto final + qué redline queda saldado.
- Trabajar por bloques del plan del doc 91 §8: A contradicciones → B concreción →
  C evidencia → D erratas. El plan de cierre y el orden de sacrificio están en el
  doc 95.
- Si el asistente detecta una contradicción entre docs, **no la resuelve en silencio**:
  la señala, propone la resolución según la jerarquía del doc 13 §1, y la registra
  como pendiente si no puede decidirse con lo disponible.

## 5. Números canónicos de referencia rápida

(Fuente: doc 92/56 §9 — verificar allí antes de citar; esta tabla es solo un índice.)

| Resultado | Valor | Artefacto |
|---|---|---|
| Benchmark clip `cb_b01_p7` (GDINO-tiny, **GT preliminar**) | P 0,50 · R 1,00 · F1 0,667 · t_alert 4000,0 ms · TTFD 0 ms · SDR 0,9986 | `operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-*` |
| G2A single-host | P50 14,7 ms / P95 31,8 ms (presupuesto 50–250 ms) | `operacion/datos/39-*` |
| Prefilter EN-2 (A/B real con GDINO) | 87 % drop on-device | doc 10 E-07 / doc 56 |
| Paridad replay↔stream | byte-idéntica (verificada por mutación) | doc 37 + datos |
| BENCH v2 imágenes | GDINO-tiny mAP 0,441; YOLOE recall CR-01 ≈ 0 (`bare_head`) | `operacion/datos/31-*` |
| Splits v2 | TRAIN 5540 / BENCH 196 / DEMO 1064 | registry datasets |
| Umbrales oficiales | CR-01 4000 ms / CR-02 7000 ms (resolve 2000/3000) | `cr01_cr02_v2.yaml` |
