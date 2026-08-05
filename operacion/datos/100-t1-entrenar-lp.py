"""T1 (E-04): linear probing de YOLOE-26s sobre el dominio EPP.

El tier 1 de la escalera pre-registrada (contingencia/20 §6): entrena SOLO la
proyección de embeddings de la cabeza — `YOLOEPETrainer.get_model` congela todo el
modelo y deja entrenable únicamente la última conv de cada rama cv3/one2one_cv3,
tras fusionar los text embeddings iniciales de los names del data.yaml. La
capacidad open-vocabulary del resto del modelo no se toca (retención por
construcción, criterio T1 del doc 20 §6).

Gotcha documentado (doc 20 §4.1): los checkpoints preentrenados son de
segmentación; para detección se inicializa desde el YAML de la misma escala y se
cargan los pesos seg encima.

**Gotcha del host (medido, 2026-08-05): los defaults de ultralytics tiran WSL
abajo.** `nproc` = 16 acá, así que ultralytics elige `workers=8`; el VM de WSL2
está en el default de 7,4 GiB (50% de los 15,25 GiB del host) y `/dev/shm` se
lleva 3,7 GiB de ese total. Ocho DataLoader workers a 640px + su pool de memoria
compartida (2,9 GiB de shmem-rss medidos) + el tooling de la sesión (~1,3 GiB)
agotan el VM -> `global_oom` -> el OOM killer siega `init.scope`, que en WSL es
donde vive el init de la distro, y la distro entera se cae (no solo el
entrenamiento). Pasó dos veces: 05:12:22 y 05:20:37.
De ahí los defaults conservadores de acá (`workers=2`, `batch=8`) y la
recomendación de correrlo acotado por cgroup, que convierte una explosión en un
proceso muerto con error claro en vez de una caída de WSL:

    systemd-run --user --scope -p MemoryMax=4G -p MemorySwapMax=2G \
        <venv>/bin/python 100-t1-entrenar-lp.py --data <data.yaml> --smoke

Uso: 100-t1-entrenar-lp.py --data <data.yaml> [--epochs 10] [--batch 8] [--smoke]
"""
import argparse
import shutil
import sys
from pathlib import Path

MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
WEIGHTS = MP / "models/yoloe/original/yoloe-26s-seg.pt"
DEST = MP / "models/yoloe/finetuned"
SEED = 100  # fijo: doc 100


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--epochs", type=int, default=10)   # doc 20 §4.1: ~10 épocas LP
    # batch/workers bajos a propósito: ver "Gotcha del host" en el docstring.
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--imgsz", type=int, default=640)   # catálogo yoloe-26s
    ap.add_argument("--smoke", action="store_true",
                    help="1 época sobre 5%% de los datos: valida el loop entero")
    ap.add_argument("--project", default="/tmp/eovrt-t1-lp/runs")
    a = ap.parse_args()

    from ultralytics import YOLOE
    from ultralytics.models.yolo.yoloe import YOLOEPETrainer

    model = YOLOE("yoloe-26s.yaml").load(str(WEIGHTS))

    kwargs = dict(
        data=a.data,
        trainer=YOLOEPETrainer,
        epochs=1 if a.smoke else a.epochs,
        fraction=0.05 if a.smoke else 1.0,
        batch=a.batch,
        workers=a.workers,
        imgsz=a.imgsz,
        seed=SEED,
        deterministic=True,
        project=a.project,
        name="smoke" if a.smoke else "t1_yoloe26s_lp",
        exist_ok=True,
        plots=False,
        val=True,
    )
    results = model.train(**kwargs)

    run_dir = Path(results.save_dir)
    best = run_dir / "weights" / "best.pt"
    if a.smoke:
        print(f"\nSMOKE OK — loop completo validado ({run_dir})")
        return 0

    if not best.exists():
        print(f"FALLO: no existe {best}")
        return 1
    DEST.mkdir(parents=True, exist_ok=True)
    dst = DEST / "yoloe-26s-lp-t1.pt"
    shutil.copy2(best, dst)
    print(f"\nT1 ENTRENADO — pesos en {dst}")
    print(f"run dir (métricas de entrenamiento): {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
