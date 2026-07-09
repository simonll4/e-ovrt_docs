# Diseño experimental de prompts y fusión E-HYB — bajada operativa de D1

- **Fecha:** 2026-07-09
- **Estado:** Diseño pre-registrado (complementa el protocolo del doc 04; se congela
  junto con él antes de correr)
- **Decisiones que baja a tierra:** ADR-001 (E-IND núcleo + E-HYB-or/and siempre en
  Fase 2) y los requisitos del protocolo de prompts del informe (§17.1.5.4, Anexo C
  Tabla C.1; relevados en doc 08 §2.3/§5.1)
- **Pregunta que responde:** cómo se experimenta con los prompts para que las
  estrategias sean **comparables**, **medibles** y no comprometan el **núcleo
  validable**.

## 1. Las tres señales y quién es quién

| Estrategia | Prompt set | Evaluador (control-plane) | Rol |
|---|---|---|---|
| E-IND | `eind_v1` — vocabulario positivo canónico (person/helmet/vest). Es la fila "indirecta" de la Tabla C.1 ("hard hat ; person"). | `spatial_absence` (existe, motor `mati`) | **Núcleo** (ADR-001) |
| E-DIR | `edir_v1` — formulaciones directas de la Tabla C.1 | `direct_evidence` (a construir, ~50 líneas) | Variante comparativa |
| E-HYB | no tiene prompt set propio: **fusiona las señales de los dos anteriores** (§4) | `spatial_absence` + `direct_evidence` + función de fusión | Rama experimental de primera clase (ADR-001, ajuste 07-09) |

La estrategia es un punto de enchufe (doc 04 §2): prompt set en el media-plane,
evaluador en el control-plane. Máquina de estados, histéresis, alertas y métricas
son idénticas para las tres — lo único que varía es cómo se genera la
`PatternEvidence`.

## 2. Prompt sets: construcción, versionado y congelamiento

### 2.1 `eind_v1`

Las tres clases canónicas (canonical_v2), sin frases compuestas. Los alias de label
viven en el evaluador, no en el prompt. Ya corrido en Sprint 2 → la Fase 1 de E-IND
se puntúa **sin re-inferir** (doc 04 §7.7).

### 2.2 `edir_v1` — desde la Tabla C.1, con los ejes del protocolo

Fuente literal: **Anexo C, Tabla C.1** (doc 08 §5.1), complementada por la Tabla 45
de Etapa 3. Por condición, un prompt por eje (los ejes SON la estructura del
experimento de sensibilidad que la metodología promete):

| Eje (§17.1.5.4.2) | CR-01 (ejemplo C.1) | CR-02 (análogo) |
|---|---|---|
| Sintáctico / negación | "person without hard hat" | "person without safety vest" |
| Especificidad | "construction worker without safety helmet" | "construction worker without reflective vest" |
| Estado observable | "person with bare head on construction site" | "person without bright colored safety clothing" |
| Template (presencia, diagnóstico) | "a photo of a hard hat" | "a photo of a safety vest" |

Reglas:

1. Cada formulación = un `prompt_id` propio dentro del set versionado. Nada se
   reformula después de congelar; si una frase resulta mal elegida, eso es un
   resultado, no un bug a arreglar en caliente.
2. **Los templates son de presencia** (C.1): entran como eje de diagnóstico
   sintáctico, no como candidatos a evidencia de ausencia.
3. **Revisión del usuario antes de congelar** (mitigación del sesgo del auditor,
   doc 07 D1.6): que nadie pueda decir que se eligieron frases débiles a propósito.
4. Los sets viven versionados en `experimental-setup/prompts/` (ADR-009) y cada
   corrida declara `prompt_set_id` en su `effective_config` — la trazabilidad
   alerta→configuración incluye al prompt exacto.

## 3. Reglas de comparabilidad (qué se congela y qué se calibra)

**Variable única = estrategia/prompt set** (regla §17.3.6.5). Todo lo demás,
congelado e idéntico entre corridas:

- **Congelado:** modelo (GDINO-tiny baseline), resolución de inferencia, NMS,
  postproceso, BENCH v2 (mitades calib/test estratificadas, doc 07 H3), tuning YAML
  de labs si la generación usa labs (doc 04 §8.6), pattern set del motor
  (`cr01_cr02_v2` alineado al informe: PR-01 alto/3–5 s, PR-02 medio/5–10 s —
  doc 08 §2.1).
- **Calibrable por estrategia (en mitad A, declarado, luego congelado para test):**
  los umbrales de confianza. El umbral es *parte de la estrategia* (E-IND tiene dos
  separables — sujeto y EPP; E-DIR tiene uno por frase; E-HYB hereda los de sus
  fuentes sin recalibrar, ver §4.3). Todo lo reportado sale de la mitad B.
- **Sub-experimento de contexto de vocabulario** (§17.1.5.4 exige aislado vs
  completo, doc 08 §2.3.1): solo para las formulaciones **finalistas**, cada prompt
  se corre en aislamiento y dentro del vocabulario completo. Además de cumplir el
  protocolo, este dato decide la mecánica operativa de E-HYB (§4.1).
- **Reporte estadístico:** n de la clase positiva contra el piso de ~200 instancias
  (§17.1.5.4); si no llega, tamaño efectivo + IC por bootstrap (doc 07 H1) y la
  Fase 2 pesa más. Confianza media de los TP por formulación (estabilidad). Para
  E-IND, métricas por entidad componente (person/helmet/vest) para atribuir
  degradación.

## 4. E-HYB: definición operativa de la fusión

### 4.1 Mecánica de generación: fusión de corridas separadas (dual-run), no vocabulario unión

Decisión pre-registrada: **E-HYB se computa fusionando las salidas de las corridas
E-IND y E-DIR ya existentes, a nivel de evidencia** — no con un pase único de
vocabulario unión.

Fundamento: en GDINO el vocabulario es parte de la inferencia (los prompts compiten
en la atención texto-imagen; es exactamente la hipótesis del eje aislado-vs-completo
del informe). Con un pase único, las señales de E-HYB serían *distintas* de las de
las corridas individuales y la comparación dejaría de ser de variable única. Con
dual-run, las señales de E-HYB son bit a bit las mismas que las individuales → toda
diferencia observada es atribuible **solo a la función de fusión**. Bonus: la Fase 1
de E-HYB no requiere inferencia nueva (§5).

El pase único (vocabulario unión, una sola inferencia — la opción operativamente
más barata para la plataforma) queda como **variante operativa condicionada**: si el
sub-experimento aislado-vs-completo muestra interacción despreciable para las
finalistas, la plataforma puede usarlo declarando la equivalencia; si hay
interacción, se declara el costo (2 pases) o se descarta. Es una pregunta del
experimento, no una decisión a adivinar ahora.

### 4.2 Gating de la señal E-DIR (auditabilidad)

Una detección E-DIR solo aporta evidencia si **matchea con una persona detectada**:
IoU≥0.5 contra el bbox de persona para frases persona-céntricas, centro-en-región
para detecciones de parte (`bare_head`) — el mismo matching por variante de la
Fase 1 (doc 07 H1). Esto evita que un falso positivo suelto (sin persona) dispare
evidencia de patrón y mantiene la alerta reconstruible ("frase F sobre la persona
en bbox X"), que es el requisito de trazabilidad causal del propio informe.

En G0 (núcleo, ADR-002) la evidencia luego se agrega a nivel escena-condición; el
gating por persona se conserva igualmente porque es lo que hace auditable la
evidencia y lo que permite comparar con G1-demo en los clips seleccionados.

### 4.3 Las dos funciones de fusión (pre-registradas; vote sigue excluida, E-13)

**E-HYB-or (unión):** la unidad visual aporta evidencia al patrón si E-IND **o**
E-DIR (gateada) la aportan. Predicción registrada: sube recall de alertas, baja
precisión; la histéresis temporal filtra parte del ruido extra.

**E-HYB-and (corroboración) — la variante conceptualmente defendible** ("la
heurística espacial decide, la señal semántica corrobora", doc 04 §5.2):

- E-IND es la señal primaria: sin evidencia E-IND no hay episodio (el recall base
  no se sacrifica).
- Un hit E-IND se marca **corroborado** si en la misma unidad visual hay una
  detección E-DIR concordante (mismo gating, misma condición).
- Regla única de efecto, explicable en un párrafo: **la ventana de confirmación del
  patrón se reduce por un factor cuando la mayoría de los hits acumulados del
  episodio están corroborados** — parámetros `corroboration_factor: 0.5` y
  `corroboration_ratio: 0.5` como valores iniciales, calibrables en mitad A y
  congelados para el test.
- Por qué esta regla y no otra (p. ej. "hit corroborado cuenta doble"): mapea
  directo a la métrica estrella — la corroboración **acelera la alerta**, y su
  efecto se lee en `t_alert-system`/TTFD contra los umbrales de la Tabla D.4, no en
  un score interno opaco.

Costo de implementación total (evaluador `direct_evidence` + marca de corroboración
+ factor de ventana en el motor): 1–2 días, ya firme en el spec 41.

## 5. Medición: tres niveles, idénticos para las tres estrategias

| Nivel | Dónde | Qué se mide | E-HYB |
|---|---|---|---|
| 0 — Detección | BENCH (hecho: Sprint 2 / doc 31) | AP por clase; insumos de cada estrategia | n/a (hereda) |
| 1 — Estado por persona (Fase 1) | BENCH, mitad test | P/R/F1 del estado "sin EPP" vs `has_helmet`/`has_vest`, matching por variante, IC bootstrap, confianza media TP | **offline, sin inferencia nueva**: fusión de los estados predichos por las dos corridas; el análisis de errores (¿FP/FN caen en las mismas personas?) mide la complementariedad ANTES de la Fase 2 |
| 2 — Alerta (Fase 2) | Clip bench, motor G0, pattern set v2 | P/R/F1 de alertas vs GT temporal escena-condición; `t_alert-system`, TTFD, SDR contra Tabla D.4 (PR-01: 5–10 s / <3 s / ≥0.60; PR-02: 10–20 s / <10 s / ≥0.70); re-alertas por episodio (ADR-011) e inesperadas; estabilidad de episodios | corre con las dos fusiones; el efecto esperado de -and es visible como reducción de `t_alert-system` sin caída de precisión |

Reglas transversales: mismos clips, mismo motor, mismo pattern set y misma GT para
todas las estrategias; toda métrica con **estado de aplicabilidad + causa**
(ADR-006); doble anotación 20% + kappa en el GT del clip bench (§17.1.5.4).

## 6. Protección del núcleo validable

1. **E-IND sigue siendo el núcleo pase lo que pase con E-HYB** (ADR-001). E-HYB solo
   se promueve a núcleo por los criterios ya fijados (doc 04 §8.3): supera a la
   mejor individual en F1 de alertas por ≥0.05 **y** su explicación cabe en un
   párrafo. Si no, queda como resultado experimental de R2 con sus números.
2. **El time-box manda** (2 semanas, doc 04 §7). Orden de ejecución dentro del
   experimento: Fase 1 E-IND/E-DIR → Fase 1 E-HYB offline (gratis) → Fase 2 E-IND →
   Fase 2 E-DIR (si pasa como candidata) → Fase 2 fusiones. Si el tiempo se corta,
   lo no corrido se reporta "no ejecutada con causa" (taxonomía §17.3.13.3) — la
   cadena del núcleo (doc 10 ítem 1) nunca depende de E-HYB.
3. **Nada toca contratos, bus ni arquitectura** (doc 04 §1): estrategia = prompt set
   + evaluador + (para E-HYB) función de fusión declarada en la config del patrón.
4. **Trazabilidad completa por corrida:** `experiment_id` + `prompt_set_id` +
   estrategia + parámetros de fusión en `effective_config` — una alerta de E-HYB se
   reconstruye hasta la frase y la regla que la aceleraron.

## 7. Delta de trabajo sobre el doc 04 §9

| Tarea | Repo | Estado tras este diseño |
|---|---|---|
| `edir_v1` desde Tabla C.1 (+eje template) | experimental-setup | Igual (horas); requiere revisión del usuario antes de congelar |
| Scoring por persona ambas estrategias | datasets | Igual (1–2 días) |
| Evaluador `direct_evidence` | control-plane | **Firme** (antes condicional al gate) |
| Fusión or/and (marca corroboración + factor de ventana) | control-plane | **Firme** (antes condicional a complementariedad) |
| Scoring E-HYB Fase 1 offline | datasets | Nuevo, barato (reusa las dos corridas) |
| Sub-experimento aislado-vs-completo (finalistas) | media-plane (corridas extra) | Nuevo, acotado a finalistas |

## 8. Salidas comprometidas

Las del doc 04 §10, más: los parámetros de fusión calibrados y congelados
(mitad A), el veredicto de la variante operativa de E-HYB (dual-run vs pase único,
con el dato de interacción de vocabulario), y la sección de sensibilidad al prompt
del informe alimentada directamente por los ejes de la Tabla C.1.
