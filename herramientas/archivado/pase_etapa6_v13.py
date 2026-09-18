#!/usr/bin/env python3
"""Pase de la Etapa 6 — §17.6, §18 y §19 · v1.2 → v1.3 (sugerencias sin aceptar).

Origen: la v1.2 que el usuario bajó de Google Docs el 2026-09-12 (todas las sugerencias de la v1.1
aceptadas, sin la lista de Referencias, con 14 hilos de comentarios nuevos, todos suyos). Este pase
responde los 14 hilos con las decisiones que él tomó sobre el análisis
`desarrollando/analisis-comentarios-etapa6-v1.2-2026-09-12.md`.

LO QUE DECIDIÓ EL USUARIO (2026-09-12)
  H01  citar UNA sola cosa: el repositorio público de documentación, que reúne los cinco repos, los
       resultados y las figuras; es la vía de acceso a todo el material que el informe identifica.
  H02/H03  no borrar: fundir §17.6.3 ¶3–4 en un párrafo concreto (qué recalcula cada comprobación).
  H04  la plataforma ESTÁ empaquetada; la construcción y el arranque integral quedan previstos para
       antes de la presentación final. Se alinean las dos frases espejo (§18.6 y Anexo E).
  H05/H14  un solo punto de entrada: el informe remite al repositorio de documentación; el material
       audiovisual va a una carpeta con acceso autorizado enlazada DESDE ese repositorio (no desde el
       informe). El Anexo E pierde nombres de archivo y comandos; la Tabla E.2 queda con las dos
       huellas completas que un tercero puede verificar.
  H06  §18.1 cierra contra la formulación literal de §12.3 («persona sin casco», «sin chaleco»).
  H07  se explica por qué la alerta por episodio se mide con F1 y no con AP; §18.2 cita el mAP50.
  H08  `machinery` es la clase del piloto de extensibilidad: se dice.
  H09  §18.3 ¶5 saltaba a otro nivel de evaluación sin avisar: se reescribe.
  H10  el presupuesto excedido, con su cifra: hasta 250 ms por unidad (§17.1.7) contra 630–890 ms.
  H11  «30 FPS» es la cadencia del material en diferido; el vivo dio 1,16–4,42 fps: se dice.
  H12  §18.5 en cuatro párrafos, con los tres tramos numerados y definidos una vez.
  H13  §18.6: caminos de continuidad para quien siga, cada uno con la base que queda lista y lo que
       falta; cierre «las bases quedan».
  Arrastre: «No implica» → «No implican» (regresión de la bajada; queda absorbida por la reescritura
  de §18.5) y la entrada de referencias del repositorio, que va al acta porque la v1.2 no trae lista.

Todo es sugerencia + comentario: rechazar todas las sugerencias devuelve la v1.2 exacta.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE si el usuario ya trabajó la v1.3 en Google Docs:
# el origen por default es la v1.2 y volver a correrlo pisaría lo que haya hecho después.

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ORIGEN = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.2.docx"
DESTINO = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.3 (sugerencias sin aceptar).docx"
FECHA = "2026-09-12T23:00:00Z"

REPO_URL = "https://github.com/simonll4/e-ovrt-vdp"
SHA_BENCH_V3 = "4557024ecc4ee497ab1fad01d6819206395c10fd794010ed8c1d9198b19a4462"
SHA_CLIP_MANIFEST = "3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75"


def _palabras(d: Documento, hasta: int | None = None) -> int:
    hasta = len(d.units) if hasta is None else hasta
    return sum(len(d.texto(i).split()) for i in range(hasta))


def parrafo(d: Documento, i: int, nuevo: str) -> None:
    """Reemplaza el texto completo de la unidad `i` por `nuevo` (como sugerencia)."""
    viejo = d.texto(i)
    assert viejo.strip(), f"u{i} está vacía"
    d.reemplazar(i, viejo, nuevo)


def tramo(d: Documento, i: int, viejo: str, nuevo: str) -> None:
    assert viejo in d.texto(i), f"u{i} no contiene {viejo[:60]!r}"
    d.reemplazar(i, viejo, nuevo)


# ═══════════════════════════════════════════════════════════ §17.6
def seccion_17_6(d: Documento) -> None:
    # --- H01 · 17.6.1 · citar el repositorio de documentación, una sola vez -------------------
    i = d.unica("El proyecto se organizó en cinco repositorios de software y datos")
    d.agregar_al_final(
        i,
        " Los cinco repositorios de código son públicos y se reúnen, junto con los resultados, sus "
        "artefactos y las figuras, en el repositorio público de documentación del proyecto, "
        f"{REPO_URL} (Carrizo, Guillaumet y Llamosas, 2026), que es la vía de acceso a todo el "
        "material que este informe identifica.")
    d.comentario(
        i, "repositorio público de documentación del proyecto",
        "H01 «¿hace falta citar los repositorios acá?» — Sí, y se cita UNA sola cosa: el "
        "repositorio de documentación, que ya lista los cinco repos de código con su URL, enlaza "
        "los índices de resultados y trae las figuras. Así el informe no carga cinco URLs que "
        "pueden cambiar de rama o de dueño. La URL va inline una vez porque es un punto de acceso, "
        "no una fuente bibliográfica; si preferís APA estricto, se quita de acá y queda sólo en la "
        "entrada de la lista de referencias (la entrada está en el acta del pase, porque esta "
        "versión no trae la lista). Verificado hoy: los siete repos son públicos.")

    # --- H02/H03 · 17.6.3 ¶3–4 · fundir en un párrafo concreto -------------------------------
    i = d.unica("El control del material experimental incluyó dos verificaciones complementarias")
    j = d.unica("La reconstrucción del banco de imágenes fue comprobada por el equipo")
    parrafo(
        d, i,
        "Además de las pruebas de los módulos, dos comprobaciones automáticas cuidan el material "
        "experimental. La primera recalcula las cifras reportadas a partir de los artefactos de cada "
        "corrida y falla si alguna no coincide; al cierre cubría 26 cifras sobre 17 campañas. La "
        "segunda revisa la organización del material de video: estratos, exclusiones, "
        "correspondencia de las anotaciones e integridad de los archivos congelados. Se comprobó, "
        "además, que el banco de imágenes se reconstruye desde sus fuentes y produce el mismo archivo "
        "byte a byte, y que releer los mismos eventos con la misma configuración produce las mismas "
        "alertas. Ninguna de estas comprobaciones sustituye repetir la inferencia en otro equipo.")
    d.comentario(
        i, "dos comprobaciones automáticas cuidan el material",
        "H02/H03 «no entiendo esto, ¿qué suma?» — Suma: es la evidencia de que las cifras del "
        "informe son verificables mecánicamente, y al tribunal le sirve. El problema era que estaba "
        "escrito en abstracto porque el informe no puede nombrar scripts. Los dos párrafos quedan en "
        "uno que dice qué hace cada comprobación, con una sola cifra (26 cifras sobre 17 campañas, "
        "estado del verificador al cierre) y con el límite explícito. Si igual te parece que no "
        "aporta, rechazá la sugerencia y borrá el párrafo: nada más depende de él.")
    d.borrar_parrafo(j)

    # --- H04 · 17.6.4 · el empaquetado está hecho; la comprobación integral, prevista ----------
    i = d.unica("El empaquetado en contenedores quedó definido y validado por configuración")
    parrafo(
        d, i,
        "La plataforma se entrega empaquetada en contenedores. Cada servicio cuenta con su "
        "especificación de construcción, y una composición única declara el conjunto: la consola, el "
        "plano de control, la distribución de alertas, el broker MQTT y las instancias del plano de "
        "medios, una por perfil de modelo, con sus redes, sus volúmenes, sus comprobaciones de salud y "
        "sus dependencias de arranque. Las instancias de inferencia se declaran inactivas y la consola "
        "activa la que requiere cada corrida, bajo la política de una activa a la vez. La composición "
        "preserva la disposición de rutas del entorno de trabajo, condición necesaria porque los "
        "contratos entre módulos intercambian rutas absolutas sobre un sistema de archivos compartido; "
        "dentro de la red interna los extremos se resuelven por nombre de servicio y no por dirección "
        "de anfitrión. Instalar la plataforma en otro equipo requiere disponer de los repositorios y "
        "declarar la raíz del espacio de trabajo, sin ninguna otra ruta fija. Su documentación "
        "operativa acompaña al software en los repositorios, porque este informe no es un manual de "
        "despliegue, y el Anexo E delimita el camino de reproducción y las comprobaciones que "
        "respaldan los resultados.")
    d.comentario(
        i, "La plataforma se entrega empaquetada en contenedores",
        "H04 — Desarrollado en afirmativo, como pediste: el empaquetado es parte de la entrega y el "
        "párrafo describe lo que existe, sin declarar ningún pendiente. Cada afirmación se comprobó "
        "contra los repositorios: los cuatro archivos de construcción (medios, control, distribución y "
        "consola), la composición de trece servicios con sus redes, volúmenes, comprobaciones de salud "
        "y dependencias, el arranque diferido de las instancias de inferencia con la política de una "
        "activa a la vez, la paridad de rutas y la resolución por nombre de servicio. Lo único que el "
        "párrafo no hace es afirmar una portabilidad medida sobre un tercer equipo, porque eso sería "
        "un resultado y no un estado de entrega. Las dos frases espejo, la de 18.6 y la del cierre del "
        "Anexo E, quedaron alineadas con esta.")

    # --- H05 · 17.6.4 ¶3 · el punto de entrada único, dicho en el cuerpo ----------------------
    i = d.unica("El cierre dejó, por tanto, una plataforma experimental documentada")
    d.agregar_al_final(
        i,
        " Todo el material que este informe identifica se alcanza desde el repositorio de "
        "documentación citado en la sección 17.6.1, incluido el acceso autorizado al material "
        "audiovisual, que no se publica.")
    d.comentario(
        i, "Todo el material que este informe identifica",
        "H05 «resolver las referencias a archivos, configs, datos… de manera sencilla» — La forma "
        "sencilla es UN punto de entrada: el informe remite siempre al repositorio de documentación; "
        "ese repositorio mantiene un mapa de artefactos (qué es cada cosa, en qué repo y ruta está, "
        "con enlace) y la sección de acceso autorizado al material audiovisual, donde irá el enlace a "
        "la carpeta de evidencia cuando la armes al final. Así una URL de carpeta no queda impresa en "
        "la tesis y el informe no nombra archivos ni rutas. El Anexo E y el Anexo F remiten a lo "
        "mismo.")


# ═══════════════════════════════════════════════════════════ §18.1 – §18.4
def seccion_18_1_a_18_4(d: Documento) -> None:
    # --- H06 · 18.1 ¶1 · cerrar contra la hipótesis literal de §12.3 --------------------------
    i = d.unica("El proyecto mostró la factibilidad técnica de integrar detección open-vocabulary")
    d.parrafo_nuevo(
        i,
        "Las dos consultas que la hipótesis de la sección 12.3 tomó como ejemplo, «persona sin casco» y "
        "«persona sin chaleco reflectivo», se transformaron en alertas evaluables sobre video, con dos "
        "precisiones que forman parte de la respuesta. La condición no pudo formularse al detector "
        "como una negación literal, porque esa formulación quedó descartada por su precisión, sino "
        "como ausencia del elemento de protección sobre una persona detectada. Y la primera condición "
        "se sostuvo en los tres niveles de evidencia, mientras que la segunda alcanzó la alerta por "
        "episodio con su clasificación por persona todavía abierta.")
    d.comentario_en_nuevo(
        i, 0,
        "H06 — Párrafo nuevo que cierra el círculo con la formulación literal de la hipótesis: las "
        "dos consultas de ejemplo de §12.3, qué se pudo hacer con ellas y con qué matices. Los tres "
        "hechos que lo sostienen están en §17.5 y más abajo en §18.2: E-DIR descartada por precisión "
        "0,146; CR-01 sostenida en percepción, estado por persona y episodio; CR-02 con recall 1,000 "
        "por episodio pero F1 0,479 por persona.")

    # --- H07 · 18.1 ¶2 · por qué F1 y no AP -------------------------------------------------
    i = d.unica("La evidencia principal es la evaluación por episodio de la sección 17.5.4")
    d.agregar_al_final(
        i,
        " El AP, que la literatura reporta para comparar detectores sobre imágenes, se informa en el "
        "nivel de percepción de la sección 17.5.2; la alerta por episodio es una decisión binaria "
        "sobre una ventana temporal y se mide con precisión, recall y F1, que es la métrica que el "
        "protocolo fijó para ese nivel.")
    d.comentario(
        i, "El AP, que la literatura reporta",
        "H07 «¿por qué F1 y no AP?» — Las dos métricas están, cada una en su nivel. El AP resume "
        "precisión y recall de un detector a lo largo de todos los umbrales de confianza sobre "
        "imágenes: es lo que reportan los papers porque evalúan detectores, y acá vive en §17.5.2 "
        "(mAP50 0,551 del perfil operativo sobre el banco). Una alerta por episodio no tiene ranking "
        "ni barrido de umbrales que promediar: para cada episodio anotado, la plataforma alertó o no "
        "dentro de la ventana; lo que corresponde es precisión, recall y F1 sobre episodios, fijado "
        "de antemano en §17.1.7. Y es el resultado principal porque el AP no puede ver el aporte de "
        "la plataforma: de 0,789 a 0,930 las detecciones no cambiaron.")

    # --- H07 (menor) · 18.2 ¶1 · citar el mAP50 ---------------------------------------------
    i = d.unica("La selección de un modelo no pudo resolverse mediante su rendimiento general")
    tramo(
        d, i,
        "gdino-tiny-560 encabezó el mAP50 por delante de gdino-base-560 y de yoloe-26x, y la sección "
        "17.5.2 reportó que conservó el liderazgo en el banco completo, integrado por ese estrato y "
        "otros dos de mayor tamaño.",
        "gdino-tiny-560 encabezó el mAP50 con 0,503, por delante de gdino-base-560, con 0,474, y de "
        "yoloe-26x, y conservó el liderazgo en el banco completo de 6.477 imágenes de tres fuentes, "
        "con 0,551 frente a 0,525; la sección 17.5.2 reporta el desglose por estrato y por clase.")

    # --- H08 · 18.2 · qué es machinery ------------------------------------------------------
    i = d.unica("La extensibilidad sin entrenamiento sí fue ejercida")
    tramo(
        d, i,
        "La extensibilidad sin entrenamiento sí fue ejercida. La incorporación de machinery produjo "
        "AP50 de 0,662 sin ninguna corrida de entrenamiento, según la sección 17.5.2.",
        "La extensibilidad sin entrenamiento sí fue ejercida: se añadió por configuración una clase "
        "ajena al núcleo, la maquinaria de obra, expresada con el prompt machinery, y sin ninguna "
        "corrida de entrenamiento alcanzó AP50 de 0,662 sobre 99 cajas de referencia del piloto de "
        "extensibilidad (sección 17.5.2).")
    tramo(
        d, i,
        "vehicle no produjo detecciones cuando acompañó a machinery y, de manera aislada, obtuvo AP "
        "de 0,026 al localizar la propia maquinaria.",
        "la palabra vehicle, probada como segunda clase, no produjo ninguna detección cuando acompañó "
        "a machinery y, aislada, obtuvo AP de 0,026 porque el modelo la resolvió sobre la propia "
        "maquinaria: para el detector no significó lo que el equipo pretendía.")
    d.comentario(
        i, "la maquinaria de obra, expresada con el prompt machinery",
        "H08 «¿qué es machinery?» — Sí: es la clase nueva del piloto de extensibilidad, ajena a "
        "CR-01/CR-02, agregada por configuración para probar que se puede sumar una clase sin "
        "entrenar; se evaluó contra 99 cajas de referencia del material del piloto (la copia de MOCS "
        "del Anexo F). La segunda mitad del párrafo es el límite: vehicle fue una segunda palabra "
        "probada y el modelo la resolvió sobre la misma maquinaria. Ahora el párrafo lo dice.")

    # --- arrastre de H13 · 18.3 ¶1 · unificar el nombre de lo que NO se midió -----------------
    i = d.unica("La separación entre detección y alerta permitió medir el aporte")
    tramo(
        d, i,
        "no equivale a una evaluación MOT del tracker ni a una garantía de conservación de identidades "
        "en cualquier escena.",
        "no equivale a una evaluación formal de seguimiento multiobjeto ni a una garantía de "
        "conservación de identidades en cualquier escena.")
    d.comentario(
        i, "una evaluación formal de seguimiento multiobjeto",
        "Arrastre de H13. Acá decía «evaluación MOT del tracker», y en 18.6 y 17.5.7 lo mismo se llama "
        "«métricas formales de seguimiento multiobjeto». Dos nombres para una misma ausencia hacen "
        "dudar de si son cosas distintas, que es justo lo que te pasó al leer 18.6. Queda el nombre de "
        "17.5.7 en los dos lugares. La palabra «tracker» sobrevive sólo en las tablas de los anexos "
        "heredados, donde es vocabulario de la métrica y no se toca.")

    # --- H09 · 18.3 ¶5 · otro nivel de evaluación, dicho ------------------------------------
    i = d.unica("La evaluación intermedia sobre 17 clips de obra real")
    parrafo(
        d, i,
        "En el nivel de estado por persona, medido cuadro a cuadro y sin motor temporal sobre 17 clips "
        "de obra real —los 13 del lote de obra real del banco temporal y cuatro de un piloto "
        "anterior—, el F1 cayó a 0,031 para CR-01 y a 0,018 para CR-02, con E-IND a dos cuadros por "
        "segundo y sobre más de diez mil cuadros con persona en cada condición (sección 17.5.3). La "
        "caída provino de la precisión, inferior a 0,02: el detector emitió la condición sobre personas "
        "cuyo estado el anotador humano no podía determinar, y cada una de esas predicciones contó "
        "como falso positivo. En obra real, la distancia mayor no está entre formular la condición en "
        "lenguaje y detectarla, sino entre detectarla y que la escena permita observarla.")
    d.comentario(
        i, "En el nivel de estado por persona, medido cuadro a cuadro",
        "H09 «acá me perdí» — Con razón: el párrafo anterior habla de episodios (2 evaluables, 26 "
        "contra 323 falsos positivos) y este saltaba sin avisar a otro nivel de evaluación —estado por "
        "persona, cuadro a cuadro, sin motor temporal— sobre otro conjunto (17 clips), con jerga que "
        "no se había definido («evaluación intermedia», «conservar esa frontera», «condición "
        "anotable»). Ahora dice de entrada qué nivel es, qué material, qué cifras y por qué cayó. "
        "Cifras y denominadores: Tabla 62 y el texto de §17.5.3.")

    # --- H10 · 18.4 ¶1 · el presupuesto excedido, con cifra ----------------------------------
    i = d.unica("El funcionamiento en vivo quedó demostrado, pero no se identificó")
    parrafo(
        d, i,
        "El funcionamiento en vivo quedó demostrado, pero no dentro del presupuesto de latencia. La "
        "sección 17.1.7 había estimado hasta 250 ms por unidad procesada para el tramo que va desde la "
        "salida del cuadro de la cola hasta el fin de la inferencia; con gdino-tiny-560 sobre la OAK-D, "
        "el p95 de ese tramo se ubicó entre 630 y 890 ms en tres corridas, entre 2,5 y 3,6 veces el "
        "presupuesto. El exceso es del detector y no de la cadena: la misma plataforma con inferencia "
        "simulada resolvió el tramo en 31,8 ms p95. Ninguna de estas cifras mide desde el sensor: la "
        "captura hasta la cola se instrumentó por separado para OAK-D y no se midió para RTSP.")
    d.comentario(
        i, "hasta 250 ms por unidad procesada",
        "H10 «no deja claro lo del presupuesto excedido» — Faltaban el presupuesto y el factor. "
        "§17.1.7.5 estima el tramo previo a la acumulación temporal «entre 35 y 250 ms por unidad "
        "procesada»; la Tabla 64 mide 630–890 ms p95 en vivo (fuera) y 31,8 ms p95 con detector "
        "simulado (dentro). Con eso el lector ve que el exceso es del modelo y no de la plataforma. No "
        "se agregó la comparación con YOLOE en vivo (entra en presupuesto pero no reconoce la "
        "condición) porque esa cifra no está en §17.5; si querés que esté, hay que subirla primero a "
        "la Tabla 64.")

    # --- H11 · 18.4 ¶3 · 30 fps es la cadencia del material, no el tiempo real ----------------
    i = d.unica("El remuestreo regular permitió examinar el efecto de disponer de menos evidencia")
    tramo(
        d, i,
        "El remuestreo regular permitió examinar el efecto de disponer de menos evidencia temporal sin "
        "cambiar las detecciones originales. En los 34 episodios evaluables del rodaje, el F1 por "
        "escena fue 0,789 a 30 FPS, 0,794 a 4,29 FPS, 0,738 a 2 FPS y 0,646 a 1,15 FPS.",
        "El remuestreo regular permitió examinar el efecto de disponer de menos evidencia temporal sin "
        "cambiar las detecciones originales. El banco se evaluó en diferido a la cadencia completa del "
        "material grabado, 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps; para "
        "cubrir esa franja, los 34 episodios evaluables del rodaje se remuestrearon de manera pareada, "
        "y el F1 por escena fue 0,789 a 30 fps, 0,794 a 4,29, 0,738 a 2 y 0,646 a 1,15 fps.")
    d.comentario(
        i, "a la cadencia completa del material grabado, 30 fps",
        "H11 «¿es correcto a 30 fps en tiempo real?» — No es tiempo real, y el texto lo insinuaba "
        "mal: 30 fps es la cadencia completa del material grabado, evaluada en diferido; el camino en "
        "vivo entregó entre 1,16 y 4,42 fps (§17.5.5). Por eso se remuestreó a 4,29 / 2 / 1,15: para "
        "cubrir la franja del vivo con el mismo material y las mismas anotaciones. Ahora el párrafo lo "
        "dice antes de la serie.")


# ═══════════════════════════════════════════════════════════ §18.5 · H12
def seccion_18_5(d: Documento) -> None:
    p1 = d.unica("La literatura de adaptación advierte que modificar pesos")
    p2 = d.unica("La rama de ajuste fino no modificó la conclusión sobre el núcleo")
    p3 = d.unica("La curva de línea base, ajuste de la proyección de clases")
    p4 = d.unica("La medición de retención abierta aporta un resultado especialmente claro")
    p5 = d.unica("El entrenamiento utilizó 2.946 imágenes")
    p6 = d.unica("El cierre del tercer tramo se sostiene primero en la escalera")
    assert [p2, p3, p4, p5, p6] == [p1 + k for k in range(1, 6)]

    parrafo(
        d, p1,
        "La rama de ajuste fino se ejecutó como comparación separada del núcleo, sobre YOLOE-26s, con "
        "una línea base sin entrenar, criterios de ganancia y de retención fijados antes de medir y una "
        "secuencia de autorizaciones que mantuvo distinguibles las decisiones anteriores y posteriores a "
        "cada resultado. Fue una escalera de tres tramos, que aquí se numeran para poder seguirlos: el "
        "primer tramo entrenó sólo la capa de proyección de clases; el segundo liberó más capacidad, "
        "hasta 10,35 millones de parámetros entrenables; el tercero preveía ajustar una variante "
        "entrenable de la familia Grounding DINO. El entrenamiento usó 2.946 imágenes de "
        "construction_site_safety y ppe_siabar, con 483 de validación; CHV quedó fuera para no "
        "compartir fuentes con el banco de evaluación.")
    parrafo(
        d, p2,
        "Ningún tramo produjo un checkpoint adoptable. El primero no alcanzó la ganancia exigida en "
        "cabeza descubierta y perdió retención de la clase persona. El segundo superó el criterio de "
        "ganancia en cabeza descubierta, pero falló las dos retenciones: la del dominio y la de "
        "vocabulario abierto, donde la métrica de retención sobre las 5.000 imágenes de validación de "
        "COCO 2017 pasó de 0,4347 a 0,1247, una caída del 71,3 %; además, su entrenamiento se detuvo en "
        "la época 16 de 60 y el mejor punto había quedado en la primera. El tercero no llegó a "
        "entrenarse: no se cumplieron las condiciones de activación de la escalera y la variante "
        "entrenable no preservaba el linaje del perfil desplegado; el checkpoint publicado de su versión "
        "tiny reprodujo además una anomalía geométrica ajena al proyecto, que reforzó el cierre sin "
        "atribuirse al adaptador propio ni extenderse a toda la familia.")
    parrafo(
        d, p3,
        "Estos veredictos se establecieron sobre el protocolo de la rama y el banco de dominio de la "
        "sección 17.5.2; no implican que ambos ajustes hayan afectado por igual a todas las fuentes ni "
        "que exista una variante ajustada superior según una única métrica. Lo que sí muestran es que, "
        "con ese volumen de datos, subir la capacidad no resolvió la adopción: el límite fue la relación "
        "entre datos y retención, no la cantidad de parámetros, y el resultado del primer tramo no "
        "puede reducirse a falta de capacidad. La literatura de adaptación anticipaba el mecanismo, "
        "porque modificar pesos puede degradar representaciones útiles fuera del dominio de ajuste "
        "según qué parámetros se actualicen (Kumar et al., 2022; Lee et al., 2023), pero no el "
        "resultado de esta receta sobre este material. Tampoco demuestra que todo método de "
        "adaptación falle con ese volumen: no se exploró una tasa de aprendizaje intermedia ni la "
        "familia de técnicas eficientes en parámetros.")
    parrafo(
        d, p4,
        "La rama no modificó la conclusión sobre el núcleo sin entrenamiento. Dejó una decisión de no "
        "adopción sustentada y auditable, no una promesa de mejoras posteriores.")
    d.comentario(
        p1, "que aquí se numeran para poder seguirlos",
        "H12 «se me hizo difícil de entender» — Reordenado en cuatro párrafos: qué fue la rama (con "
        "los tres tramos numerados y definidos una vez, que es lo que hace legible el resto sin volver "
        "a las etiquetas T1/T2/T3 que tu colega objetó), qué pasó en cada tramo, qué significa, y el "
        "cierre. Salió de ~560 a ~440 palabras. Contenido conservado: todas las cifras y veredictos "
        "(Tabla 66 y §17.5.6). Salió la oración sobre la latencia no medida de los checkpoints, que ya "
        "está en §17.5.7. De paso queda absorbida la regresión de la bajada («No implica» por «No "
        "implican»).")
    d.borrar_parrafo(p5)
    d.borrar_parrafo(p6)


# ═══════════════════════════════════════════════════════════ §18.6 · H13
def seccion_18_6(d: Documento) -> None:
    i = d.unica("Las continuidades justificadas se desprenden de lo que quedó fuera")
    j = d.unica("En adaptación, una continuidad defendible exige un nuevo protocolo")
    assert j == i + 1
    parrafo(
        d, i,
        "La plataforma se diseñó para el catálogo completo y se validó sobre su núcleo obligatorio. Las "
        "seis condiciones de riesgo quedaron operacionalizadas con su patrón, su severidad y su ventana "
        "de persistencia, y el motor de patrones las admite a todas: cuáles se activan es materia de "
        "configuración. El marco de métricas definió los tres niveles de evidencia y también las "
        "métricas de seguimiento multiobjeto. La arquitectura declaró desde el comienzo qué capacidades "
        "eran núcleo y cuáles complementarias previstas. Lo que el protocolo recortó fue el alcance de "
        "la validación, no el del diseño.")
    d.parrafo_nuevo(
        i,
        "Por eso las extensiones condicionadas encuentran su lugar ya definido. Las condiciones CR-03 a "
        "CR-06 se incorporan por configuración y esperan lo que el núcleo no necesitó: una referencia "
        "humana de relaciones espaciales y, para la zona restringida, una parametrización de la escena. "
        "Las métricas de seguimiento multiobjeto esperan identidades anotadas, no capacidad nueva, "
        "porque la identidad temporal ya está implementada y medida. La cota de falsas alarmas espera "
        "horas de obra anotada, y la adaptación del modelo, un corpus independiente del banco bajo el "
        "protocolo que la rama comparativa dejó fijado. En todos los casos lo que falta es evidencia, "
        "no arquitectura.")
    d.comentario(
        i, "La plataforma se diseñó para el catálogo completo",
        "H13, cuarta vuelta, con el encuadre que pediste: **no es «acá queda una base para que otro "
        "siga», es «el diseño contempló todo el alcance aunque se haya implementado y medido un "
        "núcleo»**. Es una afirmación más fuerte y la sostiene el propio informe con su vocabulario: "
        "17.1 dice que el catálogo retiene seis condiciones en tres niveles, que CR-01 y CR-02 son el "
        "«núcleo obligatorio de validación» y que las demás se conservan como «extensiones "
        "condicionadas»; 17.3 clasifica las capacidades en «núcleo» y «complementario previsto» y "
        "declara que el motor admite el catálogo completo de patrones, con la activación dependiendo de "
        "la configuración. La frase que cierra la idea es que **el recorte fue de la validación y no "
        "del diseño**, y la del segundo párrafo, que **lo que falta es evidencia y no arquitectura**. "
        "Sobreviven las correcciones anteriores: la identidad temporal figura como implementada y "
        "medida, y ya no se la llama «tracker».")
    d.borrar_parrafo(j)


# ═══════════════════════════════════════════════════════════ Anexo E · H05/H14
def anexo_e(d: Documento) -> None:
    # --- entrada: de dónde se alcanza todo -----------------------------------------------------
    i = d.unica("La reproducción se organiza por material y por nivel de evaluación")
    d.agregar_al_final(
        i,
        " Todos los elementos que siguen se alcanzan desde el repositorio de documentación del "
        "proyecto citado en la sección 17.6.1, que mantiene un mapa de artefactos con la ubicación de "
        "cada uno; el material audiovisual se conserva con acceso autorizado y se solicita por esa "
        "misma vía.")
    d.comentario(
        i, "que mantiene un mapa de artefactos",
        "H14 «apuntamos a archivos de los repos con identificadores que pierden al lector» — El "
        "anexo deja de nombrar archivos y comandos. Cada material se describe por lo que es y el "
        "repositorio de documentación lleva el mapa de artefactos: qué es cada cosa, en qué repositorio "
        "y ruta está, con enlace. El lector del informe tiene una sola puerta; el que quiera el archivo "
        "concreto lo encuentra en el mapa, que se mantiene al día sin tocar el informe.")

    # --- Tabla E.1: dos celdas con nombre de archivo ----------------------------------------
    t1 = d.unica("Elementos que se conservan", kind="tbl")
    d.celda(t1, 1, 1,
            "bench_v3.json, manifiesto de composición, anotaciones y referencia de cada fuente",
            "El banco bench_v3 con su manifiesto de composición, las anotaciones y la referencia de "
            "cada fuente")
    d.celda(t1, 3, 1,
            "Manifiesto, clips elegibles y referencia clip_gt.v2",
            "Manifiesto, clips elegibles y referencia temporal humana")

    # --- Tabla E.2: quedan las dos huellas completas ---------------------------------------
    i = d.unica("La Tabla E.2 consigna la identificación de los contenidos congelados")
    parrafo(
        d, i,
        "La Tabla E.2 consigna las dos huellas que identifican los materiales congelados sobre los que "
        "se sostienen las comparaciones: el banco de imágenes y el manifiesto del banco temporal de 47 "
        "clips. Este último no sustituye a la referencia histórica utilizada por los experimentos sobre "
        "el bloque de rodaje, cuya huella acompaña a ese manifiesto.")
    t2 = d.unica("Identificación conservada", kind="tbl")
    filas = d.filas(t2)
    assert filas[2][0].startswith("Banco de imágenes"), filas[2][0]
    assert len(filas) == 7, len(filas)
    d.celda(t2, 2, 0, "Banco de imágenes bench_v3.json", "Banco de imágenes bench_v3")
    d.celda(t2, 2, 1, "4557024ecc4ee497…a4462", SHA_BENCH_V3)
    d.celda(t2, 2, 2,
            "Abreviatura de identificación; el valor completo se contrasta con el manifiesto del banco.",
            "Huella SHA-256 completa del archivo del banco.")
    for fila in (3, 4, 5, 6):
        d.borrar_fila(t2, fila)
    d.comentario_en_celda(
        t2, 2, 1, SHA_BENCH_V3[:16],
        "H14 (Tabla E.2) — Quedan sólo las dos huellas completas, que son las únicas que un tercero "
        "puede comprobar de punta a punta; las dos se verificaron hoy contra los archivos en disco. "
        "Las siete abreviadas se van: por la propia nota de la tabla «no servían para una verificación "
        "criptográfica», y eran el ruido que perdía al lector. Sus valores completos acompañan a cada "
        "artefacto en el repositorio y figuran en el mapa de artefactos.")
    i = d.unica("El signo de elipsis identifica una abreviatura")
    viejo = d.texto(i).split("Nota. ", 1)[1]
    d.reemplazar(
        i, viejo,
        "Las huellas de los estratos del banco de imágenes, de los conjuntos de prompts y del "
        "manifiesto histórico del bloque de rodaje acompañan a cada artefacto en el repositorio de "
        "documentación y no se transcriben. Una huella identifica un contenido; no acredita derechos de "
        "uso ni validez de una anotación. Fuente: elaboración propia a partir de los materiales "
        "congelados.")

    # --- la prosa: de ocho párrafos a seis pasos, sin comandos --------------------------------
    a = d.unica("Los materiales identificados en la Tabla E.2 se reproducen por caminos distintos")
    b = d.unica("Para el banco temporal, la referencia se obtiene de las anotaciones humanas")
    c = d.unica("La secuencia operativa distingue construcción, procesamiento y evaluación")
    e = d.unica("La relectura del plano de control opera sobre los eventos de percepción conservados")
    f = d.unica("La agregación conserva la unidad estadística y las exclusiones")
    g = d.unica("La repetición en vivo exige, además, fijar el entorno")
    h = d.unica("La definición de G2A aplicada en este trabajo se restringe")
    k = d.unica("Las pruebas automatizadas y los verificadores descritos en la sección 17.6.3")
    assert [b, c, e, f, g, h, k] == [a + n for n in range(1, 8)]

    parrafo(
        d, a,
        "**Banco de imágenes.** Se reconstruye desde las fuentes y particiones identificadas, sin "
        "reemplazarlas por una descarga actual de contenido distinto; se verifica su huella contra la "
        "Tabla E.2; y se evalúan las predicciones conservadas de cada corrida contra la referencia, "
        "reportando por separado los estratos de obra curada, CHV y SHEL5K, porque la composición "
        "desbalanceada del banco condiciona el agregado. La semilla de la partición de calibración se "
        "conserva al reproducir la evaluación del estado por persona.")
    parrafo(
        d, b,
        "**Banco temporal.** La referencia se obtiene de las anotaciones humanas mediante conversión, "
        "validación y promoción al conjunto evaluable. El nivel de exportación de la herramienta de "
        "anotación debe corresponder al que espera la conversión: una exportación por tarea no se trata "
        "como una exportación por proyecto, porque el error produce una referencia negativa sin aviso. "
        "Antes de calcular métricas se comprueban los atributos, las correcciones adjudicadas, los "
        "intervalos de episodio y la pertenencia de cada clip al material reportable.")
    parrafo(
        d, c,
        "**Relectura y evaluación.** Las detecciones conservadas de una corrida se releen con el plano "
        "de control bajo la misma configuración efectiva, y las alertas resultantes se evalúan contra "
        "la referencia temporal. Repetir la relectura con la misma configuración permite examinar el "
        "determinismo del motor; cambiar granularidad, evaluador, vocabulario o ventanas define otra "
        "combinación y exige identificarla como tal. Los clips positivos se evalúan por episodios; los "
        "negativos se conservan para el conteo de falsos positivos; las re-confirmaciones con la "
        "condición todavía activa se cuentan aparte y no se reclasifican como errores. Cada operación "
        "identifica los artefactos de la ejecución que se reproduce y no los reemplaza por una "
        "configuración actual que haya cambiado; esta secuencia describe la reproducción, no un "
        "procedimiento de instalación.")
    d.borrar_parrafo(e)
    parrafo(
        d, f,
        "**Agregación.** Se conservan la unidad estadística y las exclusiones del procedimiento "
        "original: un promedio de latencias por clip no se presenta como percentil, los intervalos por "
        "remuestreo mantienen la unidad y el pareamiento del contraste original, y los percentiles de "
        "tramos con relojes distintos no se suman. La precaución importa sobre todo al comparar "
        "granularidades con detecciones idénticas o cadencias obtenidas del mismo material.")
    parrafo(
        d, g,
        "**Repetición en vivo.** Exige fijar el entorno, verificar que los servicios estén preparados y "
        "establecer las suscripciones antes de publicar: el orden de lanzamiento es control, "
        "distribución y medios, y la espera del publicador por su suscriptor protege el comienzo del "
        "canal de alertas sin sustituirse por una pausa supuesta. El periodo de preparación del modelo "
        "queda fuera de la ventana de medición. La latencia G2A se restringe al intervalo desde la "
        "salida del cuadro de la cola hasta el resultado de inferencia; al relacionarla con la "
        "literatura debe mantenerse explícita la diferencia con el extremo físico de captura (Bachhuber "
        "et al., 2018), y una medición ausente de RTSP no se completa con la cifra de captura de "
        "OAK-D.")
    d.borrar_parrafo(h)
    parrafo(
        d, k,
        "**Alcance.** Las pruebas automatizadas y las comprobaciones de la sección 17.6.3 verifican las "
        "propiedades para las que fueron construidas. La reproducción byte a byte del banco de imágenes "
        "acredita que el instrumento de evaluación es idéntico, y no sustituye a repetir la inferencia "
        "sobre otro equipo, cuyos tiempos dependen del hardware y del entorno de ejecución que cada "
        "corrida declara. El empaquetado en contenedores de la sección 17.6.4 provee ese entorno y fija "
        "las versiones de los servicios. El material conservado respalda la inspección y la "
        "reconstrucción de las ejecuciones documentadas.")
    d.comentario(
        a, "Se reconstruye desde las fuentes y particiones identificadas",
        "H14 (prosa del anexo) — Los ocho párrafos pasan a seis pasos con entrada en negrita, por "
        "material, sin ningún nombre de archivo ni comando (build_bench_v3.py, --run, --bench-coco, "
        "eovrt-control replay/live/evaluate-alerts: fuera). Se conserva lo que es trampa real —el "
        "nivel de exportación de la anotación, el orden de arranque, la definición de G2A desde la "
        "cola— y se funden las dos advertencias que repetían reglas de §17.5. El paso «Alcance» queda "
        "alineado con el nuevo 17.6.4.")


# ═══════════════════════════════════════════════════════════ Anexo F · acceso al material
def anexo_f(d: Documento) -> None:
    i = d.unica("El acceso a código, pesos, anotaciones y material audiovisual se trata por separado")
    d.agregar_al_final(
        i,
        " El material audiovisual del proyecto —los clips del rodaje propio y los recortes del lote de "
        "obra real— no se publica: se conserva en una carpeta de evidencia con acceso autorizado, que "
        "se solicita a los autores a través del repositorio de documentación citado en la sección "
        "17.6.1.")


# ═══════════════════════════════════════════════════════════ §18.6 · frase espejo del empaquetado
def espejo_18_6(d: Documento) -> None:
    # La frase espejo de §18.6 ¶5 vivía en el párrafo que H13 da de baja (absorbida en «Portabilidad»).
    # Se comprueba que no quede otra mención de portabilidad «no verificada» fuera del nuevo 17.6.4.
    for i in range(len(d.units)):
        t = d.texto(i)
        if "que esta entrega no verificó" in t:
            raise AssertionError(f"u{i} conserva la frase espejo del empaquetado")


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
    seccion_18_1_a_18_4(d)
    seccion_18_5(d)
    seccion_18_6(d)
    anexo_e(d)
    anexo_f(d)
    espejo_18_6(d)

    despues = _palabras(d) + sum(len(Documento.texto_de(x).split())
                                 for xs in d.nuevos.values() for x in xs)
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
