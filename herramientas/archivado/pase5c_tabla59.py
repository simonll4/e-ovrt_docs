#!/usr/bin/env python3
"""Pase 5c — baja de la fila «Pruebas automatizadas» de la Tabla 59 (§17.4.7).

    §17.4 v1.10 → v1.11

El usuario planteó el 2026-09-07 que esa fila no aportaba valor como estaba desarrollada, y pidió
decidir entre ajustarla o borrarla. Se borra, por cuatro razones verificadas:

  1. La oración que presenta la Tabla 59 enumera lo que la tabla reúne —corrección de contratos,
     cierre de corridas, paridad entre caminos, determinismo y funcionamiento de la integración— y
     las pruebas automatizadas NO están en esa lista. La misma oración ya declara que la
     repetibilidad se apoya en pruebas automatizadas, de modo que la fila repetía el marco del
     párrafo anterior y lo único que agregaba era el número.
  2. Las otras seis filas nombran una propiedad del sistema y qué muestra la evidencia. Ésta
     nombraba el INSTRUMENTO con el que se establecieron esas seis, que es el marco de la tabla y
     no una séptima fila entre pares.
  3. El conteo no resiste el detalle. Las «cinco suites» de `operacion/97` §1 son plano de medios
     641, plano de control 312, datasets 283 y la consola contada DOS VECES (backend 586 y frontend
     381). Faltan el módulo de distribución —la propia celda lo admitía— y las suites del
     repositorio de experimentación (88) y de ajuste fino (46). Y 381 de esas pruebas son de
     componentes de interfaz, que no verifican ninguna de las seis propiedades de la tabla.
  4. Ya envejeció, y su fuente lo dice. `operacion/97` lleva una nota de cabecera que remite a los
     conteos de `operacion/130`, y R-12 de ese relevamiento registra la cita como deuda. Medido hoy:
     medios 670 (era 641), datasets 431 (283), consola backend 668 (586), control 312 (312).

En reemplazo NO va otra cifra. La nota de la tabla recibe una cláusula estructural, que no envejece:
cada módulo mantiene su propio conjunto de pruebas automatizadas. El comentario ofrece borrarla si
el usuario prefiere la baja a secas.

INCREMENTAL: parte del `.docx` VIGENTE. Si el usuario baja una versión más nueva de Google Docs,
correr con `--origen` apuntando a ella.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE (2026-09-07).
# El `--origen` por default apunta a `desarrollando/archivado/`, así que correrlo tal cual reproduce
# la v1.11 y PISA lo que el usuario haya hecho después en Google Docs. El motor deja respaldo y avisa.

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ORIGEN = BASE / (
    "archivado/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.10 (entrega del pase 5b; "
    "base del pase 5c).docx")
DESTINO = BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.11 (sugerencias sin aceptar).docx"

POR_QUE_LA_BAJA = (
    "Baja propuesta el 07-09, a pedido tuyo. Cuatro razones. (1) La oración que presenta la tabla "
    "enumera lo que ésta reúne —contratos, cierre de corridas, paridad entre caminos, determinismo "
    "e integración— y las pruebas no están en esa lista; y esa misma oración ya dice que la "
    "repetibilidad se apoya en pruebas automatizadas, así que la fila repetía el marco y lo único "
    "que agregaba era el número. (2) Las otras seis filas nombran una propiedad del sistema; ésta "
    "nombraba el instrumento con el que se establecieron esas seis. (3) El conteo no resiste el "
    "detalle: las «cinco suites» eran plano de medios 641, plano de control 312, datasets 283 y la "
    "consola contada dos veces, backend 586 y frontend 381, sin el módulo de distribución —la "
    "propia celda lo admitía— ni las suites del repositorio de experimentación (88) y de ajuste "
    "fino (46); y esas 381 son pruebas de componentes de interfaz, que no verifican ninguna de las "
    "seis propiedades de arriba. (4) Envejeció, y la fuente lo dice: hoy medios da 670, datasets "
    "431 y el backend de la consola 668. Si preferís conservar la fila, se rechaza esta baja y "
    "queda como estaba."
)

CLAUSULA = (
    " Cada módulo mantiene su propio conjunto de pruebas automatizadas, con el que estas "
    "propiedades se vuelven a verificar."
)

POR_QUE_LA_CLAUSULA = (
    "Reemplaza a la fila borrada con la afirmación que no envejece, sin número: lo que sostiene la "
    "tabla es que la verificación se puede repetir, no cuántas pruebas hay. Si preferís la baja a "
    "secas, se borra esta oración y la nota queda como estaba."
)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--origen", type=Path, default=ORIGEN)
    p.add_argument("--destino", type=Path, default=DESTINO)
    a = p.parse_args()

    d = Documento(a.origen)

    tabla = d.unica("Pruebas automatizadas", kind="tbl")
    filas = d.filas(tabla)
    fila = next(k for k, f in enumerate(filas) if f[0].strip() == "Pruebas automatizadas")
    if fila != len(filas) - 1:
        raise SystemExit(f"la fila esperada era la última y es la {fila} de {len(filas)}")

    # El comentario va ANTES de la baja: `_partir` busca sobre `w:t`, y al borrar la fila el
    # contenido pasa a `w:delText`. Las marcas de comentario no son runs con texto, así que
    # sobreviven a `_del` y quedan ancladas sobre la fila tachada.
    d.comentario_en_celda(tabla, fila, 0, "Pruebas automatizadas", POR_QUE_LA_BAJA)
    d.borrar_fila(tabla, fila)

    nota = d.unica("La tabla acredita funcionamiento técnico y reproducibilidad")
    d.reemplazar(nota, "reproducibilidad.", "reproducibilidad." + CLAUSULA)
    d.comentario(nota, "La tabla acredita funcionamiento técnico", POR_QUE_LA_CLAUSULA)

    st = d.guardar(a.destino)
    print("\n".join(d.log))
    print(" ", st)
    print("  la Tabla 59 pasa de 7 filas de datos a 6")
    return 0


if __name__ == "__main__":
    sys.exit(main())
