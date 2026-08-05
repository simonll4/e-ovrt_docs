"""T1 (E-04): prepara el árbol de entrenamiento para el linear probing de YOLOE.

Por qué existe este script (dos trampas que morderían en silencio):

1. **Ultralytics deriva labels reemplazando `/images/` -> `/labels/` en la ruta de
   la imagen.** Las image_lists de canonical_v2 apuntan al RAW, y el raw de los
   exports de Roboflow trae SUS labels originales (10 clases) en esa posición:
   entrenar directo con las listas usaría las clases equivocadas sin ningún error.
   Solución: árbol de symlinks images/ + labels/ apuntando a (raw, canonical_v2).

2. **Leakage con bench_v3 que el protocolo del doc 20 no pudo prever:** el rol
   TRAIN (train_v2, 5.540) incluye TODO chv, y chv es estrato de bench_v3 desde el
   07-23. Entrenar con train_v2 tal cual y evaluar en bench_v3 sería circular justo
   en el estrato estrella de `vest`. Enmienda declarada: el entrenamiento usa SOLO
   css train (2.603) + ppe_siabar train (1.120) = 3.723 imgs; chv y shel5k quedan
   vírgenes como eval. Monitor de entrenamiento: ppe_siabar val (326) — ppe_siabar
   NO es estrato de bench_v3, así que no toca al eval.

Guards: ids de clase <= 3 en todos los labels, stems únicos entre datasets,
conteos exactos contra las image_lists.

Los `names` del data.yaml son los STRINGS DE PROMPT del set congelado
cr01_cr02_bench_v2 (`bare head` con espacio): YOLOEPETrainer deriva los text
embeddings iniciales de estos nombres (`get_text_pe`), y el baseline zero-shot
usa los mismos strings — sin eso el contraste no sería de variable única.

Uso: 100-t1-preparar-datos.py [--out DIR]
"""
import argparse
import sys
from pathlib import Path

DS = Path("/home/simonll4/projects/e-ovrt_datasets")
V2 = DS / "datasets/processed/yolo/canonical_v2"

# (dataset, split) -> destino del árbol
PLAN = [
    ("construction_site_safety", "train", "train"),
    ("ppe_siabar", "train", "train"),
    ("ppe_siabar", "val", "val"),
]

NAMES = {0: "person", 1: "helmet", 2: "vest", 3: "bare head"}


def main():
    ap = argparse.ArgumentParser()
    # Ruta estable y descartable a propósito: el árbol es 100% symlinks y se
    # regenera con este script en segundos. Lo durable (métricas) se copia a
    # docs/operacion/datos/.
    ap.add_argument("--out", default="/tmp/eovrt-t1-lp/data")
    a = ap.parse_args()
    out = Path(a.out)

    stems_globales: dict[str, str] = {}
    resumen = {}
    for ds, split, dest in PLAN:
        img_list = (V2 / ds / "image_lists" / f"{split}.txt").read_text().splitlines()
        img_list = [l.strip() for l in img_list if l.strip()]
        lbl_dir = V2 / ds / "labels" / split
        (out / "images" / dest).mkdir(parents=True, exist_ok=True)
        (out / "labels" / dest).mkdir(parents=True, exist_ok=True)

        n = 0
        for img_path in img_list:
            img = Path(img_path)
            stem = img.stem
            lbl = lbl_dir / f"{stem}.txt"
            if not lbl.exists():
                print(f"GUARD: falta label {lbl}")
                return 1
            if not img.exists():
                print(f"GUARD: falta imagen {img}")
                return 1
            # stems únicos ENTRE datasets (colisión = un label pisa a otro)
            if stem in stems_globales and stems_globales[stem] != ds:
                print(f"GUARD: stem repetido entre datasets: {stem} "
                      f"({stems_globales[stem]} vs {ds})")
                return 1
            stems_globales[stem] = ds
            # ids de clase dentro del esquema canonical_v2
            for line in lbl.read_text().splitlines():
                if line.strip() and int(line.split()[0]) > 3:
                    print(f"GUARD: id de clase fuera de canonical_v2 en {lbl}: {line}")
                    return 1
            dst_i = out / "images" / dest / img.name
            dst_l = out / "labels" / dest / f"{stem}.txt"
            if not dst_i.exists():
                dst_i.symlink_to(img)
            if not dst_l.exists():
                dst_l.symlink_to(lbl)
            n += 1
        resumen[f"{ds}/{split}->{dest}"] = n

    esperado = {"construction_site_safety/train->train": 2603,
                "ppe_siabar/train->train": 1120,
                "ppe_siabar/val->val": 326}
    for k, v in esperado.items():
        if resumen.get(k) != v:
            print(f"GUARD: conteo {k} = {resumen.get(k)}, esperaba {v}")
            return 1

    yaml_path = out / "data.yaml"
    names_block = "\n".join(f"  {k}: {v}" for k, v in NAMES.items())
    yaml_path.write_text(
        f"path: {out}\ntrain: images/train\nval: images/val\nnc: 4\nnames:\n{names_block}\n")

    print(f"OK — árbol en {out}")
    for k, v in resumen.items():
        print(f"  {k}: {v}")
    print(f"  data.yaml -> {yaml_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
