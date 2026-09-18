#!/usr/bin/env python3
"""Repara los enlaces relativos que un archivado deja colgando, y verifica que no queden rotos.

Mover un archivo a `archivado/` rompe tres cosas a la vez: los enlaces que lo apuntaban, los que
él mismo tenía hacia sus vecinos, y los que apuntaban a un vecino que se movió con él. Hacerlo a
mano se olvida siempre alguno.

Para cada enlace roto busca el archivo por su nombre en el árbol. Si aparece **exactamente una
vez**, reescribe la ruta relativa; si aparece varias o ninguna, lo informa y no toca nada.

Uso:
    python3 herramientas/reparar_enlaces.py            # informa y repara
    python3 herramientas/reparar_enlaces.py --check    # sólo informa, sin escribir
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

RAICES = ("informe", "herramientas")
ENLACE = re.compile(r'\[([^\]]*)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')


def main(argv: list[str]) -> int:
    solo_check = "--check" in argv
    raiz = Path(".").resolve()
    indice: dict[str, list[Path]] = {}
    for base in RAICES:
        for p in (raiz / base).rglob("*"):
            if p.is_file():
                indice.setdefault(p.name, []).append(p)

    reparados = irreparables = total = 0
    for base in RAICES:
        for md in (raiz / base).rglob("*.md"):
            texto = md.read_text(encoding="utf-8", errors="ignore")
            nuevo = texto
            for m in ENLACE.finditer(texto):
                destino = m.group(2)
                if re.match(r"^[a-z]+://", destino) or destino.startswith("#"):
                    continue
                total += 1
                ruta, ancla = (destino.split("#", 1) + [""])[:2]
                if (md.parent / ruta).exists():
                    continue
                candidatos = indice.get(Path(ruta).name, [])
                if len(candidatos) != 1:
                    irreparables += 1
                    print(f"  ✗ {md.relative_to(raiz)} -> {destino} "
                          f"({len(candidatos)} candidatos)")
                    continue
                correcta = os.path.relpath(candidatos[0], md.parent)
                if ancla:
                    correcta += "#" + ancla
                nuevo = nuevo.replace(f"]({destino})", f"]({correcta})")
                reparados += 1
                print(f"  ✓ {md.relative_to(raiz)}: {destino} → {correcta}")
            if nuevo != texto and not solo_check:
                md.write_text(nuevo, encoding="utf-8")

    print(f"\nenlaces revisados: {total} · reparados: {reparados} · sin resolver: {irreparables}")
    return 1 if irreparables else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
