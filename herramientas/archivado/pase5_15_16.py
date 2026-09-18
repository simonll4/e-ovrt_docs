#!/usr/bin/env python3
"""§15 y §16 v1.2 → v1.3: pase 5 de la Etapa 1, como SUGERENCIAS y COMENTARIOS.

Alcance completo, firmado por el usuario el 2026-09-07: defectos mecánicos, la oración rota que
invierte las dos formulaciones, el cierre de D-E1-11 y la alineación de la definición de
Glass-to-Algorithm con la que fija el protocolo. El documento es del colega, así que todo entra
como sugerencia y los once comentarios que ya trae se conservan intactos.

Bloqueantes que cierra:
  E1-B1  «16. Marco teórico» perdió su estilo de encabezado en esta versión (en la v1.1 era
         Título 1). Sin estilo desaparece del índice automático y de la numeración de campos.
  E1-B2  §16.3.4: «…que localice la infracción completa, o solicitar evidencia positiva.Segundo,
         derivar la ausencia…». El fragmento suelto pertenece a la segunda formulación; como
         está, la primera absorbe a la segunda y contradice la oración siguiente.
  E1-B3  §16.6.1: el párrafo que deja la inscripción como «decisión pendiente del equipo» y su
         marcador. D-E1-11 los mandó borrar y el espejo de §17.1 ya se borró, de modo que hoy
         §16 promete un recaudo que §17.1 no documenta. La Disposición y sus tres ejes quedan.

Importante que cierra:
  X-2    §16.5.2 mantiene la ecuación como marco general y declara la convención adoptada: el
         origen instrumentado es el retiro de la unidad, y el tramo anterior se reporta aparte.
         Sin esa oración, §16 define la métrica de un modo y §17.1 y §17.5 la miden de otro.

Menores: la nota de la Tabla 7 sin «que», «puede puede», «servicio.QoS», «midiendocuánto» y los
dos «siendo que» mal empleados.
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
ARCHIVO = BASE / "archivado"
# el documento de partida se archivó el 2026-09-07; la ruta queda para poder repetir el pase
SRC = ARCHIVO / "E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.2 (base del pase 5; se recupera rechazando las sugerencias de la v1.3).docx"
DST = BASE / "E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.3 (sugerencias sin aceptar).docx"


def main() -> int:
    d = Documento(SRC)

    # ---------------------------------------------------------------- E1-B1
    d.estilo_titulo(163, 1)

    # ---------------------------------------------------------------- E1-B2
    d.reemplazar(214,
                 "En primer lugar, solicitar directamente al modelo que localice la infracción "
                 "completa, o solicitar evidencia positiva.Segundo, derivar la ausencia mediante "
                 "razonamiento sobre las detecciones.",
                 "La primera pide directamente al modelo que localice la infracción completa. La "
                 "segunda solicita evidencia positiva y deriva la ausencia mediante razonamiento "
                 "sobre las detecciones.")

    # ---------------------------------------------------------------- E1-B3
    d.borrar_parrafo(285)
    d.borrar_parrafo(286)

    # ---------------------------------------------------------------- X-2
    d.agregar_al_final(260, (
        " En este trabajo la instrumentación fija ese punto en el retiro de la unidad por parte "
        "del consumidor, de modo que el tramo anterior, desde la captura hasta la disponibilidad "
        "en el host, se mide y se informa por separado."))

    # ---------------------------------------------------------------- menores
    d.reemplazar(120, "definen el espacio de problemas abiertos se abordan",
                 "definen el espacio de problemas abiertos que se abordan")
    d.reemplazar(54, "el cual puede puede preservar", "el cual puede preservar")
    d.reemplazar(142, "niveles de calidad de servicio.QoS 1 requiere",
                 "niveles de calidad de servicio. QoS 1 requiere")
    d.reemplazar(274, "midiendocuánto trabajo", "midiendo cuánto trabajo")
    d.reemplazar(200,
                 "siendo que el sistema solo puede detectar lo que fue explícitamente contemplado "
                 "en el diseño",
                 "porque el sistema solo puede detectar lo que fue explícitamente contemplado en "
                 "el diseño")
    d.reemplazar(266,
                 "que la siguiente consume, siendo que, cuando el productor supera",
                 "que la siguiente consume, y cuando el productor supera")

    # ---------------------------------------------------------------- comentarios
    d.comentario(163, "16. Marco teórico",
                 "Este título perdió su estilo de encabezado en la v1.2; en la v1.1 era Título 1. "
                 "Sin estilo no entra al índice automático ni a la numeración de campos de Word, "
                 "aunque a la vista parezca un título. La sugerencia se lo devuelve.")
    d.comentario(214, "La primera pide directamente al modelo",
                 "La versión anterior decía «…que localice la infracción completa, o solicitar "
                 "evidencia positiva.Segundo, derivar la ausencia…»: el fragmento suelto pertenece "
                 "a la segunda formulación, y pegado a la primera la hacía absorber a la segunda, "
                 "en contra de la oración siguiente. Es el fundamento de las dos estrategias que "
                 "§17.1 y §17.5 comparan, así que conviene que quede exacto.")
    d.comentario(284, "Disposición 10/2015",
                 "El párrafo siguiente y su marcador se proponen para borrar, cerrando D-E1-11: "
                 "el espejo en §17.1 ya se borró, así que hoy §16 promete un recaudo que §17.1 no "
                 "documenta, y un informe final no puede entregar un pendiente abierto. La norma "
                 "no desaparece del marco, porque este párrafo describe la Disposición con sus "
                 "tres ejes. Coincide con el comentario del colega sobre ese pasaje.")
    d.comentario(260, "el retiro de la unidad por parte del consumidor",
                 "Alineación pedida por la lectura transversal. La ecuación (1) es el marco "
                 "general y se conserva, pero el protocolo mide el tramo desde el retiro de la "
                 "unidad y reporta la captura aparte. Sin esta oración, §16 define la métrica "
                 "central de latencia de un modo y §17.1 y §17.5 la miden de otro.")

    st = d.guardar(DST)
    print("\n".join(d.log))
    print("\n", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
