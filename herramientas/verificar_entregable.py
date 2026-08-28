#!/usr/bin/env python3
"""Verificador mecánico de un `.docx` entregado por el redactor externo.

Existe por un caso real (2026-08-27): una entrega de la Etapa 1 llegó con el contenido
correcto pero con **cinco encabezados numerados que habían perdido su estilo de título**
—`16.5.3`, `16.5.4`, `16.5.5`, `16.6` y `16.6.1`, contiguos—. Se ven como títulos y no lo
son: desaparecen del índice automático y de la numeración de campos de Word. El defecto
apareció al editar el documento a través de una unidad de Drive conectada, no dentro del
Project. Revisarlo a ojo no escala; este script lo detecta en un segundo.

Chequea, sobre el `.docx` y sobre su extracción a markdown:

  DUROS (hacen fallar la verificación)
  - títulos numerados sin estilo de encabezado (el defecto que motivó la herramienta);
  - huecos y desórdenes en la numeración de secciones (se ven en el índice);
  - fugas de andamiaje interno (ids `E1-`/`AJ-`/`R-`/`PODA-`, líneas `SHA-256`,
    cabeceras `> Seleccion:`, texto de instrucción del kit);
  - citas de autor-año en el cuerpo sin entrada en el listado de referencias.

  BLANDOS (se informan, no fallan)
  - entradas de referencia que el cuerpo ya no cita;
  - misma autoría citada con años distintos (posible obra citada dos veces);
  - inventario de marcadores `[[…]]` (deben viajar al entregable, no borrarse);
  - presencia de cambios controlados y comentarios.

Uso:
    python3 herramientas/verificar_entregable.py "informe/entregable/desarrollando/X.docx"
    python3 herramientas/verificar_entregable.py X.docx --seccion 15 --seccion 16
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extraer_informe import docx_a_markdown  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

TITULO_NUMERADO = re.compile(r"^(\d{1,2}(?:\.\d+)*)\.\s+\S")
ESTILOS_TITULO = ("heading", "titulo", "título", "title")

FUGAS = (
    (re.compile(r"\b(?:AJ-\d+\.\d+|R-\d{2}|PODA-\d{2})\b"), "identificador de ficha interna"),
    (re.compile(r"(?<!P-)\bE[1345]-\d{2}\b"), "identificador de pase de correcciones"),
    (re.compile(r"SHA-256"), "línea de procedencia del generador del kit"),
    (re.compile(r">\s*Seleccion:|>\s*Selección:"), "cabecera de fuente del kit"),
    (re.compile(r"clave para la plantilla|para la plantilla:"), "texto de instrucción de redacción"),
)

# Se busca sobre el texto de los párrafos del `.docx`, NO sobre la extracción a markdown
# (que legítimamente tiene `###`): detecta markdown pegado crudo dentro del documento.
MARKDOWN_CRUDO = re.compile(r"^\s*(#{1,6}\s|\|\s*-{3,}\s*\||```)")

MARCADOR = re.compile(r"\[\[([A-ZÁÉÍÓÚ]+)\s*:")
CITA = re.compile(r"([A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚáéíóúñ'\-]{2,})"
                  r"(?:\s+(?:et al\.|y\s+[A-ZÁÉÍÓÚ][\wáéíóúñ]+|&\s+[A-ZÁÉÍÓÚ][\wáéíóúñ]+))?"
                  r",?\s*\(?((?:19|20)\d{2}[a-e]?|s\.\s?f\.(?:-[a-e])?)\)?")
ENTRADA_REF = re.compile(r"^([A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚáéíóúñ'\-]{2,})(?:,|\s+&|\s+et al\.|\s+\()")

# Apellidos que aparecen en prosa por otras razones y no son citas.
RUIDO = {
    "Tabla", "Nota", "Fuente", "Figura", "Anexo", "Sección", "Seccion", "Capítulo",
    "Ley", "Decreto", "Resolución", "Disposición", "Etapa", "Bloque", "Convención",
}

INSTITUCIONALES = {
    "Argentina", "Google", "Microsoft", "NVIDIA", "Intel", "Apple", "Adobe", "Twitch",
    "Roboflow", "Ultralytics", "Luxonis", "Board", "Consortium", "Development", "Forum",
    "Alliance", "Communications", "Authority", "Research", "Laboratory", "Developers",
}


class VerificacionError(RuntimeError):
    """El `.docx` no se puede leer o no tiene la estructura esperada."""


@dataclass
class Informe:
    duros: list[str] = field(default_factory=list)
    blandos: list[str] = field(default_factory=list)
    datos: dict[str, object] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.duros


# ------------------------------------------------------------------ .docx crudo


def _estilo(p: ET.Element) -> str:
    ppr = p.find(W + "pPr")
    if ppr is None:
        return ""
    pstyle = ppr.find(W + "pStyle")
    return pstyle.get(W + "val", "") if pstyle is not None else ""


def _texto(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.iter(W + "t")).strip()


def _parrafos(ruta: Path) -> list[tuple[str, str]]:
    """Devuelve (estilo, texto) por párrafo del cuerpo del documento."""
    try:
        with zipfile.ZipFile(ruta) as zf:
            xml = zf.read("word/document.xml")
            partes = set(zf.namelist())
    except (OSError, zipfile.BadZipFile) as error:
        raise VerificacionError(f"no se pudo abrir {ruta}: {error}") from error
    cuerpo = ET.fromstring(xml).find(W + "body")
    if cuerpo is None:
        raise VerificacionError(f"{ruta} no tiene cuerpo de documento")
    _parrafos.partes = partes  # type: ignore[attr-defined]
    return [(_estilo(p), _texto(p)) for p in cuerpo.iter(W + "p")]


def es_estilo_de_titulo(estilo: str) -> bool:
    return estilo.lower().startswith(ESTILOS_TITULO)


def titulos_sin_estilo(parrafos: list[tuple[str, str]],
                       secciones: tuple[str, ...] = ()) -> list[tuple[str, str]]:
    """Párrafos que empiezan como título numerado pero no tienen estilo de título."""
    sueltos = []
    for estilo, texto in parrafos:
        m = TITULO_NUMERADO.match(texto)
        if not m or es_estilo_de_titulo(estilo):
            continue
        if secciones and not any(_pertenece(m.group(1), s) for s in secciones):
            continue
        sueltos.append((m.group(1), texto[:70]))
    return sueltos


def _pertenece(numero: str, seccion: str) -> bool:
    return numero == seccion or numero.startswith(seccion + ".")


def numeros_de_titulo(parrafos: list[tuple[str, str]],
                      secciones: tuple[str, ...] = ()) -> list[str]:
    """Todos los números de sección, con estilo o sin él, en orden de aparición."""
    numeros = []
    for _estilo_, texto in parrafos:
        m = TITULO_NUMERADO.match(texto)
        if not m:
            continue
        if secciones and not any(_pertenece(m.group(1), s) for s in secciones):
            continue
        numeros.append(m.group(1))
    return numeros


def huecos_de_numeracion(numeros: list[str], parcial: bool = False) -> list[str]:
    """Detecta saltos y desórdenes entre hermanos del mismo padre.

    Con `parcial=True` no se juzga el nivel superior: una entrega por secciones trae
    §15, §16 y §19 sin §17 ni §18, y eso no es un hueco sino su alcance.
    """
    hijos: dict[str, list[int]] = {}
    for numero in numeros:
        partes = numero.split(".")
        padre = ".".join(partes[:-1])
        try:
            hijos.setdefault(padre, []).append(int(partes[-1]))
        except ValueError:
            continue
    problemas = []
    for padre, vistos in sorted(hijos.items()):
        if parcial and not padre:
            continue
        etiqueta = f"§{padre}." if padre else "nivel superior"
        if vistos != sorted(vistos):
            problemas.append(f"{etiqueta} numera fuera de orden: {vistos}")
            continue
        faltan = [n for n in range(vistos[0], vistos[-1] + 1) if n not in vistos]
        if faltan:
            falta = ", ".join(f"{padre}.{n}" if padre else str(n) for n in faltan)
            problemas.append(f"{etiqueta} salta de {vistos[0]} a {vistos[-1]}: falta {falta}")
        # El nivel superior arranca donde arranque la entrega (§15, §16…): no es un hueco.
        if padre and vistos and vistos[0] > 1:
            problemas.append(f"{etiqueta} arranca en {vistos[0]} y no en 1")
    return problemas


def markdown_crudo(parrafos: list[tuple[str, str]]) -> list[str]:
    """Párrafos del `.docx` que traen sintaxis markdown sin convertir."""
    return [t[:70] for _e, t in parrafos if MARKDOWN_CRUDO.match(t)]


# --------------------------------------------------------------------- markdown


def fugas_de_andamiaje(markdown: str) -> list[str]:
    hallazgos = []
    for patron, descripcion in FUGAS:
        for m in patron.finditer(markdown):
            fragmento = markdown[max(0, m.start() - 45): m.end() + 45].replace("\n", " ")
            hallazgos.append(f"{descripcion}: …{fragmento.strip()}…")
    return hallazgos


def marcadores(markdown: str) -> dict[str, int]:
    conteo: dict[str, int] = {}
    for m in MARCADOR.finditer(markdown):
        conteo[m.group(1)] = conteo.get(m.group(1), 0) + 1
    return conteo


def _partir_referencias(markdown: str) -> tuple[str, str]:
    m = re.search(r"^#{0,6}\s*Referencias\s*$", markdown, re.MULTILINE | re.IGNORECASE)
    if not m:
        return markdown, ""
    return markdown[:m.start()], markdown[m.end():]


def _apellidos_citados(cuerpo: str) -> set[str]:
    return {m.group(1) for m in CITA.finditer(cuerpo) if m.group(1) not in RUIDO}


def _apellidos_en_listado(refs: str) -> set[str]:
    apellidos = set()
    for linea in refs.splitlines():
        m = ENTRADA_REF.match(linea.strip())
        if m and m.group(1) not in RUIDO:
            apellidos.add(m.group(1))
    return apellidos


def citas_sin_referencia(markdown: str) -> list[str]:
    """Autorías citadas en el cuerpo que no figuran en ninguna parte del listado.

    Se compara contra el texto completo de las referencias, no contra la primera palabra
    de cada entrada: las autorías institucionales de varias palabras ("European Data
    Protection Board", "World Wide Web Consortium") rompen cualquier heurística de
    "apellido inicial" y producían falsos positivos en masa.
    """
    cuerpo, refs = _partir_referencias(markdown)
    if not refs.strip():
        return []
    return sorted(a for a in _apellidos_citados(cuerpo) if a not in refs)


def referencias_huerfanas(markdown: str) -> list[str]:
    cuerpo, refs = _partir_referencias(markdown)
    if not refs.strip():
        return []
    return sorted(a for a in _apellidos_en_listado(refs) if a not in cuerpo)


def _es_institucional(autor: str) -> bool:
    """Organismos y normas citan legítimamente muchos años (ISO 45001 / ISO 42001…)."""
    return autor.isupper() or autor in INSTITUCIONALES


def anios_divergentes(markdown: str) -> list[str]:
    cuerpo, _ = _partir_referencias(markdown)
    por_autor: dict[str, set[str]] = {}
    for m in CITA.finditer(cuerpo):
        if m.group(1) in RUIDO or _es_institucional(m.group(1)):
            continue
        por_autor.setdefault(m.group(1), set()).add(m.group(2))
    divergentes = []
    for autor, anios in sorted(por_autor.items()):
        base = {a[:4] for a in anios if a[:2] in ("19", "20")}
        if len(base) > 1:
            divergentes.append(f"{autor}: {', '.join(sorted(anios))}")
    return divergentes


# ---------------------------------------------------------------------- informe


def verificar(ruta: Path, secciones: tuple[str, ...] = ()) -> Informe:
    informe = Informe()
    parrafos = _parrafos(ruta)
    partes = getattr(_parrafos, "partes", set())
    markdown = docx_a_markdown(ruta)

    sueltos = titulos_sin_estilo(parrafos, secciones)
    for numero, texto in sueltos:
        informe.duros.append(f"título sin estilo de encabezado (§{numero}): {texto}")

    numeros = numeros_de_titulo(parrafos, secciones)
    for problema in huecos_de_numeracion(numeros, parcial=bool(secciones)):
        informe.duros.append(f"numeración: {problema}")

    for fuga in fugas_de_andamiaje(markdown):
        informe.duros.append(f"fuga de andamiaje — {fuga}")

    for crudo in markdown_crudo(parrafos):
        informe.duros.append(f"markdown pegado sin convertir: {crudo}")

    faltantes = citas_sin_referencia(markdown)
    if faltantes:
        informe.duros.append(
            f"{len(faltantes)} autorías citadas sin entrada en Referencias: "
            + ", ".join(faltantes[:12])
        )

    huerfanas = referencias_huerfanas(markdown)
    if huerfanas:
        informe.blandos.append(
            f"{len(huerfanas)} entradas de Referencias que el cuerpo ya no cita: "
            + ", ".join(huerfanas[:12])
        )

    for divergencia in anios_divergentes(markdown):
        informe.blandos.append(f"misma autoría con años distintos — {divergencia}")

    xml = ET.tostring(ET.fromstring(zipfile.ZipFile(ruta).read("word/document.xml")))
    if b"w:ins " in xml or b"w:del " in xml:
        informe.blandos.append("el documento trae cambios controlados")
    else:
        informe.blandos.append("el documento NO trae cambios controlados")
    if any("comments" in p for p in partes):
        informe.blandos.append("el documento trae comentarios")

    informe.datos = {
        "palabras": len(markdown.split()),
        "titulos": len(numeros),
        "marcadores": marcadores(markdown),
    }
    return informe


def formatear(informe: Informe, ruta: Path) -> str:
    lineas = [f"Verificación de {ruta.name}", ""]
    d = informe.datos
    marcas = d.get("marcadores") or {}
    resumen = ", ".join(f"{k}×{v}" for k, v in sorted(marcas.items())) or "ninguno"
    lineas.append(f"  {d.get('palabras', 0):,} palabras · {d.get('titulos', 0)} títulos numerados")
    lineas.append(f"  marcadores pendientes: {resumen}")
    lineas.append("")
    if informe.duros:
        lineas.append(f"FALLA — {len(informe.duros)} problema(s) que hay que corregir:")
        lineas += [f"  ✗ {x}" for x in informe.duros]
    else:
        lineas.append("OK — ningún problema duro")
    if informe.blandos:
        lineas.append("")
        lineas.append("Para revisar (no bloquea):")
        lineas += [f"  · {x}" for x in informe.blandos]
    return "\n".join(lineas)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("docx", type=Path, help="entrega a verificar")
    parser.add_argument(
        "--seccion", action="append", default=[], metavar="N",
        help="limitar a una sección de primer nivel (repetible: --seccion 15 --seccion 16)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        informe = verificar(args.docx, tuple(args.seccion))
    except VerificacionError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(formatear(informe, args.docx))
    return 0 if informe.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
