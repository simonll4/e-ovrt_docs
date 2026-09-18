#!/usr/bin/env python3
"""Pase 5e — cierre de la bajada del 2026-09-08 (defectos del round-trip y marcador de procedencia).

    §17.4 v1.13 → v1.14 (sugerencias sin aceptar)   ·   §17.1 v1.19 → v1.20 (sugerencias sin aceptar)

El usuario aceptó en Google Docs las sugerencias de los pases 5, 5b, 5c y 5d y bajó las cinco
secciones el 09-08: §15/16 v1.3 · §17.1 v1.19 · §17.3 v1.11 · §17.4 v1.13 · §17.5 v1.9. La vista
aceptada de cada entrega comparada con su bajada muestra que **aceptó todo**; lo que difiere son
ediciones suyas (abreviar «Impacto» en la Tabla 35, borrar dos notas de §17.1, negrita en tres
rótulos «Nota», la celda «Densidad» fusionada en la Tabla 64, un punto por un punto y coma) y
**tres defectos que introdujo el viaje por Google Docs**. Este pase corrige sólo esos defectos y
resuelve el marcador de procedencia con el dato que el usuario dejó en un comentario.

§17.4  · Los tres bloques de código que el pase 5 insertó como sugerencia perdieron su ÚLTIMA
         línea al aceptarse en Google Docs —la que sigue al último salto de línea blando (`w:br`)—:
         la llave de cierre del ejemplo `media.detection.v1`, la del ejemplo `control.alert.v1` y
         `model_name: str | None = None` del DTO `Detection`. Los bloques que no eran sugerencia
         conservaron su última línea, así que el defecto es del ciclo sugerencia→aceptar. **Se
         restituyen EN LIMPIO** (no como sugerencia): reponer texto que el usuario ya aceptó no es
         una propuesta editorial, y una sugerencia cuya última línea sigue a un `w:br` corre el
         riesgo de perderse otra vez por el mismo camino. Cada bloque lleva un comentario que lo dice.
       · El marcador `[[PENDIENTE]]` de 17.4.6 (dirección de origen y fecha de acceso del lote de
         obra real) se reemplaza, como sugerencia, por la oración que cita la lista de reproducción
         pública que el usuario indicó en su comentario del 09-08 sobre ese marcador. La ficha por
         clip (C1: `video_url: TODO` en los 18 `clip.yaml`) sigue abierta y el comentario lo dice.
§17.1  · Al borrar la nota de la Tabla 35 que llevaba el salto de sección (apaisado → vertical),
         Google Docs dejó un párrafo vacío con estilo Heading 3 delante de 17.1.11 —un título
         fantasma que entra al índice— y el título quedó en cursiva, con el «1» inicial en un run
         aparte. El párrafo vacío conserva el `sectPr` (no se puede borrar) y vuelve a Normal con
         `pPrChange`; el título se reescribe con el formato de sus hermanos. Ambas cosas, sugerencia.

§15/16 NO se toca: el colega lo sigue revisando en Google Docs (tres comentarios nuevos del 09-07 y
uno reabierto) y regenerar el `.docx` pisaría lo que haga después de la bajada. El «puede puede» de
§15.2.4 y la sugerencia sin resolver del pase 5 se le informan al usuario para que los cierre allá.
§17.3 v1.11 y §17.5 v1.9 no necesitan nada.

INCREMENTAL: parte de las bajadas del 09-08, que quedan en `desarrollando/archivado/` como base.
Para una bajada nueva de Google Docs, `--origen-*`.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE. Los `--origen-*` por default apuntan a
# `desarrollando/archivado/`; correrlo tal cual reproduce las dos salidas y PISA lo que el usuario
# haya hecho después en Google Docs (el motor deja respaldo si el destino difiere).

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import RUN_RE, T_RE, Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ARCH = BASE / "archivado"
FECHA = "2026-09-08T04:00:00Z"
ORIGEN = {
    "17.4": ARCH / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.13 (bajada del usuario 2026-09-08; base del pase 5e).docx",
    "17.1": ARCH / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.19 (bajada del usuario 2026-09-08; base del pase 5e).docx",
}
DESTINO = {
    "17.4": BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.14 (sugerencias sin aceptar).docx",
    "17.1": BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.20 (sugerencias sin aceptar).docx",
}

PLAYLIST = "https://www.youtube.com/playlist?list=PLVG3-xIaXtKzAC9JJnZJUY4aBCg0BNPKV"


# ------------------------------------------------------------------ ayudas propias de este pase
def _rpr_del_primer_run(xml: str) -> str:
    """El `w:rPr` del primer run con texto del párrafo (tipografía del bloque de código)."""
    for m in RUN_RE.finditer(xml):
        if T_RE.search(m.group(0)):
            r = re.search(r"<w:rPr>.*?</w:rPr>", m.group(0), re.S)
            return r.group(0) if r else "<w:rPr/>"
    return "<w:rPr/>"


def restituir_ultima_linea(d: Documento, i: int, linea: str) -> None:
    """Repone EN LIMPIO la última línea de un bloque de código (salto blando + texto).

    No es una sugerencia: repone texto que el usuario ya aceptó y que Google Docs descartó al
    aceptar la inserción. Se inserta antes de la marca de párrafo, con el `rPr` del bloque.
    """
    xml = d.units[i][1]
    rpr = _rpr_del_primer_run(xml)
    run = (f'<w:r>{rpr}<w:br w:type="textWrapping"/>'
           f'<w:t xml:space="preserve">{linea.replace("&", "&amp;").replace("<", "&lt;")}</w:t></w:r>')
    corte = xml.rindex("</w:p>")
    d.units[i][1] = xml[:corte] + run + xml[corte:]
    d.log.append(f"u{i}: última línea restituida EN LIMPIO {linea.strip()[:50]!r}")


def estilo_normal(d: Documento, i: int) -> None:
    """Quita el estilo de encabezado de un párrafo, dejando `pPrChange` para revisarlo.

    Inverso de `Documento.estilo_titulo`. El `sectPr` y el `rPr` del párrafo no entran en la
    copia anterior que guarda el `pPrChange` (el esquema no los admite ahí) y se conservan en
    el `pPr` vigente.
    """
    p = d.units[i][1]
    m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
    if not m:
        raise ValueError("el párrafo no tiene pPr")
    interior = m.group(1)
    estilo = re.search(r'<w:pStyle w:val="([^"]+)"/>', interior)
    if not estilo or not estilo.group(1).startswith("Heading"):
        raise ValueError("el párrafo no tiene estilo de encabezado")
    anterior = re.sub(r"<w:sectPr>.*?</w:sectPr>", "", interior, flags=re.S)
    anterior = re.sub(r"<w:rPr>.*?</w:rPr>|<w:rPr/>", "", anterior, flags=re.S)
    cambio = (f'<w:pPrChange w:id="{d._nid()}" w:author="{d.autor}" '
              f'w:date="{d.fecha}"><w:pPr>{anterior}</w:pPr></w:pPrChange>')
    nuevo_interior = interior.replace(estilo.group(0), "", 1)
    d.units[i][1] = p.replace(m.group(0), f"<w:pPr>{nuevo_interior}{cambio}</w:pPr>", 1)
    d.log.append(f"u{i}: estilo {estilo.group(1)} → Normal (pPrChange)")


def comentario_parrafo(d: Documento, i: int, texto: str) -> int:
    """Comentario anclado al párrafo ENTERO, sin partir runs.

    `Documento.comentario` parte los runs con `_partir`, que supone un `w:t` por run; un bloque de
    código es UN run con muchos `w:t` separados por `w:br`, y partirlo lo desordena (comprobado en
    la primera corrida de este pase: el texto del bloque se triplicaba). Acá las marcas van justo
    después del `w:pPr` y antes de la marca de párrafo, sin tocar los runs.
    """
    cid = d._cid
    d._cid += 1
    xml = d.units[i][1]
    m = re.search(r"</w:pPr>", xml)
    ini = m.end() if m else xml.index(">") + 1
    corte = xml.rindex("</w:p>")
    marca_fin = (f'<w:commentRangeEnd w:id="{cid}"/>'
                 f'<w:r><w:rPr><w:rtl w:val="0"/></w:rPr><w:commentReference w:id="{cid}"/></w:r>')
    d.units[i][1] = (xml[:ini] + f'<w:commentRangeStart w:id="{cid}"/>' + xml[ini:corte]
                     + marca_fin + xml[corte:])
    d.comentarios.append((cid, texto))
    d.log.append(f"u{i}: comentario {cid} sobre el párrafo entero")
    return cid


def _q(d: Documento, frag: str) -> str:
    """Google Docs exporta las comillas rectas como `&quot;` y el motor no las desescapa:
    devuelve la variante del fragmento que existe en el documento."""
    if d.buscar(frag):
        return frag
    alt = frag.replace('"', "&quot;")
    if d.buscar(alt):
        return alt
    raise LookupError(f"no aparece ni con comillas ni con &quot;: {frag[:60]!r}")


def _ultima_linea_visible(xml: str) -> str:
    sin_del = re.sub(r"<w:del\b[^>]*>.*?</w:del>", "", xml, flags=re.S)
    partes = re.split(r"<w:br[^>]*/>", sin_del)
    return Documento.texto_de(partes[-1]).strip()


# ====================================================================== §17.4
def pase_17_4(origen: Path, destino: Path) -> None:
    d = Documento(origen, fecha=FECHA)

    # --- los tres bloques de código insertados por el pase 5 perdieron su última línea -------
    bloques = [
        ('"event_type": "detection_event"', "}", "media.detection.v1"),
        ("class Detection(BaseModel):", "    model_name: str | None = None", "el DTO Detection"),
        ('"event_type": "alert_event"', "}", "control.alert.v1"),
    ]
    for frag, linea, nombre in bloques:
        i = d.unica(_q(d, frag))
        assert _ultima_linea_visible(d.units[i][1]) != linea.strip(), f"u{i}: ya tiene la línea"
        # ⚠ nunca `d.comentario` sobre un bloque de código: parte el run y lo desordena.
        comentario_parrafo(d, i,
                     f"Reparación del pase 5e, aplicada en limpio: al aceptar en Google Docs la "
                     f"sugerencia que insertó este bloque ({nombre}), se perdió su última línea "
                     f"—«{linea.strip()}», la que sigue al último salto de línea—. Los tres bloques "
                     f"insertados por el pase 5 sufrieron lo mismo; los que no eran sugerencia, no. "
                     f"Se repone el texto que ya estaba aceptado; no hay nada que decidir.")
        restituir_ultima_linea(d, i, linea)
        assert _ultima_linea_visible(d.units[i][1]) == linea.strip()

    # --- 17.4.6 · marcador de procedencia del lote de obra real -----------------------------
    marcador = ("[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real · "
                "depende de completar la ficha de procedencia primaria antes del cierre final del informe]]")
    i = d.unica("[[PENDIENTE: dirección de origen")
    d.reemplazar(i, marcador,
                 "Los videos maestros del lote se obtuvieron de una lista de reproducción pública de "
                 f"YouTube compilada por el equipo ({PLAYLIST}, consultada el 8 de septiembre de 2026) "
                 "y no se redistribuyen.")
    d.agregar_al_final(i, " La dirección de origen y la fecha de acceso de cada video se consignan en "
                          "el anexo de licencias y procedencia de la sección 19.")
    d.comentario(i, "Los videos maestros del lote",
                 "Resuelve el único marcador [[PENDIENTE]] de las cinco secciones con el dato de tu "
                 "comentario del 09-08 (lista pública). Va en dos sugerencias para que se puedan "
                 "aceptar por separado: la primera oración se sostiene sola; la segunda promete la ficha "
                 "por video en la sección 19, y eso depende de cerrar C1 (los 18 clip.yaml siguen con "
                 "`video_url: TODO`). Si C1 no se cierra antes de la versión final, rechazá la segunda "
                 "oración y la primera alcanza. La lista se cita como origen del lote; la licencia de "
                 "cada video (estándar de YouTube o CC) es lo que la ficha tiene que decir.")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


# ====================================================================== §17.1
def pase_17_1(origen: Path, destino: Path) -> None:
    d = Documento(origen, fecha=FECHA)

    titulo = "17.1.11. Conclusiones parciales de la consolidación metodológica"
    i = d.unica(titulo)
    assert "Heading3" in d.units[i][1]
    j = i - 1
    vacio = d.units[j][1]
    assert d.units[j][0] == "p" and Documento.texto_de(vacio).strip() == "", "el vecino no está vacío"
    assert 'w:val="Heading3"' in vacio and "<w:sectPr>" in vacio, "el vecino no es el título fantasma"

    estilo_normal(d, j)
    d.reemplazar(i, titulo, titulo)   # mismo texto, un solo run, sin cursiva ni color
    d.comentario(i, titulo,
                 "Reparación del pase 5e. Al borrar en Google Docs la nota «La mitigación forma parte "
                 "del diseño metodológico…» (que llevaba el salto de sección apaisado→vertical), quedó "
                 "un párrafo vacío con estilo Título 3 delante de este título —un título fantasma que "
                 "entra al índice— y el título pasó a cursiva con el «1» inicial en un tramo aparte. "
                 "Se devuelve el párrafo vacío a Normal (conserva el salto de sección, que no se puede "
                 "borrar) y se reescribe el título con el formato de sus hermanos 17.1.1–17.1.10.")

    st = d.guardar(destino)
    print("\n".join(d.log)); print(" ", st)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in ORIGEN:
        p.add_argument(f"--origen-{k.replace('.', '-')}", type=Path, default=ORIGEN[k])
        p.add_argument(f"--destino-{k.replace('.', '-')}", type=Path, default=DESTINO[k])
    p.add_argument("--solo", choices=list(ORIGEN), help="correr un solo documento")
    a = p.parse_args()
    pases = {"17.4": pase_17_4, "17.1": pase_17_1}
    for k, fn in pases.items():
        if a.solo and a.solo != k:
            continue
        print(f"\n=== §{k} ===")
        fn(getattr(a, f"origen_{k.replace('.', '_')}"), getattr(a, f"destino_{k.replace('.', '_')}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
