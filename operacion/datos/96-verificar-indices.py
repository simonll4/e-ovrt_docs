"""Guard de los índices de resultados: ¿cada enlace resuelve y cada cifra tiene artefacto?

Los índices de `results/` son el insumo directo del capítulo de resultados. Un enlace
roto o una cifra que no está en ningún artefacto es exactamente el modo de falla que
la auditoría del informe (`informe/95-auditoria-y-plan-de-cierre.md` §2.1 — ojo, la
serie `informe/9x` es un namespace DISTINTO de `operacion/9x`) ya encontró una vez:
"el número estrella del TFG no tenía respaldo en el repo". Este script lo verifica
mecánicamente.

Chequea:
1. Todos los enlaces relativos de los .md de results/ apuntan a algo que existe.
2. Las cifras clave citadas en los índices coinciden con los metrics.json en disco.
3. Los docs de procedencia referenciados existen en docs/operacion/.

Uso: 96-verificar-indices.py
"""
import json
import re
import sys
from pathlib import Path

RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results")
DOCS = Path("/home/simonll4/projects/docs")

# (archivo del índice, cifra citada, ruta del metrics.json, camino de campos)
#
# COBERTURA: desde 2026-08-09 esta lista cubre las 16 campañas con artefacto
# (14 de clip_bench + 2 de bench_nivel_a). El chequeo §2.1 falla si aparece una campaña
# nueva sin fila acá, que es como este script se quedó atrás la primera vez.
F1M = ["positives", "f1_micro"]


def _na(estrato, cond):
    """Camino del F1 del brazo E-IND en el metrics.json de Nivel A (otra forma)."""
    return ["strata", estrato, "conditions", cond, "arms", "eind", "metrics", "f1"]


CIFRAS = [
    # --- clip_bench: las 6 de combinación ---
    ("clip_bench/index.md", 0.789, "t1_gdinotiny560_v2short_scene", F1M),
    ("clip_bench/index.md", 0.704, "t2_gdinobase560_v2short_scene", F1M),
    ("clip_bench/index.md", 0.160, "d1_gdinotiny560_edirpair_scene", F1M),
    ("clip_bench/index.md", 0.296, "h1_gdinotiny560_hybor_scene", F1M),
    ("clip_bench/index.md", 0.930, "g1_gdinotiny560_v2short_subject", F1M),
    ("clip_bench/index.md", 0.377, "b1_gdinobase560_barehead_scene", F1M),
    # --- clip_bench: las 6 de densidad ---
    ("clip_bench/index.md", 0.794, "r1_gdinotiny560_v2short_scene_s7", F1M),
    ("clip_bench/index.md", 0.866, "r2_gdinotiny560_v2short_subject_s7", F1M),
    ("clip_bench/index.md", 0.738, "r3_gdinotiny560_v2short_scene_s15", F1M),
    ("clip_bench/index.md", 0.875, "r4_gdinotiny560_v2short_subject_s15", F1M),
    ("clip_bench/index.md", 0.646, "r5_gdinotiny560_v2short_scene_s26", F1M),
    ("clip_bench/index.md", 0.742, "r6_gdinotiny560_v2short_subject_s26", F1M),
    # --- clip_bench: las 2 del estrato B (post revisión ciega del GT, doc 113 §B) ---
    ("clip_bench/index.md", 0.333, "i1_gdinotiny560_v2short_scene_internet", F1M),
    ("clip_bench/index.md", 0.190, "i2_gdinotiny560_v2short_subject_internet", F1M),
    # --- bench_nivel_a: E-IND en los 3 cortes + el Nivel A sobre video ---
    ("bench_nivel_a/index.md", 0.546, "d1_gdinotiny560_edir_vs_eind", _na("shel5k", "CR-01")),
    ("bench_nivel_a/index.md", 0.408, "d1_gdinotiny560_edir_vs_eind", _na("bench_obra", "CR-01")),
    ("bench_nivel_a/index.md", 0.479, "d1_gdinotiny560_edir_vs_eind", _na("bench_obra", "CR-02")),
    ("bench_nivel_a/index.md", 0.031, "na1_gdinotiny560_v2short_video", ["agregado", "CR-01", "f1"]),
    ("bench_nivel_a/index.md", 0.018, "na1_gdinotiny560_v2short_video", ["agregado", "CR-02", "f1"]),
]

# cifras del doc 96 §4.1 que el índice raíz y el de realtime citan
BOOTSTRAP = {
    "G1 − T1 (la de referencia del doc 89)": 0.141,
    "R2 − R1 (sujeto vs escena, ambas 4,29 fps)": 0.072,
    "R4 − R3 (sujeto vs escena, ambas 2 fps)": 0.137,
}


def enlaces() -> list[tuple[Path, str, bool]]:
    out = []
    for md in sorted(RES.rglob("*.md")):
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", md.read_text()):
            dest = m.group(1)
            if dest.startswith(("http://", "https://", "#")):
                continue
            target = (md.parent / dest.split("#")[0]).resolve()
            out.append((md.relative_to(RES), dest, target.exists()))
    return out


def main():
    fallos = 0

    print("## 1. Enlaces relativos en results/\n")
    for origen, dest, ok in enlaces():
        if not ok:
            print(f"  ROTO  {origen} -> {dest}")
            fallos += 1
    print(f"  {sum(1 for _, _, ok in enlaces() if ok)} enlaces ok, "
          f"{sum(1 for _, _, ok in enlaces() if not ok)} rotos")

    print("\n## 2. Cifras citadas vs metrics.json en disco\n")
    for idx, citado, camp, campos in CIFRAS:
        p = RES / Path(idx).parent / camp / "metrics.json"
        if not p.exists():
            print(f"  FALTA  {camp}/metrics.json")
            fallos += 1
            continue
        v = json.loads(p.read_text())
        for c in campos:
            v = v[c]
        ok = abs(round(v, 3) - citado) < 0.0005
        print(f"  {'ok  ' if ok else 'MAL '} {camp[:38]:38} citado {citado:.3f} "
              f"| disco {v:.6f}")
        if not ok:
            fallos += 1

    print("\n## 2.1 Cobertura: ¿toda campaña con artefacto tiene cifra verificada?\n")
    # Sin esto el script envejece en silencio: se agrega una campaña, nadie extiende la
    # lista, y "todo verde" pasa a significar "verde sobre lo que miraba el año pasado".
    cubiertas = {camp for _, _, camp, _ in CIFRAS}
    en_disco = {
        d.name
        for fam in ("clip_bench", "bench_nivel_a")
        for d in (RES / fam).iterdir()
        if d.is_dir() and (d / "metrics.json").exists()
    }
    sin_cubrir = sorted(en_disco - cubiertas)
    huerfanas = sorted(cubiertas - en_disco)
    print(f"  {len(en_disco)} campañas con metrics.json en disco, "
          f"{len(cubiertas & en_disco)} cubiertas por CIFRAS")
    for c in sin_cubrir:
        print(f"  SIN CIFRA  {c}  -> agregar una fila a CIFRAS")
    for c in huerfanas:
        print(f"  HUERFANA   {c}  -> CIFRAS la cita pero no existe en disco")
    fallos += len(sin_cubrir) + len(huerfanas)
    if not sin_cubrir and not huerfanas:
        print("  ok   cobertura completa")

    print("\n## 3. Deltas del bootstrap citados vs 96-critica-verificacion.json\n")
    boot_p = DOCS / "operacion/datos/96-critica-verificacion.json"
    if boot_p.exists():
        boot = json.loads(boot_p.read_text())["bootstrap"]
        for nombre, citado in BOOTSTRAP.items():
            if nombre not in boot:
                print(f"  FALTA  {nombre}")
                fallos += 1
                continue
            # el IC debe excluir el cero, que es lo que el índice afirma
            obs, (lo, hi) = boot[nombre]["obs"], boot[nombre]["ic95"]
            ok = abs(round(obs, 3) - citado) < 0.0005 and lo > 0
            print(f"  {'ok  ' if ok else 'MAL '} {nombre[:44]:44} "
                  f"citado {citado:+.3f} | obs {obs:+.3f} IC[{lo:+.3f},{hi:+.3f}]")
            if not ok:
                fallos += 1
    else:
        print(f"  FALTA {boot_p}")
        fallos += 1

    print("\n## 4. Docs de procedencia referenciados\n")
    refs = set()
    for md in RES.rglob("*.md"):
        for m in re.finditer(r"docs?/operacion/(\d+)", md.read_text()):
            refs.add(int(m.group(1)))
        for m in re.finditer(r"\bdocs? (\d+)\b|\bdoc (\d+)\b", md.read_text()):
            n = m.group(1) or m.group(2)
            if n:
                refs.add(int(n))
    # Un "doc N" puede vivir en operacion/ o en nucleo/ (dos series distintas):
    # p. ej. "doc 10 E-07" es `nucleo/10-registro-alcance-y-exclusiones.md`.
    faltantes = []
    for n in sorted(refs):
        en_op = list((DOCS / "operacion").glob(f"{n}-*.md"))
        en_nucleo = list((DOCS / "nucleo").glob(f"{n:02d}-*.md"))
        if not en_op and not en_nucleo:
            faltantes.append(n)
    print(f"  {len(refs)} docs referenciados; sin archivo en operacion/ ni nucleo/: "
          f"{faltantes if faltantes else 'ninguno'}")
    fallos += len(faltantes)

    print(f"\n{'✅ Todo verificado' if not fallos else f'⚠️  {fallos} problemas'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
