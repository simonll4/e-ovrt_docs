# Prompt para GPT — reescritura de §17.3.3.2 «Capacidades arquitectónicas requeridas»

> Pegar todo lo que sigue a la línea de guiones como mensaje único en el Project.
> Requiere en el Project: `INSTRUCCIONES-PROJECT.md`, `01-etapa-3-activa.md`, el DOCX base
> y `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.4.docx`.

---

Necesito que produzcas **un `.docx` que contenga únicamente la subsección §17.3.3.2
«Capacidades arquitectónicas requeridas»**, completa y reescrita, sobre una copia del DOCX
base, para que el equipo la integre al maestro reemplazando la versión actual de esa
subsección en §17.3 v1.4.

## 0. Por qué se reescribe

La revisión de cierre encontró seis defectos en la Tabla 39 y en la prosa que la introduce.
Todos son internos al capítulo: la tabla omite dos capacidades que el propio §17.3 declara
opcionales, su leyenda define cinco clases pero la columna usa siete, cuatro filas no son
capacidades sino exclusiones o ítems de alcance, dos filas repiten casi literalmente la
Tabla 40, la fila de gobierno de corrida cubre la mitad de la decisión DA-03, y la tabla
nunca se menciona en el texto (incumple APA). El texto final ya está resuelto y te lo doy
completo abajo: **no tenés que decidir contenido, tenés que producir el documento.**

## 1. Reglas no negociables

1. **No agregues, quites ni reformules nada del texto que te doy en las secciones 3, 4 y 5.**
   Es texto final, verificado contra el resto del capítulo. Si algo te parece mejorable, no
   lo cambies: anotalo al final de tu respuesta como observación separada.
2. **El resultado es prosa y tabla de informe.** Nunca contiene asteriscos de markdown,
   comillas de cita, separadores `|` o `||`, negritas heredadas de markdown, encabezados con
   `#`, ni ninguna marca de este prompt. Las viñetas de este documento son andamiaje: no
   viajan al `.docx`.
3. **Reemplazo, no agregado.** El `.docx` que entregás contiene la versión nueva de la
   subsección y nada de la versión vieja. No dejes la tabla anterior, ni párrafos anteriores,
   ni filas anteriores conviviendo con las nuevas.
4. **La tabla sigue siendo la Tabla 39.** No la renumeres. No toques, copies ni renumeres la
   Tabla 40 ni la Tabla 41: no forman parte de este entregable.
5. **Autocontención.** En el texto no aparece ninguna referencia a documentación interna,
   ADRs, especificaciones, fichas, IDs de unidad, índices ni rutas. Sí se usan los
   identificadores que el informe define: CR-01, CR-02, DA-01…DA-13, los nombres de los
   escenarios DBE y EBE.
6. **No inventes.** No agregues capacidades, cifras, contratos, nombres de campo, puertos,
   tecnologías ni resultados. Esta subsección es conceptual: describe responsabilidades del
   diseño, no la implementación ni sus mediciones.
7. **es-AR**, y se conserva el registro del capítulo: tercera persona, sin condicionales
   sobre lo ya decidido, sin adjetivación valorativa.

## 2. Formato del `.docx`

- Copia del DOCX base, plantilla heredada literalmente: estilos y no formato manual, papel
  Carta, márgenes 2,54 cm, cuerpo 12 pt, interlineado doble, sangría inicial 1,27 cm,
  tipografía heredada.
- Encabezado de la subsección con el mismo estilo de nivel 4 que usa el documento actual,
  con el texto exacto: `17.3.3.2. Capacidades arquitectónicas requeridas`.
- **Tabla en formato APA 7, igual que el resto del capítulo**: número y título arriba —
  `Tabla 39` en negrita en su propia línea, y el título `Capacidades arquitectónicas y su
  tratamiento en el diseño` en itálica en la línea siguiente—; la tabla; y debajo la nota,
  que abre con `Nota.` y sigue en redonda.
- Tres columnas, con los encabezados exactos: **Capacidad requerida** · **Compromiso** ·
  **Lectura de diseño**. Encabezado de tabla marcado para repetirse si la tabla corta de
  página. Diecinueve filas de contenido, en el orden en que te las doy.
- No entregues el documento completo ni ninguna otra sección.

## 3. Prosa que precede a la tabla (dos párrafos, texto final)

Párrafo 1:

A partir del alcance definido, la arquitectura debe habilitar un conjunto mínimo de
capacidades que permitan desarrollar un prototipo experimental medible, trazable y
extensible. Estas capacidades no describen todavía componentes de implementación, sino
responsabilidades que el diseño debe contemplar para que el sistema pueda procesar fuentes
visuales, ejecutar inferencia open-vocabulary, evaluar patrones, registrar alertas,
distribuir avisos y producir evidencia experimental. La enumeración reúne únicamente
responsabilidades: los criterios de exclusión y las cualidades exigidas al diseño se tratan,
respectivamente, entre las decisiones arquitectónicas iniciales y los requisitos no
funcionales de referencia.

Párrafo 2:

La clasificación declara el régimen de cada capacidad mediante cinco compromisos —núcleo,
complementario previsto, capacidad opcional, extensión condicionada y rama comparativa
condicionada—, cuyo alcance se precisa en la nota de la tabla. Esta separación permite
ordenar el desarrollo sin convertir funcionalidades deseables en dependencias obligatorias
del flujo base y evita que una capacidad quede habilitada de manera implícita. La Tabla 39
resume las capacidades requeridas y el compromiso que el diseño asume con cada una.

## 4. Contenido de la Tabla 39 (diecinueve filas, texto final)

Cada bloque es una fila. La primera línea es la celda de «Capacidad requerida», la segunda la
de «Compromiso», la tercera la de «Lectura de diseño».

1. Gestión y gobierno de la corrida
   · Núcleo
   · Debe existir un punto explícito que declare y congele la configuración efectiva de cada
   ejecución y gobierne su ciclo de vida —creación, consulta, cancelación y cierre— con un
   orden de disparo definido cuando la corrida acopla varios módulos.

2. Operación sobre fuentes reproducibles
   · Núcleo
   · Debe operar sobre imágenes, datasets o videos locales, que admiten regular el ritmo de
   lectura, repetirse y detenerse sin alterar el contenido observado. Es el escenario donde se
   estabilizan inferencia, contratos, eventos y métricas antes de incorporar captura continua.

3. Operación sobre fuentes en vivo
   · Complementario previsto
   · Debe admitir captura o streaming en entorno controlado, donde la fuente continúa
   evolucionando aunque el procesamiento no alcance la cadencia de captura, para observar el
   comportamiento operativo del sistema.

4. Normalización de entrada visual
   · Núcleo
   · Cada frame debe representarse con metadatos de corrida, fuente, orden temporal,
   resolución y política de muestreo, de modo que ambos tipos de fuente compartan el pipeline
   sin ocultar su diferencia temporal.

5. Inferencia OVD configurable
   · Núcleo
   · La arquitectura debe integrar modelos de detección open-vocabulary mediante adaptadores,
   de modo que sustituir o comparar un modelo no obligue a rediseñar el resto de la cadena.

6. Gestión de prompts y vocabulario activo
   · Núcleo
   · Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y
   umbrales asociados.

7. Normalización de detecciones
   · Núcleo
   · La salida del plano de medios debe expresarse como un contrato de evento de percepción
   versionado, que constituya la única unidad de evidencia compartida por la interpretación de
   patrones, la persistencia y la relectura posterior.

8. Evaluación de patrones de Nivel 1
   · Núcleo
   · Las detecciones positivas deben asociarse espacialmente por sujeto, transformarse en un
   estado de ausencia evaluable y estabilizarse mediante persistencia temporal e histéresis.

9. Registro de alertas asistivas
   · Núcleo
   · Las alertas deben registrarse cuando un patrón alcanza estado confirmado, sin constituir
   un juicio normativo automático.

10. Publicación y persistencia de eventos
    · Núcleo
    · La publicación debe desacoplar la producción de evidencia perceptiva de sus consumidores
    sin bloquear la ruta crítica, y la persistencia debe conservar un historial de sólo adición
    que sobreviva a la corrida y permita releerla.

11. Observabilidad y métricas
    · Núcleo
    · La instrumentación debe formar parte del diseño del pipeline y no de una etapa
    posterior: cada tramo debe emitir sus propias mediciones, y ninguna medición debe
    reconstruirse a posteriori a partir de artefactos que no la registraron.

12. Reporte experimental
    · Núcleo
    · Cada corrida debe producir un artefacto de síntesis persistido que consolide su
    configuración, sus resultados y sus limitaciones, y que pueda leerse sin acceso al sistema
    en ejecución.

13. Inspección mínima de resultados
    · Núcleo
    · Debe existir una interfaz de revisión de corridas, alertas, métricas y evidencia
    asociada, acotada a la verificación experimental y sin convertirse en un tablero operativo.

14. Gestión de evidencia visual controlada
    · Complementario previsto
    · Debe admitir clips, snapshots o recortes justificados para validación, revisión técnica
    o comunicación académica.

15. Distribución de alertas confirmadas
    · Capacidad opcional
    · Debe transformar una alerta ya confirmada en intentos de entrega registrados, aguas
    abajo del registro interno y sin participar del razonamiento que la produjo, de modo que la
    indisponibilidad de un canal externo no se propague al motor de patrones.

16. Preselección liviana en el rol de captura
    · Capacidad opcional
    · Debe poder reducir la carga descartando unidades antes de la inferencia, bajo un
    criterio conservador de degradación segura que conserve la unidad en el flujo principal ante
    falla o incertidumbre del preselector, sin convertir el borde en fuente de verdad ni
    ocultar descartes.

17. Identidad temporal de sujeto
    · Capacidad opcional
    · La arquitectura admite granularidad por sujeto mediante una identidad temporal válida.
    Las métricas formales de seguimiento multiobjeto no condicionan la evaluación del núcleo y
    no deben confundirse con la capacidad de mantener identidad.

18. Capacidades contextuales y relacionales
    · Extensión condicionada
    · Habilitan las condiciones de riesgo de Nivel 2 y Nivel 3, que exigen contexto,
    razonamiento espacial, zonas, proximidad o relaciones entre entidades. Zonas y evaluadores
    relacionales quedan previstos sin bloquear CR-01 y CR-02; su habilitación requiere evidencia
    e instrumentación adecuadas.

19. Adaptación al dominio (fine-tuning)
    · Rama comparativa condicionada
    · Sólo corresponde bajo una línea base preentrenada congelada, datos suficientes,
    partición disjunta y criterios de escalamiento definidos con anterioridad a los resultados.

## 5. Nota de la tabla (texto final)

Nota. El compromiso declara el régimen de cada capacidad. “Núcleo” identifica capacidades
necesarias para el flujo base; “complementario previsto” agrupa capacidades útiles para la
validación, la revisión técnica o la comunicación académica; “capacidad opcional” identifica
capacidades que el diseño contempla pero que se declaran en la configuración de cada corrida y
permanecen deshabilitadas por defecto, de modo que ninguna pueda operar como comportamiento
implícito; “extensión condicionada” identifica capacidades previstas cuya habilitación exige
evidencia e instrumentación adicionales; y “rama comparativa condicionada” refiere a variantes
que sólo deben incorporarse si se cumplen las condiciones metodológicas correspondientes. La
tabla enumera responsabilidades del diseño y no componentes de implementación.

## 6. Qué cambió respecto de la versión actual (para que verifiques, no para el documento)

- **Dos filas nuevas**: «Distribución de alertas confirmadas» y «Preselección liviana en el rol
  de captura». Ambas capacidades ya estaban tratadas en el capítulo —tienen decisión propia y
  subsección propia— pero faltaban en la tabla, que por eso no era el inventario que declara
  ser.
- **Una fila eliminada**: «Video crudo continuo». Es una exclusión, no una capacidad, y su
  contenido ya está dicho en la fila de evidencia visual controlada, en DA-08, en DA-09 y en la
  Tabla 40.
- **Una fila fusionada**: «Condiciones de riesgo de Nivel 2 y Nivel 3» se absorbe en
  «Capacidades contextuales y relacionales», que es la capacidad que esas condiciones requieren.
- **Dos filas renombradas**: «Procesamiento DBE» y «Procesamiento EBE» pasan a nombrar la
  capacidad —operación sobre fuentes reproducibles y sobre fuentes en vivo— porque el propio
  §17.3.3.4 establece que DBE y EBE son escenarios experimentales y no capacidades. Con ese
  cambio, la operación sobre fuentes reproducibles pasa a «Núcleo» y desaparece la clase «núcleo
  de evaluación», que tenía un único miembro.
- **La columna Compromiso queda cerrada en las cinco clases que la nota define.** Desaparecen
  los dos valores que no estaban definidos: «Fuera del comportamiento ordinario» y «Capacidad
  opcional; métricas fuera del núcleo». El segundo se convierte en «Capacidad opcional»; la
  exclusión de las métricas de seguimiento multiobjeto se conserva íntegra en la lectura de
  diseño de esa misma fila, porque lo excluido son las métricas y no la capacidad de asociar
  sujetos.
- **Tres lecturas de diseño reescritas para que no se deriven entre sí**: inferencia OVD
  configurable argumenta desde el adaptador, normalización de detecciones desde el contrato de
  evento de percepción, y gestión de la corrida incorpora el gobierno de ciclo de vida y el
  orden de disparo, que son la mitad de DA-03 y no estaban en ninguna fila.
- **Desduplicación contra la Tabla 40**: las filas de gestión de la corrida y de observabilidad
  ya no repiten la enumeración que la Tabla 40 vuelve a dar doce líneas después. Ahora enuncian
  la obligación funcional, y la Tabla 40 enuncia la cualidad.
- **La tabla se menciona en el texto**, como exige APA y como no ocurría antes.
- Total: diecinueve filas antes, diecinueve después.

## 7. Control final antes de entregar

Verificá y confirmá punto por punto en tu respuesta:

1. El `.docx` contiene sólo §17.3.3.2: un encabezado, dos párrafos, la Tabla 39 con su título
   y su nota. Nada más.
2. Diecinueve filas de contenido, en el orden dado, con el texto exacto de la sección 4.
3. La columna Compromiso usa exclusivamente los cinco valores que la nota define, y los cinco
   aparecen al menos una vez.
4. No quedó ninguna fila de la versión anterior, en particular «Video crudo continuo»,
   «Condiciones de riesgo de Nivel 2 y Nivel 3», «Procesamiento DBE» ni «Procesamiento EBE».
5. No hay asteriscos, `|`, `||`, `#`, comillas de cita, viñetas de andamiaje ni texto de este
   prompt en el documento.
6. La tabla se llama Tabla 39 y no se renumeró nada.
7. No aparecen referencias a documentación interna, rutas, IDs de unidad ni nombres de
   campaña; tampoco tecnologías, puertos, cifras ni nombres de campo.
8. Estilos heredados de la plantilla, encabezado de tabla configurado para repetirse en corte
   de página, y ningún marcador `[[…]]` nuevo.

Si algo del texto que te di entra en conflicto con la plantilla o con el resto del capítulo,
**no lo resuelvas por tu cuenta**: entregá el documento con el texto tal como está y planteá el
conflicto al final de tu respuesta.
