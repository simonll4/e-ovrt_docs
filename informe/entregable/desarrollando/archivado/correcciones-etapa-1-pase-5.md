# Etapa 1 — pase 5: unificación de formato y terminología (versión final)

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1 — final 2026-08-27.docx` (§15 y §16; 22.800
  palabras; 92 títulos; 13 tablas). **Es el archivo que se te entrega junto con este brief.**
- **Qué es este pase:** el último. **El contenido está cerrado y verificado** — cuatro pases
  aplicados y comprobados unidad por unidad (64 de 64). Lo que queda es que el documento
  quede **uniforme en formato y en terminología**, alineado a la convención de las secciones
  ya cerradas del informe (§17.3, §17.4, §17.5). Nada más.
- **Cómo trabajar:** dentro del Project, sobre el `.docx` entregado, **sin Drive**. El texto
  vigente también está en el knowledge (`90d`), pero **el entregable se construye editando
  este `.docx`**, no regenerándolo.

---

## 0. Límites — leer antes de tocar nada

Este pase **no es de redacción**. Se corrige formato; el texto queda como está.

**Prohibido:**
- Reescribir, resumir, ampliar, reordenar o "mejorar" párrafos. Ni uno.
- Tocar cifras, citas, años, nombres de modelos, filas o celdas de tablas (salvo los cambios
  de rótulo indicados abajo).
- Agregar o quitar párrafos, secciones, tablas, notas o referencias.
- Reaplicar cualquier corrección anterior: **ya están todas** (E1-01 a E1-56, las 16 `AJ-`,
  las 11 podas). Si algo parece faltar, **no lo agregues**: anótalo en el registro de cambios.
- Agregar Anexo A, Anexo B o listado de Referencias: **el entregable es solo el desarrollo**.
- Borrar o completar el marcador `[[PENDIENTE: … AAIP …]]` de §16.6.2.2: **viaja tal cual**.
- Cambiar el estilo de encabezado de ningún título (los 92 tienen su `Heading N` correcto).

**Criterio de aceptación:** el diff entre el archivo entregado y tu versión debe mostrar
**únicamente** los cambios de las secciones 1 a 6. El conteo de palabras debe quedar en
22.800 ± 60 (los cambios de terminología mueven unas pocas decenas, nada más).

---

## 1. Títulos: tipo frase (F1)

**Vara:** las secciones cerradas del informe usan títulos **tipo frase** — solo mayúscula
inicial, más nombres propios y siglas (85 de 86 títulos en §17.3/§17.4/§17.5). En Etapa 1
**39 de los 92 títulos** están en Title Case. Ejemplos:

| Hoy | Debe quedar |
|---|---|
| 15.2.1. Paradigmas Arquitectónicos y Modelos Representativos | 15.2.1. Paradigmas arquitectónicos y modelos representativos |
| 15.2.3. Síntesis Comparativa y Trade-Offs para Tiempo Real | 15.2.3. Síntesis comparativa y *trade-offs* para tiempo real |
| 16.2. Condiciones de Riesgo Observables | 16.2. Condiciones de riesgo observables |
| 16.5.2. Descomposición Instrumental de Glass-to-Algorithm | 16.5.2. Descomposición instrumental de Glass-to-Algorithm |

**Conservan mayúscula:** nombres propios y de modelos (Grounding DINO, DINO-X, YOLO-World,
YOLOE, OWL-ViT, OWLv2, Florence-2, SORT, CLIP), siglas (OVD, MOT, DETR, DINO, EPP, IoU),
Glass-to-Algorithm / Glass-to-Glass como denominaciones, y "Ley", "Decreto", "Resolución",
"ISO 45001".

**Los cuatro títulos de bloque** usan hoy dos separadores distintos ("Bloque A —" y
"Bloque B:", con un doble dos-puntos en el D). Unificar con **raya**:
- 15.2.1.1. Bloque A — Detectores end-to-end tipo DETR/DINO con fusión visión–lenguaje en el decoder
- 15.2.1.2. Bloque B — Detectores one-stage tipo YOLO con puntuación región–texto
- 15.2.1.3. Bloque C — Detectores basados en dual-encoders (CLIP-like) y matching por similitud
- 15.2.1.4. Bloque D — Modelos guiados por prompts generalistas: generativos e híbridos

Cambiar **solo las mayúsculas y el separador**: ni una palabra del título.

## 2. Rótulo de tabla: negrita simple (F2)

**Vara:** `**Tabla N**` en negrita, y el título de la tabla debajo **en itálica** (así están
las 29 tablas de §17.3–§17.5). En Etapa 1, las Tablas **2 a 8** llevan el rótulo en
negrita+itálica (`***Tabla 2***`) y las 9 a 12 en negrita simple. Pasar las siete a negrita
simple. Los títulos ya están en itálica: no tocar.

## 3. Rótulo de nota: *Nota.* en itálica (F3)

**Vara:** APA 7 — *Nota.* en itálica, con el punto dentro de la itálica, y el resto del
párrafo en redonda (es la forma de las seis notas de §17.5, la sección más reciente). Hoy
conviven cuatro variantes: `**Nota.**` (×5), `*Nota.*` (×4), `**Nota**.` (×1) y una
malformada `**Nota***.*` (Tabla 8). Unificar las 11 a *Nota.* itálica. La "Fuente: …" sigue
dentro del mismo párrafo, como está.

## 4. Rótulos de párrafo: negrita con el punto dentro (F4)

Las fichas usan `**Arquitectura base.**` (punto dentro de la negrita) en 24 de 28 casos.
Cuatro lo llevan fuera: `**Convención de lectura**.`, `**Alta latencia (>~3 s)**.`,
`**Latencia media (~0,5 a 3 s)**.` y `**Baja latencia (<~500 ms)**.` → mover el punto
dentro. Nada más en esos párrafos.

## 5. Terminología: una palabra por concepto (F5)

El documento debe ser **internamente consistente**; la convención para todo el informe se
fija en la integración, pero la Etapa 1 no puede usar tres palabras para lo mismo.

| Concepto | Hoy en el texto | Usar | Excepción que se conserva |
|---|---|---|---|
| unidad de video | **cuadro** (21) · fotograma (7) · *frame* (15) | **cuadro** | ninguna — "frame-a-frame", "frame-to-frame" y "frame-by-frame" pasan a **"cuadro a cuadro"** o "entre cuadros consecutivos" |
| latencia de punta a punta | **extremo a extremo** (4) · end-to-end (3) · E2E (2) | **extremo a extremo** | **"arquitecturas end-to-end"** (DETR) es término de arte: **se conserva** |
| asociación temporal | **seguimiento** (20) · tracking (19) | **seguimiento** en prosa | **"tracking-by-detection"** y "seguimiento multiobjeto (MOT)" se conservan como términos de arte |

**Se conservan tal como están** (son el vocabulario canónico del informe y de su glosario):
*open-vocabulary*, *zero-shot*, *fine-tuning*, *prompt*, *pipeline*, *benchmark*, *linear
probing*, *full tuning*, *phrase grounding*, *tracking-by-detection*, *ground truth*. No
traducirlos ni ponerlos en itálica donde no la tengan.

**Prueba de aceptación de F5:** al terminar, "fotograma" = 0, "frame" = 0 fuera de nombres
propios, "end-to-end" solo junto a "arquitecturas", "E2E" = 0, "tracking" solo dentro de
"tracking-by-detection".

## 6. Siglas: definir la primera vez (F6)

El glosario del informe (§11) ya define OVD, EPP, AP, FPS y MOT: **no se redefinen**. Faltan
tres, todas de una sola intervención:

- **IoU** — primera aparición en la "Convención de lectura" de §15.2.1: *"…AP promediado entre
  umbrales IoU de 0,50 a 0,95"* → *"…umbrales de intersección sobre unión (IoU) de 0,50 a
  0,95"*.
- **SFU** y **NACK** — aparecen solo en la Tabla 8 (fila WebRTC). Agregar a la Nota de esa
  tabla, junto a las siglas que ya define: *"SFU = Selective Forwarding Unit. NACK = Negative
  Acknowledgement."*
- **E2E** — desaparece con F5 (cabecera "Latencia típica E2E" → "Latencia típica extremo a
  extremo", y la Nota de la Tabla 8).

---

## 7. Lo que está bien y **no se toca**

- Los 92 títulos tienen su estilo `Heading N` correcto y la numeración es contigua.
- Las 13 tablas tienen columnas uniformes, título en itálica, nota y fuente, y mención en prosa.
- La ecuación (1) de §16.5.2 está centrada e introducida en prosa.
- Las 83 obras citadas están todas en el listado global (que **no** va en este archivo).
- El `[[PENDIENTE: …]]` de la AAIP.
- Los separadores decimales: **coma** decimal y **punto** de miles (19.587 y 25.326 son
  números de ley; 5.210, 1.000, 2.000 y 50.000 son miles). Todos correctos.
- Cero identificadores internos, cero resultados propios, cero andamiaje.

---

## 8. Forma de la entrega

1. **Un `.docx`**, construido editando el archivo entregado — no un documento regenerado.
2. **Con cambios controlados activados**, para que cada cambio de F1–F6 sea visible.
3. **Estilos intactos**: mismo `Heading N` en cada título; sin negrita imitando títulos; sin
   markdown crudo (`###`, `|---|`).
4. **Un registro de cambios** al pie del chat (no dentro del documento), con el conteo por
   ítem: títulos cambiados (esperado 39 + 4 de bloque) · rótulos de tabla (7) · notas (11)
   · rótulos de párrafo (4) · reemplazos de terminología por palabra · siglas (3). Si algún
   conteo difiere de lo esperado, decir cuál y por qué.
5. **Sin** Anexo A, Anexo B ni Referencias.

## ✎ Verificación de la entrega (2026-08-28)

**Entrega:** `Etapa_1_final_ajustada_pase_5.docx` (22.846 palabras; **con cambios controlados:
173 inserciones / 170 borrados — la primera entrega que los trae**).

| Ítem | Resultado |
|---|---|
| F1 títulos tipo frase | ✅ 39 → 0 (el único "Title Case" residual es *Glass-to-Algorithm*, nombre propio) · los cuatro Bloques con raya |
| F2 rótulo de tabla | ✅ 11 × `**Tabla N**`, ninguno en negrita+itálica |
| F3 rótulo de nota | ✅ 11 × `*Nota.*`, una sola variante |
| F4 punto dentro del rótulo | ✅ 0 casos con el punto fuera |
| F5 terminología | ✅ fotograma 0 · frame 0 · E2E 0 · "end-to-end" solo en "arquitecturas end-to-end" (×2 + título del Bloque A) · "tracking" solo en *tracking-by-detection* y en el nombre de SORT |
| F6 siglas | ✅ IoU definida en la Convención de lectura · SFU y NACK en la Nota de la Tabla 8 |
| Contenido | ✅ las 26 líneas de prosa que cambiaron son todas terminología o rótulo; 22.798 → 22.846 palabras (+48, dentro del ± 60) |
| Verificador | ✅ OK, exit 0 |

**Lectura completa de punta a punta** (las 22.800 palabras, contra el diseño y la
implementación de la plataforma). Dos cosas que ningún pase anterior había visto:

- **E1-57 · 🟠 · una capacidad no implementada descrita como el sistema.** §15.4.3.1 decía que
  la brecha impide predecir *"el desempeño de un sistema que combina **ingesta
  multi-protocolo, decodificación acelerada**, inferencia OVD y emisión de eventos"*. La
  plataforma no tiene ni lo uno ni lo otro (ingesta RTSP + SDK; decodificación por software).
  Texto heredado del v1.1 que PODA-04 conservó al proteger §15.4.3. Corregido a *"ingesta de
  video, inferencia OVD y emisión de eventos"*.
- **E1-58 · 🟠 · formato roto en mitad de palabra.** Tres frases de §16.5.2, §16.5.4 y §16.5.5
  llevaban runs en **negrita+itálica que empezaban y terminaban dentro de una palabra**
  (*"pro|tocolo reproducible sin anticipar la s|elección"*): en Word se ven letras sueltas en
  cursiva negrita. Más el título §16.6.2.1 con negrita parcial a nivel de run. **Venía desde
  la entrega del pase 3** (verificado en las cuatro versiones), no es de esta pasada. Los
  cuatro casos se repararon quitando el formato de run; el estilo del párrafo gobierna.

Ambos arreglos se aplicaron de forma determinista sobre el `.docx`, con validación XML
previa. **Diff contra la entrega: solo los cuatro párrafos afectados.** Verificador OK.

**Documento final de la Etapa 1: `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`.** La entrega de GPT y el
final previo quedaron en `archivado/`.

**Tres frases que NO se tocaron y conviene saber que existen:** *"sin anticipar la estrategia
que adopte el diseño"* (§16.3.4), *"sin anticipar la selección del stack"* (§16.5.5) y *"no se
anticipa en esta sección"* (§16.7.3). Son la regla de no-anacronismo **filtrándose a la prosa**
como comentario del autor sobre su propio texto. Correctas, pero un jurado las lee como
meta-texto. Si se quiere pulir, es borrar la cláusula final de cada una — tres tijeretazos que
pueden hacerse al integrar al maestro.

## 9. Cómo se va a verificar

El equipo corre `verificar_entregable.py` (debe dar **OK**) y un diff palabra por palabra
contra el archivo entregado. **Cualquier cambio fuera de F1–F6 hace rechazar la entrega
entera**, aunque sea una mejora. Si algo del contenido te parece incorrecto, **no lo
corrijas**: anótalo en el registro de cambios y el equipo lo evalúa.
