# 90c — Texto extraído del documento de trabajo: §17.5 Evaluación y Validación (v1.3)

> **Extracción derivada (2026-08-23)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.3.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.5. Evaluación y validación del prototipo

#### 17.5.1. Encuadre y reglas de lectura

La presente sección informa cuánto produjo el prototipo bajo las condiciones experimentales definidas. Los resultados se organizan por pregunta de medición y distinguen tres niveles: percepción sobre imágenes, estado observable por persona y alerta temporal por episodio. El primero caracteriza al detector, el segundo evalúa la reconstrucción de una condición por sujeto y el tercero representa a la plataforma completa. Las capacidades funcionales y su verificación técnica se documentaron en la sección 17.4; aquí se reportan sus mediciones, mientras que la interpretación de conjunto corresponde a las conclusiones.

Toda cifra se vincula con una combinación, un material o estrato y un denominador. Las métricas de precisión, recall y F1 se calcularon únicamente sobre casos positivos con referencia aplicable. Los materiales negativos se analizaron mediante conteos de falsos positivos; cuando se derivó una tasa horaria, se informó junto con la duración observada y no se la utilizó como cota operativa. Las re-alertas se contabilizaron por separado y no se clasificaron como falsos positivos. Los percentiles de latencia pertenecientes a relojes o tramos distintos no se sumaron.

El banco temporal congelado comprendió 47 clips, distribuidos en 32 positivos y 15 negativos, con 37 episodios de referencia. Esta descomposición no debe confundirse con los 34 clips del bloque de rodaje guionado. El estrato de obra real no guionada se mantuvo separado y no se utilizó para ordenar granularidades cuando su denominador efectivo fue insuficiente. La referencia temporal fue humana y quedó congelada antes del reporte.

Una métrica se trató como computable sólo cuando existieron referencia, reloj e instrumentación compatibles con su definición. Cuando faltó alguno de esos elementos, el resultado se declaró no aplicable o no interpretable en lugar de convertir la ausencia de medición en un cero.

#### 17.5.2. Percepción sobre imágenes

La primera pregunta examinó la capacidad perceptiva de las combinaciones sobre un banco congelado de 6.477 imágenes y 55.165 anotaciones. El material se dividió en tres estratos independientes: obra curada (n = 147 imágenes), obra con mayor cobertura de chaleco (n = 1.330 imágenes) y una fuente con clase nativa de cabeza descubierta (n = 5.000 imágenes). El último aportó el 77 % del banco, 5.000 de 6.477 imágenes; por esa razón, el agregado se leyó siempre junto con el desglose por estrato.

La Tabla 62 muestra que la combinación gdino-tiny-560 alcanzó el mAP50 más alto en el agregado y en el núcleo curado, mientras que gdino-base-560 produjo el recall más alto para CR-01. Por lo tanto, el veredicto se formuló por combinación: el primer perfil se retuvo como configuración operativa mediante un criterio fijado antes de leer los resultados y el segundo como contraste especializado para cabeza descubierta y chaleco. No se estableció una jerarquía universal entre modelos.

**Tabla 62**

*Resultados de percepción por combinación en el banco congelado*

| **Combinación** | **mAP50 agregado (n = 6.477 imágenes)** | **mAP50 obra curada (n = 147 imágenes)** | **Recall CR-01 (n+ = 5.313)** | **Veredicto por combinación** |
| --- | --- | --- | --- | --- |
| gdino-tiny-560 | 0,551 | 0,503 | 0,308 | Retenida como perfil operativo por liderar el mAP50 en las dos escalas reportadas. |
| gdino-base-560 | 0,525 | 0,474 | 0,599 | Retenida como contraste de mayor cobertura para CR-01 y chaleco. |
| yoloe-26x | 0,442 | 0,405 | 0,000 | No apta para CR-01 bajo esta formulación: no recuperó cabeza descubierta. |

*Nota.* El denominador del agregado es el banco completo. El recall de CR-01 se informa sobre 5.313 positivos de referencia.

La especialización del perfil base también apareció en chaleco: registró AP 0,582 frente a 0,520 del perfil operativo en el estrato de mayor cobertura de esa clase (n = 1.330 imágenes). En los tres estratos, persona y casco se mantuvieron entre 0,70 y 0,89 de AP, mientras que chaleco quedó entre 0,55 y 0,58. La asimetría no dependió de una única fuente, sino que se sostuvo en los estratos de 147, 1.330 y 5.000 imágenes.

La familia YOLOE presentó una limitación distinta: sus cuatro variantes produjeron AP 0,000 para bare_head en el estrato con clase nativa de cabeza descubierta (n = 5.000 imágenes). Aunque la familia resultó adecuada para rutas de mayor velocidad, esa ceguera la volvió inservible para CR-01 en la configuración evaluada.

La extensibilidad semántica se ejerció con una clase nueva (n = 1) y requirió 0 corridas de entrenamiento. La incorporación se resolvió mediante un archivo de 48 líneas y 9 minutos de trabajo, y alcanzó AP@0,5 de 0,662 sobre 99 cajas de referencia. El costo reducido no eliminó la necesidad de validación semántica: sobre el mismo material (n = 99 cajas de referencia), un sinónimo produjo 0 detecciones, mientras que otra palabra generó 252 cajas y ninguna fue correcta.

#### 17.5.3. Estado por persona

El nivel intermedio evaluó si la evidencia perceptiva permitía determinar el estado observable de cada persona. La calibración se realizó sobre una mitad del material y las métricas sobre la otra, con IoU mayor o igual que 0,5. Se compararon E-IND, estrategia indirecta que reconstruye la ausencia desde evidencia positiva, y E-DIR, formulación directa retenida para el contraste.

**Tabla 63**

*Resultados de estado por persona*

| **Material y condición** | **Resultado E-IND** | **Contraste E-DIR** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Imágenes, CR-01 | F1 0,546 | F1 0,188 | n+ = 2.487 | Los intervalos de confianza no se solaparon. |
| Núcleo curado, CR-01 | F1 0,408 | F1 0,189 | n+ = 28 | La ventaja se conservó en el estrato objetivo. |
| Imágenes, CR-02 | F1 0,479 | F1 0,418 | n+ = 82 | Un único estrato; el resultado no cerró la condición. |
| Video de obra real, CR-01 | P 0,016 · R 0,467 · F1 0,031 | No corresponde a esta medición | n+ = 92 de 10.356 person-frames | La caída provino de precisión, no de recall. |
| Video de obra real, CR-02 | P 0,009 · R 0,318 · F1 0,018 | No corresponde a esta medición | n+ = 170 de 10.361 person-frames | La misma frontera de juzgabilidad dominó el resultado. |

*Nota.* La medición sobre imágenes utilizó calibración en una mitad y evaluación en la otra. La medición sobre video de obra real abarcó 17 clips y no incluyó el motor temporal.

La estrategia directa no se comportó como un detector estable del estado, sino como un recuperador de casos omitidos por la estrategia indirecta. Recuperó el 18,5 % de esos casos, equivalentes a 155 de 840, pero lo hizo a costa de precisión. Esa relación explica por qué la estrategia no se adoptó aunque aportara evidencia complementaria en un subconjunto.

La medición sobre 17 clips de obra real mostró un cambio de régimen. Para CR-01, el recall se mantuvo en 0,467 sobre 92 positivos dentro de 10.356 person-frames; para CR-02, fue 0,318 sobre 170 positivos dentro de 10.361 person-frames. El F1 cayó por la acumulación de falsos positivos sobre personas cuyo estado no podía determinarse visualmente. El evaluador excluyó del denominador 1.414 person-frames no juzgables para CR-01 y 1.409 para CR-02, pero cualquier predicción emitida sobre ellos se contabilizó como falso positivo.

#### 17.5.4. Alerta por episodio contra la referencia temporal humana

La alerta por episodio constituyó el resultado principal porque integra percepción, asociación, histéresis, estado temporal y registro de alerta. El bloque de rodaje guionado reunió 34 clips y 35 episodios de referencia (28 de CR-01 y 7 de CR-02); 34 episodios fueron evaluables y uno quedó censurado con causa. Cuatro clips fueron negativos. Todas las combinaciones de la tabla siguiente se ejecutaron sobre ese mismo material y cambiaron una sola variable por fila.

**Tabla 64**

*Alerta por episodio en el bloque de rodaje guionado*

| **Combinación** | **Recall** | **Precisión** | **F1** | **t_alert (ms)** | **SDR** | **FP en 4 negativos** | **Veredicto local** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Núcleo E-IND, escena | 0,824 | 0,757 | 0,789 | 5.327 | 0,698 | 0/4 | Línea de base de la plataforma. |
| Contraste base-560 | 0,735 | 0,676 | 0,704 | 4.899 | 0,819 | 0/4 | Mayor SDR, menor F1 que el perfil operativo. |
| E-DIR de extremo a extremo | 0,176 | 0,146 | 0,160 | 6.611 | 0,210 | 2/4 | Vetada por precisión. |
| E-HYB por disyunción | 0,353 | 0,255 | 0,296 | 6.956 | 0,738 | 2/4 | Ejecutada y refutada. |
| Núcleo E-IND, sujeto | 0,971 | 0,892 | 0,930 | 5.236 | 0,698 | 0/4 | La identidad elevó F1 sin cambiar las detecciones. |
| Vocabulario nativo bare_head | 0,382 | 0,371 | 0,377 | 3.919 | 0,940 | 3/4 | Alerta temprana, con mayor costo en falsos positivos. |

*Nota.* Las métricas temporales se calcularon sobre 34 episodios evaluables de 35 en el bloque de rodaje. Los falsos positivos se cuentan sobre los cuatro clips negativos y no incluyen re-alertas.

En el orden de las filas de la Tabla 64, los denominadores de t_alert fueron n = 28, n = 25, n = 6, n = 12, n = 33 y n = 13 episodios confirmados, respectivamente, dentro de los 34 episodios evaluables del bloque de rodaje.

La histéresis rescató evidencia intermitente. CR-02 confirmó 7 de 7 episodios, con recall 1,000 y SDR 0,281, aunque requirió t_alert de 8.572 ms frente a 4.314 ms para CR-01 (n = 23 episodios CR-01 confirmados del bloque de rodaje), dentro del conjunto de 34 episodios evaluables. La diferencia fue coherente con ventanas de confirmación de 7,0 s y 4,0 s, respectivamente: una detección sostenida sólo durante una fracción del episodio pudo producir una alerta correcta si acumuló evidencia suficiente en la ventana temporal.

La identidad temporal fue la capa con mayor aporte medido dentro del banco. Con las mismas detecciones, la granularidad por sujeto elevó el F1 de 0,789 a 0,930, una diferencia de 0,141 sobre los 34 episodios evaluables. En el escenario de mayor dificultad, el resultado pasó de 0,400 a 1,000 (2/5 con granularidad de escena frente a 5/5 con granularidad por sujeto; n = 5 episodios evaluables del bloque de rodaje). La mejora no provino del detector, sino de evitar que la evidencia de personas distintas se mezclara dentro de un mismo estado de escena.

El estrato de obra real no guionada se informó por separado. Comprendió 13 clips. Una revisión ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación por sobre-declarar estados que no resultaban observables; quedaron 2 episodios evaluables y 11 clips negativos. Ese denominador impidió ordenar granularidades. El resultado robusto del estrato fue, en cambio, la asimetría de falsos positivos: 26 con granularidad de escena frente a 323 con granularidad por sujeto sobre los mismos 11 clips negativos.

**Tabla 65**

*Falsos positivos en el estrato de obra real no guionada*

| **Granularidad** | **FP en 11 clips negativos** | **FP en 6 min 9,6 s de cumplimiento** | **Duración observada** | **FA/h derivadas** |
| --- | --- | --- | --- | --- |
| Escena | 26 | 3 | 0,1027 h | 29,2 |
| Sujeto | 323 | 190 | 0,1027 h | 1.850,8 |

*Nota.* Los conteos sobre 11 clips negativos describen el estrato completo. La tasa horaria se deriva del subconjunto continuo de 6 min 9,6 s y se presenta junto con su exposición de 0,1027 h; no constituye una cota operativa.

La exposición disponible estuvo dos órdenes de magnitud por debajo de la necesaria para sostener una cota. Por ello, las tasas de 29,2 y 1.850,8 falsas alarmas por hora se conservaron como magnitudes derivadas de 3 y 190 falsos positivos observados en 0,1027 h, y no como estimaciones de comportamiento horario estable.

#### 17.5.5. Tiempo real

La evaluación en vivo examinó qué parte del resultado temporal sobrevivía cuando la densidad de procesamiento descendía respecto de la evidencia disponible. El banco se representó a 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps en cuatro densidades medidas sobre el bloque de rodaje (n = 34 clips). El contraste mantuvo ese material y remuestreó los clips de manera pareada.

**Tabla 66**

*Resultados del camino en vivo por densidad, integridad y tramo temporal*

| **Eje** | **Condición o material** | **Resultado** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Densidad | Techo en vivo, aproximadamente 4,29 fps | Escena 0,794 · sujeto 0,866 | n = 34 episodios evaluables | La ganancia por identidad se conservó. |
| Densidad | Peor caso, aproximadamente 1,15 fps | Escena 0,646 · sujeto 0,742 | n = 34 episodios evaluables | La restricción redujo ambos resultados sin invertir el orden. |
| Identidad | Cuatro densidades medidas | Ganancias de F1 +0,141 · +0,072 · +0,137 · +0,096 | n = 4 densidades sobre 34 clips; remuestreo pareado por clip | El intervalo empírico excluyó el cero en las cuatro condiciones. |
| Integridad | Relectura frente a transmisión | Paridad byte a byte · 0 eventos perdidos | n = 6 corridas del rodaje | El transporte no alteró la evidencia. |
| Latencia | Detector de referencia | p50 14,7 · p95 31,8 ms | n = 20 unidades | Dentro del presupuesto de 50–250 ms. |
| Latencia | Detector open-vocabulary en vivo | p95 630–890 ms | n = 47, 93 y 55 unidades procesadas en las tres corridas en vivo | Fuera del presupuesto; la corrida lo declaró. |
| Captura | Antes del retiro de la unidad | 202–217 ms | medianas por corrida; n = 47 a 295 unidades procesadas en cada una de las seis corridas | No está incluida en el tramo anterior. |
| Alerta | CR-01 en vivo | 7 alertas: 4,1–4,6 s | n = 7 confirmaciones | Ventana: 4,0 s. |
| Alerta | CR-02 en vivo | 3 alertas: ≥ 7,1 s | n = 3 confirmaciones | Ventana: 7,0 s. |
| Canal | Bus de alertas a confirmación del canal | p95 64,534 ms · sostenido 102,025 ms | n = 460 · sostenido n = 104 | Tramo separado; no se suma a la alerta del sistema. |

*Nota.* Los percentiles pertenecen a tramos con relojes distintos y no se suman. El tramo desde el retiro de la unidad comienza en el dequeue, no en la captura de la escena.

La cobertura del episodio no se comparó entre cadencias porque depende de cuántas unidades sobreviven al muestreo. Tampoco se comparó la latencia agregada entre densidades sin controlar la supervivencia: los episodios que no alcanzan a confirmar desaparecen del promedio y lo sesgan. Entre los episodios supervivientes, el costo real de bajar la densidad fue de 0,7 a 1,3 s sobre ventanas de 4 a 7 s (n = 21, 20 y 16 episodios supervivientes comunes a 4,29, 2 y 1,15 fps, respectivamente).

La medición temporal confirmó además la separación entre captura, procesamiento y distribución. Los percentiles de procesamiento y la latencia de captura se consignan en la Tabla 66 con los denominadores que permanecen abiertos; corresponden a relojes distintos. En distribución, el p95 fue 64,534 ms sobre 460 entregas (n = 460) y el p95 sostenido fue 102,025 ms sobre 104 entregas (n = 104). Ambos valores describieron el intervalo desde el bus de alertas hasta la confirmación del canal, no la latencia completa de la plataforma.

#### 17.5.6. Caminos probados y no adoptados

Los caminos no adoptados se evaluaron contra criterios fijados antes de leer sus resultados. La estrategia directa quedó descartada por un veto de precisión: obtuvo 0,146, por debajo del umbral de 0,5, sobre los 34 episodios evaluables del rodaje. Su recall fue 0,176 y el F1 0,160; la brecha observada en estado por persona se amplió al atravesar el motor temporal.

La fusión híbrida por disyunción fue ejecutada y refutada. Sobre los mismos 34 episodios evaluables, el recall descendió de 0,824 para el núcleo indirecto a 0,353. La unión de evidencia no resultó monótona dentro del motor temporal: detecciones más tempranas desplazaron confirmaciones fuera de la ventana de referencia. La variante híbrida por conjunción no se ejecutó porque no podía medirse contra el banco sin romper la comparabilidad de las seis combinaciones. Una familia adicional de modelos fue integrada, evaluada y archivada durante la selección, sin incorporarse al perfil operativo.

La rama comparativa de ajuste fino se cerró como una curva de capacidad con criterios y expectativas registrados antes de cada evaluación. Sus cifras se mantuvieron separadas del núcleo sin entrenamiento. El banco de evaluación in-domain fue el banco congelado de 6.477 imágenes; el segundo tramo utilizó 2.946 imágenes de ajuste para 10,35 millones de parámetros.

**Tabla 67**

*Curva de capacidad de la rama comparativa de ajuste fino*

| **Punto o tramo** | **Resultado de ganancia** | **Retención y comportamiento** | **Veredicto** |
| --- | --- | --- | --- |
| Línea base sin ajuste | AP50 bare_head 0,0000 · recall CR-01 0,0002 | Referencia previa a los tramos entrenados. | Punto de partida. |
| Primer tramo entrenado | AP50 bare_head 0,0455 · recall CR-01 0,2089 | Quedó a 0,0045 del umbral y redujo person 11,62 %, con tope de 10 %. | NO-GO pre-registrado; checkpoint no adoptado. |
| Segundo tramo entrenado | AP50 bare_head 0,0909 | Detención temprana 16/60, mejor época 1; mAP50 protegido -43,4 %; retención open-vocabulary 0,4347 a 0,1247 (-71,3 %) · n = 5.000 imágenes del banco generalista. | NO-GO pre-registrado; checkpoint no adoptado. |
| Tramo adicional | No corresponde | Cerrado con causa técnica antes de producir una comparación interpretable. | Sin checkpoint y sin nuevo brazo contra el banco. |

*Nota.* Los puntos medidos pertenecen a una rama comparativa separada. Las métricas in-domain de la línea base y de los dos tramos entrenados se calcularon sobre el banco congelado (n = 6.477 imágenes); el segundo tramo utilizó 2.946 imágenes de ajuste para 10,35 millones de parámetros. El primer tramo agregó principalmente recall y el segundo, AP. No existe una combinación ajustada universalmente superior.

El segundo tramo duplicó el AP50 de cabeza descubierta respecto del primero, pero colapsó durante el entrenamiento y falló las dos retenciones. El patrón conjunto mostró que el límite no era capacidad de cómputo, sino estructura experimental: 2.946 imágenes de ajuste frente a 10,35 millones de parámetros. Los tramos tampoco ganaron por la misma vía, ya que el primero se destacó por recall y el segundo por AP. Ningún checkpoint se adoptó como modelo de servicio y los veredictos negativos se conservaron como resultados pre-registrados, no como trabajo pendiente.

#### 17.5.7. Lo no ejecutado y lo no implementado, con su justificación

Las condiciones de Nivel 2 y Nivel 3 no se implementaron en el núcleo evaluativo porque el material disponible no aportaba verdad de terreno del dominio ni evaluadores relacionales, zonales o de trayectoria que pudieran validarse. Incorporarlas habría producido capacidades sin medición defendible y habría confundido extensión arquitectónica con resultado experimental.

Las métricas formales de seguimiento multiobjeto tampoco se calcularon: faltó una referencia de identidad apta para ese propósito. Esta exclusión no alcanzó a la capacidad de identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta; la ganancia de F1 de 0,141 sobre 34 episodios evaluables del rodaje y su persistencia en cuatro densidades sobre los mismos 34 clips pertenecen a esa capacidad, no a una métrica MOT.

La preselección liviana en el dispositivo de captura fue implementada para la fuente propia y caracterizada mediante una comparación pareada. Descartó el 87 % de las unidades antes de abandonar el dispositivo (206 de 236 unidades vistas por la compuerta; la rama sin preselección procesó 277), pero permaneció deshabilitada en todas las corridas evaluativas. La exclusión fue deliberada: un filtro de fotogramas sin persona habría suprimido la evidencia sostenida que la medición de falsas alarmas debía observar y habría superpuesto el error de un detector auxiliar sobre la cadena evaluada.

Tampoco se sostuvo una cota operativa de falsas alarmas. Para hacerlo se requerían aproximadamente 3 h de cumplimiento anotado, mientras que la exposición continua disponible fue de 0,1027 h. La tasa horaria se reportó como derivación observacional, pero el material no habilitó una afirmación poblacional.

Finalmente, la comparación temporal directa entre una fuente en vivo y su reproducción desde clip se declaró no interpretable. Sin un ancla común entre el reloj de pared y el tiempo del medio, el emparejamiento habría mezclado desfases instrumentales con el comportamiento de la plataforma.

#### 17.5.8. Síntesis de la sección

La evaluación mostró que la detección sin entrenamiento sostuvo CR-01 con mayor consistencia, pero no cerró CR-02 al nivel de percepción. La selección del perfil operativo respondió al mAP50 por estrato, mientras que otras combinaciones ofrecieron mayor recall o mayor SDR; por ello, los veredictos se mantuvieron locales y no se formuló una superioridad universal entre modelos.

El aporte cuantitativo principal provino de la plataforma alrededor del detector. Sobre 34 episodios evaluables del bloque de rodaje, la granularidad por sujeto elevó el F1 de 0,789 a 0,930 con las mismas detecciones y mantuvo una ganancia positiva en cuatro densidades sobre los mismos 34 clips. La histéresis, a su vez, permitió confirmar los 7 episodios de CR-02 (n = 7) aun con SDR 0,281, a costa de una latencia coherente con su ventana temporal.

La limitación dominante apareció en la obra real no guionada: el sistema continuó recuperando condiciones, pero produjo falsos positivos sobre estados no juzgables. La exposición de 0,1027 h permitió reportar conteos y tasas derivadas, no una cota operativa. Los caminos descartados y las capacidades no ejecutadas quedaron asociados a criterios explícitos de precisión, comparabilidad, evaluabilidad o referencia disponible. Estos resultados deben leerse junto con las limitaciones L1-L8 declaradas; su interpretación respecto de la factibilidad de la plataforma se desarrolla en las conclusiones.
