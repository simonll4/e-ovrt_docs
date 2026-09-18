#!/usr/bin/env python3
"""§17.1 v1.16 → v1.17: tres precisiones hacia atrás, como SUGERENCIAS y COMENTARIOS.

La Etapa 2 quedó cerrada el 2026-09-03 y su texto no se reabre por estilo. Lo que este pase
corrige son tres reglas que §17.1 escribe y que la ejecución no cumplió tal como están
formuladas: no es prosa, es coherencia entre el protocolo y lo que §17.4 hizo y §17.5 reporta.
El usuario firmó las tres el 2026-09-07.

  X-1  **Retirada el 2026-09-07 por decisión del usuario.** La regla de fuente única de §17.1.6.3
       no se toca: era deliberada y precisarla después de ver que la ejecución no la cumplió sería
       ajustar el protocolo a los resultados. La desviación se declara en §17.4.7, que es donde el
       informe ya declara la del rango de tamaño del conjunto de ajuste.
  X-7  La Tabla 26 declara que el banco «no interviene en calibración». La medición de estado por
       persona calibró umbrales de decisión sobre una mitad del material y midió sobre la otra.
       La fila admite esa calibración, que no modifica el modelo, con la condición de que las
       mitades se predeclaren y sean disjuntas.
  X-8  La estrategia de datos cubre cuatro fuentes de imágenes y dos benchmarks de seguimiento,
       y no fija el banco temporal propio, que es el material del resultado principal. Se agrega
       como decisión, sin cifras, para no romper el no-anacronismo de la sección.
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
SRC = ARCHIVO / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.16 (base del pase 5; se recupera rechazando las sugerencias de la v1.17).docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.17 (sugerencias sin aceptar).docx"

BANCO_TEMPORAL = (
    "La evaluación temporal exige además un material propio, porque ninguna de las fuentes "
    "retenidas aporta secuencias con episodios anotados de las condiciones del núcleo. Ese banco "
    "se construye con dos bloques de procedencia y control experimental distintos, un rodaje "
    "guionado registrado con el hardware de captura del prototipo y un lote de obra real no "
    "guionada obtenido de fuentes públicas, que aporta tiempo en cumplimiento y permite medir "
    "especificidad. Cada clip conserva su procedencia y su grado de control como atributo, y la "
    "referencia de episodios se congela antes de reportar."
)


def main() -> int:
    d = Documento(SRC)

    # ---------------------------------------------------------------- X-1: NO se aplica
    # Decisión del usuario (2026-09-07): la regla de fuente única **no se toca**. Era deliberada
    # —el propio texto declara que es más restrictiva que la separación de imágenes— y precisarla
    # después de ver que la ejecución no la cumplió sería ajustar el protocolo a los resultados,
    # en contra de la pre-registración que sostiene el resto del trabajo. La desviación se declara
    # donde el informe ya declara la otra, en §17.4.7, con su causa y sus controles.

    # ---------------------------------------------------------------- X-7
    d.celda_agregar(119, 7, 1, (
        " La calibración de umbrales de decisión, que no modifica el modelo, se admite sobre una "
        "mitad predeclarada del banco, disjunta de aquella sobre la que se informan las métricas."))

    # ---------------------------------------------------------------- X-8
    d.parrafo_nuevo(113, BANCO_TEMPORAL, muestra=113)

    # ---------------------------------------------------------------- comentarios
    d.comentario(119, "La calibración de umbrales de decisión",
                 "§17.5.3 calibra umbrales sobre una mitad del banco de imágenes y mide sobre la "
                 "otra. Sin esta salvedad, la fila prohíbe esa calibración. La condición que la "
                 "hace admisible es que las mitades se fijen antes de calibrar y sean disjuntas.")
    d.comentario_en_nuevo(113, 0,
                          "El banco temporal es el material del resultado principal de §17.5 y la "
                          "estrategia de datos no lo fijaba como decisión: sólo aparecía como "
                          "«material controlado del EBE» al final de la escalera de ampliación. "
                          "Va sin cifras, para no adelantar resultados en esta sección.")

    st = d.guardar(DST)
    print("\n".join(d.log))
    print("\n", st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
