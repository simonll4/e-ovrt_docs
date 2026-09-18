#!/usr/bin/env python3
"""§17.4 v1.8 → v1.9: pase 5 de la Etapa 4, como SUGERENCIAS y COMENTARIOS.

Aplica la lista de trabajo de `desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md` §8
para §17.4, con la decisión del usuario del 2026-09-07 de que las figuras se inserten por XML.

Bloqueante que cierra:
  E4-B1  la Figura 4.5 quedó incrustada en medio de la última oración de 17.4.1, sin epígrafe, y
         con la imagen del 23-08 que deja al módulo de distribución fuera del orden de arranque.
         El pase la saca de la oración, le devuelve su epígrafe, convierte el párrafo que la
         describía en la nota de la figura e inserta `figuras/fig-a-vista-de-procesos.png`.

Importantes que cierra: E4-I1 (llamadas de las Tablas 57 y 59), E4-I2 (la Tabla 56 nombraba dos
contratos que el diseño no usa), E4-I3 (el despliegue integral en presente cuando nunca se
construyó), E4-I4 (la cifra de pruebas queda fechada), E4-I5 (el nivel de calidad de servicio),
X-1 (la desviación de la regla de partición, declarada acá en vez de precisar §17.1), X-3 («cuarto componente
funcional» contra §17.3.7), X-4 (el perfil operativo se nombra donde se configura), X-5 (una sola
causa para el tercer tramo de ajuste fino) y X-13 (la evidencia visual controlada tenía capacidad
declarada en la Tabla 39 y ningún destino acá).

La causa del tercer tramo se corrige contra las actas: no se cerró porque el corpus comparta
fuentes con el banco —eso es la regla de partición, que sí se cumplió— sino porque sin una línea
base sana de esa familia la diferencia no era interpretable.
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
SRC = ARCHIVO / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.8 (base del pase 5; se recupera rechazando las sugerencias de la v1.9).docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.9 (sugerencias sin aceptar).docx"

ANCHO_16CM = 5760720

EVIDENCIA_VISUAL = (
    "La gestión de evidencia visual controlada quedó implementada como opción de corrida. El "
    "plano de medios puede conservar una previsualización por unidad procesada, con un tope "
    "configurable, y un video anotado de la corrida completa. Las dos posibilidades vienen "
    "habilitadas por defecto y se declararon apagadas en todas las campañas del banco, conforme "
    "a la política de minimización de evidencia visual que fija el diseño, de modo que los "
    "artefactos evaluativos conservan identificadores, metadatos y coordenadas, y no imágenes."
)

SALVEDAD_FUENTE = (
    "El cumplimiento de esa regla tuvo un límite que conviene declarar. Una de las dos fuentes "
    "retenidas para el ajuste aporta además el estrato curado del banco de imágenes, de modo que "
    "en ese punto la partición se apartó del protocolo, que reserva para el banco a toda fuente "
    "que lo integre aunque sus particiones nominales sean disjuntas. Excluirla habría reducido el "
    "conjunto de ajuste de 2.946 a 743 imágenes. La desviación se admitió con dos controles "
    "verificados, particiones disjuntas y deduplicación perceptual contra el banco en cero, y la "
    "retención medida sobre ese estrato se lee con esa salvedad."
)


# ---------------------------------------------------------------------------- concreción técnica
# Observación del tutor técnico, registrada como R-06: los contratos del núcleo ya no son
# preliminares y deben mostrarse con su artefacto real, «una clase, un DTO o una API». El texto y
# los dos JSON están redactados y verificados desde el 2026-08-22 en el material de la Etapa 3;
# llegaron la tabla de correspondencia y las interfaces, y faltaban la clase y el contrato de
# salida. Los dos fragmentos de abajo son transcripción literal de artefactos de corrida.

EVENTO_JSON = """{
  "schema_version": "media.detection.v1",
  "event_type": "detection_event",
  "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",
  "unit_id": "frame_000229",
  "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",
               "frame_index": 229, "timestamp_ms": 7633.33,
               "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },
  "detections": [
    { "detection_id": "det_000001", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.88,
      "bbox_xyxy":      [1239.8, 149.8, 1503.2, 861.9],
      "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],
      "area_px": 187612.4, "model_name": "grounding_dino" },
    { "detection_id": "det_000002", "label": "vest",
      "prompt_id": "vest", "source_prompt": "vest", "confidence": 0.8755,
      "bbox_xyxy":      [1286.5, 235.3, 1459.3, 487.0],
      "bbox_norm_xyxy": [0.67, 0.2179, 0.76, 0.4509],
      "area_px": 43490.1, "model_name": "grounding_dino" },
    { "detection_id": "det_000003", "label": "helmet",
      "prompt_id": "helmet", "source_prompt": "helmet", "confidence": 0.456,
      "bbox_xyxy":      [1519.0, 432.5, 1648.1, 521.3],
      "bbox_norm_xyxy": [0.7911, 0.4005, 0.8584, 0.4827],
      "area_px": 11463.6, "model_name": "grounding_dino" }
  ],
  "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,
              "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 }
}"""

CLASE = """class DetectionEvent(BaseModel):
    schema_version: str = "media.detection.v1"
    event_type: str = "detection_event"
    run_id: str
    unit_id: str
    source: DetectionEventSource
    model: DetectionEventModel
    prompts: DetectionEventPrompts
    detections: list[Detection]
    timing: DetectionEventTiming

class Detection(BaseModel):
    detection_id: str | None = None
    track_id: str | None = None        # aditivo: identidad entre fotogramas
    label: str
    prompt_id: str | None = None
    source_prompt: str | None = None
    strategy: str | None = None
    condition_id: str | None = None
    confidence: float
    bbox_xyxy: list[float]             # coordenadas en la imagen original
    bbox_norm_xyxy: list[float]        # coordenadas normalizadas
    area_px: float | None = None
    model_name: str | None = None"""

ALERTA_JSON = """{
  "schema_version": "control.alert.v1",
  "event_type": "alert_event",
  "control_run_id": "bench_a_p1_c02_gdino_20260822_20260822T225536Z",
  "media_run_id":   "run_20260803_211225_dbe_grounding_dino_1e06f3",
  "alert_id": "394c9116-a38d-568d-b620-20d147c4cac9",
  "pattern_id": "CR-01", "condition_id": "CR-01",
  "subject_key": "CR-01:a_p1_c02", "source_id": "a_p1_c02",
  "severity": "high", "state": "open",
  "unit_id": "frame_000229", "frame_index": 229, "timestamp_ms": 7633.33,
  "evidence": {
    "subject": { "detection_id": "det_000001", "label": "person", "confidence": 0.88,
                 "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9] },
    "missing_class": "helmet",
    "supporting": [],
    "score": 0.88, "subjects_in_evidence": 1,
    "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 1 sujeto(s)."
  },
  "first_evidence_ms": 41990631.527, "first_evidence_unit_id": "frame_000109",
  "first_evidence_frame_index": 109,
  "alert_registered_ms": 41990642.511
}"""


def main() -> int:
    d = Documento(SRC)

    # ---------------------------------------------------------------- 17.4.1
    # X-3: §17.3.7 dice que la distribución no es un tercer plano ni un cuarto rol funcional.
    d.reemplazar(5, "El módulo de distribución de alertas es el cuarto componente funcional.",
                 "El módulo de distribución de alertas es un módulo desacoplado y no un tercer "
                 "plano de ejecución.")
    # E4-I5: el nivel de calidad de servicio ejercido es el que sostiene la confirmación.
    d.reemplazar(5, "entrega por MQTT con confirmación de calidad de servicio",
                 "entrega por MQTT en el nivel de calidad de servicio 1, con confirmación por mensaje")

    # E4-B1: la figura recupera su epígrafe y su imagen, y el párrafo que la describía pasa a nota.
    d.parrafo_nuevo(6, "", muestra=9)
    d.parrafo_nuevo(6, "**Figura 4.5**", muestra=10)
    d.parrafo_nuevo(6, "*Vista de procesos y patrones de acople de la plataforma experimental*",
                    muestra=11)
    d.figura(6, FIGS / "fig-a-vista-de-procesos.png", ANCHO_16CM, muestra=11)
    d.borrar_figura(7)
    d.reemplazar(7, "La figura 4.5 representa la materialización efectiva de los dos patrones de acople.",
                 "**Nota.** La figura representa la materialización efectiva de los dos patrones "
                 "de acople.")

    # ---------------------------------------------------------------- 17.4.2
    # R-06: el evento se muestra sobre la unidad en la que la condición se confirma, y no sobre el
    # primer cuadro de la corrida. Esa unidad trae tres detecciones e incluye un casco que NO
    # suprime la condición, porque cae fuera de la región cefálica del sujeto: es la lectura que la
    # ficha pedía conservar. El párrafo anterior se marca borrado y el nuevo entra al lado.
    d.borrar_parrafo(17)
    d.bloque_codigo(17, EVENTO_JSON, muestra=17)
    d.parrafo_nuevo(17, (
        "La misma estructura se declara en el código como modelo de datos con tipos explícitos. "
        "El campo de identidad entre fotogramas aparece acá como opcional y sin valor por defecto, "
        "que es el mecanismo con el que un dato todavía no producido puede incorporarse sin "
        "cambiar la versión del esquema ni alterar los artefactos ya escritos."), muestra=16)
    d.bloque_codigo(17, CLASE, muestra=17)

    d.celda(12, 1, 0, "RunConfig", "Manifiesto de experimento")
    d.celda(12, 1, 1, "Manifiesto de experimento y configuraciones efectivas por plano",
            "Archivo de manifiesto del experimento y configuraciones efectivas por plano")
    d.celda(12, 17, 0, "Alerta distribuida", "NotificationEnvelope y DeliveryRecord")
    d.celda(12, 17, 1, "NotificationEnvelope y DeliveryRecord",
            "Envoltorio de notificación y registro de entrega en el ledger")

    # R-06: el contrato de salida del sistema, mostrado. Transcripción literal del artefacto de
    # la corrida sobre el mismo clip que el evento anterior, de modo que los dos se leen juntos.
    d.agregar_al_final(21, (
        " El fragmento siguiente reproduce la alerta registrada sobre el mismo clip y la misma "
        "unidad que el evento anterior, y permite verificar la ventana de confirmación desde los "
        "hitos que la propia alerta transporta: la primera evidencia cae a los 3.633 ms del video "
        "y la confirmación a los 7.633, exactamente los 4.000 ms configurados para la condición."))
    d.bloque_codigo(21, ALERTA_JSON, muestra=17)

    # ---------------------------------------------------------------- 17.4.3
    d.agregar_al_final(25, " La Tabla 57 reúne sus operaciones de gobierno.")
    d.reemplazar(32, "porque debe quedar suscrito al canal", "porque debe quedar suscripto al canal")

    # ---------------------------------------------------------------- 17.4.4
    # X-4: el perfil operativo se nombra donde se declara su configuración.
    d.reemplazar(43,
                 "El perfil fijado por criterio pre-registrado para las corridas en vivo declara "
                 "umbral de caja de 0,30 y de texto de 0,25.",
                 "El perfil fijado por criterio pre-registrado para las corridas en vivo es la "
                 "variante tiny de Grounding DINO con resolución de entrada de 560 píxeles, "
                 "identificada en el catálogo como gdino-tiny-560, y declara umbral de caja de "
                 "0,30 y de texto de 0,25.")
    # E4-I3: el despliegue integral quedó definido y validado, y todavía no se construyó.
    d.reemplazar(42, "y el despliegue integral instancia un servicio por perfil del catálogo",
                 "y el despliegue integral define un servicio por perfil del catálogo")

    # ---------------------------------------------------------------- 17.4.5 y 17.4.6
    d.reemplazar(56, "Un guión segundo a segundo", "Un guion segundo a segundo")

    # ---------------------------------------------------------------- 17.4.7
    d.agregar_al_final(66, (
        " La Tabla 59 reúne esa evidencia, concentrada en corrección de contratos, cierre de "
        "corridas, paridad entre caminos, determinismo y funcionamiento de la integración."))
    d.celda(70, 7, 1, "Una verificación integral registró 2.203 pruebas aprobadas",
            "Una verificación integral de agosto de 2026 registró 2.203 pruebas aprobadas")

    # X-13: la capacidad de evidencia visual controlada no tenía destino en esta sección.
    d.parrafo_nuevo(77, EVIDENCIA_VISUAL, muestra=77)

    # X-5: la causa del tercer tramo, alineada con la que registran las actas.
    d.reemplazar(78,
                 "El tercer tramo se cerró con causa técnica, porque el único corpus disponible de "
                 "ese volumen comparte fuentes con el banco de evaluación.",
                 "El tercer tramo se cerró con causa técnica, porque la familia de modelos que le "
                 "correspondía no ofrecía una línea base sana sobre la que la diferencia fuera "
                 "interpretable, y la escalera pre-registrada impedía sustituirla por otra.")

    # X-1: la regla de partición, dicha con precisión, y la salvedad que faltaba.
    d.reemplazar(79,
                 "después de excluir íntegramente la fuente que el banco de evaluación comparte",
                 "después de excluir íntegramente la única fuente que el banco de evaluación "
                 "incorpora completa")
    d.parrafo_nuevo(79, SALVEDAD_FUENTE, muestra=79)

    # ---------------------------------------------------------------- comentarios
    d.comentario_en_nuevo(6, 1,
                          "Figura rehecha. La imagen anterior era la del 23-08, que deja al módulo "
                          "de distribución fuera del orden de arranque; esta es la producida en "
                          "informe/figuras, con el orden real control → distribución → medios. "
                          "Rechazar esta sugerencia deja el documento como estaba, con la imagen "
                          "vieja incrustada dentro de la oración.")
    d.comentario_en_nuevo(17, 1,
                          "Responde a los dos comentarios sobre los DTO y a la observación del "
                          "tutor técnico. La ficha R-06 pedía cuatro piezas: la tabla de "
                          "correspondencia, el contrato central como DTO y como clase, los dos "
                          "contratos del plano de control, y las interfaces. Estaban la tabla y "
                          "las interfaces; faltaban la clase y el contrato de salida, y el JSON "
                          "pegado no era el que la ficha especificaba. Los tres fragmentos son "
                          "transcripción literal de artefactos de corrida, verificados hoy contra "
                          "el repositorio. El texto estaba redactado desde el 22-08 en el material "
                          "de la Etapa 3 y nunca se había pegado.")
    d.comentario(12, "Manifiesto de experimento",
                 "La primera columna es «contrato del diseño» y estos dos nombres no existen en "
                 "§17.3: el diseño llama «Manifiesto de experimento» al primero, y al último lo "
                 "define como NotificationEnvelope y DeliveryRecord. Quedan alineados.")
    d.comentario(43, "gdino-tiny-560",
                 "El nombre del perfil operativo faltaba acá y aparecía por primera vez en la "
                 "Tabla 61 de §17.5. Con esto, la cifra de resultados y la configuración que la "
                 "produjo quedan atadas.")
    d.comentario(70, "Una verificación integral de agosto de 2026",
                 "El conteo es real y corresponde a la verificación del 05-08. Queda fechado para "
                 "que no envejezca en silencio: las suites siguieron creciendo después.")
    d.comentario_en_nuevo(77, 0,
                          "Cierra la única capacidad de la Tabla 39 que no tenía destino en esta "
                          "sección. Verificado sobre el código y los artefactos: la opción existe "
                          "en el esquema de configuración, viene en verdadero por defecto, y las "
                          "corridas del banco la declaran en falso, con cero imágenes en sus "
                          "directorios. Una redacción anterior decía que la capacidad había quedado "
                          "sin implementar, y era falsa.")
    d.comentario_en_nuevo(79, 0,
                          "Desviación declarada, no regla ajustada. La primera versión de este "
                          "pase precisaba la regla de §17.1.6.3 para que abarcara lo que se hizo; "
                          "el 07-09 se decidió lo contrario, porque la regla era deliberada y "
                          "cambiarla al cerrar sería acomodar el protocolo a los resultados. Se "
                          "usa el mismo patrón que el párrafo anterior emplea para la desviación "
                          "del rango de tamaño: se declara contra el protocolo, con su causa y "
                          "sus controles, y el protocolo queda como estaba.")
    d.comentario(78, "no ofrecía una línea base sana",
                 "Causa corregida contra las actas de la jornada de ajuste fino. La versión "
                 "anterior decía que el corpus compartía fuentes con el banco, que es la regla de "
                 "partición y sí se cumplió; la causa real es que sin línea base sana de esa "
                 "familia la diferencia no era interpretable.")

    st = d.guardar(DST)
    print("\n".join(d.log))
    print("\n", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
