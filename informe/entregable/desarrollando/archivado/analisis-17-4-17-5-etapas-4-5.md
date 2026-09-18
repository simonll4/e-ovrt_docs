# Análisis exhaustivo de §17.4 Implementación (v1.6) y §17.5 Evaluación y Validación (v1.3) — para el pase de consolidación de las Etapas 4 y 5

> **Estatuto.** Diagnóstico previo a la escritura, mismo formato que el que cerró la Etapa 3
> (`analisis-17-3-etapa-3.md`). No modifica ningún `.docx`. La vara es **§17.3 v1.6** (aceptada por el
> usuario el 2026-09-04, último documento cerrado) y **§17.1 v1.15**; para la voz de resultados, el propio
> §17.5 v1.3 sigue siendo la referencia del capítulo. Fecha: 2026-09-04.
>
> **Insumos medidos:** `desarrollando/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx` y
> `…_17.5_Evaluacion_y_Validacion_v1.3.docx` (exportaciones del 2026-08-27, extraídas frescas; el texto de
> §17.4 es idéntico al de la v1.6 del 08-24, el de §17.5 perdió una celda, ver §1); `17.3 v1.6` extraída
> fresca; `90f` (§17.1 v1.15), `90g` (Anexos C/D), `90d` (§15/16 v1.1); `ajustes/04` y `ajustes/05`
> (planes de contenido, con los handoffs H2-01/H2-02 y AJ-5.14); pase 3 §D/§H/§I; `ajustes/09` §2;
> `correcciones-etapa-3-pase-4.md` §E (E4-31); `figuras/README.md`; `operacion/130`. Instrumento y
> salidas crudas en el scratchpad de la sesión (`etapa45/analisis_1745.py`, `analisis_1745.md`).

---

## 0. Veredicto en ocho líneas

1. **Son dos capítulos distintos con dos problemas distintos.** §17.4 (5.044 palabras de prosa) está
   **sobre-argumentado**: 27,4 palabras por oración contra 22 en §17.1 y §17.3, nueve párrafos de más de
   150 palabras (uno de 314), 27 oraciones de más de 45 palabras y **54 dos puntos (10,7 ‰, el doble que
   §17.3 antes de su pase)**. §17.5 (2.593 palabras) ya es magro y de oración corta (20,9); su grasa es de
   **cifra repetida** (el denominador «34 episodios evaluables» aparece 11 veces; 0,789 → 0,930 cinco; 0,1027 h
   seis) y su problema real son **defectos y ausencias**, no verborragia.
2. **Hay una afirmación falsa en §17.4 y §17.3 v1.6 remite a ella.** §17.4.4 dice que la corrida en vivo se
   dispara «primero la distribución, después el control, por último el plano de medios»; §17.4.5 dice «primero el
   control… después medios» citando una **sección que ya no existe** (17.3.8.4); la nota de la Figura 4.7 dice una
   tercera versión; la figura embebida no es la FIG-A producida. El orden real es **control → distribución →
   medios** y la no-pérdida en el bus de alertas la garantiza el *handshake* del publicador, no el orden
   (`operacion/130` R-01, handoff **H2-01**). §17.3.6.3 v1.6 dice «el orden efectivo de arranque se documenta en
   la sección 17.4»: hoy §17.4 lo documenta mal, tres veces.
3. **Cuatro handoffs registrados siguen sin aterrizar**: H2-01 (orden real), **H2-02** (2.946 imágenes de ajuste
   contra el rango 500–2.000 de §17.1, con la causa anti-*leakage*), **E4-31** (detalle operativo del ledger que
   salió de §17.3) y **AJ-5.14** (el costo medido del vocabulario activo, 0,704 → 0,622, y el sub-experimento
   aislado-vs-completo que no se corrió). Ninguno está en los textos; los cuatro son inserciones acotadas.
4. **La Tabla 66 perdió una celda.** En la exportación vigente del 08-27 la fila «CR-02 en vivo» tiene el
   resultado vacío; la v1.3 del 08-23 decía «3 alertas: ≥ 7,1 s». Hay que restaurarla desde el artefacto.
5. **Los ocho comentarios (7 en §17.4, 1 en §17.5) tienen destino claro** y seis se resuelven de facto con la
   consolidación; uno pide un dato que **no existe en ninguna fuente del repositorio** (horas de anotación en
   CVAT) y sólo el usuario puede aportarlo.
6. **§17.4 re-argumenta lo que §17.3 v1.6 acaba de fijar**: patrones de acople, persistir-primero, huecos de
   secuencia, evento de ciclo de vida, cooldown fuera del motor, ausencia inferida en el control, evolución
   aditiva del contrato, «no es un tercer plano», estados de aplicabilidad. Y cuenta tres veces dentro de sí
   mismo que los servicios cargan el modelo una vez, admiten una corrida por vez y persisten la configuración
   efectiva (§3). Entre §17.4 y §17.5 hay **nueve temas contados en ambos con cifras** (§3.3).
7. **La limitación L1–L8 está citada y no declarada en ningún lado.** §17.5.8 dice «junto con las limitaciones
   L1-L8 declaradas», y ninguna sección vigente (§15/16, §17.1, Anexos, §17.3, §17.4, §17.5) las declara.
   Además el usuario anotó «borrar» sobre §17.5.8. AJ-5.05 (🟠) exige que §17.5 las traiga con la formulación
   exacta de L4. Es la decisión de fondo del pase de §17.5 (D-H).
8. **Objetivo razonable:** §17.4: 5.044 → ~3.700 palabras de prosa (−27 %), 16 → 9–12 títulos (cero nivel 4
   opcional), 6 → 5 tablas (la Tabla 60 a prosa, como pide el comentario 6), dos puntos ≤ 10, punto y coma ≤ 8,
   cero párrafos de más de 150 palabras. §17.5: 2.593 → ~2.300 (−11 % neto, porque **suma** AJ-5.14 y L1–L8 y
   resta repeticiones), 9 → 8 títulos, 6 → 5 tablas (la Tabla 65, de dos filas, a prosa), dos puntos y punto y
   coma ≤ 3 cada uno. **Habilitante verificado:** nadie cita las Tablas 56–67 ni la Figura 4.7 desde otra
   sección; §17.3 v1.6 cita **«sección 17.4.6» una vez** y «sección 17.4» cinco; §17.1 y §15/16, ninguna. Renumerar
   §17.4 por dentro cuesta un token en §17.3 (o nada, si se elige la Opción B).

---

## 1. Estado de los artefactos

| Ítem | §17.4 v1.6 | §17.5 v1.3 |
|---|---|---|
| Archivo vigente | `…_17.4_Implementacion_v1.6.docx` (756.074 bytes, 2026-08-27 01:32, exportación de Google Docs) | `…_17.5_Evaluacion_y_Validacion_v1.3.docx` (27.864 bytes, misma fecha) |
| Contra la versión anterior en `archivado/` | Texto **idéntico** a la v1.6 del 08-24 (0 líneas de diferencia; sha distinto por metadatos) | **1 línea distinta**: la celda de resultado de «CR-02 en vivo» (Tabla 66) quedó **vacía**; el 08-23 decía «3 alertas: ≥ 7,1 s» |
| Cambios controlados | 0 inserciones, 0 borrados | 0 / 0 |
| Comentarios | **7**, todos del usuario, ver §1.1 | **1** («borrar», sobre §17.5.8) |
| Títulos | 16: 17.4 + 11 de nivel 3 + **4 de nivel 4** (17.4.8.1–4). Cero de nivel 5 | 9: 17.5 + 8 de nivel 3. Cero de nivel 4 |
| Tablas | 6, numeradas **56–61**. **Cuatro no se citan en prosa** (57, 58, 59, 61) | 6, numeradas **62–67**. **Tres no se citan** (63, 65, 67) |
| Figuras | 1 embebida, «Figura 4.7» (numeración del esquema viejo de §17.3: hoy §17.3 tiene 4 figuras, ésta sería la 4.5). **No se cita en prosa.** No es la FIG-A producida, ver §1.2 | **0**. Las tres figuras destinadas a §17.5 (FIG-B, FIG-C, FIG-F) están producidas en `informe/figuras/` desde el 08-21 y **sin pegar** |
| Bloques de código | 3 (evento JSON, clase `Detection`, árbol del repositorio) — pedidos por el tutor técnico (comentario 0), se quedan | 0 |
| Marcadores | 1 `[[PENDIENTE]]` en 17.4.8.1 (C1, diferido a post-entrega; **no se toca**) | 0 |
| Autocontención | Limpia: 0 ADR, 0 rutas, 0 códigos internos. Una sola cifra de verificación: **«2.203 pruebas aprobadas… en cinco suites»**, foto del 08-05 que `operacion/130` R-12 da por **vencida** | Limpia. «L1-L8» es código del informe (válido) pero cuelga, ver §0.7 |
| Remisiones | `sección 17.3.8.4` (17.4.5) **no existe** en §17.3 v1.6 → es **17.3.6.3**. `17.4.8`, `17.4.11` (×2) y `17.5` (**×9**) existen | `sección 17.4` (×1) existe. Cero remisiones a §17.1/§17.3 |
| Terminología | «contratos **preliminares**» (17.4.2) donde §17.3.8 dice «contratos mínimos» versionados · «Los **dos** planos se implementaron como servicios» (17.4.4 párr. 1) y «Los **tres** servicios» (párr. 3) en la misma sección · «open-vocabulary» y «vocabulario abierto» conviven · `sólo` ×9 / `solo` ×1 · «Éste es el mecanismo» | «mAP50» ×6, «AP50» ×4, «AP@0,5» ×1 para la misma familia de métrica · `bare_head` ×5 y «cabeza descubierta» ×5 · «person-frames» ×5 · «in-domain» ×3 · «open-vocabulary» ×2 · «dequeue» |
| Nombres cruzados | Nombra a **MM-Grounding DINO** como familia integrada y descartada (17.4.6) | La misma familia queda **anónima** («una familia adicional de modelos», 17.5.6) |

### 1.1 Los ocho comentarios (se informan, no se tocan — el usuario decide cuándo)

| # | Doc · ancla | Texto | Lectura para este pase |
|---|---|---|---|
| 0 | §17.4 · título 17.4.3 | «agregar los DTO fue algo que nos marco mariano» | Justifica la sección y los dos bloques de código. **Se queda**; lo que se poda es lo que 17.4.3 repite de §17.3.6.3 y de 17.4.11 (§5) |
| 1 | §17.4 · 17.4.5 «co-ubicados en un único host con GPU» | «referenciar a la seccion donde se hablo de la pc como recurso» | Remisión a **§17.1.4.1** (Infraestructura y roles de ejecución), donde §17.1 v1.15 define el CPN y su equipo |
| 2 | §17.4 · 17.4.7 párr. 2 («Cada plano conserva su repositorio completo…») | «falta el modulo de distribucion» | El párrafo **repite en prosa las filas 1–2 de la Tabla 58**, que ya trae las cuatro filas incluida Distribución. Borrar el párrafo resuelve el comentario sin agregar texto |
| 3 | §17.4 · 17.4.7 párr. 3, oración «La modularidad… se expresa en que un tramo pueda no estar habilitado» | «este dato es como que esta de mas» | Coincide: cae |
| 4 | §17.4 · título 17.4.8.2 | «agregar hs de anotacion» | **El dato no existe en ninguna fuente del repositorio** (`operacion/126` sólo dice «horas de anotación humana en CVAT: no hay comando que lo rehaga»; la única cifra de horas del set es una estimación *a priori* de §17.1 v1.1 para imágenes, nunca usada). Sólo el usuario puede aportarlo; si lo aporta, va en el bloque de CVAT (17.4.8.3), no en el de segmentación |
| 5 | §17.4 · 17.4.8.3 última oración («…actividad intensiva en revisión, no un etiquetado manual…») | «da como a entender que no fue una actividad de mucho esfuerzo» | Reescribir la oración para que el esfuerzo quede afirmado (qué revisó la pasada humana, sobre cuántos clips y episodios, y las horas si el comentario 4 se completa). Es el mismo sitio que E4-19 ya había corregido al quitar «esfuerzo humano acotado» |
| 6 | §17.4 · título de la Tabla 60 | «pasar a desarrollo esta tabla, es mucho texto asi en las columnas» | Coincide con la medición: 472 palabras en 8 filas, **cuatro celdas de 40 a 70 palabras** (las dos de ajuste fino y las dos de preselección). Va a prosa, ordenada por estatuto (§5, 17.4.10) |
| 7 | §17.5 · toda la sección 17.5.8 | «borrar» | Se borra. Consecuencia: la única mención a las limitaciones L1–L8 desaparece, y AJ-5.05 exige que estén. Ver D-H |

### 1.2 La figura de §17.4 y las tres que faltan en §17.5

| Figura | Estado | Observación |
|---|---|---|
| Figura 4.7 (17.4.1), embebida | PNG de 2.046 × 1.432 px fechado 2026-08-23, «Plataforma experimental» con puertos, buses y repositorio | **No es** `informe/figuras/fig-a-vista-de-procesos.png` (1.926 × 1.684, regenerada el 2026-08-28 con los rótulos ①②③ = control → distribución → medios y la nota del *handshake*). La embebida rotula «1. iniciar control · 2. suscripción confirmada · 3. iniciar medios» y **deja a la distribución fuera del orden**; su nota al pie repite el error. Es la versión que el README de figuras declara falsa. Reemplazar por la producida (D-F) y **citarla en prosa** |
| FIG-B calidad vs densidad | producida, sin pegar | destino §17.5.5; su nota al pie está redactada en el README |
| FIG-C fotograma con alerta confirmada | producida, sin pegar | destino §17.5.4; el README pide señalar que el casco detectado sobre la mesa **no** suprime CR-01 |
| FIG-F frontera de juzgabilidad | producida, sin pegar | destino §17.5.4 o §17.5.7 (estrato B); tres ejes: escala × iluminación × oclusión |

Pegar las figuras es trabajo del usuario en Google Docs o de la integración (D-J); lo que sí puede hacer este
pase es dejar la prosa escrita **para** ellas (cita por número, nota al pie lista) en vez de una prosa que las
ignora.

---

## 2. Medición

### 2.1 La vara (mismo instrumento para los seis documentos)

| Documento | Prosa (w) | Tablas (w) | Oraciones | w/oración | `:` prosa (‰) | `;` prosa (‰) | `—` | Metadiscurso | debe (‰) | Párr. >150 w | Oraciones >45 w | Títulos (‰) | Nivel 4 / 5 |
|---|---:|---:|---:|---:|---|---|---:|---:|---|---:|---:|---|---|
| **§17.4 v1.6** | **5.044** | **1.472** | 184 | **27,4** | **54 (10,7)** | 29 (5,7) | **28** | 4 | 2 (0,4) | **9** (máx. 314) | **27** | 16 (3,2) | **4** / 0 |
| **§17.5 v1.3** | **2.593** | **702** | 124 | 20,9 | 15 (5,8) | 16 (6,2) | 0 | 2 | 2 (0,8) | 0 (máx. 95) | 2 | 9 (3,5) | 0 / 0 |
| §17.3 v1.6 | 10.080 | 3.199 | 456 | 22,1 | 0 (0,0) | 0 (0,0) | 2 | 6 | 9 (0,9) | 0 | — | 30 (3,0) | 19 / 0 |
| §17.1 v1.15 | 11.353 | 3.445 | 508 | 22,3 | 5 (0,4) | 27 (2,4) | 8 | 6 | 39 (3,4) | 13 | — | 35 (3,1) | 22 / 0 |
| Anexos C/D | 617 | 1.526 | 61 | 10,1 | 4 | 4 | 7 | 0 | 1 | 0 | — | 3 | 0 / 0 |
| §15/16 v1.1 | 19.307 | 2.188 | 764 | 25,3 | 101 (5,2) | 170 (8,8) | 70 | 16 | 74 (3,8) | 4 | — | 92 (4,8) | 31 / 6 |

Notas de instrumento: la prosa incluye las notas de tabla y figura (§17.4: 316 w en notas; §17.5: 216) y excluye
los tres bloques de código de §17.4 (~270 w). En las celdas hay además 18 `:` y 36 `;` en §17.4 y 4 y 9 en §17.5,
que son notación de lista y se toleran. El conteo de metadiscurso usa el patrón amplio («la presente sección»,
«lo que sigue precisa», «aquí se reportan», «el presente trabajo»). Las cifras de §17.4/§17.5 del análisis de la
Etapa 3 (5.238 / 1.776 y 2.539 / 1.009) salieron de otro corte prosa-tabla; las de esta tabla son las comparables
entre sí.

Voz y conectores en §17.4: «mediante» 12 · «de modo que» 7 · «en cambio» 3 · «El primero/segundo…» 2 · «no X,
sino Y» 2 · rayas 28 (una cada 180 palabras; §17.3 v1.6 quedó en 2). En §17.5: «Por lo tanto / Por ello» 3 ·
«en cambio» 1 · «a su vez» 1 · «Finalmente» 1 · **«n =» 41 veces, 17 de ellas entre paréntesis**.

### 2.2 Peso por sección — §17.4 v1.6

| Sección | Prosa | Tablas | Títulos | Párr. | `:` | `;` | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| 17.4 (entrada) | 111 | — | 1 | 2 | 0 | 0 | «La presente sección documenta…»; el segundo párrafo explica la frontera con §17.5, que el capítulo vuelve a explicar en ocho remisiones más |
| 17.4.1 Componentes y cadena de datos | 422 | — | 1 | 4 + nota 112 | **8** | 1 | Describe medios y control como «servicio gobernado por configuración, modelo cargado una vez, una corrida por vez» (vuelve en 17.4.4 y 17.4.6); «cuarto componente y no un tercer plano» es §17.3.7; la cadena del banco se enumera acá, en 17.4.8 intro y en los cuatro títulos H4. La nota de la figura es un párrafo de 112 w con el orden incompleto |
| 17.4.2 Correspondencia | 128 | 267 | 1 | 2 + nota | 0 | 0 | **El corazón del capítulo** (AJ-4.02). Prosa justa. «contratos preliminares» → «contratos mínimos» |
| 17.4.3 Contratos materializados | **1.114** | — | 1 | 8 + 2 código | **16** | 5 | La más densa: cuatro párrafos >150 w (157, 222, 248, 211), 13 oraciones >45 w. Cuenta persistir-primero, secuencia y ciclo de vida (§17.3.6.3 y 17.4.5), DA-13 y ausencia inferida (17.4.6, §17.3.7, §17.3.4.3) y la evolución aditiva con `track_id` (17.4.11, Tabla 60, §17.3.8.1) |
| 17.4.4 Interfaces y gobierno | 480 | 255 | 1 | 5 + nota 58 | **8** | 5 | «dos planos» vs «tres servicios» en la misma sección; el modelo cargado una vez por tercera vez; **el párrafo 4 trae el orden de arranque falso**; la detención cooperativa es propia y se queda |
| 17.4.5 Acople y caminos | 266 | — | 1 | 4 | 1 | 3 | Re-explica DBE/EBE (§17.1.4.2, §17.3.10.1) y los dos patrones (§17.3.3); el orden por segunda vez, con **remisión rota**; persistir-primero por segunda vez; comentario 1 |
| 17.4.6 Configuración efectiva y catálogo | 524 | — | 1 | 6 | 4 | 5 | Los valores del núcleo y los literales del campeón son **lo que §17.3 remite acá** (17.4.6, «sección 17.4.6» en 17.3.6.2): se quedan. Cooldown/DA-13 (72 w) y evidencia positiva (38 w) son §17.3.7 y §17.3.4.3. Los párrafos 4 y 5 dicen dos veces que hay un servicio por perfil |
| 17.4.7 Artefactos y trazabilidad | 232 | 118 | 1 | 4 + nota + árbol | 2 | 1 | El párrafo 2 repite la Tabla 58 (comentario 2); la oración de la modularidad sobra (comentario 3); los estados de aplicabilidad vuelven en 17.4.9. **Es la casa natural de E4-31**, que falta |
| 17.4.8 Banco temporal y referencia | **953** | — | **5** | 5 | **10** | 3 | Cinco títulos para cinco párrafos: cada H4 es **un párrafo con título** (207, 314, 168, 158 w). El de 314 w tiene **una oración de 102 palabras**. El contenido es el verificado por E4-19 y se queda; el problema es de forma. Comentarios 4 y 5 |
| 17.4.9 Verificación técnica | 149 | 196 | 1 | 2 + nota | 0 | 0 | Cinco de las siete filas de la Tabla 59 re-enuncian propiedades ya afirmadas en 17.4.3/17.4.4/17.4.5; la cifra de pruebas está vencida; el párrafo 2 (ceros silenciosos) es §17.3.9 |
| 17.4.10 Alcance efectivo, límites y brechas | 273 | **472** | 1 | 3 + nota | 2 | 2 | Tabla 60 → prosa (comentario 6). El párrafo de 174 w (E4-17, Nivel 1 vs 2/3) se cuenta otra vez en §17.5.7. La fila «Paridad» dice lo mismo en sus dos celdas. El párrafo asistivo es §17.1.10/§17.3.8.3 |
| 17.4.11 Extensibilidad | 392 | 164 | 1 | 5 + nota | 3 | 4 | Tabla 61 se queda (R-26). El piloto `machinery` (48 líneas, 9 min) se cuenta también en §17.5.2; la identidad como decorador es la tercera vez; MOT por segunda; el cierre repite la entrada |

Estructura: 27 oraciones de más de 45 palabras (17.4.3 concentra 13; 17.4.8, 9). Una sección (17.4.8) con
**cinco títulos para 953 palabras**; el resto, un título por sección.

### 2.3 Peso por sección — §17.5 v1.3

| Sección | Prosa | Tablas | Párr. | `:` | `;` | «n =» | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| 17.5.1 Encuadre y reglas | 285 | — | 4 | 1 | 2 | 0 | Párrafo 2 (87 w) reformula §17.1.7.3 (oración casi literal, similitud 0,6); párrafo 4 (aplicabilidad) es §17.1.7.6/§17.3.9. Lo propio: los tres niveles y el banco de 47 clips |
| 17.5.2 Percepción sobre imágenes | 391 | 68 | 5 + nota | **5** | 1 | 6 | Bien. Tres notaciones de la misma métrica; el piloto de clase nueva solapa con §17.4.11 |
| 17.5.3 Estado por persona | 235 | 125 | 3 + nota | 0 | 1 | 4 | El párrafo 3 **repite literalmente las filas 4–5 de la Tabla 63** (0,467 · 92 · 10.356 · 0,318 · 170 · 10.361); lo nuevo son los 1.414/1.409 person-frames excluidos |
| 17.5.4 Alerta por episodio | **520** | 134 | 6 + 2 notas | 2 | 4 | 6 | El resultado principal. El párrafo de denominadores («n = 28, n = 25, n = 6…, respectivamente») pertenece a la Tabla 64. La Tabla 65 (dos filas) repite el párrafo anterior. La cota FAR se niega acá, en la nota, en 17.5.7 y en 17.5.8. **Falta AJ-5.14** |
| 17.5.5 Tiempo real | 276 | **256** | 3 + nota | 1 | 1 | 4 | Tabla 66 con la **celda vacía** y «50–250 ms» donde §17.1 declara 35–250; el párrafo 3 repite dos filas de la tabla con doble denominador («sobre 460 entregas (n = 460)») |
| 17.5.6 Caminos no adoptados | 368 | 119 | 4 + nota 63 | 3 | 3 | 1 | Los párrafos 1–2 repiten las cifras de las filas E-DIR y E-HYB de la Tabla 64; «2.946 imágenes… 10,35 millones» tres veces en 150 palabras; la familia descartada sin nombre |
| 17.5.7 Lo no ejecutado | 303 | — | 5 | 2 | 2 | 0 | Cada párrafo es propio de esta sección (D.0 bloque 7). Nivel 2/3, MOT y preselección también viven en §17.4.10; la cota FAR por tercera vez. **Falta la oración de AJ-5.14** |
| 17.5.8 Síntesis | 215 | — | 3 | 1 | 2 | 0 | Comentario «borrar». Repite 0,789 → 0,930, 7/7 CR-02 con SDR 0,281, 0,1027 h; cita L1–L8 que nadie declara; anticipa la interpretación de §18 |

---

## 3. Mapa de repeticiones

### 3.1 Dentro de §17.4 (idea → dónde aparece → casa propuesta)

El detector de oraciones casi iguales sólo da dos pares literales (la cadena del banco en 17.4.1 y 17.4.8; las dos
oraciones de configuración CR-01/CR-02). Lo grave, como en §17.3, son las **ideas** re-explicadas con otras
palabras. Las diecisiete, por cantidad de apariciones:

| # | Idea | Apariciones | Casa propuesta |
|---|---|---|---|
| 1 | Servicio gobernado por configuración, con HTTP, modelo cargado una vez al iniciar, una corrida activa por vez | 17.4.1 párr. 2 (×2) · nota Fig. 4.7 · 17.4.4 párr. 1, 2 y 3 · 17.4.6 párr. 5 · Tabla 59 fila 1 (**8**) | 17.4.4 (una vez, en su entrada); 17.4.1 sólo nombra los componentes |
| 2 | Configuración efectiva persistida por corrida | 17.4.4 párr. 1 y 3 · Tabla 57 (×2) · 17.4.6 párr. 6 · 17.4.7 párr. 2 y 4 · Tabla 59 (**8**) | 17.4.4 (gobierno) y una mención en 17.4.7 (artefacto) |
| 3 | Persistir antes de publicar; JSONL es la verdad; paridad relectura/bus | 17.4.3 párr. 4 · 17.4.5 párr. 4 · 17.4.7 párr. 1 · Tabla 59 fila 4 · Tabla 60 fila 7 (**dos celdas iguales**) (**6**, + §17.3.3 y §17.3.6.3) | Una oración en el acople (17.4.5 fundida en 17.4.4) y la fila de verificación |
| 4 | Cierre de corrida por evento de ciclo de vida; relación 1:1 medios–control | 17.4.3 párr. 4 · 17.4.4 párr. 5 · 17.4.5 párr. 2 · Tabla 56 · Tabla 59 fila 3 (**5**) | Tabla 56 (declaración) + 17.4.3 (qué lleva) |
| 5 | Orden de arranque / consumidor suscripto antes que el productor | nota Fig. 4.7 · 17.4.4 párr. 4 · 17.4.5 párr. 3 · Tabla 59 fila 3 (**4**, con **tres versiones distintas, una falsa**) | **Una sola vez**, en el acople, con el orden real y la garantía del *handshake* (H2-01); la nota de la figura remite |
| 6 | Número de secuencia y huecos → `bus_dropped_events`, degradación | 17.4.3 párr. 4 · 17.4.5 párr. 3 · 17.4.9 párr. 2 · Tabla 59 fila 3 (**4**, + §17.3.6.3) | 17.4.3 (el envoltorio lo lleva); el resto nombra |
| 7 | Evolución aditiva del contrato; `track_id` opcional sin productor; el control lo consume; velocidad/pose/segmentación previstas | 17.4.3 párr. 7–8 + código (250 w) · Tabla 60 fila 1 · 17.4.11 párr. 3–4 · Tabla 61 última fila (**4**, + §17.3.8.1 último párr.) | **17.4.11** (extensibilidad), ~120 w; 17.4.3 deja una oración y el ejemplo de código si se conserva (D-D) |
| 8 | Distribución: cuarto componente, no tercer plano; integrada a consola y orquestación | 17.4.1 párr. 3 (×2) · Tabla 59 fila 6 · Tabla 60 fila 3 (**4**, + §17.3.7) | 17.4.1 (una oración: existe, es servicio, entrega por MQTT); lo de «tercer plano» es §17.3.7 |
| 9 | Cooldown/supresión fuera del motor (DA-13); re-alertas medibles | 17.4.1 párr. 3 · 17.4.3 párr. 6 · 17.4.6 párr. 2 (**3**, + dos párrafos de §17.3.7) | Una oración en 17.4.6 («el motor registra cada confirmación sin supresión, conforme a DA-13») |
| 10 | Ausencia inferida en el control, no negación opaca; evidencia positiva person/helmet/vest | 17.4.3 párr. 6 · 17.4.6 párr. 3 (**2**, + §17.3.4.3 ×2) | Ya está en §17.3.4.3; en §17.4 cabe en la oración de la alerta (lo que la alerta conserva) |
| 11 | Estados de aplicabilidad; fallas no se vuelven ceros | 17.4.7 párr. 4 · 17.4.9 párr. 2 (**2**, + §17.3.9, §17.3.10.2, §17.1.7.6) | 17.4.7 (el reporte los declara) en una oración |
| 12 | Cadena del banco temporal (adquisición → segmentación → anotación → congelamiento) | 17.4.1 párr. 4 · 17.4.8 intro · los 4 títulos H4 (**3**) | 17.4.8 |
| 13 | Nivel 1 medible vs Nivel 2/3 sin insumos | 17.4.10 párr. 2 (174 w) · Tabla 60 fila 5 (**2**, + §17.5.7 párr. 1, §17.3.2.1, §17.1.5.1) | Ver §3.3 |
| 14 | Frontera implementación / resultados (remisión a §17.5) | 17.4 párr. 2 · 17.4.6 · nota Tabla 59 · 17.4.9 · 17.4.10 (×3) · 17.4.11 (×2) (**9**) | La entrada dice la regla una vez; las secciones remiten sin re-justificar |
| 15 | Identidad de sujeto implementada como decorador configurable del control | Tabla 60 fila 1 · 17.4.6 párr. 2 · 17.4.11 párr. 3 (**3**) | 17.4.11 |
| 16 | MOT excluidas, no la capacidad de asociar sujetos | Tabla 60 fila 1 · 17.4.11 párr. 4 (**2**, + §17.5.7, §17.3 ×7, §17.1 ×10) | Una oración en 17.4.11; §17.5.7 conserva la suya (es la que tiene el dato medido) |
| 17 | Carácter asistivo, sin identidad personal, no determina incumplimientos | 17.4.10 párr. 3 (**1**, + §17.1.10, §17.3.8.3) | Cae o queda en una oración con remisión a §17.1.10 |

### 3.2 Dentro de §17.5 (cifra o idea → dónde aparece)

| # | Cifra / idea | Apariciones | Propuesta |
|---|---|---|---|
| 1 | «34 episodios evaluables» / «34 clips» | 9 + 5 en prosa, 2 en tablas | El denominador acompaña a cada cifra **cuando cambia**; dentro de un mismo párrafo o tabla se dice una vez y después «sobre el mismo material» |
| 2 | F1 0,789 → 0,930 (+0,141) | Tabla 64 · 17.5.4 párr. 4 · Tabla 66 · 17.5.7 párr. 2 · 17.5.8 (**5**) | 17.5.4 (una vez); 17.5.7 remite sin cifra; 17.5.8 cae |
| 3 | 0,1027 h y «no es una cota operativa» | Tabla 65 (×2) · su nota · 17.5.4 párr. 6 · 17.5.7 párr. 4 · 17.5.8 · 17.5.1 párr. 2 (**7**) | 17.5.4 informa el recuento sobre su duración con la tasa como derivada (AJ-5.09); 17.5.7 dice una vez por qué no hay cota (3 h necesarias) |
| 4 | 2.946 imágenes / 10,35 M de parámetros | 17.5.6 párr. 3 · nota Tabla 67 · 17.5.6 párr. 4 (**3**, dos oraciones casi iguales) | Una vez, en el párrafo de lectura de la Tabla 67 |
| 5 | E-DIR: 0,176 / 0,146 / 0,160, veto por precisión | Tabla 64 · 17.5.6 párr. 1 · 17.5.3 párr. 2 (**3**) | La tabla trae las cifras; 17.5.6 conserva **el criterio** (umbral 0,5 fijado antes) y remite |
| 6 | E-HYB: recall 0,824 → 0,353, refutada | Tabla 64 · 17.5.6 párr. 2 (**2**) | Ídem: 17.5.6 conserva el mecanismo (la unión no es monótona en el motor) y `hyb_and` no ejecutable |
| 7 | p95 64,534 ms (n = 460) · sostenido 102,025 (n = 104) | Tabla 66 · 17.5.5 párr. 3 con doble denominador (**2**) | Sólo la tabla; el párrafo se reduce a la regla de relojes |
| 8 | Video de obra real CR-01/CR-02 (0,467 · 92 · 10.356 · 0,318 · 170 · 10.361) | Tabla 63 filas 4–5 · 17.5.3 párr. 3 (**2**, literal) | Sólo la tabla; el párrafo conserva lo nuevo (cambio de régimen, 1.414/1.409 excluidos) |
| 9 | Estrato B: 13 clips, 5 de 7 declaraciones, 2 evaluables, 11 negativos, 26 vs 323 FP | 17.5.4 párr. 5 · Tabla 65 · 17.5.8 (**3**) | Prosa de 17.5.4 (la revisión ciega es resultado, AJ-5.07); la Tabla 65 de dos filas pasa a la misma prosa (D-I) |
| 10 | Reglas de lectura (positivos con referencia, negativos → FP, re-alertas ≠ FP, percentiles no se suman) | 17.5.1 párr. 2 (+ §17.1.7.3, oración 0,6) | Se compacta con remisión a 17.1.7.3 (D.0 las quiere acá; la restricción 1 del pase 3 pide no reintroducirlas: una lista de cuatro cláusulas cumple ambas) |
| 11 | Ventanas de confirmación 4,0 / 7,0 s | 17.5.4 párr. 3 · Tabla 66 (×2) (+ §17.4.6, §17.1.5.2) | Se quedan (son lectura de resultado), sin re-explicar la histéresis |

### 3.3 Entre §17.4 y §17.5 (contado en los dos con cifras)

| Tema | §17.4 | §17.5 | Quién lo cuenta |
|---|---|---|---|
| Preselección en el borde, 87 % | Tabla 60 fila 6: dos celdas de 60 y 70 w con la cifra y la causa | 17.5.7 párr. 3: cifra **con denominadores** (206 de 236; 277) y la causa | **§17.5.7** (restricción 3 del pase 3: si §17.5 la cita, va con denominador). §17.4 dice «implementada y caracterizada fuera del régimen evaluativo» y remite |
| Rama de ajuste fino | Tabla 60 fila 4: ~120 w narrando la escalera, los veredictos y las expectativas | 17.5.6 + Tabla 67: la curva de tres puntos | **§17.5.6** (restricción 4: la rama cierra en §17.5). §17.4 conserva lo de implementación (protocolo, procedencia, servicio de inferencia, línea base congelada, escalera ejecutada, ningún checkpoint incorporado) **más la causa de la desviación 2.946 vs 500–2.000 (H2-02)**, que es implementación |
| Nivel 2/3 no implementadas, por evaluabilidad | 17.4.10 párr. 2 (174 w, E4-17) y Tabla 60 fila 5 | 17.5.7 párr. 1 (51 w) | Ambas secciones lo reclaman por decisión propia (E4-17 en §17.4; D.0 bloque 7 en §17.5). Propuesta: §17.4.10 conserva el hecho y la razón en ~60 w; §17.5.7 conserva la justificación por evaluabilidad; ninguno repite la lista de insumos faltantes del otro |
| Métricas MOT excluidas ≠ capacidad | Tabla 60 fila 1 · 17.4.11 párr. 4 | 17.5.7 párr. 2 (con la ganancia 0,141) | §17.4.11 una oración; §17.5.7 la que tiene el dato, sin repetir la cifra de 17.5.4 |
| Piloto `machinery` | 17.4.11 párr. 2: 0 entrenamientos, 48 líneas, 9 minutos + la advertencia semántica | 17.5.2 párr. 5: lo mismo + AP 0,662 sobre 99 cajas + sinónimo 0 / otra palabra 252 | Reparto: **§17.4.11 el costo** (configuración, líneas, minutos, sin entrenamiento) y **§17.5.2 el rendimiento** (AP, n, los dos fallos semánticos); cada uno remite al otro en una cláusula |
| Identidad por sujeto medida | Tabla 60 fila 1 «capacidad medida» · 17.4.11 párr. 3 «su efecto se informa en 17.5» | 17.5.4 párr. 4 | §17.4 dice implementada como decorador y remite; §17.5.4 mide |
| Estrategias E-DIR/E-IND/E-HYB | Tabla 60 fila 2 | 17.5.3, 17.5.4, 17.5.6 | §17.4: una oración («las tres variantes se implementaron; la comparación se ejecutó») |
| Paridad DBE/EBE | 17.4.5 párr. 4 · Tabla 59 fila 4 · Tabla 60 fila 7 | Tabla 66 fila «Integridad» (byte a byte, 0 eventos perdidos, n = 6) | §17.4: la propiedad y su verificación (una vez); §17.5: la cifra |
| Familia descartada | 17.4.6 la nombra (MM-Grounding DINO) | 17.5.6 la deja anónima | Nombrarla en los dos o en ninguno (D-L) |

---

## 4. Coherencia con las Etapas 1, 2 y 3 (lo que §17.4/§17.5 re-argumentan y deberían remitir)

| Bloque | Lo que ya establece la etapa anterior | Acción |
|---|---|---|
| 17.4.5 párr. 1–2 (dos patrones de acople; DBE por archivo, EBE por bus con envoltorio, 1:1, cierre) | **§17.3.3** (los dos patrones, con la razón de HTTP y de ZeroMQ) · **§17.3.10.1** y **§17.1.4.2/Tabla 17** (DBE/EBE) | §17.4 conserva sólo lo implementado: nombre del archivo releído, la relectura, el orden real y la paridad verificada. Cae «Mantener ambas clasificaciones separadas evita reducir la plataforma a una dicotomía incompleta» |
| 17.4.3 párr. 4 (persistir-primero, secuencia, ciclo de vida, «espejo») | **§17.3.6.3** dice lo mismo salvo dos aportes de §17.4: los **cuatro campos** del envoltorio y que el publicador de alertas es **espejo** del de medios | Conservar los dos aportes (~70 w); el resto remite |
| 17.4.3 párr. 7–8, 17.4.11 párr. 3–4, Tabla 60 fila 1 (evolución aditiva; velocidad, dirección, pose, segmentación previstas) | **§17.3.8.1 último párrafo** enumera exactamente las mismas previsiones y dice que el control puede materializar la identidad por configuración | §17.4 lo cuenta **una vez** como hecho verificado (17.4.11): el campo existe, ningún productor lo emite, el control lo consume, el contrato no cambió de versión, los tres mecanismos que lo permiten |
| 17.4.6 párr. 2 (cooldown fuera del motor) | **§17.3.7**, dos párrafos, incluido el cambio de granularidad y las re-alertas | Una oración |
| 17.4.6 párr. 3 y 17.4.3 párr. 6 (ausencia inferida, evidencia positiva) | **§17.3.4.3** (dos veces) | Cae en 17.4.6; en 17.4.3 queda dentro de «la alerta conserva evidencia auditable» |
| 17.4.1 párr. 3 («cuarto componente funcional y no un tercer plano») | **§17.3.7** («No constituye un tercer plano ni un cuarto rol funcional») | Cae la negación; queda el hecho |
| 17.4.7 párr. 4 y 17.4.9 párr. 2 (estados de aplicabilidad, ceros silenciosos) | **§17.3.9**, **§17.3.10.2**, **§17.1.7.6** | Una oración en 17.4.7 |
| 17.4.10 párr. 2 y 17.5.7 párr. 1 (Nivel 1 vs 2/3) | **§17.1.5.1** (evaluabilidad del catálogo) y **§17.3.2.1/Tabla 39** (núcleo y extensiones) | Ver §3.3 |
| 17.4.10 párr. 3 (asistivo, sin identidad personal) | **§17.1.10** (salvaguardas) y **§17.3.8.3** | Una oración con remisión o cae |
| 17.4.11 párr. 4, Tabla 60, 17.5.7 párr. 2 (MOT) | **§17.1.5.1/17.1.7** (E-10) y **§17.3** (siete veces) | Ver §3.3 |
| 17.5.1 párr. 2 (reglas de lectura) | **§17.1.7.3** («Toda cifra se informa con la combinación… el material o estrato… y su denominador») | Compactar con remisión (ver §3.2 fila 10) |
| 17.5.1 párr. 4 (métrica computable sólo con referencia, reloj e instrumentación) | **§17.1.7.1/17.1.7.6** y **§17.3.9** | Una cláusula |
| 17.5.5 Tabla 66, «Dentro del presupuesto de 50–250 ms» | **§17.1** declara **35–250 ms** para el tramo previo a la acumulación (`mapa-secciones-17-1-v1-15.md` §4: «§17.4 y §17.5 deben mapear una cifra a la otra al reportar») | Citar la cifra de §17.1 y remitir (el p95 de 31,8 ms cae dentro de ambas cotas, así que el cambio de texto no cambia la lectura). D-K |
| 17.4.6 párr. 1 y 17.4.8.4 (ventanas 4.000/7.000 ms) | **§17.1.5.2** fija los valores de protocolo | En §17.4.6 se quedan (son la configuración efectiva); en 17.4.8.4 se dice «las mismas ventanas del motor» sin repetir los números |
| 17.4.5 párr. 4 («co-ubicados en un único host con GPU») | **§17.1.4.1** define el CPN y su equipo | Remisión (comentario 1) |
| 17.4.2 «contratos preliminares definidos durante el diseño» | **§17.3.8.1** los llama «contratos mínimos», versionados (D-P2-5) | Alinear el término |

Y las dos dependencias inversas que §17.3 v1.6 dejó apuntando a §17.4 y que **hoy no se cumplen**:

- **§17.3.6.3**: «El orden efectivo de arranque de los módulos se documenta en la sección 17.4» → §17.4 lo
  documenta mal (§0.2, H2-01).
- **§17.3.7**: «El detalle operativo del ledger, incluida la unidad de conteo del tramo, se documenta en la
  sección 17.4» → §17.4 no lo dice (E4-31). La Tabla 58 llega hasta «cada intento… descartes definitivos por
  separado»; faltan la **unidad de conteo** (la notificación, no la fila), la **fila por intento más la del
  descarte definitivo** y el **archivado de generaciones** al reutilizar un directorio con deduplicación sobre
  todas ellas.

---

## 5. Diagnóstico y propuesta por sección

Convención: **w** = palabras de prosa propias. Objetivos indicativos.

### §17.4

#### 17.4 entrada (111 w) → ~60 w
Un párrafo: qué documenta el capítulo y la regla de frontera con §17.5 dicha una vez («los resultados de
desempeño se presentan en 17.5»). Cae «La presente sección…»; caen las otras ocho justificaciones de la
frontera repartidas por el capítulo (quedan las remisiones secas).

#### 17.4.1 Componentes construidos y cadena de datos (422 w + Figura + nota 112 w) → ~280 w + figura + nota ≤ 60 w
Los cuatro componentes en un párrafo por rol, sin las propiedades de servicio (idea 1, van a 17.4.4) y sin «no
un tercer plano» (§17.3.7). La cadena de datos en dos oraciones que remiten a 17.4.8, sin enumerar sus cuatro
etapas (las enumera 17.4.8). **La figura se reemplaza por la FIG-A producida** (D-F), se cita en prosa y su nota
dice el orden real en una oración («①②③: control, distribución, medios; la no-pérdida de alertas la garantiza el
publicador, que espera al suscriptor») o remite a 17.4.4. Numeración: 4.5 si se sigue el esquema del capítulo
(§17.3 quedó en 4.1–4.4); la global es de la integración.

#### 17.4.2 + 17.4.3 → una sección «Correspondencia y contratos materializados» (128 + 1.114 w + Tabla 56 + 2 códigos) → ~750 w
- La prosa de 17.4.2 (dos párrafos) se queda casi entera; «preliminares» → «mínimos»; el párrafo post-tabla
  se reduce a su primera oración (la segunda vuelve a enumerar los cuatro componentes).
- Párrafo 2 de 17.4.3 (157 w): la definición genérica de contrato (clase de modelo, validada en la frontera,
  JSON por línea, envoltorio binario) se queda en ~60 w; la **cadena interna de cuatro contratos del plano de
  medios** (unidad visual → preparada → detección cruda → normalizada) es propia y valiosa, se queda como
  oración separada, sin los dos puntos.
- DetectionEvent + JSON: se quedan (comentario 0). La frase introductoria del bloque de código pierde los dos
  puntos.
- Párrafo 4 (222 w): se parte en tres oraciones cortas y se queda sólo lo que §17.3.6.3 no dice: los cuatro
  campos del envoltorio, «espejo» entre los dos publicadores, y que el ciclo de vida delimita el cierre y no el
  inicio. Persistir-primero y huecos: una cláusula cada uno.
- PatternStateChanged (78 w): se queda; «los mismos que fija la máquina de estados del diseño» remite a
  §17.3.6.1 (la FIG-E vive allá, §H del pase 3).
- AlertEvent (248 w): **se queda la derivación determinista del identificador y sus tres consecuencias** (es lo
  más propio de la sección), en tres oraciones sin «Primero/Segundo/Tercero» ni rayas; cae la coda
  «Por eso la ausencia no se presenta como…» (§17.3.4.3) y la oración de DA-13 (17.4.6).
- Párrafos 7–8 + clase `Detection` (250 w): **migran a 17.4.11** reducidos a ~120 w (D-D). Si el usuario quiere
  conservar el segundo bloque de código, va con ellos.

#### 17.4.4 + 17.4.5 → una sección «Servicios, gobierno por configuración y acople» (480 + 266 w + Tabla 57) → ~480 w
- Entrada (~80 w): **tres** servicios (no «dos planos»), gobernados por configuración, HTTP, modelo cargado
  una vez, una corrida activa por vez, configuración efectiva persistida. Es la **única casa de la idea 1 y 2**.
- Tabla 57 se queda entera (E4-06/E4-25: única tabla de interfaces del informe). Nota a una oración, sin «(ver el
  texto)».
- Consulta previa de configuración y perfil (~40 w): se queda, es propio.
- **Orden de arranque (~90 w), una sola vez y correcto**: primero el control (queda suscripto al canal de
  detecciones antes de que los medios emitan), después la distribución (necesita el identificador de la corrida de
  control), por último los medios; la no-pérdida en el bus de alertas la garantiza el publicador, que espera al
  suscriptor antes de emitir, no el orden. Reemplaza al párrafo 4 de 17.4.4 (falso), al párrafo 3 de 17.4.5
  (incompleto, remisión rota) y a la nota de la figura. Cierra **H2-01** y la dependencia inversa de §17.3.6.3.
- Detención cooperativa y la asimetría del control (~80 w): se queda, sin rayas.
- DBE/EBE como se implementaron (~90 w): archivo releído (`detections.jsonl`), bus con envoltorio, persistir
  antes de publicar, paridad verificada; «co-ubicados en un único host» con remisión a **§17.1.4.1** (comentario
  1). Cae todo lo que es §17.3.3/§17.3.10.1.

#### 17.4.6 Configuración efectiva y catálogo de modelos (524 w) → ~330 w
Se quedan íntegros los valores del conjunto de patrones (párr. 1, partido en tres oraciones sin los dos puntos)
y los literales del perfil (párr. 6). Párrafo 2 → una oración (DA-13). Párrafo 3 cae (§17.3.4.3). Párrafos 4 y 5 se
funden (~110 w): familias del catálogo, un servicio por perfil, comparación disponiendo instancias, la familia
descartada **con nombre** (D-L), remisión a §17.5 para la selección. ⚠ Es la sección que **§17.3 v1.6 cita por
número** («sección 17.4.6», en 17.3.6.2): ver D-A.

#### 17.4.7 Artefactos y trazabilidad por corrida (232 w + Tabla 58 + árbol) → ~230 w
Párrafo 2 **cae** (repite la Tabla 58; comentario 2). Oración de la modularidad **cae** (comentario 3). Párrafo 4 se
queda (versión de código; estados de aplicabilidad en una oración). **Entra E4-31** (~70 w): unidad de conteo =
notificación; una notificación no entregada deja una fila por intento y la del descarte definitivo; al reutilizar un
directorio de salida la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones.
La Tabla 58 se cita en prosa.

#### 17.4.8 Construcción del banco temporal y de la referencia humana (953 w, 5 títulos) → ~750 w, 1 título (D-B)
El contenido es el verificado el 2026-08-20 para E4-19 y **no cambia de fondo**. Cambia la forma:
- La entrada deja de enumerar las cuatro etapas (las enumeran los párrafos); conserva la historia de
  `clip_gt.v2` en una cláusula.
- Los cuatro H4 desaparecen; cada uno queda como uno o dos párrafos con entradilla en negrita (rodaje y lote ·
  segmentación · preanotación y revisión · derivación y congelamiento). El párrafo de 314 w se parte en tres y
  su oración de 102 palabras en tres o cuatro. Ninguna oración > 40 w.
- El `[[PENDIENTE]]` de procedencia queda donde está.
- Comentarios 4 y 5: la última oración del bloque de CVAT se reescribe para afirmar el esfuerzo (qué se revisó:
  cajas, trayectorias, identidades, atributos por tramo y límites de episodio, sobre 47 clips y 37 episodios), y
  toma las horas si el usuario las aporta (D-G). Sin ese dato no se inventa ninguno.
- En 17.4.8.4, «4.000 ms para CR-01 y 7.000 ms para CR-02» → «las mismas ventanas de confirmación que usa el
  motor» (ya están en 17.4.6).

#### 17.4.9 + 17.4.10 → una sección «Verificación, alcance efectivo y brechas» (149 + 273 w + Tablas 59 y 60) → ~500 w + Tabla 59
- Entrada de verificación (~60 w) y **Tabla 59 con celdas acortadas** (cada fila una oración de ≤ 20 w; las
  propiedades ya afirmadas en el capítulo se nombran, no se re-explican). Fila «Pruebas automatizadas»: D-E.
  Cae el párrafo 2 (ceros silenciosos, ya en 17.4.7).
- **Tabla 60 → prosa por estatuto** (comentario 6), ~300 w en cuatro párrafos: (a) ejercido y medido —
  identidad por sujeto como decorador, las tres estrategias, distribución MQTT integrada, paridad DBE/EBE; los
  valores en §17.5; (b) implementado y caracterizado fuera del régimen evaluativo — la preselección, con la
  causa en una oración y la cifra en §17.5.7; (c) especificado y no implementado — Nivel 2/3, con la razón en
  ~60 w (E4-17 recortado; la lista de insumos faltantes queda en §17.5.7); (d) rama comparativa de ajuste fino —
  lo implementado (protocolo, procedencia, servicio de inferencia, línea base congelada, escalera ejecutada
  completa, ningún checkpoint incorporado) **más H2-02**: 2.946 imágenes de ajuste porque se tomó el 100 % de los
  linajes elegibles tras excluir íntegramente la fuente compartida con el banco (1.330 imágenes) y deduplicar
  perceptualmente contra él (81 más), sin submuestrear al techo del rango de §17.1; controles de solapamiento en
  cero y semilla registrada. Las cifras de la curva, en §17.5.6.
- Párrafo asistivo (41 w): una oración con remisión a §17.1.10, o cae.

#### 17.4.11 Extensibilidad implementada y costo de extensión (392 w + Tabla 61) → ~350 w + Tabla 61
Tabla 61 se queda y se cita. **Se vuelve la única casa de la evolución aditiva** (idea 7, ~120 w, con los tres
mecanismos y el caso `track_id`). Piloto `machinery`: el costo (sin entrenamiento, 48 líneas de configuración,
nueve minutos) y una oración sobre la validación semántica con remisión a §17.5.2 para el rendimiento. MOT: una
oración. Cierre: ~40 w (la cadena materializada y qué evalúa §17.5), sin repetir la entrada del capítulo.

### §17.5

#### 17.5.1 Encuadre y reglas de lectura (285 w) → ~200 w
«La presente sección informa…» → voz de sistema. Los tres niveles se quedan. Las reglas de lectura como cuatro
cláusulas con remisión a 17.1.7.3 («rigen las reglas de lectura de 17.1.7.3: métricas sólo sobre positivos con
referencia aplicable, negativos por recuento de falsos positivos, re-alertas aparte, percentiles de tramos
distintos sin sumar»). El banco de 47 clips se queda entero (P3: 47, no 34). Aplicabilidad en una cláusula.

#### 17.5.2 Percepción sobre imágenes (391 w + Tabla 62) → ~340 w
Se queda casi todo. Una sola notación de métrica (D-N). «bare_head» nombrado una vez con su equivalente y
después en castellano. El piloto de clase nueva conserva AP 0,662 (n = 99) y los dos fallos semánticos, y remite
a §17.4.11 por el costo de configuración (§3.3). Cinco dos puntos → 0.

#### 17.5.3 Estado por persona (235 w + Tabla 63) → ~170 w
Párrafo 3: caen las seis cifras que repiten las filas 4–5; quedan el cambio de régimen (la caída es de precisión)
y los person-frames excluidos del denominador. «person-frames» se define una vez (cuadros con persona) o se
traduce. La Tabla 63 se cita.

#### 17.5.4 Alerta por episodio (520 w + Tablas 64–65) → ~520 w con una tabla menos
- Los denominadores de t_alert **entran a la Tabla 64** como columna o entre paréntesis en la celda; cae el
  párrafo «En el orden de las filas…, respectivamente».
- Histéresis (párr. 3): se queda, con los paréntesis resueltos en prosa.
- Identidad (párr. 4): **única casa** de 0,789 → 0,930.
- **Entra AJ-5.14** (~90 w): con el mismo modelo, evaluador, conjunto de patrones, referencia y tiempos, una
  palabra más en el vocabulario activo (la clase nativa de cabeza descubierta) costó F1 0,704 → 0,622 (recall
  0,735 → 0,676; precisión 0,676 → 0,575) sobre el mismo material. Es el contraste de variable única que
  sostiene que el vocabulario es una variable experimental.
- Estrato B (párr. 5): se queda; la **Tabla 65 pasa a la prosa** (D-I): 26 contra 323 falsos positivos sobre los
  mismos 11 clips negativos; 3 y 190 en los 6 min 9,6 s del clip continuo (0,1027 h), con la tasa horaria como
  derivada y no como cota. El párrafo 6 (52 w) cae: lo dice 17.5.7.
- La prosa cita FIG-C (alerta confirmada) y FIG-F (frontera) donde correspondan, con las notas del README, si
  D-J = pegar.

#### 17.5.5 Tiempo real (276 w + Tabla 66) → ~200 w + Tabla 66 reparada
**Restaurar la celda «3 alertas: ≥ 7,1 s»** verificándola contra el índice `realtime` (185 cifras fueron
verificadas el 08-23; ésta se perdió después). «Dentro del presupuesto de 50–250 ms» → cifra de §17.1 con
remisión (D-K). Párrafo 2 (trampas de SDR y t_alert, AJ-5.10) se queda. Párrafo 3 → una oración (relojes
distintos, la Tabla 66 trae los tramos). Cita a FIG-B si D-J = pegar.

#### 17.5.6 Caminos probados y no adoptados (368 w + Tabla 67) → ~280 w
Párrafos 1–2: se conservan **los criterios** (veto de precisión fijado en 0,5 antes de leer; la disyunción no es
monótona dentro del motor; la conjunción no ejecutable por diseño) y caen las cifras que la Tabla 64 ya trae. La
familia descartada, con nombre (D-L). Ajuste fino: entrada de una oración + Tabla 67 + **un** párrafo de lectura
(el límite es estructural: 2.946 imágenes contra 10,35 millones de parámetros, dicho una vez; T1 gana por recall y
T2 por AP; ningún checkpoint adoptado). Nota de la Tabla 67 sin repetir el párrafo.

#### 17.5.7 Lo no ejecutado y lo no implementado (303 w) → ~330 w
Cada párrafo es de esta sección y se queda, más corto: Nivel 2/3 (la lista de insumos faltantes, que sale de
§17.4.10); MOT (sin la cifra 0,141); preselección con sus denominadores (única casa de la cifra); cota FAR (única
casa de las 3 h necesarias); ancla EBE-desde-clip. **Entra la oración de AJ-5.14**: el sub-experimento formal
aislado-vs-completo sobre las finalistas no se corrió; la pregunta quedó respondida por el contraste de 17.5.4.
**Y, según D-H, cierra con las limitaciones L1–L8** (~120 w o una tabla de 8 filas cortas), con la formulación
firmada de L4 («se precisó, no se levantó»).

#### 17.5.8 Síntesis (215 w) → desaparece (comentario 7)
Nada de lo que dice es nuevo salvo dos remisiones que necesitan casa: L1–L8 (→ 17.5.7 por D-H) y el «círculo con
§15» / interpretación (→ §18, Etapa 6, handoff).

---

## 6. Lo que NO se toca (con nombre)

- **Tabla 56** (correspondencia diseño → artefacto: es la respuesta al tutor técnico), **Tabla 57** (única tabla
  de interfaces, E4-06/E4-25), **Tabla 58** (artefactos), **Tabla 61** (puntos de extensión, R-26) y las **Tablas
  62, 63, 64, 66 y 67** de §17.5: sus filas no cambian (la 59 sólo acorta celdas; la 64 gana los denominadores;
  la 66 recupera su celda).
- **Los dos bloques de código de 17.4.3** y el árbol de 17.4.7 (comentario 0; E4-13/E4-29). Si D-D mueve la
  evolución aditiva a 17.4.11, la clase `Detection` va con ella o cae, pero no se reescribe.
- **Los valores efectivos del núcleo** (4.000/2.000 y 7.000/3.000 ms; 0,35 y 400 px²; 0,25; franjas 0–45 % con
  12 % y 25–85 % con 8 %) y **los literales del perfil operativo** (560 px · caja 0,30 · texto 0,25 · confianza
  0,25 · IoU 0,50 · área 100 px² · paso 1 · cola 8). Son lo que §17.3 remite a §17.4.
- **La derivación determinista del identificador de alerta** y sus tres consecuencias (una vez).
- **El fundamento del recorte ex-ante** de los clips (preludio 3,5 s, cola 3–10 s, piso de duración, argumento
  bidireccional): hechos verificados para E4-19; se re-escribe la forma, no el contenido.
- **El `[[PENDIENTE]]` de procedencia** (C1, bloqueante recién para la versión final).
- **Todas las cifras de §17.5** (185 verificadas contra la hoja de datos el 08-23), incluido `n+ = 5.313` (es el
  denominador medido; la nota del CLAUDE.md sobre el GT vigente de 5.308 es interna y no entra).
- **El pretérito de §17.5** (es la vara de voz del informe) y el presente de §17.4.
- **Las reglas de casa de §17.5**: banco de 47 clips, sin ranking sobre n = 2, FAR como recuento sobre duración
  observada, «L4 se precisó», nada de «el mejor modelo» (E4-26), la rama de ajuste fino nunca «por tiempo».
- **Autocontención**: hoy limpia en ambos; ninguna reescritura introduce códigos internos, rutas ni ADR. Los
  códigos que sí valen son los del informe (DA-13, E-DIR/E-IND/E-HYB, Nivel 1–3, L1–L8).
- **Las decisiones vigentes de los pases 1–3** (D-P2-5/D-P2-6: §17.4 único punto de declaración de
  identificadores versionados; E4-17; E4-19; E4-26; E4-27; enmienda a E4-22; D.0 de §17.5).

---

## 7. Propuesta de reestructuración (a decidir)

### §17.4 — Opción A (recomendada): 8 secciones, cero nivel 4, renumeración interna

| Nueva | Contenido (viene de) | Tablas / figuras | Prosa objetivo |
|---|---|---|---|
| 17.4.1 Componentes construidos y cadena de datos | 17.4 entrada + 17.4.1 | FIG-A producida (4.5) | ~330 |
| 17.4.2 Correspondencia y contratos materializados | 17.4.2 + 17.4.3 | T56 + 2 códigos | ~750 |
| 17.4.3 Servicios, gobierno por configuración y acople | 17.4.4 + 17.4.5 | T57 | ~480 |
| 17.4.4 Configuración efectiva y catálogo de modelos | 17.4.6 | — | ~330 |
| 17.4.5 Artefactos y trazabilidad por corrida | 17.4.7 + E4-31 | T58 + árbol | ~230 |
| 17.4.6 Banco temporal y referencia humana de evaluación | 17.4.8 sin H4 | — | ~750 |
| 17.4.7 Verificación, alcance efectivo y brechas | 17.4.9 + 17.4.10 (T60 → prosa) + H2-02 | T59 | ~500 |
| 17.4.8 Extensibilidad y costo de extensión | 17.4.11 + evolución aditiva de 17.4.3 | T61 (→ 60) | ~350 |

Totales: **~3.700 w de prosa (−27 %)**, **9 títulos** (1 + 8), cero nivel 4, **5 tablas** renumeradas 56–60,
1 figura. Costo aguas abajo: **un token en §17.3 v1.6** («sección 17.4.6» → «17.4.4»), que puede hacerse ahora
(v1.7 mínima) o en la integración, cuando se renumeren tablas y figuras de todo el capítulo. Requiere
`mapa-secciones-17-4-v1-7.md` para leer E4-01…E4-31 y `ajustes/04`.

### §17.4 — Opción B (conservadora): 11 secciones con su número, sin nivel 4

Se conservan los 11 títulos de nivel 3 y su numeración (la remisión de §17.3 sigue válida sin tocar nada); caen
los 4 H4 de 17.4.8; se aplica toda la poda de §3–§5 (incluida Tabla 60 → prosa). Resultado: ~3.900 w, 12
títulos. Costo: 17.4.2 (128 w), 17.4.5 (~120 w tras la poda) y 17.4.9 (~60 w + tabla) sobreviven como secciones
de un párrafo.

### §17.5 — una sola opción: 7 secciones, misma numeración

17.5.1–17.5.7 se conservan con su número y título; 17.5.8 desaparece (comentario 7). Cambios de fondo: Tabla 66
reparada, Tabla 65 a prosa, denominadores a la Tabla 64, AJ-5.14 (dos inserciones), L1–L8 (D-H), figuras
citadas (D-J). Totales: **~2.300 w** (−11 % neto), 8 títulos, 5 tablas renumeradas 61–65 (o lo que fije la
integración).

### Puntuación y estilo, cualquiera sea la opción

| Marcador | §17.4 hoy | §17.5 hoy | Objetivo | Cómo |
|---|---:|---:|---|---|
| `:` en prosa | 54 | 15 | ≤ 10 / ≤ 3 | Las 69 oraciones están listadas en el instrumento. Patrones: «X: enumeración» (se vuelve oración con verbo), «X no es Y: es Z» (dos oraciones), introducción de código (se deja **una** por bloque, o se cierra con punto) |
| `;` en prosa | 29 | 16 | ≤ 8 / ≤ 3 | Enumeraciones de tres miembros → oraciones; en celdas se toleran |
| `—` | 28 | 0 | ≤ 4 / 0 | Incisos → oración aparte o paréntesis eliminado |
| Párrafos > 150 w | 9 | 0 | 0 | 17.4.3 (×4), 17.4.8 (×4), 17.4.10 (×1) |
| Oraciones > 45 w | 27 | 2 | ≤ 5 / 0 | La de 102 w de 17.4.8.2 se parte en cuatro |
| Metadiscurso | 4 | 2 | 0 | «La presente sección…» (×2), «lo que sigue precisa», «aquí se reportan», «del presente trabajo» |
| «Primero/Segundo/Tercero» | 2 | 0 | 0 | 17.4.3 párr. 6 |
| «n =» entre paréntesis | 0 | 17 | ≤ 4 | A tablas o a prosa («sobre 34 episodios») |
| Notación de métrica | — | mAP50/AP50/AP@0,5 | una | «mAP50» para el agregado multiclase, «AP50» por clase, y nunca «AP@0,5» |
| Anglicismos | live ×5, runner, webconsole, backend, pipeline, ledger, manifest, checkpoint, dead_letter, replay | person-frames ×5, in-domain ×3, open-vocabulary ×2, checkpoint ×4, dequeue | lista cerrada | Se conservan los que son nombre de artefacto o término establecido en §17.3 (ledger, checkpoint, msgpack); «live» → «en vivo» (§17.4 ya usa ambos); «open-vocabulary» → «de vocabulario abierto» (E3-33); «in-domain» → «en dominio»; «person-frames» se define una vez |
| «vídeo»/«video» | video ×7 | Video ×3 | «video» | unificar en los dos |
| Erratas | «Éste es el mecanismo»; `sólo` ×9 / `solo` ×1 | — | 0 | unificar acento según la norma que usen §17.1/§17.3 |

---

## 8. Decisiones para el usuario antes de escribir

> ✅ **FIRMADAS POR EL USUARIO EL 2026-09-04. Las quince quedaron en la recomendación.** Las cuatro
> que se preguntaron una por una: **D-A = Opción A** (ocho secciones, renumeración interna y mapa) ·
> **D-H = cerrar §17.5.7 con L1–L8** (con la formulación firmada de L4) · **D-G = escribir sin cifra**
> (el dato de horas no existe y no se inventa) · **D-M = los ocho comentarios quedan abiertos con su
> ancla**. Las once restantes se aplicaron por recomendación. Ejecución: `correcciones-etapa-4-pase-4.md`
> (E4-32…) y `correcciones-etapa-5-pase-4.md` (E5-01…).

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| **D-A** | Profundidad de la reestructura de §17.4 | A (8 secciones, renumeración interna + mapa, un token en §17.3) / B (11 secciones, sin nivel 4, cero renumeración) | **A**. Tres de las once secciones quedan de un párrafo tras la poda; el token de §17.3 es trivial y la integración renumera todo igual |
| **D-B** | Los cuatro títulos de nivel 4 de 17.4.8 (creados por E4-19) | Quitarlos y dejar párrafos con entradilla en negrita / conservarlos | **Quitarlos**: cada uno encabeza un solo párrafo; el contenido de E4-19 se conserva íntegro |
| **D-C** | Tabla 60 → prosa (comentario 6) y reparto con §17.5 | Prosa por estatuto en §17.4, cifras (87 %, curva FT) sólo en §17.5 / prosa que conserve las cifras en ambos | **Prosa por estatuto, cifras en §17.5** (restricciones 3 y 4 del pase 3) |
| **D-D** | Casa única de la evolución aditiva del contrato e identidad | 17.4.11 (extensibilidad) / 17.4.3 (contratos) | **17.4.11**; 17.4.3 deja una oración. El bloque `class Detection` viaja con ella o cae (los campos ya se ven en el JSON) |
| **D-E** | La cifra «2.203 pruebas aprobadas… cinco suites» (foto del 08-05, vencida) | Fechar la cifra («al 2026-08-05») y decir que la suite de distribución se agregó después / actualizar con los conteos del 08-28 (`operacion/130`: 643 + 312 + 133 + 88 + 46 + 668 + 431 = 2.321 recolectadas, **no ejecutadas ese día**) / quitar el número | **Fechar**: es la única corrida completa verificada en verde; «2.321» no puede escribirse como «aprobadas» |
| **D-F** | Figura 4.7 embebida (versión del 08-23, orden incompleto) | Reemplazar por `fig-a-vista-de-procesos.png` regenerada (①②③, nota del README) / corregir la embebida | **Reemplazar**: es la figura gobernada por script y verificada contra el código. Lo hace el usuario en Google Docs o la integración; el pase deja la cita y la nota |
| **D-G** | Comentario 4, horas de anotación en CVAT | El usuario aporta la cifra (no existe en el repositorio) / se responde con la caracterización cualitativa del esfuerzo (comentario 5) | Aportar la cifra si existe en los registros de CVAT; **no se inventa** |
| **D-H** | §17.5.8 «borrar» y el destino de L1–L8 (AJ-5.05 🟠, hoy incumplida: nadie las declara) | Cerrar 17.5.7 con un párrafo o tabla corta de L1–L8 con la formulación firmada de L4 / dejarlas para §18 (handoff a la Etapa 6) | **Cerrar 17.5.7 con L1–L8**: AJ-5.05 las asigna a §17.5 y el material ya está en la sección (FAR, revisión ciega, bloque único, tracker en multitud, CR-02 a Nivel A). La interpretación y el círculo con §15 van a §18 |
| **D-I** | Tabla 65 (dos filas) | A prosa (D-P2-1 corolario 2; `ajustes/09` §2.2 ya lo decidió para T-82) / conservar | **A prosa** |
| **D-J** | FIG-B, FIG-C y FIG-F en §17.5 (producidas, sin pegar) | El pase escribe la prosa citándolas y el usuario las pega en Google Docs con las notas del README / se deja todo a la integración | **Citarlas ahora y pegar después**; una prosa de resultados escrita sin sus figuras se reescribe (manual §6) |
| **D-K** | «50–250 ms» de la Tabla 66 vs «35–250» de §17.1 | Citar la cifra de §17.1 con remisión / conservar 50–250 y anotar la fuente | **Cifra de §17.1**; el p95 medido está dentro de ambas |
| **D-L** | MM-Grounding DINO | Nombrarla en §17.5.6 como en §17.4.6 / anonimizar en §17.4 | **Nombrarla en los dos**: el descarte se «informa con los resultados» según §17.4.6, y §17.5.6 es donde se informa |
| **D-M** | Los 8 comentarios | Resolverlos al aceptar, con acta que los mapee a unidades / dejarlos viajar | Resolverlos al aceptar (6 quedan atendidos de facto; el 4 depende de D-G). Lo decide el usuario |
| **D-N** | Notación y términos de §17.5 | Unificar (mAP50/AP50; `bare_head` una vez; person-frames definido; «en dominio»; «de vocabulario abierto») / dejar | **Unificar** |
| **D-O** | Casa de la remisión de §17.3.6.3 sobre el orden de arranque | El pase escribe el orden real una vez (17.4.4 fundida) y §17.3 no se toca | Sí; es lo que §17.3 v1.6 ya promete |

---

## 9. Cómo se aplicaría (para cuando se decida)

1. **Bases:** §17.4 v1.6 (exportación 08-27) y §17.5 v1.3 (exportación 08-27, con la celda a restaurar).
   **Salidas:** §17.4 **v1.7** y §17.5 **v1.4** con control de cambios, misma mecánica que las Etapas 2 y 3 (XML
   byte a byte; párrafos con `sectPr` se reescriben por dentro; marcas autocerradas antes que las emparejadas;
   un párrafo borrado con imagen deja la imagen viva; filas de tabla se borran, columnas no). Actas:
   `desarrollando/correcciones-etapa-4-pase-4.md` (unidades **E4-32…**, absorbe H2-01, H2-02 y E4-31) y
   `desarrollando/correcciones-etapa-5-pase-4.md` (unidades **E5-01…**, absorbe AJ-5.14 y las decisiones
   D-H…D-N); `mapa-secciones-17-4-v1-7.md` si D-A = A.
2. **Orden interno:** primero los cuatro handoffs (H2-01, H2-02, E4-31, AJ-5.14) y la celda de la Tabla 66
   (son los pendientes registrados y el defecto), después la reestructura, después puntuación y estilo.
3. **Verificación (compuerta `verificar_v17_17_4.py` / `verificar_v14_17_5.py`):** títulos por nivel; tablas y
   figuras citadas exactamente una vez; **la cadena «primero la distribución» en cero**; `17.3.8.4` en cero;
   metadiscurso, «Primero/Segundo», `live`, `open-vocabulary`, `AP@0,5` en cero; conteo de `:`/`;`/`—`;
   párrafos > 150 w y oraciones > 45 w en cero; **las cifras de §17.5 idénticas a la v1.3** (185, más la celda
   restaurada y las de AJ-5.14 verificadas contra su artefacto); los literales de 17.4.6 intactos; los 8
   comentarios con su ancla; el `[[PENDIENTE]]` intacto; chequeo anti-duplicación (ninguna oración ≥ 12 palabras
   repetida dentro del capítulo ni contra §17.3 v1.6/§17.1 v1.15); autocontención en cero; diff párrafo a
   párrafo atribuido a unidades.
4. **Al cerrar:** re-extraer `90b` y `90c` (regla D-C), fechar en `00-el-informe-hoy.md`, cerrar en
   `00-lo-que-resta.md` §3.5 (AJ-5.14) y §0 (estado por sección), actualizar `ajustes/04` §0 (H2-01/H2-02) y
   `ajustes/05` (AJ-5.14), regenerar el kit (`generar_project_kit.py --check`).
5. **Handoffs que nacen acá:** a la **integración** — un token en §17.3 v1.6 si D-A = A; numeración global de
   figuras (la 4.7 de §17.4 y las tres de §17.5) y de tablas (hueco 53–55 tras §17.3; 56–67 corren si caen la 60 y
   la 65); pegado de FIG-A/B/C/F. A la **Etapa 6** — la interpretación de conjunto, el círculo con §15 (AJ-5.11) y
   la escala AF-1…AF-11, que §17.5.8 anticipaba y §18 debe absorber. Al **usuario** — el dato de horas de
   anotación (D-G) y la ficha de procedencia del lote (C1, ya registrada).
