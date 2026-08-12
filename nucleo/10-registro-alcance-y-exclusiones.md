# Registro de alcance y exclusiones — cierre formal del "no se implementa"

> ✎ **2026-08-05 — el alcance final NO es exactamente el de este doc.** El tramo
> experimental completo (docs 61–101) movió cuatro exclusiones, y eso está registrado en
> **[ADR-015 — Cierre de alcance](../decisiones/adr-015-cierre-de-alcance.md)**
> (✅ **aceptada el 2026-08-05, y ya aplicada abajo**: ítem 10 de la lista de alcance +
> filas E-03/E-04/E-07/E-13 de la tabla de exclusiones):
> **E-03** — G1 dejó de ser "demostrativa en 2–3 clips": es **capacidad operativa medida
> en 34/34 clips** (F1 0,930 vs 0,789 de G0) y verificada en vivo. Sigue excluido el GT de
> identidades y la validación MOT · **E-07** — parcial (OAK-D como fuente + EN-2 con 87%
> de descarte on-device) · **E-13** — E-HYB-or **ejecutada y refutada**; `hyb_and` no
> ejecutada con causa · **E-04** — *(⚠️ esta línea quedó **derogada por ADR-017**, ver el
> tercer banner: el encuadre por «secuenciación» está prohibido)* sigue no ejercida, pero por secuenciación, no por falta
> de preparación. **E-10 no cambia** (métricas MOT siguen "no aplicable"), y las otras
> ocho exclusiones tampoco. ADR-015 además **cierra la puerta**: ninguna capacidad nueva
> de acá a la defensa, y la distribución MQTT queda declarada NO implementada.
>
> ✎ **2026-08-10 — esas dos últimas cláusulas están DEROGADAS por
> [ADR-016](../decisiones/adr-016-reapertura-acotada-distribucion.md).** El usuario decidió
> **implementar la distribución de alertas** para cerrar la arquitectura de la plataforma,
> con el recorte exacto de ADR-005 y nada más (**E-06 sigue excluida**). Nada más se
> reabre: E-04, EN-3, E-10 y las condiciones CR nuevas siguen cerradas. **La
> implementación no bloquea el informe** — el cierre arquitectónico lo entrega
> `nucleo/19`, y si el módulo no llega a tiempo se declara como estaba. Ver el **ítem 5**
> más abajo, ya actualizado.
>
> ✎ **2026-08-11 — E-04 sale de esa lista por
> [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md).** El fine-tuning
> **se ejerce como jornada experimental completa** (escalera pre-registrada T1→T2/T3 con
> go/no-go, entrenamiento en Mendieta, evaluación contra `bench_v3`, documentación de
> resultados **y limitaciones**), y su encuadre pasa a **rama experimental condicionada
> por datos y protocolo desde el planteo inicial** — las causas "presupuesto de tiempo"
> (julio) y "secuenciación" (ADR-015) quedan **derogadas como lectura**: el cómputo no es
> la restricción (≤1 GPU-h medido) y el cronograma lo define el proyecto. Ver la ficha
> **E-04**, ya actualizada. Siguen cerradas EN-3, E-10, E-06 y las condiciones CR nuevas.

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
3. **Clip bench** con GT temporal (grabación escenificada) y evaluación de alertas
   contra umbrales Tabla D.4. (✎ 2026-08-06: el GT quedó `gt_ready` **sin doble
   anotación ni kappa** — es la **limitación L2**, decisión declarada y no omisión;
   *decía "doble anotación 20%+kappa"*, que volvía a L2 un incumplimiento de esta
   definición de terminado.)
4. **EBE complementario sobre la infraestructura two-node ya construida** (Nodo A =
   EN-0/EN-1, Nodo B = CPN) con fuente viva de contingencia oficial (cámara IP/webcam
   o RTSP simulado). Se implementa porque ya existe (Fase 2 verificada) y produce R4
   con costo marginal bajo — no es una ampliación de alcance sino capitalización de
   trabajo hecho.
5. **Distribución mínima — EN ALCANCE, aún no implementada** (✎ reescrito 2026-08-10
   conforme **ADR-016**; *decía "NO IMPLEMENTADA, exclusión ejercida" por ADR-015 §2c
   entre el 08-05 y el 08-10, y antes de eso describía el alcance sin estado*): un canal
   **MQTT** + `NotificationEnvelope` + ledger de idempotencia + retry mínimo + **vista de
   alertas en la webconsole existente**, en repo propio, consumiendo el bus
   control→distribución (ADR-005). El condicional del ADR-005 quedó resuelto en **sí**,
   por un motivo **arquitectónico**: es donde se gestiona el ciclo de vida completo de la
   alerta y su distribución, incluidas las políticas que ADR-011 sacó del motor
   (cooldown, supresión por ventana, re-notificación, agrupación). **E-06 sigue
   excluida** (canales adicionales y dashboard dedicado). Construido a la fecha: solo la
   frontera de salida del control-plane (`control.alert.v1`). **No bloquea el informe**:
   el cierre arquitectónico lo entrega `nucleo/19` y, si el módulo no llega a tiempo, se
   declara como estaba (ADR-016 §2d).
6. **Bus ZeroMQ media→control** (necesario para el punto 4).
7. **Overlay renderer** offline (videos V1–V3 de la defensa + figuras del informe).
8. **Mini-experimento A1** (costo marginal de una condición nueva por configuración).
9. **Control-plane como servicio mínimo** (ADR-008, 2026-07-09): cáscara HTTP sobre
   el runtime live (disparo, estado, config efectiva) + webconsole como cliente de
   ambos planos. Sin sesiones/auth/concurrencia (E-12 sigue vigente).
10. **G1 — capacidad operativa medida** (ADR-002 + **ADR-015**, actualizado 2026-08-05;
    *decía "G1 demostrativa … demostrada en 2–3 clips"*): granularidad por sujeto
    **config-driven**, medida sobre **los 34 clips del banco** (F1 0,930 vs 0,789 de G0,
    con las detecciones bit a bit idénticas) y verificada en vivo. El tracker vive en el
    control-plane. Sin métricas MOT (E-10 sigue "no aplicable"). Redefine E-03.
11. **Config centralizada + webconsole como superficie de gestión** (ADR-009,
    2026-07-09): configuración experimental de ambos planos versionada en
    experimental-setup; webconsole gestiona configs y dispara corridas en los dos
    servicios, con mejora de UI/organización UX (navegación por experimento).

Nada fuera de esta lista entra a implementación. Si algo de la lista peligra por
tiempo, el orden de sacrificio es: **11-UX (la mejora visual; la centralización de
config no se sacrifica — la usa el runner) → 10 → 9 (queda el runner CLI; el
runtime live no se sacrifica) → 8 → 7 (se reemplaza por overlays simples) → 5 (se
reduce a `mosquitto_sub`)** — nunca 1, 2 ni 3.

> ✎ **2026-08-06 — el orden de sacrificio quedó obsoleto** (ADR-015 §2b cerró la
> agenda de implementación): el ítem 10 terminó **creciendo** (G1 medida, el mejor
> resultado del banco) y el ítem 5 se declaró **no implementado** con causa. Se
> conserva como registro de cómo se priorizó; ya no es una lista de candidatos.

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
- **Cambio de situación (3 — adenda ADR-002 ratificada + ADR-015, 2026-08-05; ✎
  propagado acá 2026-08-06):** dos correcciones sobre el punto anterior. (a) El
  tracker **no** se portó al media-plane: se implementó **en el control-plane como
  decorador de fuente** (adenda ADR-002; la deuda del spec 42 §3 queda abierta pero
  no bloqueante). (b) G1 **dejó de ser demostrativa**: es capacidad operativa
  config-driven **medida sobre los 34 clips del banco** (F1 0,930 vs 0,789 de G0,
  con detecciones bit a bit idénticas — F-89.1) y verificada en vivo. Lo excluido no
  cambia: G1 como modo del núcleo, y las métricas MOT / GT de identidades (E-10).
- **Justificación (ajustada):** el núcleo sigue sin exigir identidad persistente por
  definición metodológica (§17.1.10.2); G1 se muestra como extensión operativa del
  contrato sin prometer atribución por sujeto validada — no requiere GT MOT.
  (✎ 2026-08-06: *decía además "la demo … es lo primero que se sacrifica si la
  agenda aprieta"* — obsoleto: ADR-015 §2b cerró la agenda y G1 terminó siendo el
  mejor resultado del banco.)
- **Rastro documental:** decisión D2 con análisis (doc 03 §3); contrato `track_id`
  opcional especificado (docs 03/05); métrica ΔFP_tracker definida y con regla de
  aplicación (Tabla D.2) para cuando se habilite; semántica G1 descrita (doc 04 §
  granularidad, doc 07 D2).
- **Declaración (✎ reescrita 2026-08-06 conforme ADR-015 E-03):** "El núcleo evalúa
  a nivel de patrón por fuente y condición, conforme §17.1.10.2. La atribución por
  sujeto individual se implementa como **capacidad operativa config-driven**
  (contrato `track_id` opcional, tracker IoU liviano como decorador en el
  control-plane), **medida sobre los 34 clips del banco** (F1 0,930) y verificada en
  vivo; su validación con métricas MOT y GT de identidades queda fuera del alcance
  conforme Tabla D.2 (E-10)." (*Decía: "…se implementa como capacidad demostrativa …
  y se ilustra sobre clips seleccionados; su validación rigurosa … queda fuera del
  alcance…"*)
- **Habilitación futura:** GT de identidad + ΔFP_tracker con unidad de FP declarada,
  solo si se exigen métricas MOT estándar (E-10).

### E-04 — Fine-tuning / adaptación al dominio / rol TN

- **Estado (✎ 2026-08-11, [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md)):**
  **rama experimental comprometida — se ejerce como jornada completa de fine-tuning**:
  preparación de datos y entorno, entrenamiento en Mendieta, evaluación contra
  `bench_v3` y documentación de resultados **y limitaciones**. La forma es la escalera
  pre-registrada — **T1 (linear probing) como entrada**, escalamiento a T2/T3 gobernado
  por los go/no-go de la Tabla 37 y `contingencia/20` §6, sin prometer tiers por
  adelantado. Deja de ser exclusión.
- **Justificación del encuadre:** la regla del informe es explícita: "no prescribe que
  el fine-tuning deba ejecutarse; define cuándo vale la pena" (Tabla 37) — la rama fue
  **experimental y condicionada desde el planteo inicial**, nunca un descarte. La
  baseline zero-shot —el prerequisito de la regla— se ejecutó (R1/Sprint 2) y el
  benchmarking cerró. Las condiciones reales que la jornada atraviesa son **de datos y
  de protocolo**: F-100.1 (no existe validación con `bare_head` fuera del bench
  congelado — doc 100 §4), licencias y transporte (entrenar en el clúster, evaluar
  local — doc 100 §6.3) y el riesgo de erosión de la capacidad open-vocabulary
  (§15.2.4.5). **No son de cómputo** (el TN/Mendieta existe y está caracterizado en
  §17.1.4.3; costo medido ≤1 GPU-h en A30 para T1, doc 100) **ni de plazo** (el
  cronograma lo define el proyecto). (✎ histórico: esta ficha declaró primero
  "presupuesto de tiempo del proyecto" —julio— y luego "secuenciación" —ADR-015,
  2026-08-06—; **ADR-017 deroga ambas causas como encuadre del informe**.)
- **Rastro documental:** protocolo comparativo completo especificado (Tabla 32:
  ΔAP/ΔRecall/ΔPrecision/ΔSDR, retención generalista, costo de entrenamiento);
  particiones sin leakage definidas y **materializadas** (splits v2 del repo; train ∩
  `bench_v3` = 0 verificado); candidatos acotados (GDINO/YOLOE, §17.1.9.2); escalera
  T1–T3 con presupuestos GPU y go/no-go pre-registrados (`contingencia/20`); costo T1
  medido con smoke verde end-to-end (doc 100).
- **Declaración (✎ reescrita 2026-08-11 conforme ADR-017):** "Rama comparativa
  experimental, condicionada desde el diseño metodológico (Tabla 37: baseline
  zero-shot primero, ajuste cuando la regla lo amerita): la baseline fue establecida,
  el protocolo comparativo y las particiones quedaron especificados y materializados,
  el costo de ejecución quedó medido (≈1 GPU-h en A30, doc 100), y la jornada de
  fine-tuning se lleva a cabo documentando sus resultados y limitaciones — sin afectar
  la pregunta central, que evalúa precisamente el desempeño sin entrenamiento."
  (*Decía "no ejercida por secuenciación del tramo experimental"*, y antes *"se
  difirió por presupuesto del proyecto"*.)
- **Puertas previas a pedir turno (no se saltean):** decisión del usuario sobre
  F-100.1 (tres enmiendas posibles, doc 100 §4) + checklist de viabilidad completa
  (doc 100 §6: entorno reproducible, transporte, puente de evaluación). El estado de
  la jornada al momento de la entrega se declara tal cual, con causa técnica —
  nunca temporal (ADR-017 §2f).

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
- **Declaración (✎ reescrita 2026-08-06 conforme ADR-015 §2c):** "El tramo de
  distribución queda en la frontera de salida del control-plane (`control.alert.v1`);
  el canal demostrativo (MQTT), el ledger de idempotencia y los canales restantes
  quedan **diseñados y no implementados** (spec 45 + anexo doc 06, exclusión
  ejercida), y su incorporación futura no altera la semántica de la alerta (DA-13)."
  (*Decía: "Se implementa el tramo de distribución con un canal demostrativo (MQTT) y
  ledger de idempotencia…"* — contradicción con ADR-015 detectada en el relevamiento
  del 2026-08-06.)

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

- **Justificación (✎ actualizada 2026-08-06 conforme ADR-015 §2e / R-21):**
  condicionadas a **GT con identidades persistentes**, que no existe (Tabla D.2,
  §17.1.7.8.2). El antecedente viejo ("sin E-03 son no aplicables") ya no corre: el
  tracker **está habilitado y medido** (G1, F1 0,930 en 34 clips). Lo excluido son
  las **métricas** MOT y el GT de identidades, **no la capacidad**. El fundamento
  ahora es medido, no solo definicional: la ganancia de G1 se mide en alertas porque
  las detecciones son bit a bit idénticas (F-89.1) — la mejora no es de percepción y
  no se expresaría en MOTA/IDF1.
- **Declaración (✎ reescrita 2026-08-06; la anterior es la formulación que ADR-015
  §2e marca como FALSA al cierre):** "No aplicables: no existe GT de identidades
  persistentes, condición de aplicación no satisfecha conforme §17.1.7.8.2; la
  granularidad por sujeto está implementada y medida a nivel de alertas (E-03,
  F-89.1), y su validación con métricas MOT queda fuera del alcance." (*Decía: "No
  aplicables: tracker no habilitado en el núcleo (§17.1.10.2)…"*. En el reporte
  consolidado deben figurar con estado `not_applicable:<causa>`, no omitirse.)

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
- **Declaración:** "Persistencia experimental append-only conforme ADR-0003 (serie
  del control-plane, 4 dígitos);
  capacidades operacionales de producto (DB, concurrencia, autenticación, retención)
  fuera del alcance del prototipo experimental."

### E-13 — Modelos OVD adicionales (Florence-2, OWL-ViT, YOLO-World…) y E-HYB-vote

- **Justificación:** los candidatos de trabajo quedaron acotados a GDINO y YOLOE por
  el propio protocolo (§17.1.9.2) tras la comparación de 5 variantes en R1/Sprint 2
  (que ya cumplió el rol de barrido de modelos).
  > ✎ **2026-08-10 — trazabilidad de ese barrido, porque era la pata más débil de esta
  > exclusión.** El "R1/Sprint 2" no tiene documento propio en la serie `docs/`; el
  > artefacto **auditable** equivalente es **`operacion/31-benchmark-modelos-host-local.md`**
  > (2026-07-09), que mide calidad en BENCH v2 val + rendimiento live. Dos precisiones que
  > hay que hacer al citarlo: **(1)** el doc 31 barre **6 variantes**, no 5
  > (`gdino-tiny`, `gdino-base`, `yoloe-26s/m/l/x`) — el "5" viene de `nucleo/historicos/02` y del
  > ADR-001, y el propio ADR-001 los trata como artefactos distintos; **(2)** el doc 31 se
  > declara **posterior** a Sprint 2 (hace *cross-check* contra él), así que no ES Sprint 2:
  > es su reemplazo auditable. El barrido total sobre la familia OVD, sumando la selección
  > S1/S2 del doc 64, llega a **10 configuraciones**. **Nada de esto cambia la exclusión**
  > —Florence-2, OWL-ViT y YOLO-World nunca se probaron y siguen excluidos por alcance—,
  > pero sí cambia **qué documento se cita**: citar `operacion/31` + `operacion/64`, no
  > "Sprint 2" a secas, que remite a un artefacto fuera de esta serie. (✎ 2026-08-06, ADR-015 E-13: la
  condición sobre E-HYB **ya se resolvió por medición** — E-HYB-or se **ejecutó y
  quedó refutada** (recall 0,824→0,353; mecanismo F-87.2: la unión de evidencia no
  es monótona en un motor temporal) y **`hyb_and` no se ejecutó con causa** (D-90.4:
  no medible contra este banco sin romper la comparabilidad de las 6 campañas).
  *Decía en futuro: "evidencia de complementariedad que la Fase 1 de D1 debe
  mostrar"*.) E-HYB-vote (fusión ponderada) sigue fuera: sin complementariedad
  demostrada, agregarla sería complejidad sin retorno (Tabla 38, riesgo 4).
- **Declaración:** "El barrido de modelos se realizó en la baseline (R1); el
  protocolo concentra la comparación en dos candidatos que representan los polos del
  trade-off expresividad-latencia (§17.1.9.2)."

## 4. Tabla resumen (para pegar en Etapa 4 / anexo del informe)

| # | Capacidad | Estado | Regla del informe que la ampara | Rastro |
|---|---|---|---|---|
| E-01 | CR-03/CR-04 | Especificada, no implementada | Tabla 17; Tabla C.3 (0 fuentes); Tabla 38 | Tabla 24, Anexo C |
| E-02 | CR-05/CR-06 | Especificada (criterios de activación) | Tabla 23; §17.1.5.2.4 | §17.1.5.3.6, Anexo C |
| E-03 | G1 como modo del núcleo / GT de identidades | ✎ **Ampliada (ADR-015, 2026-08-05)**: G1 no es demostrativa — es **capacidad operativa medida en los 34 clips** (F1 0,930) y verificada en vivo. **Sigue excluido**: GT de identidades y validación MOT | DA-06; §17.1.10.2 | ADR-002 + adenda 08-04; **ADR-015**; doc 89; `results/clip_bench/g1_*` |
| E-04 | Fine-tuning / TN | ✎ **Rama experimental comprometida (ADR-017, 2026-08-11)**: se ejerce como **jornada completa** — escalera T1→T2/T3 con go/no-go pre-registrados, entrenamiento en Mendieta, eval contra `bench_v3`, resultados y limitaciones documentados. Encuadre: condicionada **por datos y protocolo** (F-100.1, licencias, Tabla 37), no por cómputo (≤1 GPU-h medido) ni por plazo | Tabla 37; §15.2.4.5 | Tabla 32; splits v2 materializados; doc 100; `contingencia/20`; **ADR-017** |
| E-05 | Broker | Diseñada (seam) | DA-03 | docs 05 §7, 06 §17 |
| E-06 | Canales extra + dashboard | Diseñada (anexo) | §17.3.10.3; DA-13 | doc 06 completo |
| E-07 | Borde / EN-2 / OAK-D | Parcial: OAK-D como **fuente** ejercida (2026-07-13) y EN-2 (preselección) implementada opcional, default off (2026-07-15), con **87% de descarte on-device** medido A/B contra GDINO; inferencia en borde (EN-3) sigue no ejercida | DA-11; §17.1.4.2.3–4 | Tabla 56; two-node = EN-0/1/2; **ADR-015** |
| E-08 | Zonas / calibración | Especificada | §17.1.5.2.4 | §17.1.5.3.6 |
| E-09 | Prompts multilingües | Prevista no ejercida | §17.1.5.4.3 | — |
| E-10 | Métricas MOT estándar | ✎ **No aplicable, con fundamento medido (ADR-015)**: lo excluido son las **métricas** y el GT de identidades, no la capacidad (el tracker está medido — E-03); la ganancia de G1 se mide en alertas porque las detecciones son bit a bit idénticas (F-89.1) | Tabla D.2; §17.1.7.8.2 | reporte con estado; **ADR-015**; doc 89 |
| E-11 | Evidencia visual runtime | Excluida por diseño | DA-08/09 | overlay offline |
| E-12 | DB / hardening | Fuera de alcance de prototipo | ADR-0003; §17.3.3 | ADRs control-plane |
| E-13 | Modelos extra / E-HYB-vote | ✎ **Ejercida más de lo previsto (ADR-015)**: modelo especialista corrido (T2/B1) y **E-HYB-or ejecutada y REFUTADA** (F-87.2: la unión de evidencia no es monótona en un motor temporal). **`hyb_and` no ejecutada con causa** (D-90.4: no medible contra este banco sin romper la comparabilidad de las 6 campañas). E-HYB-vote sigue fuera | §17.1.9.2; Tabla 38 | R1/Sprint 2; doc 04 §5; docs 84/87/88; **ADR-015** |

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
