# 90c — Texto extraído del documento de trabajo: §17.5 Evaluación y Validación (bajada del 2026-09-08, nombrada v1.5 pero con el contenido de la v1.9: el número retrocedió al renumerar. Limpia, sin comentarios. ETAPA 5 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.5.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.5. Evaluación y validación del prototipo

#### 17.5.1. Encuadre y reglas de lectura

La evaluación informa cuánto produjo el prototipo bajo las condiciones experimentales definidas. Los resultados se organizan por pregunta de medición y distinguen tres niveles. La percepción sobre imágenes caracteriza al detector, el estado observable por persona evalúa la reconstrucción de una condición por sujeto, y la alerta temporal por episodio representa a la plataforma completa. Las mediciones de percepción, estado por persona y alerta por episodio pertenecen al Escenario A, sobre material congelado y relectura por archivo, y las de tiempo real al Escenario B, sobre captura continua.

Rigen las reglas de lectura fijadas en la sección 17.1.7.3. Cada cifra se acompaña de la combinación que la produjo, del material o estrato sobre el que se calculó y de su denominador. Precisión, recall y F1 se calcularon sólo sobre casos positivos con referencia aplicable, los materiales negativos se analizaron por conteo de falsos positivos, las re-alertas se contabilizaron aparte y los percentiles de tramos con relojes distintos no se sumaron. Los nombres abreviados de esta sección siguen al marco de métricas, con dos equivalencias. AP50 y mAP50 designan la precisión media a solapamiento 0,5 que el marco escribe AP@0,5, y la latencia de alerta es el intervalo que el marco llama t_alert-system. La latencia de alerta mide el intervalo entre el inicio del episodio anotado y su alerta confirmada, y la cobertura del episodio, que las tablas abrevian SDR, expresa qué proporción del tiempo con la condición activa mantuvo evidencia correcta.

El banco temporal congelado comprendió 47 clips, distribuidos en 32 positivos y 15 negativos, con 37 episodios de referencia. Lo integran 34 clips de un bloque de rodaje guionado y 13 de un estrato de obra real no guionada. El estrato de obra real no guionada se mantuvo separado y no se utilizó para ordenar granularidades cuando su denominador efectivo fue insuficiente. La referencia temporal fue humana y quedó congelada antes del reporte.

Una métrica se trató como computable sólo cuando existieron referencia, reloj e instrumentación compatibles con su definición. Cuando faltó alguno de esos elementos, el resultado se declaró no aplicable o no interpretable en lugar de convertir la ausencia de medición en un cero.

#### 17.5.2. Percepción sobre imágenes

La primera pregunta examinó la capacidad perceptiva de las combinaciones sobre un banco congelado de 6.477 imágenes y 55.165 anotaciones. El material se dividió en tres estratos independientes de 147, 1.330 y 5.000 imágenes, correspondientes a obra curada, a obra con mayor cobertura de chaleco y a una fuente con clase nativa de cabeza descubierta. El tercero aportó el 77 % del banco, de modo que el agregado se leyó siempre junto con el desglose por estrato.

La Tabla 61 muestra que la combinación gdino-tiny-560 alcanzó el mAP50 más alto en el agregado y en el núcleo curado, mientras que gdino-base-560 produjo el recall más alto de CR-01 por evidencia directa. El veredicto se formuló entonces por combinación. El primer perfil se retuvo como configuración operativa por un criterio fijado antes de leer los resultados, y el segundo como contraste especializado para cabeza descubierta y chaleco. No se estableció una jerarquía universal entre modelos. Las dos comparten resolución de entrada y umbrales, que declara la sección 17.4.4, y difieren en el tamaño del perfil.

**Tabla 61**

*Resultados de percepción por combinación en el banco congelado*

| **Combinación** | **mAP50 agregado (n = 6.477 imágenes)** | **mAP50 obra curada (n = 147 imágenes)** | **Recall de CR-01 por evidencia directa (n+ = 5.313)** | **Veredicto por combinación** |
| --- | --- | --- | --- | --- |
| gdino-tiny-560 | 0,551 | 0,503 | 0,308 | Retenida como perfil operativo por liderar el mAP50 en las dos escalas reportadas. |
| gdino-base-560 | 0,525 | 0,474 | 0,599 | Retenida como contraste de mayor cobertura de cabeza descubierta y chaleco. |
| yoloe-26x | 0,442 | 0,405 | 0,000 | Ciega a la cabeza descubierta, de modo que no sostiene la formulación directa. Su límite para el núcleo es el chaleco, con AP 0,182 en obra curada frente a 0,520 del perfil operativo. |

***Nota****.* El denominador del agregado es el banco completo. El recall de CR-01 se informa sobre 5.313 positivos, el conteo de la referencia con la que se ejecutó la campaña. Una corrección posterior de esa referencia lo dejó en 5.308 y la medición no se repitió. Esa columna cuenta sólo detecciones de cabeza descubierta, de modo que mide la formulación directa. El núcleo opera con la indirecta, que deriva la ausencia desde persona y casco, y su capacidad para la condición no se lee en esta columna.

La especialización del perfil base también apareció en chaleco, con AP 0,582 frente a 0,520 del perfil operativo sobre el estrato de obra curada. Para el perfil operativo, persona y casco se mantuvieron entre 0,70 y 0,89 de AP en los dos estratos públicos, mientras que chaleco quedó en 0,553 y 0,520 en los dos estratos que anotan esa clase. La asimetría no dependió de una única fuente, porque se sostuvo en ambos.

La familia YOLOE presentó una limitación distinta. Sus cuatro variantes produjeron AP 0,000 para bare_head, la clase de cabeza descubierta, sobre el banco anterior al congelado, y la variante mayor repitió el cero sobre el estrato que anota esa clase de forma nativa. Aunque resultó adecuada para rutas de mayor velocidad, esa ceguera la volvió inservible para la formulación directa de CR-01 en la configuración evaluada.

La extensibilidad semántica se ejerció sobre una clase nueva, cuyo costo de incorporación informa la sección 17.4.8. La clase alcanzó AP50 de 0,662 sobre 99 cajas de referencia sin ninguna corrida de entrenamiento. El costo reducido no eliminó la necesidad de validación semántica. Sobre el mismo material, la palabra vehicle no produjo ninguna detección cuando acompañó a machinery en el vocabulario y, aislada, produjo 118 cajas con AP 0,026, porque el modelo la resolvió sobre la maquinaria misma.

#### 17.5.3. Estado por persona

El nivel intermedio evaluó si la evidencia perceptiva permitía determinar el estado observable de cada persona. La calibración se realizó sobre una mitad del material y las métricas sobre la otra, con IoU mayor o igual que 0,5. La partición en mitades se registró con su semilla y fue la misma para todos los brazos, de modo que ninguna imagen que ajustó un umbral entró después en la medición. Se compararon E-IND, la estrategia indirecta que reconstruye la ausencia desde evidencia positiva, y E-DIR, la formulación directa retenida para el contraste. La medición sobre video abarcó 17 clips de obra real, los 13 del estrato de obra real del banco temporal y 4 de un piloto anterior, evaluados al nivel del estado por persona sobre su referencia de atributos, submuestreados a 2 Hz y sin calibración de umbrales, con el punto de operación desplegado, y no incluyó el motor de patrones. La Tabla 62 reúne los resultados.

**Tabla 62**

*Resultados de estado por persona*

| **Material y condición** | **Resultado E-IND** | **Contraste E-DIR** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Imágenes, CR-01 | F1 0,546 | F1 0,188 | n+ = 2.487 | Los intervalos de confianza no se solaparon. |
| Núcleo curado, CR-01 | F1 0,408 | F1 0,189 | n+ = 28 | La ventaja se conservó en el estrato objetivo. |
| Imágenes, CR-02 | F1 0,479 | F1 0,418 | n+ = 82 | Un único estrato; el resultado no cerró la condición. |
| Video de obra real - CR-01 | P 0,016 · R 0,467 · F1 0,031 | No corresponde a esta medición | n+ = 92 de 10.356 cuadros con persona | La caída provino de precisión, no de recall. |
| Video de obra real - CR-02 | P 0,009 · R 0,318 · F1 0,018 | No corresponde a esta medición | n+ = 170 de 10.361 cuadros con persona | La misma frontera de juzgabilidad dominó el resultado. |

La estrategia directa no se comportó como un detector estable del estado, sino como un recuperador de casos omitidos por la estrategia indirecta. Recuperó el 18,5 % de esos casos, equivalentes a 155 de 840, pero lo hizo a costa de precisión. Esa relación explica por qué la estrategia no se adoptó aunque aportara evidencia complementaria en un subconjunto.

La medición sobre 17 clips de obra real mostró un cambio de régimen. La caída del F1 provino de la precisión y no del recall, por acumulación de falsos positivos sobre personas cuyo estado no podía determinarse visualmente. El evaluador excluyó del denominador 1.414 cuadros con persona no juzgables para CR-01, aquellos en los que el anotador no pudo determinar el estado, y 1.409 para CR-02, y contabilizó como falso positivo cualquier predicción emitida sobre ellos.

Esa frontera tiene al menos tres ejes y ninguno de los tres, por sí solo, anticipa si el material es evaluable. La escala ordena dentro de un mismo régimen de luz. En los clips diurnos del estrato de obra real, la proporción de sujetos detectados a los que se asocia un chaleco pasa de alrededor del 10 % en la banda de 80 a 120 píxeles de altura a entre 63 y 73 % en la banda de 220 a 320, y en el bloque de rodaje, con medianas de altura por encima de 700 píxeles, esa misma asociación se sostuvo entre 96 y 100 %. La iluminación desplaza la curva entera, porque en el clip nocturno del estrato la banda de 80 a 120 píxeles cae a 0 % y las siguientes, hasta 320, quedan entre 6 y 13 %. Y la oclusión invierte el orden de los dos ejes anteriores, ya que el clip con los sujetos más grandes del conjunto, con mediana de 370 píxeles, quedó entre los peores resultados con F1 0,084 sobre una cuadrilla apiñada en la que el 58,5 % de las personas aparece solapada con otra. Tampoco la juzgabilidad humana anticipa el rendimiento del sistema, porque el clip con la segunda proporción más baja de cuadros no observables para el anotador rindió el peor F1 del conjunto.

#### 17.5.4. Alerta por episodio contra la referencia temporal humana

La alerta por episodio constituyó el resultado principal porque integra percepción, asociación, histéresis, estado temporal y registro de alerta. El bloque de rodaje guionado reunió 34 clips y 35 episodios de referencia, 28 de CR-01 y 7 de CR-02. Treinta y cuatro episodios resultaron evaluables y uno quedó censurado con causa declarada, porque su duración no permitía que una alerta lenta ocurriera dentro del clip, y cuatro clips fueron negativos. La Tabla 63 reúne las combinaciones ejecutadas sobre ese material, cada una con una sola variable cambiada respecto de la línea de base.

**Tabla 63**

*Alerta por episodio en el bloque de rodaje guionado*

| **Combinación** | **Recall** | **Precisión** | **F1** | **t_alert en ms (n de episodios confirmados)** | **SDR** | **FP en 4 negativos** | **Veredicto local** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Núcleo E-IND, escena | 0,824 | 0,757 | 0,789 | 5.327 (n = 28) | 0,698 | 0/4 | Línea de base de la plataforma. |
| Contraste base-560 | 0,735 | 0,676 | 0,704 | 4.899 (n = 25) | 0,819 | 0/4 | Mayor SDR, menor F1 que el perfil operativo. |
| E-DIR de extremo a extremo | 0,176 | 0,146 | 0,160 | 6.611 (n = 6) | 0,210 | 2/4 | Vetada por precisión. |
| E-HYB por disyunción | 0,353 | 0,255 | 0,296 | 6.956 (n = 12) | 0,738 | 2/4 | Ejecutada y refutada. |
| Núcleo E-IND, sujeto | 0,971 | 0,892 | 0,930 | 5.236 (n = 33) | 0,698 | 0/4 | La identidad elevó F1 sin cambiar las detecciones. |
| Vocabulario nativo bare_head | 0,382 | 0,371 | 0,377 | 3.919 (n = 13) | 0,940 | 3/4 | Alerta temprana, con mayor costo en falsos positivos. |

***Nota****.* Las métricas temporales se calcularon sobre 34 episodios evaluables de 35 en el bloque de rodaje, y el número entre paréntesis de la columna de latencia es la cantidad de episodios confirmados, mientras que la media se promedia por clip con alerta confirmada, un conteo menor cuando un mismo clip contiene las dos condiciones. Los falsos positivos se cuentan sobre los cuatro clips negativos y no incluyen re-alertas.

La histéresis rescató evidencia intermitente. CR-02 confirmó sus 7 episodios, con recall 1,000 y SDR 0,281, aunque requirió una latencia de alerta de 8.572 ms frente a 4.314 ms para CR-01. Las dos medias se promediaron por clip con alerta confirmada, siete en CR-02 y veintiuno en CR-01. La diferencia fue coherente con ventanas de confirmación de 7,0 y 4,0 s. Una detección sostenida sólo durante una fracción del episodio pudo producir una alerta correcta cuando acumuló evidencia suficiente dentro de la ventana. La Figura 4.6 muestra un fotograma con la alerta ya confirmada. Las referencias por severidad de la sección 17.1.7.5 no se usaron como criterio de aceptación, porque el propio protocolo las condiciona a una recalibración previa que esta evaluación no realizó, y sus valores se leen como dato.

**Figura 4.6**

*Fotograma con alerta confirmada de CR-01*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** Fotograma del clip a_p1_c04 del bloque de rodaje a los 8,5 s, en la corrida de línea de base, con la alerta emitida a los 7,3 s y el motor en estado sostenido. El casco visible sobre la mesa, que el detector marca en cuadros vecinos, no suprime la condición, porque CR-01 se evalúa sobre la región del sujeto y no sobre la escena.

La identidad temporal fue la capa con mayor aporte medido dentro del banco. Con las mismas detecciones, la granularidad por sujeto elevó el F1 de 0,789 a 0,930, una diferencia de 0,141 sobre los 34 episodios evaluables. En el escenario de mayor dificultad el resultado pasó de 0,400 a 1,000, es decir de dos episodios confirmados sobre cinco a los cinco. La mejora no provino del detector, sino de evitar que la evidencia de personas distintas se mezclara dentro de un mismo estado de escena.

El vocabulario activo también se comportó como una variable experimental. Sobre la combinación de contraste base-560, un ensayo posterior mantuvo fijos el modelo, el evaluador, el conjunto de patrones, la referencia y los tiempos, y sumó al vocabulario una sola palabra, la de cabeza descubierta. El F1 por episodio bajó de 0,704 a 0,622, el recall de 0,735 a 0,676 y la precisión de 0,676 a 0,575. La interacción entre términos de un mismo vocabulario no resultó despreciable, de modo que dos configuraciones sólo son comparables cuando declaran el vocabulario completo que vieron.

El estrato de obra real no guionada se informó por separado y comprendió 13 clips. Una revisión ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación por sobre-declarar estados que no resultaban observables, y dejó 2 episodios evaluables y 11 clips negativos. Ese denominador impidió ordenar granularidades. El resultado robusto del estrato fue la asimetría de falsos positivos, 26 con granularidad de escena frente a 323 con granularidad por sujeto sobre los mismos 11 clips negativos. Esa asimetría es el ΔFP_tracking que adopta el marco de métricas de la sección 17.1.7, y su signo es el contrario al del riesgo que la sección 17.1.10 anticipaba, que el seguimiento agregara complejidad sin reducir falsas alarmas.

Sobre el único tramo continuo de cumplimiento, de 6 minutos y 9,6 segundos, los conteos fueron 3 falsos positivos con granularidad de escena y 190 con granularidad por sujeto. Las tasas de 29,2 y 1.850,8 falsas alarmas por hora se derivan de esa exposición de 0,1027 h y se informan como magnitudes derivadas, nunca como cota operativa, porque la exposición disponible estuvo casi treinta veces por debajo de la necesaria para sostener una.

#### 17.5.5. Tiempo real

La evaluación en vivo examinó qué parte del resultado temporal sobrevivía cuando la densidad de procesamiento descendía respecto de la evidencia disponible. El banco se representó a 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps. Para cubrir esa franja, los 34 clips del bloque de rodaje se remuestrearon de manera pareada a cuatro densidades, de 30 a 1,15 cuadros por segundo. La Tabla 64 reúne esas mediciones junto con las de integridad y latencia por tramo.

**Tabla 64**

*Resultados del camino en vivo por densidad, integridad y tramo temporal*

| **Eje** | **Condición o material** | **Resultado** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Densidad | Referencia del banco, 30 fps | Escena 0,789 · sujeto 0,930 | n = 34 episodios evaluables | Punto de partida de la comparación. |
|  | Techo en vivo, aproximadamente 4,29 fps | Escena 0,794 · sujeto 0,866 | n = 34 episodios evaluables | La ganancia por identidad se conservó. |
|  | Intermedia, aproximadamente 2,00 fps | Escena 0,738 · sujeto 0,875 | n = 34 episodios evaluables | La pérdida no avanza de manera uniforme. |
|  | Peor caso, aproximadamente 1,15 fps | Escena 0,646 · sujeto 0,742 | n = 34 episodios evaluables | La restricción redujo ambos resultados sin invertir el orden. |
| Identidad | Cuatro densidades medidas | Ganancias de F1 +0,141 · +0,072 · +0,137 · +0,096 | n = 4 densidades sobre 34 clips; remuestreo pareado por clip | El intervalo empírico excluyó el cero en las cuatro condiciones. |
| Integridad | Relectura frente a transmisión | 0 eventos perdidos · paridad byte a byte verificada en una corrida y protegida por prueba automatizada | n = 6 corridas del rodaje para los eventos. n = 1 corrida para la paridad | El transporte no alteró la evidencia. |
| Latencia | Sobrecarga de la plataforma con detector simulado, en diferido | p50 14,7 - p95 31,8 ms | n = 20 unidades | Costo propio de la cadena sin inferencia, dentro del presupuesto de la sección 17.1.7. |
| Latencia | Detector open-vocabulary en vivo | p95 630–890 ms | n = 47, 93 y 55 unidades procesadas en las tres corridas en vivo | Fuera del presupuesto; la corrida lo declaró. |
| Captura | Antes del retiro de la unidad | 202–217 ms | medianas por corrida; n = 47 a 295 unidades procesadas en cada una de las seis corridas | No está incluida en el tramo anterior. |
| Alerta | CR-01 en vivo | 7 alertas: 4,1–4,6 s | n = 7 confirmaciones | Ventana: 4,0 s. |
| Alerta | CR-02 en vivo | 3 alertas: ≥ 7,1 s | n = 3 confirmaciones | Ventana: 7,0 s. |
| Canal | Bus de alertas a confirmación del canal | p95 64,534 ms · sostenido 102,025 ms | n = 460 · sostenido n = 104 | Tramo separado; no se suma a la alerta del sistema. |

*Nota.* Los percentiles pertenecen a tramos con relojes distintos y no se suman. El tramo desde el retiro de la unidad comienza en el dequeue, no en la captura de la escena.

La cobertura del episodio no se comparó entre cadencias porque depende de cuántas unidades sobreviven al muestreo. Tampoco se comparó la latencia agregada entre densidades sin controlar la supervivencia, porque los episodios que no alcanzan a confirmar desaparecen del promedio y lo sesgan. Entre los episodios supervivientes, el costo de bajar la densidad fue de 0,7 a 1,3 s sobre ventanas de 4 a 7 s, medido sobre 21, 20 y 16 episodios comunes a las cadencias comparadas. Entre la densidad del banco y el techo del camino en vivo el resultado por escena no cambió de manera apreciable y el resultado por sujeto perdió 0,064, mientras que en la densidad más baja la caída ya alcanza 0,143 y 0,188 respectivamente. Con 34 episodios evaluables, las diferencias del orden de un episodio, 0,029 de recall, quedan dentro de la resolución del banco y no se leen como orden.

La medición confirmó además la separación entre captura, procesamiento y distribución. Los tres tramos corresponden a relojes distintos y por eso sus percentiles no se suman. El del tramo de distribución describe el intervalo desde el bus de alertas hasta la confirmación del canal, y no la latencia completa de la plataforma.

#### 17.5.6. Caminos probados y no adoptados

Los caminos no adoptados se evaluaron contra criterios fijados antes de leer sus resultados. La estrategia directa quedó descartada por un veto de precisión, cuyo umbral de 0,5 se fijó de antemano en el pre-registro de la comparación de estrategias y quedó muy por encima del valor obtenido. La brecha que ya mostraba en el estado por persona se amplió al atravesar el motor de patrones.

La fusión híbrida por disyunción fue ejecutada y refutada, porque el recall descendió respecto del núcleo indirecto en lugar de crecer. La unión de evidencia no resultó monótona dentro del motor de patrones, ya que las detecciones más tempranas desplazaron confirmaciones fuera de la ventana de referencia. La variante por conjunción no se ejecutó, porque no podía medirse contra el banco sin romper la comparabilidad de las seis combinaciones. La familia MM-Grounding-DINO se integró por el mismo mecanismo de adaptación y se archivó durante la selección de modelos, sobre el banco anterior al congelado, de modo que no tiene cifra comparable en esta sección. Una de sus variantes no aportó ventaja en ninguna dimensión evaluada, otra entregó cajas degeneradas con origen en el punto de control publicado y no en el adaptador que las integró, y la tercera localizó mal con geometría normal.

La rama comparativa de ajuste fino se cerró como una curva de capacidad, con criterios y expectativas registrados antes de cada evaluación, y sus cifras se mantuvieron separadas de las del núcleo sin entrenamiento. La Tabla 65 recorre sus tres puntos.

**Tabla 65**

*Curva de capacidad de la rama comparativa de ajuste fino*

| **Punto o tramo** | **Resultado de ganancia** | **Retención y comportamiento** | **Veredicto** |
| --- | --- | --- | --- |
| Línea base sin ajuste | AP50 bare_head 0,0000 · recall de CR-01 por evidencia directa 0,0002 | Referencia previa a los tramos entrenados. | Punto de partida. |
| Primer tramo entrenado | AP50 bare_head 0,0455 · recall de CR-01 por evidencia directa 0,2089 | Quedó a 0,0045 del umbral de AP50 0,05 y redujo person de 0,7843 a 0,6932 (−11,62 %), con tope de 10 %. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Segundo tramo entrenado | AP50 bare_head 0,0909 | Detención temprana 16/60, mejor época 1; person de 0,7843 a 0,3943 (−49,7 %) y mAP50 en dominio de 0,4193 a 0,2374 (−43,4 %); retención open-vocabulary 0,4347 a 0,1247 (−71,3 %) · n = 5.000 imágenes de validación de COCO 2017. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Tramo adicional | No corresponde | Cerrado con causa técnica antes de producir una comparación interpretable. | Sin checkpoint y sin nuevo brazo contra el banco. |

***Nota****.* Los puntos medidos pertenecen a una rama comparativa separada. Las métricas en dominio de la línea base y de los dos tramos entrenados se calcularon sobre el banco congelado de 6.477 imágenes. El primer tramo agregó principalmente recall y el segundo, AP, de modo que no existe una combinación ajustada universalmente superior. Los tres puntos corresponden a la variante s de YOLOE-26. El primer tramo entrenó sólo la proyección de clases, 3.096 parámetros, y el segundo el detector completo con las rutas de prompt congeladas, 10,35 millones. La retención open-vocabulary se midió sobre un material ajeno al dominio, distinto del estrato de 5.000 imágenes del banco.

El segundo tramo duplicó el AP50 de cabeza descubierta respecto del primero, pero colapsó durante el entrenamiento y falló las dos retenciones. El patrón conjunto mostró que el límite no fue capacidad de cómputo sino estructura experimental, con 2.946 imágenes de ajuste frente a 10,35 millones de parámetros, un conjunto cuya composición, regla de partición y configuración de entrenamiento declara la sección 17.4.7. Ningún checkpoint se adoptó como modelo de servicio, y los veredictos negativos se conservaron como resultados pre-registrados y no como trabajo pendiente.

#### 17.5.7. Lo no ejecutado y lo no implementado

Las condiciones de Nivel 2 y Nivel 3 no se implementaron en el núcleo evaluativo porque el material disponible no aportaba verdad de terreno del dominio ni evaluadores relacionales, zonales o de trayectoria que pudieran validarse. Incorporarlas habría producido capacidades sin medición defendible y habría confundido extensión arquitectónica con resultado experimental.

Las métricas formales de seguimiento multiobjeto tampoco se calcularon, porque faltó una referencia de identidad apta para ese propósito. La exclusión no alcanzó a la capacidad de identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta. La ganancia informada más arriba y su persistencia en las cuatro densidades pertenecen a esa capacidad y no a una métrica de seguimiento.

La preselección liviana en el dispositivo de captura fue implementada para la fuente propia y caracterizada mediante una comparación pareada. Descartó el 87 % de las unidades antes de abandonar el dispositivo, 206 de las 236 que vio la compuerta, frente a las 277 que procesó la rama sin preselección, y permaneció deshabilitada en todas las corridas evaluativas. La exclusión fue deliberada, porque un filtro de cuadros sin persona habría suprimido la evidencia sostenida que la medición de falsas alarmas debía observar y habría superpuesto el error de un detector auxiliar sobre la cadena evaluada.

Tampoco se sostuvo una cota operativa de falsas alarmas. Para hacerlo se requerían aproximadamente 3 h de cumplimiento anotado, mientras que la exposición continua disponible fue de 0,1027 h. La tasa horaria se reportó como derivación observacional, pero el material no habilitó una afirmación poblacional.

Finalmente, la comparación temporal directa entre una fuente en vivo y su reproducción desde clip se declaró no interpretable. Sin un ancla común entre el reloj de pared y el tiempo del medio, el emparejamiento habría mezclado desfases instrumentales con el comportamiento de la plataforma.

El sub-experimento formal que evaluaba cada prompt en aislamiento y dentro del vocabulario completo no se ejecutó sobre las combinaciones finalistas. La pregunta que lo motivaba quedó respondida por el contraste de variable única informado más arriba, que midió el costo de sumar un término al vocabulario activo.

El marco de métricas admite además medidas que esta evaluación no reporta, y su estado se declara en lugar de omitirse. El tiempo hasta la primera detección se computó en todas las campañas y no se informa aquí, porque la comparación entre combinaciones se resolvió con la latencia de alerta, que es la que integra el motor de patrones. La precisión media promediada sobre el rango de umbrales de solapamiento quedó sin computar, porque la lectura se fijó en un único umbral. El percentil 99 de latencia se computó por corrida y no se consolidó como resultado comparativo, porque las corridas en vivo procesaron entre 30 y 295 unidades, muy por debajo de lo que ese percentil requiere. El consumo de memoria del acelerador se registró por corrida y no se consolidó como resultado comparativo, porque describe al perfil cargado y no a la combinación evaluada. Los benchmarks públicos de seguimiento multiobjeto previstos en la estrategia de datos no se ejecutaron, por la misma falta de referencia de identidad que excluyó a sus métricas. La curva de falsos positivos en función de la duración de la ventana, que la sección 17.1.5.2 prevé como eje de la calibración empírica, no se ejecutó, y las ventanas se usaron con sus valores de protocolo.

Ocho limitaciones acotan la lectura de todo lo anterior. La tasa de falsas alarmas por hora no sostiene una cota operativa. La referencia temporal no tuvo doble anotación ni medida de acuerdo entre anotadores. Los bordes de episodio se adjudicaron por criterio único en seis clips. El material guionado proviene de un solo bloque de rodaje, y la medición sobre obra real precisó esa limitación sin levantarla, porque caracteriza por mecanismo dónde el sistema deja de ser evaluable en lugar de validarlo sobre obra real. Los escenarios quedaron desbalanceados, de modo que todo resultado se reporta por estrato además del agregado. El seguimiento no tiene métricas formales en obra real con multitud, aunque un clip con 127 personas mostró la fragmentación de identidades que explica la precisión por sujeto de ese estrato. Una de las fuentes de imágenes conserva licencia parcial. Y la condición de chaleco no quedó cerrada al nivel del estado por persona.
