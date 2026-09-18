#!/usr/bin/env python3
"""Verifica la integridad OPC de un `.docx` producido por un pase.

Existe por dos defectos reales del 2026-09-07: un pase generó `word/comments.xml` en memoria
pero no lo escribió en el zip, y otro insertó imágenes sin declarar el `Default` de la
extensión `png` en `[Content_Types].xml`. Word abre esos archivos como dañados y la extracción
a markdown no lo nota, porque lee sólo `word/document.xml`.

Chequea:
  · toda parte XML parsea;
  · cada `r:embed` / `r:id` usado en el documento está declarado en las relaciones;
  · cada destino de relación existe como parte del paquete;
  · cada extensión presente tiene `Default` y cada parte especial su `Override`;
  · las anclas de comentario del documento coinciden con los comentarios declarados;
  · los `w15:commentEx` cubren a los comentarios.

Uso:
    python3 herramientas/verificar_paquete.py ARCHIVO.docx [ARCHIVO2.docx ...]
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ESPECIALES = {
    "word/comments.xml": "wordprocessingml.comments+xml",
    "word/commentsExtended.xml": "wordprocessingml.commentsExtended+xml",
    "word/document.xml": "wordprocessingml.document.main+xml",
}


def verificar(ruta: Path) -> list[str]:
    fallas: list[str] = []
    with zipfile.ZipFile(ruta) as z:
        nombres = set(z.namelist())
        for n in sorted(nombres):
            if n.endswith(".xml") or n.endswith(".rels"):
                try:
                    ET.fromstring(z.read(n))
                except ET.ParseError as e:
                    fallas.append(f"{n} no parsea: {e}")
        doc = z.read("word/document.xml").decode("utf8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf8")
        ct = z.read("[Content_Types].xml").decode("utf8")

        mapa = {m.group(1): m.group(2)
                for m in re.finditer(r'Id="([^"]+)"[^>]*Target="([^"]+)"', rels)}
        for rid, destino in mapa.items():
            if destino.startswith("..") or destino.startswith("http"):
                continue
            if f"word/{destino}" not in nombres:
                fallas.append(f"relación {rid} apunta a word/{destino}, que no está en el paquete")
        usados = set(re.findall(r'r:embed="([^"]+)"', doc)) | set(re.findall(r'r:id="([^"]+)"', doc))
        for rid in sorted(usados - set(mapa)):
            fallas.append(f"el documento usa {rid}, que no está declarado en las relaciones")

        extensiones = {n.rsplit(".", 1)[-1].lower() for n in nombres if "." in n.rsplit("/", 1)[-1]}
        for ext in sorted(extensiones - {"rels"}):
            if f'Extension="{ext}"' not in ct and not any(
                    f'PartName="/{n}"' in ct for n in nombres if n.endswith("." + ext)):
                fallas.append(f'falta el Default o el Override del tipo de contenido para ".{ext}"')
        for parte, marca in ESPECIALES.items():
            if parte in nombres and marca not in ct:
                fallas.append(f"{parte} está en el paquete sin su Override en [Content_Types].xml")

        # el patrón es tolerante a la reescritura de ElementTree (atributos y cierre normalizados)
        anclas = set(re.findall(r'<w:commentRangeStart[^>]*w:id="(\d+)"', doc))
        refs = set(re.findall(r'<w:commentReference[^>]*w:id="(\d+)"', doc))
        if "word/comments.xml" in nombres:
            declarados = set(re.findall(r'<w:comment [^>]*w:id="(\d+)"',
                                        z.read("word/comments.xml").decode("utf8")))
        else:
            declarados = set()
        if anclas - declarados:
            fallas.append(f"anclas sin comentario declarado: {sorted(anclas - declarados)}")
        if declarados - anclas:
            fallas.append(f"comentarios sin ancla en el documento: {sorted(declarados - anclas)}")
        if anclas != refs:
            fallas.append(f"anclas sin referencia de comentario: {sorted(anclas ^ refs)}")
        if "word/commentsExtended.xml" in nombres:
            ex = z.read("word/commentsExtended.xml").decode("utf8")
            n_ex = len(re.findall(r"<w15:commentEx", ex))
            if n_ex < len(declarados):
                fallas.append(f"commentsExtended cubre {n_ex} de {len(declarados)} comentarios")
    return fallas


def main(argv: list[str]) -> int:
    problemas = 0
    for arg in argv:
        ruta = Path(arg)
        fallas = verificar(ruta)
        print(f"== {ruta.name}")
        if fallas:
            problemas += len(fallas)
            for f in fallas:
                print(f"  ✗ {f}")
        else:
            print("  ✓ paquete íntegro")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
