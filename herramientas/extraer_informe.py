#!/usr/bin/env python3
"""Extractor .docx → markdown para la foto de `informe/entregable/` (D-C del manual 08).

Regla D-C (manual `informe/ajustes/08-manual-de-aplicacion.md` §2, firmada 2026-08-16):
una sección cerrada en Google Docs ⇒ se re-extrae su `.md` y se anota la fecha en
`entregable/00-el-informe-hoy.md`. Este script es esa herramienta. Sin dependencias:
stdlib puro (el entorno de docs no tiene pandoc ni python-docx).

Limitaciones declaradas (las mismas del banner de la serie 96):
- Figuras no se extraen: quedan marcadas con MARCA_FIGURA.
- Ecuaciones de Word no se convierten: quedan marcadas con MARCA_ECUACION — así dejan
  de "parecer campos vacíos" (trampa NO-TOCAR del mapa `00` §7).
- Numeración automática de listas no se reconstruye: toda lista sale con viñeta `-`.
- La numeración de títulos debe estar escrita en el texto (como en el informe v1.1).

Uso típico (re-extraer §15 tras cerrarla en Google Docs):
    python3 herramientas/extraer_informe.py entregable.docx --seccion 15 \
        --titulo "96c — Texto extraído del informe v1.1: §15 Estado del Arte" \
        --out informe/entregable/96c-informe-v11-estado-del-arte.md
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"

MARCA_ECUACION = "⟦ECUACIÓN: no extraída — ver el .docx⟧"
MARCA_FIGURA = "⟦FIGURA: no extraída — ver el .docx⟧"

_HEADING_STYLE = re.compile(r"^Heading(\d)$", re.IGNORECASE)


class SeccionNoEncontrada(ValueError):
    """La sección pedida no existe como título numerado en el markdown."""


# ---------------------------------------------------------------- runs y párrafos


def _flag_activo(rpr: ET.Element | None, tag: str) -> bool:
    if rpr is None:
        return False
    el = rpr.find(W + tag)
    if el is None:
        return False
    val = el.get(W + "val")
    return val is None or val.lower() not in ("0", "false", "none")


def _recolectar_runs(el: ET.Element, salida: list[tuple[str, bool, bool]]) -> None:
    for hijo in el:
        tag = hijo.tag
        if tag == W + "r":
            rpr = hijo.find(W + "rPr")
            negrita = _flag_activo(rpr, "b")
            cursiva = _flag_activo(rpr, "i")
            partes: list[str] = []
            for sub in hijo:
                if sub.tag == W + "t":
                    partes.append(sub.text or "")
                elif sub.tag == W + "tab":
                    partes.append("\t")
                elif sub.tag == W + "br":
                    partes.append(" ")
                elif sub.tag in (W + "drawing", W + "pict", W + "object"):
                    salida.append((MARCA_FIGURA, False, False))
            if partes:
                salida.append(("".join(partes), negrita, cursiva))
        elif tag in (M + "oMath", M + "oMathPara"):
            salida.append((MARCA_ECUACION, False, False))
        elif tag in (W + "hyperlink", W + "ins", W + "smartTag"):
            _recolectar_runs(hijo, salida)


def _fusionar(runs: list[tuple[str, bool, bool]]) -> list[tuple[str, bool, bool]]:
    fusionados: list[tuple[str, bool, bool]] = []
    for texto, b, i in runs:
        if fusionados and fusionados[-1][1:] == (b, i):
            fusionados[-1] = (fusionados[-1][0] + texto, b, i)
        else:
            fusionados.append((texto, b, i))
    return fusionados


def _formatear_run(texto: str, negrita: bool, cursiva: bool) -> str:
    if not (negrita or cursiva) or not texto.strip():
        return texto
    izquierda = texto[: len(texto) - len(texto.lstrip())]
    derecha = texto[len(texto.rstrip()):]
    nucleo = texto.strip()
    marca = ("**" if negrita else "") + ("*" if cursiva else "")
    cierre = ("*" if cursiva else "") + ("**" if negrita else "")
    return f"{izquierda}{marca}{nucleo}{cierre}{derecha}"


def _texto_parrafo(p: ET.Element, con_formato: bool) -> str:
    runs: list[tuple[str, bool, bool]] = []
    _recolectar_runs(p, runs)
    if con_formato:
        return "".join(_formatear_run(*run) for run in _fusionar(runs))
    return "".join(texto for texto, _, _ in runs)


def _estilo(p: ET.Element) -> str:
    ppr = p.find(W + "pPr")
    if ppr is None:
        return ""
    pstyle = ppr.find(W + "pStyle")
    return pstyle.get(W + "val", "") if pstyle is not None else ""


def _nivel_lista(p: ET.Element) -> int | None:
    ppr = p.find(W + "pPr")
    numpr = ppr.find(W + "numPr") if ppr is not None else None
    if numpr is None:
        return None
    ilvl = numpr.find(W + "ilvl")
    try:
        return int(ilvl.get(W + "val", "0")) if ilvl is not None else 0
    except ValueError:
        return 0


def _parrafo_a_md(p: ET.Element) -> str:
    estilo = _estilo(p)
    if estilo == "Title":
        texto = _texto_parrafo(p, con_formato=False).strip()
        return f"# {texto}" if texto else ""
    coincidencia = _HEADING_STYLE.match(estilo)
    if coincidencia:
        nivel = min(int(coincidencia.group(1)) + 1, 6)
        texto = _texto_parrafo(p, con_formato=False).strip()
        return f"{'#' * nivel} {texto}" if texto else ""
    texto = _texto_parrafo(p, con_formato=True).strip()
    if not texto:
        return ""
    nivel_lista = _nivel_lista(p)
    if nivel_lista is not None:
        return f"{'  ' * nivel_lista}- {texto}"
    return texto


# ------------------------------------------------------------------------ tablas


def _celda_a_texto(tc: ET.Element) -> str:
    parrafos = [_texto_parrafo(p, con_formato=True).strip() for p in tc.iter(W + "p")]
    texto = " ".join(p for p in parrafos if p)
    return texto.replace("|", "\\|")


def _tabla_a_md(tbl: ET.Element) -> str:
    filas: list[list[str]] = []
    for tr in tbl.findall(W + "tr"):
        filas.append([_celda_a_texto(tc) for tc in tr.findall(W + "tc")])
    if not filas:
        return ""
    columnas = max(len(fila) for fila in filas)
    filas = [fila + [""] * (columnas - len(fila)) for fila in filas]
    lineas = ["| " + " | ".join(filas[0]) + " |"]
    lineas.append("| " + " | ".join(["---"] * columnas) + " |")
    lineas.extend("| " + " | ".join(fila) + " |" for fila in filas[1:])
    return "\n".join(lineas)


# ---------------------------------------------------------------- documento entero


def docx_a_markdown(ruta_docx: Path | str) -> str:
    with zipfile.ZipFile(ruta_docx) as zf:
        raiz = ET.fromstring(zf.read("word/document.xml"))
    cuerpo = raiz.find(W + "body")
    if cuerpo is None:
        return ""
    bloques: list[str] = []
    for hijo in cuerpo:
        if hijo.tag == W + "p":
            bloque = _parrafo_a_md(hijo)
        elif hijo.tag == W + "tbl":
            bloque = _tabla_a_md(hijo)
        else:
            bloque = ""
        if bloque:
            bloques.append(bloque)
    return "\n\n".join(bloques) + ("\n" if bloques else "")


def extraer_seccion(markdown: str, seccion: str) -> str:
    """Recorta desde el título numerado `seccion` hasta el próximo del mismo nivel o mayor."""
    numero = re.escape(seccion.rstrip("."))
    patron_inicio = re.compile(rf"^(#+)\s+{numero}\.\s")
    lineas = markdown.splitlines()
    inicio = nivel = None
    for indice, linea in enumerate(lineas):
        coincidencia = patron_inicio.match(linea)
        if coincidencia:
            inicio, nivel = indice, len(coincidencia.group(1))
            break
    if inicio is None:
        raise SeccionNoEncontrada(f"no hay título numerado «{seccion}.» en el documento")
    fin = len(lineas)
    patron_corte = re.compile(rf"^#{{1,{nivel}}}\s")
    for indice in range(inicio + 1, len(lineas)):
        if patron_corte.match(lineas[indice]):
            fin = indice
            break
    return "\n".join(lineas[inicio:fin]).rstrip() + "\n"


def construir_banner(titulo: str, nombre_docx: str, fecha: str | None = None) -> str:
    fecha = fecha or datetime.date.today().isoformat()
    return (
        f"# {titulo}\n"
        "\n"
        f"> **Extracción derivada ({fecha})** del `.docx`\n"
        f"> `informe/entregable/{nombre_docx}`, **solo para búsqueda y cita**\n"
        "> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca\n"
        "> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se\n"
        f"> extraen y las ecuaciones no se convierten — quedan `{MARCA_FIGURA}` y\n"
        f"> `{MARCA_ECUACION}` donde estaban. Regenerado con\n"
        "> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).\n"
        "\n"
        "---\n"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("docx", type=Path, help="ruta al .docx exportado de Google Docs")
    parser.add_argument("--seccion", help="título numerado a recortar (ej.: 15 o 17.1)")
    parser.add_argument("--titulo", help="título del archivo; agrega el banner de derivada")
    parser.add_argument("--fecha", help="fecha del banner (default: hoy)")
    parser.add_argument("--out", type=Path, help="archivo de salida (default: stdout)")
    args = parser.parse_args(argv)

    markdown = docx_a_markdown(args.docx)
    if args.seccion:
        markdown = extraer_seccion(markdown, args.seccion)
    if args.titulo:
        markdown = construir_banner(args.titulo, args.docx.name, args.fecha) + "\n" + markdown

    if args.out:
        args.out.write_text(markdown, encoding="utf-8")
        print(f"escrito: {args.out}")
    else:
        sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
