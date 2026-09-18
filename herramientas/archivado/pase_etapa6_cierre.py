#!/usr/bin/env python3
"""Pase de la Etapa 6 — §17.6, §18 y §19 · v1.0 → v1.1 (sugerencias sin aceptar).

El usuario y su colega leyeron la v1.0 (redactada por el chat de ChatGPT con el kit `--etapa 6`)
y dejaron cuatro hilos de comentarios, con el diagnóstico de que «el cierre del informe es muy
extenso y los anexos se llevan una gran parte». La medición del documento matizó ese diagnóstico
y lo ubicó en dos lugares concretos; este pase aplica lo que se recomendó y respondió.

QUÉ NO SE TOCA, y por qué (medido, no supuesto)
  · Anexos A, C y D: son copia fila a fila del material ya cerrado (`90e` el A, `90g` los C y D) y
    §15.2.3, §15.3.3 y §17.1 remiten a sus tablas por número. Cambiarlos acá desincroniza secciones
    cerradas.
  · Anexo B: 7 tablas, reescritas de «candidato» a «utilizado / no ejercido» respecto del maestro
    v1.1. §17.1.4 remite al Anexo B. `ajustes/07` §7 declara que B, C y D no se podan porque son el
    destino de lo que sale del cuerpo.
  · El bloque de anexos NO creció: 4.957 palabras contra 5.302 del maestro v1.1 (A–D bajaron 42 %;
    E y F son nuevos porque los pide el contrato, AJ-6.02 y AJ-6.03).

QUÉ SE COMPRIME
  · §18.2–§18.4 traían 6 cifras cada 100 palabras, más que el propio §17.5 (4,8): re-reportaban las
    Tablas 61–65. Se conserva la cifra que ES la conclusión (el par 0,930/0,789, el veto de precisión
    0,146 contra el umbral 0,5, la reducción de retención del 71,3 %) y se remite a la tabla para las
    series completas, los denominadores repetidos y los conteos de contexto.
  · Anexo E: era el anexo más largo en prosa (854 palabras) y sus últimos párrafos repetían reglas ya
    escritas —unidad estadística y SDR de §17.5, G2A desde el dequeue de §18.4, empaquetado no
    verificado de §17.6.4 (que aparecía tres veces en el documento)—. Se funden y se recortan.

LOS CUATRO HILOS DE COMENTARIOS
  · 17.6.1 «medio al vicio … eso ya es cosa nuestra» / «si, no suma» → se dan de baja las dos
    oraciones sobre el repositorio documental; sobreviven las dos que hablan del software.
  · 17.6.4 «palabra rancia» → «contenedorización» pasa a «empaquetado en contenedores».
  · 18.5 «llamarlas de otra forma, no hay contexto de que son» (T1/T2/T3) → verificado: ni §17.4 ni
    §17.5 usan esas etiquetas (cero menciones); dicen «escalera de tres tramos», «el primer tramo
    entrenó sólo la proyección de clases». Se reemplazan por esos nombres.
  · 19.5 «esto no se de qué es, si va en el anexo o se coló de algún otro lado» → sí va (es la cadena
    de reproducción que pide AJ-6.02), le faltaba la oración que dice de qué material habla.

REFERENCIAS — el hallazgo que bloquea la integración
La lista de la v1.0 (149 entradas) fusionó `90e` en el maestro y podó las huérfanas, que era lo
pedido, pero además actualizó tres preprints a su versión publicada y re-letró los sufijos de NVIDIA.
Eso deja SIN RESOLVER citas de secciones ya cerradas, que este documento no puede editar:
    §15/16 → L. H. Li et al., 2021 · Shen et al., 2023 · NVIDIA, s. f.-g · NVIDIA, s. f.-h ·
             Roy, 2024 (dada de baja) · May, 2017 (re-alfabetizada bajo Pantos)
    §17.1  → Gu et al., 2021 · NVIDIA Corporation, s. f.-b
    §19.1  → la nota de la Tabla A.1, copiada de `90e`, cita L. H. Li et al. (2021) y Shen et al. (2023)
El pase devuelve cada entrada a la forma que la cita vigente espera y deja el desajuste anotado en
comentarios: actualizar a la versión publicada es una mejora real (sube la proporción de fuentes
arbitradas) pero exige cambiar esas citas en §15/16 y §17.1, y eso es trabajo de integración.
También se quita la entrada duplicada de Chen y Zou (estaba dos veces, 2025 y 2026, para la misma obra).

INCREMENTAL: parte de la v1.0 en `desarrollando/`. Para una bajada nueva de Google Docs, `--origen`.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE si el usuario ya trabajó la v1.1 en Google Docs:
# el origen por default es la v1.0 y volver a correrlo pisaría lo que haya hecho después.

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ORIGEN = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.0.docx"
DESTINO = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.1 (sugerencias sin aceptar).docx"
FECHA = "2026-09-09T12:00:00Z"


def _palabras(d: Documento, hasta: int = 161) -> int:
    """Palabras del cuerpo (sin la lista de Referencias), en la vista aceptada."""
    return sum(len(d.texto(i).split()) for i in range(hasta))


# ═══════════════════════════════════════════════════════════ §17.6 · los dos hilos del colega
def seccion_17_6(d: Documento) -> None:
    # --- 17.6.1 · «medio al vicio … eso ya es cosa nuestra» / «si, no suma» -------------------
    i = d.unica("El repositorio documental tuvo historia de versiones")
    d.comentario(
        i, "Las ramas experimentales",
        "Responde el hilo de Matías («habla de como organizamos el documento, pero eso ya es cosa "
        "nuestra») y tu «si, no suma». Se dan de baja las dos oraciones sobre el repositorio "
        "documental. Estaban porque el contrato de la etapa (AJ-6.04) pedía declarar que `docs/` es "
        "un repo propio con remoto y respaldo, pero eso describe cómo trabajó el equipo, no la "
        "plataforma evaluada. Las dos oraciones que quedan hablan del software y sostienen el título "
        "de la subsección junto con la mención del repositorio documental del primer párrafo. Si "
        "rechazás la baja, el párrafo vuelve entero.")
    d.borrar(
        i,
        "El repositorio documental tuvo historia de versiones y acceso remoto para el equipo, además "
        "de un respaldo en otro disco. Reunió el protocolo, las decisiones de diseño, las condiciones "
        "de ejecución y las verificaciones realizadas. ")

    # --- 17.6.2 · la trazabilidad se dice una vez ---------------------------------------------
    i = d.unica("La regla de persistencia antes de publicación")
    d.reemplazar(
        i,
        "Una vez finalizada una corrida, los eventos pudieron releerse para inspeccionar la secuencia "
        "o repetir la evaluación del plano de control. La reconstrucción no requirió que el canal de "
        "mensajería hubiera conservado el historial.",
        "Una vez finalizada una corrida, los eventos pudieron releerse para inspeccionar la secuencia "
        "o repetir la evaluación del plano de control, sin que el canal de mensajería hubiera "
        "conservado el historial.")

    i = d.unica("La cadena de una alerta pudo rastrearse")
    d.reemplazar(
        i,
        "El registro de un intento fallido o de un descarte definitivo permaneció separado del "
        "registro de confirmación del patrón. Por ello, contar filas del registro de distribución no "
        "equivale a contar alertas distintas ni entregas satisfactorias.",
        "Como el registro de los intentos fallidos y de los descartes definitivos permaneció separado "
        "del de confirmación del patrón, contar filas del registro de distribución no equivale a "
        "contar alertas distintas ni entregas satisfactorias.")

    # --- 17.6.4 · «he» / «ya se que es» / «pero palabra rancia» -------------------------------
    i = d.unica("La contenedorización quedó definida y validada por configuración")
    d.reemplazar(i, "La contenedorización quedó definida y validada por configuración",
                 "El empaquetado en contenedores quedó definido y validado por configuración")
    d.reemplazar(
        i,
        "Su documentación operativa acompaña al software, mientras que el Anexo E delimita el camino "
        "de reproducción y las comprobaciones que respaldan los resultados del informe.",
        "Su documentación operativa acompaña al software, y el Anexo E delimita el camino de "
        "reproducción y las comprobaciones que respaldan los resultados.")
    d.comentario(
        i, "El despliegue no fue verificado",
        "Responde el hilo «pero palabra rancia». «Contenedorización» sale una sola vez en las tres "
        "secciones y el resto del documento ya dice «empaquetado», así que el cambio también unifica "
        "el término. El contenido del párrafo no se toca porque coincide con el estado real "
        "verificado: el compose de los 13 servicios valida, y los builds y el smoke integral no se "
        "corrieron.")

    i = d.unica("El cierre dejó, por tanto, una plataforma experimental documentada")
    d.reemplazar(
        i,
        "y una cadena de evidencia inspeccionable. La reproducción de resultados sobre artefactos "
        "congelados, la repetición del procesamiento y la ejecución en otro entorno se mantienen como "
        "alcances diferentes. Las condiciones de acceso",
        "y una cadena de evidencia inspeccionable, con los alcances de reproducción que delimita el "
        "Anexo E. Las condiciones de acceso")


# ═══════════════════════════════════════════════════════════ §18 · compresión y T1/T2/T3
def seccion_18(d: Documento) -> None:
    # --- 18.1 · la cita de Chen y Zou sigue al año de la entrada de la lista -------------------
    i = d.unica("Los antecedentes de detección de EPP con modelos visión-lenguaje")
    d.reemplazar(i, "Chen y Zou, 2026", "Chen y Zou, 2025")
    d.comentario(
        i, "(Choi y Greer, 2024; Chen y Zou, 2025)",
        "La lista de la v1.0 traía esta obra DOS veces, como preprint de 2025 y como artículo de 2026, "
        "y acá se citaba la de 2026 mientras §15/16 cita la de 2025. Se quita la entrada duplicada y "
        "queda 2025, que es la que citan §15/16 y el material cerrado de la Etapa 1. Si preferís la "
        "versión publicada, hay que cambiar también las dos citas de §15/16 (ver el comentario de la "
        "lista de Referencias).")

    d.comentario(
        d.unica("Las conclusiones siguientes distinguen resultados establecidos"),
        "Las conclusiones siguientes distinguen resultados establecidos",
        "Nota de lectura del pase, no hay nada que decidir acá. Esta oración es la que gobierna la "
        "compresión de §18.2 a §18.4: las cifras que quedan son las que SON la conclusión (el par "
        "0,930 contra 0,789, el veto de precisión 0,146 contra el umbral 0,5, la reducción de "
        "retención del 71,3 %). Las series completas, los denominadores repetidos y los conteos de "
        "contexto se remiten a las Tablas 61 a 65 de §17.5, que es donde viven. §18.2 a §18.4 traían "
        "6 cifras cada 100 palabras, más que el propio §17.5, que tiene 4,8.")

    # --- 18.2 · selección del perfil -----------------------------------------------------------
    i = d.unica("La selección de un modelo no pudo resolverse")
    d.reemplazar(
        i,
        "En el estrato de obra curada de 147 imágenes, gdino-tiny-560 obtuvo mAP50 de 0,503, "
        "gdino-base-560 de 0,474 y yoloe-26x de 0,405. La sección 17.5.2 reportó, además, que el "
        "primer perfil conservó el liderazgo en el banco completo, integrado por ese estrato y otros "
        "dos de 1.330 y 5.000 imágenes.",
        "En el estrato de obra curada de 147 imágenes, gdino-tiny-560 encabezó el mAP50 por delante de "
        "gdino-base-560 y de yoloe-26x, y la sección 17.5.2 reportó que conservó el liderazgo en el "
        "banco completo, integrado por ese estrato y otros dos de mayor tamaño.")

    i = d.unica("El perfil base conservó un papel distinto")
    d.reemplazar(
        i,
        "En el mismo estrato de 147 imágenes, el AP de chaleco fue 0,582 frente a 0,520 del perfil "
        "operativo. La mayor capacidad para una clase no implicó el mejor resultado de la plataforma "
        "completa. El contraste especializado se justifica, por tanto, por el comportamiento de la "
        "combinación en condiciones concretas, y no por asumir que un modelo de mayor tamaño mejora "
        "de manera uniforme todos los eslabones.",
        "En el mismo estrato, su AP de chaleco fue 0,582 frente a 0,520 del perfil operativo. Esa "
        "ventaja en una clase no implicó el mejor resultado de la plataforma completa, y por eso el "
        "contraste se justifica por el comportamiento de la combinación en condiciones concretas y no "
        "por el tamaño del modelo.")

    # --- 18.2 · estrategias --------------------------------------------------------------------
    i = d.unica("La comparación de estrategias mostró por qué expresar una condición")
    d.reemplazar(
        i,
        "En el subconjunto curado de CR-01, E-IND alcanzó F1 de 0,408 y E-DIR de 0,189, con 28 casos "
        "positivos. En el nivel temporal",
        "En el subconjunto curado de CR-01, E-IND ya superaba a E-DIR en la comparación por persona. "
        "En el nivel temporal")

    i = d.unica("La estrategia indirecta aportó una explicación inspeccionable")
    d.reemplazar(i, "sobre un único estrato con 82 positivos e intervalos solapados",
                 "sobre un único estrato y con intervalos solapados")

    # --- 18.2 · extensibilidad -----------------------------------------------------------------
    i = d.unica("La extensibilidad sin entrenamiento sí fue ejercida")
    d.reemplazar(i, "produjo AP50 de 0,662 sobre 99 cajas de referencia sin ninguna corrida de "
                    "entrenamiento", "produjo AP50 de 0,662 sin ninguna corrida de entrenamiento")
    d.reemplazar(i, "y, de manera aislada, produjo 118 cajas con AP de 0,026 al localizar la propia "
                    "maquinaria",
                 "y, de manera aislada, obtuvo AP de 0,026 al localizar la propia maquinaria")

    i = d.unica("Esa sensibilidad también alcanzó al vocabulario del núcleo")
    d.reemplazar(i, "redujo el F1 temporal de 0,704 a 0,622 sobre los 34 episodios evaluables del "
                    "rodaje", "redujo el F1 temporal de 0,704 a 0,622 en ese bloque")

    # --- 18.3 · el par 0,930/0,789 ya está en 18.1 ---------------------------------------------
    i = d.unica("La separación entre detección y alerta permitió medir el aporte")
    d.reemplazar(
        i,
        "En el rodaje, cambiar de escena a sujeto elevó el F1 de 0,789 a 0,930 sobre 34 episodios "
        "evaluables con detecciones idénticas.",
        "En el rodaje, cambiar de escena a sujeto produjo, con detecciones idénticas, el salto de F1 "
        "citado en la sección 18.1.")
    d.comentario(
        i, "el salto de F1 citado en la sección 18.1",
        "El par 0,930 contra 0,789 estaba escrito dos veces con las mismas palabras, acá y en 18.1, "
        "donde es la evidencia principal. Se remite en lugar de repetirlo. Si preferís que §18.3 se "
        "lea sola, rechazá la sugerencia y vuelven las cifras.")

    i = d.unica("La fusión por disyunción refutó una expectativa")
    d.reemplazar(i, "Sobre los 34 episodios evaluables del rodaje, el recall pasó",
                 "En ese bloque, el recall pasó")
    d.reemplazar(
        i,
        "La refutación es establecida para esa regla de fusión; no se extiende a la variante por "
        "conjunción, que no se ejecutó. El hallazgo muestra que el rendimiento de una composición "
        "temporal no puede deducirse únicamente de la unión de detecciones por imagen.",
        "La refutación es establecida para esa regla de fusión y no se extiende a la variante por "
        "conjunción, que no se ejecutó. El rendimiento de una composición temporal no puede deducirse "
        "de la unión de detecciones por imagen.")

    # --- 18.3 · obra real ----------------------------------------------------------------------
    i = d.unica("La evaluación intermedia sobre 17 clips de obra real")
    d.reemplazar(
        i,
        "Con E-IND a 2 Hz y sin motor temporal, CR-01 obtuvo F1 de 0,031, con 92 positivos entre "
        "10.356 cuadros con persona juzgables; CR-02 obtuvo 0,018, con 170 positivos entre 10.361. La "
        "precisión, de 0,016 y 0,009, respectivamente, fue la principal restricción.",
        "Con E-IND a 2 Hz y sin motor temporal, CR-01 obtuvo F1 de 0,031 y CR-02 de 0,018, sobre más "
        "de diez mil cuadros con persona juzgables en cada condición. La precisión, inferior a 0,02 en "
        "ambas, fue la principal restricción.")

    i = d.unica("Tampoco el control de negativos del rodaje permite sostener una cota horaria")
    d.reemplazar(
        i,
        "En el único clip negativo continuo de obra real, de 6 minutos y 9,6 segundos, se observaron "
        "tres falsos positivos por escena y 190 por sujeto; las tasas derivadas fueron 29,2 y 1.850,8 "
        "por hora, respectivamente.",
        "En el único clip negativo continuo de obra real, de 6 minutos y 9,6 segundos, las tasas "
        "derivadas fueron 29,2 falsas alertas por hora con granularidad de escena y 1.850,8 por sujeto.")

    # --- 18.4 · en vivo y remuestreo -----------------------------------------------------------
    i = d.unica("El funcionamiento en vivo quedó demostrado")
    d.reemplazar(i, "se ubicó entre 630 y 890 ms en tres corridas de 47, 93 y 55 unidades visuales",
                 "se ubicó entre 630 y 890 ms en tres corridas")

    # La serie de las cuatro cadencias NO se toca: 23 palabras para cuatro pares es más compacto que
    # cualquier paráfrasis (se probó, y la versión en prosa salía más larga y con menos información).
    i = d.unica("La granularidad por sujeto mantuvo una ventaja")
    d.reemplazar(
        i,
        "pero esa comparación no autoriza a afirmar que una configuración de baja cadencia supera a "
        "otra de alta cadencia cuando el contraste cruzado no es concluyente. Tampoco corresponde "
        "comparar SDR entre cadencias diferentes como si sólo hubiera cambiado la calidad del sistema: "
        "cambia el instrumento con el que se observa la continuidad de la evidencia.",
        "pero el contraste cruzado entre cadencias distintas no es concluyente. Tampoco corresponde "
        "comparar SDR entre cadencias, porque cambia el instrumento con el que se observa la "
        "continuidad de la evidencia.")

    # --- 18.5 · los nombres de los tramos, no las etiquetas internas ---------------------------
    i = d.unica("La rama de ajuste fino no modificó la conclusión")
    d.reemplazar(
        i,
        "T1 y T2 produjeron veredictos negativos de adopción; T3 quedó cerrado por las condiciones de "
        "activación y de linaje.",
        "Los dos tramos entrenados produjeron veredictos negativos de adopción y el tercero quedó "
        "cerrado por las condiciones de activación y de linaje.")
    d.comentario(
        i, "Los dos tramos entrenados produjeron veredictos negativos",
        "Responde el hilo «llamarlas de otra forma, no hay contexto de que son». Verificado: ni §17.4 "
        "ni §17.5 usan las etiquetas T1, T2 y T3 —cero menciones en las dos—, y nombran los tramos "
        "como «la escalera de tres tramos», «el primer tramo entrenó sólo la proyección de clases» y "
        "«el ajuste de mayor capacidad». En §18.5 se pasa a esos nombres, que además ya aparecen en el "
        "párrafo siguiente. Las etiquetas T1/T2/T3 son de los documentos de operación, no del informe.")

    i = d.unica("La curva de línea base, ajuste de la proyección de clases")
    d.reemplazar(
        i,
        "En T1 no se alcanzó la ganancia exigida y se incumplió la retención de persona. En T2 se "
        "superó el criterio de ganancia de cabeza descubierta, pero fallaron las retenciones del "
        "dominio y de vocabulario abierto. Estos veredictos se establecieron sobre el protocolo de la "
        "rama, cuyo banco de dominio reunió los estratos de 147, 1.330 y 5.000 imágenes.",
        "En el ajuste de la proyección de clases no se alcanzó la ganancia exigida y se incumplió la "
        "retención de persona. En el de mayor capacidad se superó el criterio de ganancia de cabeza "
        "descubierta, pero fallaron las retenciones del dominio y de vocabulario abierto. Estos "
        "veredictos se establecieron sobre el protocolo de la rama, cuyo banco de dominio fue el "
        "mismo de la sección 17.5.2.")

    i = d.unica("La medición de retención abierta aporta un resultado")
    d.reemplazar(i, "de 0,4347 en la línea base a 0,1247 en T2", "de 0,4347 a 0,1247 en ese tramo")
    d.reemplazar(i, "el checkpoint evaluado de T2 provino", "el checkpoint evaluado provino")

    i = d.unica("El entrenamiento utilizó 2.946 imágenes")
    d.reemplazar(i, "no permite reducir el resultado de T1 a falta de parámetros",
                 "no permite reducir el resultado del primer tramo a falta de parámetros")

    i = d.unica("El cierre de T3 se sostiene primero en la escalera de activación")
    d.reemplazar(i, "El cierre de T3 se sostiene", "El cierre del tercer tramo se sostiene")

    # --- 18.6 · el andamiaje de las continuidades ---------------------------------------------
    i = d.unica("Las continuidades justificadas se desprenden")
    d.reemplazar(
        i,
        "condiciones de acceso resueltas, antes de intentar fijar una cota de falsas alarmas o "
        "generalizar el efecto del tracker. La segunda es evaluar la conservación de identidades con "
        "referencia apropiada y separar sus errores de los de percepción en escenas con múltiples "
        "personas. La tercera es disponer de anotaciones y evaluadores adecuados antes de extender el "
        "núcleo a relaciones espaciales o condiciones de mayor complejidad.",
        "condiciones de acceso resueltas, antes de fijar una cota de falsas alarmas o generalizar el "
        "efecto del tracker. La segunda es evaluar la conservación de identidades con referencia "
        "apropiada, separando sus errores de los de percepción en escenas con múltiples personas. La "
        "tercera exige anotaciones y evaluadores adecuados antes de extender el núcleo a relaciones "
        "espaciales o condiciones de mayor complejidad.")


# ═══════════════════════════════════════════════════════════ §19.5 · Anexo E
def anexo_e(d: Documento) -> None:
    # --- el hilo «esto no se de qué es» --------------------------------------------------------
    i = d.unica("La comprobación de imágenes comienza por reconstruir el banco")
    d.reemplazar(
        i, "La comprobación de imágenes comienza por reconstruir el banco",
        "Los materiales identificados en la Tabla E.2 se reproducen por caminos distintos, que las "
        "secuencias siguientes describen. La comprobación del banco de imágenes comienza por "
        "reconstruirlo")
    d.comentario(
        i, "Los materiales identificados en la Tabla E.2",
        "Responde el hilo «esto no se de qué es, si va en el anexo o se coló de algún otro lado». Sí "
        "va acá: es la cadena de reproducción que pide el contrato de la etapa (AJ-6.02), y es lo que "
        "hace auditable el capítulo de resultados. Lo que faltaba era la oración que dice de qué "
        "material habla y que abre las tres secuencias que siguen (banco de imágenes, banco temporal y "
        "comandos). Sin ella el párrafo arrancaba en el aire.")

    # --- fundir las dos advertencias de agregación y medición ---------------------------------
    i = d.unica("La agregación conserva la unidad estadística")
    d.reemplazar(
        i,
        "Un promedio de latencias por clip no se presenta como percentil ni como promedio ponderado de "
        "todas las alertas. Los intervalos obtenidos mediante remuestreo deben mantener la unidad y el "
        "pareamiento del contraste original. Esta precaución resulta especialmente importante al "
        "comparar granularidades con detecciones idénticas o cadencias obtenidas por remuestreo del "
        "mismo material.",
        "Un promedio de latencias por clip no se presenta como percentil, y los intervalos obtenidos "
        "mediante remuestreo mantienen la unidad y el pareamiento del contraste original. La "
        "precaución importa sobre todo al comparar granularidades con detecciones idénticas o "
        "cadencias obtenidas por remuestreo del mismo material.")

    i = d.unica("La repetición en vivo exige, además, fijar el entorno")
    d.reemplazar(
        i,
        "La espera de la suscripción por parte del publicador protege el comienzo del canal de "
        "alertas; no se sustituye esa condición por una pausa supuesta. El periodo de preparación del "
        "modelo permanece fuera de la ventana de medición, y cada tramo temporal conserva sus hitos y "
        "su dominio de reloj.",
        "La espera de la suscripción por parte del publicador protege el comienzo del canal de "
        "alertas y no se sustituye por una pausa supuesta. El periodo de preparación del modelo "
        "permanece fuera de la ventana de medición.")

    i = d.unica("La definición de G2A aplicada en este trabajo")
    d.reemplazar(
        i,
        "Por ello, al relacionarla con la literatura de latencia de video, debe mantenerse explícita "
        "la diferencia entre el extremo físico de captura y el extremo instrumentado por software "
        "(Bachhuber et al., 2018). No se completa una medición ausente de RTSP con la cifra de captura "
        "de OAK-D, ni se suman percentiles de distribuciones no emparejadas.",
        "Al relacionarla con la literatura de latencia de video debe mantenerse explícita la "
        "diferencia con el extremo físico de captura (Bachhuber et al., 2018). Cada tramo conserva sus "
        "hitos y su dominio de reloj, de modo que una medición ausente de RTSP no se completa con la "
        "cifra de captura de OAK-D.")

    i = d.unica("Las pruebas automatizadas y los verificadores descritos")
    d.reemplazar(
        i,
        "La reproducción byte a byte del banco no equivale a una repetición independiente de toda la "
        "inferencia sobre otro equipo. Asimismo, el código y la configuración de contenedores no "
        "acreditan un despliegue ejecutado: la construcción de las imágenes y la prueba integral no se "
        "realizaron. El material conservado respalda la inspección y reconstrucción de las ejecuciones "
        "documentadas, sin presentar una validación externa de portabilidad que no existe.",
        "La reproducción byte a byte del banco no equivale a una repetición independiente de toda la "
        "inferencia sobre otro equipo, y el empaquetado definido no acredita un despliegue ejecutado, "
        "según lo delimitado en la sección 17.6.4. El material conservado respalda la inspección y "
        "reconstrucción de las ejecuciones documentadas, sin presentar una validación externa de "
        "portabilidad que no existe.")
    d.comentario(
        i, "según lo delimitado en la sección 17.6.4",
        "El límite del empaquetado estaba escrito tres veces en el documento, en 17.6.4, en 18.6 y "
        "acá. Queda enunciado una vez y las otras dos remiten. La versión larga de este párrafo "
        "repetía además el «byte a byte» de 17.6.3.")


# ═══════════════════════════════════════════════════════════ Referencias
def referencias(d: Documento) -> None:
    # --- 1. los tres preprints vuelven al año que citan las secciones vigentes ----------------
    i = d.unica("Grounded language-image pre-training")
    d.reemplazar(i, "y Gao, J. (2022). Grounded language-image pre-training. En Proceedings of the "
                    "IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 10965–10975). "
                    "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Grounded_Language-Image_"
                    "Pre-Training_CVPR_2022_paper.html",
                 "y Gao, J. (2021). Grounded language-image pre-training (arXiv:2112.03857). arXiv. "
                 "https://doi.org/10.48550/arXiv.2112.03857")
    cita_larga = (
        "Las citas del informe tienen que resolver contra esta lista, y §15/16, §17.1 y la nota de la "
        "Tabla A.1 —material ya cerrado, que este documento no puede editar— citan el año del "
        "preprint. La v1.0 actualizó tres obras a su versión publicada (esta, ViLD de Gu y otros, y "
        "APE de Shen y otros): es una mejora real, porque sube la proporción de fuentes arbitradas, "
        "pero deja las citas colgando. Se vuelve al año citado. Si querés la versión publicada, hay "
        "que cambiar en la integración estas citas: «L. H. Li et al., 2021» en §15/16 y en la nota de "
        "la Tabla A.1, «Shen et al., 2023» en las dos mismas, «Gu et al., 2021» en §17.1 y en el Anexo "
        "C, y «Chen y Zou (2025)» dos veces en §15/16. "
        "Con este pase, las citas de §15, §16, §17.3, §17.4, §17.5 y de este documento resuelven todas "
        "contra la lista. Queda una que no, y es anterior a la Etapa 6: §17.1 cita «Axis Communications "
        "AB, s. f.» mientras la entrada —y §15/16— dicen 2015. Esa cita hay que corregirla en §17.1 al "
        "integrar; la entrada es la correcta, porque el informe técnico tiene año y número de documento.")
    d.comentario(i, "(2021). Grounded language-image pre-training", cita_larga)

    i = d.unica("Open-vocabulary object detection via vision and language knowledge distillation")
    d.reemplazar(i, "y Cui, Y. (2022). Open-vocabulary object detection via vision and language "
                    "knowledge distillation. International Conference on Learning Representations. "
                    "https://iclr.cc/virtual/2022/poster/6372",
                 "y Cui, Y. (2021). Open-vocabulary object detection via vision and language "
                 "knowledge distillation (arXiv:2104.13921). arXiv. "
                 "https://doi.org/10.48550/arXiv.2104.13921")

    i = d.unica("Aligning and prompting everything all at once")
    d.reemplazar(i, "y Ji, R. (2024). Aligning and prompting everything all at once for universal "
                    "visual perception. En Proceedings of the IEEE/CVF Conference on Computer Vision "
                    "and Pattern Recognition (pp. 13193–13203). "
                    "https://openaccess.thecvf.com/content/CVPR2024/html/Shen_Aligning_and_Prompting_"
                    "Everything_All_at_Once_for_Universal_Visual_CVPR_2024_paper.html",
                 "y Ji, R. (2023). Aligning and prompting everything all at once for universal visual "
                 "perception (arXiv:2312.02153). arXiv. https://doi.org/10.48550/arXiv.2312.02153")

    # --- 2. la obra de Chen y Zou estaba dos veces --------------------------------------------
    i = d.unica("Data-Centric Engineering, 7, e11")
    d.borrar_parrafo(i)

    # --- 3. los sufijos de NVIDIA que citan §15/16 y §17.1 ------------------------------------
    i = d.unica("Grounding DINO. NVIDIA TAO Toolkit Documentation")
    d.reemplazar(i, "NVIDIA. (s. f.-b). Grounding DINO.", "NVIDIA. (s. f.-g). Grounding DINO.")
    d.comentario(
        i, "NVIDIA. (s. f.-g). Grounding DINO.",
        "§15/16 cita «NVIDIA, s. f.-g» para esta ficha y «NVIDIA, s. f.-h» para Triton, y §17.1 cita "
        "«NVIDIA Corporation, s. f.-b» para el Video Codec SDK. La v1.0 unificó las tres bajo NVIDIA "
        "con sufijos de la a a la d, lo que dejó esas citas sin entrada. Se devuelven las etiquetas "
        "citadas. Quedan huecos en la secuencia de sufijos, que es la herencia de haber podado las "
        "entradas huérfanas de esa autoría. Cerrar los huecos exige renumerar y cambiar cuatro citas "
        "en §15/16 y §17.1, y eso es trabajo de integración, no de esta sección.")

    i = d.unica("NVIDIA Triton Inference Server. Recuperado")
    d.reemplazar(i, "NVIDIA. (s. f.-c). NVIDIA Triton Inference Server.",
                 "NVIDIA. (s. f.-h). NVIDIA Triton Inference Server.")

    i = d.unica("NVIDIA Video Codec SDK")
    d.reemplazar(i, "NVIDIA. (s. f.-d). NVIDIA Video Codec SDK.",
                 "NVIDIA Corporation. (s. f.-b). NVIDIA Video Codec SDK.")

    # --- 4. May 2017 vuelve a su lugar alfabético, como la cita de §15/16 --------------------
    i = d.unica("Pantos, R. (Ed.), y May, W. (2017)")
    d.borrar_parrafo(i)
    j = d.unica("OAK-D Pro PoE [Documentación de hardware]")
    d.parrafo_nuevo(
        j,
        "May, W. (2017). HTTP live streaming (R. Pantos, Ed.; RFC 8216). RFC Editor. "
        "https://doi.org/10.17487/RFC8216")
    d.comentario_en_nuevo(
        j, 0,
        "§15/16 cita «May (2017)» y la v1.0 había re-alfabetizado la entrada bajo Pantos, donde nadie "
        "la busca. Vuelve a su lugar, con la forma del listado de la Etapa 1. La entrada de Pantos "
        "(2025), que es otra obra y §15/16 también cita, se queda donde está.")

    # --- 5. Roy (Whalen) 2024 estaba citada y había quedado sin entrada ----------------------
    j = d.unica("Roboflow Universe Projects. (2026)")
    d.parrafo_nuevo(
        j,
        "Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which protocol should you choose? (Update). "
        "Wowza Media Systems. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose")
    d.comentario_en_nuevo(
        j, 0,
        "Alta que repone una baja: §15/16 cita «Roy (2024)» en la enumeración de fuentes de protocolos "
        "de streaming, y la poda de entradas huérfanas de la v1.0 se la llevó. Es la única de las bajas "
        "que estaba citada por una sección viva. Verifiqué las 149 entradas contra las citas de §15, "
        "§16, §17.1, §17.3, §17.4, §17.5 y de este documento.")


# ═══════════════════════════════════════════════════════════ §19.1 · la nota de la Tabla A.1
def anexo_a(d: Documento) -> None:
    i = d.unica("no constituyen un benchmark homogéneo")
    d.reemplazar(i, "L. H. Li et al. (2022)", "L. H. Li et al. (2021)")
    d.reemplazar(i, "Shen et al. (2024)", "Shen et al. (2023)")
    d.comentario(
        i, "L. H. Li et al. (2021)",
        "Los dos años vuelven a lo que dice esta misma nota en el material cerrado de la Etapa 1, de "
        "donde la tabla es copia fila a fila. Es la contrapartida del cambio en la lista de "
        "Referencias.")

    # el typo del primer párrafo del anexo
    i = d.unica("El Anexo A reúne comparativas complementarias")
    d.reemplazar(i, "respaldan el estado del artel", "respaldan el estado del arte")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--origen", type=Path, default=ORIGEN)
    p.add_argument("--destino", type=Path, default=DESTINO)
    a = p.parse_args()

    d = Documento(a.origen, fecha=FECHA)
    antes = _palabras(d)
    comentarios_previos = len(re.findall(r"<w:commentRangeStart", d.ensamblar()))

    seccion_17_6(d)
    seccion_18(d)
    anexo_e(d)
    anexo_a(d)
    referencias(d)

    despues = _palabras(d)
    ensamblado = d.ensamblar()
    comentarios_ahora = len(re.findall(r"<w:commentRangeStart", ensamblado))
    st = d.guardar(a.destino)

    print("\n".join(d.log))
    print(f"\n  cuerpo (vista aceptada): {antes} → {despues} palabras "
          f"({despues - antes:+d}, {100 * (despues - antes) / antes:+.1f} %)")
    print(f"  anclas de comentario: {comentarios_previos} → {comentarios_ahora} "
          f"(los {comentarios_previos} previos se conservan)")
    print(f"  {st}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
