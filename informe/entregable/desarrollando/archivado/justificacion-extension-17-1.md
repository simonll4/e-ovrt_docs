# Justificación de la extensión de §17.1 — por qué no se podó más

> ⚠️ **SUPERADO el 2026-09-03 — sus cifras ya no describen el capítulo.** Este documento explicaba
> por qué §17.1 conservaba ~140 páginas después de los pases 3 a 5 (v1.5/v1.6, ~26.000 palabras).
> El ciclo de reestructuración v1.9 → v1.15 (§17.1.2, §17.1.4, §17.1.5, §17.1.6, §17.1.7 y el tramo
> §17.1.8–§17.1.11) dejó el capítulo en **15.464 palabras y 37 títulos**, sin perder tablas de
> pre-registro ni referencias. **La pregunta que este documento respondía ya no se plantea**; se
> conserva como registro de la decisión de entonces y no se actualiza. Diagnóstico y actas del
> ciclo nuevo: [`relevamiento-17-1-v1-11.md`](relevamiento-17-1-v1-11.md) y
> [`analisis-17-1-8-anexos.md`](analisis-17-1-8-anexos.md).

> **Qué es.** El registro de por qué la Consolidación Metodológica conserva su extensión final
> tras cinco pases de corrección, para quien pregunte —el equipo, un colega redactor o la
> preparación de la defensa— "¿por qué este capítulo mide lo que mide?". Complementa a
> [`analisis-poda-17-1.md`](analisis-poda-17-1.md) (el diagnóstico que originó la última poda) y
> al pase que la ejecuta ([`correcciones-etapa-2-pase-5.md`](correcciones-etapa-2-pase-5.md)).
> Cifras: v1.5 = 26.376 palabras de desarrollo (151 páginas con anexos y 27 tablas en APA doble
> espacio); tras el pase 5 ≈ **24.600–25.000 palabras ≈ ~140 páginas**.

---

## 1. Lo que ya se podó — el capítulo no está sin trabajar

| Pase | Mandato | Efecto |
|---|---|---|
| 1–2 (08-28) | 26 unidades + poda PODA-12/13/14 | **32.669 → 28.534 w** (−12,7 %): catálogo de datasets −72 %, proyección eliminada, infraestructura al Anexo B |
| 3 (08-31) | desduplicación + anexos | **→ 26.586 w**: −2 tablas del desarrollo, anexos 11→6 tablas, −8 títulos |
| 4 (08-31) | legibilidad | metadiscurso 33→11, 14 párrafos gordos partidos, cero pérdida |
| 5 (08-31) | poda por aporte A+B | **→ ~24.700 w**: auto-presentación, re-argumentación bibliográfica, no-aplicación duplicada; −1 tabla, −3 títulos |

**Acumulado: −24 % de palabras, −3 tablas del desarrollo, −5 de anexos, −13 títulos.** Cada pase
tuvo mandato firmado y verificación con targets; nada se recortó por cuota (guardrail de
`ajustes/07`: *"no se recorta por recortar"* — D-E1-13).

## 2. Por qué ~140 páginas es el piso honesto de este capítulo

### 2.1 El formato pesa más que la prosa

APA con doble espacio rinde ~190 palabras por página, y el capítulo lleva **26 tablas** (20 del
desarrollo + 6 de anexo), cada una de media a una página y media. Para calibrar con el propio
informe: §15+§16 pesa **~100 páginas con 22.900 palabras** después de una poda del 51 %. La
relación palabras→páginas de §17.1 es la misma; no hay grasa de formato propia.

### 2.2 §17.1 es el protocolo completo de la tesis — su función es ser exhaustivo

La Consolidación Metodológica es la **pre-registración** del trabajo experimental: qué se mide,
con qué reglas, bajo qué criterios de aceptación y con qué límites de interpretación. Cada
sección restante responde una pregunta que el jurado puede hacer:

| Sección | La pregunta del jurado que responde |
|---|---|
| Catálogo CR-01…CR-06 + niveles | "¿Por qué estas condiciones y no otras? ¿Por qué sólo dos se validan a fondo?" — la distinción núcleo/extensiones es la respuesta, y es la tesis misma (el aporte es el planteo, no la implementación) |
| Patrones, severidad, persistencia | "¿Por qué una alerta a los 4 s y no inmediata? ¿Por qué tres niveles?" — fundamentación normativa (Decreto 911/96) + trade-off FP pre-registrado |
| Protocolo de prompts (5 fases, ejes, idioma) | "¿Cómo sé que el prompt elegido no fue arbitrario?" — variación sistemática, congelamiento con acta, piso muestral con bootstrap |
| Estrategia de datos + Tabla de partición | "¿Cómo sé que no hay leakage?" — las 7 condiciones obligatorias que después permitieron excluir `chv` del fine-tuning |
| Framework de métricas + reglas de lectura | Cada regla de §17.1.7.8 es **la vara contra la que §17.5 declara resultados** — cortarlas deja cifras sin criterio pre-registrado |
| Regla de adaptación (§17.1.9) | "¿Por qué no adoptaron el modelo fine-tuned?" — la regla de decisión que produjo el NO-GO estaba escrita antes de entrenar |
| Supuestos (§17.1.10) | Cinco objeciones respondidas por anticipado (asistivo ≠ sancionatorio, límites del zero-shot con corpus de terceros, etc.) |

### 2.3 El pre-registro no ejercido NO se puede borrar

MOT17/OVT-B, los templates de prompt, el español, la doble anotación con kappa, los datos
complementarios para CR-03/04: nada de eso se ejecutó, y **por eso mismo debe quedar escrito**.
La doctrina del informe (regla de no-anacronismo) es que §17.5 reporta "prescripto y no
ejercido" **contra** el protocolo; si el protocolo se poda, esa declaración pierde su referente y
el trabajo pierde la honestidad metodológica que lo defiende. Está además protegido por decisión
firmada (D-E2-6, ratificada como D-P5-3: *"sin perder defensa de plataforma"*).

### 2.4 Cero bajas de referencias

La poda B comprime la re-argumentación bibliográfica remitiendo al marco teórico, pero **ninguna
obra citada desaparece del capítulo** (regla 2 del pase 5): cada cita es un punto de apoyo en la
defensa y una entrada del listado global de Referencias que otras secciones pueden no cubrir.

## 3. Qué habría que sacrificar para bajar de ~140 páginas — y por qué se decidió no hacerlo

| Recorte posible | Ahorro | Costo (por eso se descartó) |
|---|---|---|
| Comprimir MOT17/OVT-B y las métricas MOT | ~250 w | Reabre D-E2-6; adelgaza el pre-registro justo donde §17.5 declara la exclusión E-10/E-03 |
| Podar las justificaciones normativas de severidad | ~300 w | La severidad quedaría asignada "porque sí" — es la conexión tesis↔Decreto 911/96 |
| Reducir el protocolo de 5 fases a un párrafo | ~600 w | Es la evidencia de que la selección de prompts fue sistemática y no post-hoc |
| Fusionar las condiciones de partición en prosa | ~200 w | La Tabla de partición es la defensa anti-leakage — la cita §17.4 al justificar la exclusión de `chv` |
| Cortar los supuestos de interpretación | ~250 w | Son respuestas pre-escritas a objeciones del jurado; se usan en la defensa oral |
| Podar el catálogo a CR-01/CR-02 | ~1.500 w | Contradice la decisión de fondo del usuario: el valor de la tesis es el planteo del espacio completo, no la implementación |

**Suma de lo descartado: ~3.100 palabras ≈ 16 páginas.** Ese es el precio de las páginas que
faltan para "un capítulo corto", y se paga en capacidad de defensa. La decisión (2026-08-31) fue
no pagarlo.

## 4. Síntesis para citar

> §17.1 pasó por cinco pases con mandato y verificación: perdió el 24 % de sus palabras, 8 tablas
> entre desarrollo y anexos y 13 títulos, eliminó toda duplicación medible (metadiscurso 33→11,
> cero oraciones repetidas, una sola casa por concepto) y comprimió la argumentación cuya fuente
> vive en §15/§16. Lo que queda —~24.700 palabras, ~140 páginas en APA doble espacio con 26
> tablas— es el protocolo experimental completo de la tesis: catálogo y priorización de
> condiciones, patrones con fundamento normativo, protocolo sistemático de prompts, estrategia de
> datos anti-leakage, framework de métricas con reglas de lectura pre-registradas, regla de
> decisión del fine-tuning y supuestos de interpretación. Cada recorte adicional identificado
> (~3.100 palabras ≈ 16 páginas) sacrifica un elemento que responde una pregunta del jurado, y
> por eso se decidió no ejecutarlo.
