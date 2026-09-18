# Pase de la Etapa 6 — §17.6, §18 y §19 · v1.0 → v1.1

> **Entregado el 2026-09-09 como SUGERENCIAS Y COMENTARIOS.** Nada en limpio: rechazar todas
> las sugerencias devuelve la v1.0 exacta (verificado).
> Guion: [`herramientas/pase_etapa6_cierre.py`](../../../../herramientas/archivado/pase_etapa6_cierre.py) ·
> Documento: `E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.1 (sugerencias sin aceptar).docx`

Punto de partida: la v1.0 (sha256 `e2cf60e9…`) redactada por el chat de ChatGPT con el kit
`--etapa 6`, con cuatro hilos de comentarios del usuario y de Matías, y el diagnóstico de que
**«a simple vista nos pareció muy extenso el cierre del informe, los anexos se llevan una gran
parte»**.

---

## 1. La medición matiza el diagnóstico

Los anexos **son** más de la mitad del cierre, y de ahí viene la impresión. Pero **no crecieron**:
como bloque quedaron más cortos que en el maestro v1.1.

| Bloque | Prosa | Tablas | Total |
|---|---:|---:|---:|
| §17.6 | 1.145 | — | 1.145 |
| §18 | 2.894 | — | 2.894 |
| §19 Anexos A–D (heredados) | 1.039 | 15 tablas, 2.028 | 3.067 |
| §19 Anexos E–F (nuevos, los pide el contrato) | 1.499 | 3 tablas, 391 | 1.890 |
| Referencias (149 entradas) | 3.798 | — | 3.798 |

| | Maestro v1.1 | Etapa 6 v1.0 |
|---|---:|---:|
| Anexos A–D | 5.302 | 3.067 |
| Anexos E–F | no existían | 1.890 |
| **Total anexos** | **5.302** | **4.957** |

En el informe integrado (~80.000 palabras), §18 pesa cerca del 3,6 % y los anexos cerca del 6 %.

**Dónde estaba la grasa, medida:** §18.2 a §18.4 traían **6 cifras cada 100 palabras**, más que el
propio §17.5, que tiene 4,8 — es decir, re-reportaban las Tablas 61 a 65. Y el Anexo E era el anexo
más largo en prosa (854 palabras), con los últimos párrafos repitiendo reglas ya escritas en §17.5,
§18.4 y §17.6.4. El límite del empaquetado en contenedores estaba enunciado **tres veces** en el
documento.

---

## 2. Lo que este pase NO toca, y por qué

No es prudencia: cada uno está anclado por remisiones de secciones ya cerradas.

| Bloque | Por qué se queda |
|---|---|
| **Anexo A** (561 palabras) | `PODA-17` propone eliminarlo y **su decisión sigue sin marcar**, pero §15.2.3 y §15.3.3 remiten a las Tablas A.1 y A.2 por número. Las dos tablas son copia fila a fila de `90e`. |
| **Anexo B** (1.133) | §17.1.4 remite al Anexo B. Respecto del maestro fue reescrito de «candidato» a «utilizado / no ejercido», que es lo correcto. |
| **Anexos C y D** (651 y 722) | §17.1 remite a las seis tablas C.1–C.3 y D.1–D.3 **por número**. Verificado: son idénticas fila a fila a `90g`. `ajustes/07` §7 declara que B, C y D no se podan porque son el destino de lo que sale del cuerpo. |
| **Anexo F** (770) | Es la evidencia que pide `AJ-6.03` (licencias, consentimientos, procedencia). Contiene el único `[[PENDIENTE]]`, que depende de C1. |
| **La serie de las cuatro cadencias en 18.4** | Se intentó pasarla a prosa y la versión narrativa salía **más larga** y con menos información: 23 palabras para cuatro pares es más compacto que cualquier paráfrasis. El cambio se descartó. |

---

## 3. Lo aplicado

### 3.1. Los cuatro hilos de comentarios

| Hilo | Qué se hizo |
|---|---|
| 17.6.1 · «medio al vicio … eso ya es cosa nuestra» + «si, no suma» | Baja de las dos oraciones sobre el repositorio documental. Estaban porque `AJ-6.04` las pedía, pero describen cómo trabajó el equipo, no la plataforma evaluada. Sobreviven las dos que hablan del software. |
| 17.6.4 · «he» / «ya se que es» / «pero palabra rancia» | «contenedorización» → **«empaquetado en contenedores»**. Salía una sola vez y el resto del documento ya decía «empaquetado», así que además unifica el término. El contenido no se toca: coincide con el estado real (compose validado, builds y smoke sin correr). |
| 18.5 · «llamarlas de otra forma, no hay contexto de que son» (T1/T2/T3) | **Verificado y confirmado**: ni §17.4 ni §17.5 usan esas etiquetas (cero menciones). Dicen «la escalera de tres tramos», «el primer tramo entrenó sólo la proyección de clases», «el ajuste de mayor capacidad». Se reemplazan por esos nombres en las seis apariciones. Cuesta +10 palabras y las paga. |
| 19.5 · «esto no se de qué es, si va en el anexo o se coló de algún otro lado» | **Sí va acá**: es la cadena de reproducción que pide `AJ-6.02`. Le faltaba la oración que dice de qué material habla y que abre las tres secuencias siguientes. Se agrega. |

### 3.2. Compresión

| Bloque | Antes | Después | Δ |
|---|---:|---:|---:|
| §17.6 | 1.145 | 1.092 | −53 |
| §18 | 2.894 | 2.814 | −80 |
| Anexo E | 854 | 838 | −16 |
| Referencias | 3.798 | 3.769 | −29 |
| **Cuerpo sin Referencias** | **8.996** | **8.847** | **−149 (−1,7 %)** |

Densidad numérica, que era la crítica de fondo:

| | v1.0 | v1.1 |
|---|---:|---:|
| §18.2 | 6,2 | 4,0 |
| §18.3 | 5,7 | 4,1 |
| §18.4 | 6,4 | 6,1 |

Las tres quedan en o por debajo de §17.5 (4,8), que es donde las cifras deben vivir.

**Criterio aplicado:** se conserva la cifra que **es** la conclusión (el par 0,930 contra 0,789, el
veto de precisión 0,146 contra el umbral 0,5, la reducción de retención del 71,3 %) y se remite a la
tabla para las series completas, los denominadores repetidos y los conteos de contexto. Además se
quitaron tres repeticiones literales: el par 0,930/0,789 estaba escrito dos veces con las mismas
palabras (§18.1 y §18.3), el límite del empaquetado tres veces, y el «byte a byte» dos.

**−149 palabras es lo que el texto soporta sin perder contenido.** El §18 no tiene relleno: cada
párrafo trae una afirmación, su evidencia y su calificación de fuerza, que es exactamente lo que
pide `AJ-6.01`. Un recorte mayor exige decidir qué conclusión se va, y eso no es trabajo del pase
— ver §5.

### 3.3. Referencias — el hallazgo que bloqueaba la integración

La lista de la v1.0 fusionó `90e` en el maestro y podó las huérfanas, que era lo pedido. Pero además
**actualizó tres preprints a su versión publicada y re-letró los sufijos de NVIDIA**, y eso dejaba
sin resolver citas de secciones que este documento no puede editar. `verificar_entregable.py` no lo
ve, porque sólo chequea las citas del propio `.docx`.

| Entrada | v1.0 | v1.1 | Quién la citaba |
|---|---|---|---|
| L. H. Li y otros, GLIP | 2022 (CVPR) | **2021** (arXiv) | §15/16 y la nota de la Tabla A.1 |
| Gu y otros, ViLD | 2022 (ICLR) | **2021** (arXiv) | §17.1 y el Anexo C |
| Shen y otros, APE | 2024 (CVPR) | **2023** (arXiv) | §15/16 y la nota de la Tabla A.1 |
| Chen y Zou | **duplicada** (2025 y 2026) | sólo 2025 | §15/16 cita 2025; §18.1 citaba 2026 (corregido) |
| NVIDIA, Grounding DINO TAO | s. f.-b | **s. f.-g** | §15/16 |
| NVIDIA, Triton | s. f.-c | **s. f.-h** | §15/16 |
| NVIDIA, Video Codec SDK | NVIDIA, s. f.-d | **NVIDIA Corporation, s. f.-b** | §17.1 |
| May, 2017, RFC 8216 | bajo «Pantos, R. (Ed.), y May, W.» | **«May, W. (2017)»**, en su lugar alfabético | §15/16 |
| Roy (Whalen), 2024 | **dada de baja** | restaurada | §15/16 |

**Resultado verificado:** §15, §16, §17.3, §17.4, §17.5 y este documento resuelven **todas** sus
citas contra la lista. Antes había 10 sin entrada. La lista quedó en 149 entradas (dos bajas, dos
altas), **sin pares fuera de orden alfabético** y sin duplicados de obra.

Y de paso: «respaldan el estado del **artel**» → «del arte» (§19.1).

---

## 4. Compuertas

| Compuerta | Resultado |
|---|---|
| Rechazar todas las sugerencias devuelve la v1.0 | ✅ texto idéntico (98.840 caracteres), 18 tablas, 0 figuras, 884 párrafos |
| Integridad OPC del paquete | ✅ íntegro |
| Comentarios previos conservados | ✅ los 8 siguen anclados; 13 nuevos, uno por bloque discutible |
| Tests de las herramientas | ✅ 67 passed, 53 subtests |
| `verificar_entregable.py` | las **mismas 2 fallas que la v1.0**, ambas conocidas y falsas (ver §5) |

---

## 5. Lo que queda para el usuario

**Decisiones editoriales de recorte mayor** (ninguna es del pase; todas tocan material cerrado):

1. **`PODA-17` sigue sin marcar.** Eliminar el Anexo A ahorra 561 palabras, pero hay que mudar las
   Tablas A.1 y A.2 a §15 o al Anexo B, o quedan dos remisiones colgadas en §15.2.3 y §15.3.3.
2. **Anexos C y D** (1.373 palabras) son catálogos del **protocolo**, no resultados. Sacarlos exige
   cambiar seis remisiones por número en §17.1.
3. **Fundir §18.6 con §18.1**, que son las dos caras del mismo balance, ahorraría del orden de 150
   palabras de andamiaje.

**Dos defectos del verificador y de §17.1, no del documento:**

4. `verificar_entregable.py` marca **fuga de andamiaje** sobre la huella SHA-256 completa de la Tabla
   E.2. Es un **falso positivo**: las once huellas de esa tabla se comprobaron contra disco y son
   correctas (`clip_bench/manifest.yaml` `3f14f50a…`, `bench_v3.json` `4557024e…`, los cuatro
   estratos del manifiesto, el manifiesto histórico del rodaje `cef5082e…` y los tres prompt sets).
   Hay que aflojarle el patrón al verificador. La otra falla, «§17 arranca en 6», es esperable en un
   `.docx` por sección.
5. **§17.1 cita «Axis Communications AB, s. f.»** mientras la entrada —y §15/16— dicen 2015. Es
   anterior a la Etapa 6 y hay que corregir la cita al integrar; la entrada es la correcta.

**Para la integración**, además de lo que ya lista `00-lo-que-resta` §4:

6. Si se prefiere la **versión publicada** de los tres preprints (sube la proporción de fuentes
   arbitradas, que era una recomendación de la auditoría del 09-08), hay que cambiar estas citas:
   «L. H. Li et al., 2021» en §15/16 y en la nota de la Tabla A.1, «Shen et al., 2023» en las dos
   mismas, «Gu et al., 2021» en §17.1 y en el Anexo C, y «Chen y Zou (2025)» dos veces en §15/16.
7. Los **sufijos de NVIDIA** quedan con huecos (`s. f.-a`, `-g`, `-h`), herencia de haber podado las
   huérfanas de esa autoría. Cerrarlos exige renumerar y tocar cuatro citas en §15/16 y §17.1.
8. **§17.6 no menciona el repositorio público `e-ovrt-vdp`**, que según el `CLAUDE.md` es la única
   referencia externa que cita el informe. El kit tampoco lo pide. Decisión del usuario.

**De la auditoría bibliográfica del 09-08** quedó ejecutada la parte del cierre (fusión de `90e`,
las 12 entradas faltantes, las altas de Milan 2016 y Liang y Han 2024, la baja de AAIP s. f.-b).
Sigue abierto lo que no vive en §19: la **Figura 4.3**, que dibuja dos transiciones que el motor no
hace, y el mismo error en el texto de 17.3.6.1.
