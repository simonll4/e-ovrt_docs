#!/usr/bin/env python3
"""Pase de la Etapa 6 — §17.6 y §19 · v1.4 → v1.5 (sugerencias sin aceptar).

QUÉ AGREGA
  Las capturas de la consola de inspección, que el informe describe pero nunca muestra. Se
  incorporan como CUATRO figuras: una en el cuerpo y tres en un anexo nuevo.

  §17.6.2  una oración que llama a la figura y al anexo, y la Figura 4.7 con su pie.
  §19.7    Anexo G nuevo — «Consola de inspección: pantallas de operación y de evidencia»,
           con un párrafo de entrada y las Figuras G.1, G.2 y G.3.

POR QUÉ ACÁ Y NO EN §17.4
  §17.4 es donde la consola está descrita como componente, pero está CERRADA (v1.15) y tiene su
  propio mapa de secciones; abrirla obligaría a tocar su numeración y su serie de figuras. La
  Etapa 6 es el frente abierto, los anexos A–F no tienen ninguna figura y la serie del cuerpo se
  agota en la 4.6, así que la 4.7 no desordena nada.

LAS CAPTURAS
  Se tomaron con `webconsole/tools/capture_console.mjs` (la herramienta que ya vive en el repo)
  contra el BFF en :8090 con los tres servicios arriba, sobre el material conservado. Viewport
  1440×1000 a factor 2, tema oscuro —la consola no tiene tema claro—, página completa.
  Ninguna salió con el encabezado en «servicio caído»: el guion recarga hasta que el motor
  responde, y falla si no lo consigue.

LO QUE NO ENTRÓ, Y POR QUÉ
  · Plataforma  — sin el compose de `infra/platform` arriba, la pantalla dice «la orquestación no
    está habilitada». Mostraría una limitación del entorno de captura, no de la plataforma.
  · Conjuntos de prompts — la pantalla tiene un defecto de maquetado: la insignia de estado se
    alinea al ancho del nombre y se sale del borde de la tarjeta en cualquier resolución. Es un
    bug real de la consola, no del entorno; publicarlo en un anexo mostraría el defecto.
  · Comparar — sin corridas elegidas no muestra nada.

UNA ADVERTENCIA QUE VA EN EL PIE
  El indicador del encabezado («mock») es el motor cargado al tomar la captura, no el modelo con
  que se produjo la corrida histórica. Se aclara en la nota de la Figura G.2 para que nadie lea
  que esas detecciones salieron de un modelo simulado.

Todo es sugerencia + comentario: rechazar todas las sugerencias devuelve la v1.4 exacta.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
FIGURAS = Path(__file__).resolve().parent.parent / "informe/figuras"
ORIGEN = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.4.docx"
DESTINO = BASE / "E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.5 (sugerencias sin aceptar).docx"
FECHA = "2026-09-13T12:00:00Z"

CM = 360000  # EMU por centímetro

# Unidades del documento de origen (verificadas contra la v1.4).
U_17_6_2_FIN = 10   # último párrafo de §17.6.2 («La cadena de una alerta pudo rastrearse…»)
U_PROSA = 129       # párrafo de prosa de anexo, modelo de pPr
U_ROTULO = 130      # «Tabla E.1»: rótulo con keepNext
U_TITULO = 131      # título en cursiva de la tabla, con keepNext
# ⚠ El anexo se ancla en u156 y NO en u157 (el párrafo vacío del final). Al rechazar, un párrafo
# insertado se fusiona con el SIGUIENTE; si el bloque va después del último párrafo del cuerpo,
# el último insertado no tiene con quién fusionarse y sobrevive vacío: la compuerta pasaba a
# «719 → 720 párrafos» con el texto idéntico. Anclado en u156, el último se fusiona con u157.
U_FIN = 156         # último párrafo con contenido; u157 es el vacío de cierre


def _figura(d: Documento, i: int, rotulo: str, titulo: str, png: str, ancho_cm: float,
            nota: str) -> None:
    """Rótulo + título en cursiva + imagen + nota, en el formato APA del documento."""
    d.parrafo_nuevo(i, f"**{rotulo}**", muestra=U_ROTULO)
    d.parrafo_nuevo(i, f"*{titulo}*", muestra=U_TITULO)
    d.figura(i, FIGURAS / png, ancho_emu=int(ancho_cm * CM), muestra=U_TITULO)
    d.parrafo_nuevo(i, nota, muestra=U_PROSA)


def cuerpo_17_6_2(d: Documento) -> None:
    """La llamada a la figura y la Figura 4.7, al cierre de §17.6.2."""
    d.agregar_al_final(U_17_6_2_FIN, (
        " La Figura 4.7 muestra cómo la consola de inspección presenta ese recorrido: cada cifra "
        "reportada abre los resultados que la sostienen y, desde ellos, las corridas que los "
        "respaldan; el Anexo G registra sus demás pantallas."
    ))
    _figura(
        d, U_17_6_2_FIN,
        "Figura 4.7",
        "Recorrido de evidencia en la consola de inspección",
        "fig-4-7-consola-evidencia.png", 14.0,
        "Nota. La pantalla agrupa los resultados reportados según el recorrido del argumento del "
        "informe y muestra, para cada uno, la cifra que lo identifica y el material del que "
        "proviene. Se construye leyendo el archivo curado de resultados y no consulta a los "
        "servicios de la plataforma, de modo que sigue disponible con los tres planos apagados. "
        "Fuente: elaboración propia.",
    )
    d.comentario(
        U_17_6_2_FIN, "La Figura 4.7 muestra",
        "Capturas de la consola (1 de 2). Va una sola figura al cuerpo, y va acá porque este "
        "apartado es el que afirma que cada ejecución queda identificada y su evidencia "
        "conservada: la pantalla es esa afirmación hecha visible. Las otras tres van al Anexo G "
        "para no engrosar el cuerpo. No se tocó §17.4 —donde la consola está descrita como "
        "componente— porque está cerrada y tiene su propio mapa de secciones. La serie del "
        "cuerpo se agotaba en la 4.6, así que la 4.7 no renumera nada.",
    )


def anexo_g(d: Documento) -> None:
    """Anexo G nuevo, al final del documento."""
    d.parrafo_nuevo(
        U_FIN,
        "19.7. Anexo G - Consola de inspección: pantallas de operación y de evidencia",
        muestra=U_PROSA, estilo="Heading2",
    )
    d.parrafo_nuevo(U_FIN, (
        "La consola de inspección fue el instrumento con el que se compusieron y lanzaron las "
        "ejecuciones, se inspeccionó su traza y se recorre la evidencia conservada. Las figuras "
        "que siguen registran sus pantallas principales en el estado de cierre, tomadas sobre el "
        "material conservado. Documentan el instrumento; las comprobaciones que respaldan los "
        "resultados se delimitan en el Anexo E y el inventario de artefactos por componente, en "
        "la sección 17.4.5."
    ), muestra=U_PROSA)

    _figura(
        d, U_FIN,
        "Figura G.1",
        "Inventario de corridas agrupado por el resultado que las cita",
        "fig-g1-consola-corridas.png", 13.5,
        "Nota. Cada fila reúne las corridas que sostienen un resultado reportado, con la cifra del "
        "paso correspondiente y la clase asignada a la corrida. Una corrida citada por dos "
        "resultados aparece en los dos grupos, de modo que la suma de los grupos no equivale al "
        "total de corridas. Fuente: elaboración propia.",
    )
    _figura(
        d, U_FIN,
        "Figura G.2",
        "Detalle de una corrida: traza por cuadro e inspección de las detecciones",
        "fig-g2-consola-corrida.png", 12.0,
        "Nota. La traza recorre las unidades de la corrida y, para la seleccionada, muestra las "
        "detecciones con su confianza y el progreso de cada condición configurada. El indicador "
        "del encabezado corresponde al motor de detección cargado al tomar la captura, no al "
        "modelo con el que se produjo la corrida, que consta en su identificador y en su "
        "configuración efectiva. Fuente: elaboración propia.",
    )
    _figura(
        d, U_FIN,
        "Figura G.3",
        "Detalle de un experimento: métricas, alertas y trazabilidad",
        "fig-g3-consola-experimento.png", 13.2,
        "Nota. El reporte informa el valor medido de cada métrica y, cuando no pudo medirse, la "
        "razón, sin convertir una ausencia en un resultado. El bloque de trazabilidad enlaza la "
        "corrida de medios, la corrida de control y el manifiesto que las liga. Fuente: "
        "elaboración propia.",
    )

    d.comentario_en_nuevo(
        U_FIN, 0,
        "Capturas de la consola (2 de 2). Anexo nuevo en vez de ampliar el B: el B está amarrado "
        "por número a §17.1.4 y §17.4, y son tablas. Quedan tres pantallas de cuatro candidatas. "
        "Fuera quedaron, con motivo: Plataforma (sin el compose de infra/platform arriba dice «la "
        "orquestación no está habilitada» y mostraría una limitación del entorno de captura, no "
        "de la plataforma); Conjuntos de prompts (la insignia de estado se alinea al ancho del "
        "nombre y se sale del borde de la tarjeta en cualquier resolución: es un defecto real de "
        "maquetado de la consola, y publicarlo lo dejaría en el informe); y Comparar (sin "
        "corridas elegidas no muestra nada). Las cuatro capturas son del software corriendo sobre "
        "el material conservado, con los tres servicios arriba; ninguna salió con el encabezado "
        "en «servicio caído». La consola no tiene tema claro, así que las cuatro son oscuras: o "
        "van todas así o no va ninguna, mezclarlas se lee como descuido.",
    )


def _palabras(d: Documento) -> int:
    return sum(len(d.texto(i).split()) for i in range(len(d.units)))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--origen", type=Path, default=ORIGEN)
    ap.add_argument("--destino", type=Path, default=DESTINO)
    a = ap.parse_args()

    d = Documento(a.origen, fecha=FECHA)
    antes = _palabras(d)
    comentarios_previos = len(re.findall(r"<w:commentRangeStart", d.ensamblar()))

    cuerpo_17_6_2(d)
    anexo_g(d)

    despues = _palabras(d) + sum(len(Documento.texto_de(x).split())
                                 for xs in d.nuevos.values() for x in xs)
    ensamblado = d.ensamblar()
    comentarios_ahora = len(re.findall(r"<w:commentRangeStart", ensamblado))
    figuras = len(re.findall(r"<w:drawing", ensamblado))
    st = d.guardar(a.destino)

    print("\n".join(d.log))
    print(f"\n  cuerpo (vista aceptada): {antes} → {despues} palabras "
          f"({despues - antes:+d}, {100 * (despues - antes) / antes:+.1f} %)")
    print(f"  anclas de comentario: {comentarios_previos} → {comentarios_ahora}")
    print(f"  dibujos en el documento: {figuras}")
    print(f"  {st}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
