# Registro de alcance y exclusiones — cierre formal del "no se implementa"

- **Fecha:** 2026-07-07 · **Actualizado 2026-07-09:** decisiones formalizadas en
  `decisiones/` (ADR-001…011). Tres ADRs amplían el alcance de forma acotada y
  quedan registrados acá: **ADR-002** (G1 demostrativa — ítem 10, redefine E-03),
  **ADR-008** (control-plane como servicio mínimo — ítem 9) y **ADR-009** (config
  centralizada + webconsole — ítem 11). **ADR-010** fija el orden de ejecución
  (plataforma primero) y **ADR-011** la frontera de política de alertas (no
  cambian el alcance).
- **Decisión que registra:** el proyecto implementa el **núcleo validable y lo
  detiene ahí** (decisión del usuario, 2026-07-07). Todo lo demás queda **excluido de
  implementación pero cerrado documentalmente**: con justificación metodológica
  anclada en el propio informe, rastro documental verificable y frase de declaración
  para el texto final.
- **Principio rector:** una exclusión bien cerrada no es "no llegamos" — es una
  decisión de alcance tomada con las reglas que el informe fijó de antemano
  (núcleo obligatorio vs extensión condicionada §17.1.2.2, niveles de compromiso
  §17.1.7.3.2, regla de fine-tuning Tabla 37, política de aplicabilidad §17.3.13.3).
  El informe ya trae el lenguaje para esto; acá se aplica caso por caso.

## 1. Vocabulario de estados (usar siempre el mismo)

| Estado | Significado | Cómo se declara en el informe |
|---|---|---|
| **Implementado y validado** | Corre, tiene tests y produce evidencia en corridas registradas. | Resultados con métricas. |
| **Especificado, no implementado** | Existe definición operativa completa (patrones, prompts, contratos, criterios) lista para implementarse. | "Extensión condicionada especificada; su validación excede el alcance experimental." |
| **Diseñado, no implementado** | Existe diseño técnico detallado (documento de arquitectura/módulo). | "Diseño registrado como anexo; implementación diferida a trabajo futuro." |
| **Condicionado no ejercido** | El protocolo define cuándo ejecutarlo y las condiciones no se dieron o no se priorizaron. | "Rama condicionada no ejercida según la regla [X]; condiciones de habilitación documentadas." |
| **No aplicable** | Métricas/evaluaciones cuya condición de aplicación no se cumple. | Taxonomía de aplicabilidad (§17.3.13.3), con causa. |

## 2. Lo que SÍ se implementa (lista cerrada — definición de terminado)

1. **Cadena completa DBE para CR-01/CR-02** (núcleo obligatorio): media-plane →
   bus/replay → motor de patrones (pattern set v2 alineado a Tabla 24) → alerta
   interna → reporte consolidado con estados de aplicabilidad.
2. **Experimento D1** (protocolo de prompts §17.1.5.4 / Tabla C.1): estrategia
   directa vs indirecta, **con la híbrida simple (or/and) como rama experimental
   de primera clase en la Fase 2** (ajuste 2026-07-09, ADR-001; vote sigue E-13).
3. **Clip bench** con GT temporal (grabación escenificada, doble anotación 20%+kappa)
   y evaluación de alertas contra umbrales Tabla D.4.
4. **EBE complementario sobre la infraestructura two-node ya construida** (Nodo A =
   EN-0/EN-1, Nodo B = CPN) con fuente viva de contingencia oficial (cámara IP/webcam
   o RTSP simulado). Se implementa porque ya existe (Fase 2 verificada) y produce R4
   con costo marginal bajo — no es una ampliación de alcance sino capitalización de
   trabajo hecho.
5. **Distribución mínima**: un canal (MQTT) + ledger de idempotencia + vista de
   alertas en la webconsole existente. **En repo propio**, consumiendo el bus
   control→distribución (ADR-005).
6. **Bus ZeroMQ media→control** (necesario para el punto 4).
7. **Overlay renderer** offline (videos V1–V3 de la defensa + figuras del informe).
8. **Mini-experimento A1** (costo marginal de una condición nueva por configuración).
9. **Control-plane como servicio mínimo** (ADR-008, 2026-07-09): cáscara HTTP sobre
   el runtime live (disparo, estado, config efectiva) + webconsole como cliente de
   ambos planos. Sin sesiones/auth/concurrencia (E-12 sigue vigente).
10. **G1 demostrativa** (ADR-002, 2026-07-09): tracker de labs portado al
    media-plane (`track_id` opcional aditivo), demostrada en 2–3 clips. Sin
    métricas MOT (E-10 sigue "no aplicable"). Redefine E-03.
11. **Config centralizada + webconsole como superficie de gestión** (ADR-009,
    2026-07-09): configuración experimental de ambos planos versionada en
    experimental-setup; webconsole gestiona configs y dispara corridas en los dos
    servicios, con mejora de UI/organización UX (navegación por experimento).

Nada fuera de esta lista entra a implementación. Si algo de la lista peligra por
tiempo, el orden de sacrificio es: **11-UX (la mejora visual; la centralización de
config no se sacrifica — la usa el runner) → 10 → 9 (queda el runner CLI; el
runtime live no se sacrifica) → 8 → 7 (se reemplaza por overlays simples) → 5 (se
reduce a `mosquitto_sub`)** — nunca 1, 2 ni 3.

## 3. Registro de exclusiones

Formato por entrada: qué es → justificación → rastro documental existente → frase de
declaración → condición de habilitación futura.

### E-01 — Condiciones CR-03 y CR-04 (Nivel 2: reglas espaciales intra-frame)

- **Justificación:** brecha de datos **total** — cero fuentes públicas con la
  condición completa anotada (Tabla C.3); dificultad OVD estimada "Alta" por
  visibilidad fina del EPP y ambigüedad geométrica 2D (§17.1.5.2.4, Bianchi et al.
  2024). El informe las clasifica extensión condicionada desde la consolidación
  (Tabla 17) y su regla de datos las deja "fuera del camino ordinario" (Tabla 37).
- **Rastro documental:** patrones PR-03/PR-04 especificados con severidad y
  persistencia (Tabla 24); prompts candidatos formulados (Anexo C, Tabla C.1);
  requisitos de módulo espacial descritos (§17.3.8.3.3).
- **Declaración:** "Especificadas, no validadas: su evaluación requiere datos que no
  existen públicamente (Tabla C.3) y cuya producción excedería el alcance del
  prototipo sin desplazar el núcleo (Tabla 38, riesgo 2)."
- **Habilitación futura:** dataset propio o público con la condición anotada +
  módulo de reglas espaciales intra-frame.

### E-02 — Condiciones CR-05 y CR-06 (Nivel 3: relacional / zonas)

- **Justificación:** requieren MOT + razonamiento contextual (CR-05) y cámara fija +
  polígono parametrizado externo (CR-06) — dependencias que el informe excluye del
  núcleo explícitamente (§17.1.5.2.4, Tabla 23). Cobertura de datos parcial.
- **Rastro documental:** criterios de activación combinada definidos conceptualmente
  (§17.1.5.3.6: métrica de proximidad, punto de apoyo, punto-en-polígono); prompts de
  entidades componentes (Tabla C.1, CR-05a/b, CR-06a/b); severidades asignadas
  (Tabla 24).
- **Declaración:** "Especificadas a nivel de criterios de activación; su validación
  requiere módulos (MOT, zonas) definidos como extensiones condicionadas que el
  núcleo no exige (DA-06)."
- **Habilitación futura:** E-03 + parametrización de zonas + escenas con maquinaria.

### E-03 — MOT formal en el flujo de plataforma / métricas MOT (REDEFINIDA 2026-07-09; acotada por ADR-002)

- **Cambio de situación (1):** la rama `mati` implementó un tracker IoU liviano con ids
  estables (`SimpleIoUTracker`, en `eovrt_labs`) y el motor ya opera por sujeto con
  expiración y cooldown (doc 01 §12).
- **Cambio de situación (2 — ADR-002, cierra D2):** el tracker **se porta al
  media-plane** como componente opcional post-normalización (`track_id` aditivo en
  `media.detection.v1`) y G1 entra al alcance como **capacidad demostrativa**
  (2–3 clips, comparación de episodios G0 vs G1). **Lo excluido queda acotado a:**
  (a) G1 como modo del núcleo (el núcleo evalúa en G0, escena/fuente), y (b) las
  métricas MOT estándar y el GT de identidades que exigirían (Tabla D.2 → E-10).
- **Justificación (ajustada):** el núcleo sigue sin exigir identidad persistente por
  definición metodológica (§17.1.10.2); G1 se muestra como extensión operativa del
  contrato sin prometer atribución por sujeto validada — la demo no requiere GT MOT
  y es lo primero que se sacrifica si la agenda aprieta (§2, orden de sacrificio).
- **Rastro documental:** decisión D2 con análisis (doc 03 §3); contrato `track_id`
  opcional especificado (docs 03/05); métrica ΔFP_tracker definida y con regla de
  aplicación (Tabla D.2) para cuando se habilite; semántica G1 descrita (doc 04 §
  granularidad, doc 07 D2).
- **Declaración:** "El núcleo evalúa a nivel de patrón por fuente y condición,
  conforme §17.1.10.2. La atribución por sujeto individual se implementa como
  capacidad demostrativa (contrato `track_id` opcional, tracker liviano IoU) y se
  ilustra sobre clips seleccionados; su validación rigurosa (métricas MOT, GT de
  identidades) queda fuera del alcance conforme Tabla D.2."
- **Habilitación futura:** GT de identidad + ΔFP_tracker con unidad de FP declarada,
  solo si se exigen métricas MOT estándar (E-10).

### E-04 — Fine-tuning / adaptación al dominio / rol TN

- **Justificación:** la regla del informe es explícita: "no prescribe que el
  fine-tuning deba ejecutarse; define cuándo vale la pena" (Tabla 37). La baseline
  zero-shot —el prerequisito— sí se ejecutó (R1/Sprint 2). La exclusión es por
  **presupuesto de tiempo del proyecto**, no por recursos (el TN/Mendieta existe y
  está caracterizado en §17.1.4.3) ni por falta de datos (el split train_v2 con 5540
  imágenes ya está generado en el repo datasets — evidencia de preparación). Riesgo
  que evita: ciclo costoso con "retorno metodológico débil" (Tabla 37) y erosión de
  la capacidad open-vocabulary (§15.2.4.5).
- **Rastro documental:** protocolo comparativo completo especificado (Tabla 32:
  ΔAP/ΔRecall/ΔPrecision/ΔSDR, retención generalista, costo de entrenamiento);
  particiones sin leakage definidas y **materializadas** (splits v2 del repo);
  candidatos acotados (GDINO/YOLOE, §17.1.9.2).
- **Declaración:** "Rama comparativa condicionada no ejercida: la baseline zero-shot
  fue establecida (requisito de la Tabla 37), el protocolo comparativo y las
  particiones quedaron especificados y materializados, y la ejecución del ajuste se
  difirió por presupuesto del proyecto sin afectar la pregunta central, que evalúa
  precisamente el desempeño sin entrenamiento."
- **Habilitación futura:** disponibilidad de Mendieta + ganancia exigible según
  Tabla 37; todo lo demás ya está listo. **La contingencia quedó armada** (2026-07-09):
  investigación completa con escalera de ejecución T1–T3 y criterios go/no-go
  pre-registrados en `20-investigacion-finetuning-condicionada-e04.md` — si aparece
  tiempo, se ejecuta sin investigación previa.

### E-05 — Broker de eventos (Kafka/RabbitMQ/NATS)

- **Justificación:** DA-03 separa transporte de persistencia y fija el log como
  fuente de verdad; un broker aportaría durabilidad/replay que el JSONL ya provee, al
  costo de un servicio pesado en la ruta de la plataforma (WSL). ZeroMQ cubre el
  fan-out requerido con dependencia nula de infraestructura.
- **Rastro documental:** análisis comparativo con criterios (doc 05 §7); seam
  documentado (`BrokerSource`/`BrokerPublisher`, doc 06 §17); decisión D3 (doc 03 §4).
- **Declaración:** "El bus transporta y el log persiste (DA-03); la incorporación de
  un broker queda como implementación adicional del mismo contrato, sin cambios en
  productores ni consumidores (seam documentado)."

### E-06 — Canales de distribución adicionales y dashboard dedicado

- **Justificación:** la Etapa 3 solo exige consumidores desacoplados con registro de
  intento/resultado (§17.3.10.3); un canal (MQTT) basta para demostrar el tramo y
  medir t_alert-notification. El dashboard dedicado duplicaría la webconsole.
- **Rastro documental:** diseño completo del módulo (doc 06: 4 canales, retry,
  dead-letter, dashboard) conservado como anexo de diseño; recorte D5 con
  fundamentos (docs 02 §4.7, 03 §6).
- **Declaración:** "Se implementa el tramo de distribución con un canal demostrativo
  (MQTT) y ledger de idempotencia; los canales restantes quedan diseñados (anexo) y
  su incorporación no altera la semántica de la alerta (DA-13)."

### E-07 — Inferencia en borde, preselección EN-2 y OAK-D Pro PoE

- **Justificación:** la inferencia OVD en borde está excluida del flujo base por el
  propio informe (§17.1.4.2.3: "no forma parte del flujo base"; EN limitado a 1.4
  TOPS); la preselección EN-2 es condicionada con riesgo de pérdida de evidencia
  (DA-11, Tabla 57). **Update 2026-07-13:** el hardware OAK-D Pro PoE ya está
  disponible e integrado al media-plane **como fuente RGB** (plugin `oak_d`,
  verificado E2E); la contingencia cámara IP (§17.1.4.2.4) se ejerció antes y
  sigue vigente como alternativa. Lo que sigue excluido es la **inferencia en el
  borde** (EN-2): la OAK solo captura, el modelo corre en el host. **Update
  2026-07-15:** la preselección EN-2 (que no es inferencia OVD, sino una
  compuerta con un detector cerrado liviano) dejó de ser condicionada-no-ejercida:
  se implementó como variante opcional de corrida sobre la OAK-D, apagada por
  defecto (`e-ovrt_media-plane/docs/superpowers/specs/2026-07-15-oak-d-prefilter-en2-design.md`),
  cumpliendo las tres condiciones de DA-11/Tabla 57 (criterio conservador
  fail-open, registro de descartes en `summary.json`, corrida A/B de
  comparación contra el flujo sin preselector). La inferencia OVD (EN-3) sigue
  sin ejercerse: el modelo de vocabulario abierto sigue corriendo en el CPN. En
  la topología two-node los contadores de descarte de EN-2 todavía no viajan al
  nodo de referencia y quedan declarados no disponibles (v1).
- **Rastro documental:** modos EN-0/1/2 especificados (Tabla 56); contingencia
  documentada en el informe; el two-node implementado ya materializa EN-0/EN-1;
  EN-2 implementada y documentada en el spec 2026-07-15 y en Tabla 56 actualizada
  del media-plane.
- **Declaración:** "El rol EN opera en modos EN-0/EN-1 (captura y preprocesamiento no
  semántico), materializados en la topología two-node, y EN-2 (preselección
  liviana conservadora), implementada como variante opcional apagada por
  defecto conforme DA-11 y Tabla 57; la inferencia en borde (EN-3) permanece
  fuera de alcance conforme §17.1.4.2.3."

### E-08 — Zonas, geofences y calibración de escena

- **Justificación:** dependencia exclusiva de CR-06 (excluida, E-02); presupone
  cámara fija y parametrización externa al prompt (§17.1.5.2.4).
- **Rastro documental:** lógica punto-en-polígono y requisitos especificados
  (§17.1.5.3.6).
- **Declaración:** incluida en la de E-02.

### E-09 — Prompts en español / evaluación multilingüe

- **Justificación:** el inglés como idioma primario está fundamentado (§17.1.5.4.3);
  la línea multilingüe es explícitamente complementaria y opcional en el informe.
- **Declaración:** "Línea complementaria prevista en §17.1.5.4.3, no ejercida;
  contribución adicional posible, sin impacto sobre las conclusiones del núcleo."

### E-10 — Métricas MOT estándar (HOTA, DetA/AssA, IDF1, MOTA, IDSW/Frag) y benchmarks MOT17/OVT-B

- **Justificación:** condicionadas a tracker habilitado + GT con identidades
  persistentes (Tabla D.2, §17.1.7.8.2); sin E-03 son **no aplicables** por
  definición del propio framework — este es el caso ejemplar de la taxonomía de
  aplicabilidad.
- **Declaración:** "No aplicables: tracker no habilitado en el núcleo (§17.1.10.2);
  condición de aplicación no satisfecha conforme §17.1.7.8.2." (En el reporte
  consolidado deben figurar con ese estado, no omitirse.)

### E-11 — Evidencia visual automática por alerta (clips/snapshots en runtime)

- **Justificación:** la política de minimización (DA-08/09) hace de la *ausencia* de
  captura automática una decisión de diseño, no una carencia. La evidencia visual
  para el informe y la defensa se genera offline con el overlay renderer sobre
  material escenificado con consentimiento.
- **Declaración:** "La trazabilidad ordinaria se apoya en eventos y metadatos
  (DA-08); la evidencia visual se produce como artefacto controlado offline para
  comunicación académica (DA-09)."

### E-12 — Persistencia robusta (base de datos), multi-run concurrente, hardening de servicio

- **Justificación:** ADR-0003 del control-plane (JSONL append-only, "una base más
  robusta puede incorporarse cuando la lógica esté estabilizada"); el prototipo es
  experimental, no productivo (§17.3.3). Un run activo por vez es una simplificación
  declarada del media-plane.
- **Declaración:** "Persistencia experimental append-only conforme ADR-0003;
  capacidades operacionales de producto (DB, concurrencia, autenticación, retención)
  fuera del alcance del prototipo experimental."

### E-13 — Modelos OVD adicionales (Florence-2, OWL-ViT, YOLO-World…) y E-HYB-vote

- **Justificación:** los candidatos de trabajo quedaron acotados a GDINO y YOLOE por
  el propio protocolo (§17.1.9.2) tras la comparación de 5 variantes en R1/Sprint 2
  (que ya cumplió el rol de barrido de modelos). E-HYB-vote (fusión ponderada) solo
  se justificaría con evidencia de complementariedad que la Fase 1 de D1 debe
  mostrar; sin ella, agregarla sería complejidad sin retorno (Tabla 38, riesgo 4).
- **Declaración:** "El barrido de modelos se realizó en la baseline (R1); el
  protocolo concentra la comparación en dos candidatos que representan los polos del
  trade-off expresividad-latencia (§17.1.9.2)."

## 4. Tabla resumen (para pegar en Etapa 4 / anexo del informe)

| # | Capacidad | Estado | Regla del informe que la ampara | Rastro |
|---|---|---|---|---|
| E-01 | CR-03/CR-04 | Especificada, no implementada | Tabla 17; Tabla C.3 (0 fuentes); Tabla 38 | Tabla 24, Anexo C |
| E-02 | CR-05/CR-06 | Especificada (criterios de activación) | Tabla 23; §17.1.5.2.4 | §17.1.5.3.6, Anexo C |
| E-03 | G1 como modo del núcleo / GT de identidades | Acotada: G1 demostrativa SÍ se implementa (ADR-002); validación MOT excluida | DA-06; §17.1.10.2 | ADR-002; docs 03/04/05; Tabla D.2 |
| E-04 | Fine-tuning / TN | Condicionada no ejercida | Tabla 37; §15.2.4.5 | Tabla 32; splits v2 materializados |
| E-05 | Broker | Diseñada (seam) | DA-03 | docs 05 §7, 06 §17 |
| E-06 | Canales extra + dashboard | Diseñada (anexo) | §17.3.10.3; DA-13 | doc 06 completo |
| E-07 | Borde / EN-2 / OAK-D | Parcial: OAK-D como **fuente** ejercida (2026-07-13) y EN-2 (preselección) implementada opcional, default off (2026-07-15); inferencia en borde (EN-3) sigue no ejercida | DA-11; §17.1.4.2.3–4 | Tabla 56; two-node = EN-0/1/2 |
| E-08 | Zonas / calibración | Especificada | §17.1.5.2.4 | §17.1.5.3.6 |
| E-09 | Prompts multilingües | Prevista no ejercida | §17.1.5.4.3 | — |
| E-10 | Métricas MOT estándar | No aplicable | Tabla D.2; §17.1.7.8.2 | reporte con estado |
| E-11 | Evidencia visual runtime | Excluida por diseño | DA-08/09 | overlay offline |
| E-12 | DB / hardening | Fuera de alcance de prototipo | ADR-0003; §17.3.3 | ADRs control-plane |
| E-13 | Modelos extra / E-HYB-vote | Acotada por protocolo | §17.1.9.2; Tabla 38 | R1/Sprint 2; doc 04 §5 |

## 5. Reglas de redacción para que el cierre no suene a deuda

1. **Cada exclusión se declara donde se define, no al final**: cuando el informe
   introduce la capacidad, en la misma sección dice su estado y su regla — el lector
   nunca descubre "faltantes" por su cuenta.
2. **Usar la taxonomía de aplicabilidad** para métricas (no aplicable ≠ no medido) y
   los estados del §1 para capacidades — vocabulario consistente en todo el texto.
3. **Toda exclusión cita su regla previa** (Tabla 17/37/D.2, DA-XX): la decisión se
   tomó *antes* de los resultados, no después — eso es lo que la vuelve metodología y
   no excusa.
4. **Mostrar el rastro**: "especificada" siempre con puntero al artefacto (tabla,
   anexo, contrato, split generado). Una exclusión con artefactos es trabajo hecho.
5. En la defensa oral, si preguntan por algo excluido: estado + regla + rastro +
   habilitación futura, en ese orden, 20 segundos. (Se suma al Q&A del doc 09.)

## 6. Ajustes que este registro aplica al resto del set

*(Vigentes al cierre de esta auditoría, 2026-07-07. **Superados por decisiones
posteriores del 2026-07-09** donde se indica — ver `decisiones/ADR-002` y
`ADR-001`/doc 12; se conservan como registro histórico de por qué se pensó así.)*

- **Doc 02 §5 (recorte):** G1/tracker sale de "should" y pasa a exclusión E-03
  (especificada); el "should" queda solo con refinamientos menores del motor
  (cooldown) y el segundo canal se elimina (E-06). ✎ Aplicado. **✎ Nota posterior:**
  el cooldown se implementó en `mati` y ADR-011 lo reubicó en distribución — ya no
  es refinamiento del motor.
- **Doc 03 (tablero):** sin cambios de decisiones; D2 queda reforzada (G0 sin
  vía G1 en este proyecto). **✎ Superado 2026-07-09 (ADR-002):** D2 se cerró
  como G0 núcleo **+ G1 demostrativa** (tracker portado al media-plane, 2–3
  clips, sin métricas MOT) — ver E-03 arriba (§3), ya redefinida en consecuencia.
- **Doc 04:** E-HYB limitada a or/and condicionada a complementariedad; vote → E-13.
  (Ya estaba condicionada así; sin edición necesaria.) **✎ Superado 2026-07-09
  (ADR-001, doc 12):** la condición de complementariedad se retira — E-HYB-or/and
  corre siempre en la Fase 2 como rama experimental de primera clase; vote sigue
  excluida (E-13, sin cambios).
- **Plan 12 semanas:** las semanas 7–8 pierden el ítem "G1 sobre 2–3 clips si sobra
  agenda" — ese margen se reasigna a overlay renderer + guion de grabación.
  **✎ Superado 2026-07-09 (ADR-002):** la demo G1 sobre 2–3 clips vuelve a las
  semanas 7–8 como ítem 10 del §2, primera en el orden de sacrificio tras 11-UX.
