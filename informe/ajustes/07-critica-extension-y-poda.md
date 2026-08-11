# Crítica de extensión — qué podar del informe, sección por sección

- **Fecha:** 2026-08-11
- **Qué es esto:** la crítica de **extensión** del informe v1.1, medida y sección por
  sección: qué eliminar porque **ya no se alinea con la plataforma que se construyó**, y
  qué comprimir porque **no suma** al argumento. No existía: el `93` audita *corrección*
  (26 redlines), `nucleo/historicos/02` auditó *contenido* de Etapa 3, y el "orden de
  sacrificio" del `95` era de redlines contra tiempo. Ninguno mide longitud.
- **Método:** conteo de palabras por sección sobre el texto extraído (`entregable/90`,
  `96a`–`96e`), contrastado contra lo que la plataforma **es** (E-IND · GDINO-560 ·
  dos planos servicios HTTP · bus ZeroMQ · bench_v3 · clip bench · sin fine-tuning ·
  sin métricas MOT · sin inferencia en borde · distribución como trabajo comprometido).
- **Serie de IDs: `PODA-nn`** (prefijo verificado libre). Ortogonal a `AJ-`/`R-`: un
  mismo pase por sección aplica los dos. Cada ítem lleva casilla de decisión, como el 93.
- **La decisión final es tuya**: esto propone; ninguna poda se aplica desde acá.

> **✅ Regla de gobierno fijada por el usuario (2026-08-11): no hay límite institucional
> de extensión, y no se poda por cuota — se poda por aporte.** *"Todo lo que tenemos que
> desarrollar tiene que sumar."* Consecuencias operativas:
> 1. **El filtro único es el aporte**: una sección se queda si sostiene un resultado,
>    una decisión de diseño o un argumento de defensa. Si no sostiene nada, no va — sin
>    importar cuánto costó escribirla.
> 2. **No existe "segunda vuelta" sobre §17.1.5/§17.1.7**: bajo este criterio no se
>    comprime prosa del protocolo ejercido para llegar a un número. Las 18 podas de este
>    documento se justifican todas por desalineación o no-aporte, ninguna por cuota.
> 3. **La misma vara gobierna lo que falta escribir**: §17.4, §17.5 y §17.6 se redactan
>    al largo que su contenido exige y ni una palabra más — los insumos ya están
>    inventariados (T-68…T-84, FIG-A…F), y relleno alrededor de una tabla verificable
>    es dilución, no desarrollo.

---

## 1. El diagnóstico en números

**El informe ya tiene ~127.000 palabras** (≈280+ páginas de cuerpo) **y las tres
secciones más importantes todavía no existen** (§17.4, §17.5, §17.6, que van a sumar
15–20k más). El problema no es solo estético: un tribunal que atraviesa 60 páginas de
surveys de tecnologías no usadas llega cansado a los resultados.

| Bloque | Palabras | % | Estado de alineación |
|---|---:|---:|---|
| §2–§14 frontmatter (`96a`) | 4.530 | 3,6% | OK — se corrige (AJ-0.x), no se poda |
| §15 Estado del Arte (`96c`) | 21.575 | 17,0% | **8.000 de streaming/servidores** para una decisión que colapsó |
| §16 Marco Teórico (`96d`) | 31.732 | 25,0% | **13.285 en §16.5** (transmisión/aceleración/arquitecturas/borde) |
| §17.1 Consolidación (`96b`) | 32.222 | 25,4% | protocolo ejercido (se queda) + **5.054 de catálogo de datasets** viejo |
| §17.3 Diseño (`90`) | 24.389 | 19,2% | lo opera el `93`; acá solo 2 ítems de longitud |
| §18–§19 + Referencias (`96e`) | 12.339 | 9,7% | anexos se completan; Anexo A pierde función |
| **Total escrito** | **≈126.800** | 100% | |

**El titular, y es uno solo:** los dos temas **más desalineados** con la plataforma
final están cubiertos **dos veces** — una en el estado del arte y otra en el marco
teórico:

- **MOT / seguimiento multiobjeto:** §15.3 (2.484) + §16.4 (2.769) = **5.253 palabras**
  — para un proyecto que **excluyó las métricas MOT** (E-10, con fundamento medido:
  F-89.1, las detecciones son bit a bit las mismas) y cuya ganancia por sujeto se mide
  en la métrica de la plataforma, no en MOTA/IDF1.
- **Streaming / arquitecturas de video / borde:** §15.4 (7.998) + §16.5.3–16.5.5
  (8.009) = **16.007 palabras** — para una plataforma cuyo espacio de decisión colapsó a
  *"RTSP de entrada, bus ZeroMQ adentro, archivo como verdad"*, que usa mediamtx solo
  como herramienta de desarrollo, y que **excluyó la inferencia en borde** (EN-3; lo
  ejercido es el prefilter EN-2).

Juntos: **~21.200 palabras — el 17% del informe — dedicadas a los dos temas que menos
sostienen el trabajo.** Mientras tanto, el §15 no tiene ni una cifra de la vara
supervisada de EPP (`AJ-1.01`, el hueco que sí importa).

---

## 2. Los cinco criterios de poda

| # | Criterio | Acción |
|---|---|---|
| C1 | **Desalineado**: describe una capacidad/tecnología que la plataforma final no usa, excluyó o refutó | ELIMINAR o comprimir a decisión declarada |
| C2 | **Espacio de decisión colapsado**: survey amplio de opciones cuando la decisión final fue una y está justificada en una página | COMPRIMIR al camino tomado + por qué |
| C3 | **Doble cobertura**: el mismo tema desarrollado en §15 y §16 (o §16 y §17.1) | FUSIONAR — una sola casa por tema |
| C4 | **Meta-texto**: secciones que resumen, anticipan o "proyectan" otras secciones del mismo documento | ELIMINAR — el índice ya hace ese trabajo |
| C5 | **Catálogo sin uso posterior**: listas/tablas de ítems que ninguna sección vuelve a citar | COMPRIMIR a los ítems con rol en el trabajo |

**Regla de honestidad (no negociable, `gobierno/97` §3):** lo **pre-registrado y no
ejercido no se borra en silencio** — se comprime a decisión declarada con su causa y su
costo (el caso testigo: fine-tuning E-04, ≈1 GPU-h medido). Podar no es ocultar.

---

## 3. §15 Estado del Arte (21.575 palabras)

### PODA-01 · §15.2.1 Paradigmas y modelos (4.530) · C5 · 🟠
El catálogo trae **~25 modelos con cifras COCO/LVIS**; el trabajo evaluó **tres familias**
(GDINO, MM-GDINO, YOLOE) y tiene **un** comparable externo (OWLv2). Comprimir a: los 4
paradigmas en un párrafo cada uno + ficha solo de los modelos con rol en el trabajo
(GDINO/MM-GDINO/YOLO-World/YOLOE/OWLv2 · GDINO 1.5/DINO-X como techo de API cerrada) +
la Tabla 3 reducida a esas filas. Beneficio doble: **menos superficie de erratas** — las
AJ-1.04…08 viven justo en las filas que se van (OmDet-Turbo, LLMDet, el caching de 40 ms).
**Ahorro: ~2.000** · DECISIÓN → [ ] acepto [ ] modifico [ ] rechazo

### PODA-02 · §15.2.4 Ventajas/limitaciones/trade-offs (2.764) · C3/C4 · 🟠
Solapa con §15.2.3 (síntesis comparativa, 1.153) y con §16.7. Fusionar 15.2.3+15.2.4 en
una sola síntesis de ~1.200 con tabla. **Ahorro: ~1.500** · DECISIÓN → [ ]

### PODA-03 · §15.3 MOT completo (2.484) · C1 · 🟠
La plataforma **no evalúa MOT**: E-10 excluye MOTA/IDF1 con causa medida, y el tracker
que existe se mide por alertas. Mantener ~800: tracking-by-detection en un párrafo (es lo
que fundamenta G1) + la brecha. **Eliminar §15.3.3 entero** (métricas MOT, 385 — no se
usa ni una) y podar el catálogo de métodos (§15.3.1–15.3.2) a los dos que expliquen el
approach del tracker propio. **Ahorro: ~1.600** · DECISIÓN → [ ]

### PODA-04 · §15.4 Streaming y servidores de medios (7.998) · C1/C2 · 🔴 la mayor
**La sección más desalineada del informe.** 4.041 palabras de protocolos (WebRTC, HLS,
SRT, …) + 2.594 de comparativa de servidores de medios open source + criterios — y la
decisión final fue: **RTSP como ingesta, ZeroMQ+msgpack como bus interno (ADR-003),
mediamtx solo como herramienta de desarrollo, archivo JSONL como verdad**. Ni WebRTC ni
HLS ni la comparativa de servidores sostienen una sola decisión del sistema construido.
Comprimir a ~1.200: panorama mínimo de protocolos de **ingesta** + la brecha
streaming×OVD (§15.4.3, que sí vale). La *justificación de la decisión tomada*
(RTSP en la entrada, bus de eventos adentro) no va acá: es material de §17.1/§17.3
(regla de no-anacronismo — el §15 no relata elecciones del proyecto).
**Ahorro: ~6.800** · DECISIÓN → [ ]

**Lo que el §15 GANA mientras pierde esto:** la vara supervisada (AJ-1.01), el cruce con
la evidencia propia (AJ-1.02) y la Vara 3 OVD×EPP (AJ-1.13). La poda no deja al §15 más
flaco de contenido útil — lo deja con el contenido que la defensa necesita.

---

## 4. §16 Marco Teórico (31.732 palabras)

### Lo que NO se toca (y por qué)
- **§16.3 Percepción visión-lenguaje (2.594)** — es el **corazón conceptual de la
  tesis** (el lenguaje como especificación dinámica; sostiene AF-2/AF-5 y toda la
  narrativa léxico-conceptual). Intacta.
- **§16.2 Condiciones de riesgo observables (3.100)** — es lo que ancla CR-01/CR-02 a la
  normativa; sin esto las condiciones son arbitrarias. A lo sumo podar §16.2.3 (~300).
- **§16.5.1 Latencia end-to-end como restricción (494)** — el eje de tiempo real ES
  central a los resultados (G2A, densidad live). La poda de §16.5 es de *surveys*, no
  del concepto.

### PODA-05 · §16.4 MOT teórico (2.769) · C1/C3 · 🟠
Segunda casa del MOT. Mantener §16.4.1 (la limitación del fotograma — motiva la
histéresis) y §16.4.3 (integración OVD+tracking — motiva G1); comprimir §16.4.2
(fundamentos MOT, 1.600 → ~700) y **eliminar §16.4.4** (criterios de selección de
métodos MOT, 487 — no hubo selección de método de catálogo). **Ahorro: ~1.400** ·
DECISIÓN → [ ]

### PODA-06 · §16.5.2 Descomposición del pipeline (4.874) · C3 · 🔴
Mantener lo que **define G2A y sus componentes** (t_capture/t_transport/t_preprocess/
t_inference — es vocabulario que §17.1.7 y los resultados usan): ~1.400. El resto
duplica lo que §17.1.7 ya formaliza como framework de métricas. **Ahorro: ~3.400** ·
DECISIÓN → [ ]

### PODA-07 · §16.5.3 Arquitecturas de procesamiento de video (3.594) · C1/C2 · 🔴
Survey de frameworks/arquitecturas de video analytics — y la plataforma es **un pipeline
Python propio de dos servicios config-driven**. Comprimir a ~600: el patrón
productor/consumidor como fundamento conceptual; la elección concreta (pipeline propio,
no framework) se justifica en §17.3, no en el marco teórico. **Ahorro: ~3.000** ·
DECISIÓN → [ ]

### PODA-08 · §16.5.4 Computación en el borde (2.729) · C1 · 🔴
**EN-3 (inferencia en borde) está excluida.** Lo ejercido es el prefilter EN-2 on-device
(87% de descarte medido) y la OAK-D como fuente. Comprimir a ~700: el fundamento
**conceptual** del prefiltrado en el borde; la decisión de dónde vive la inferencia (y su
resultado medido) pertenecen a §17.3 y §17.5. **Ahorro: ~2.000** · DECISIÓN → [ ]

### PODA-09 · §16.5.5 Criterios para protocolos y stacks de streaming (1.686) · C2 · 🔴
Criterios de selección para una selección que ya ocurrió y colapsó (ver PODA-04). Un
párrafo puente a la decisión tomada. **Ahorro: ~1.400** · DECISIÓN → [ ]

### PODA-10 · §16.6 Marco ético-legal (4.364) · C5 parcial · 🟠
Tiene núcleo vivo: §16.6.2 (delimitación del tratamiento de datos — **implementada** en
§17.3.12, minimización de evidencia visual) y §16.6.6 (implicaciones de diseño). Podar lo
genérico: §16.6.4 referentes comparados (422), §16.6.5 gobernanza de IA (499), y
comprimir §16.6.7 (955 → ~400). **Ahorro: ~1.400** · DECISIÓN → [ ]

### PODA-11 · §16.7 Convergencias y brechas transversales (4.429) · C4 · 🔴
**Meta-texto puro**: seis subsecciones que re-resumen el propio §16 y anticipan §17.1
("convergencias del análisis", "lectura arquitectónica integrada", "proyección hacia la
consolidación"). El lector ya leyó el §16 y va a leer el §17.1; este puente de 4.400
palabras no aporta contenido nuevo. Fusionar con §16.8 en un cierre único de ~1.000
(el mapa de brechas de §16.7.3 es lo único que se rescata, comprimido). **Ahorro:
~3.400** · DECISIÓN → [ ]

---

## 5. §17.1 Consolidación Metodológica (32.222 palabras)

**Advertencia previa:** este es el capítulo **mejor alineado** del informe — el
protocolo que describe se ejerció casi completo, y `nucleo/historicos/08` §1 documenta
que valida lo construido. La poda acá es quirúrgica, no estructural.

### PODA-12 · §17.1.6.2 Datasets de gestión directa (5.054) · C5 · 🔴
Un catálogo de 5.000 palabras de datasets, escrito **antes** de que la selección
colapsara a **3 datasets TRAIN** (`construction_site_safety`, `chv`, `ppe_siabar`) y un
benchmark (`bench_v3`, 3 fuentes) — y es exactamente lo que **R-24** marca como
inventario desactualizado. Comprimir a: ficha de los efectivamente usados + tabla de
descartados con causa (una línea cada uno). Se corrige y se poda en el mismo pase.
**Ahorro: ~3.000** · DECISIÓN → [ ]

### PODA-13 · §17.1.10 Proyección hacia instancias posteriores (637) · C4 · 🟡
Las "instancias posteriores" **ya ocurrieron** — son §17.4 y §17.5. Reemplazar por un
párrafo puente. **Ahorro: ~450** · DECISIÓN → [ ]

### PODA-14 · §17.1.4 Entorno e infraestructura (3.252) · C5 parcial · 🟡
Parámetros y detalle de infraestructura que el **Anexo B ya existe para alojar**
(1.792). Mover el detalle al anexo, dejar en el cuerpo el diseño de escenarios DBE/EBE.
**Ahorro neto: ~1.000** · DECISIÓN → [ ]

**Lo que NO se toca en §17.1:** §17.1.5 (9.426 — condiciones, patrones y protocolo de
prompts: es el protocolo que SÍ se ejerció; lo no ejercido de adentro —kappa/doble
anotación— se **declara**, AJ-2.06, no se borra) · §17.1.7 (6.605 — el framework de
métricas es la fuente del diccionario y de todo §17.5).

---

## 6. §17.3 Diseño arquitectónico (24.389 palabras)

**Acá opera el `93` (26 redlines), no esta crítica** — podar §17.3 por extensión
mientras se le aplican redlines de corrección es operar dos veces el mismo texto. Solo
dos ítems son de pura longitud:

### PODA-15 · §17.3.15 Roles CPN/EN/TN (1.319) · C1 parcial · 🟡
**R-17 ya pide** convertir esto en tabla rol→contenedor. El TN (nodo de entrenamiento)
no se ejerció (E-04). Al aplicar R-17, dejar la tabla + ~300 palabras, no la prosa
completa. **Ahorro: ~700** · DECISIÓN → [ ]

### PODA-16 · §17.3.17 Backlog (1.101) · C5 · 🟡
**R-21 ya reescribe** el estado de los 16 ítems. Al aplicarlo, comprimir las Tablas
58/59 al estado final con referencia, sin la prosa de justificación ítem por ítem.
**Ahorro: ~500** · DECISIÓN → [ ]

---

## 7. §18, §19 y Referencias (12.339 palabras)

### PODA-17 · §19.1 Anexo A — comparativas técnicas (749) · C3 · 🟡
Con la vara supervisada dentro del §15 (AJ-1.01/1.13), el anexo de "estado del arte
complementario" pierde su función. Rescatar lo vivo (la Tabla A.1 con las licencias
**corregidas** — AJ-1.09) hacia §15 o Anexo B, y eliminar el resto. **Ahorro: ~500** ·
DECISIÓN → [ ]

### PODA-18 · Referencias (5.886) · consecuencia · 🟡
Se poda sola al caer las secciones (los ~25 modelos, los protocolos, los servidores de
medios arrastran decenas de entradas), y el pase de AJ-1.10 unifica duplicados
(Liu 2023/2024, Lin 2014/2015, Ren a/b/c). **Ahorro estimado: ~800** · DECISIÓN → [ ]

**Anexos B/C/D: no se podan** — son el destino natural de lo que sale del cuerpo
(PODA-14) y del anexo de reproducibilidad (`AJ-6.02`).

---

## 8. Tablero de poda

| ID | Sección | Hoy | Acción | Ahorro | Pri |
|---|---|---:|---|---:|---|
| PODA-01 | §15.2.1 catálogo de modelos | 4.530 | comprimir a modelos con rol | ~2.000 | 🟠 |
| PODA-02 | §15.2.3+.4 síntesis duplicada | 3.917 | fusionar en una | ~1.500 | 🟠 |
| PODA-03 | §15.3 MOT | 2.484 | comprimir; eliminar métricas MOT | ~1.600 | 🟠 |
| PODA-04 | §15.4 streaming/servidores | 7.998 | **comprimir a decisión tomada** | **~6.800** | 🔴 |
| PODA-05 | §16.4 MOT teórico | 2.769 | mantener lo que motiva G1/histéresis | ~1.400 | 🟠 |
| PODA-06 | §16.5.2 pipeline | 4.874 | mantener solo definición de G2A | ~3.400 | 🔴 |
| PODA-07 | §16.5.3 arquitecturas de video | 3.594 | comprimir a patrón usado | ~3.000 | 🔴 |
| PODA-08 | §16.5.4 borde | 2.729 | comprimir a EN-2 + exclusión EN-3 | ~2.000 | 🔴 |
| PODA-09 | §16.5.5 criterios streaming | 1.686 | párrafo puente | ~1.400 | 🔴 |
| PODA-10 | §16.6 ético-legal | 4.364 | podar genérico, mantener lo implementado | ~1.400 | 🟠 |
| PODA-11 | §16.7 convergencias | 4.429 | **fusionar con 16.8, es meta-texto** | ~3.400 | 🔴 |
| PODA-12 | §17.1.6.2 catálogo datasets | 5.054 | comprimir a usados + descartes (con R-24) | ~3.000 | 🔴 |
| PODA-13 | §17.1.10 proyección | 637 | párrafo puente | ~450 | 🟡 |
| PODA-14 | §17.1.4 infra | 3.252 | detalle al Anexo B | ~1.000 | 🟡 |
| PODA-15 | §17.3.15 roles | 1.319 | con R-17: tabla, no prosa | ~700 | 🟡 |
| PODA-16 | §17.3.17 backlog | 1.101 | con R-21: estado final | ~500 | 🟡 |
| PODA-17 | §19.1 Anexo A | 749 | eliminar tras AJ-1.01/1.09 | ~500 | 🟡 |
| PODA-18 | Referencias | 5.886 | consecuencia + AJ-1.10 | ~800 | 🟡 |
| **Total** | | | | **~34.900 (~27%)** | |

**Resultado esperado (consecuencia, no meta):** de ~127k a **~92k escritas**; con
§17.4/§17.5/§17.6 sumadas (15–20k), el informe final queda en ~110k en lugar de ~145k.
✎ 2026-08-11 — **no hay objetivo numérico** (regla de gobierno del encabezado): estas
cifras miden el efecto de podar lo que no aporta, no un tope a alcanzar. No hay segunda
vuelta sobre §17.1.5/§17.1.7.

**Orden recomendado:** los ocho 🔴 primero (son el 65% del ahorro y tienen el riesgo
argumental más bajo: nada de lo que eliminan sostiene un resultado ni un argumento de
defensa). Los 🟠 en el pase de cada sección junto a sus AJ-. Los 🟡 al final.

---

## 9. Guardrails — lo que esta crítica NO autoriza a tocar

1. **§16.3** (visión-lenguaje) y **§16.2** (normativa→condiciones): el corazón
   conceptual y el ancla de CR-01/CR-02.
2. **§17.1.5 y §17.1.7**: el protocolo ejercido y el framework de métricas — son la
   columna vertebral metodológica que §17.5 va a citar.
3. **La latencia como restricción** (§16.5.1) y la definición de G2A: el eje de tiempo
   real es un resultado central, no un survey.
4. **Nada pre-registrado se borra en silencio**: fine-tuning, kappa, TN — se comprimen a
   decisión declarada con causa (regla `97` §3; los textos de declaración ya existen:
   `94` §8, AJ-2.06, AJ-2.11).
5. **Ningún texto que un redline necesita como ancla**: antes de eliminar un párrafo de
   §17.3, verificar que ningún R-xx lo cita como "DICE HOY".
6. **Las adiciones mandan sobre las podas**: AJ-1.01/1.02/1.13 (la vara y el cruce)
   *agregan* al §15 — la poda les hace lugar, no compite con ellas.

## 10. Fuentes

Conteos: medidos el 2026-08-11 sobre `entregable/90` y `96a`–`96e` (por encabezado,
`wc -w` por sección). Alineación: `nucleo/10` (exclusiones E-01…E-13) · ADR-002/003/015/016 ·
`nucleo/14`–`19` (los relevamientos vigentes) · `operacion/97` (la plataforma verificada) ·
`sintesis/resultados-y-conclusiones.md` §7 (lo que el §15 debe ganar) ·
`material-etapa-3/93` (los redlines con los que esta poda se coordina).
