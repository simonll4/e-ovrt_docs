# Spec integrador: la plataforma por los dos caminos y el mecanismo de convergencia

- **Fecha:** 2026-07-06
- **Estado:** Spec de decisión — gobierna cómo se desarrollan documentalmente ambos
  caminos y cómo se inclina la implementación una vez decidido cada punto.
- **Documentos que integra:**
  - `02-revision-critica-etapa3-y-norte.md` (críticas, recorte, plan 12 semanas)
  - `04-diseno-comparativo-estrategias-edir-eind.md` (fork empírico de estrategia)
  - `05-integracion-media-control-bus-eventos.md` (diseño del bus)
  - `06-diseno-distribucion-alertas.md` (distribución, a recortar)
  - `docs/informe/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (Camino B en cada dimensión)

## 1. Método

"Camino A" = lo implementado hoy en los repos. "Camino B" = lo que plantea la Etapa 3.
La divergencia real entre ambos **no es una sola bifurcación global sino seis
dimensiones independientes**, y no todas se deciden igual:

- **Decisión empírica** — se resuelve con un experimento pre-registrado (solo donde
  hay incertidumbre técnica real).
- **Decisión de diseño (ADR)** — se resuelve por análisis documentado; correr un
  experimento no aportaría información.

Cada dimensión de abajo desarrolla: ambos caminos, el análisis, el mecanismo de
decisión, la recomendación con su fundamento, y el **impacto en implementación**
cuando se decida. Al final, el tablero de decisiones (§9) funciona como registro
vivo: cada fila se cierra con un ADR y a partir de ahí la implementación se inclina.

Principio rector (ya acordado): **un solo código**; los caminos viven como
configuración, documentos y experimentos — nunca como ramas de git divergentes.

## 2. Dimensión 1 — Estrategia de detección del núcleo (DECISIÓN EMPÍRICA)

**Camino A:** E-IND — evidencia positiva (person/helmet/vest) + inferencia espacial
de ausencia en el control-plane. Implementada y testeada.
**Camino B:** E-DIR — prompts directos de ausencia/estado ("person without hard
hat", "bare head") como vocabulario principal (§17.3.9.2 de Etapa 3).
**Convergencia posible:** E-HYB (fusión or/and/vote a nivel de evidencia de patrón).

Esta es la única dimensión con un fork empírico completo, y ya tiene su documento
dedicado con protocolo pre-registrado, gates y criterios de decisión fijados:
`04-diseno-comparativo-estrategias-edir-eind.md`. No se repite aquí.

- **Mecanismo:** experimento en dos fases (BENCH por persona → clip bench por
  alertas), time-box 2 semanas (semanas 3–4).
- **Cierre:** ADR "Estrategia del núcleo validable" en el control-plane + redlines
  a §17.3.9.2 del informe.
- **Inclinación posterior:** si gana E-IND, la implementación no cambia (calibrar
  regiones/umbrales); si gana E-DIR, se promueve el evaluador `direct_evidence` a
  núcleo y `spatial_absence` queda como variante; si converge E-HYB, se implementa
  la fusión elegida (1–2 días) y el patrón declara ambas fuentes de evidencia.

## 3. Dimensión 2 — Granularidad del patrón e identidad del sujeto (EMPÍRICA LIVIANA + ADR)

**Camino A (implementado):** estado del patrón **por sujeto**, usando `detection_id`
del media-plane como identidad — que es un índice por frame, no un track. En video
real la identidad es falsa (aliasing entre personas).
**Camino B (Etapa 3, §17.3.8.3.2):** memoria del núcleo **por fuente y condición**
("hay al menos una persona sin casco en esta fuente"), sin exigir identidad; la
identidad por sujeto queda condicionada a tracking (DA-06).

**Análisis.** Camino B es más honesto que el estado actual del código: no promete
una identidad que el media-plane no provee. Su costo es semántico: el episodio pasa
de "el trabajador X estuvo sin casco 8 s" a "la condición estuvo presente en la
escena 8 s" — suficiente para un sistema asistivo y para todas las métricas del
informe (TTFA, SDR, precision/recall de alertas a nivel episodio-escena). Camino A
solo se vuelve defendible con `track_id` real (tracker liviano IoU/centroid en el
media-plane), que es trabajo acotado pero no gratuito y agrega una fuente de error
nueva (ID switches) que habría que medir.

- **Mecanismo de decisión:** ADR ahora + validación empírica barata después. Se
  adopta **G0 (escena/fuente) como núcleo** por ADR — es lo que el propio doc
  declara y elimina el defecto actual con un cambio chico en el `PatternEngine`
  (clave `(pattern, source)`). **G1 (sujeto con track_id)** queda como extensión
  condicionada: se implementa solo si sobran las semanas 7–8, y se valida sobre
  2–3 clips del clip bench comparando episodios G0 vs G1.
- **Cierre:** ADR "Granularidad del patrón del núcleo" en el control-plane.
- **Inclinación posterior:** refactor menor del motor (clave de estado + conteo de
  sujetos en evidencia como metadato del episodio); el GT del clip bench se anota a
  nivel escena-condición (compatible con ambas, anotar por sujeto solo los clips
  destinados a G1).

## 4. Dimensión 3 — Acople media→control: archivo vs bus de eventos (ADR)

**Camino A:** acople por archivo (`detections.jsonl` → replay offline). Funciona hoy.
**Camino B:** bus interno de eventos (DA-02/DA-03), tecnología sin fijar en Etapa 3.

**Análisis.** No hay incertidumbre que un experimento resuelva: para DBE el replay
por archivo *ya es conforme* al diseño (DA-03 distingue bus de repositorio y declara
el log como fuente de reconstrucción); para EBE el bus es necesario y la tecnología
natural es ZeroMQ PUB/SUB + msgpack (paridad con `transport/` two-node, cero
infraestructura nueva). Kafka/broker queda como seam documentado, fuera del alcance
de los 3 meses. Análisis completo en el doc de integración del 2026-07-06.

- **Mecanismo:** ADR directo (recomendación ya fundamentada; solo falta confirmarla).
- **Cierre:** ADR "Bus media→control: ZeroMQ PUB/SUB, broker diferido" (control-plane
  o doc de plataforma).
- **Inclinación posterior (semanas 5–6):** `BusPublishingArtifactWriter` en
  media-plane; `MediaEventSource` (jsonl/memory/bus) + runtime live en control-plane;
  señal `run_finished`; test de paridad replay↔stream con el fixture temporal.
  Mitigaciones de pérdida de mensajes (auditoría, doc 07/H6): el control-plane se
  suscribe **antes** de disparar el run (slow joiner); contador de secuencia por
  evento para detectar drops y reportarlos como métrica de corrida degradada; el
  JSONL sigue siendo la verdad — toda corrida live es re-evaluable offline y la
  comparación live-vs-replay se reporta como resultado de robustez.

## 5. Dimensión 4 — Configuración: tres configs vs RunConfig paraguas (ADR)

**Camino A:** tres configuraciones desconectadas (manifiesto experimental,
run media-plane, replay control-plane).
**Camino B:** `RunConfig` único que gobierna la corrida completa (§17.3.6, Tabla 44).

**Análisis.** Camino B literal (una config monolítica) contradice la separación de
repos ya adoptada. La convergencia correcta es un **manifiesto paraguas** en
`experimental-setup` con `experiment_id` propagado a ambos planos — el `RunSummary`
del media-plane ya tiene el campo; falta propagarlo al control-plane y al disparo.
Con eso, la promesa de trazabilidad del doc ("reconstruir la alerta hasta la
configuración") se cumple sin fusionar configs.

- **Mecanismo:** ADR directo.
- **Cierre:** ADR "Corrida experimental paraguas" en experimental-setup.
- **Inclinación posterior (semanas 1–2):** schema del manifiesto paraguas; campo
  `experiment_id` en eventos del control-plane; la webconsole agrupa por experimento.

## 6. Dimensión 5 — Distribución de alertas: módulo completo vs recorte (ADR)

**Camino A (diseño 2026-07-04):** módulo completo — 4 canales, ledger, retry con
backoff, dead-letter, dashboard propio.
**Camino B (Etapa 3, §17.3.10):** exige mucho menos — consumidores desacoplados,
registro intento/resultado, métrica separada de la alerta interna.

**Análisis.** Aquí el doc de tesis es el que recorta al diseño técnico, no al revés.
Para la defensa alcanza: un canal demostrativo + envelope + ledger de idempotencia
simple + vista de alertas en la webconsole (no un dashboard nuevo). El diseño
completo queda como anexo de diseño (trabajo futuro documentado).

- **Mecanismo:** ADR directo. **Canal elegido: MQTT** (decisión del usuario,
  2026-07-06 — el canal es intercambiable por diseño; se opta por MQTT por su bajo
  peso y latencia, y porque permite medir `t-alert-notification` sin la variabilidad
  de una API externa como Telegram).
- **Cierre:** ADR "Alcance de distribución para el prototipo".
- **Inclinación posterior (semanas 7–8):** implementar el recorte; medir
  `t_alert-notification` por separado, con la definición exacta del framework de
  métricas del informe (§17.1.7; ver doc 08 §2.2).

## 7. Dimensión 6 — Reporte y métricas: summaries por plano vs reporte consolidado (ADR)

**Camino A:** `summary.json` independiente por plano; métricas sin estados de
aplicabilidad; TTFD/SDR/T-alert sin definición operacional única.
**Camino B (§17.3.13):** reporte por corrida con métricas calculadas / aplicables no
calculadas / no aplicables / no interpretables, diccionario de métricas por tramo.

**Análisis.** Camino B gana sin discusión — es barato y es de lo más defendible del
diseño. Convergencia: un `report.json` consolidado por `experiment_id` que junta los
summaries de ambos planos + estados de aplicabilidad + causa. Incluir el criterio de
relojes para EBE two-node (latencias intra-nodo + end-to-end en un solo reloj, o
sincronización declarada), que el doc omite.

- **Mecanismo:** ADR + diccionario de métricas (1 página: nombre, fórmula, evento t0,
  evento t1, unidad, condición de aplicación).
- **Cierre:** ADR "Reporte consolidado y aplicabilidad de métricas" + diccionario.
- **Inclinación posterior (semanas 1–4):** generador de reporte consolidado
  (probablemente en experimental-setup); campos de estado en las evals existentes.

## 8. Lo que NO es un fork (común a ambos caminos, arranca ya)

Estas piezas se necesitan idénticas gane quien gane cada dimensión — por eso no se
posponen a ninguna decisión:

1. **Corrida DBE end-to-end real** (media→control sobre detecciones reales) — Fase 0,
   valida contratos y da los primeros números reales. Semana 1.
2. **Clip bench con GT temporal** (8–15 clips, GT de episodios a nivel
   escena-condición) — el ítem de mayor lead time; bloquea la Fase 2 del fork de
   estrategia y el resultado R3. Arranca semana 1, en paralelo.
3. **Calibración de umbrales/regiones** con salidas reales (partición de calibración
   separada de BENCH).
4. Erratas del docx de Etapa 3 (§4.8 de la revisión crítica) — para la versión final
   del informe.

## 9. Tablero de decisiones (registro vivo)

> **2026-07-09 — TABLERO CERRADO.** Todas las filas quedaron decididas y
> formalizadas como ADRs en `decisiones/` (D1 como encuadre: el experimento del
> doc 04 corre igual y es lo único que puede revisarla; ajuste del mismo día:
> E-HYB-or/and corre siempre en Fase 2). Se sumaron tres decisiones fuera del
> tablero original: **ADR-007** (semántica de corrida 1:1 en EBE, pregunta 4 del
> doc 02 §9), **ADR-008** (control-plane como servicio mínimo — excepción
> registrada en el doc 10) y **ADR-009** (config experimental centralizada en
> experimental-setup + webconsole como superficie de gestión, doc 10 ítem 11).
> Los specs por módulo (doc 02 §8) se escriben ya sin alternativas.

| # | Dimensión | Mecanismo | Cuándo se cierra | Recomendación previa | Estado |
|---|---|---|---|---|---|
| D1 | Estrategia del núcleo (E-IND/E-DIR/E-HYB) | Empírico (protocolo pre-registrado) | Fin semana 4 | E-IND favorita; E-HYB-and si hay complementariedad | **Encuadre decidido — ADR-001** (E-IND núcleo provisional; el experimento cuantifica y puede revisar) |
| D2 | Granularidad del patrón (G0/G1) | ADR + validación liviana | Semana 1 (ADR) | G0 núcleo, G1 condicionada | **Decidida — ADR-002** (G0 núcleo + G1 demostrativa: tracker de labs portado al media-plane, sin métricas MOT) |
| D3 | Bus media→control | ADR | Semana 1 | ZeroMQ PUB/SUB; broker diferido | **Decidida — ADR-003** |
| D4 | Config paraguas / experiment_id | ADR | Semana 1 | Manifiesto paraguas en experimental-setup | **Decidida — ADR-004** |
| D5 | Alcance de distribución + canal | ADR + elección de canal | Semana 2 | Recorte; canal: **MQTT** (elegido 2026-07-06) | **Decidida — ADR-005** (+ módulo en repo propio) |
| D6 | Reporte consolidado + métricas | ADR + diccionario | Semana 2 | Adoptar Camino B (doc) | **Decidida — ADR-006** |

Regla de cierre: cada fila se cierra con un ADR corto (decisión, alternativas,
fundamento, referencias a los docs de este set) en el repo dueño de la dimensión.
Cuando D1–D6 estén cerradas, los specs por módulo (§8 de la revisión crítica) se
escriben ya sin alternativas — solo con la implementación elegida — y el plan de
12 semanas corre sin re-litigar decisiones.

## 10. Cómo se inclina la implementación después de decidir

```
Semana 1–2          Semana 3–4              Semana 5+
─────────────       ─────────────────       ───────────────────────────
ADRs D2–D6    ──►   Experimento D1    ──►   Specs por módulo cerrados
Fase 0 (DBE real)   (E-DIR vs E-IND)        Implementación inclinada:
Clip bench (GT)     Conclusiones por         bus, live runtime, EBE e2e,
                    camino + ADR D1          distribución, campaña R1–R4
```

- Las decisiones ADR (D2–D6) se toman primero porque **no dependen del experimento**
  y desbloquean los specs de bus, reporte y configuración.
- El experimento D1 corre en su time-box con el resto ya decidido; su resultado solo
  ajusta el evaluador/prompt set del núcleo, no la plataforma.
- El informe (Etapa 4) se redacta con la cadena completa de justificación: cada
  decisión tiene su documento de análisis, su experimento cuando aplica, y su ADR —
  exactamente la trazabilidad de decisiones que un tribunal quiere ver.
