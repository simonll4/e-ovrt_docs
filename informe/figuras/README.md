# Figuras del informe — producidas, listas para insertar

Las **cinco figuras** que `ajustes/08` §6 y `gobierno/99` §1 listaban como lo único que
faltaba producir. Con esto, **el inventario de materiales del informe queda completo**:
las 17 tablas (`T-68`…`T-85`) y `FIG-D` ya estaban en disco y se llenan copiando desde
su artefacto; estas cinco eran trabajo real y están hechas (2026-08-21).

> **Regla que gobierna esta carpeta:** ninguna figura se dibuja "a mano" desde una tabla
> intermedia. Cada una declara su artefacto de origen y, cuando la cifra vive en un
> `metrics.json`, el script **la lee de ahí y falla si no coincide con el índice
> publicado**. Es la misma disciplina que las tablas: el inventario dice cuál es la
> fuente, y la fuente es la que manda.

## Qué hay acá

| Figura | Archivo | Va en | Origen |
|---|---|---|---|
| **FIG-A** | `fig-a-vista-de-procesos` | **§17.4.1** | especificación de `ajustes/material-etapa-3/94` §4 (R-09) + enmienda 08-18 |
| **FIG-B** | `fig-b-calidad-vs-densidad` | §17.5 | `results/clip_bench/{t1,g1,r1…r6}/metrics.json` (leídos y verificados) |
| **FIG-C** | `fig-c-alerta-confirmada` | §17.5 | fotograma de `defensa/videos/V1_a_p1_c04.mp4`, t = 8,5 s |
| **FIG-E** | `fig-e-maquina-de-estados` | **§17.3.8.2** | contrato `pattern_events` (`control-plane/engine/pattern_engine.py`) |
| **FIG-F** | `fig-f-frontera-juzgabilidad` | §17.5 | `operacion/103` §7.1 (panel A) · `operacion/105` §4.1 y F-105.3 (panel B) |

Cada figura está en **PNG a 300 dpi** (el que se inserta en el `.docx`) y en **SVG**
(vectorial, por si hay que retocar). Ancho de diseño: **16 cm**, la columna del informe
— insertar a ese ancho y no reescalar, que es donde se eligieron los tamaños de letra.

## Cómo se regeneran

```bash
cd docs/informe/figuras/scripts
MP=../../../../e-ovrt_media-plane/.venv/bin/python
$MP fig_a_vista_de_procesos.py
$MP fig_b_calidad_vs_densidad.py      # falla si las cifras no coinciden con el índice
$MP fig_e_maquina_de_estados.py
$MP fig_f_frontera_juzgabilidad.py
# FIG-C es una extracción de fotograma; ver §FIG-C abajo
```

Se usa el venv del media-plane porque es el que tiene `matplotlib`. `estilo.py` concentra
paleta, tipografía y cromo: **tocar ahí cambia las cuatro figuras a la vez**.

### La paleta está validada, no elegida a ojo

Los tres colores (`#2a78d6` azul · `#eb6834` naranja · `#1baf7a` aqua) pasaron el
validador de seis chequeos en modo claro sobre la superficie del informe: banda de
luminosidad, piso de croma, separación para daltonismo (peor par ΔE 9,2 deutan en la
terna; 24,7 en el par), piso de visión normal y contraste. **El aqua queda con contraste
2,74 (<3:1)**, así que por regla de relieve toda serie de ese color lleva **etiqueta
directa visible** — está aplicado en FIG-F y no debe quitarse.

### Una trampa que ya costó una vuelta

`savefig(bbox_inches="tight")` **expande el lienzo hasta abarcar la línea de texto más
larga**. Una nota al pie sin cortar produjo un PNG de 4.083 px de ancho para una figura
de 6,3 pulgadas: insertado a 16 cm, eso achica *toda* la figura a la mitad y deja los
ejes ilegibles. Por eso las notas van por `nota_al_pie()`, que corta a 112 caracteres.
Si agregás texto al pie, usá esa función; no llames a `fig.text` directamente.

---

## Nota al pie de cada figura (para pegar en el documento)

Las figuras **no llevan título horneado**: el epígrafe (`Figura N — …`) lo pone Word, y
duplicarlo dentro de la imagen se lee como descuido de edición. Lo que sí llevan
impreso es la línea de procedencia, que es la que las hace verificables por un tercero.

**FIG-A — Vista de procesos de la plataforma experimental.**
> La figura representa la disposición efectiva de procesos del prototipo, complementaria
> de la vista lógica de la Figura 4.1. Los tres módulos de la cadena se ejecutan como
> servicios independientes gobernados por configuración y pueden disponerse en un mismo
> host o en hosts distintos sin modificar su lógica.

⚠ **Dos cosas que la figura corrige respecto de la especificación original, y que el
texto debe acompañar:** (a) el módulo de distribución va en **línea continua** —desde
ADR-019/020 es un servicio HTTP más, disparado por el orquestador igual que los otros
dos—, no punteada como "capacidad especificada y no implementada"; la nota al pie vieja
de `94` §4 quedó **falsa** y está reemplazada allí mismo. (b) El **orden de arranque es
el inverso del flujo de datos** (①distribución → ②control → ③medios): cada consumidor
queda suscripto antes de que su productor emita, porque en PUB/SUB lo publicado antes de
la suscripción se pierde. La especificación numeraba "1º control, 2º medios" porque es
anterior a que la distribución fuera servicio; el dibujo sigue el orden operativo
vigente. **Confirmalo antes de cerrar la sección.**

**FIG-B — Calidad contra densidad de evidencia.**
> Campañas t1/g1 (stride 1) y r1–r6 (strides 7/15/26) sobre el banco de 34 clips del
> rodaje; modelo gdino-tiny-560 y prompts cr01_cr02_v2_short en las ocho, variable única
> el stride. Los clips negativos no entran a F1 —su métrica son los falsos positivos,
> 0/4 en las ocho campañas— y no se grafica el SDR, que no es comparable entre cadencias
> (F-96.6). Con 34 episodios evaluables, las diferencias menores a ~0,02 están dentro de
> la resolución del banco y no se leen como orden.

**FIG-C — Fotograma con alerta confirmada.**
> Fotograma en t = 8,5 s de la corrida sobre el clip `a_p1_c04` con la combinación T1 del
> banco (gdino-tiny-560 + `cr01_cr02_v2_short` + patrón CR-01, `confirm_after_ms` = 4 s).
> La alerta se emitió en t = 7,3 s; el estado del motor en el instante mostrado es
> `sustained`. La línea de tiempo al pie marca la primera evidencia y el instante de la
> alerta.

Detalle que conviene señalar en el texto: el casco **está detectado sobre la mesa**, y no
suprime CR-01 — la condición es sobre el sujeto, no sobre la escena.
Hay dos archivos: `fig-c-alerta-confirmada.png` (recortada la banda de cabecera del
renderer de defensa, **es la que va al informe**) y `fig-c-alerta-confirmada-completa.png`
(fotograma íntegro, conserva el rótulo del video V1 y la línea de procedencia del
renderer; queda como respaldo).

**FIG-E — Máquina de estados del motor de patrones.**
> Estados y transiciones del contrato `pattern_events` del plano de control. La alerta se
> emite en la transición de entrada a `confirmed`: entre la primera evidencia y la alerta
> media una condición temporal (`confirm_after_ms`), y eso es lo que separa una detección
> de una alerta. `sustained` es el estado de régimen —la evidencia que sigue llegando lo
> mantiene ahí sin producir un cambio de estado nuevo—, de modo que un episodio
> prolongado no multiplica alertas.

⚠ Son **cinco** estados y el rótulo de tres (`open → confirmed → resolved`) que circuló
antes es incorrecto (enmienda del 08-19). Dos detalles del comportamiento real que el
dibujo respeta: desde `inactive`/`resolved` se puede **saltar directo a `confirmed`** si
la condición ya se cumple con el primer evento, y a `resolved` se llega por **dos caminos
distintos** (despeje sostenido o ausencia por encima del tiempo de expiración). La
reapertura va de `resolved` a **`candidate`**, no a `inactive`: `inactive` es sólo el
estado inicial.

**FIG-F — Frontera de juzgabilidad: escala × iluminación × oclusión.**
> Panel A: asociación de chaleco por banda de altura del sujeto sobre las detecciones
> crudas de la campaña I1 (clips v06 y v10 diurnos, v04 nocturno); el tramo ≥320 px de
> v10 no fue medido y por eso la serie se corta. Panel B: los cuatro clips con referencia
> humana y Nivel A medido; el de sujetos más grandes rinde F1 0,084 por oclusión mutua,
> no por escala (F-105.3). La frontera tiene al menos tres ejes y ninguno de los tres,
> por sí solo, predice si el material es evaluable.

Al citarla: el régimen donde el rodaje validó la plataforma (≥320 px, diurno, asociación
96–100 %) **es un régimen, no una garantía general** — el estrato B vive fuera de él, y
eso es justamente lo que la figura muestra.

---

## Lo que estas figuras habilitan

- **§17.3.8.2** ya tiene FIG-E ⇒ la puerta P4 de esa sección deja de estar bloqueada por
  material faltante.
- **§17.4.1** ya tiene FIG-A ⇒ ídem para §17.4, y es la respuesta gráfica al "cómo está
  hecho" que pidió el tutor técnico (R-09).
- **§17.5** ya tiene FIG-B, FIG-C y FIG-F ⇒ la sección de resultados se puede escribir con
  sus figuras delante, que es la regla del §6 de `ajustes/08`: *un capítulo escrito sin sus
  figuras se reescribe*.
