# Pases 5, 5b, 5c y 5d — acta de las cinco secciones (2026-09-07)

> **Qué es.** Constancia de lo que se cambió en las cinco secciones del informe durante la jornada
> del 2026-09-07, sobre las versiones que el usuario bajó de Google Docs el 09-06. Este documento
> se reescribió al cerrar la jornada: reemplaza a sus versiones parciales, que quedaron desfasadas
> por las dos correcciones de rumbo del §1. Los pases **5b** (§10), **5c** (§11) y **5d** (§12, la
> revisión completa), incrementales y posteriores, se agregaron a esta misma acta porque en
> `desarrollando/` queda un solo documento de ajustes.
>
> **Condición de entrega, fijada por el usuario:** *todo* entra como **sugerencias y comentarios**.
> Nada se aplicó en limpio, y **rechazar todas las sugerencias devuelve el documento de partida** en
> las cinco secciones, verificado en el §7.
>
> Diagnóstico de origen: [`archivado/lectura-transversal-etapas-1-5-2026-09-07.md`](lectura-transversal-etapas-1-5-2026-09-07.md) §8.

---

## 1. Las vueltas de la jornada

La entrega no salió de una sola pasada. El usuario revisó y corrigió el rumbo varias veces, y cada
corrección mejoró el resultado.

| Vuelta | Qué decidió el usuario | Efecto |
|---|---|---|
| **Primera** | Cuatro decisiones firmadas, todas en la recomendación: **D5-A** restaurar las ocho limitaciones tal como estaban · **D5-B** tocar §17.1 con sus tres correcciones hacia atrás · **D5-C** alcance completo en §15/§16 · **D5-D** insertar las figuras por XML | Se aplicó la lista de trabajo entera y se entregaron las cinco secciones |
| **Segunda** | **Las dos figuras de datos de §17.5 se descartan.** «No quiero mantener ninguno de esos gráficos; lo que se pierde sobre la poca luz lo agregamos en el desarrollo» | La curva de densidad volvió a la Tabla 64 y la frontera de juzgabilidad pasó a prosa, con más precisión que la figura |
| **Tercera** | Cubrir también la condición de chaleco con un fotograma propio | Se produjo, se auditó y **se descartó con causa**: ningún clip del rodaje da una imagen limpia (§6) |
| **Cuarta** | Los dos comentarios que el usuario dejó sobre la Tabla 65: falta la configuración del entrenamiento, y duda de si va en §17.5 o en §17.4 | **Pase 5b**, incremental sobre las versiones vigentes: la configuración entró en §17.4.7 y §17.5 amplió su remisión (§10) |
| **Quinta** | «La fila de pruebas automatizadas de la Tabla 59 no aporta valor como está; hay que ajustarla o borrarla» | **Pase 5c**: se borra, sin reemplazarla por otra cifra. El conteo no resistía el detalle y ya había envejecido (§11) |
| **Sexta** | «Ejecutá una revisión completa; asegurate de que estos ajustes tengan sentido y hayan quedado coherentes entre ellos y con la plataforma» | **Pase 5d**: cinco auditorías cruzadas; se corrigieron 13 contradicciones de §17.5 contra los índices, 9 imprecisiones de §17.4 contra el código y la coherencia protocolo↔resultados; 20 decisiones quedan listadas (§12) |

---

## 2. Cómo quedó cada documento

| Sección | Versión | Inserciones | Borrados | Formato | Comentarios | Figuras |
|---|---|---|---|---|---|---|
| §15 + §16 | v1.2 → **v1.3** | 8 | 13 | 1 estilo de encabezado | 4 míos, 11 previos intactos | — |
| §17.1 | v1.16 → **v1.17** | 2 | 0 | — | 2 míos | — |
| §17.3 | v1.8 → **v1.9** | 5 | 4 | — | 3 míos | las 4 previas, intactas |
| §17.4 | v1.8 → **v1.9** | 37 | 20 | — | 8 míos, 6 previos intactos | **4.5 rehecha** |
| §17.5 | v1.5 → **v1.6** | 53 | 29 | — | 9 míos | **4.6, el fotograma** |

Ningún comentario preexistente se resolvió ni se borró: viajan con su ancla, y cuándo se cierran lo
decide el usuario.

El pase 5b llevó después **§17.4 a la v1.10** (tres párrafos nuevos, tres comentarios) y **§17.5 a la
v1.7** (una remisión ampliada, dos comentarios de respuesta). El 5c llevó **§17.4 a la v1.11** (una fila
de tabla borrada, una cláusula en la nota, dos comentarios). El 5d llevó **§17.4 a la v1.12, §17.5 a
la v1.8, §17.3 a la v1.10 y §17.1 a la v1.18**. El detalle está en los §10, §11 y §12.

---

## 3. Qué se cambió, sección por sección

### §17.5 Evaluación y validación → v1.6

Es la que más recibió: 14 reemplazos de tramo, 6 agregados de cierre, 7 párrafos nuevos, 2 filas de
tabla, 5 correcciones de celda y 1 figura.

**Bloqueantes que cierra**

- **Las ocho limitaciones vuelven** al final de 17.5.7, con el texto exacto que tenían antes de la
  edición del 09-06. Es lo que piden `AJ-5.05` y la decisión D-H.
- **«Medida sobre 23 episodios confirmados» era un cruce.** El 23 es la cantidad de clips con la
  condición de casco confirmada en la campaña de línea de base, no el denominador de la media.
  Reconstruido desde el artefacto: la media de 4.314 ms se promedia sobre **21** clips y la de
  8.572 ms sobre **7**.
- **La figura que faltaba entró**, el fotograma con la alerta confirmada, como 4.6.

**Coherencia entre la columna de recall y la estrategia adoptada**

La columna que la Tabla 61 llamaba «Recall CR-01» **no mide la capacidad del núcleo**. Su evaluador
cuenta sólo detecciones de cabeza descubierta, de modo que mide la formulación **directa**, que es
la que el proyecto no adoptó. Con ese encabezado la tabla usaba dos varas: el 0,000 descalificaba a
la familia YOLOE «para CR-01» mientras el 0,308 del perfil operativo no lo descalificaba a él.

Se corrigió en cuatro lugares. El encabezado dice ahora **recall de CR-01 por evidencia directa**; la
nota aclara que el núcleo opera con la vía indirecta y que su capacidad no se lee en esa columna; y
el veredicto de YOLOE deja de decir «no apta para CR-01»; y la tabla del ajuste fino, que usa la
misma métrica, la nombra igual, de modo que las dos se leen con la misma vara. Verificado sobre los
artefactos: en las
dos clases que la vía indirecta necesita, esa familia mide persona 0,785 y casco 0,715 contra 0,770
y 0,707 del perfil operativo, así que para la condición por vía indirecta no es inferior. **Lo que
sí la deja fuera del núcleo es el chaleco**, con AP 0,182 en obra curada frente a 0,520, y el mAP50
agregado. El descarte sigue siendo válido; lo que cambia es la razón que lo sostiene.

El alcance de la corrección se revisó: **no hay que re-evaluar nada**. Ninguna cifra cambia y
ninguna decisión se invierte, porque el campeón se eligió por mAP50 y el descarte de YOLOE se
sostiene por chaleco. Lo que cambia es la razón publicada. Fuera del informe se corrigieron dos
cosas, ambas de documentación y sin efecto sobre resultados: el docstring del evaluador, que
prometía contemplar la ausencia de casco y nunca lo hizo, y el índice del banco de imágenes, que
ahora fija qué mide esa columna antes de las tres tablas que la usan y precisa la celda de YOLOE.

**Un dato que conviene tener presente:** el estado por persona **nunca se corrió con YOLOE**, de
modo que no existe medición de su rendimiento en la condición por la vía que el núcleo usa. Por eso
el veredicto nuevo no afirma que sería apta: dice qué la deja fuera, que es lo que sí está medido.

**Precisión que sólo apareció yendo al artefacto**

La columna de latencia de la Tabla 63 declara los episodios confirmados, mientras que la media se
promedia **por clip** con alerta confirmada. Son números distintos cuando un clip contiene las dos
condiciones: 28 contra 26 en la línea de base, y 33 contra 29 con granularidad por sujeto. La nota
de la tabla lo dice ahora.

**Coherencia con el protocolo**

- Cada pregunta declara a qué escenario del protocolo pertenece, que §17.5 no decía.
- Se ata el vocabulario de la sección al del marco de métricas, incluida la equivalencia de la
  cobertura del episodio.
- Párrafo nuevo con el **estado de las métricas adoptadas y no computadas**, que el marco exige
  declarar: tiempo hasta la primera detección, precisión media sobre el rango de umbrales,
  percentil 99, memoria del acelerador y benchmarks de seguimiento.
- La calibración sobre una mitad del banco se declara predeclarada y disjunta, para que no choque
  con la regla de congelamiento.

**Un comentario que se quitó**

Había uno sobre el desglose por estrato de la Tabla 61 que decía que el índice no publica un mAP50
por estrato y que, si se lo quisiera, habría que recalcularlo. Estaba mal fundado: la razón no es de
disponibilidad sino de comparabilidad. Cada estrato anota un conjunto de clases distinto, uno sin
chaleco y otro sin cabeza descubierta, de modo que un mAP50 por estrato promediaría sobre bases
diferentes y no sería comparable ni entre estratos ni con el agregado. La regla de reportar por
estrato ya se cumple en el párrafo que informa AP por clase y estrato. El comentario ofrecía además
una opción que no conviene tomar, así que se quitó sin reemplazo.

**Exactitud**

- El denominador del recall queda fechado, con la corrección posterior a 5.308 declarada.
- La descomposición del banco temporal se hace explícita: 34 clips de rodaje y 13 de obra real.
- Los dos materiales de obra real, el de 17 clips y el estrato de 13, dejan de confundirse.
- La familia de modelos archivada durante la selección recibe su causa, sin citar el banco anterior
  al congelado.
- «Frontera de de juicio» vuelve a ser «frontera de juzgabilidad»; se quita una oración duplicada;
  se corrige «no tuvo su dependencia» y un sujeto elidido; «dos órdenes de magnitud» pasa a «casi
  treinta veces», que es lo que dicen los números.
- Las llamadas de las Tablas 62 y 63, que la edición previa había borrado, se restituyen.

**Lo que reemplazó a las dos figuras descartadas**

- *Calidad contra densidad*: la Tabla 64 suma las dos densidades que le faltaban y queda con la
  serie completa, de 30 a 1,15 cuadros por segundo. El cierre de 17.5.5 agrega la lectura de los
  dos regímenes y repite que las diferencias menores que 0,02 no se leen como orden.
- *Frontera de juzgabilidad*: párrafo nuevo al final de 17.5.3 con los tres ejes y sus cifras. La
  asociación del chaleco pasa de alrededor del 10 % a entre 63 y 73 % con la escala en clips
  diurnos, se sostuvo entre 96 y 100 % en el rodaje, y **en el clip nocturno queda entre 6 y 13 %
  en las mismas bandas**. Sigue el contraejemplo de oclusión y el de juzgabilidad humana.

### §17.4 Implementación → v1.9

**Bloqueante**

La **Figura 4.5** estaba incrustada en medio de la última oración de 17.4.1, sin epígrafe, y con la
imagen del 23-08 que deja al módulo de distribución fuera del orden de arranque. Ahora sale de la
oración, recupera epígrafe y título, el párrafo que la describía pasa a ser su nota, la imagen vieja
queda marcada como borrada y entra la vista de procesos vigente.

**Concreción técnica: la observación del tutor**

Al retomar los dos comentarios sobre los DTO se revisó qué pedía el tutor técnico y qué había
llegado al informe. La ficha que registró esa observación pide cuatro piezas. **Estaban dos y media**:
la tabla de correspondencia entre cada contrato y su materialización, las interfaces de los tres
servicios, y el evento de percepción en JSON, aunque con un ejemplo distinto del especificado.
**Faltaban la clase y el contrato de salida**, y el texto para las dos estaba redactado y verificado
desde el 22-08 en el material de la Etapa 3, sin haberse pegado nunca.

El pase agrega tres fragmentos en 17.4.2, todos transcripción literal de artefactos de corrida
verificados contra el repositorio:

- **El evento de percepción se reemplaza por el que la ficha especificaba**, el de la unidad en la
  que la condición se confirma. Trae tres detecciones e incluye un casco que **no** suprime la
  condición porque cae fuera de la región cefálica del sujeto, que es la lectura que la ficha pedía
  conservar. El anterior era el primer cuadro de otra corrida, con dos detecciones y sin ese detalle.
- **La misma estructura, declarada como modelo de datos con tipos explícitos.** Es la tercera forma
  que el tutor ofrecía, «o simplemente una clase», y hace visible el mecanismo del que su pedido más
  profundo dependía: el campo de identidad entre fotogramas aparece como opcional y sin valor, que
  es como un dato todavía no producido se incorpora sin cambiar la versión del esquema.
- **El contrato de salida, la alerta interna, en JSON.** Sobre el mismo clip y la misma unidad que
  el evento, de modo que los dos se leen juntos, y con los hitos que permiten verificar la ventana
  de confirmación: primera evidencia a los 3.633 ms y confirmación a los 7.633.

Lo que el informe ya tenía y responde al resto de la observación: la frase que el tutor citó, la de
las «denominaciones contractuales preliminares», **fue eliminada** en un pase anterior; §17.4.8
desarrolla la regla de evolución aditiva del evento; y la evidencia de qué funciona y cómo se mide
está en la tabla de verificación de esta sección y en §17.5 entera.

**Correcciones de contenido**

- «Cuarto componente funcional» contradecía a §17.3.7, que dice que la distribución no es un tercer
  plano ni un cuarto rol. Corregido.
- El **perfil operativo se nombra en 17.4.4**, donde se declara su configuración; antes aparecía por
  primera vez en la Tabla 61 de §17.5.
- **La causa del tercer tramo de ajuste fino se corrigió contra las actas.** No se cerró porque el
  corpus comparta fuentes con el banco, que es la regla de partición y sí se cumplió, sino porque
  sin una línea base sana de esa familia la diferencia no era interpretable.
- La Tabla 56 usaba dos nombres de contrato que el diseño no tiene. Quedan alineados con §17.3.
- El despliegue integral pasa de «instancia» a «define»: está definido y validado, y nunca se
  construyó.
- La cifra de pruebas queda fechada en agosto de 2026, para que no envejezca en silencio.
- El nivel de calidad de servicio de la entrega queda explícito.
- La **evidencia visual controlada** recibe su estado: era la única capacidad de la Tabla 39 sin
  destino en esta sección.
- Se declara la salvedad de la fuente de ajuste que aporta un estrato al banco, y la regla de
  partición se dice con precisión.
- Restituidas las llamadas de las Tablas 57 y 59; unificados «suscripto» y «guion».

### §17.1 Consolidación metodológica → v1.17

Dos precisiones hacia atrás. No son estilo: son reglas que §17.1 escribe y que la ejecución no
cumplió tal como estaban formuladas. Una tercera, sobre la regla de fuente única, **se retiró**: el
protocolo queda como estaba y la desviación se declara en §17.4.7 (§4).

1. **Congelamiento del banco.** La Tabla 26 prohibía usarlo en calibración. La medición de estado
   por persona calibró umbrales sobre una mitad y midió sobre la otra. La fila admite esa
   calibración, que no modifica el modelo, con la condición de que las mitades se predeclaren y sean
   disjuntas.
2. **Banco temporal.** La estrategia de datos cubría cuatro fuentes de imágenes y dos benchmarks de
   seguimiento, y no fijaba el banco temporal propio, que es el material del resultado principal. Se
   agrega como decisión, sin cifras, para no romper el no-anacronismo de la sección.

### §17.3 Diseño arquitectónico → v1.9

- Dos ediciones del 09-06 habían cambiado el sentido: «artefactos inatribuibles» pasó a «sin
  atributos», y «la frontera que esa elección fija» perdió el relativo. Restituidas.
- Vuelven **tres notas de interpretación** que desaparecieron sin figura ni tabla que las
  absorbiera, ahora como oración final del párrafo que introduce cada tabla, que es el estilo que la
  edición adoptó. Si el borrado fue deliberado, rechazarlas las quita de nuevo.
- Dos promesas hacia §17.4 se ajustan a lo que esa sección entrega, que es en conjunto y no ítem por
  ítem.

### §15 y §16 Estado del arte y Marco teórico → v1.3

- **«16. Marco teórico» recupera su estilo de encabezado.** Lo había perdido en la v1.2: sin estilo
  desaparece del índice automático y de la numeración de campos, aunque a la vista parezca un
  título. Con esto la sección **pasa el verificador mecánico por primera vez**.
- **La oración rota de §16.3.4**, que hacía que la primera formulación absorbiera a la segunda,
  queda reparada. Es el fundamento de las dos estrategias que §17.1 y §17.5 comparan.
- Se propone **borrar el párrafo y el marcador de la inscripción**, cerrando D-E1-11: el espejo de
  §17.1 ya se había borrado, así que §16 prometía un recaudo que §17.1 no documenta. La norma no
  desaparece del marco, porque el párrafo anterior la describe con sus tres ejes.
- §16.5.2 declara el **origen instrumentado** de la métrica de latencia. La ecuación queda como
  marco general, pero el protocolo la mide desde el retiro de la unidad y reporta la captura aparte.
  Sin esa oración, §16 define la métrica de un modo y §17.1 y §17.5 la miden de otro.
- La nota de la Tabla 7 recupera su relativo, y se corrigen los cinco typos que venían del 09-01.

---

## 4. Las cinco confirmaciones, todas cerradas

Cinco comentarios piden una respuesta que no está en los artefactos:

Eran cinco. **Tres se resolvieron con evidencia** y las **dos restantes las decidió el usuario el
mismo día**, de modo que no queda ninguna abierta.

### Las dos que decidió el usuario, el 2026-09-07

**La regla de fuente única no se toca.** La primera versión de este pase la precisaba para que
abarcara lo que la ejecución hizo. Se decidió lo contrario, y §17.1 queda como estaba. La regla era
deliberada, porque el propio texto declara que es más restrictiva que la separación de imágenes, de
modo que precisarla al cerrar habría sido acomodar el protocolo a los resultados, en contra de la
pre-registración que sostiene el resto del trabajo. **La desviación se declara en §17.4.7**, con el
mismo patrón que el informe ya usa dos párrafos antes para la desviación del rango de tamaño: se
enuncia contra el protocolo, con su causa y sus controles, y el protocolo queda intacto. El párrafo
nuevo dice que la partición se apartó en ese punto, que excluir esa fuente habría reducido el
conjunto de ajuste de 2.946 a 743 imágenes, y que la desviación se admitió con particiones disjuntas
y deduplicación perceptual verificada en cero.

**Las ocho limitaciones se quedan en §17.5.** Lo pidieron `AJ-5.05` y la decisión D-H, §18 todavía no
existe, y las salvedades acotan los resultados en el punto donde se leen. Nada impide que el cierre
retome después las que sean del trabajo entero, que son otras.

### Las tres que se resolvieron verificando

**El borrado de las tres notas de §17.3 fue deliberado.** De diecisiete notas, la edición del 09-06
conservó nueve y borró ocho. Las cuatro de figura se absorbieron en el párrafo previo, y de las
cuatro restantes el patrón es claro: **quedaron las que describen su tabla y se fueron las que
advertían cómo no leerla**. De las tres que este pase quería restituir, dos ya están dichas en otro
lugar de la sección, la vista que «no prescribe una distribución obligatoria» y la tabla de
capacidades que dice que las métricas de seguimiento no condicionan al núcleo. **Se retiraron esas
dos restauraciones**; queda sólo la que no tiene equivalente en ningún documento, la que impide leer
las métricas como extrapolables entre unidades desplegables.

**La evidencia visual controlada está implementada, y la redacción anterior era falsa.** El esquema
de configuración tiene la opción de conservar una previsualización por unidad procesada, con tope, y
un video anotado de la corrida. Las dos vienen habilitadas por defecto, y **las campañas del banco
las declaran apagadas**, con cero imágenes en sus directorios, mientras que otras corridas del
repositorio sí las conservan. El párrafo se reescribió: la capacidad existe y la política de
minimización se ejerció, que es mejor noticia que la que decía el texto anterior.

**La partición de calibración está registrada con su semilla.** El artefacto de la campaña la trae,
y es la misma en la corrida principal y en su réplica, de modo que la partición es determinista y
previa a los resultados. El texto lo dice ahora en esos términos, que son verificables, en vez de
afirmar que se fijó antes de calibrar.

---

## 5. Figuras: qué entró, qué salió y por qué

| Figura | Destino | Estado |
|---|---|---|
| Vista de procesos | §17.4.1, como 4.5 | **Entró**, reemplazando la imagen del 23-08 |
| Fotograma con alerta confirmada | §17.5.4, como 4.6 | **Entró** |
| Calidad contra densidad | §17.5.5 | **Descartada** en la segunda vuelta |
| Frontera de juzgabilidad | §17.5.3 | **Descartada** en la segunda vuelta |
| Fotograma de la condición de chaleco | §17.5.4 | **Descartada** en la tercera vuelta (§6) |

Las dos que entraron coinciden por huella criptográfica con las de `informe/figuras/` y conservan su
proporción exacta a 16 cm de ancho, el ancho de diseño.

**Por qué se descartaron las dos de datos.** Además del argumento operativo, que una figura no se
puede corregir desde Google Docs, cada una tenía su motivo propio:

- *Calidad contra densidad* era una tabla de cuatro filas dibujada como curva, con seis de sus ocho
  valores ya en la Tabla 64, y su propio pie tenía que advertir que las diferencias menores que dos
  centésimas no se leen como orden, que es justo lo que un gráfico de líneas invita a hacer.
- *Frontera de juzgabilidad* mezclaba dos cosas distintas. Juzgabilidad es si el anotador humano
  puede determinar el estado, y lo que graficaba era rendimiento del sistema. Su panel inferior
  tomaba además cuatro clips de una foto anterior al cierre de la campaña de diecisiete, omitía un
  clip con dato medido y dejaba afuera la variable que define el fenómeno.

Ninguna de las dos se archiva: se siguen produciendo y están publicadas en el repositorio público,
de modo que cambia su destino y no su validez. Queda anotado en el README de figuras.

---

## 6. Un fotograma de la condición de chaleco: intentado y descartado

Se produjo con el mismo pipeline que la 4.6, sobre el único escenario del rodaje donde las dos
condiciones se confirman sobre el mismo sujeto, y **el resultado fue inservible**: sobre la espalda
del actor, que viste ropa oscura, el detector dibuja una caja de chaleco, de modo que la imagen
muestra una alerta de persona sin chaleco junto a una caja de chaleco sobre esa misma persona.

No es del clip. En los **siete clips del rodaje** con episodio de esa condición, el detector propone
un chaleco en el **70 % al 96 % de los cuadros del episodio**, con el anotador declarando que no lo
hay. El fenómeno ya estaba documentado y no es un hallazgo de este pase.

Lo que sostiene el acierto no es que el detector no vea un chaleco, sino la geometría de la
asociación, que exige que el centro de la caja caiga en la franja del torso, y la ventana de
resolución de tres segundos, que impide que un falso intermitente apague la condición. En el cuadro
renderizado el centro caía **dentro** de la región por siete décimas de píxel y el patrón seguía
sostenido por la histéresis. Todo correcto, y todo imposible de contar en un epígrafe.

**Ningún clip de esa condición da un fotograma limpio.** Si alguna vez se quiere evidencia visual de
ella, lo honesto es que ilustre el falso positivo y no el acierto. La constancia del intento quedó
en el README de los videos de defensa; la entrada del pipeline se revirtió y el video se borró.

---

## 7. Compuerta

| Sección | Rechazar todo devuelve el original | Paquete íntegro | Verificador sobre el aceptado |
|---|---|---|---|
| §15 + §16 v1.3 | ✓ | ✓ | **OK, ningún problema duro** (antes fallaba por el título sin estilo) |
| §17.1 v1.17 | ✓ | ✓ | OK |
| §17.3 v1.9 | ✓ | ✓ | OK |
| §17.4 v1.9 | ✓ | ✓ | sólo el aviso de sección suelta |
| §17.5 v1.6 | ✓ | ✓ | sólo el aviso de sección suelta |
| §17.4 **v1.10** (pase 5b) | ✓ devuelve la v1.8 | ✓ | sólo el aviso de sección suelta y el marcador de procedencia, los dos previos |
| §17.5 **v1.7** (pase 5b) | ✓ devuelve la v1.5 | ✓ | sólo el aviso de sección suelta |
| §17.4 **v1.11** (pase 5c) | ✓ devuelve la v1.8, con sus 264 párrafos y 5 tablas | ✓ | sólo el aviso de sección suelta y el marcador de procedencia |
| **v1.12 · v1.8 · v1.10 · v1.18** (pase 5d) | ✓ las cuatro devuelven su base del pase 5 | ✓ | sólo lo previo; §17.3 y §17.1 OK |

En las dos versiones del pase 5b, rechazar todo devuelve la base del pase 5, porque las sugerencias
de ese pase siguen sin aceptar y las del 6 se apilan encima. Ningún comentario se perdió al apilar,
verificado uno por uno: §17.4 pasó de 14 a 17 y §17.5 de 11 a 13, y el 5c llevó §17.4 de 17 a 19.

Además: los cinco pases se repiten desde las bases archivadas con **resultado idéntico parte por
parte** —el 6 también—, 135 enlaces del informe sin ninguno roto, kit vigente y 63 pruebas en verde.

---

## 8. Herramientas

| Archivo | Para qué |
|---|---|
| `herramientas/pase_docx.py` | Motor de pases con edición **quirúrgica**: marca como borrado sólo el tramo que cambia, no el párrafo entero. Agrega comentarios creando `comments.xml` cuando el documento no lo tiene, inserta imágenes y filas de tabla como sugerencia, y repara estilos de encabezado dejando `pPrChange` |
| `herramientas/rechazar_cambios.py` | Inverso de aceptar. Sostiene la propiedad que hace segura la entrega |
| `herramientas/verificar_paquete.py` | Integridad OPC. Existe por dos defectos reales de esta jornada: partes generadas y no escritas en el zip, e imágenes sin su tipo de contenido. Word abre esos archivos como dañados y la extracción a markdown no lo nota |
| `herramientas/reparar_enlaces.py` | Tras un archivado, resuelve cada enlace roto por nombre y reescribe la ruta relativa. Reparó 18 de una pasada |
| `herramientas/pase5_*.py` | Un guion por sección, con el enunciado de cada cambio junto al texto que inserta o borra |
| `herramientas/pase5b_config_entrenamiento.py` | El pase incremental del §10. Acepta `--origen-17-4` y `--origen-17-5`, así que los mismos cambios se pueden reaplicar sobre una bajada nueva de Google Docs en vez de re-correr un pase desde la base |
| `herramientas/pase5c_tabla59.py` | El pase incremental del §11, con `--origen`. Estrenó `borrar_fila` y `comentario_en_celda` en el motor |
| `herramientas/pase5d_revision.py` | El pase de la revisión completa del §12: un guion, cuatro documentos, `--origen-*` y `--solo` |

Los once guiones de los pases 4 y del pase 6 de §17.1 pasaron a `herramientas/archivado/`. El pase
nuevo se llama **5b** y no 6 justamente para no chocar con aquel. Los seis vigentes llevan
arriba la advertencia de no re-ejecutarlos sobre el documento vigente, que es el resguardo que dejó
el incidente del §10.

---

## 9. Archivado de la jornada

Cada carpeta tiene su `00-que-hay-aca.md` con el criterio: entra lo **superado**, se queda lo que es
constancia única o herramienta viva.

| Dónde | Qué |
|---|---|
| `desarrollando/archivado/` | Las **cinco bases del pase 5**, los dos análisis previos a los pases 4, las tres actas del pase 4 y la lectura transversal que originó este pase. Después, las **dos bases del pase 5b** (§17.4 v1.9 y la §17.5 v1.6 que el usuario bajó con sus comentarios) y la **base del pase 5c** (§17.4 v1.10). Después, las **cuatro bases del pase 5d**: §17.4 v1.11, §17.5 v1.7, §17.3 v1.9 y §17.1 v1.17 |
| `entregable/archivado/` | `96b`, `96c` y `96d`, superados por `90f` y `90d`; el capítulo suelto de Etapa 3; la variante `-sin-etapa3` del informe v1.1; y los dos borradores ya pegados |
| `herramientas/archivado/` | Los once guiones de los pases 4 y del pase 6 de §17.1 |

Tres archivos de `desarrollando/archivado/` llevaban nombre ambiguo y se precisaron, porque había
**dos §17.4 v1.9 y dos §17.5 v1.6 distintas** conviviendo. Ahora el paréntesis dice cuál es cuál: la
primera entrega del pase 5 frente a la definitiva, y la entrega del pase 5 frente a la bajada del
usuario. Son documentos con el mismo número de versión y contenido diferente, así que sin eso no hay
manera de saber cuál es la base de qué.

**En `desarrollando/` queda un solo documento de ajustes, este**, más los tres mapas de secciones,
que no son documentos de un pase sino la herramienta con la que se traduce cualquier unidad de
corrección anterior a una renumeración.

---

## 10. Pase 5b: la configuración del entrenamiento

El usuario dejó dos comentarios sobre la Tabla 65 de §17.5, la curva de capacidad del ajuste fino:
«dejar clara cómo se configuró el entrenamiento, épocas, etc.» y «ver si esto corresponde a este
documento o al de implementación». Los dos se responden juntos, porque el segundo decide dónde va lo
que pide el primero.

**Decisión, firmada por el usuario:** la configuración va a **§17.4.7**. Es donde vive el «cómo está
hecho», y esa subsección ya declara el conjunto de ajuste, su regla de partición y la desviación de
rango, así que el perfil de entrenamiento completa ese hilo en vez de abrir uno nuevo. **§17.5 se
queda con resultados y veredictos** y amplía su remisión. Es la misma separación que las dos
secciones sostienen en todo lo demás.

### Qué se escribió

En §17.4.7, tres párrafos nuevos después del de la desviación:

1. **El perfil común a los dos tramos**, que la comparación por única variable obliga a mantener
   idéntico: 640 píxeles de lado, lotes de ocho, semilla fija y ejecución determinista, la partición
   de 2.946 imágenes de ajuste y 483 de validación, y el punto de control elegido por mejor precisión
   media sobre las cuatro clases de validación en lugar del de la última época.
2. **El régimen de época y de optimización**, que es lo único que difiere. El primer tramo recorrió
   10 épocas completas con selección automática de optimizador, y su detención temprana quedó
   inoperante porque la paciencia configurada superaba ese techo. El segundo fijó techo de 60 y
   detención tras 15 sin mejora —ambos registrados antes de ver resultado alguno—, con optimizador
   declarado de forma explícita, descenso de gradiente estocástico, tasa inicial 0,01, momento 0,937
   y tres épocas de calentamiento. Se detuvo en la época 16 con la mejor época en la primera, que es
   el dato sobre el que se apoya la lectura de colapso durante el entrenamiento.
3. **Por qué el segundo tramo declara el optimizador** en vez de usar el modo automático. Ese modo
   deriva la tasa de aprendizaje del número de clases y no del alcance entrenable, de modo que le
   asignaba la misma a un tramo de 3.096 parámetros y a otro de 10,35 millones. Es un hallazgo del
   proceso, no un resultado del banco. El comentario que lo acompaña ofrece borrarlo si al usuario le
   parece detalle de más; los otros dos no dependen de él.

En §17.5.6, el párrafo que cierra la Tabla 65 ya remitía a §17.4.7 por la composición del conjunto y
su regla de partición. Ahora nombra también la configuración de entrenamiento. Es un reemplazo de
tramo, no un párrafo nuevo. Los dos comentarios de respuesta quedan anclados sobre el epígrafe de la
tabla, junto a los del usuario, y el primero ofrece mover la configuración a §17.5 si prefiere.

**Procedencia de cada cifra.** Los perfiles de los dos tramos y la configuración efectiva que
registró cada corrida, en el repositorio de experimentación. No hay ningún número que no esté en un
artefacto.

### El incidente que dejó el resguardo

Al preparar este pase se sobrescribió el §17.5 que el usuario había bajado de Google Docs con sus
comentarios, por re-ejecutar el guion del pase 5, que parte de la base archivada. Se recuperó porque
existía una copia de un minuto antes. De ahí salieron tres cambios permanentes:

- El motor **respalda el destino antes de escribirlo** cuando el contenido difiere, y avisa si el
  archivo traía comentarios de otros autores.
- Los guiones de pase llevan arriba **«no re-ejecutar sobre el documento vigente»**.
- Todo cambio nuevo se aplica con un **pase incremental que toma el archivo del usuario como
  origen**. Por eso este guion acepta `--origen-17-4` y `--origen-17-5`.

### Resolver un comentario en Google Docs lo borra del archivo

La alarma inicial fue equivocada y conviene dejarlo escrito. Al comparar la entrega del pase 5 con la
bajada del usuario, §17.5 tenía **9 comentarios míos en la entrega y 8 en la bajada**. No se perdió
ninguno: el usuario resolvió uno, y **resolver en Google Docs elimina el comentario de la
exportación**, sin dejarlo marcado como resuelto. Verificado sobre el archivo, donde los once
comentarios que quedan figuran todos como no resueltos.

La consecuencia operativa importa más que el episodio: **mientras el usuario trabaja en Google Docs,
el disco no es la fuente de verdad**. Regenerar un documento desde su base archivada revive los
comentarios que él ya cerró.

### Una salvedad sobre §17.4

El §17.4 en disco no muestra rastro de haber vuelto de Google Docs: sus seis comentarios previos son
exactamente los de la base del pase 5, así que nada se perdió. Pero eso también significa que **si el
usuario o su colega comentaron ahí después de bajarlo, esos comentarios no están en la v1.10**. Si
aparecieran, no hay que rehacer nada: se corre el mismo guion con `--origen-17-4` apuntando a la
bajada nueva.

---

## 11. Pase 5c: baja de la fila «Pruebas automatizadas» de la Tabla 59

El usuario planteó que esa fila no aportaba valor como estaba desarrollada y pidió decidir entre
ajustarla o borrarla. **Se borra**, y no se reemplaza por otra cifra.

**Qué decía.** «Una verificación integral de agosto de 2026 registró 2.203 pruebas aprobadas sin
fallos en cinco suites, y el módulo de distribución incorporó después su propia suite. El conteo
corresponde a esa verificación.»

### Las cuatro razones

1. **No pertenece a lo que la tabla reúne.** La oración que la presenta enumera corrección de
   contratos, cierre de corridas, paridad entre caminos, determinismo y funcionamiento de la
   integración. Las pruebas no están en esa lista. Y esa misma oración **ya declara** que la
   repetibilidad se apoya en pruebas automatizadas o artefactos persistidos, de modo que la fila
   repetía el marco del párrafo anterior y lo único que agregaba era el número.
2. **Es de otra especie que sus seis vecinas.** Cada una de ellas nombra una propiedad del sistema y
   qué muestra la evidencia. Ésta nombraba el **instrumento** con el que se establecieron esas seis,
   que es el marco de la tabla y no una séptima fila entre pares.
3. **El conteo no resiste el detalle.** Las «cinco suites» son plano de medios 641, plano de control
   312, datasets 283 y **la consola contada dos veces**, backend 586 y frontend 381. Faltan el
   módulo de distribución —la propia celda lo admitía— y las suites del repositorio de
   experimentación y de ajuste fino. Un lector que sabe que la plataforma tiene cinco módulos va a
   mapear «cinco suites» sobre ellos y va a estar equivocado. Además, esas 381 son pruebas de
   componentes de interfaz, que no verifican ninguna de las seis propiedades de la tabla.
4. **Ya envejeció, y su fuente lo dice.** El relevamiento del 08-05 lleva una nota de cabecera que
   remite a conteos posteriores, y la punch-list del relevamiento de agosto registra esta cita como
   deuda. Medido el 09-07:

| Suite | 08-05 | 09-07 |
|---|---|---|
| Plano de medios | 641 | 670 |
| Datasets | 283 | 431 |
| Consola, backend | 586 | 668 |
| Plano de control | 312 | 312 |

El frontend no se volvió a correr. Con lo medido, tres de las cinco cambiaron.

### Qué quedó en su lugar

Una cláusula en la nota de la tabla, **estructural y sin número**, que es lo que no envejece: «Cada
módulo mantiene su propio conjunto de pruebas automatizadas, con el que estas propiedades se vuelven
a verificar.» Su comentario ofrece borrarla si el usuario prefiere la baja a secas, y el de la fila
ofrece rechazar la baja si prefiere conservarla.

### Herramienta

La baja de una fila con cambios controlados no existía en el motor. Se agregaron dos métodos a
`pase_docx.py`, `borrar_fila` y `comentario_en_celda`. La marca `w:del` va en el `w:trPr` —inversa
exacta de `fila_nueva`— y el contenido pasa a `w:delText`, de modo que la fila se ve tachada
mientras la sugerencia no se resuelva y desaparece al aceptarla. **El comentario tiene que anclarse
antes de la baja**, porque después el texto ya no está en `w:t`; las marcas de comentario no son
runs con texto, así que sobreviven al borrado. El comentario de la nota se ancló sobre texto previo por
prudencia; el pase 5d verificó después en el esquema que las marcas de comentario **sí** son
contenido válido de `w:ins` (`EG_RunLevelElements`), así que esa prudencia no hacía falta.

Compuerta verde: rechazar todo devuelve la base del pase 5 con 264 párrafos y 5 tablas —que es la
prueba de que `borrar_fila` restituye la fila entera—, paquete íntegro, 17 → 19 comentarios sin
perder ninguno, y el pase se reproduce parte por parte desde su base archivada.

---

## 12. Pase 5d: la revisión completa

El usuario pidió una revisión completa que asegurara que los ajustes de los pases 5, 5b y 5c
tuvieran sentido y quedaran coherentes entre sí y con la plataforma experimental, antes de volver a
leer los documentos con su colega. Se hizo sobre la **vista aceptada** de las cinco versiones
vigentes, que es lo que queda si aceptan todo.

### Cómo se revisó

Una capa mecánica propia (numeración de tablas y figuras, remisiones a secciones, anclas de los 52
comentarios, puntuación en prosa) y **cinco auditorías en paralelo**, cada una con su pregunta:

| Auditoría | Pregunta | Hallazgos que dejó |
|---|---|---|
| Protocolo ↔ resultados | ¿Lo que §17.1 promete es lo que §17.4 hizo y §17.5 midió? | 3 bloqueantes, 17 importantes, 20 menores |
| Diseño ↔ implementación | ¿Todo lo que §17.3 diseña tiene destino en §17.4, y nada de §17.4 contradice a §17.3? | 1 bloqueante, 9 importantes, 15 menores |
| §17.4 ↔ código | Cada afirmación verificable contra repos, configs y artefactos | 1 contradicha, 8 parciales, ~120 confirmadas |
| §17.5 ↔ índices de `results/` | Cada cifra y afirmación de resultado contra su artefacto | 13 contradichas, 3 no verificables, el resto confirmado |
| §15/16 ↔ vocabulario, y los 52 comentarios | ¿§15/16 prepara lo que §17 pisa, con las mismas palabras? ¿Cada comentario sigue vigente? | 2 bloqueantes, 13 importantes, 27 menores; 52 comentarios clasificados |

**Cada hallazgo que este pase aplica se volvió a verificar contra el artefacto antes de
escribirlo**; los auditores también se equivocaron (dos citaron una frase de §17.5 que no existe, uno
contó trece capacidades de núcleo donde hay doce), y eso se filtró.

### El resultado en una frase

La coherencia estructural estaba bien —remisiones, numeración, estrategias, escenarios,
denominadores, ventanas, ocho limitaciones, dos patrones de acople, orden de arranque— y **lo que
fallaba eran afirmaciones puntuales de contenido, varias de ellas mías**, que la lectura de un
documento aislado no detecta y el cruce con los artefactos sí.

### Errores propios que este pase corrige

Conviene dejarlos escritos, porque son el tipo de error que vuelve:

- **«Las dos posibilidades vienen habilitadas por defecto»** (§17.4.7, pase 5). La previsualización
  sí; el video anotado no (`save_annotated_video: bool = False`). Generalicé desde un campo al otro.
- **«17 clips de obra real, un material distinto del estrato que integra el banco temporal»**
  (§17.5.3, pase 5). Son los 13 del estrato B más 4 del piloto. Lo distinto es el nivel de la medición
  y el punto de operación, no el material.
- **«El casco detectado sobre la mesa»** (nota de la Figura 4.6, pase 5). En el cuadro mostrado no
  hay detección de casco, y la imagen no dibuja ninguna caja sobre él; sí en los cuadros vecinos.
- **«Las diferencias menores que 0,02 quedan dentro de la resolución del banco»** (§17.5.5, pase 5).
  El 0,02 no sale de ningún artefacto. Con 34 episodios, un episodio vale 0,029.
- **«En el clip nocturno las mismas bandas quedan entre 6 y 13 %»** (§17.5.3, pase 5). La banda de
  80–120 px da 0,0 %; el 6–13 % es de 120–320.
- **«La comparación por única variable obliga a mantenerlo idéntico»** (§17.4.7, pase 5b), seguido
  de tres diferencias entre tramos. Y «mejor precisión media» donde el criterio es mAP50-95.
- **«`w:commentRangeStart` no es contenido válido de `w:ins`»** (acta del pase 5c, §11). Falso: lo
  admite `EG_RunLevelElements`. La prudencia no costó nada, pero la afirmación era incorrecta y este
  pase ancla comentarios sobre texto insertado sin problema.

### Qué se corrigió, por documento

Todo como sugerencia con su comentario. El detalle de cada cifra y su fuente está en los
comentarios y en la cabecera de `herramientas/pase5d_revision.py`.

**§17.4 → v1.12** (20 comentarios nuevos)
- Evidencia visual: default real y su relación con la regla opt-in del diseño (DA-08, 17.3.4.4).
- Ejemplo de alerta: la alerta transporta el fotograma 109, no los 3.633 ms; los ms de la alerta son
  reloj del equipo de control; 30 fps verificados con ffprobe y con 7.633,33 / 229.
- DTO: «sin valor por defecto» contradecía al código y a 17.4.8.
- Configuración del entrenamiento reescrita: modelo nombrado (YOLOE-26 s), alcance entrenable como
  variable de la escalera con sus dos cifras, checkpoint por mAP50-95, y dos párrafos nuevos con la
  **asignación efectiva de las cuatro fuentes de la Tabla 23**, el material de retención (COCO
  val2017, 5.000, que colisionaba con el estrato de 5.000), el aumento de datos (defaults de la
  biblioteca) y el costo (7,7 y 23,8 min en una A30).
- Tercer tramo: causa según la verificación del 01-09 (linaje + escalera; la fórmula «sin línea
  base sana» estaba en la lista de lo que no hay que escribir), con la familia nombrada.
- «Ninguno se incorporó como modelo de servicio» (los perfiles ft existen en el catálogo), «un
  servicio por perfil» (9 de 11), «persiste la configuración efectiva» (la distribución la expone),
  «espera a que haya un suscriptor» (lo configura el orquestador).
- Perfil operativo nombrado, fp16 declarado como opción de corrida, base-560 comparte umbrales;
  YOLOE-26 con tamaños y puente tiny/base ↔ Swin-T/Swin-B; MM-Grounding-DINO con guion.
- Tabla 39: la operación sobre fuentes en vivo y las doce filas del núcleo reciben destino; «cuatro
  capacidades» ya no mezcla filas con propiedades; la conjunción híbrida lleva su salvedad.
- Tabla 56 «Contrato del diseño» → «Elemento del diseño», «Repositorio de hechos» como en §17.3.
- Tablas 58/56 con report.md; intro del bloque del árbol; Tabla 59 con la intro alineada a sus seis
  filas y «motor de patrones»; Tabla 60 sin `spatial_absence`; seguidor con método; §17.4.6 con los
  4 clips del piloto y la doble anotación declarada como desviación; el último dos puntos de la
  prosa; «acá», «hoy»; el identificador del pattern set con glosa (comentario de Matías).

**§17.5 → v1.8** (15 comentarios nuevos)
- 17.5.2: 0,582/0,520 son de obra curada, no del estrato de chaleco; chaleco no tiene referencia en
  el estrato mayor; el 0,000 de las cuatro variantes es del banco anterior; «inservible para CR-01»
  reabría la incoherencia cerrada en la Tabla 61; `vehicle` no es sinónimo y las 252 cajas eran de
  otro material (`gloves`, un video del rodaje, fuera de `results/`).
- 17.5.3: los 17 clips; «no juzgables» definido; nocturno 80–120 px = 0 %; «juzgabilidad del
  sistema» → rendimiento.
- 17.5.4: nota de la Figura 4.6 con clip, instantes y el casco en cuadros vecinos; referencias por
  severidad de la Tabla 30 declaradas como no usadas y por qué (17.1.7.5 las condiciona a
  recalibrar); el ΔFP_tracking nombrado y leído contra el riesgo de la Tabla 35.
- 17.5.5: Tabla 64, paridad n = 1 y «detector de referencia» era el detector simulado en diferido;
  0,02 → 0,029.
- 17.5.6: veto de precisión con su pre-registro; MM-Grounding-DINO `large` falla con geometría
  normal, distinta de `tiny`; Tabla 65 con antes/después de person y mAP50, umbral 0,05, COCO,
  modelo, «Veredicto negativo pre-registrado» en lugar de un NO-GO que nadie define.
- 17.5.7: p99 sí se computó por corrida; el «20» era la corrida simulada; la curva FP-ventana de
  17.1.5.2 declarada no ejecutada; L2 y L3 en oraciones separadas (eran «ocho» con siete oraciones);
  L6 actualizada según `results/index.md`.
- Nombres de métricas con sus equivalencias (AP@0,5, t_alert-system); «motor temporal» → «motor de
  patrones» en las cuatro apariciones; «acá» → «aquí» en el párrafo de métricas no computadas (mío, del
  pase 5; detectado en el pre-vuelo de la lectura final).

**§17.3 → v1.10** (2 comentarios)
- 17.3.6.3 generalizaba a todos los canales la garantía del orden de creación; en el canal de alertas
  la garantía es el publicador. Residuo de la corrección del orden de arranque.
- Planos ↔ rutas de §16.5.3, en el lugar donde §17.3 remite a esa sección. «vídeo» → «video».

**§17.1 → v1.18** (3 comentarios)
- «temporales, Por último»; Liu et al. 2023 → 2024 (el listado sólo trae 2024); «material propio»
  para un banco que incluye videos públicos; «Sección» → «sección» ×7; Tabla 26 «se acota» → «se
  orienta», alineada con 17.1.6.4 y §17.4.7, con la alternativa ofrecida en el comentario.

### Lo que NO se aplicó y queda para el usuario y su colega

Son decisiones de contenido, datos que sólo tiene el usuario, o cosas de integración.

**Decisiones de contenido**
1. **Tabla 46 de §17.3**: el envoltorio del bus (`bus.envelope.v1`) y el ciclo de vida
   (`run.lifecycle.v1`) son contratos versionados que hoy sólo viven en prosa. Se resolvió por el
   lado de §17.4 (columna «Elemento del diseño»); la alternativa es agregar dos filas a la Tabla 46.
2. **Consentimiento, finalidad, acceso y retención del rodaje**: 17.1.10 las fija como salvaguardas
   para material propio; §17.4.6 describe el rodaje con personas y no dice nada de eso; §17.4.7 cita
   tres compromisos de la Tabla 16 y no esas cuatro. Hace falta una oración con hechos que no están
   en el repositorio.
3. **Matriz de prompts de cinco fases** (17.1.5.4, Tabla 33 «variantes de contraste definidos»):
   §17.4/§17.5 sólo declaran el vocabulario congelado, E-DIR contra E-IND y el ensayo de una
   palabra; los ejes sintáctico, de especificidad y de plantilla no tienen estado declarado.
4. **Intervalos bootstrap del 95 %** para n+ < 200 (17.1.5.4): la Tabla 62 ordena con n+ = 28 y 82
   sin intervalo.
5. **Métricas adoptadas sin estado en §17.5**: precisión y F1 por clase en el punto operativo
   (17.1.7.3); jitter, uso de GPU/RAM/CPU, período de calentamiento y estabilidad del atraso
   (17.1.7.5, Tabla D.1). O se reportan o se suman al párrafo de estado de 17.5.7.
6. **La fuente de captura no se nombra**: §17.4.7 dice «fuente propia»; §17.1 nombra la OAK-D dos
   veces y §15.4.2 nunca (comentario de Simon en §15). Nombrarla en §17.4.3 o §17.4.6 cierra las dos.
7. **Tabla 57 omite las operaciones DELETE** de los tres servicios, que existen (`DELETE
   /api/runs/{id}`; en la distribución olvida el registro sin borrar artefactos) y que §17.3 llama
   «descartar». La tabla dice «principales»; decidir si van.
8. **§15/16**: dar de baja «AAIP, s. f.-b» en el listado global (el párrafo que la citaba se borró);
   ZeroMQ y msgpack no tienen antecedente en §15.4/§16.5.3 (una oración sobre buses sin broker
   alcanza); «motor de patrones», «histéresis», F1, «juzgabilidad» y «Nivel 1/2/3» se usan en §17 sin
   introducción en §16; la identidad de sujeto tiene cinco nombres entre §16 y §17.
9. **El quinto supuesto de 17.1.10** (posible filtración del preentrenamiento, las cifras zero-shot
   no prueban generalización) no tiene eco en las reglas de lectura de 17.5.1.
10. **«prerregistrados» (§17.1) frente a «pre-registrado» (×6 en §17.4/§17.5)**: la forma de la RAE
    es la primera; unificar es global y mecánico.
11. **Tabla 59, fila 5**: «identificador determinista, estable ante el reprocesamiento» está
    sostenido por el código (`uuid5` sobre la quíntupla), no por una prueba; el único test de paridad
    declara `alert_id` volátil. Fila 6: la entrega MQTT contra broker real es una prueba de
    integración que se saltea sin broker.

**Datos que sólo tiene el usuario**
12. **`[[PENDIENTE]]` de procedencia del lote de obra real** (§17.4.6, C1): el único marcador de las
    cinco secciones; bloquea la versión final, no esta ronda.
13. **Horas de anotación** (comentario de Simon en §17.4.6): la cifra no está en ningún repositorio.

**Artefactos a mirar, no texto**
14. **Figura 4.6**: la imagen sale de un render de defensa (`V1_a_p1_c04.mp4`), no de un artefacto
    de `results/`, y **la corrida de control archivada para ese clip alerta a 6,4 s con otro run de
    medios**, mientras la evaluación de la campaña da 7,3 s (3.133 + 4.167). El texto usa 7,3 s;
    conviene resolver de dónde sale la imagen antes de la versión final.
15. **17.5.7, sub-experimento de prompts en aislamiento y dentro del vocabulario**: declarado como no
    ejecutado; no hay definición de ese ítem en `results/` ni en el plan. Es una declaración, no
    necesita artefacto, pero conviene que el protocolo lo nombre igual.

**Integración y cosmética**
16. Numeración global de tablas con catorce números libres (§4.1 de `00-lo-que-resta.md`) y el título
    «17.3» ausente del documento de esa sección.
17. Figuras 4.1–4.4 de §17.3 sin nota ni lectura posterior; verificar en el `.docx` que la imagen de
    4.1 y 4.2 no quedó dentro del párrafo del epígrafe.
18. Nombres de archivo en las Tablas 56 y 58 (norma de autocontención): son artefactos de salida y
    la nota los legitima; decidir si se mueven al bloque de código.
19. Rótulo «Nota» con negrita y cursiva mezcladas en Tablas 60, 61, 63 y 65; negrita parcial en el
    encabezado de la columna de recall de la Tabla 61 (residuo del pase 5, dentro de una sugerencia,
    por eso no se tocó); guion simple en una etiqueta de la Tabla 62.
20. El comentario [10] de §17.4 (fechar el conteo de pruebas) quedó atado a la fila que el pase 5c
    borró: se va con ella al aceptar la baja.

### Compuerta

| Documento | Rechazar todo devuelve la base del pase 5 | Paquete | Comentarios | Reproducible | Verificador |
|---|---|---|---|---|---|
| §17.4 v1.12 | ✓ v1.8 (264 párrafos, 5 tablas, 1 figura) | ✓ | 19 → 39, 0 perdidos | ✓ | sólo lo previo |
| §17.5 v1.8 | ✓ v1.5 | ✓ | 13 → 28, 0 perdidos | ✓ | sólo lo previo |
| §17.3 v1.10 | ✓ v1.8 (643 párrafos, 14 tablas, 4 figuras) | ✓ | 3 → 5, 0 perdidos | ✓ | OK |
| §17.1 v1.18 | ✓ v1.16 (895 párrafos, 22 tablas) | ✓ | 2 → 5, 0 perdidos | ✓ | OK |

Además se validó la estructura de los cambios controlados con un parser XML: ningún `w:delText`
fuera de un `w:del`, ninguna inserción dentro de un borrado, todas las anclas de comentario
completas. Las ediciones sobre párrafos que el pase 5 había insertado quedan como cambios anidados
(23 en §17.4, 27 en §17.5), que es lo que Word produce cuando un segundo revisor edita la
inserción de otro y lo que el esquema admite.

### Herramientas

- `herramientas/pase5d_revision.py`: un guion, cuatro documentos, `--origen-*` y `--solo`.
- `pase_docx.celda(..., rpr=)`: formato de lo insertado en una celda (negrita en encabezados).
- `extraer_informe.py` salta las filas marcadas como borradas (`w:trPr/w:del`): la vista aceptada de
  un documento con sugerencias ya no muestra la fila fantasma `|  |  |`.

---

## 13. Lo que sigue

1. **Revisar las cinco secciones en Google Docs** y aceptar o rechazar. Cada bloque discutible lleva
   un comentario que dice por qué se propone y qué pasa si se rechaza. Las vigentes son §15/§16
   v1.3, **§17.1 v1.18, §17.3 v1.10, §17.4 v1.12 y §17.5 v1.8**; las cuatro incluyen el pase 5d, así
   que hay que subir esas y no las que ya estén arriba.
2. **Responder las cinco confirmaciones** del §4.
3. **Al aceptar:** re-extraer `90d`, `90f`, `90`, `90b` y `90c` por la regla D-C, regenerar el kit,
   archivar las versiones superadas y repetir la lectura transversal sobre las versiones corregidas.
   Recién ahí se declara cerrada cada sección.
4. Después quedan tres frentes que no dependen de esta ronda: escribir §17.6, §18 y §19; la
   integración al documento maestro con la numeración global de tablas y la bibliografía; y el
   marcador de procedencia del lote de obra real, bloqueado hasta cerrar las licencias.

> §17.5 crece unas 890 palabras entre las limitaciones, el estado de las métricas y el párrafo de la
> frontera. Es material que el marco de métricas y la revisión de cierre exigen; si se quiere
> compensar extensión, el lugar no es esa sección.

---

## 14. Bajada del 2026-09-08: lo que aceptó el usuario, y el pase 5e

El usuario revisó las cinco entregas en Google Docs, aceptó las sugerencias y bajó los `.docx` el
09-08: §15/16 **v1.3** (mismo número: el documento sigue abierto a los colegas) · §17.1 **v1.19** ·
§17.3 **v1.11** · §17.4 **v1.13** · §17.5 **v1.9**.

### Qué aceptó

Se extrajo la **vista aceptada** de cada entrega (v1.3 · v1.18 · v1.10 · v1.12 · v1.8) y se comparó,
línea por línea, con la bajada. **Aceptó todo.** Las diferencias son ediciones suyas:

| Sección | Diferencia | Lectura |
|---|---|---|
| §17.1 | «Impacto probable» → «Imp. probable» en el encabezado de la Tabla 35 | ancho de columna; se respeta |
| §17.1 | borradas dos notas: «La mitigación forma parte del diseño metodológico…» (Tabla 35) y «Una métrica sin contexto de corrida pierde interpretabilidad…» | deliberado; se respeta |
| §17.1 | «Nota» en negrita+cursiva en tres tablas más (20, 21, 30) | ya lo estaba en otras ocho; la unificación de rótulos es tarea de integración |
| §17.4 | los tres bloques de código insertados por el pase 5 perdieron su **última línea** | **defecto del viaje**, ver abajo |
| §17.5 | negrita completa en el encabezado de recall de la Tabla 61 (cierra el ítem 19 del §12) · celda «Densidad» fusionada en la Tabla 64 · un punto por un punto y coma · «·» → «-» en una celda | se respeta |
| §15/16 | «puede puede» en el párrafo sobre ajuste selectivo de capas (Lee et al., 2023) | typo introducido al aceptar; **el usuario lo corrige en Google Docs** (el documento sigue vivo allá) |

En §17.3 la bajada es **idéntica** a la vista aceptada. La Figura 4.5 de §17.4 quedó con la imagen
vigente (1926×1684 px, 16 cm) y sin la del 23-08; Google Docs re-codifica el PNG al exportar, así que
se verifica por dimensiones y no por huella.

### Tres defectos que introdujo el viaje por Google Docs

1. **§17.4 — la última línea de los tres bloques de código insertados como sugerencia.** El bloque es
   un solo run con saltos de línea blandos (`w:br`); al aceptar la inserción, Google Docs descartó el
   texto que seguía al último salto: la llave de cierre del ejemplo `media.detection.v1`, la del
   ejemplo `control.alert.v1` y `model_name: str | None = None` del DTO `Detection`. Los bloques que
   no eran sugerencia conservaron su última línea; el único otro tramo insertado con `w:br` (el
   encabezado de dos líneas de la Tabla 61) también. El defecto es del ciclo sugerencia → aceptar sobre
   un bloque de varias líneas.
2. **§17.1 — título fantasma delante de 17.1.11.** Al borrar la nota que llevaba el salto de sección
   (apaisado → vertical), Google Docs dejó un párrafo vacío con estilo Título 3 —entra al índice— y el
   título quedó en cursiva, con el «1» inicial en un tramo aparte.
3. **§15/16 — «puede puede».** Duplicación al aceptar; queda para Google Docs.

### Pase 5e (`herramientas/pase5e_cierre.py`)

- **§17.4 v1.13 → v1.14.** Las tres líneas se repusieron **en limpio**, cada bloque con un comentario
  que lo explica. No van como sugerencia por dos razones: repone texto que el usuario ya aceptó, y una
  sugerencia cuya última línea sigue a un `w:br` corre el riesgo de perderse otra vez por el mismo
  camino. El único marcador `[[PENDIENTE]]` de las cinco secciones (17.4.6, procedencia del lote de obra
  real) se reemplazó **como sugerencia** por la oración que cita la lista de reproducción pública que el
  usuario dejó en su comentario del 09-08, en dos tramos aceptables por separado: la primera oración se
  sostiene sola; la segunda promete la ficha por video en §19 y depende de cerrar C1 (`video_url: TODO`
  en los 18 `clip.yaml`).
- **§17.1 v1.19 → v1.20.** El párrafo vacío conserva el `sectPr` (no se puede borrar) y vuelve a Normal
  con `pPrChange`; el título se reescribe con el formato de sus hermanos. Ambas cosas, sugerencia.
- **§15/16 no se toca**: un segundo colega empezó a revisarlo el 09-07 (tres comentarios; «llegué hasta
  acá» en 16.2.2) y reabrió el pedido de no nombrar CR-01/CR-02 en §15 antes de definirlos en §16.
  Regenerar el `.docx` pisaría lo que haga después de la bajada. Quedan allá 9 comentarios y la
  sugerencia del pase 5 sobre «porque el sistema solo puede detectar…».
- **§17.3 v1.11 y §17.5 v1.9**: nada que hacer.

### Compuerta

| Documento | Rechazar todo devuelve la bajada | Paquete | Vista aceptada vs bajada | Verificador |
|---|---|---|---|---|
| §17.1 v1.20 | ✓ idéntico (895 párrafos, 22 tablas) | ✓ | sin diferencias de texto | OK |
| §17.4 v1.14 | sólo las tres líneas repuestas (`}` · `model_name` · `}`) | ✓ | esas tres líneas + la oración de procedencia | sólo lo previo |

Trampa nueva del motor, encontrada en la primera corrida: **`Documento.comentario` parte los runs con
`_partir`, que supone un `w:t` por run**; un bloque de código es un run con muchos `w:t`, y partirlo lo
desordena (el texto se triplicaba). Para anclar un comentario a un bloque de código se marca el párrafo
entero sin tocar los runs (`comentario_parrafo` en el guion del pase).

### Cierre de la ronda

- Textos base re-extraídos por la regla D-C: `90d` ← v1.3 (banner: en revisión del colega) · `90f` ←
  vista aceptada de v1.20 · `90` ← v1.11 · `90b` ← vista aceptada de v1.14 · `90c` ← v1.9.
- Archivadas en `desarrollando/archivado/` las cinco entregas del pase 5/5d (con el paréntesis «el
  usuario la aceptó como vX») y las dos bajadas que son base del 5e (v1.13 y v1.19).
- Kit regenerado con la **Etapa 6 activa**; su paquete lleva ahora los cinco textos cerrados (`90c` y
  `90b` completos; conclusiones parciales de §16, §17.1 y §17.3; §12–§13 del informe v1.1) y un contrato
  de uso propio: las cinco secciones no se reabren desde §17.6/§18/§19.
- **Cerradas: §17.1, §17.3, §17.4, §17.5.** §15/16 cierra cuando el colega termine.

### Lo que sigue

1. Del usuario, en Google Docs: subir §17.1 v1.20 y §17.4 v1.14, aceptar las tres sugerencias del 5e;
   corregir «puede puede» y cerrar la revisión de §15/16 con los colegas; C1.
2. Etapa 6: §17.6, §18 y §19 con el kit (`--etapa 6`). Después, la integración al maestro (§4 de
   `00-lo-que-resta.md`) y la Etapa 0.
3. Siguen abiertas las decisiones editoriales del §12 que no dependen de esta ronda (1–11, 13–15).

---

## 15. Cierre de la ronda: el pase 5e aceptado y el maestro en posición (2026-09-08)

El usuario aceptó las tres sugerencias del pase 5e y bajó las cinco secciones renumeradas.

| Sección | Bajada | Contra la vista aceptada de lo entregado | Estado |
|---|---|---|---|
| §15 + §16 | **v1.4** | byte a byte la v1.3: sólo cambió el número | ⏳ en revisión de los colegas |
| §17.1 | **v1.21** | idéntica, sin una línea de diferencia | ✅ **CERRADA**, limpia |
| §17.3 | **v1.12** | byte a byte la v1.11: sólo cambió el número | ✅ **CERRADA**, limpia |
| §17.4 | **v1.15** | idéntica, sin una línea de diferencia | ✅ **CERRADA**, 3 comentarios abiertos |
| §17.5 | **«v1.5»** | byte a byte la v1.9: sólo cambió el número | ✅ **CERRADA**, limpia |

Verificado sobre §17.4 v1.15: están las tres líneas de código que Google Docs había descartado, el
marcador `[[PENDIENTE]]` ya no existe y los dos tramos de la oración de procedencia quedaron aceptados,
incluida la promesa de la ficha por video en la sección 19. En §17.1 v1.21 el documento tiene 37
títulos: el fantasma se fue.

⚠ **El número de §17.5 retrocedió.** El archivo se llama v1.5 y ya existía una v1.5 histórica con otro
contenido, la base del pase 5, archivada con su paréntesis. No hay choque de nombres en disco, pero sí
al citar: **esa sección se nombra por su estado, no por ese número**, hasta que se renumere en Drive.
Es el mismo tropiezo que el archivado del 09-07 ya había registrado con las dos §17.4 v1.9.

Los tres comentarios que quedan en §17.4 son dos míos, que explican la reparación de los bloques de
código y ya cumplieron su función, y uno del usuario, «revisar», sobre la dirección de la lista pública.

### El maestro vuelve, con una trampa de estilos

El usuario trajo un export nuevo del informe completo y lo dejó en `desarrollando/`, que es donde vive
ahora porque es el destino de la integración. Sus **420 títulos son idénticos** a los del export del
08-16, que pasó a `archivado/` con su paréntesis: mismo contenido, otra exportación.

Lo que cambió es cómo se llaman los estilos. **El export nuevo trae `Ttulo1`…`Ttulo5` donde el viejo
traía `Heading1`…`Heading5`**, porque Google Docs nombra el estilo según el idioma de la interfaz en que
se editó el documento y le quita los acentos al normalizar el identificador: «Título» queda en «Ttulo».
El costo, medido antes de arreglarlo:

| Herramienta | Sobre el maestro nuevo, antes | Después |
|---|---|---|
| `extraer_informe.py` | 0 títulos en el markdown | 420 títulos |
| `verificar_entregable.py` | 420 problemas duros falsos | 4 observaciones reales |

Las cuatro que quedan son del maestro y eran esperables: el salto de numeración de §8 a §11, la §17.1
vieja que arranca en 17.1.2, una fuga de andamiaje de redacción y cuatro autorías citadas sin entrada en
Referencias.

Las tres herramientas reconocen ahora las dos familias. `pase_docx.py` además **detecta cuál usa el
documento** antes de escribir un estilo de título, porque escribir `Heading3` en un documento de la
familia `Ttulo` deja el párrafo con un estilo inexistente que Word muestra como texto normal. Dos
pruebas nuevas fijan el comportamiento; la suite quedó en 65.

### Cierre

- Textos base re-extraídos de las cinco versiones nuevas. El texto no cambió ni una línea respecto de la
  extracción anterior, que es la confirmación de que el usuario aceptó exactamente lo propuesto.
- Archivadas las cinco superadas, cada una con el paréntesis que dice qué fue. Borrados dos duplicados
  exactos que habían vuelto a `desarrollando/` y los cinco que se habían copiado a `borradores/`, que
  vuelve a estar vacía a propósito.
- Kit regenerado con la Etapa 6 activa y las versiones nuevas en sus notas.
- **Queda del usuario:** cerrar §15/16 con los colegas, renumerar §17.5 en Drive, C1, y las quince
  decisiones editoriales del §12 que siguen abiertas.
