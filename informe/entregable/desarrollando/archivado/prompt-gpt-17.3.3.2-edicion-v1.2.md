# Prompt para GPT — edición de cierre de §17.3.3.2 (v1.1 → v1.2)

> Pegar todo lo que sigue a la línea de guiones como mensaje único en el Project, junto con
> el `.docx` `E-OVRT-VDP_Seccion_17.3.3.2_Capacidades_Arquitectonicas_Requeridas_v1.1.docx`.

---

Revisé el `.docx` que entregaste de §17.3.3.2. **Está bien**: la estructura es la correcta, las
cuatro filas que debían salir salieron, la columna Compromiso cierra en las cinco clases que la
nota define, los dos párrafos y la nota quedaron textuales, y la herencia de plantilla es exacta
—el bloque de propiedades de la tabla es idéntico al de la Tabla 39 del documento maestro—.

Falta una sola pasada de cierre: **ocho ediciones de palabra en la tabla y cuatro ajustes de
formato.** Con eso queda listo para pegar en el documento de desarrollo.

## 0. Alcance de esta pasada

1. **Editás el `.docx` v1.1 que ya entregaste y devolvés v1.2.** No lo regeneres desde cero.
2. **Sólo cambia lo que esta lista indica.** Todo lo demás queda exactamente como está: los dos
   párrafos, el texto de la nota, las diecinueve filas en su orden, los encabezados de columna,
   el estilo y el ancho de la tabla, el cuerpo a doble espacio, la sangría y el cuerpo de celda
   a 11 pt.
3. **No agregues ni quites filas.** Siguen siendo diecinueve.
4. **La tabla sigue siendo la Tabla 39.** No renumeres nada.
5. **No vuelvas a acortar el texto.** El pedido anterior de reducir la tabla ya se aplicó y el
   resultado es correcto. Estas ocho ediciones **agregan** unas dieciocho palabras a propósito:
   recuperan términos técnicos que la reducción se llevó. No compenses recortando en otra celda.
6. El resultado no contiene asteriscos, `|`, `#`, comillas de cita, viñetas de andamiaje ni
   ningún fragmento de este prompt.

## 1. Ediciones en la tabla (ocho celdas de «Lectura de diseño»)

Para cada una te doy el texto actual y el texto final. **Reemplazá la celda completa** por el
texto final: es más seguro que buscar y sustituir fragmentos.

### E1 · Fila «Gestión y gobierno de la corrida»

Actual:

Debe existir un punto explícito para congelar la configuración efectiva de cada ejecución,
gobernar su ciclo de vida —creación, consulta, cancelación y cierre— y ordenar el disparo entre
módulos.

Final:

Debe existir un punto explícito para declarar y congelar la configuración efectiva de cada
ejecución, gobernar su ciclo de vida —creación, consulta, cancelación y cierre— y ordenar el
disparo entre módulos.

### E2 · Fila «Operación sobre fuentes en vivo»

Actual:

Debe admitir captura o streaming controlado, donde la fuente continúa evolucionando aunque el
procesamiento no sostenga la cadencia, para observar el comportamiento operativo del sistema.

Final:

Debe admitir captura o streaming en entorno controlado, donde la fuente continúa evolucionando
aunque el procesamiento no sostenga la cadencia, para observar el comportamiento operativo del
sistema.

### E3 · Fila «Normalización de entrada visual»

Actual:

Cada frame debe incluir metadatos de corrida, fuente, orden temporal, resolución y muestreo,
para compartir el pipeline sin ocultar las diferencias temporales entre fuentes.

Final:

Cada frame debe incluir metadatos de corrida, fuente, orden temporal, resolución y política de
muestreo, para compartir el pipeline sin ocultar las diferencias temporales entre fuentes.

### E4 · Fila «Normalización de detecciones»

Actual:

La salida del plano de medios debe usar un evento de percepción versionado como única unidad de
evidencia compartida para interpretar patrones, persistir y releer corridas.

Final:

La salida del plano de medios debe expresarse como un contrato de evento de percepción
versionado, única unidad de evidencia compartida para interpretar patrones, persistir y releer
corridas.

### E5 · Fila «Evaluación de patrones de Nivel 1»

Actual:

Las detecciones positivas deben asociarse por sujeto, convertirse en un estado evaluable de
ausencia y estabilizarse mediante persistencia temporal e histéresis.

Final:

Las detecciones positivas deben asociarse espacialmente por sujeto, convertirse en un estado
evaluable de ausencia y estabilizarse mediante persistencia temporal e histéresis.

### E6 · Fila «Distribución de alertas confirmadas»

Actual:

Debe convertir alertas confirmadas en intentos de entrega registrados, después del registro
interno y fuera del razonamiento del patrón, para que fallas externas no afecten al motor.

Final:

Debe convertir alertas confirmadas en intentos de entrega registrados, después del registro
interno y fuera del razonamiento del patrón, para que una falla externa no se propague al motor
de patrones.

### E7 · Fila «Identidad temporal de sujeto»

Actual:

Debe admitir granularidad por sujeto mediante identidad temporal válida. Las métricas formales
de seguimiento multiobjeto no condicionan la evaluación del núcleo ni se confunden con esta
capacidad.

Final:

Debe admitir granularidad por sujeto mediante identidad temporal válida. Las métricas formales
de seguimiento multiobjeto no condicionan la evaluación del núcleo ni deben confundirse con la
capacidad de mantener identidad.

### E8 · Fila «Capacidades contextuales y relacionales»

Actual:

Debe prever contexto, zonas, proximidad y evaluadores relacionales para condiciones de Nivel 2
y 3, sin bloquear CR-01 y CR-02. Su habilitación exige evidencia e instrumentación adecuadas.

Final:

Debe prever contexto, razonamiento espacial, zonas, proximidad y evaluadores relacionales para
las condiciones de Nivel 2 y Nivel 3, sin bloquear CR-01 y CR-02. Su habilitación exige
evidencia e instrumentación adecuadas.

### Por qué estas ocho y no otras

No es preferencia de estilo: cada una recupera un término que el documento usa con un sentido
preciso. «Espacialmente» es lo único que dice *cómo* se asocian las detecciones por sujeto.
«Contrato» conecta la fila con el tratamiento de contratos versionados del capítulo, que es la
razón por la que esa capacidad existe como fila propia. «Razonamiento espacial» distingue una
zona de una relación entre entidades. «Política de muestreo» es un parámetro declarado de la
corrida, no el acto de muestrear. «En entorno controlado» dice que lo controlado es el entorno y
no el stream. «Motor de patrones» y «propagarse» nombran el mecanismo exacto del desacople.
«Declarar y congelar» son dos operaciones distintas. Y «la capacidad de mantener identidad»
evita un pronombre justo en la distinción que separa la capacidad de las métricas.

## 2. Ajustes de formato

### F1 · La nota de la tabla va con «Nota» en negrita

Hoy dice `Nota.` en itálica. En el documento maestro, las notas de la Tabla 39 y de la Tabla 40
usan **«Nota» en negrita**, con el punto y el resto del texto en redonda. Como esta subsección
se pega junto a la Tabla 40, tiene que seguir la convención del maestro:

- «Nota» en negrita.
- El punto que le sigue y todo el resto de la nota, en redonda. Sin itálica.
- El texto de la nota no cambia ni una palabra.

### F2 · El encabezado tiene que igualar a sus hermanos

Hoy el encabezado `17.3.3.2. Capacidades arquitectónicas requeridas` está entero en itálica. En
el maestro, los cuatro encabezados hermanos —§17.3.3.1, §17.3.3.2, §17.3.3.3 y §17.3.3.4— tienen
itálica **sólo en el prefijo «17.3»**, y el resto hereda la negrita del estilo de nivel 4.
Reproducí ese patrón exacto: itálica en `17.3`, y `.3.2. Capacidades arquitectónicas requeridas`
sin itálica, heredando el estilo.

### F3 · Sólo la primera fila es fila de encabezado repetible

Hoy las veinte filas están marcadas como fila de encabezado que se repite al cortar página. Eso
viene del maestro, pero acá conviene corregirlo: la tabla ocupa varias páginas a doble espacio y
con las veinte marcadas no puede repetir sólo el encabezado. Dejá la marca **únicamente en la
primera fila** (la de «Capacidad requerida · Compromiso · Lectura de diseño») y quitala de las
diecinueve filas de contenido.

### F4 · Sacá las imágenes que no se usan

El archivo pesa 5,8 MB porque arrastra seis imágenes de la plantilla base (unos 5,5 MB) que no
están referenciadas en el cuerpo, ni en el encabezado, ni en el pie de página. Si podés
entregarlo sin esos archivos incrustados, hacelo. Si no podés, entregalo igual: no afecta el
contenido ni el pegado.

## 3. Control final

Antes de entregar, verificá y confirmá punto por punto en tu respuesta:

1. Las ocho ediciones aplicadas, con el texto final exacto, y **ninguna otra celda modificada**.
2. Ninguna celda quedó con el texto viejo y el nuevo conviviendo.
3. Diecinueve filas de contenido, en el mismo orden que en v1.1.
4. La columna Compromiso sigue usando sólo las cinco clases que la nota define.
5. Los dos párrafos y el texto de la nota, idénticos a v1.1.
6. «Nota» en negrita y el resto de la nota en redonda.
7. Itálica sólo en el prefijo «17.3» del encabezado.
8. Marca de fila de encabezado repetible sólo en la primera fila.
9. El documento contiene únicamente §17.3.3.2: encabezado, dos párrafos, Tabla 39, nota. Nada
   más, ninguna otra sección, ninguna otra tabla.
10. Sin asteriscos, `|`, `#`, comillas de cita, marcadores nuevos ni texto de este prompt.
11. Estilo, ancho, bordes y alineación de la tabla sin cambios respecto de v1.1; cuerpo a doble
    espacio con sangría 1,27 cm; celdas a 11 pt.

Entregá el archivo como
`E-OVRT-VDP_Seccion_17.3.3.2_Capacidades_Arquitectonicas_Requeridas_v1.2.docx`.

Si alguna de las ediciones entra en conflicto con la plantilla o con el resto del capítulo, **no
lo resuelvas por tu cuenta**: entregá el documento con el texto tal como está acá y planteá el
conflicto al final de tu respuesta.
