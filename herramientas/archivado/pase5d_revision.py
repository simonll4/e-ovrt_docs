#!/usr/bin/env python3
"""Pase 5d — correcciones de la revisión completa del 2026-09-07 (cinco auditorías cruzadas).

    §17.4 v1.11 → v1.12   ·   §17.5 v1.7 → v1.8   ·   §17.3 v1.9 → v1.10   ·   §17.1 v1.17 → v1.18

El usuario pidió una revisión completa que asegurara que los ajustes de los pases 5, 5b y 5c
tuvieran sentido y quedaran coherentes entre secciones y con la plataforma. Se corrieron cinco
auditorías en paralelo (protocolo↔resultados, diseño↔implementación, §17.4↔código, §17.5↔índices
de `results/`, §15/16↔vocabulario y los 52 comentarios) y cada hallazgo que este pase aplica se
verificó contra el artefacto antes de escribirlo. Todo entra como SUGERENCIA con su comentario; lo
que era decisión editorial del usuario quedó en el informe de la revisión, no acá.

Lo que corrige, por documento (el detalle y la fuente de cada cifra están en los comentarios):

§17.4  · la evidencia visual: sólo la previsualización viene habilitada por defecto, el video
         anotado no (`schemas.py:527`), y el default invierte la regla opt-in del diseño (§17.3)
       · el ejemplo de alerta: 3.633 ms no viaja en la alerta, viaja el fotograma 109; los ms de
         la alerta son reloj del equipo de control
       · el DTO decía «sin valor por defecto» y el código dice `= None`
       · la configuración del entrenamiento: «única variable» era falso (difieren alcance, épocas
         y optimizador); el criterio de checkpoint es mAP50-95; se nombra el modelo (YOLOE-26 s),
         el material de retención (COCO val2017), el aumento de datos y el costo (7,7 / 23,8 min
         en una A30); asignación efectiva de las cuatro fuentes de la Tabla 23
       · el tercer tramo: causa según `operacion/131` §5 (linaje + escalera), sin la fórmula
         «sin línea base sana»
       · «Ninguno se incorporó»: los perfiles ft existen en el catálogo; «un servicio por perfil»:
         son 9 de 11; «persiste la configuración efectiva»: la distribución sólo la expone;
         «espera a que haya un suscriptor»: lo configura el orquestador
       · perfil operativo: nombre, fp16 (opción de corrida), base-560 comparte umbrales;
         YOLOE-26 con tamaños y puente tiny/base ↔ Swin-T/Swin-B
       · Tabla 39: la operación sobre fuentes en vivo no tenía destino; «cuatro capacidades»
         mezclaba filas de la tabla con propiedades del diseño; la conjunción híbrida no se ejecutó
       · Tabla 56: la columna no eran «contratos» (bus, cierre, repositorio de hechos, reporte)
       · Tabla 58/56: report.md faltaba; Tabla 59: intro alineada a sus seis filas, «motor de
         patrones»; Tabla 60: `spatial_absence` sin definir; seguidor sin método; 4 clips piloto y
         doble anotación en §17.4.6; dos puntos en prosa; «acá», «hoy»; cr01_cr02_v2 con glosa
§17.5  · L31: 0,582/0,520 son de obra curada, no del estrato de chaleco; chaleco no tiene GT en
         el estrato mayor · L33: el 0,000 de las cuatro variantes es del banco anterior; «inservible
         para CR-01» contradecía la Tabla 61 corregida · L35: `vehicle` no es sinónimo y las 252
         cajas eran de otro material · L39: los 17 clips son 13 del estrato B + 4 del piloto ·
         L57: nocturno 80–120 px = 0 % · Fig. 4.6: el casco no está detectado en ese cuadro, sí en
         los vecinos; se identifica clip e instantes · Tabla 64: paridad n = 1, «detector de
         referencia» era el detector simulado · L129: `large` falla con geometría normal ·
         L162: p99 sí se computó por corrida; el 20 era la corrida simulada; curva FP-ventana no
         ejecutada · L164: L2 y L3 en oraciones separadas; L6 según `results/index.md` ·
         Tabla 65: antes/después de person y mAP50, umbral 0,05, COCO, modelo, «veredicto negativo»
         · nombres de métricas (AP@0,5 / t_alert-system) · ΔFP_tracking · juzgabilidad definida ·
         referencias por severidad declaradas · 0,02 → 0,029 · «motor temporal» → «motor de patrones»
§17.3  · L333 generalizaba la garantía del orden a todos los canales · planos ↔ rutas de §16.5.3 ·
         «vídeo»
§17.1  · «temporales, Por último» · Liu et al. 2023 → 2024 (el listado sólo trae 2024) · «material
         propio» para un banco con videos públicos · «Sección» → «sección» · Tabla 26 «se acota»
         vs «orientativo» (L289 y §17.4)

INCREMENTAL: parte de los `.docx` VIGENTES. Para una bajada nueva de Google Docs, `--origen-*`.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE (2026-09-07).
# Los `--origen-*` por default apuntan a `desarrollando/archivado/`; correrlo tal cual reproduce las
# cuatro salidas y PISA lo que el usuario haya hecho después en Google Docs. El motor deja respaldo.

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import RPR_B, Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ARCH = BASE / "archivado"
ORIGEN = {
    "17.4": ARCH / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.11 (entrega del pase 5c; base del pase 5d).docx",
    "17.5": ARCH / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.7 (entrega del pase 5b; base del pase 5d).docx",
    "17.3": ARCH / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.9 (entrega del pase 5; base del pase 5d).docx",
    "17.1": ARCH / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.17 (entrega del pase 5; base del pase 5d).docx",
}
DESTINO = {
    "17.4": BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.12 (sugerencias sin aceptar).docx",
    "17.5": BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.8 (sugerencias sin aceptar).docx",
    "17.3": BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.10 (sugerencias sin aceptar).docx",
    "17.1": BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.18 (sugerencias sin aceptar).docx",
}


def _tabla(d: Documento, frag: str) -> int:
    return d.unica(frag, kind="tbl")


def _fila(d: Documento, t: int, col: int, texto: str) -> int:
    for k, f in enumerate(d.filas(t)):
        if f[col].strip() == texto:
            return k
    raise SystemExit(f"fila con {texto!r} no encontrada en la tabla u{t}")


# ====================================================================== §17.4
def pase_17_4(origen: Path, destino: Path) -> None:
    d = Documento(origen)

    # --- 17.4.1 · Tabla 56: la primera columna no son sólo contratos ---------------------------
    t56 = _tabla(d, "Contrato del diseño")
    d.celda(t56, 0, 0, "Contrato del diseño", "Elemento del diseño", rpr=RPR_B)
    d.celda(t56, _fila(d, t56, 0, "Repositorio de eventos"), 0,
            "Repositorio de eventos", "Repositorio de hechos")
    d.celda(t56, _fila(d, t56, 0, "Reporte experimental"), 1,
            "Reporte consolidado report.json y por experimento",
            "Reporte consolidado por experimento, report.json y report.md")
    d.comentario_en_celda(t56, 0, 0, "Elemento del diseño",
                          "La columna decía «Contrato del diseño», pero cuatro filas no son contratos de "
                          "la Tabla 46 de §17.3: el envoltorio del bus es un patrón de acople, el cierre "
                          "de corrida es un evento de ciclo de vida, el repositorio se llama «de hechos» "
                          "en 17.3.8.2 y el reporte es una proyección. Con «Elemento» todas las filas "
                          "caben y el nombre del repositorio vuelve al de §17.3. La alternativa es "
                          "agregar a la Tabla 46 dos filas (envoltorio y ciclo de vida), que de hecho "
                          "son contratos versionados; esa es una decisión de diseño y va en el informe "
                          "de la revisión.")

    # --- 17.4.2 · DTO: el default es nulo, no inexistente; «acá» ------------------------------
    i = d.unica("aparece acá como opcional y sin valor por defecto")
    d.reemplazar(i, "aparece acá como opcional y sin valor por defecto",
                 "aparece aquí como opcional y con valor nulo por defecto")
    d.comentario(i, "La misma estructura se declara en el código",
                 "Contradecía al propio fragmento de código (`track_id: str | None = None`) y al "
                 "párrafo de 17.4.8, que dice «con valor por defecto». Verificado en "
                 "`contracts/detection.py`. «Acá» es coloquial; §17.3 usa «aquí».")

    # --- 17.4.2 · el ejemplo de alerta: qué viaja y qué se deriva ------------------------------
    i = d.unica("y permite verificar la ventana de confirmación desde los hitos que la propia alerta transporta")
    d.reemplazar(i,
                 "y permite verificar la ventana de confirmación desde los hitos que la propia alerta "
                 "transporta: la primera evidencia cae a los 3.633 ms del video y la confirmación a los "
                 "7.633, exactamente los 4.000 ms configurados para la condición.",
                 "y permite verificar la ventana de confirmación. La alerta transporta el fotograma de "
                 "la primera evidencia, el 109, y el de la confirmación, el 229. A los 30 cuadros por "
                 "segundo del clip, esos fotogramas corresponden a 3.633 y 7.633 ms de video, "
                 "exactamente los 4.000 ms configurados para la condición. Los dos instantes en "
                 "milisegundos que la alerta también conserva pertenecen al reloj del equipo de control "
                 "y no al tiempo de video.")
    d.comentario(i, "La alerta interna registra la confirmación del episodio",
                 "El fragmento no trae los 3.633 ms: trae `first_evidence_frame_index: 109`, y "
                 "`first_evidence_ms` / `alert_registered_ms` son reloj monotónico del host "
                 "(`contracts/alerts.py`), distan 11 ms entre sí. El 3.633 sale de 109 cuadros a 30 "
                 "fps, que es la cadencia del clip (verificada con ffprobe y con 7.633,33 / 229). Así "
                 "el lector puede rehacer la cuenta desde lo que ve. De paso se va el único dos puntos "
                 "que quedaba en la prosa de §17.4.")

    # --- 17.4.3 · lo que hace cada servicio, con precisión ------------------------------------
    i = d.unica("rechaza las solicitudes concurrentes señalando la que está en curso y persiste la configuración efectiva")
    d.reemplazar(i, "y persiste la configuración efectiva que utilizó.",
                 "y los dos planos persisten además la configuración efectiva que utilizaron, que el "
                 "módulo de distribución expone por su interfaz.")
    d.comentario(i, "Los tres módulos de la cadena se implementaron",
                 "La distribución no escribe una configuración efectiva: la expone por GET /api/config "
                 "y resume canal y modo en su `distribution_summary.json` (`distributor.py`). Medios y "
                 "control sí escriben `effective_config.yaml`.")

    i = d.unica("La no pérdida en el canal de alertas no depende de ese orden sino del publicador")
    d.reemplazar(i, "sino del publicador, que espera a que haya un suscriptor antes de emitir.",
                 "sino del publicador, configurado por el orquestador para esperar a que haya un "
                 "suscriptor antes de emitir.")
    d.comentario(i, "En una corrida en vivo el orquestador inicia primero",
                 "La espera existe porque el orquestador la configura: `wait_for_subscriber_ms` vale 0 "
                 "por defecto en los dos publicadores y el runner de la consola lo fuerza a 10 s o más "
                 "(`runner.py`). Sin esa palabra, el texto atribuía al servicio una garantía que es de "
                 "la orquestación.")

    # --- 17.4.4 · pattern set con glosa (comentario de Matías), catálogo, perfil operativo -----
    i = d.unica("El conjunto de patrones efectivo del núcleo es cr01_cr02_v2.")
    d.reemplazar(i, "El conjunto de patrones efectivo del núcleo es cr01_cr02_v2.",
                 "El conjunto de patrones efectivo del núcleo es el que el catálogo de configuración "
                 "identifica como cr01_cr02_v2.")
    d.comentario(i, "El conjunto de patrones efectivo del núcleo",
                 "Responde al comentario de Matías sobre qué formato lleva ese nombre: es el "
                 "identificador del conjunto de patrones en el catálogo de configuración del plano de "
                 "control (`configs/patterns/cr01_cr02_v2.yaml`), igual que gdino-tiny-560 lo es del "
                 "catálogo de modelos. Con la glosa no hace falta tipografía especial.")

    i = d.unica("Reúne variantes de Grounding DINO en sus versiones tiny y base")
    d.reemplazar(i,
                 "Reúne variantes de Grounding DINO en sus versiones tiny y base, cada una con "
                 "resolución de entrada de 800 y de 560 píxeles, y YOLOE en cuatro tamaños,",
                 "Reúne variantes de Grounding DINO en sus versiones tiny y base, que corresponden a "
                 "los backbones Swin-T y Swin-B que presenta la sección 15.2.1.1, cada una con "
                 "resolución de entrada de 800 y de 560 píxeles, y YOLOE-26 en cuatro tamaños, s, m, "
                 "l y x,")
    d.reemplazar(i, "MM-Grounding DINO", "MM-Grounding-DINO")
    d.comentario(i, "El catálogo de perfiles de modelo materializa",
                 "§15 nombra las variantes de Grounding DINO por backbone (Swin-T, Swin-B) y §17 por "
                 "tiny y base: faltaba el puente. §15.2.1.2 advierte que las cifras de YOLO v8 no "
                 "deben presentarse como de YOLOE-26, y acá la versión no aparecía; los tamaños s, m, "
                 "l y x son los del catálogo (`configs/models/yoloe/`). La grafía MM-Grounding-DINO, "
                 "con guion, es la de §15 y la del proyecto original.")

    i = d.unica("el despliegue integral define un servicio por perfil del catálogo")
    d.reemplazar(i, "define un servicio por perfil del catálogo.",
                 "define un servicio por cada uno de los nueve perfiles de servicio del catálogo, y "
                 "deja fuera los dos perfiles de ajuste fino que se conservan sólo para reproducir su "
                 "evaluación.")
    d.comentario(i, "El núcleo no fija un modelo único",
                 "El compose integral define nueve servicios de medios (mock, cuatro Grounding DINO, "
                 "cuatro YOLOE-26) y el catálogo tiene once perfiles: los dos que faltan son "
                 "`yoloe-26s-ft-t1` y `-t2`, con sus pesos, que existen para poder repetir la "
                 "evaluación única de la rama de ajuste fino. Verificado en `infra/platform/"
                 "docker-compose.yml` y `configs/models/yoloe/`.")

    i = d.unica("El perfil fijado por criterio pre-registrado para las corridas en vivo es la variante tiny")
    d.reemplazar(i, "El perfil fijado por criterio pre-registrado para las corridas en vivo es",
                 "El perfil operativo, fijado por criterio pre-registrado para las campañas temporales "
                 "y en vivo, es")
    d.agregar_al_final(i,
                       " La inferencia corre en coma flotante de 16 bits sobre la unidad gráfica, una "
                       "opción de la corrida y no del perfil, y la variante base de 560 píxeles, "
                       "gdino-base-560, comparte resolución, umbrales y postproceso.")
    d.comentario(i, "Cada perfil declara sus umbrales y su postproceso en el catálogo",
                 "Tres cosas. §17.5 habla de «perfil operativo» desde su primera tabla y §17.4 nunca "
                 "usaba la expresión, así que el término se introduce acá. La precisión numérica es un "
                 "elemento de configuración que §17.3 exige declarar (Tablas 42 y 46) y faltaba: es "
                 "`half_precision: true` en las corridas del banco, una opción de corrida y no del "
                 "catálogo (`schemas.py:375`). Y §17.5 dice que tiny-560 y base-560 comparten "
                 "resolución y umbrales: ahora §17.4 lo declara (ambos a 560 px, caja 0,30, texto "
                 "0,25).")

    # --- 17.4.5 · Tabla 58 y el bloque del árbol --------------------------------------------
    t58 = _tabla(d, "manifest.effective.yaml")
    f = _fila(d, t58, 0, "Soporte experimental")
    d.celda(t58, f, 1, "report.json;", "report.json; report.md")
    nota58 = d.unica("Los nombres de archivo corresponden a los artefactos implementados")
    d.parrafo_nuevo(nota58,
                    "La disposición del repositorio del soporte experimental es la siguiente.",
                    muestra=d.unica("La ejecución experimental consolida así los cuatro componentes"))
    d.comentario_en_nuevo(nota58, 0,
                          "El bloque del árbol de directorios era el único de los cuatro bloques de "
                          "código sin oración que lo anuncie. La Tabla 58 omitía report.md, que el "
                          "árbol sí lista y el soporte experimental sí escribe.")

    # --- 17.4.6 · cuatro clips piloto y la doble anotación ---------------------------------
    i = d.unica("Esa revisión corrigió las cajas y las trayectorias de los 47 clips del banco")
    d.agregar_al_final(i,
                       " Cuatro clips de un piloto anterior sobre video de obra real, anotados con la "
                       "misma referencia de atributos y ajenos al banco temporal, se conservaron para la "
                       "medición del estado por persona que informa la sección 17.5.3. La anotación la "
                       "realizó un único anotador, sin la doble anotación sobre el 20 % del material que "
                       "la sección 17.1.5.4 exige para la anotación propia, desviación que la sección "
                       "17.5.7 registra como limitación.")
    d.comentario(i, "Sobre esa propuesta se realizó la pasada humana en CVAT",
                 "Dos cosas que §17.5 usa y §17.4 no declaraba. (1) La medición del estado por persona "
                 "sobre video (Tabla 62) corre sobre 17 clips: los 13 del estrato de obra real del "
                 "banco temporal más 4 de un piloto anterior que no integran los 47 "
                 "(`results/bench_nivel_a/index.md`, campaña NA1). (2) §17.1.5.4 hace obligatoria la "
                 "doble anotación del 20 % para toda anotación propia; §17.5.7 la lista como limitación "
                 "pero nadie decía que es una desviación del protocolo. Es el mismo patrón que la "
                 "desviación de partición de 17.4.7.")

    # --- 17.4.7 · Tabla 59: intro alineada a sus filas; motor de patrones -------------------
    i = d.unica("La Tabla 59 reúne esa evidencia, concentrada en corrección de contratos")
    d.reemplazar(i,
                 "concentrada en corrección de contratos, cierre de corridas, paridad entre caminos, "
                 "determinismo y funcionamiento de la integración.",
                 "concentrada en gobierno por configuración, cierre de corridas, paridad entre "
                 "caminos, determinismo del motor y funcionamiento de la integración.")
    t59 = _tabla(d, "Propiedad verificada")
    d.celda(t59, _fila(d, t59, 0, "Motor temporal e idempotencia"), 0,
            "Motor temporal e idempotencia", "Motor de patrones e idempotencia")
    d.comentario(i, "El criterio de cierre de la implementación exigió",
                 "La enumeración prometía «corrección de contratos» y ninguna fila la verifica: la "
                 "primera habla de configuraciones validadas, no de eventos contra su esquema. Ahora "
                 "nombra lo que las seis filas son. Y «motor temporal» era el único lugar de §17.4 con "
                 "ese nombre; §17.1 y §17.3 dicen «motor de patrones» quince veces. §17.5 se unifica "
                 "en el mismo pase.")

    # --- 17.4.7 · alcance efectivo: núcleo, fuentes en vivo, «cuatro capacidades» ----------
    i = d.unica("La concentración del prototipo en el núcleo validable no responde a una reducción tardía")
    d.agregar_al_final(i,
                       " Las doce capacidades del núcleo y la operación sobre fuentes en vivo quedaron "
                       "implementadas, se describen en las secciones 17.4.1 a 17.4.5 y se ejercieron "
                       "en las campañas de la sección 17.5.")
    j = d.unica("Cuatro capacidades quedaron implementadas y medidas.")
    d.reemplazar(j, "Cuatro capacidades quedaron implementadas y medidas.",
                 "Dos capacidades opcionales de la Tabla 39 y dos propiedades del diseño quedaron "
                 "implementadas y medidas.")
    d.reemplazar(j, "Las tres estrategias de detección se implementaron y su comparación se ejecutó.",
                 "Las tres estrategias de detección se implementaron y su comparación se ejecutó, con "
                 "la salvedad de la variante híbrida por conjunción que declara la sección 17.5.6.")
    d.comentario(j, "La identidad persistente de sujeto opera como decorador",
                 "Cotejado fila por fila contra la Tabla 39. La operación sobre fuentes en vivo "
                 "(complementario previsto) no tenía destino declarado en 17.4.7, y las doce filas del "
                 "núcleo tampoco recibían una oración de cierre. De las «cuatro capacidades», sólo dos "
                 "son filas de la tabla (identidad, distribución); las estrategias vienen de 17.3.4.3 "
                 "y la paridad de 17.3.6.3. Y §17.5.6 dice que la conjunción no se ejecutó, así que "
                 "«su comparación se ejecutó» necesitaba la salvedad.")

    # --- 17.4.7 · evidencia visual: el default real y su relación con el diseño -------------
    i = d.unica("La gestión de evidencia visual controlada quedó implementada como opción de corrida")
    d.reemplazar(i,
                 "Las dos posibilidades vienen habilitadas por defecto y se declararon apagadas en "
                 "todas las campañas del banco, conforme a la política de minimización de evidencia "
                 "visual que fija el diseño, de modo que",
                 "La previsualización viene habilitada por defecto, un valor que invierte la regla de "
                 "habilitación explícita que el diseño fija para los módulos opcionales, y el video "
                 "anotado viene deshabilitado. Las campañas del banco declararon apagadas las dos, "
                 "conforme a la política de minimización de evidencia visual, de modo que")
    d.comentario(i, "La gestión de evidencia visual controlada",
                 "Corrección de un error mío del pase 5: decía que las dos opciones venían habilitadas "
                 "por defecto, y en el esquema `save_previews` es True pero `save_annotated_video` es "
                 "False (`schemas.py:522,527`). Además §17.3 (17.3.4.4) exige que ningún módulo "
                 "opcional opere como comportamiento implícito y DA-08 fija la minimización como "
                 "comportamiento base; un default encendido contradice eso, y el texto lo presentaba "
                 "como conforme. Ahora declara la desviación y cómo la neutralizaron las campañas "
                 "(verificado: 0 corridas del banco con previsualización).")

    # --- 17.4.7 · rama de ajuste fino: causa del tercer tramo, perfiles ft ------------------
    i = d.unica("La rama comparativa de ajuste fino se ejerció por completo")
    d.reemplazar(i, "y la escalera de tramos pre-registrada se ejecutó entera.",
                 "y la escalera de tres tramos, registrada antes de entrenar, se ejecutó entera.")
    d.reemplazar(i,
                 "El tercer tramo se cerró con causa técnica, porque la familia de modelos que le "
                 "correspondía no ofrecía una línea base sana sobre la que la diferencia fuera "
                 "interpretable, y la escalera pre-registrada impedía sustituirla por otra.",
                 "El tercer tramo, que habría ajustado MM-Grounding-DINO como linaje entrenable de "
                 "Grounding DINO, se cerró con causa técnica por dos razones. La escalera lo "
                 "condicionaba a que alguno de los dos tramos anteriores alcanzara sus criterios, y "
                 "ninguno lo hizo. Y la variante que iba a ajustarse entregaba cajas degeneradas con "
                 "origen en el punto de control publicado, verificado con la biblioteca de referencia "
                 "sin código del proyecto, mientras que la variante sana de esa familia no había "
                 "mostrado ventaja en ninguna dimensión evaluada, de modo que el linaje ajustado no "
                 "habría sido el del perfil operativo.")
    d.reemplazar(i, "Ninguno se incorporó como modelo de servicio, y los valores por tramo se informan",
                 "Ninguno se adoptó como modelo de servicio ni entró al despliegue, y sus perfiles "
                 "permanecen en el catálogo sólo para reproducir la evaluación. Los valores por tramo "
                 "se informan")
    d.comentario(i, "La rama comparativa de ajuste fino se ejerció por completo",
                 "Tres ajustes verificados. (1) La escalera no está en §17.1 (cero apariciones de "
                 "«escalera» o «tramo»): se pre-registró en la jornada de ajuste fino, así que el texto "
                 "no puede atribuírsela al protocolo. (2) La causa del tercer tramo decía «sin línea "
                 "base sana», y la verificación experimental del 01-09 fijó que esa fórmula no se "
                 "sostiene: la variante base de MM-Grounding-DINO es geométricamente sana; lo que no "
                 "hay es línea base de la variante que iba a ajustarse (tiny, cajas degeneradas con "
                 "origen en el checkpoint publicado, reproducidas con `transformers` puro y hash "
                 "verificado) ni una que valga la pena (base sin ventaja). El cierre se encabeza por "
                 "linaje y por escalera; las cajas van de refuerzo. Ahora también se nombra la "
                 "familia, que el texto nunca decía. (3) «Ninguno se incorporó como modelo de "
                 "servicio»: los perfiles `yoloe-26s-ft-t1/-t2` existen en el catálogo con sus pesos; "
                 "lo que no hubo es adopción ni despliegue.")

    # --- 17.4.7 · conjunto de ajuste: «desviación» ambigua; salvedad de retención -----------
    i = d.unica("El subconjunto de ajuste reunió 2.946 imágenes")
    d.reemplazar(i, "y la desviación es consecuencia de cumplir la regla de partición y no de apartarse de ella.",
                 "y ese exceso es consecuencia de aplicar la regla de partición y no de apartarse de ella.")
    j = d.unica("El cumplimiento de esa regla tuvo un límite que conviene declarar")
    d.reemplazar(j, "y la retención medida sobre ese estrato se lee con esa salvedad.",
                 "y la retención medida sobre el banco, que incluye ese estrato, se lee con esa salvedad.")
    d.comentario(i, "El subconjunto de ajuste reunió",
                 "«La desviación» nombraba el exceso sobre el rango de tamaño y el párrafo siguiente "
                 "usa «se apartó del protocolo» para otra cosa, la fuente compartida: un lector podía "
                 "leer que la misma desviación cumple y no cumple. Y la Tabla 65 no reporta retención "
                 "por estrato, sólo sobre el banco entero, así que la salvedad se refiere al banco.")

    # --- 17.4.7 · asignación de fuentes, material de retención, aumento y costo -------------
    d.parrafo_nuevo(j,
                    "La asignación efectiva de las cuatro fuentes de la sección 17.1.6.2 fue la "
                    "siguiente. SHEL5K y CHV integran el banco de evaluación como los estratos de 5.000 "
                    "y 1.330 imágenes, y CHV es la fuente que quedó excluida íntegramente del ajuste. "
                    "construction_site_safety aportó 2.203 imágenes al ajuste y es además el origen del "
                    "estrato curado de obra, que es la desviación declarada arriba. ppe_siabar aportó "
                    "las 743 restantes. La retención open-vocabulary se midió sobre las 5.000 imágenes "
                    "de validación de COCO 2017, un material ajeno al dominio y distinto del estrato de "
                    "5.000 imágenes del banco.",
                    muestra=i)
    d.parrafo_nuevo(j,
                    "El aumento de datos fue el conjunto por defecto de la biblioteca de entrenamiento, "
                    "mosaico, variación de color, traslación, escala, volteo horizontal y borrado "
                    "aleatorio, sin ajustes propios, y quedó registrado en la configuración efectiva "
                    "de cada corrida. El costo fue de 7,7 minutos para el primer tramo y de 23,8 para "
                    "el segundo, sobre una unidad gráfica NVIDIA A30 del clúster de cómputo.",
                    muestra=i)
    d.comentario_en_nuevo(j, 0,
                          "§17.1 promete asignar cada fuente retenida a un rol antes de ejecutar (17.1.6, "
                          "Tabla 23 con cuatro nombres) y §17.4/§17.5 nunca nombraban ninguna: hablaban "
                          "de «la única fuente que el banco incorpora completa» o «el estrato de mayor "
                          "cobertura de chaleco». El lector no podía cerrar el círculo. Verificado en "
                          "`finetuning_v1.summary.json` (css 2.203 + ppe 743 = 2.946; val 483), "
                          "`bench_v3.md` (estratos) y `t2_coco_retention_base.yaml` (COCO val2017, "
                          "5.000). El «banco generalista, n = 5.000» de la Tabla 65 colisionaba con el "
                          "estrato de 5.000 del banco; ahora tiene nombre.")
    d.comentario_en_nuevo(j, 1,
                          "§17.1 exige declarar el aumento de datos antes de entrenar (17.1.6.4) y "
                          "registrar horas de GPU, tiempo y parámetros (17.1.7.4); ninguno aparecía. "
                          "Aumento: son los defaults de la biblioteca (`args.yaml`: mosaic 1,0, hsv, "
                          "translate 0,1, scale 0,5, fliplr 0,5, erasing 0,4). Tiempos: columna `time` "
                          "de `results.csv` de cada corrida (7,7 y 23,8 min); GPU A30 según los "
                          "registros del clúster. Si el clúster tiene que nombrarse, §17.3 ya lo llama "
                          "por su nombre.")

    # --- 17.4.7 · configuración del entrenamiento: sin «única variable», con modelo ---------
    k = d.unica("Los dos tramos entrenados compartieron el perfil de entrenamiento")
    d.reemplazar(k,
                 "Los dos tramos entrenados compartieron el perfil de entrenamiento, porque la "
                 "comparación por única variable obliga a mantenerlo idéntico. Las imágenes se "
                 "procesaron a 640 píxeles de lado en lotes de ocho, con semilla fija y ejecución "
                 "determinista, sobre la partición de 2.946 imágenes de ajuste y 483 de validación. En "
                 "cada tramo se conservó el punto de control de mejor precisión media sobre las cuatro "
                 "clases de validación y no el de la última época.",
                 "Los dos tramos entrenados ajustaron la variante s de YOLOE-26 sobre la misma "
                 "partición de 2.946 imágenes de ajuste y 483 de validación, con imágenes a 640 "
                 "píxeles de lado, lotes de ocho, semilla fija y ejecución determinista, y en cada uno "
                 "se conservó el punto de control de mejor mAP50-95 sobre las cuatro clases de "
                 "validación y no el de la última época. Lo que la escalera varía es el alcance "
                 "entrenable. El primer tramo entrenó sólo la proyección de clases, 3.096 parámetros, "
                 "en la modalidad de linear probing que describe la sección 15.2.4. El segundo entrenó "
                 "el detector completo con las rutas de prompt congeladas, 10,35 millones de "
                 "parámetros, y modificó además su régimen de época y de optimización por una enmienda "
                 "registrada antes de observar resultado alguno.")
    m = d.unica("El régimen de época y de optimización es la diferencia declarada entre ambos")
    d.reemplazar(m, "El régimen de época y de optimización es la diferencia declarada entre ambos.",
                 "Ese régimen es la segunda diferencia entre ambos.")
    d.comentario(k, "Los dos tramos entrenados",
                 "Corrección de mi párrafo del pase 5b. Decía «comparación por única variable» y a "
                 "renglón seguido listaba tres diferencias (alcance entrenable, épocas, optimizador); la "
                 "que define la escalera, el alcance, vivía sólo en el párrafo opcional del optimizador. "
                 "Ahora el alcance está acá con sus dos cifras, y el tercer párrafo se puede borrar sin "
                 "perderlas. Además el criterio de checkpoint es mAP50-95 (`checkpoint_policy: "
                 "best_metrics_mAP50-95_B_all_four_val_classes`), no «precisión media»; y el modelo "
                 "ajustado, YOLOE-26 s, no se nombraba en ninguna parte de §17.4 ni de §17.5, cuando "
                 "§15.2.4 ya dice que YOLOE ofrece linear probing y full tuning.")

    # --- 17.4.8 · Tabla 60 y la identidad ---------------------------------------------------
    t60 = _tabla(d, "Familia nueva de condiciones")
    d.celda(t60, _fila(d, t60, 0, "Familia nueva de condiciones"), 1,
            "no cubierta por spatial_absence", "no cubierta por el evaluador de ausencia espacial")
    i = d.unica("pero el seguidor y el orden del flujo son deterministas")
    d.reemplazar(i, "pero el seguidor y el orden del flujo son deterministas",
                 "pero el seguidor, que asocia cajas de persona por solapamiento entre cuadros "
                 "consecutivos, y el orden del flujo son deterministas")
    i = d.unica("La detección normalizada incluye hoy un campo de identidad")
    d.reemplazar(i, "incluye hoy un campo", "incluye un campo")
    d.comentario(i, "El evento de percepción admite además información",
                 "«spatial_absence» era un identificador interno que ni §17.3 ni §17.4 definen (§17.3 "
                 "lo llama «inferencia espacial de ausencia»). El seguidor no tenía método: §15.3 "
                 "presenta SORT, ByteTrack y variantes, y el implementado es una asociación por "
                 "solapamiento IoU entre cuadros consecutivos, sin modelo de movimiento "
                 "(`sources/tracking.py`, umbral 0,20). «Hoy» fecha el texto.")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


# ====================================================================== §17.5
def pase_17_5(origen: Path, destino: Path) -> None:
    d = Documento(origen)

    # --- 17.5.1 · nombres de métricas ---------------------------------------------------------
    i = d.unica("Los nombres abreviados de esta sección son los del marco de métricas.")
    d.reemplazar(i, "Los nombres abreviados de esta sección son los del marco de métricas.",
                 "Los nombres abreviados de esta sección siguen al marco de métricas, con dos "
                 "equivalencias. AP50 y mAP50 designan la precisión media a solapamiento 0,5 que el "
                 "marco escribe AP@0,5, y la latencia de alerta es el intervalo que el marco llama "
                 "t_alert-system.")
    d.comentario(i, "Rigen las reglas de lectura fijadas",
                 "La oración prometía los nombres del marco y §17.5 abrevia distinto: §17.1 escribe "
                 "AP@0,5 y t_alert-system, §17.5 mAP50, AP50 y latencia de alerta. Con las dos "
                 "equivalencias la promesa es cierta.")

    # --- 17.5.2 · Tabla 61 y la prosa de percepción ------------------------------------------
    t61 = _tabla(d, "Veredicto por combinación")
    fb = _fila(d, t61, 0, "gdino-base-560")
    d.celda(t61, fb, 4, "Retenida como contraste de mayor cobertura para CR-01 y chaleco.",
            "Retenida como contraste de mayor cobertura de cabeza descubierta y chaleco.")

    i = d.unica("La especialización del perfil base también apareció en chaleco")
    d.reemplazar(i,
                 "con AP 0,582 frente a 0,520 del perfil operativo sobre el estrato de mayor cobertura "
                 "de esa clase. En los tres estratos, persona y casco se mantuvieron entre 0,70 y 0,89 "
                 "de AP, mientras que chaleco quedó entre 0,55 y 0,58. La asimetría no dependió de una "
                 "única fuente, porque se sostuvo en los tres.",
                 "con AP 0,582 frente a 0,520 del perfil operativo sobre el estrato de obra curada. "
                 "Para el perfil operativo, persona y casco se mantuvieron entre 0,70 y 0,89 de AP en "
                 "los dos estratos públicos, mientras que chaleco quedó en 0,553 y 0,520 en los dos "
                 "estratos que anotan esa clase. La asimetría no dependió de una única fuente, porque "
                 "se sostuvo en ambos.")
    d.comentario(i, "La especialización del perfil base también apareció en chaleco",
                 "Verificado en `results/bench_imagenes/index.md`. Los 0,582 y 0,520 son el AP de "
                 "chaleco sobre `bench_obra` (147), no sobre el estrato de mayor cobertura de esa clase, "
                 "donde dan 0,576 y 0,553. Chaleco no tiene referencia en el estrato de 5.000, así que "
                 "«en los tres estratos» no podía sostenerse, y el 0,520 quedaba fuera del rango "
                 "«0,55–0,58» que el texto daba. Persona y casco del campeón: 0,770/0,707 en el "
                 "estrato de 5.000 y 0,862/0,886 en el de 1.330.")

    i = d.unica("La familia YOLOE presentó una limitación distinta")
    d.reemplazar(i,
                 "Sus cuatro variantes produjeron AP 0,000 para bare_head, la clase de cabeza "
                 "descubierta, en el estrato que la anota de forma nativa.",
                 "Sus cuatro variantes produjeron AP 0,000 para bare_head, la clase de cabeza "
                 "descubierta, sobre el banco anterior al congelado, y la variante mayor repitió el "
                 "cero sobre el estrato que anota esa clase de forma nativa.")
    d.reemplazar(i, "esa ceguera la volvió inservible para CR-01 en la configuración evaluada.",
                 "esa ceguera la volvió inservible para la formulación directa de CR-01 en la "
                 "configuración evaluada.")
    d.comentario(i, "La familia YOLOE presentó una limitación distinta",
                 "Dos precisiones del índice del banco. El 0,000 «en las cuatro variantes» se midió "
                 "sobre el banco anterior (196 imágenes); sobre el estrato de 5.000 sólo corrieron 26x "
                 "y 26s, ambas con 0,000. Y «inservible para CR-01» reabría la incoherencia que el "
                 "pase 5 cerró en la Tabla 61: la columna mide la formulación directa, el núcleo opera "
                 "con la indirecta, y el Nivel A nunca se corrió con YOLOE, así que sobre CR-01 por la "
                 "vía indirecta no debe afirmarse nada.")

    i = d.unica("La extensibilidad semántica se ejerció sobre una clase nueva")
    d.reemplazar(i,
                 "Sobre el mismo material, un sinónimo produjo 0 detecciones y otra palabra generó "
                 "252 cajas, ninguna correcta.",
                 "Sobre el mismo material, la palabra vehicle no produjo ninguna detección cuando "
                 "acompañó a machinery en el vocabulario y, aislada, produjo 118 cajas con AP 0,026, "
                 "porque el modelo la resolvió sobre la maquinaria misma.")
    d.comentario(i, "La extensibilidad semántica se ejerció sobre una clase nueva",
                 "Corregido contra el acta del piloto (`operacion/94` §3). `vehicle` no es un "
                 "sinónimo de `machinery`; junto a él dio 0 detecciones y aislada 118 cajas con AP "
                 "0,026, el 67 % sobre lo que la referencia llama maquinaria. Las 252 cajas «ninguna "
                 "correcta» eran de `gloves` sobre un video del rodaje, otro material, y no están en "
                 "ningún índice de `results/`.")

    # --- 17.5.3 · los 17 clips, juzgabilidad, nocturno --------------------------------------
    i = d.unica("La medición sobre video abarcó 17 clips de obra real")
    d.reemplazar(i,
                 "La medición sobre video abarcó 17 clips de obra real, un material distinto del "
                 "estrato que integra el banco temporal, y no incluyó el motor temporal.",
                 "La medición sobre video abarcó 17 clips de obra real, los 13 del estrato de obra "
                 "real del banco temporal y 4 de un piloto anterior, evaluados al nivel del estado por "
                 "persona sobre su referencia de atributos, submuestreados a 2 Hz y sin calibración de "
                 "umbrales, con el punto de operación desplegado, y no incluyó el motor de patrones.")
    d.comentario(i, "El nivel intermedio evaluó si la evidencia perceptiva",
                 "Corrección de un error mío del pase 5. Decía que los 17 clips eran «un material "
                 "distinto del estrato que integra el banco temporal»; la campaña NA1 "
                 "(`results/bench_nivel_a/index.md`) consolida los 13 clips del estrato B más 4 del "
                 "piloto del 18-07. Lo distinto es el nivel de la medición (estado por persona sobre "
                 "atributos, no episodios) y el punto de operación (desplegado, sin calibración, a "
                 "2 Hz). §17.4.6 declara ahora los 4 clips del piloto.")

    i = d.unica("El evaluador excluyó del denominador 1.414 cuadros con persona no juzgables")
    d.reemplazar(i, "1.414 cuadros con persona no juzgables para CR-01",
                 "1.414 cuadros con persona no juzgables para CR-01, aquellos en los que el anotador "
                 "no pudo determinar el estado,")
    i = d.unica("Esa frontera tiene al menos tres ejes")
    d.reemplazar(i, "en el clip nocturno del estrato las mismas bandas quedan entre 6 y 13 %.",
                 "en el clip nocturno del estrato la banda de 80 a 120 píxeles cae a 0 % y las "
                 "siguientes, hasta 320, quedan entre 6 y 13 %.")
    d.reemplazar(i, "Tampoco la juzgabilidad humana anticipa la del sistema",
                 "Tampoco la juzgabilidad humana anticipa el rendimiento del sistema")
    d.comentario(i, "Esa frontera tiene al menos tres ejes",
                 "Dos ajustes. El nocturno: en `operacion/103` §7.1 la banda de 80–120 px da 0,0 % y "
                 "las de 120–320 dan 6,1–13,2 %, así que «las mismas bandas entre 6 y 13 %» tapaba el "
                 "cero. Y «la juzgabilidad del sistema» reintroducía la confusión por la que se "
                 "descartó la figura: la juzgabilidad es del anotador; lo del sistema es rendimiento. "
                 "La primera aparición de «no juzgables» quedó definida en el párrafo anterior.")

    # --- 17.5.4 · Figura 4.6, referencias por severidad, ΔFP_tracking -----------------------
    i = d.unica("Fotograma de la corrida de línea de base sobre un clip del bloque de rodaje")
    d.reemplazar(i,
                 "Fotograma de la corrida de línea de base sobre un clip del bloque de rodaje, en un "
                 "instante posterior a la alerta, con el motor en estado sostenido. El casco detectado "
                 "sobre la mesa no suprime la condición, porque CR-01 se evalúa sobre el sujeto y no "
                 "sobre la escena.",
                 "Fotograma del clip a_p1_c04 del bloque de rodaje a los 8,5 s, en la corrida de línea "
                 "de base, con la alerta emitida a los 7,3 s y el motor en estado sostenido. El casco "
                 "visible sobre la mesa, que el detector marca en cuadros vecinos, no suprime la "
                 "condición, porque CR-01 se evalúa sobre la región del sujeto y no sobre la escena.")
    d.comentario(i, "Fotograma del clip a_p1_c04",
                 "Corrección de mi nota del pase 5. En el cuadro mostrado (8,5 s, fotograma 255) el "
                 "detector no emite ninguna caja de casco, y la imagen tampoco la dibuja: sólo persona "
                 "0,88 y chaleco 0,86. El casco de la mesa sí se detecta en los cuadros vecinos "
                 "(8,43–8,70 s). Verificado en el `detections.jsonl` de la corrida. La nota identifica "
                 "ahora clip e instantes, que el epígrafe no daba y que la propia imagen muestra en su "
                 "cabecera y su línea de tiempo.")

    i = d.unica("La diferencia fue coherente con ventanas de confirmación de 7,0 y 4,0 s")
    d.agregar_al_final(i,
                       " Las referencias por severidad de la sección 17.1.7.5 no se usaron como criterio "
                       "de aceptación, porque el propio protocolo las condiciona a una recalibración "
                       "previa que esta evaluación no realizó, y sus valores se leen como dato.")
    d.comentario(i, "Las referencias por severidad",
                 "La Tabla 30 de §17.1 fija objetivos por severidad (latencia de alerta, TTFD, "
                 "cobertura) y §17.5 nunca los leía ni decía por qué: la cobertura de CR-02, 0,281, "
                 "queda lejos del ≥ 0,70 de su severidad sin una palabra. El propio 17.1.7.5 dice que "
                 "esos valores deben recalibrarse antes de usarse como criterio de aceptación, y esta "
                 "evaluación no lo hizo. Declararlo cierra el hueco sin acomodar nada.")

    i = d.unica("El resultado robusto del estrato fue la asimetría de falsos positivos")
    d.agregar_al_final(i,
                       " Esa asimetría es el ΔFP_tracking que adopta el marco de métricas de la sección "
                       "17.1.7, y su signo es el contrario al del riesgo que la sección 17.1.10 "
                       "anticipaba, que el seguimiento agregara complejidad sin reducir falsas alarmas.")
    d.comentario(i, "Esa asimetría es el",
                 "§17.1 adopta ΔFP_tracking (17.1.7.4) y la Tabla 35 lo fija como mitigación del riesgo "
                 "«el tracker agrega complejidad sin reducir falsas alarmas». El dato estaba acá (26 "
                 "contra 323) pero nadie lo nombraba ni lo leía contra ese riesgo, que no se "
                 "materializó.")

    # --- 17.5.5 · Tabla 64 y la resolución del banco ----------------------------------------
    t64 = _tabla(d, "Condición o material")
    fi = _fila(d, t64, 1, "Relectura frente a transmisión")
    d.celda(t64, fi, 2, "Paridad byte a byte · 0 eventos perdidos",
            "0 eventos perdidos · paridad byte a byte verificada en una corrida y protegida por prueba automatizada")
    d.celda(t64, fi, 3, "n = 6 corridas del rodaje",
            "n = 6 corridas del rodaje para los eventos; n = 1 corrida para la paridad")
    fd = _fila(d, t64, 1, "Detector de referencia")
    d.celda(t64, fd, 1, "Detector de referencia",
            "Sobrecarga de la plataforma con detector simulado, en diferido")
    d.celda(t64, fd, 4, "Dentro del presupuesto declarado en la sección 17.1.7.",
            "Costo propio de la cadena sin inferencia, dentro del presupuesto de la sección 17.1.7.")
    d.comentario_en_celda(t64, fi, 1, "Relectura frente a transmisión",
                          "Dos celdas corregidas contra `results/realtime/index.md` y las actas. La "
                          "paridad byte a byte se verificó en una corrida en vivo de extremo a extremo y "
                          "se protege con una prueba de mutación; el rodaje no la re-verificó (acta del "
                          "rodaje, §parity). Lo que sí vale para las 6 corridas es `bus_dropped_events` "
                          "= 0. Y la fila «Detector de referencia» (p50 14,7 / p95 31,8 ms, n = 20) es la "
                          "corrida con `model_name: mock` en CPU sobre archivo de video: mide la "
                          "sobrecarga propia de la plataforma, no un detector ni una corrida en vivo.")

    i = d.unica("Con 34 episodios evaluables, las diferencias menores que 0,02")
    d.reemplazar(i, "las diferencias menores que 0,02 quedan dentro de la resolución del banco",
                 "las diferencias del orden de un episodio, 0,029 de recall, quedan dentro de la "
                 "resolución del banco")
    d.comentario(i, "Con 34 episodios evaluables",
                 "El 0,02 era mío, del pase 5, y no sale de ningún artefacto. Con 34 episodios, un "
                 "episodio vale 1/34 = 0,029 de recall; esa es la resolución. La diferencia que el "
                 "párrafo llama ruido (0,875 contra 0,866) es 0,009, menor que un episodio.")

    # --- 17.5.6 · caminos no adoptados, Tabla 65 ---------------------------------------------
    i = d.unica("La estrategia directa quedó descartada por un veto de precisión")
    d.reemplazar(i, "cuyo umbral de 0,5 se fijó de antemano",
                 "cuyo umbral de 0,5 se fijó de antemano en el pre-registro de la comparación de "
                 "estrategias")
    d.reemplazar(i, "al atravesar el motor temporal", "al atravesar el motor de patrones")

    i = d.unica("La fusión híbrida por disyunción fue ejecutada y refutada")
    d.reemplazar(i, "dentro del motor temporal", "dentro del motor de patrones")
    d.reemplazar(i, "MM-Grounding DINO", "MM-Grounding-DINO")
    d.reemplazar(i,
                 "y las otras dos entregaron cajas cuya geometría las volvía inservibles, con origen "
                 "en el punto de control publicado y no en el adaptador que las integró.",
                 "otra entregó cajas degeneradas con origen en el punto de control publicado y no en "
                 "el adaptador que las integró, y la tercera localizó mal con geometría normal.")
    d.comentario(i, "La familia MM-Grounding-DINO se integró",
                 "La verificación experimental del 01-09 (`operacion/131`) prohíbe decir que las dos "
                 "variantes fallan igual: tiny entrega cajas degeneradas con origen en el checkpoint "
                 "publicado (hash verificado, reproducido sin código del proyecto); large localiza mal "
                 "con geometría normal, una falla distinta. La grafía con guion es la de §15.")

    t65 = _tabla(d, "Punto o tramo")
    f1 = _fila(d, t65, 0, "Primer tramo entrenado")
    f2 = _fila(d, t65, 0, "Segundo tramo entrenado")
    d.celda(t65, f1, 2, "Quedó a 0,0045 del umbral y redujo person 11,62 %, con tope de 10 %.",
            "Quedó a 0,0045 del umbral de AP50 0,05 y redujo person de 0,7843 a 0,6932 (−11,62 %), "
            "con tope de 10 %.")
    d.celda(t65, f2, 2,
            "Detención temprana 16/60, mejor época 1; mAP50 protegido -43,4 %; retención "
            "open-vocabulary 0,4347 a 0,1247 (-71,3 %) · n = 5.000 imágenes del banco generalista.",
            "Detención temprana 16/60, mejor época 1; person de 0,7843 a 0,3943 (−49,7 %) y mAP50 en "
            "dominio de 0,4193 a 0,2374 (−43,4 %); retención open-vocabulary 0,4347 a 0,1247 "
            "(−71,3 %) · n = 5.000 imágenes de validación de COCO 2017.")
    for f in (f1, f2):
        d.celda(t65, f, 3, "NO-GO pre-registrado; checkpoint no adoptado.",
                "Veredicto negativo pre-registrado; checkpoint no adoptado.")
    nota65 = d.unica("Los puntos medidos pertenecen a una rama comparativa separada")
    d.agregar_al_final(nota65,
                       " Los tres puntos corresponden a la variante s de YOLOE-26. El primer tramo "
                       "entrenó sólo la proyección de clases, 3.096 parámetros, y el segundo el detector "
                       "completo con las rutas de prompt congeladas, 10,35 millones. La retención "
                       "open-vocabulary se midió sobre un material ajeno al dominio, distinto del "
                       "estrato de 5.000 imágenes del banco.")
    d.comentario(nota65, "Los puntos medidos pertenecen a una rama comparativa separada",
                 "Cuatro ajustes verificados en `finetuning/runs/*/eval` y las actas de la jornada. "
                 "(1) §17.1.7.4 exige informar valor de referencia, valor posterior y variación; la "
                 "tabla daba sólo porcentajes: ahora person 0,7843 → 0,6932 (T1) y 0,7843 → 0,3943, "
                 "mAP50 0,4193 → 0,2374 (T2). «mAP50 protegido» no estaba definido; es el mAP50 en "
                 "dominio de la regla de retención. (2) El umbral de ganancia (AP50 ≥ 0,05) había que "
                 "deducirlo. (3) «Banco generalista, n = 5.000» colisionaba con el estrato de 5.000: "
                 "es COCO val2017. (4) La familia ajustada no se nombraba en ninguna parte; «NO-GO» no "
                 "está definido en el informe, §17.1 habla de veredicto y reglas de aceptación.")

    # --- 17.5.7 · métricas no computadas, limitaciones ---------------------------------------
    i = d.unica("El marco de métricas admite además medidas que esta evaluación no reporta")
    d.reemplazar(i, "que es la que integra el motor temporal.", "que es la que integra el motor de patrones.")
    d.reemplazar(i, "no se informa acá", "no se informa aquí")
    d.reemplazar(i,
                 "La precisión media promediada sobre el rango de umbrales de solapamiento y el "
                 "percentil 99 de latencia quedaron sin computar, el primero porque la lectura se fijó "
                 "en un único umbral y el segundo porque las corridas en vivo procesaron entre 20 y "
                 "295 unidades, muy por debajo de lo que ese percentil requiere.",
                 "La precisión media promediada sobre el rango de umbrales de solapamiento quedó sin "
                 "computar, porque la lectura se fijó en un único umbral. El percentil 99 de latencia "
                 "se computó por corrida y no se consolidó como resultado comparativo, porque las "
                 "corridas en vivo procesaron entre 30 y 295 unidades, muy por debajo de lo que ese "
                 "percentil requiere.")
    d.agregar_al_final(i,
                       " La curva de falsos positivos en función de la duración de la ventana, que la "
                       "sección 17.1.5.2 prevé como eje de la calibración empírica, no se ejecutó, y "
                       "las ventanas se usaron con sus valores de protocolo.")
    d.comentario(i, "El marco de métricas admite además medidas",
                 "Tres correcciones contra los artefactos. El p99 sí está computado por corrida "
                 "(`p99_latency_ms` y `g2a.p99_ms` en cada `summary.json`); lo que falta es "
                 "consolidarlo, la misma fórmula que el texto ya usa para la memoria del acelerador. "
                 "El «20» era la corrida diferida con detector simulado, no una corrida en vivo: las "
                 "en vivo van de 30 a 295. Y §17.1.5.2 promete evaluar la curva de falsos positivos "
                 "contra la duración de la ventana; nadie decía que no se hizo. «Acá» es coloquial y "
                 "era mío; el informe dice «aquí».")

    i = d.unica("Ocho limitaciones acotan la lectura de todo lo anterior")
    d.reemplazar(i,
                 "La referencia temporal no tuvo doble anotación ni medida de acuerdo entre anotadores, "
                 "y los bordes de episodio se adjudicaron por criterio único en seis clips.",
                 "La referencia temporal no tuvo doble anotación ni medida de acuerdo entre anotadores. "
                 "Los bordes de episodio se adjudicaron por criterio único en seis clips.")
    d.reemplazar(i, "El seguimiento no se midió en obra real con multitud.",
                 "El seguimiento no tiene métricas formales en obra real con multitud, aunque un clip "
                 "con 127 personas mostró la fragmentación de identidades que explica la precisión por "
                 "sujeto de ese estrato.")
    d.comentario(i, "Ocho limitaciones acotan la lectura",
                 "«Ocho» seguido de siete oraciones: la segunda fundía dos limitaciones del catálogo "
                 "(L2, sin doble anotación; L3, seis bordes adjudicados). Y la sexta quedó "
                 "desactualizada respecto de `results/index.md`, que el 09-08 levantó su parte "
                 "descriptiva: el clip con 127 personas puso al seguidor en multitud real (182 "
                 "identidades con falsos positivos) y sigue en pie sólo la ausencia de métricas "
                 "formales. Restaurar las ocho tal como estaban era la decisión D5-A; esto no las "
                 "quita, corrige un dato.")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


# ====================================================================== §17.3
def pase_17_3(origen: Path, destino: Path) -> None:
    d = Documento(origen)

    i = d.unica("El plano de medios produce evidencia perceptiva y el plano de control la interpreta.")
    d.reemplazar(i, "El plano de medios produce evidencia perceptiva y el plano de control la interpreta.",
                 "El plano de medios, la ruta de datos de la sección 16.5.3, produce evidencia "
                 "perceptiva, y el plano de control, su ruta de control, la interpreta.")
    d.comentario(i, "La plataforma se estructura alrededor de la separación",
                 "§16.5.3 llama «ruta de datos» y «ruta de control» a lo que §17.3 y §17.4 llaman "
                 "planos de medios y de control, más de cien veces, y ninguna sección hacía el puente. "
                 "Acá es donde §17.3 remite a §16.5.3, así que acá va la equivalencia.")

    i = d.unica("Todo consumidor se suscribe antes de que su productor publique")
    d.reemplazar(i,
                 "porque la respuesta de creación de un consumidor implica su disponibilidad.",
                 "porque la respuesta de creación de un consumidor implica su disponibilidad, y cuando "
                 "un consumidor se crea después de su productor, como ocurre con el módulo de "
                 "distribución, es el publicador el que retiene la emisión hasta que exista un "
                 "suscriptor.")
    d.comentario(i, "Todo consumidor se suscribe antes",
                 "La oración generalizaba a todos los canales la garantía del canal de detecciones "
                 "(control se crea antes que medios). En el canal de alertas el consumidor, la "
                 "distribución, se crea después del productor, el control, y la no pérdida la da el "
                 "publicador que espera suscriptor, como §17.4.3 ya cuenta. Es el residuo de la "
                 "corrección del orden de arranque que se aplicó en §17.4.")

    for i, u in enumerate(d.units):
        if u[0] != "tbl":
            continue
        for r, fila in enumerate(d.filas(i)):
            for c, celda in enumerate(fila):
                while "vídeo" in d.texto_celda(i, r, c):
                    d.celda(i, r, c, "vídeo", "video")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


# ====================================================================== §17.1
def pase_17_1(origen: Path, destino: Path) -> None:
    d = Documento(origen)

    i = d.unica("relaciones espaciales o temporales, Por último")
    d.reemplazar(i, "relaciones espaciales o temporales, Por último,",
                 "relaciones espaciales o temporales. Por último,")

    i = d.unica("Liu et al., 2023")
    d.reemplazar(i, "Liu et al., 2023", "Liu et al., 2024")
    d.comentario(i, "Liu et al., 2024",
                 "El listado global de referencias trae una sola entrada de Grounding DINO, Liu et al. "
                 "(2024), y §15 la cita once veces con ese año. Era la única cita con 2023.")

    i = d.unica("La evaluación temporal exige además un material propio")
    d.reemplazar(i, "exige además un material propio", "exige además un material construido para ese fin")
    d.comentario(i, "La evaluación temporal exige además",
                 "El banco temporal reúne el rodaje propio y un lote de videos públicos de obra real, "
                 "así que «material propio» no describe al conjunto; la misma oración lo dice dos "
                 "renglones después.")

    n = 0
    for i in d.buscar("Sección 17."):
        while "Sección 17." in d.texto(i):
            d.reemplazar(i, "Sección 17.", "sección 17.")
            n += 1
    d.log.append(f"«Sección» → «sección»: {n} reemplazos")

    t26 = _tabla(d, "Rango protocolar de entrenamiento")
    f = _fila(d, t26, 0, "Rango protocolar de entrenamiento")
    d.celda(t26, f, 1, "se acota a 500–2.000 imágenes", "se orienta a 500–2.000 imágenes")
    d.comentario_en_celda(t26, f, 0, "Rango protocolar de entrenamiento",
                          "§17.1 se contradice a sí misma: 17.1.6.4 llama al rango «orientativo» y esta "
                          "celda dice «se acota». §17.4.7 declara el exceso (2.946) como desviación "
                          "de un «rango orientativo». Alinear la celda con la prosa es lo mínimo; si "
                          "preferís que el rango sea una cota dura, se rechaza esto y §17.4.7 tiene "
                          "que decir «rango que acota el protocolo». En ningún caso se acomoda el "
                          "protocolo al resultado: la desviación sigue declarada.")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    for k in ORIGEN:
        p.add_argument(f"--origen-{k.replace('.', '-')}", type=Path, default=ORIGEN[k])
        p.add_argument(f"--destino-{k.replace('.', '-')}", type=Path, default=DESTINO[k])
    p.add_argument("--solo", choices=list(ORIGEN), help="correr un solo documento")
    a = p.parse_args()
    pases = {"17.4": pase_17_4, "17.5": pase_17_5, "17.3": pase_17_3, "17.1": pase_17_1}
    for k, fn in pases.items():
        if a.solo and a.solo != k:
            continue
        print(f"\n=== §{k} ===")
        fn(getattr(a, f"origen_{k.replace('.', '_')}"), getattr(a, f"destino_{k.replace('.', '_')}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
