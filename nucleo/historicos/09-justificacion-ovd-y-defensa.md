# Justificación de OVD y estrategia de defensa de la tesis

> ⚠️ **2026-08-10 — DOCUMENTO HISTÓRICO, y esto es un hallazgo, no un trámite.**
> Este es **el argumento central de la tesis** —los cinco argumentos A1–A5 de por qué OVD—
> y su última actualización es del **2026-07-09**: **no incorpora los números que después se
> midieron.** El caso más claro es **A1** (costo de agregar una condición nueva), que quedó
> medido en `../../operacion/94` el 2026-08-05 y que acá todavía se plantea como
> expectativa.
>
> **Antes de usarlo para redactar la defensa, contrastarlo contra `../../operacion/98`**
> (conclusiones AF-1…AF-11) y contra los cuatro índices de
> `e-ovrt_experimental-setup/results/`. Lo que sigue vigente sin reservas es el
> **encuadre**: la tesis no es "OVD detecta mejor", sino una plataforma con condiciones
> expresadas en lenguaje y la medición de qué se logra sin entrenar.
>
> **Amerita un sucesor vigente en la raíz de `nucleo/`.** Ver el `README.md` de esta carpeta.

- **Fecha:** 2026-07-07
- **Propósito:** responder la objeción central de la tesis ("los objetos del núcleo
  validable se detectan fácil con modelos cerrados — ¿qué aporta OVD?"), fijar cómo se
  defiende en el desarrollo del informe (cierre incluido) y qué se muestra en la
  implementación y la presentación final (números y videos).
- **Insumos:** informe §12 (intro/hipótesis), §15.2.4–15.2.5 (trade-offs y brechas),
  §17.1 (consolidación metodológica, Tabla 37), docs 02 (R1–R4), 04 (D1), 08 (alineación).

## 1. La objeción, sin anestesia

"CR-01 y CR-02 son detección de casco y chaleco. Un YOLO entrenado sobre SHEL5K/CHV
lo resuelve con mAP alto, corre a 100+ FPS y es un problema resuelto hace años. Su
propio marco teórico cita que los OVD preentrenados rinden **peor** que detectores
ajustados al dominio en construcción (Abdalwhab et al., 2025). ¿Por qué OVD?"

Esta pregunta va a aparecer — en el mejor caso formulada por el propio informe antes
de que la haga el tribunal. La regla de oro de toda la defensa: **nunca discutir en el
eje "OVD detecta cascos mejor que un modelo cerrado"**. En ese eje la tesis pierde, y
además no es su eje: es una comparación que el propio marco teórico ya concede.

## 2. El reencuadre: qué es realmente el objeto de la tesis

La tesis **no** propone un detector de cascos. Propone y evalúa una **plataforma
asistiva donde las condiciones de riesgo se especifican en lenguaje, no se
entrenan** — y mide con rigor qué se obtiene a cambio de no entrenar. Tres
desplazamientos de encuadre que deben quedar explícitos en el informe:

1. **Del modelo a la plataforma.** La contribución es la cadena completa trazable
   (evidencia perceptiva → patrón temporal → alerta interna → distribución) con su
   protocolo experimental, métricas operativas (t_alert-system, TTFD, SDR) y
   presupuesto de latencia — algo que el propio estado del arte identifica como
   brecha: no existen benchmarks end-to-end integrados para pipelines OVD sobre
   streaming (§15.2.5.5, §15.4.3.1) ni métricas alineadas a seguridad laboral
   (§15.4.3.4). El detector es un **componente sustituible por adaptador** (DA-05).
2. **Del caso al catálogo.** CR-01/CR-02 no son la propuesta de valor: son el
   **testbed medible** (única zona del catálogo con cobertura de datos sólida —
   Tabla C.3: CR-01 7 fuentes, CR-03/04 **cero**). La propuesta de valor es que el
   *mismo sistema, sin reentrenar*, expresa CR-03…CR-06 y cualquier condición futura
   como configuración: prompts + reglas de patrón. La pregunta correcta no es "¿qué
   tan bien detecta cascos?" sino "¿cuánto cuesta la condición N+1?".
3. **De la promesa a la medición.** La hipótesis de trabajo no afirma que OVD gana:
   pregunta **qué se puede hacer sin entrenar** y si eso alcanza el umbral operativo
   asistivo. El resultado es válido en ambos sentidos (ver §4, A5).

## 3. Los cinco argumentos de defensa

### A1 — La economía del catálogo: el costo marginal de la condición N+1

El argumento cuantificable más fuerte. Con detectores cerrados, cada condición nueva
(o cada EPP nuevo, o cada regla específica de una obra) exige el ciclo completo:
recolectar datos → anotar → entrenar → validar → desplegar. El propio análisis de
datos de la tesis lo demuestra involuntariamente: para CR-03 y CR-04 la cobertura de
datasets públicos es **cero** (Tabla C.3) — con enfoque cerrado, esas condiciones son
una campaña de datos cada una; con OVD, son formulaciones del Anexo C más reglas de
patrón, evaluables en cuanto haya escenas. En la plataforma, agregar una condición
es editar dos YAML (prompt set + pattern set). **Este número — "condición nueva: 0
entrenamientos, ~20 líneas de configuración, minutos" — debe medirse y reportarse
como resultado**, no solo afirmarse.

Refuerzo normativo: el catálogo de riesgos no es fijo — deriva del Decreto 911/96 y
evoluciona por obra, temporada y normativa. Un sistema asistivo real necesita que el
**técnico de seguridad** (no un ingeniero de ML con GPU y dataset) exprese la
condición. El lenguaje es la única interfaz que lo permite.

### A2 — La plataforma no pierde si OVD pierde

La arquitectura es agnóstica del detector (adaptadores DA-05; GDINO/YOLOE/mock ya
conviven). La baseline zero-shot es obligatoria por protocolo y la comparación con
variantes ajustadas es una rama condicionada con regla formal (Tabla 37). Si mañana
un modelo cerrado o fine-tuned resulta superior, **se enchufa como un adaptador más y
la plataforma es exactamente el instrumento que lo demuestra**. La tesis produce el
banco de pruebas, no una apuesta a un modelo. (Nota defensiva: esto también responde
"¿por qué no fine-tunear y ya?" — además del costo, el fine-tuning puede erosionar la
capacidad open-vocabulary que motiva el enfoque, §15.2.4.5, y por eso el protocolo
exige verificar retención con un subset generalista, Tabla 32.)

### A3 — La brecha medida ES la contribución científica

El marco teórico identifica cinco brechas (§15.2.5): contextualización semántica
limitada, sin consistencia temporal nativa, sensibilidad al prompt, sensibilidad al
dominio, y ausencia de protocolos de evaluación para seguridad industrial. La tesis
ataca las cinco **por construcción**: la consistencia temporal la aporta el motor de
patrones (no el modelo), la sensibilidad al prompt se estudia sistemáticamente (D1 /
protocolo §17.1.5.4), y el protocolo+plataforma+métricas operativas *son* el aporte
frente a la quinta brecha. Cuantificar "cuánto le falta al zero-shot para el umbral
operativo, y dónde se origina la pérdida (modelo vs formulación vs estrategia)" es
conocimiento nuevo y transferible — nadie lo reporta para este dominio con cadena
completa hasta la alerta.

### A4 — Detección ≠ alerta: el valor está en la capa que los modelos no tienen

Un YOLO cerrado con mAP 0.9 sigue sin resolver el problema de la tesis: emite cajas
por frame, no episodios de riesgo. La transformación detección→patrón→alerta
(persistencia, histéresis, severidad, trazabilidad causal, minimización de evidencia)
es independiente del detector y es donde vive el valor asistivo. La tesis demuestra
esa capa con métricas propias (t_alert-system, TTFD, SDR, precision/recall de
alertas) que **no existen** en los benchmarks de detección. Esto desarma la
comparación "contra un YOLO": un modelo no es un sistema.

### A5 — Resultado dual garantizado (la tesis no puede "fallar")

Formular explícitamente en el informe: si el zero-shot alcanza los umbrales
operativos (Tabla D.4) para el núcleo → queda demostrada la viabilidad del enfoque
sin entrenamiento. Si no los alcanza → queda cuantificada la brecha bajo protocolo
reproducible, con diagnóstico de origen y **criterios de decisión de ingeniería**
(cuándo conviene OVD, cuándo cerrado, cuándo fine-tuning — ver §5.3). Ambos
desenlaces responden la pregunta de investigación. Lo único que sería un fracaso es
no medir con rigor — y todo el diseño experimental existe para impedirlo.

## 4. Preguntas hostiles anticipadas (Q&A para la defensa)

| Pregunta | Respuesta (línea corta) |
|---|---|
| "¿Por qué no un YOLO entrenado? Es más preciso." | Cierto para casco/chaleco aislado, y está citado en mi marco. La tesis no compite ahí: mide si un sustrato *sin entrenamiento* alcanza umbral asistivo, porque el catálogo real es abierto y evolutivo — para CR-03/04 no existe ni un dataset público (Tabla C.3): con enfoque cerrado son una campaña de datos cada una; acá son configuración. |
| "Sus números zero-shot son peores que el estado del arte supervisado." | Sí, y la brecha está cuantificada bajo protocolo reproducible — eso es un resultado, no una debilidad ocultada. El aporte es saber *cuánto* falta, *dónde* se pierde y *qué* alcanza para uso asistivo. |
| "Si el núcleo es CR-01/02, ¿dónde está lo open-vocabulary?" | En tres evidencias: la matriz de formulaciones evaluada sistemáticamente (D1), la demo de extensión de vocabulario sin reentrenar (§6, V2), y el catálogo completo especificado en la misma plataforma con costo marginal de configuración. |
| "¿Y si gana la estrategia indirecta (E-IND), no fracasó el lenguaje?" | No: E-IND también es open-vocabulary — persona/casco/chaleco/alias se consultan por texto y una clase nueva de EPP sigue siendo un string, no un dataset. Lo que se aprende es *a qué altura* funciona el lenguaje hoy (entidades sí, negación no) — guía de ingeniería transferible para cualquier aplicación OVD. |
| "¿Por qué no fine-tunearon si tenían el clúster?" | Regla metodológica explícita (Tabla 37): baseline primero, ajuste solo con ganancia exigible y sin comprometer la capacidad abierta (§15.2.4.5). Quedó como rama condicionada no ejercida por presupuesto de tiempo del proyecto, con el protocolo comparativo completo especificado (Tabla 32). (✎ 2026-08-11: respuesta **superada por ADR-017** — la rama se ejerce como jornada comprometida y la causa temporal está derogada; el guion vigente de esta pregunta está en `sintesis/fundamentos-teoricos.md`.) |
| "¿Esto reemplaza al supervisor / sanciona trabajadores?" | No: sistema asistivo, alerta interna ≠ juicio normativo (DA-13), sin identidad ni biometría, minimización de evidencia visual (DA-08/09). La decisión es siempre humana. |
| "¿Funciona en una obra real?" | El alcance declarado es entorno controlado/simulado (EBE, Tabla 20). La validación en obra real es trabajo futuro y el informe lo dice desde la intro — no se sobrevende. |

## 5. El cierre del informe: qué debe responder y con qué arco

### 5.1 Las cinco preguntas que la conclusión debe contestar (con número o evidencia)

1. **¿Qué se logra sin entrenar?** → R1: tabla zero-shot multi-modelo sobre BENCH
   (ya existe: GDINO-tiny mAP 0.441 con *cero* imágenes de construcción vistas en
   entrenamiento específico — presentarlo así, no como "0.441 vs 0.9 supervisado").
2. **¿Cómo conviene preguntarle al modelo?** → R2/D1: directa vs indirecta vs
   híbrida, sensibilidad a formulación, con criterios pre-registrados.
3. **¿La cadena completa produce alertas operativamente válidas?** → R3: precision/
   recall/F1 de alertas, TTFD, t_alert-system y SDR sobre el clip bench, leídos
   contra los umbrales por severidad (Tabla D.4).
4. **¿Es viable en tiempo real y distribuido?** → R4: G2A vs presupuesto 50–250 ms,
   FPS efectivo, latencias EBE two-node.
5. **¿Cuánto cuesta extender el catálogo?** → el "resultado A1": condición nueva =
   configuración, medido en tiempo/artefactos, con la demo V2 como evidencia visual.

### 5.2 Arco narrativo del documento (intro → cierre)

La intro plantea la promesa ("especificar riesgos en lenguaje"); el cierre debe
volver a ella con forma de **veredicto honesto en dos ejes**: (i) qué parte de la
promesa se sostiene hoy con evidencia (p.ej. "entidades y vocabulario sí; negación y
atributos finos no; la capa de patrones compensa la inestabilidad temporal"), y
(ii) qué criterios de decisión deja instalados. Estructura sugerida del capítulo de
cierre: síntesis de resultados por pregunta (5.1) → lectura contra la hipótesis →
limitaciones (heredadas del alcance, no descubiertas tarde) → criterios de adopción
(5.3) → trabajo futuro (CR-05/06 con MOT/zonas, obra real, broker, fine-tuning).

### 5.3 El entregable de ingeniería del cierre: criterios de adopción

Una tabla final "¿cuándo usar qué?" convierte la tesis en guía accionable — es lo que
un tribunal de ingeniería valora:

| Situación | Enfoque recomendado | Fundamento (resultado propio) |
|---|---|---|
| Condición estable, alto volumen, datos anotados disponibles | Detector cerrado / fine-tuned | Brecha de precisión medida en R1/R2 |
| Catálogo abierto/evolutivo, sin datos por condición | OVD zero-shot + patrones | Costo marginal A1 + cobertura Tabla C.3 |
| Condición nueva urgente ("desde mañana, detectar X") | OVD (única opción sin ciclo de datos) | Demo V2 |
| Condición por ausencia de EPP | Estrategia según resultado D1 (previsiblemente indirecta) | R2 |

## 6. Qué mostrar en la presentación final (números y videos)

Presupuesto realista: ~12–15 min de exposición + demo. Regla: **pocos números
grandes, videos cortos pre-renderizados, cero dependencia de que algo ande en vivo**.

### 6.1 Los números (uno por slide, grandes)

1. mAP zero-shot del mejor modelo sobre BENCH — "sin haber visto una sola imagen
   etiquetada de obra".
2. Precision/recall de **alertas** (no de detecciones) sobre el clip bench + t_alert
   medio vs umbral de severidad — "el sistema alerta bien y a tiempo / con esta brecha".
3. Latencia G2A y FPS efectivo en EBE two-node — "cabe en el presupuesto de tiempo real".
4. El número A1: "condición nueva = 0 entrenamientos, N líneas de YAML, M minutos".

### 6.2 Los videos (pre-renderizados con overlay; 3 esenciales + 1 bonus)

- **V1 — La cadena completa (45–60 s), el video central.** Clip escenificado: entra
  un trabajador sin casco → se ven las detecciones (cajas), el estado del patrón
  sobreimpreso (inactive → candidate → **confirmed**) y la alerta apareciendo
  (webconsole o `mosquitto_sub` en pantalla partida), con una línea de tiempo que
  marca TTFD y t_alert-system. Mensaje: *detección no es alerta; el sistema razona en
  el tiempo*.
- **V2 — Open-vocabulary en acción (30–45 s), el argumento A1 hecho video.** Misma
  escena; se muestra el YAML del prompt set, se agrega una clase nunca entrenada
  (p.ej. `ladder`, `safety glasses` o una máquina) y se relanza la corrida: la clase
  nueva aparece detectada. Mensaje: *esto es lo que un modelo cerrado no puede hacer
  sin un proyecto de datos*.
- **V3 — Lo que NO alerta (20–30 s), el video de madurez.** Condición transitoria
  (el casco se ocluye 1–2 s al agacharse el trabajador): las detecciones parpadean
  pero el patrón queda en candidate y **no hay alerta**. Mensaje: *histéresis y
  persistencia controlan los falsos positivos* — mostrar lo que el sistema no hace
  es lo que más credibilidad genera frente a un tribunal.
- **V4 (bonus) — EBE distribuido:** cámara → Nodo A (edge) → Nodo B (GPU) → alerta,
  con las latencias por tramo sobreimpresas. Si la logística de la sala lo permite,
  este es el único candidato a demo en vivo — con V4 grabado como respaldo en el
  bolsillo.

Guion de escenas alineado con la Tabla C.2 (distancias 5–10/10–20 m, oclusión baja/
media, iluminación variada): los mismos clips sirven para el clip bench (GT temporal),
la campaña EBE y los videos de la defensa. **Una sola sesión de grabación alimenta
las tres cosas** — diseñar el guion con ese triple propósito.

### 6.3 Herramienta necesaria (única pieza nueva): overlay renderer

Para V1–V3 hace falta un renderizador post-hoc que componga sobre el video:
detecciones (`detections.jsonl`), estados de patrón (`pattern_events.jsonl`) y
alertas (`alerts.jsonl`) con timeline. Es un script offline (~1–2 días, OpenCV) que
además sirve como herramienta de inspección cualitativa para el informe (frames de
ejemplo en el capítulo de resultados). Encaja como utilidad del control-plane o de
experimental-setup. Agregarlo al plan (semanas 7–8, junto con la campaña EBE).

*Actualización 2026-07-09 (docs 11 §7 y 01 §12):* la herramienta está casi completa
entre los dos repos — el media-plane tiene `VideoAnnotationWriter`+`visualize.py`
(anotación de detecciones, .mp4, transcode H.264) y la rama `mati` del control-plane
tiene `eovrt_labs.visualization.frame_drawing` + `alerts_csv` (dibuja las cajas de
las **alertas** sobre los frames). Falta solo componer estados de patrón + timeline
TTFD/t_alert en una salida única. Estimación revisada: **horas, no días**.

*Refuerzo para el Q&A (§4):* el backend `yolo-ppe` de labs (modelo supervisado de
seguridad en obra) habilita la comparación **OVD vs detector cerrado** con el mismo
motor y el mismo video — la pregunta "¿y contra un YOLO entrenado?" puede responderse
con números propios sin romper el won't de fine-tuning (E-04).

### 6.4 Gestión del riesgo de demo

- Todo lo crítico pre-renderizado; lo vivo (si lo hay) es V4 con respaldo grabado.
- Un solo comando de arranque para la demo viva (compose de la plataforma) ensayado
  en la sala o con hotspot propio; nunca depender de la red del aula.
- Los videos también cierran otra necesidad del informe: evidencia visual controlada
  (DA-09) para la comunicación académica — snapshots de V1–V3 van al capítulo de
  resultados.

## 7. Qué NO decir (claims prohibidos)

1. "OVD detecta mejor que los modelos cerrados" — falso y innecesario.
2. "El sistema previene accidentes" — no hay evidencia causal; es asistivo.
3. "Funciona en obra real" — el alcance es entorno controlado; decirlo como futuro.
4. "El sistema decide/sanciona" — nunca; DA-13 y marco ético.
5. Prometer CR-05/CR-06 como resultados — son extensiones especificadas, no validadas.
6. Números sin condición de aplicación — cada métrica con su n, su punto operativo y
   su estado (la política de aplicabilidad es un rasgo distintivo: usarla en escena).

## 8. Acciones que este documento agrega al plan

1. **Redline a la intro/cierre del informe:** incorporar el reencuadre §2 y el
   resultado dual (A5) de forma explícita; el cierre con la estructura §5.
2. **Medir el resultado A1** (costo marginal de condición nueva) como mini-experimento
   documentado: tiempo + artefactos para agregar una condición de la Tabla C.1 no
   usada en el núcleo.
3. **Guion de grabación de triple propósito** (clip bench + EBE + videos V1–V3/V4),
   variando según Tabla C.2, con consentimientos.
4. **Overlay renderer** (§6.3) — sumar a semanas 7–8.
5. **Slide-deck esqueleto** con los 4 números de §6.1 y los 3 videos — armarlo
   temprano (semana 9) para que la campaña final sepa exactamente qué números tiene
   que producir.
6. Q&A de §4 como anexo de preparación de defensa; ensayar respuestas de 30 segundos.
