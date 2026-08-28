# Indicaciones de corrección — sobre los tres documentos que generaste (2026-08-23)

Revisamos los tres `.docx` que entregaste contra las instrucciones de los pases. El contenido
que elegiste es el correcto, pero **la integración falló de una forma específica**: agregaste
sin quitar. Esta pasada corrige eso **editando los documentos ya generados** — no los
regeneres desde cero.

**Diagnóstico, para que sepas exactamente qué corregir:**

1. **Ninguna eliminación se ejecutó.** Las 6 tablas, las 4 subsecciones y la columna que los
   pases mandaban eliminar siguen todas en los documentos.
2. **Los reemplazos quedaron como agregados.** Pegaste el texto nuevo al lado del texto viejo
   que debía reemplazar. Ejemplo: §17.3.2 ahora dice lo mismo cuatro veces; §17.4.3 contiene
   la versión vieja y la nueva completas.
3. **Pegaste texto guía sin procesar**: fragmentos con asteriscos de markdown, comillas de
   cita, y celdas de tabla con el separador `||` como si fueran párrafos.
4. **Se filtró material del andamiaje que jamás puede estar en el informe**: dos líneas
   `SHA-256 del bloque: …`, un banner interno de conteo de palabras, una cita diagnóstica que
   empieza `**T40:**`, y una nota editorial que empieza `⚠ Esta unidad reemplaza…`.
5. **Fragmentos en la sección equivocada**: una celda de §17.4 quedó pegada dentro de §17.3,
   y tres párrafos de §17.4.4 quedaron en §17.4.8.
6. **§17.5 quedó como esqueleto**: el esquema de organización pegado como contenido, cero
   cifras, y oraciones rotas donde quitaste los códigos de unidad.

---

## Reglas de esta pasada (no negociables)

1. **Editás los tres documentos existentes** (§17.3 v1.2 → entregás v1.3; §17.4 v1.3 → v1.4;
   §17.5 v1.0 → v1.1). Nada se regenera desde cero.
2. **Toda operación de abajo es de uno de cuatro tipos**: ELIMINAR (el texto desaparece),
   INTEGRAR (un fragmento ya pegado se convierte en prosa o celda del informe: sin asteriscos,
   sin comillas de cita, sin `||`, sin negritas heredadas del markdown), MOVER (un fragmento
   cambia de lugar y se integra allá), o REEMPLAZAR (texto viejo afuera, texto dado adentro).
3. **No agregues contenido propio.** Todo el texto nuevo que hace falta ya está: o pegado en
   el documento, o dado acá, o en el knowledge (unidades E3-/E4- de los pases 2 y 3).
4. **El resultado nunca contiene**: `||` · `SHA-256` · asteriscos de markdown · referencias a
   unidades (E3-, E4-, D-P…), a documentos internos, a fichas ni a rutas · nombres de campaña
   (T1/G1/R1…) fuera del bloque donde se citan como procedencia.
5. **Trabajá por partes y entregá para verificación** en este orden: Parte A+B (§17.3) →
   confirmación → Parte C (§17.4) → confirmación → Parte D (renumeración de ambos) →
   confirmación → Parte E (§17.5). No avances a la parte siguiente sin confirmación.
6. Los marcadores `[[PENDIENTE: …]]` que las operaciones no mencionan **se conservan** (en
   particular el de dirección de origen y fecha de acceso por clip, en §17.4.8.1).

---

## PARTE A — Basura del andamiaje (eliminar primero, en los tres documentos)

Buscá y **ELIMINÁ** estos bloques completos. Ninguno es texto del informe:

- A1 · En §17.3.11: la línea que empieza `SHA-256 del bloque: 9f37e8d3…`.
- A2 · En §17.4.6: la línea que empieza `SHA-256 del bloque: 8a03908d…`.
- A3 · En §17.3.3.2: el bloque que empieza `**T40:** "…'complementario previsto'…` (es una
  cita diagnóstica de un documento de trabajo).
- A4 · En §17.3.14.5: el bloque que empieza `Dato que ordena todo este bloque: §17.3 pesa`
  (es un banner interno de conteo de palabras).
- A5 · En §17.3.11.3: la nota que empieza `⚠ Esta unidad reemplaza a su primera versión`.
- A6 · En §17.4.6: el fragmento que empieza `el ledger deduplica exactos` y termina
  `demasiado seguidas.` (material de otro documento, pegado fuera de lugar; su contenido ya
  está dicho en §17.3.10.3).

---

## PARTE B — §17.3 (v1.2 → v1.3), en orden del documento

### §17.3.2

- B1 · ELIMINAR los cuatro párrafos iniciales (desde `La arquitectura propuesta se construye
  a partir de` hasta `…La Tabla 39 sintetiza esta relación entre definiciones previas y
  decisiones arquitectónicas derivadas.` inclusive) y REEMPLAZARLOS por este único párrafo:

  > La arquitectura propuesta se deriva de las definiciones metodológicas ya consolidadas: el
  > alcance experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios
  > de evaluación, los roles funcionales del entorno, el marco de métricas y los lineamientos
  > ético-legales actúan como restricciones de diseño. Lo que sigue no reitera el protocolo
  > experimental: explicita qué consecuencia arquitectónica se deriva de cada uno de esos
  > insumos, de modo que ningún módulo, frontera o flujo del sistema aparezca como una
  > decisión aislada.

- B2 · ELIMINAR la **Tabla 39** completa con su Nota.
- B3 · ELIMINAR el bloque de viñetas pegado que empieza `"Cada decisión de diseño se vincula
  con un insumo metodológico ya consolidado:` y termina `…comunicación académica."` (fue
  derogado: la prosa desarrollada que le sigue es la que queda).
- B4 · Los seis párrafos desarrollados (`El marco teórico de detección…`, `El núcleo validable
  se concentra…`, etc.) SE CONSERVAN, con dos ediciones:
  - En `el flujo base prioriza la estrategia indirecta E-IND` quitar `E-IND` (el código nace
    después, en §17.3.6.4): queda `…prioriza la estrategia indirecta y comprende…`.
  - REEMPLAZAR el párrafo `Los roles CPN, EN y TN se adoptan como responsabilidades
    funcionales de referencia… servicio o contenedor independiente.` por:

    > De los roles funcionales ya establecidos se deriva una restricción de diseño y no una
    > nueva definición: se adoptan como responsabilidades de referencia que permiten declarar
    > dónde se captura, dónde se ejecuta la inferencia y dónde se prepara una variante
    > ajustada, sin que la distribución física de componentes pase a formar parte de la
    > semántica de los contratos.

- B5 · MOVER el fragmento pegado `"Esta sección no redefine los roles funcionales ya
  establecidos…"` fuera de §17.3.2: es el nuevo primer párrafo de **§17.3.15** (ver B26).

### §17.3.3.1 y §17.3.3.2 (fusión de las Tablas 40 y 41)

- B6 · ELIMINAR la **Tabla 40** completa con su Nota. La prosa de §17.3.3.1 se conserva; si
  alguna oración remite a la Tabla 40, pasa a remitir a la tabla única de §17.3.3.2.
- B7 · La **Tabla 41** queda en §17.3.3.2 retitulada **"Capacidades arquitectónicas y su
  tratamiento en el diseño"**, con estos injertos de la ex Tabla 40:
  - Fila nueva **Video crudo continuo** — *Fuera del comportamiento ordinario* — «La
    trazabilidad principal se apoya en eventos, metadatos, métricas y referencias
    controladas.»
  - Fila nueva **Condiciones de riesgo de Nivel 2 y Nivel 3** — *Extensión condicionada*
    (separada de "Capacidades contextuales y relacionales": una es el catálogo de
    condiciones, la otra los mecanismos).
  - En la fila de identidad temporal/MOT, usar la redacción de la ex Tabla 40: «La
    arquitectura admite granularidad por sujeto mediante una identidad temporal válida. Las
    métricas MOT no condicionan la evaluación del núcleo ni deben confundirse con la
    capacidad de mantener identidad.»
  - En la fila de adaptación al dominio, usar: «Sólo corresponde bajo una línea base
    preentrenada congelada, datos suficientes, partición disjunta y criterios de
    escalamiento definidos con anterioridad a los resultados.»
  - Una sola Nota: la de la Tabla 41 (la más completa).

### §17.3.3.4 (Tabla 43)

- B8 · REEMPLAZAR la celda de Justificación de **DA-03** por: «Cada preocupación tiene un
  régimen propio: el gobierno es puntual y de solicitud–respuesta, el transporte es continuo
  y no debe bloquear la ruta crítica, y la persistencia debe sobrevivir a la corrida para
  habilitar su relectura. Mantenerlas separadas permite sustituir el mecanismo de transporte
  sin alterar el gobierno ni la evidencia, y reevaluar cualquier corrida sin depender de la
  mensajería.» — y ELIMINAR el bloque `**DA-03 · Decisión:** …` que quedó pegado como párrafo
  suelto en §17.3.5.
- B9 · REEMPLAZAR la fila **DA-11** completa por — Decisión: «Permitir preselección liviana
  en el rol de captura como variante opcional, conservadora y deshabilitada por defecto, que
  conserva la unidad en el flujo principal ante falla o incertidumbre del preselector.» ·
  Justificación: «La variante puede reducir carga sin transformar el borde en fuente de
  verdad ni ocultar descartes, porque el flujo base continúa disponible y comparable.»

### §17.3.6

- B10 · En §17.3.6.1, AGREGAR al final estos dos cierres (el segundo es el fragmento ya
  pegado en §17.3.6.6, que se integra acá):

  > Esa función de gobierno sólo se sostiene si la configuración se resuelve y se valida
  > antes de iniciar la ejecución: una corrida cuya declaración esté incompleta debe fallar
  > al crearse y no producir artefactos que luego resulten inatribuibles. La función se
  > proyecta además sobre los tres destinatarios de la configuración: el plano de medios
  > recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control
  > recibe los criterios con los que evalúa, y el soporte experimental la utiliza como clave
  > de reconstrucción, de modo que todo evento, métrica, alerta o evidencia conservada pueda
  > rastrearse hasta la corrida que le dio origen.

- B11 · En §17.3.6.4, REEMPLAZAR la oración que remite a la sección 17.1.5.4.2 (`Las
  consultas negativas o de estado observable se mantienen… (sección 17.1.5.4.2)…`) por:

  > Las consultas negativas o de estado observable se mantienen en conjuntos separados para
  > las estrategias directa e híbrida ya distinguidas en la consolidación metodológica, de
  > modo que sus resultados sean atribuibles a una estrategia explícita y no a una mezcla
  > informal de vocabularios. En el diseño arquitectónico y en lo que sigue del trabajo,
  > estas familias se identifican mediante un código: estrategia directa (E-DIR), cuando el
  > prompt intenta describir la condición de riesgo completa; estrategia indirecta (E-IND),
  > cuando el detector identifica entidades visibles por separado y la condición se
  > reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se
  > combinan consultas de ambos tipos bajo una regla de composición explícita.

- B12 · En §17.3.6.4, ELIMINAR el fragmento pegado `"notifications.jsonl (ledger de intentos
  y entregas…` — es una celda de una tabla de §17.4 y su contenido ya se usa allá (C10).
- B13 · Al final de §17.3.6.5, AGREGAR (integrando el fragmento ya pegado en §17.3.6.6 que
  empieza `"Por la misma razón, ningún módulo opcional…`):

  > Por la misma razón, ningún módulo opcional —evidencia visual, identidad temporal, zonas,
  > preselección en el rol de captura o distribución externa— puede operar como
  > comportamiento implícito: su habilitación se declara en la configuración de la corrida,
  > porque una activación silenciosa alteraría la interpretación de latencia, cobertura
  > temporal, privacidad y aplicabilidad de métricas, es decir, la base misma de la
  > comparación.

- B14 · ELIMINAR completas las subsecciones **§17.3.6.6** ("Validaciones previas al inicio de
  la corrida") y **§17.3.6.7** ("Frontera con los planos…"), incluidos los fragmentos
  pegados que queden dentro. §17.3.6 termina en la 6.5.

### §17.3.7

- B15 · En §17.3.7.3: ELIMINAR el cuarto párrafo completo (`Las capacidades opcionales del
  plano de medios se incorporan sin modificar su contrato de salida…`). Y en el segundo
  párrafo, reemplazar `con fuentes pulleables como datasets, imágenes, videos locales o
  archivos` por `con fuentes cuya lectura puede regularse —conjuntos de imágenes, videos
  locales o archivos—`.
- B16 · ELIMINAR la subsección **§17.3.7.4** ("Relación con configuración, modelos y
  prompts") completa, con dos rescates hacia §17.3.7.1:
  - Al final del bloque **Inferencia open-vocabulary**: «Cuando el modelo lo permita, el
    adaptador puede reutilizar representaciones textuales precalculadas o mecanismos
    equivalentes para reducir el costo de inferencia, siempre que esa optimización no altere
    la trazabilidad de la corrida.»
  - Como cierre de la subsección, tras **Publicación de evidencia perceptiva**: «En
    consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto,
    pero tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su
    producto es evidencia visual primaria, normalizada y trazable: la interpretación de esa
    evidencia corresponde al plano de control, y la comparación entre configuraciones,
    modelos y prompts, al análisis experimental posterior.»
- B17 · En la ex §17.3.7.5 ("Capacidades opcionales sin desplazar el núcleo validable", que
  pasa a ser 7.4): REEMPLAZAR el primer párrafo por:

  > El núcleo validable del plano de medios debe poder operar sin exigir seguimiento
  > multiobjeto formal, preselección en borde ni adaptación de modelos al dominio. Estas
  > capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en
  > requisitos para demostrar el procesamiento básico de CR-01 y CR-02, y su incorporación no
  > modifica el contrato de salida del plano de medios. La preselección en borde se adopta
  > además bajo un criterio de degradación segura, denominado fail-open: ante una falla o una
  > decisión incierta del preselector, la unidad visual se conserva para el flujo principal.
  > De ese modo la variante puede descartar carga, pero nunca convertirse en causa de pérdida
  > de evidencia.

  Además: ELIMINAR la última oración del párrafo de tracking (`La decisión de que una
  detección persistió durante una ventana temporal sigue perteneciendo al motor de
  patrones.`) y ELIMINAR el párrafo de cierre completo (`Con esta delimitación, el Pipeline
  de Medios queda definido…`).

### §17.3.8

- B18 · Identificadores versionados y anglicismos (regla general: el identificador de esquema
  no aparece en §17.3; se usa la denominación conceptual). Aplicar este mapa en TODO §17.3
  (prosa y celdas):
  | Aparece | Se reemplaza por |
  |---|---|
  | `media.detection.v1` | el evento de percepción (o «el contrato de percepción») |
  | `control.pattern_state.v1` | el evento de transición de patrón |
  | `control.alert.v1` | la alerta interna |
  | `control.notification.v1` | el sobre de notificación |
  | `control.delivery.v1` | el registro de entrega |
  | `bus.envelope.v1` | el envoltorio versionado del bus |
  | `run.lifecycle.v1` / `run_finished` | el contrato de ciclo de vida / el evento de finalización |
  | `clip_gt.v2` | la referencia temporal de evaluación |
  | `experiment.manifest.v1` | el manifiesto de experimento |
  | `PUB/SUB` | publicador-suscriptor |
  | `outcome` / `outcomes` | resultado de entrega / resultados de entrega |
  | `backpressure` | acumulación de atraso |
  | `keep-up` | capacidad de sostener el ritmo |
  | `letterbox` | relleno de bordes |
  | `config-driven` | gobernado por configuración |
  | `frescura` | actualidad (de la unidad visual) |
  | `fuente viva` / `fuentes vivas` / `corrida viva` | fuente en vivo / fuentes en vivo / corrida en vivo |
  | `opt-in` | opcional (o «estado de habilitación» en la celda de la Tabla 57) |
  NO tocar: `fail-open` (queda glosado una sola vez, en B17), `scene`/`subject` (literales de
  configuración), `checkpoint`, `ledger`, `frame`, `buffer`, `tracker`, `streaming`,
  `snapshot`, `jitter`, ni los nombres de campo (`experiment_id`, `unit_id`, `source_id`,
  `track_id`, `detection_id`, `prompt_set_id`, `clip_id`). Los nombres de estados
  (`inactive`…`resolved`) se quedan.
- B19a · En §17.3.8.3.1, tabla de componentes de una definición de patrón: ELIMINAR la
  tercera columna («Función en el motor») — quedó circular tras el pase 1: repite el nombre
  de la fila con otras palabras. La tabla resultante tiene dos columnas
  (`Componente | Contenido esperado`), así que PASARLA A VIÑETAS con el componente en
  negrita al inicio de cada ítem. Su Nota se conserva sin cambios (remite a §17.4.6 por los
  valores).
- B19 · En §17.3.8.3.1: ELIMINAR el tercer párrafo (`El motor opera sobre patrones de riesgo
  configurados…`) e INTEGRAR el fragmento pegado (`…y qué evento debe emitirse cuando cambia
  de estado. La codificación PR-01 a PR-06…`) como cierre del segundo párrafo, sin markdown.
- B20 · En §17.3.8.3.4: REEMPLAZAR el tercer párrafo (`Las métricas operativas del plano de
  control se apoyan en estas transiciones. El tiempo hasta la primera detección se vincula…`)
  por el fragmento ya pegado que usa las siglas (TTFD, t_alert-system, SDR), integrado.

### §17.3.9

- B21 · En §17.3.9.1, REEMPLAZAR el tercer párrafo (`El plano de control evalúa esa evidencia
  mediante el patrón de riesgo correspondiente. Allí se aplican criterios…`) por:

  > El plano de control evalúa esa evidencia mediante el patrón correspondiente y, cuando la
  > evaluación confirma el episodio, registra una alerta interna. Esa alerta es una salida
  > asistiva del sistema: no equivale a una notificación externa ni a una certificación
  > normativa.

- B22 · REEMPLAZAR §17.3.9.2 completa (los cuatro párrafos) por estos dos:

  > Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de
  > ausencia (E-IND). La frontera que esa elección fija es explícita: el plano de medios
  > informa qué entidades observó, dónde y con qué confianza; el plano de control decide si
  > la evidencia del elemento de protección se asocia al sujeto, construye el estado
  > evaluable de la condición y lo estabiliza antes de registrar una alerta.
  >
  > La estrategia se adopta por auditabilidad: cada evaluación puede reconstruirse a partir
  > de la caja del sujeto, la región analizada, las detecciones de protección, los umbrales y
  > la regla aplicada, de modo que la ausencia no se presenta como una conclusión opaca del
  > modelo. La detección directa (E-DIR) y las variantes híbridas (E-HYB) se conservan como
  > ramas comparativas configurables, con conjuntos de prompts y reglas identificados por
  > separado; comparten los contratos de publicación, evaluación temporal y registro, de modo
  > que la comparación no requiera alterar la arquitectura central.

- B23 · §17.3.9.3: RETITULAR a **"Comparabilidad entre estrategias"** y REEMPLAZAR su cuerpo
  por el fragmento ya pegado al final de §17.3.9 (`"Para que la comparación entre variantes
  sea posible…"`), integrado sin markdown.

### §17.3.10

- B24 · AGREGAR un párrafo de entrada a §17.3.10, antes de la 10.1: «La alerta interna es el
  hecho terminal del plano de control, pero todavía no es un aviso. Esta sección define el
  tramo que la convierte en entregas observables sin incorporar la comunicación a la ruta que
  la produjo.» — y en §17.3.10.1 REEMPLAZAR el primer párrafo (`La cadena descrita hasta aquí
  termina en un hecho interno… Falta el último tramo…`) por el fragmento ya pegado
  (`"La función arquitectónica de la distribución es transformar una alerta ya confirmada…"`),
  integrado.

- B24b · REEMPLAZAR el cuerpo completo de **§17.3.10.3** («Política, medición y límites de
  interpretación») por estos cuatro párrafos:

  > El conjunto de patrones adoptado no suprime confirmaciones: cada alerta interna se
  > registra para conservar la dinámica real del episodio. La decisión es deliberada —el
  > motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja
  > inactivo— porque un motor que suprimiera dejaría de reflejar la duración del episodio y
  > no permitiría distinguir una condición que persiste de una que se resolvió.
  >
  > La supresión de re-notificación se reubica en la política del módulo de distribución, y
  > al reubicarse cambia de granularidad: el motor la aplicaría por patrón y sujeto, mientras
  > que la política de entrega aplica una ventana de silencio por condición y fuente, porque
  > para una notificación asistiva lo relevante es que esa condición en esa cámara ya fue
  > avisada. La agrupación de avisos y la limitación de tasa quedan como punto de extensión
  > de la política. Una alerta suprimida para comunicación existió y continúa siendo medible:
  > las re-alertas de un episodio activo se informan por separado y no se computan como
  > falsos positivos, de modo que una decisión de comunicación no altera la precisión del
  > motor.
  >
  > El ledger de entregas aplica una clave de idempotencia por notificación y canal, es de
  > sólo agregado y acumula entre corridas: al reutilizar un directorio de salida la
  > generación anterior se archiva íntegra y la deduplicación considera todas las
  > generaciones, por lo que un reprocesamiento no vuelve a entregar lo ya entregado. Cada
  > fila conserva número de intento, marca temporal, resultado, motivo de error y
  > confirmación del canal, y distingue cinco resultados: entrega exitosa, supresión por
  > política, descarte por duplicado, falla de un intento y descarte definitivo por
  > agotamiento de reintentos. La unidad de conteo del tramo es la notificación y no la fila:
  > una notificación no entregada deja una fila por cada intento más la del descarte
  > definitivo.
  >
  > Cada fila registra además la modalidad en que se midió t_alert-notification, y la
  > latencia del tramo se informa siempre separada por modalidad: en relectura diferida el
  > intervalo incorpora el ritmo de reinyección de las alertas persistidas, que es propiedad
  > del reprocesamiento y no del canal.

### §17.3.11

- B25 · REEMPLAZAR el párrafo introductorio de §17.3.11 por:

  > Los contratos estabilizan la semántica de intercambio entre componentes: definen qué
  > información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del
  > núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e
  > interfaces concretas, y cada uno queda asociado a una corrida para que productores y
  > consumidores puedan evolucionar de forma independiente. La versión viaja dentro del
  > payload y no en el envoltorio de transporte: el canal puede cambiar sin que el hecho
  > persistido pierda la identificación de su esquema. Las capacidades futuras deben
  > evolucionar de forma aditiva sin romper la lectura de corridas históricas.

  Después: ELIMINAR la subsección **§17.3.11.1** completa · ELIMINAR la **Tabla 49** con su
  oración introductoria (la 11.2 conserva solo su prosa restante) · en §17.3.11.3, quitar los
  identificadores de la columna "Información mínima" de la **Tabla 50** (cada celda empieza
  directamente con los campos; los identificadores viven en §17.4) · en §17.3.11.4, ELIMINAR
  la **Tabla 51** con su Nota e INTEGRAR como párrafo el fragmento ya pegado (`"La superficie
  de crecimiento del evento de percepción se mantiene acotada…"`).

### §17.3.14 a §17.3.18

- B26 · §17.3.14.2: retitular a **"EBE como escenario de fuente en vivo controlada"** (el
  mapa de B18 cubre el cuerpo). §17.3.14.5: reescribir la segunda oración del párrafo del rol
  EN como: «La variante de preselección liviana en el borde es opcional, está deshabilitada
  por defecto y opera con el criterio de degradación segura fijado para las capacidades
  opcionales del plano de medios: una falla o incertidumbre del preselector no elimina la
  unidad del flujo principal.»
- B27 · §17.3.15: REEMPLAZAR el primer párrafo (`CPN, EN y TN son roles funcionales y no
  equivalen…`) por el fragmento movido desde §17.3.2 (B5): «Esta sección no redefine los
  roles funcionales ya establecidos en la consolidación metodológica: fija la topología de
  referencia con la que se materializan en el prototipo y ubica en ella al módulo de
  distribución. La única precisión que el diseño agrega es que ninguno de los tres roles
  equivale necesariamente a una máquina dedicada.»
- B28 · §17.3.17: ELIMINAR la **Tabla 61** completa (el párrafo de extensibilidad que la
  sigue se conserva).
- B29 · §17.3.18: ELIMINAR la **Tabla 62** con su Nota, e INTEGRAR como párrafo final el
  fragmento ya pegado (`"El diseño se considera completo cuando…"`).

---

## PARTE C — §17.4 (v1.3 → v1.4), en orden del documento

- C1 · §17.4.1, Nota de la figura: `buses ZeroMQ PUB/SUB con serialización msgpack` →
  `buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack`.
- C2 · §17.4.2, Tabla de correspondencia: INSERTAR la fila **Cierre de corrida** después de
  la fila "Bus interno de eventos": `Cierre de corrida | Evento de finalización publicado al
  cerrar la corrida | run.lifecycle.v1 (evento run_finished) | Plano de medios`. El contenido
  ya está pegado como párrafo suelto con `||` en §17.4.5: integralo acá y ELIMINÁ ese párrafo.
- C3 · §17.4.3: ELIMINAR los tres párrafos viejos completos (desde `Cinco contratos
  concentran los hechos principales de la ejecución. El evento de percepción,
  media.detection.v1, normaliza…` hasta `…inferencia reconstruible del plano de control sobre
  evidencia positiva.`). Los cuatro párrafos nuevos ya pegados (que empiezan `"Cinco
  contratos concentran los hechos principales de la ejecución: el evento de percepción, el
  envoltorio del bus…`) SE INTEGRAN como el cuerpo de la sección, sin comillas ni asteriscos.
  El fragmento de la referencia temporal (`"…materializada mediante el esquema clip_gt.v2,
  segunda versión…"`) NO va acá: MOVERLO a §17.4.8 (C8).
- C4 · §17.4.4 (la unidad más incumplida — rehacer entera):
  - INSERTAR en la tabla de interfaces, tras `POST /api/runs` del plano de medios, la fila:
    `Plano de medios (:8080) | POST /api/runs/{id}/stop | Detiene cooperativamente la corrida
    en curso; el cierre se propaga a los consumidores por el bus.`
  - Celda de `GET /api/runs/{id}` de distribución → «Consulta estado y conteos de entrega;
    determina cuándo consolidar artefactos.»
  - Celda de `POST /api/runs/{id}/cancel` → «Detiene cooperativamente una corrida de entrega
    en curso.»
  - Fila del canal de detecciones: operación `ZeroMQ PUB/SUB + msgpack` → **«Bus ZeroMQ
    publicador-suscriptor (msgpack)»**, función → «Transporta los eventos de percepción y el
    ciclo de vida de la corrida dentro del envoltorio versionado del bus.»
  - Fila del canal de alertas: operación ídem, función → «Transporta las alertas internas
    confirmadas hacia el módulo de distribución.»
  - REEMPLAZAR la Nota de la tabla por: «La tabla resume las operaciones de gobierno
    principales; no es un inventario exhaustivo (listados, corrida actual, artefactos por
    corrida, comprobaciones de salud y limpieza del registro se omiten). La detención figura
    únicamente donde el servicio la expone: el plano de control no ofrece detención de una
    corrida en curso, y esa asimetría es deliberada (ver el texto).»
  - ELIMINAR la oración `En una corrida live, la respuesta afirmativa del plano de control
    implica que su consumidor ya está suscripto.` y MOVER acá, como cierre de la sección, los
    tres párrafos que quedaron pegados en §17.4.8 (`Los tres servicios implementan el mismo
    contrato de gobierno…` · `En una corrida en vivo, la respuesta afirmativa de cada
    consumidor…` · `La detención de corridas es cooperativa…`).
- C5 · §17.4.5: ELIMINAR la tabla **"Patrones técnicos de acople implementados"** completa
  con su Nota (la prosa de la sección se conserva). En la prosa: `dentro de bus.envelope.v1;
  la relación… y el cierre se comunica mediante run_finished` → «dentro del envoltorio
  versionado del bus; la relación entre una corrida de medios y una de control es uno a uno y
  el cierre se comunica mediante el evento de finalización del contrato de ciclo de vida».
- C6 · §17.4.6: RETITULAR a **"Configuración efectiva y catálogo de modelos"** y aplicar la
  unidad E4-26 del pase 2 (está en tu knowledge): reescribir el tercer párrafo con su
  estructura de tres partes — (1) el catálogo entero como materialización de la
  sustituibilidad, con MM-Grounding DINO como familia integrada, evaluada y archivada;
  (2) «el núcleo no fija un único modelo»: comparar perfiles = desplegar instancias con
  perfiles distintos bajo la misma configuración; (3) los valores efectivos del perfil
  operativo (umbral de caja 0,30, texto 0,25, postproceso, ritmo) como ejemplo de
  configuración persistida y auditable, con la selección enunciada como decisión operativa
  pre-registrada por campaña.
- C7 · §17.4.7: en el árbol de artefactos, INSERTAR entre `control/` y `report/` la línea:
  `distribution/  notifications.jsonl · distribution_summary.json · dead_letter.jsonl
  (cuando la corrida habilita el tramo de distribución)`. REEMPLAZAR la celda de artefactos
  de la fila **Distribución** de la tabla de artefactos por: «notifications.jsonl (ledger de
  intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json» y su
  celda de función por: «Relaciona cada intento y resultado de entrega con la alerta interna
  original sin reescribirla, y conserva por separado los descartes definitivos por
  agotamiento de reintentos.» REEMPLAZAR la oración `Cuando el tramo de distribución está
  habilitado, su ledger y su reporte se consolidan del mismo modo.` por: «La ejecución
  experimental consolida así los cuatro componentes bajo una misma clave. La modularidad de
  la plataforma se expresa en que un tramo pueda no estar habilitado, no en que su evidencia
  se consolide de otro modo cuando lo está.» ELIMINAR el fragmento suelto con `||` que
  duplica la celda.
- C8 · §17.4.8: quitar los tres párrafos movidos a §17.4.4 (C4). En el primer párrafo,
  extender `…materializada mediante el esquema clip_gt.v2.` a: «…materializada mediante el
  esquema clip_gt.v2, segunda versión de la referencia: la primera generación registraba
  alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición
  con tiempos en milisegundos, junto con estados de aplicabilidad por clip.» (el fragmento ya
  pegado en §17.4.3 es este texto). El `[[PENDIENTE]]` de §17.4.8.1 NO SE TOCA.
- C9 · §17.4.9: ELIMINAR la columna **Estado** de la tabla de verificación (todas las filas
  dicen "Verificada": no discrimina nada).
- C10 · §17.4.10, tabla de capacidades:
  - REEMPLAZAR la celda de estado de la fila de ajuste fino (la que dice `…El tramo
    exploratorio adicional fue enviado y permanece en cola, sin haber iniciado.`) por:
    «Protocolo, procedencia, servicio de inferencia, evaluación y línea base quedaron
    congelados, y la escalera de tramos pre-registrada se ejecutó completa. Los dos tramos
    entrenados se evaluaron una única vez contra el banco congelado y ninguno superó los
    criterios de incorporación, firmados antes de que existiera el checkpoint que se les
    aplicaría. El tercer tramo se cerró con causa técnica: el único corpus disponible de ese
    volumen comparte fuentes con el banco de evaluación y deriva la clase de cabeza
    descubierta de una forma que el vocabulario canónico vigente no admite.»
  - REEMPLAZAR su celda de consecuencia (la que contiene `[[PENDIENTE: resultado y veredicto
    del tramo exploratorio…]]`) por el fragmento ya pegado que empieza `"Ningún checkpoint se
    incorporó como modelo de servicio…"`, integrado.
  - INSERTAR después de la fila "Condiciones de riesgo de nivel 2 y 3" la fila de
    **Preselección liviana en el rol de captura**, integrando el fragmento pegado con `||`
    (estado y consecuencia como dos celdas, sin `||` ni asteriscos).
  - En la Nota de la tabla, ELIMINAR la oración sobre el marcador del tramo exploratorio
    (`El marcador del tramo exploratorio adicional permanece visible hasta…`).

- C11 · §17.4.11: en la tabla de puntos de extensión, la celda «Evolución aditiva sin
  ruptura de media.detection.v1» → «Evolución aditiva sin ruptura del contrato de
  percepción»; y en la prosa, «ni romper media.detection.v1» → «ni romper el contrato de
  percepción». (El identificador queda declarado una sola vez, en la tabla de
  correspondencia de §17.4.2.)

---

## PARTE D — Renumeración (después de B y C, nunca antes)

- D1 · Subsecciones de §17.3: §17.3.6 queda con 6.1–6.5 · la ex 7.5 pasa a **7.4** · la ex
  11.2 pasa a **11.1**, la 11.3 a **11.2**, la 11.4 a **11.3**. Buscar en TODO el documento
  las cadenas `17.3.6.6`, `17.3.6.7`, `17.3.7.5`, `17.3.11.4` y corregir las referencias que
  queden.
- D2 · Tablas — renumerar con este mapa exacto y actualizar TODA mención «Tabla NN» en prosa
  y en Notas (✎ mapa corregido tras verificar la v1.3 de §17.3: la ex Tabla 46 pasó a
  viñetas, así que §17.3 queda con 17 tablas, no 18):
  - §17.3 (queda con 17, Tablas 39–55): 41→39 · 42→40 · 43→41 · 44→42 · 45→43 · 47→44 ·
    48→45 · 50→46 · 52→47 · 53→48 · 54→49 · 55→50 · 56→51 · 57→52 · 58→53 · 59→54 · 60→55.
  - §17.4 (queda con 6, Tablas 56–61): 63→56 · 64→57 · 66→58 · 67→59 · 68→60 · 69→61.
  - §17.5 arranca en la **Tabla 62**.
- D3 · Verificar que ninguna referencia numérica quede apuntando a una tabla eliminada
  (las ex 39, 40, 46, 49, 51, 61, 62 de §17.3 y la ex 65 de §17.4).
- D4 · En §17.3.8.2, la oración «Los componentes de una definición de patrón… se presentan a
  continuación» → «…se presentan al describir el motor de evaluación (sección 17.3.8.3.1)»
  — las viñetas viven dos subsecciones más adelante, no inmediatamente después.

---

## PARTE E — §17.5 (v1.0 → v1.1): estructura + desarrollo con las cifras dadas

### E-1 · Arreglos estructurales

1. El título de la sección es **«17.5. Evaluación y validación del prototipo»** (no
   «Resultados»).
2. ELIMINAR el título `17.5.1. D.0 — La organización de la sección` y todo el esquema pegado
   (la lista 1–8 y el párrafo «Reparto con las secciones vecinas»): era una guía de trabajo,
   no contenido. CONSERVAR el párrafo del banco (47 clips = 32 + 15, 37 episodios), que pasa
   al bloque de encuadre.
3. En el párrafo introductorio, `la interpretación que corresponde a la sección de discusión`
   → «la interpretación que corresponde a las conclusiones».
4. Reestructurar las subsecciones a estos ocho bloques (en este orden):
   **17.5.1 Encuadre y reglas de lectura** (absorbe los dos párrafos introductorios actuales
   y el del banco) · **17.5.2 Percepción sobre imágenes** · **17.5.3 Estado por persona** ·
   **17.5.4 Alerta por episodio contra la referencia temporal humana** (absorbe el actual
   «Comportamiento sobre material negativo»: los negativos, la tasa de falsas alarmas y el
   estrato de obra real viven acá) · **17.5.5 Tiempo real** (incluye la latencia de
   distribución) · **17.5.6 Caminos probados y no adoptados** · **17.5.7 Lo no ejecutado y lo
   no implementado, con su justificación** · **17.5.8 Síntesis de la sección**.
5. Ningún título de subsección lleva nombre de campaña. Los nombres de campaña no aparecen en
   el texto (la procedencia se expresa como «la campaña de comparación de modelos», «la
   campaña de granularidad», etc.).

### E-2 · Desarrollo por bloque — con estas cifras y SOLO estas

Reglas: toda cifra va con su material/estrato y denominador · decimales con coma · nunca
«el mejor modelo»: veredictos por combinación · lo no medido se declara, no se estima · si un
dato no está en esta lista, dejá `[[CIFRA: …]]` — no lo tomes de otro lado ni lo completes.

**17.5.2 Percepción sobre imágenes.** Banco congelado de 6.477 imágenes y 55.165
anotaciones, tres estratos independientes: obra curada (147), obra con mejor cobertura de
chaleco (1.330) y fuente con clase nativa de cabeza descubierta (5.000); el agregado está
dominado por este último (77 %) ⇒ siempre por estrato. Tabla (la primera de la sección):
gdino-tiny-560 — mAP50 agregado **0,551**, núcleo curado **0,503**, recall CR-01 0,308
(n = 5.313) · gdino-base-560 — 0,525 / 0,474 / **0,599** · yoloe-26x — 0,442 / 0,405 /
0,000. Lecturas: el perfil operativo gana mAP50 en las dos escalas (robusto a la fuente); el
base-560 es el especialista en cabeza descubierta y chaleco (AP 0,582 vs 0,520); la
asimetría es estructural — persona/casco sólidas (0,70–0,89 por estrato), chaleco débil
(0,55–0,58); la familia YOLOE es rápida pero ciega a la cabeza descubierta (AP 0,000 en las
cuatro variantes) ⇒ inservible para CR-01. Extensibilidad medida: una clase nueva costó
0 entrenamientos, un archivo de 48 líneas y 9 minutos, y dio AP@0.5 **0,662** zero-shot
(n = 99 cajas); contrapeso obligatorio: la palabra debe validarse contra el concepto visual
(un sinónimo dio 0 detecciones; otra palabra produjo 252 cajas y ninguna correcta).

**17.5.3 Estado por persona.** Sobre imágenes (calibración en mitad A, métricas en mitad B,
IoU ≥ 0,5): E-IND vs mejor E-DIR — CR-01: 0,546 vs 0,188 (n+ = 2.487, IC sin solaparse) y
0,408 vs 0,189 en el núcleo curado (n+ = 28); CR-02: 0,479 vs 0,418 (n+ = 82 — un solo
estrato: se declara como no cerrado). E-DIR no es detector sino recuperador: recupera el
18,5 % de lo que E-IND no ve (155/840) pagando precisión. Sobre video de obra real (17
clips, mismo criterio, sin motor temporal): CR-01 F1 **0,031** (P 0,016 · R 0,467; n+ = 92
de 10.356 person-frames) y CR-02 **0,018** (P 0,009 · R 0,318; n+ = 170 de 10.361): el
derrumbe respecto de imágenes es de precisión, no de recall — el sistema sigue viendo; lo
que no puede es dejar de afirmar sobre personas cuyo estado no es determinable. Regla
declarada del evaluador: las person-frames no juzgables salen del denominador (1.414 y
1.409 excluidas) pero la predicción sobre ellas cuenta como falso positivo.

**17.5.4 Alerta por episodio (el resultado principal).** Banco del rodaje: 34 clips, 35
episodios (28 CR-01 / 7 CR-02), **34 evaluables sobre 35** (1 censurado con causa);
referencia humana congelada. Tabla principal — seis combinaciones, mismo banco, variable
única por fila (recall · precisión · F1 · t_alert · SDR · FP en los 4 negativos):
núcleo E-IND escena 0,824 · 0,757 · **0,789** · 5.327 ms · 0,698 · 0/4 — contraste de
modelo (base-560) 0,735 · 0,676 · 0,704 · 4.899 ms · 0,819 · 0/4 — E-DIR de punta a punta
0,176 · **0,146** · 0,160 · 6.611 ms · 0,210 · 2/4 — fusión híbrida-o 0,353 · 0,255 ·
0,296 · 6.956 ms · 0,738 · 2/4 — **núcleo + granularidad por sujeto 0,971 · 0,892 ·
0,930 · 5.236 ms · 0,698 · 0/4** — vocabulario nativo de cabeza descubierta 0,382 · 0,371 ·
0,377 · 3.919 ms · 0,940 · 3/4. Los dos aportes medidos de la plataforma: la histéresis
rescata percepción intermitente (CR-02 confirma 7/7 = recall 1,000 con SDR 0,281, pagando
t_alert 8.572 vs 4.314 ms de CR-01) y la identidad es la capa que más agrega: +0,141 de F1
con las mismas detecciones bit a bit (el escenario más difícil pasa de 0,400 a 1,000).
Estrato de obra real no guionada (13 clips, fila aparte, jamás fusionada): una revisión
ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación —
sobre-declaración donde el estado no era observable —, resultado en sí sobre la frontera de
juzgabilidad; quedan 2 episodios evaluables ⇒ ningún ranking de granularidades sale de acá.
Lo robusto es la asimetría de falsos positivos: 26 (escena) contra 323 (sujeto) sobre los
11 negativos. Falsas alarmas con denominador a la vista: sobre 6:09,6 min de obra real sin
infracción, 3 FP en escena y 190 en sujeto; las tasas derivadas (29,2 y 1.850,8 FA/hora) se
reportan pero no sostienen una cota — la exposición disponible (0,1027 h) está dos órdenes
por debajo de la necesaria.

**17.5.5 Tiempo real.** El banco corre a 30 fps de evidencia; el camino en vivo entrega
1,16–4,42 fps. A la densidad del techo en vivo (≈4,29 fps): escena 0,794, sujeto 0,866; al
peor caso (≈1,15): 0,646 y 0,742. El hallazgo central: la ganancia de la identidad excluye
el cero en las cuatro densidades medidas (+0,141 / +0,072 / +0,137 / +0,096, remuestreo
pareado por clip) — única palanca del banco significativa bajo esa restricción. Dos
advertencias de instrumento: la cobertura del episodio no se compara entre cadencias, y la
latencia de alerta agregada no se compara entre densidades sin control de supervivencia (el
costo real entre supervivientes es +0,7 a +1,3 s sobre ventanas de 4–7 s). Integridad del
acople: paridad relectura↔transmisión byte-idéntica y cero eventos perdidos en las seis
corridas del rodaje. Latencia por tramos (los percentiles no se suman entre tramos): con
detector de referencia, del retiro de la unidad al resultado p50 14,7 ms / p95 31,8 ms
(dentro del presupuesto 50–250 ms); con el detector open-vocabulary evaluado en vivo, p95
630–890 ms (fuera — y el sistema lo declara); la medición arranca en el retiro de la unidad,
no en el fotón: la captura suma 202–217 ms medidos. Confirmaciones en vivo: CR-01 siete
legítimas (4,1–4,6 s sobre ventana de 4,0) y CR-02 tres (7,1 s+ sobre 7,0). Distribución:
del bus de alertas a la confirmación del canal, p95 **64,534 ms** (n = 460) y en régimen
sostenido p95 102,025 ms (n = 104); no se suma a la latencia de alerta del sistema.

**17.5.6 Caminos probados y no adoptados.** El criterio precede al resultado: la estrategia
directa quedó descartada por un veto de precisión pre-registrado (0,146 < 0,5) — su brecha
con la indirecta se agranda al pasar por la plataforma; la fusión híbrida-o fue ejecutada y
refutada: el recall se derrumba de 0,824 a 0,353 porque la unión de evidencia no es monótona
en un motor temporal (evidencia más temprana corre las alertas fuera de su ventana); la
variante híbrida-y no se ejecutó con causa declarada (no es medible contra este banco sin
romper la comparabilidad de las seis campañas); una familia de modelos adicional se integró,
se evaluó y se archivó durante la selección. La rama de ajuste fino cerró como curva de
capacidad de tres puntos, con márgenes y expectativas firmados antes de cada evaluación:
la línea base (AP50 de cabeza descubierta 0,000; recall CR-01 agregado 0,0002) · el primer
tramo rescata la clase del cero (0,0000 → 0,0455, a 0,0045 del umbral) multiplicando el
recall CR-01 (0,0002 → 0,2089), pero rompe la retención de persona (−11,62 %, tope 10 %) ·
el segundo tramo logra la ganancia (0,0909, el doble) pero colapsa en entrenamiento
(detención temprana 16/60, mejor época = 1) y falla las dos retenciones: dominio propio
−43,4 % de mAP50 protegido y vocabulario abierto −71,3 % (0,4347 → 0,1247). La lectura de la
curva: el límite es estructural — 2.946 imágenes de ajuste contra 10,35 millones de
parámetros —, no de capacidad; los tramos no ganan por la misma vía (el primero por recall,
el segundo por AP), ningún checkpoint se adoptó y el resultado es un veredicto negativo
pre-registrado, no un tramo pendiente.

**17.5.7 Lo no ejecutado y lo no implementado.** Condiciones de Nivel 2 y 3: sin verdad de
terreno del dominio ni evaluadores validables — incorporarlas habría producido capacidades
no medibles. Métricas de seguimiento multiobjeto: sin anotación de identidad no tienen
referencia; la capacidad de identidad sí está medida y su ganancia se expresa en alertas.
Preselección en el borde: implementada para la fuente de captura propia y medida (87 % de
unidades descartadas en el dispositivo, comparación pareada), pero deliberadamente
deshabilitada en todo lo evaluativo — un filtro de fotogramas sin persona suprimiría las
detecciones sostenidas que la tasa de falsas alarmas existe para medir. Cota operativa de
falsas alarmas: requiere ~3 h de material de cumplimiento anotado; la exposición disponible
es 0,1027 h. Comparación en vivo contra clip: sin un ancla común entre reloj de pared y
tiempo de medio, el emparejamiento temporal se declara no interpretable.

**17.5.8 Síntesis de la sección.** La detección sin entrenar sostiene una condición (CR-01)
y no la otra (CR-02) al nivel de percepción; la plataforma alrededor del modelo cambia el
resultado más que cualquier elección de modelo o formulación — de 0,789 a 0,930 con las
mismas detecciones — y esa ganancia sobrevive a la restricción del tiempo real. La tasa de
falsas alarmas en obra real no guionada es la limitación principal y se reporta sin cota.
Remitir a las limitaciones declaradas; la interpretación pertenece a las conclusiones.

---

## PARTE F — Verificación final (autoaplicá esto antes de entregar)

1. Buscar en los tres documentos: `||` · `SHA-256` · `**` · `E3-` · `E4-` · `D-P` · `T40` ·
   `pase` (como referencia a los pases) → **cero resultados**.
2. Buscar: `Tabla 39` · `Tabla 40` (como referencia viva) · `opt-in` · `frescura` ·
   `fuentes vivas` · `pulleable` · `PUB/SUB` · `outcome` · `backpressure` · `keep-up` ·
   `letterbox` · `config-driven` · `17.1.5.4.2` · `permanece en cola` → **cero resultados**.
3. En §17.3: `media.detection.v1`, `clip_gt.v2`, `bus.envelope.v1`, `run_finished`,
   `control.alert.v1` → **cero resultados** (viven solo en §17.4).
4. `fail-open` aparece **una sola vez glosado en prosa** (§17.3.7.4 nueva) más las celdas de
   las tablas de EBE, roles y riesgos — nunca más.
5. Conteo de tablas: §17.3 = 18 (Tablas 39–56) · §17.4 = 6 (Tablas 57–62). Ninguna referencia
   «Tabla NN» apunta a un número inexistente.
6. §17.4.8.1 conserva su `[[PENDIENTE: dirección de origen y fecha de acceso por clip…]]`.
7. §17.5: título «Evaluación y validación del prototipo»; ocho subsecciones; ningún nombre de
   campaña; toda cifra con denominador; los `[[CIFRA: …]]` solo donde esta guía no dio el
   dato.
8. Entregar los tres `.docx` con la plantilla intacta y cerrar con la lista de marcadores
   `[[…]]` que quedaron.
