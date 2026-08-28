# Prompt para GPT — desarrollo de §17.4.3 (17.4 v1.5 → v1.6)

> Pegar todo lo que sigue a la línea de guiones como mensaje único en el Project, junto con
> el `.docx` `E-OVRT-VDP_Seccion_17.4_Implementacion_v1.5.docx`.

---

Necesito una pasada de desarrollo sobre **una sola subsección** del documento adjunto: **§17.4.3.
Contratos de datos materializados**. El resto del documento no se toca.

El motivo es una devolución del tutor sobre esta fase del informe. Su observación textual: *«se
definen contratos y módulos pero no siempre se evidencia cómo se implementan concretamente
(clases, APIs, servicios)»*, y sobre esta sección en particular: *«se definen entidades clave del
sistema, pero explícitamente dicen que no son clases, no son APIs, no tienen formato, no tienen
implementación. No espero un detalle extremo, pero sí algo como un DTO, una API o simplemente una
clase»*. Agregó un pedido específico: *«es muy importante ser muy claro en la definición de
eventos tipo inferencias para que den soporte a datos que a lo mejor hoy no están, pero mañana sí,
por ejemplo: agregar a las detecciones detecciones asociadas, datos de tracking, velocidad,
dirección, eventualmente pose o segmentación»*.

De las tres patas del comentario, la de las interfaces ya está cubierta: la Tabla 57 de §17.4.4
lista las operaciones con verbo y puerto. **Esta pasada cubre las otras dos: la forma concreta de
los contratos y el mecanismo de extensión del evento de percepción.** §17.4.3 pasa de cuatro
párrafos a ocho párrafos y dos bloques monoespaciados.

## 0. Alcance de esta pasada

1. **Editás el `.docx` v1.5 adjunto y devolvés v1.6.** No lo regeneres desde cero.
2. **Cambia el cuerpo de §17.4.3 completo** (los cuatro párrafos actuales se reemplazan por lo
   que doy en la sección 2) **y una sola celda de la Tabla 56** (sección 3). Nada más.
3. **El encabezado `17.4.3. Contratos de datos materializados` no cambia** ni en texto ni en
   formato.
4. **No se agrega ninguna tabla y no se renumera nada.** El documento sigue teniendo la Figura
   4.7 y las Tablas 56 a 61, con los mismos números y en el mismo orden. Si en algún momento te
   parece que este material «pide una tabla», no la hagas: la decisión de redacción es prosa más
   bloques monoespaciados, deliberadamente.
5. **Los dos bloques monoespaciados van sin numerar, sin título y sin nota**, exactamente igual
   que el árbol de artefactos que ya existe en §17.4.7. No son figuras. No llevan la etiqueta
   «Figura», ni epígrafe, ni «Nota.».
6. **No toques §17.4.11.** Esa subsección ya declara el *costo* de cada extensión; §17.4.3 declara
   el *mecanismo*. La referencia cruzada del último párrafo evita que se lean como repetición. No
   muevas material de una a la otra ni agregues nada allá.
7. El texto que doy en la sección 2 va **literal**. No lo parafrasees, no lo acortes, no lo
   reordenes, no le agregues conectores ni le cambies el vocabulario técnico.
8. Regla de autocontención del informe, vigente: **el texto no referencia documentos locales,
   decisiones de arquitectura numeradas, fichas, especificaciones internas ni rutas del
   repositorio.** Las únicas referencias admitidas son a secciones del propio informe
   (`sección 17.3`, `sección 17.4.11`, `sección 17.5`) y la etiqueta `DA-13`, que ya se usa en
   §17.4.6. No agregues ninguna otra.
9. El resultado no contiene asteriscos de énfasis, `|` de tabla markdown, `#` de título markdown,
   viñetas, comillas de cita ni ningún fragmento de este prompt **en el cuerpo del texto**.
   Atención: esta prohibición **no se aplica dentro de los dos bloques monoespaciados**, donde
   `{`, `}`, `"`, `:`, `#`, `|` y `[` son sintaxis y tienen que quedar tal cual (ver sección 4).

## 1. Por qué se cambia, para que no lo «arregles» de vuelta

Tres de los cambios corrigen afirmaciones del texto actual que son inexactas contra la
implementación. Si al redactar te suenan más ásperas que la versión anterior, es porque son más
precisas. **No las suavices.**

1. **El contrato de ciclo de vida no delimita el inicio de la corrida.** El texto actual dice que
   «delimita el inicio y el cierre». La implementación publica un único evento de finalización;
   el inicio queda establecido por la respuesta afirmativa de la operación de creación en el
   servicio. Además, el texto actual se contradice con su propia Tabla 56, que ya dice «Cierre de
   corrida … (evento `run_finished`)».
2. **El identificador determinista necesita su derivación.** «Reprocesar la misma corrida produce
   la misma identidad» es cierto sólo bajo una condición que el texto no declara. La versión
   nueva da la fórmula y las tres consecuencias, incluida la que el texto actual omite: la
   identidad se asigna por confirmación y no por episodio.
3. **El envoltorio y el ciclo de vida se usan en los dos buses**, no sólo en la frontera entre
   planos. Decirlo refuerza el argumento de §17.4.5 de que hay dos patrones de acople y no tres.
4. Los dos bloques monoespaciados son **evidencia real, no ilustraciones**: el objeto JSON es la
   primera línea del artefacto de detecciones de una corrida existente del repositorio, y la
   firma de clase es la declaración vigente del contrato. Por eso no se pueden «redondear», ni
   completar, ni embellecer.

## 2. Cuerpo nuevo de §17.4.3

Reemplazá los cuatro párrafos actuales de §17.4.3 por lo que sigue: **ocho párrafos y dos bloques
monoespaciados**, en este orden exacto.

### Párrafo 1

Cinco contratos concentran los hechos principales de la ejecución: el evento de percepción, el
envoltorio del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta
interna. Los cinco están declarados con su identificador en la tabla anterior; lo que sigue
precisa cómo se materializan, qué lleva cada uno y qué propiedad técnica habilita.

### Párrafo 2

La materialización no es una denominación conceptual. Cada contrato es una clase de modelo
declarada en el módulo de contratos de su componente, con tipos y campos obligatorios explícitos,
validada en la frontera de entrada, persistida como un objeto JSON por línea en los artefactos de
sólo adición —omitiendo los campos sin valor— y transportada por el bus dentro de un envoltorio
serializado en formato binario compacto. Dentro del plano de medios la evidencia atraviesa además
una cadena interna de contratos antes de publicarse: la unidad visual normaliza la lectura de la
fuente, la unidad preparada transporta los píxeles junto con la transformación espacial que
permite volver del espacio del modelo al de la imagen original, la detección cruda recoge la
salida del adaptador y la detección normalizada es la que finalmente se persiste. Esa cadena es la
que hace que la reproyección de coordenadas sea una operación declarada y no un ajuste disperso en
el código.

### Párrafo 3

El evento de percepción, `DetectionEvent`, normaliza la salida del detector. Identifica la corrida
y la unidad visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto
de prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su
etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su
equivalente normalizado. Esa composición es la que permite que una detección se atribuya después a
una variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del
evento, tal como se persiste, es la siguiente:

### Bloque monoespaciado A

Va inmediatamente después del párrafo 3. Contenido exacto, respetando saltos de línea, sangrías,
comillas rectas y comas:

```
{
  "schema_version": "media.detection.v1",
  "event_type": "detection_event",
  "run_id": "run_20260805_033712_dbe_grounding_dino_53cb6f",
  "unit_id": "frame_000000",
  "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",
               "frame_index": 0, "timestamp_ms": 0.0,
               "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny",
               "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },
  "detections": [
    { "detection_id": "det_000001", "label": "person", "prompt_id": "person",
      "confidence": 0.8784,
      "bbox_xyxy": [1027.3, 105.5, 1340.8, 1083.9],
      "bbox_norm_xyxy": [0.5351, 0.0977, 0.6983, 1.0],
      "area_px": 306732.1, "model_name": "grounding_dino" },
    { "detection_id": "det_000002", "label": "helmet", "prompt_id": "helmet",
      "confidence": 0.8387,
      "bbox_xyxy": [1098.1, 106.5, 1255.8, 217.3],
      "bbox_norm_xyxy": [0.5719, 0.0986, 0.6541, 0.2012],
      "area_px": 17475.1, "model_name": "grounding_dino" }
  ],
  "timing": { "normalize_ms": 11.53, "inference_ms": 445.76,
              "postprocess_ms": 0.11, "write_ms": 0.0, "total_ms": 445.88 }
}
```

### Párrafo 4

El envoltorio del bus no reempaqueta ese contenido: transporta como carga la misma cadena que se
escribió en el artefacto —la persistencia ocurre primero y la publicación después— y le agrega
cuatro campos propios del transporte: el tópico, la clave de particionado, un número de secuencia
monótono por publicador y el instante de publicación en reloj de pared, que es el que el módulo de
distribución conserva luego como marca de confirmación. El número de secuencia se consume incluso
cuando el envío se descarta por saturación del canal, de modo que la pérdida se vuelva observable
como un hueco del lado del consumidor en lugar de pasar por ausencia de evidencia. El contrato de
ciclo de vida, por su parte, no delimita el inicio de la corrida —eso lo establece la respuesta
afirmativa de la operación de creación en el servicio— sino su cierre: publica un único evento de
finalización con el identificador de corrida y su estado, de modo que el final lógico se distinga
de una interrupción y los consumidores puedan cerrarse y consolidar sus artefactos. Ambos
contratos se emplean sin variantes en los dos buses de la plataforma, el de detecciones y el de
alertas: el publicador de alertas del plano de control es un espejo deliberado del publicador de
medios, con el mismo envoltorio y las mismas garantías.

### Párrafo 5

El evento de transición, `PatternStateChanged`, registra los cambios entre los estados del patrón
—los mismos que fija la máquina de estados del diseño— junto con la evidencia y los hitos
temporales que los motivaron, e incorpora el instante y la unidad de la primera evidencia positiva
del episodio, que es el punto de partida de la medición de latencia. Un contrato hermano registra
el progreso parcial mientras la condición está en curso y no ha sido confirmada todavía.

### Párrafo 6

La alerta interna, `AlertEvent`, registra la confirmación del episodio. Su identificador no es un
valor aleatorio: se deriva como un identificador único universal de versión 5 —un resumen
determinista— sobre la cadena que concatena el identificador de corrida de control, el de corrida
de medios, la unidad, el patrón y la clave de sujeto, donde esa clave adopta la forma
`CR-01:a_p1_c08` cuando el patrón opera con granularidad de escena y `CR-01:a_p1_c08:subject_001`
cuando opera con identidad de sujeto. La identidad de la alerta es entonces una función pura de
esa quíntupla, con tres consecuencias verificables. Primero, reprocesar la misma evidencia bajo el
mismo identificador de corrida de control reproduce exactamente los mismos identificadores de
alerta. Segundo, la deduplicación no requiere estado compartido entre componentes: el módulo de
distribución construye su clave de idempotencia como un resumen criptográfico del identificador de
alerta y la asienta en un registro de sólo agregado, sin consultar al plano de control. Tercero,
la identidad se asigna por confirmación y no por episodio, de modo que una confirmación posterior
sobre el mismo sujeto recibe identidad propia; esto es coherente con la decisión de no suprimir
dentro del motor (DA-13) y evita que el mecanismo de idempotencia oculte reincidencias reales. La
alerta conserva además evidencia auditable: sujeto observado, detecciones de soporte, clase de
protección ausente, región evaluada, puntaje y justificación legible. Por eso la ausencia no se
presenta como una afirmación opaca del detector, sino como una inferencia del plano de control
reconstruible sobre evidencia positiva.

### Párrafo 7

Los contratos se diseñaron para admitir información que la implementación actual no produce, y esa
capacidad fue ejercida antes de declararse. La detección normalizada incluye hoy un campo de
identidad de sujeto entre fotogramas que ningún productor emite:

### Bloque monoespaciado B

Va inmediatamente después del párrafo 7. Contenido exacto, respetando la alineación en columnas de
los tipos y de los comentarios:

```
class Detection(BaseModel):          # media.detection.v1
    detection_id:   str | None = None
    track_id:       str | None = None   # identidad entre fotogramas; hoy sin productor
    label:          str
    prompt_id:      str | None = None
    confidence:     float
    bbox_xyxy:      list[float]         # píxeles [x1, y1, x2, y2]
    bbox_norm_xyxy: list[float]         # normalizado [0, 1]
    area_px:        float | None = None
    model_name:     str | None = None
```

### Párrafo 8

El campo se declara como opcional con valor por defecto, se omite al serializar cuando no tiene
valor —de modo que su presencia en el contrato no altera un solo byte de los artefactos
existentes— y, sin embargo, el plano de control ya lo consume como clave de estado cuando opera
con granularidad por sujeto. El contrato conservó su versión: la extensión no exigió un cambio
incompatible ni la coordinación de un despliegue conjunto. Tres decisiones de implementación
sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto; los
consumidores validan contra su propia declaración del contrato y descartan sin error los campos
que no conocen, en lugar de rechazar el mensaje; y la frontera de la distribución declara
explícitamente que admite campos adicionales. El plano de control mantiene por eso su propia
declaración espejo del evento de percepción, no una biblioteca compartida con el plano de medios:
la frontera entre planos es el esquema serializado y no una dependencia de código, lo que permite
versionarlos y desplegarlos por separado. Éste es el mecanismo por el cual velocidad, dirección,
pose, segmentación o detecciones asociadas podrían incorporarse a la evidencia perceptiva; su
costo se detalla en la sección 17.4.11, donde también se declara que hoy no están implementadas.

## 3. Única edición fuera de §17.4.3

En la **Tabla 56** de §17.4.2, fila `FrameMetadata`, columna «Materialización efectiva».

Actual:

Unidad visual interna y bloque de fuente del evento publicado

Final:

Unidad visual y unidad preparada internas, y bloque de fuente del evento publicado

Es una sola celda. **No toques ninguna otra celda, ni el orden de las filas, ni los encabezados de
columna, ni el estilo, el ancho, los bordes o la alineación de la tabla, ni su nota.** La tabla
sigue teniendo diecisiete filas de contenido y sigue siendo la Tabla 56.

## 4. Formato

### F1 · Los ocho párrafos heredan el formato de cuerpo del documento

Idéntico al de los párrafos que estás reemplazando: estilo Normal, interlineado doble, espacio
posterior cero, sangría de primera línea de 1,27 cm, sin negrita y sin itálica. Sin viñetas y sin
numeración: los «Primero / Segundo / Tercero» del párrafo 6 y los enumerados del párrafo 8 son
prosa corrida, no listas.

### F2 · Los identificadores en línea van en monoespaciado, como ya hace el documento

El cuerpo de este documento ya escribe en Courier New los identificadores citados en prosa
—`detections.jsonl` en §17.4.5, `cr01_cr02_v2`, `person`, `helmet` y `vest` en §17.4.6,
`clip_gt.v2` en §17.4.8—, en **Courier New a 10,5 pt**, sin cambiar el resto del párrafo. Aplicá
exactamente ese tratamiento a los identificadores que aparecen entre acentos graves en la sección
2 de este prompt, y **sólo a ésos**:

- Párrafo 3: `DetectionEvent`
- Párrafo 5: `PatternStateChanged`
- Párrafo 6: `AlertEvent`, `CR-01:a_p1_c08`, `CR-01:a_p1_c08:subject_001`

Los acentos graves son marcación de este prompt: **no aparecen en el documento entregado.** Y
`DA-13` va en texto normal, como en §17.4.6.

### F3 · Los dos bloques monoespaciados clonan el bloque que ya existe en §17.4.7

En §17.4.7 hay un bloque monoespaciado con el árbol de artefactos del repositorio experimental
(`runs/<experiment_id>/ …`). Ese bloque ya tiene resueltas todas las propiedades que necesitan los
bloques nuevos. **Duplicá ese párrafo dos veces y reemplazale el contenido**, en lugar de armar el
formato desde cero. Para control, sus propiedades son:

- Un único párrafo por bloque, con los saltos de línea internos como saltos de línea manuales
  dentro del mismo párrafo —no un párrafo por renglón—.
- Courier New a 8,5 pt.
- Interlineado simple, no doble.
- Sangría de primera línea cero; sangría izquierda y derecha de 0,5 cm.
- Recuadro de línea simple de 0,5 pt en los cuatro lados, color gris claro (BFBFBF), con
  separación de 2 pt respecto del texto.
- Sombreado de relleno gris muy claro (F2F2F2).
- Marcado para no cortarse entre páginas.

Si por el largo el bloque A no cabe en una página, dejá que se corte: no lo reduzcas, no lo
partas en dos bloques y no le saques renglones.

### F4 · El contenido de los bloques es literal y la autocorrección no lo toca

Éste es el punto donde más fácil se arruina la entrega. Verificá, carácter por carácter, que en
los dos bloques:

- Las comillas son **comillas dobles rectas** (`"`), no comillas tipográficas curvas.
- Los guiones son **guiones simples**, no rayas ni guiones largos.
- La barra vertical de `str | None` está presente en las cinco líneas que la llevan.
- El numeral `#` de los cuatro comentarios está presente, y el texto del comentario queda tal
  cual, en español, sin traducir ni reescribir.
- Los corchetes de `list[float]`, `[x1, y1, x2, y2]` y `[0, 1]` están presentes.
- Ninguna palabra quedó capitalizada por autocorrección: `class`, `str`, `float`, `list`, `None`,
  `person`, `helmet` y todas las claves JSON van en minúscula tal como están escritas.
- Los números son exactamente los del prompt: ni redondeados, ni con coma decimal, ni con
  separador de miles. En estos dos bloques el separador decimal es el punto.
- La indentación de cuatro espacios del bloque B y la alineación en columnas de sus tipos y
  comentarios se conservan.
- No agregaste campos, ni comas finales, ni la detección `vest` que el objeto original tiene y
  este extracto omite a propósito.

## 5. Control final

Antes de entregar, verificá y confirmá punto por punto en tu respuesta:

1. §17.4.3 tiene ocho párrafos y dos bloques monoespaciados, en el orden dado, con el texto
   literal del prompt.
2. El encabezado de §17.4.3 no cambió, ni en texto ni en formato.
3. Ningún párrafo quedó con el texto viejo y el nuevo conviviendo, y ninguno de los cuatro
   párrafos originales sobrevivió en otra parte de la sección.
4. El documento no ganó ninguna tabla ni ninguna figura. Sigue con la Figura 4.7 y las Tablas 56
   a 61, con los mismos números.
5. Los dos bloques no llevan etiqueta «Figura», ni epígrafe, ni «Nota.».
6. La celda de la fila `FrameMetadata` de la Tabla 56 tiene el texto final indicado, y **ninguna
   otra celda de esa tabla cambió**.
7. Los cinco identificadores en línea de la lista de F2 están en Courier New a 10,5 pt; ningún
   otro término del texto nuevo quedó en monoespaciado; no quedó ningún acento grave en el
   documento.
8. Los dos bloques pasan la revisión de F4: comillas rectas, `|`, `#`, corchetes, minúsculas,
   números y alineación intactos.
9. El texto nuevo no referencia documentos locales, decisiones de arquitectura numeradas, fichas,
   especificaciones ni rutas del repositorio. Las únicas referencias son a las secciones 17.4.11 y
   17.5, a la máquina de estados del diseño y a `DA-13`.
10. Las demás subsecciones de §17.4 —17.4.1, 17.4.2 salvo la celda indicada, y 17.4.4 a 17.4.11—
    están idénticas a v1.5, palabra por palabra.
11. El cuerpo no contiene asteriscos, `|`, `#`, viñetas, comillas de cita, marcadores nuevos ni
    texto de este prompt, fuera de los dos bloques monoespaciados.

Entregá el archivo como `E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx`.

Si alguno de estos cambios entra en conflicto con la plantilla o con el resto del capítulo, **no lo
resuelvas por tu cuenta**: entregá el documento con el texto tal como está acá y planteá el
conflicto al final de tu respuesta.
