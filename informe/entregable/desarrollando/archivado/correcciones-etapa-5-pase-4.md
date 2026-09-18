# Correcciones — pase 4 sobre §17.5 Evaluación y Validación (v1.3 → v1.4)

> **Estatuto.** Acta del pase de consolidación de la Etapa 5, aplicado el 2026-09-04 sobre
> `desarrollando/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.3.docx` y entregado como
> `…_v1.4 (sugerencias sin aceptar).docx`, con control de cambios y autoría propia.
>
> **Origen:** diagnóstico [`analisis-17-4-17-5-etapas-4-5.md`](analisis-17-4-17-5-etapas-4-5.md),
> con las quince decisiones D-A…D-O firmadas por el usuario el 2026-09-04. Aplicador
> `herramientas/aplicar_v14_17_5.py`, compuerta `herramientas/verificar_pase_17_4_17_5.py`
> (**verde, 0 fallas**).
>
> La numeración de subsecciones **no cambia**: 17.5.1 a 17.5.7 conservan su número y su título, y
> sólo desaparece la 17.5.8. Las tablas sí se renumeran, 62–67 → 61–65.
>
> ⚠ **Ninguna cifra del capítulo se recalculó.** Las 185 verificadas contra la hoja de datos el
> 2026-08-23 llegan intactas a la v1.4. Lo que el pase hace con ellas es dejar de repetirlas y
> devolver una que la exportación había perdido.

---

## 0. Resultado, medido con el mismo instrumento antes y después

| Marcador | v1.3 | v1.4 |
|---|---:|---:|
| Prosa | 2.605 w | **2.437 w** |
| Tablas | 512 w | **526 w** |
| Títulos | 9 | **8** |
| Tablas | 6 | **5**, renumeradas 61–65 |
| Dos puntos en prosa | 15 | **0** |
| Punto y coma en prosa | 16 | **0** |
| Oraciones de más de 45 palabras | 2 | **0** |
| Palabras por oración | 20,0 | **19,0** |

El capítulo baja poco porque ya era magro y porque el pase **suma** dos contenidos que faltaban,
el costo medido del vocabulario activo y la declaración de las ocho limitaciones. Las tablas suben
catorce palabras porque la de alerta por episodio absorbe sus denominadores.

---

## A. Los dos defectos de hecho

### E5-07 · 🔴 La celda perdida de la tabla de tiempo real
La exportación vigente del 2026-08-27 tiene **vacía** la celda de resultado de la fila «CR-02 en
vivo». La versión del 08-23 decía **«3 alertas: ≥ 7,1 s»**, y ese valor está entre las 185 cifras
verificadas. Se restaura con su forma original, idéntica a la de la fila hermana de CR-01. El
denominador de la fila, n = 3 confirmaciones, nunca se había perdido.

### E5-09 · 🟠 Las ocho limitaciones se citaban y no se declaraban
§17.5.8 decía «junto con las limitaciones L1-L8 declaradas», y **ninguna sección vigente del
informe las declara**: cero apariciones en §15/§16, §17.1, los Anexos C y D, §17.3 y §17.4. Como
el usuario además pidió borrar §17.5.8, la única mención iba a desaparecer con ella. Por **D-H**,
el cierre de 17.5.7 las declara en prosa, sin códigos internos, con la formulación firmada de la
cuarta: la medición sobre obra real **la precisó sin levantarla**, porque caracteriza por mecanismo
dónde el sistema deja de ser evaluable en lugar de validarlo sobre obra real.

---

## B. AJ-5.14 — el costo del vocabulario activo

### E5-05 · Lo que se midió, en §17.5.4
§17.1.5.3 pre-registra el eje de composición del vocabulario activo y promete que cada prompt se
evalúa en aislamiento y dentro del vocabulario completo. §17.5 v1.3 no reportaba ni el resultado ni
la no ejecución. Entra un párrafo en la sección de alerta por episodio, que es donde vive el nivel
de medición al que pertenece el dato.

El contraste es de **variable única** sobre la combinación de contraste base-560 que la tabla ya
reporta. Se mantuvieron fijos el modelo, el evaluador, el conjunto de patrones, la referencia y los
tiempos, y se sumó al vocabulario una sola palabra, la de cabeza descubierta. El F1 por episodio
bajó de **0,704 a 0,622**, el recall de 0,735 a 0,676 y la precisión de 0,676 a 0,575. La lectura
que habilita es que la interacción entre términos de un mismo vocabulario no es despreciable, de
modo que dos configuraciones sólo son comparables cuando declaran el vocabulario completo que
vieron.

### E5-09 · Lo que no se corrió, en §17.5.7
Una oración declara que el sub-experimento formal de aislamiento contra vocabulario completo **no
se ejecutó** sobre las combinaciones finalistas, y que la pregunta quedó respondida por el
contraste de arriba. Sin ella, la promesa de §17.1 quedaba huérfana. **§17.1 no se toca**: es
pre-registro, y D-P3-3 prohíbe reescribirlo para que encaje con el resultado.

---

## C. La poda

### E5-01 · §17.5.1 — voz y reglas de lectura
«La presente sección informa» pasa a voz de sistema. El párrafo de reglas de lectura reformulaba
§17.1.7.3 casi literalmente, con una oración de similitud 0,6 contra la suya: ahora **remite** a
esa sección y conserva sólo las cuatro cláusulas que §17.5 aplica. El banco de 47 clips y la regla
de aplicabilidad quedan intactos.

### E5-02 · §17.5.2 — puntuación, notación y reparto
Los cinco dos puntos desaparecen. Los tamaños de los tres estratos se dicen una vez. **El piloto de
clase nueva se reparte con §17.4.8**: el costo de incorporación (sin entrenamiento, 48 líneas,
nueve minutos) queda allá y acá quedan el rendimiento y los dos fallos semánticos, cada uno con su
denominador.

### E5-03 · §17.5.3 — el párrafo deja de repetir la tabla
El tercer párrafo repetía las seis cifras de las filas de video de la tabla. Ahora conserva sólo lo
que la tabla no dice: que la caída provino de la precisión y no del recall, y los 1.414 y 1.409
cuadros con persona no juzgables que el evaluador excluyó del denominador.

### E5-04 · §17.5.4 — los denominadores bajan a la tabla
El párrafo «En el orden de las filas…, respectivamente» existía para colgar seis valores de n de la
tabla anterior. Los seis pasan a la columna de latencia, que ahora los declara fila por fila, y el
párrafo desaparece. La nota lo dice explícitamente.

### E5-06 · D-I · La Tabla 65 pasa a prosa
Dos filas y cinco columnas para cuatro números. Por el corolario de D-P2-1 y por la decisión ya
registrada para esa tabla, pasa a la prosa del estrato de obra real. Los conteos, la duración
observada y las dos tasas derivadas se conservan **con la advertencia de que no son una cota**, que
antes se repetía cuatro veces y ahora se dice una.

### E5-08 · §17.5.6 — el criterio se conserva, la cifra queda en la tabla
Los dos primeros párrafos repetían las cifras de las filas de estrategia directa e híbrida de la
tabla de alerta por episodio. Conservan **el criterio** —el umbral de precisión fijado de antemano,
la no monotonía de la unión dentro del motor temporal, y por qué la variante por conjunción no era
ejecutable— y sueltan los números. Por **D-L**, la familia descartada se nombra, igual que en
§17.4. El par «2.946 imágenes contra 10,35 millones de parámetros» se decía tres veces en 150
palabras y queda una.

### E5-10 · D-H · §17.5.8 se elimina
Nada de lo que decía era nuevo. Repetía la ganancia de identidad, los 7 episodios de CR-02 con su
SDR y la exposición de 0,1027 h, y anticipaba la interpretación, que es de §18. Las dos remisiones
que sí necesitaban casa se resolvieron: las limitaciones cierran 17.5.7 y la interpretación queda
como handoff a la Etapa 6. **El comentario «borrar» se re-ancla** al párrafo de las limitaciones,
que es lo que reemplaza a la sección.

---

## D. Notación y remisiones

### E5-02 · D-N · Notación unificada
- La métrica de detección se escribe **mAP50** para el agregado multiclase y **AP50** por clase.
  La tercera forma, `AP@0,5`, desaparece.
- `bare_head` se nombra **una vez**, glosado como la clase de cabeza descubierta, y después el
  texto usa el castellano. La tabla de la curva conserva el nombre del artefacto.
- «person-frames» pasa a **cuadros con persona**, en la prosa y en las dos celdas que lo usaban.
- «in-domain» pasa a **en dominio**.

### E5-07 · D-K · El presupuesto de latencia
La celda decía «Dentro del presupuesto de 50–250 ms», mientras §17.1 declara **35–250 ms** para ese
tramo. En vez de elegir una cifra, la celda **remite a §17.1.7**, que es donde el presupuesto se
define. El percentil medido cae dentro de las dos cotas, así que la lectura del resultado no
cambia.

### E5-11 · Renumeración de tablas
62 → **61** · 63 → **62** · 64 → **63** · 65 → **prosa** · 66 → **64** · 67 → **65**. Con §17.4
cerrando en la Tabla 60, el capítulo queda contiguo, que es lo que el pase 3 §G previó cuando fijó
que §17.5 arranca en la 61. **Cada tabla se cita ahora exactamente una vez**; en la v1.3, tres no
se citaban.

---

## E. Lo que NO se tocó

- **Las 185 cifras verificadas.** Ninguna se recalculó ni se reformuló.
- **El pretérito del capítulo**, que es la vara de voz del informe.
- **Las reglas de casa de §17.5**: el banco de 47 clips y no 34, sin ranking sobre el estrato de
  dos episodios evaluables, la tasa de falsas alarmas como recuento sobre su duración observada,
  la cuarta limitación precisada y no levantada, y ningún veredicto formulado como «el mejor
  modelo».
- **La organización por pregunta de medición** (D-P3-6). Ningún título lleva nombre de campaña.
- **El denominador n+ = 5.313** del recall de CR-01, que es el medido.
- **La revisión ciega del banco de obra real** como resultado, no como nota al pie.

---

## F. Verificación

`herramientas/verificar_pase_17_4_17_5.py` — **verde, 0 fallas**:

1. **Rechazar todos los cambios devuelve exactamente la v1.3.**
2. Ocho títulos, cero de nivel 4.
3. Cero dos puntos y cero punto y coma en prosa, cero párrafos de más de 150 palabras y cero
   oraciones de más de 45.
4. Greps prohibidos en cero: la síntesis eliminada, «person-frames», la tercera notación de la
   métrica, «in-domain», el presupuesto propio, el metadiscurso y las limitaciones citadas por
   código.
5. Greps exigidos presentes: el costo del vocabulario activo, su no ejecución, la declaración de
   las ocho limitaciones, la celda restaurada y la familia descartada nombrada.
6. Cada tabla con un rótulo y una cita.
7. El comentario y el `sectPr` del cuerpo sobreviven, y la entrega trae cambios controlados.

---

## G. Lo que queda

**Del usuario:**
1. Aceptar los cambios de `…_17.5_…_v1.4 (sugerencias sin aceptar).docx` y guardar como
   `…_v1.4.docx`.
2. **Pegar las tres figuras** que este capítulo tiene producidas y sin insertar, a 16 cm de ancho y
   sin reescalar: la de calidad contra densidad en 17.5.5, la del fotograma con alerta confirmada
   en 17.5.4 y la de la frontera de juzgabilidad en 17.5.4 o 17.5.7. Sus notas al pie están
   redactadas en el README de figuras. Al pegarlas, citarlas en prosa por número.
3. Cerrar el comentario cuando quiera.
4. Git.

**Al aceptar:** re-extraer `90c-etapa5-texto-extraido.md` (regla D-C) y regenerar el kit.

**Handoff a la Etapa 6 (§18):** la interpretación de conjunto, el cierre del círculo con §15 en
tres tiempos y la escala de afirmaciones con su fuerza. La síntesis eliminada las anticipaba, y
ahora §18 es su única casa.
