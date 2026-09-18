#!/usr/bin/env python3
"""§17.5 v1.5 → v1.6: pase 5 de la Etapa 5, como SUGERENCIAS y COMENTARIOS.

Aplica la lista de trabajo de `desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md` §8
para §17.5, con las cuatro decisiones que el usuario firmó en la recomendación el 2026-09-07:
las ocho limitaciones se restauran tal como estaban, las tres figuras se insertan por XML,
§17.1 recibe sus tres correcciones hacia atrás (en su propio pase) y §15/16 va completo.

Bloqueantes que cierra:
  E5-B1  el párrafo de las ocho limitaciones vuelve al final de 17.5.7
  E5-B2  FIG-F, FIG-C y FIG-B entran como Figuras 4.6, 4.7 y 4.8 con su epígrafe
  E5-B3  «medida sobre 23 episodios confirmados» era el conteo de clips con CR-01 confirmado,
         no el denominador de la media: verificado contra `metrics.json` de la línea de base,
         la media de CR-01 se promedia sobre 21 clips y la de CR-02 sobre 7

Hallazgo nuevo de este pase (no estaba en la lectura transversal): la columna de latencia de
la Tabla 63 declara `matched`, los episodios confirmados, mientras que la media se promedia
**por clip** con alerta confirmada. Son distintos cuando un clip contiene las dos condiciones
(28 vs 26 en la línea de base, 33 vs 29 con granularidad por sujeto). La nota lo dice ahora.

Importantes que cierra: E5-I1 (llamadas de las Tablas 62 y 63), E5-I2 («frontera de de juicio»),
E5-I3 (oración duplicada), E5-I4 (fps del vivo contra densidades de remuestreo), E5-I5 (fecha de
la referencia del recall), E5-I6 (términos sin introducir), X-6 (métricas sin estado), X-7
(calibración contra congelamiento), X-9 (Escenario A y B), X-10 (equivalencias de nombres),
X-11 (los dos materiales de obra real), X-14 (MM-Grounding DINO), y los menores del §5.

Toda cifra nueva rastrea a `results/`: las medias por clip salen de
`clip_bench/t1_gdinotiny560_v2short_scene/metrics.json` (`by_clip`), las densidades de
remuestreo de las campañas r1–r6 (strides 7, 15 y 26 sobre 30 fps) y el descarte de
MM-Grounding DINO del índice del banco de imágenes.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE (2026-09-07).
# El usuario bajó los `.docx` de Google Docs con comentarios propios. Este guion parte de la base
# archivada y sobrescribe el destino, de modo que volver a correrlo PISA ese trabajo. El motor deja
# un respaldo automático y avisa, pero la regla es: para cambiar algo sobre la versión vigente, se
# escribe un pase incremental que la tome como origen, no se re-corre este.

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
FIGS = Path("/home/simonll4/projects/docs/informe/figuras")
ARCHIVO = BASE / "archivado"
# el documento de partida se archivó el 2026-09-07; la ruta queda para poder repetir el pase
SRC = ARCHIVO / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.5 (base del pase 5; se recupera rechazando las sugerencias de la v1.6).docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.6 (sugerencias sin aceptar).docx"

ANCHO_16CM = 5760720   # 16 cm en EMU, el ancho de diseño de las figuras

LIMITACIONES = (
    "Ocho limitaciones acotan la lectura de todo lo anterior. La tasa de falsas alarmas por "
    "hora no sostiene una cota operativa. La referencia temporal no tuvo doble anotación ni "
    "medida de acuerdo entre anotadores, y los bordes de episodio se adjudicaron por criterio "
    "único en seis clips. El material guionado proviene de un solo bloque de rodaje, y la "
    "medición sobre obra real precisó esa limitación sin levantarla, porque caracteriza por "
    "mecanismo dónde el sistema deja de ser evaluable en lugar de validarlo sobre obra real. "
    "Los escenarios quedaron desbalanceados, de modo que todo resultado se reporta por estrato "
    "además del agregado. El seguimiento no se midió en obra real con multitud. Una de las "
    "fuentes de imágenes conserva licencia parcial. Y la condición de chaleco no quedó cerrada "
    "al nivel del estado por persona."
)

FRONTERA = (
    "Esa frontera tiene al menos tres ejes y ninguno de los tres, por sí solo, anticipa si el "
    "material es evaluable. La escala ordena dentro de un mismo régimen de luz. En los clips "
    "diurnos del estrato de obra real, la proporción de sujetos detectados a los que se asocia "
    "un chaleco pasa de alrededor del 10 % en la banda de 80 a 120 píxeles de altura a entre 63 "
    "y 73 % en la banda de 220 a 320, y en el bloque de rodaje, con medianas de altura por "
    "encima de 700 píxeles, esa misma asociación se sostuvo entre 96 y 100 %. La iluminación "
    "desplaza la curva entera, porque en el clip nocturno del estrato las mismas bandas quedan "
    "entre 6 y 13 %. Y la oclusión invierte el orden de los dos ejes anteriores, ya que el clip "
    "con los sujetos más grandes del conjunto, con mediana de 370 píxeles, quedó entre los peores "
    "resultados con F1 0,084 sobre una cuadrilla apiñada en la que el 58,5 % de las personas "
    "aparece solapada con otra. Tampoco la juzgabilidad humana anticipa la del sistema, porque el "
    "clip con la segunda proporción más baja de cuadros no observables para el anotador rindió el "
    "peor F1 del conjunto."
)

NO_COMPUTADAS = (
    "El marco de métricas admite además medidas que esta evaluación no reporta, y su estado se "
    "declara en lugar de omitirse. El tiempo hasta la primera detección se computó en todas las "
    "campañas y no se informa acá, porque la comparación entre combinaciones se resolvió con la "
    "latencia de alerta, que es la que integra el motor temporal. La precisión media promediada "
    "sobre el rango de umbrales de solapamiento y el percentil 99 de latencia quedaron sin "
    "computar, el primero porque la lectura se fijó en un único umbral y el segundo porque las "
    "corridas en vivo procesaron entre 20 y 295 unidades, muy por debajo de lo que ese percentil "
    "requiere. El consumo de memoria del acelerador se registró por corrida y no se consolidó "
    "como resultado comparativo, porque describe al perfil cargado y no a la combinación "
    "evaluada. Los benchmarks públicos de seguimiento multiobjeto previstos en la estrategia de "
    "datos no se ejecutaron, por la misma falta de referencia de identidad que excluyó a sus "
    "métricas."
)


def main() -> int:
    d = Documento(SRC)

    # ---------------------------------------------------------------- 17.5.1 Encuadre
    # X-9: cada pregunta declara a qué escenario del protocolo pertenece.
    d.agregar_al_final(2, (
        " Las mediciones de percepción, estado por persona y alerta por episodio pertenecen al "
        "Escenario A, sobre material congelado y relectura por archivo, y las de tiempo real al "
        "Escenario B, sobre captura continua."))

    # X-10: los nombres cortos de §17.5 se atan a los del marco de métricas de §17.1.
    d.agregar_al_final(3, (
        " Los nombres abreviados de esta sección son los del marco de métricas. La latencia de "
        "alerta mide el intervalo entre el inicio del episodio anotado y su alerta confirmada, y "
        "la cobertura del episodio, que las tablas abrevian SDR, expresa qué proporción del "
        "tiempo con la condición activa mantuvo evidencia correcta."))

    # Bloqueante 3 de la lectura transversal: la descomposición del banco temporal, explícita.
    d.reemplazar(4,
                 "Esta descomposición no debe confundirse con los 34 clips del bloque de rodaje guionado.",
                 "Lo integran 34 clips de un bloque de rodaje guionado y 13 de un estrato de obra "
                 "real no guionada.")

    # ---------------------------------------------------------------- 17.5.2 Percepción
    # X-4: el perfil operativo y su contraste comparten configuración; el par vive en §17.4.4.
    d.agregar_al_final(8, (
        " Las dos comparten resolución de entrada y umbrales, que declara la sección 17.4.4, y "
        "difieren en el tamaño del perfil."))

    # Coherencia entre la columna de recall y la estrategia que el núcleo adoptó (2026-09-07).
    # `evaluate_cr01` cuenta sólo detecciones de cabeza descubierta, o sea la formulación
    # DIRECTA. El núcleo opera con la indirecta, que deriva la ausencia desde persona y casco,
    # de modo que la columna no mide la capacidad del núcleo y el encabezado debe decirlo.
    d.celda(12, 0, 3, "Recall CR-01", "Recall de CR-01 por evidencia directa")
    d.celda(12, 3, 4,
            "No apta para CR-01 bajo esta formulación: no recuperó cabeza descubierta.",
            "Ciega a la cabeza descubierta, de modo que no sostiene la formulación directa. Su "
            "límite para el núcleo es el chaleco, con AP 0,182 en obra curada frente a 0,520 del "
            "perfil operativo.")
    d.reemplazar(8, "mientras que gdino-base-560 produjo el recall más alto para CR-01",
                 "mientras que gdino-base-560 produjo el recall más alto de CR-01 por evidencia "
                 "directa")

    # E5-I5: el denominador del recall pertenece a una referencia fechada.
    d.reemplazar(13,
                 "El recall de CR-01 se informa sobre 5.313 positivos de referencia.",
                 "El recall de CR-01 se informa sobre 5.313 positivos, el conteo de la referencia "
                 "con la que se ejecutó la campaña. Una corrección posterior de esa referencia lo "
                 "dejó en 5.308 y la medición no se repitió. Esa columna cuenta sólo detecciones de "
                 "cabeza descubierta, de modo que mide la formulación directa. El núcleo opera con "
                 "la indirecta, que deriva la ausencia desde persona y casco, y su capacidad para "
                 "la condición no se lee en esta columna.")

    d.reemplazar(14, "La asimetría no tuvo su dependencia de una única fuente",
                 "La asimetría no dependió de una única fuente")

    d.reemplazar(16,
                 "Sin ninguna corrida de entrenamiento alcanzó AP50 de 0,662 sobre 99 cajas de referencia.",
                 "La clase alcanzó AP50 de 0,662 sobre 99 cajas de referencia sin ninguna corrida "
                 "de entrenamiento.")

    # ---------------------------------------------------------------- 17.5.3 Estado por persona
    # X-7: la mitad de calibración se predeclaró y es disjunta del material de medición.
    d.reemplazar(18,
                 "con IoU mayor o igual que 0,5.",
                 "con IoU mayor o igual que 0,5. La partición en mitades se registró con su "
                 "semilla y fue la misma para todos los brazos, de modo que ninguna imagen que "
                 "ajustó un umbral entró después en la medición.")
    # E5-I3: la oración quedó duplicada al absorber la nota de la tabla.
    d.borrar(18, " La medición sobre imágenes utilizó calibración en una mitad y evaluación en la otra.")
    # X-11 y E5-I1: los dos materiales de obra real son distintos, y la tabla necesita su llamada.
    d.reemplazar(18,
                 "La medición sobre video de obra real abarcó 17 clips y no incluyó el motor temporal.",
                 "La medición sobre video abarcó 17 clips de obra real, un material distinto del "
                 "estrato que integra el banco temporal, y no incluyó el motor temporal. La Tabla "
                 "62 reúne los resultados.")

    # E5-I2: el término del proyecto es «juzgabilidad»; «de de juicio» quedó de una edición.
    d.celda(22, 5, 4, "La misma frontera de de juicio dominó el resultado.",
            "La misma frontera de juzgabilidad dominó el resultado.")

    # E5-B2 · decisión del usuario del 2026-09-07: la frontera se caracteriza en prosa, sin figura.
    d.parrafo_nuevo(25, FRONTERA, muestra=25)

    # ---------------------------------------------------------------- 17.5.4 Alerta por episodio
    d.reemplazar(27, "y uno quedó censurado con causa",
                 "y uno quedó censurado con causa declarada, porque su duración no permitía que "
                 "una alerta lenta ocurriera dentro del clip")
    d.agregar_al_final(27, (
        " La Tabla 63 reúne las combinaciones ejecutadas sobre ese material, cada una con una "
        "sola variable cambiada respecto de la línea de base."))

    # Hallazgo del pase: el n de la columna de latencia no es el denominador de la media.
    d.reemplazar(32,
                 "y la columna de latencia declara cuántos episodios confirmados sostienen cada valor",
                 "y el número entre paréntesis de la columna de latencia es la cantidad de "
                 "episodios confirmados, mientras que la media se promedia por clip con alerta "
                 "confirmada, un conteo menor cuando un mismo clip contiene las dos condiciones")

    # E5-B3
    d.reemplazar(33,
                 ", medida sobre 23 episodios confirmados.",
                 ". Las dos medias se promediaron por clip con alerta confirmada, siete en CR-02 "
                 "y veintiuno en CR-01.")
    d.agregar_al_final(33, " La Figura 4.6 muestra un fotograma con la alerta ya confirmada.")

    d.parrafo_nuevo(33, "", muestra=28)
    d.parrafo_nuevo(33, "**Figura 4.6**", muestra=29)
    d.parrafo_nuevo(33, "*Fotograma con alerta confirmada de CR-01*", muestra=30)
    d.figura(33, FIGS / "fig-c-alerta-confirmada.png", ANCHO_16CM, muestra=30)
    d.parrafo_nuevo(33, (
        "**Nota.** Fotograma de la corrida de línea de base sobre un clip del bloque de rodaje, "
        "en un instante posterior a la alerta, con el motor en estado sostenido. El casco "
        "detectado sobre la mesa no suprime la condición, porque CR-01 se evalúa sobre el sujeto "
        "y no sobre la escena."), muestra=32)

    d.reemplazar(37,
                 "estuvo dos órdenes de magnitud por debajo de la necesaria para sostener una",
                 "estuvo casi treinta veces por debajo de la necesaria para sostener una")

    # ---------------------------------------------------------------- 17.5.5 Tiempo real
    # E5-I4: la franja del camino en vivo y las densidades de remuestreo son dos cosas.
    d.reemplazar(39,
                 "entregó entre 1,16 y 4,42 fps en cuatro densidades medidas sobre los 34 clips del "
                 "bloque de rodaje, remuestreados de manera pareada.",
                 "entregó entre 1,16 y 4,42 fps. Para cubrir esa franja, los 34 clips del bloque "
                 "de rodaje se remuestrearon de manera pareada a cuatro densidades, de 30 a 1,15 "
                 "cuadros por segundo.")

    # Decisión del usuario del 2026-09-07: sin figura de densidad; la serie completa la Tabla 64.
    # el orden de la serie queda de mayor a menor densidad: 30 · 4,29 · 2,00 · 1,15
    d.fila_nueva(43, 0, [
        "Densidad", "Referencia del banco, 30 fps", "Escena 0,789 · sujeto 0,930",
        "n = 34 episodios evaluables", "Punto de partida de la comparación."], modelo=1)
    d.fila_nueva(43, 2, [
        "Densidad", "Intermedia, aproximadamente 2,00 fps", "Escena 0,738 · sujeto 0,875",
        "n = 34 episodios evaluables", "La pérdida no avanza de manera uniforme."], modelo=2)
    d.agregar_al_final(45, (
        " Entre la densidad del banco y el techo del camino en vivo el resultado por escena no "
        "cambió de manera apreciable y el resultado por sujeto perdió 0,064, mientras que en la "
        "densidad más baja la caída ya alcanza 0,143 y 0,188 respectivamente. Con 34 episodios "
        "evaluables, las diferencias menores que 0,02 quedan dentro de la resolución del banco y "
        "no se leen como orden."))

    # ---------------------------------------------------------------- 17.5.6 Caminos no adoptados
    # X-14: la promesa de §17.4.4 se responde con causa y sin cifra del banco anterior.
    d.reemplazar(49,
                 "La familia MM-Grounding DINO se integró por el mismo mecanismo de adaptación, se "
                 "evaluó y se archivó durante la selección, sin incorporarse al perfil operativo.",
                 "La familia MM-Grounding DINO se integró por el mismo mecanismo de adaptación y "
                 "se archivó durante la selección de modelos, sobre el banco anterior al "
                 "congelado, de modo que no tiene cifra comparable en esta sección. Una de sus "
                 "variantes no aportó ventaja en ninguna dimensión evaluada, y las otras dos "
                 "entregaron cajas cuya geometría las volvía inservibles, con origen en el punto "
                 "de control publicado y no en el adaptador que las integró.")

    # Misma métrica que la Tabla 61, mismo nombre: la columna del ajuste fino también mide la
    # vía directa, y así queda dicho para que las dos tablas se lean con la misma vara.
    d.celda(54, 1, 1, "recall CR-01 0,0002", "recall de CR-01 por evidencia directa 0,0002")
    d.celda(54, 2, 1, "recall CR-01 0,2089", "recall de CR-01 por evidencia directa 0,2089")

    d.reemplazar(56,
                 "con 2.946 imágenes de ajuste frente a 10,35 millones de parámetros",
                 "con 2.946 imágenes de ajuste frente a 10,35 millones de parámetros, un conjunto "
                 "cuya composición y regla de partición declara la sección 17.4.7")

    # ---------------------------------------------------------------- 17.5.7 y cierre
    d.parrafo_nuevo(63, NO_COMPUTADAS, muestra=62)
    d.parrafo_nuevo(63, LIMITACIONES, muestra=62)

    # ---------------------------------------------------------------- comentarios
    # Sin comentario sobre el desglose por estrato: la regla ya se cumple en el párrafo que
    # reporta AP por clase y estrato, y un mAP50 por estrato no sería comparable entre estratos
    # porque cada uno anota un conjunto de clases distinto.
    d.comentario(12, "Recall de CR-01 por evidencia directa",
                 "Coherencia pedida el 07-09. El evaluador de esta columna cuenta sólo detecciones "
                 "de cabeza descubierta, así que mide la formulación DIRECTA, que es la que el "
                 "proyecto no adoptó. Con el encabezado anterior la tabla usaba dos varas: el "
                 "0,000 descalificaba a YOLOE «para CR-01» mientras el 0,308 del perfil operativo "
                 "no lo descalificaba a él. Verificado sobre los artefactos: en las dos clases que "
                 "la vía indirecta necesita, YOLOE mide person 0,785 y helmet 0,715 contra 0,770 y "
                 "0,707 del perfil operativo, de modo que para CR-01 por vía indirecta no es "
                 "inferior. Lo que sí la deja fuera del núcleo es el chaleco y el mAP50 agregado.")
    d.comentario(32, "la media se promedia por clip con alerta confirmada",
                 "Corrección verificada contra el artefacto de cada campaña. El número entre "
                 "paréntesis es matched, los episodios confirmados; la media de latencia se "
                 "calcula por clip con alerta confirmada. En la línea de base son 28 episodios y "
                 "26 clips, y en la fila de granularidad por sujeto, 33 y 29.")
    d.comentario(33, "siete en CR-02 y veintiuno en CR-01",
                 "El «23» anterior era la cantidad de clips con CR-01 confirmado en la campaña, no "
                 "el denominador de la media. Reconstruido desde el artefacto: la media de 4.314 "
                 "ms sale de 21 clips y la de 8.572 ms, de 7.")
    d.comentario(18, "La partición en mitades se registró con su semilla",
                 "Agregado para que esta medición no choque con la regla de congelamiento del "
                 "banco, que prohíbe usarlo en calibración. Verificado sobre el artefacto de la "
                 "campaña: la semilla está registrada y es la misma en la corrida principal y en "
                 "su réplica, así que la partición es determinista y previa a los resultados.")
    d.comentario_en_nuevo(63, 0,
                          "Responde a la exigencia del marco de métricas de declarar el estado de "
                          "cada medida adoptada. Si alguna de las cuatro te parece de más, se saca.")
    d.comentario_en_nuevo(63, 1,
                          "Restaurado tal como estaba antes de la edición del 06-09; es lo que "
                          "piden AJ-5.05 y la decisión D-H. Si preferís que las limitaciones vivan "
                          "en el cierre y no acá, se borra este párrafo y queda anotado el "
                          "traslado a §18.")
    d.comentario_en_nuevo(25, 0,
                          "Reemplaza a la figura de la frontera de juzgabilidad, que se descartó "
                          "el 07-09. La figura mezclaba dos cosas distintas: la juzgabilidad es "
                          "si el anotador humano puede determinar el estado, y lo que graficaba "
                          "era rendimiento del sistema. Además tomaba cuatro clips de una foto "
                          "anterior al cierre de la campaña de 17. Este párrafo conserva los tres "
                          "ejes con las cifras exactas, incluida la caída nocturna, que era lo "
                          "que valía la pena no perder.")
    d.comentario(45, "la caída ya alcanza 0,143 y 0,188",
                 "Reemplaza a la figura de calidad contra densidad, descartada el 07-09. Los ocho "
                 "valores que graficaba están ahora en la Tabla 64, que suma las dos densidades "
                 "que le faltaban, y la lectura queda en esta oración. Una curva de cuatro puntos "
                 "invitaba a leer pendientes que el banco no resuelve.")
    d.comentario_en_nuevo(33, 1,
                          "Numeración: §17.3 lleva las Figuras 4.1 a 4.4 y §17.4 la 4.5, así que "
                          "esta es la 4.6 y la única de §17.5. Al integrar el maestro conviene "
                          "numerarlas con campo de Word.")

    st = d.guardar(DST)
    print("\n".join(d.log))
    print("\n", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
