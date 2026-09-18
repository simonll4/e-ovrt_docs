#!/usr/bin/env python3
"""§17.3 v1.8 → v1.9: retoques de la Etapa 3, como SUGERENCIAS y COMENTARIOS.

La sección quedó cerrada el 2026-09-04 y la edición del usuario del 09-06 la mejoró: glosas en
español de los cinco estados, identificadores en itálica y notas de figura absorbidas en el
párrafo previo. Este pase toca sólo lo que esa edición dejó abierto.

  E3-1  «artefactos sin atributos» reemplazó a «artefactos inatribuibles» y cambió el sentido:
        lo que la regla evita es que un artefacto no pueda atribuirse a una configuración
        declarada, no que carezca de atributos.
  E3-2  «La frontera de esa elección fija es explícita» perdió el relativo: la frontera es la que
        esa elección fija, y tal como quedó se lee «una elección fija».
  E3-3  Tres notas desaparecieron con el pase de absorción y ninguna tenía figura que absorberla:
        eran guardarraíles de interpretación. Vuelven como oración final del párrafo que
        introduce cada tabla, que es el estilo que la edición del 09-06 adoptó. Si el borrado fue
        deliberado, rechazar la sugerencia las quita de nuevo.
  X-12  Las notas de la Tabla 41 y el cierre de la Tabla 52 prometen que §17.4 documenta la
        materialización «de cada ítem». §17.4 lo hace en conjunto y no ítem por ítem, así que la
        promesa se ajusta a lo que la sección siguiente entrega.
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
SRC = ARCHIVO / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.8 (base del pase 5; se recupera rechazando las sugerencias de la v1.9).docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.9 (sugerencias sin aceptar).docx"


def main() -> int:
    d = Documento(SRC)

    # ---------------------------------------------------------------- E3-1 y E3-2
    d.reemplazar(41, "y no produzca artefactos sin atributos",
                 "y no produzca artefactos que no puedan atribuirse a una configuración declarada")
    d.reemplazar(58, "La frontera de esa elección fija es explícita.",
                 "La frontera que esa elección fija es explícita.")

    # ---------------------------------------------------------------- E3-3
    # Verificado el 2026-09-07: de las tres notas borradas, dos ya están dichas en otro lugar
    # de la sección —la vista «no prescribe una distribución obligatoria» cubre la primera, y la
    # tabla de capacidades cubre la tercera con «las métricas de seguimiento no condicionan la
    # evaluación del núcleo»—. Sólo se restituye la que no tiene equivalente en ningún documento.
    d.agregar_al_final(226, (
        " Las métricas se atribuyen al rol y al despliegue efectivamente declarados en la "
        "corrida, y no se extrapolan entre unidades desplegables distintas."))
    # ---------------------------------------------------------------- X-12
    d.reemplazar(25, "Su materialización y verificación se documentan en la sección 17.4.",
                 "Su materialización y su verificación se documentan en conjunto en la sección 17.4.")
    d.reemplazar(238, "El estado ejecutado de cada ítem corresponde a la sección 17.4.",
                 "El estado alcanzado por el conjunto de los incrementos corresponde a la sección 17.4.")

    # ---------------------------------------------------------------- comentarios
    d.comentario(41, "que no puedan atribuirse a una configuración declarada",
                 "La edición del 06-09 cambió «artefactos inatribuibles» por «artefactos sin "
                 "atributos», que dice otra cosa: lo que la regla evita es que una corrida "
                 "produzca artefactos que no se puedan atribuir a la configuración que los generó.")
    d.comentario(226, "no se extrapolan entre unidades desplegables distintas",
                 "En la edición del 06-09 desaparecieron tres notas de tabla. El patrón indica que "
                 "el borrado fue deliberado: quedaron las nueve notas que describen su tabla y se "
                 "fueron las tres que advertían cómo no leerla. De esas tres, dos ya están dichas "
                 "en otro lugar de la sección, así que no vuelven. Esta es la única sin equivalente "
                 "en ningún documento, y sin ella las métricas de la tabla parecen extrapolables "
                 "entre unidades desplegables. Si aun así preferís no tenerla, rechazá la sugerencia.")
    d.comentario(238, "El estado alcanzado por el conjunto de los incrementos",
                 "§17.4 documenta la materialización en conjunto y no ítem por ítem. La promesa "
                 "queda ajustada a lo que la sección siguiente entrega; la nota de la Tabla 41 "
                 "recibe el mismo ajuste.")

    st = d.guardar(DST)
    print("\n".join(d.log))
    print("\n", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
