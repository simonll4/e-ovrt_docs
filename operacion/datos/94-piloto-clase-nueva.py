"""Mini-piloto de clase nueva (doc 62 §7, argumento A1 de nucleo/09).

Mide lo que nucleo/09 exige medir y que no estaba medido en ninguna parte:
*"condicion nueva: 0 entrenamientos, ~20 lineas de configuracion, minutos"*.

Tres corridas con `prompts/clase_nueva_v1.yaml` (el ARTEFACTO cuyo costo se mide):

  A) bench_obra val+test (196 raw -> scoring restringido a las 147 curadas), caption =
     catalogo desplegado + machinery + vehicle. Estas dos clases tienen GT HUMANO en
     el raw (99 + 76 cajas) que canonical_v2 nunca uso -> **AP@0.5 real de clases
     jamas configuradas**, zero-shot, sobre el bench congelado.
  B) MOCS valid (151 imgs), caption = person + excavator + dump truck + tower crane.
     MOCS (Roboflow) solo anota Worker -> `person` vs Worker da un **ancla
     cuantitativa cross-dataset** (507 cajas GT) y las clases de maquina dan
     evidencia cualitativa (previews + tasas de deteccion).

Uso: python3 94-piloto-clase-nueva.py
"""
import json, sys, time, urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
OUT = Path(__file__).parent / "94-piloto-clase-nueva"

sys.path.insert(0, str(DS / "datasets/scripts"))
from bench.evaluate_bench import evaluate_class, load_detections  # noqa: E402
from bench.person_gt_cr02 import CSS_CLASSES, resolve_label_paths, yolo_line_to_xyxy  # noqa: E402

# Transcripcion literal de prompts/clase_nueva_v1.yaml (el runner no reformula).
CLASSES = {
    "person": ["person"], "helmet": ["helmet"], "vest": ["vest"],
    "machinery": ["machinery"], "vehicle": ["vehicle"],
    "excavator": ["excavator"], "dump_truck": ["dump truck"],
    "tower_crane": ["tower crane"],
}

RUNS = [
    {"name": "clase_nueva_bench_obra_val",
     "path": DS / "datasets/raw/construction_site_safety/valid/images",
     "active": ["person", "helmet", "vest", "machinery", "vehicle"], "previews": False},
    {"name": "clase_nueva_bench_obra_test",
     "path": DS / "datasets/raw/construction_site_safety/test/images",
     "active": ["person", "helmet", "vest", "machinery", "vehicle"], "previews": False},
    {"name": "clase_nueva_mocs_valid",
     "path": DS / "datasets/raw/MOCS/valid",
     "active": ["person", "excavator", "dump_truck", "tower_crane"], "previews": True},
]


def _post(path, body):
    req = urllib.request.Request(MEDIA + path, method="POST",
                                data=json.dumps(body).encode(),
                                headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())


def _get(path):
    return json.loads(urllib.request.urlopen(MEDIA + path, timeout=60).read())


def run_one(spec):
    body = {
        "ingest": {"plugin": "image_folder", "config": {"path": str(spec["path"])}},
        "prompts": {"set_inline": {"id": "clase_nueva_v1", "classes": [
            {"id": c, "phrasings": {"default": CLASSES[c]}} for c in spec["active"]]},
            "active_ids": spec["active"]},
        "run": {"name": spec["name"], "save_previews": spec["previews"]},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(4)
        s = _get(f"/api/runs/{run_id}")
        if (s.get("status") or "").lower() in ("completed", "finished", "succeeded",
                                               "failed", "error", "stopped"):
            return run_id, s


def gt_bench_obra_nuevas():
    """COCO sintetico con machinery/vehicle desde el raw, restringido a las 147 curadas."""
    curated = [json.loads((DS / "datasets/processed/coco/bench/curated" / f).read_text())
               for f in ("construction_site_safety_bench_obra_val.json",
                         "construction_site_safety_bench_obra_test.json")]
    labels = resolve_label_paths(curated, DS / "datasets/raw/construction_site_safety")
    images_by_filename, gt_by_image_id = {}, {}
    cat_by_id = {1: "machinery", 2: "vehicle"}
    idx = {"machinery": CSS_CLASSES.index("machinery"), "vehicle": CSS_CLASSES.index("vehicle")}
    next_id = 1
    for coco in curated:
        for img in coco["images"]:
            base = Path(img["file_name"]).name
            if base in images_by_filename:
                continue
            iid = next_id; next_id += 1
            images_by_filename[base] = {"id": iid}
            anns = []
            lab = labels.get(base)
            if lab and lab.exists():
                for line in lab.read_text().splitlines():
                    if not line.strip():
                        continue
                    cid, xyxy = yolo_line_to_xyxy(line, img["width"], img["height"])
                    for cname, raw_idx in idx.items():
                        if cid == raw_idx:
                            anns.append({"category_id": 1 if cname == "machinery" else 2,
                                         "bbox": [xyxy[0], xyxy[1],
                                                  xyxy[2] - xyxy[0], xyxy[3] - xyxy[1]]})
            gt_by_image_id[iid] = anns
    return images_by_filename, gt_by_image_id, cat_by_id


def gt_mocs_person():
    """MOCS valid: Worker renombrado a person (ancla cuantitativa cross-dataset)."""
    coco = json.loads((DS / "datasets/raw/MOCS/valid/_annotations.coco.json").read_text())
    images_by_filename, gt_by_image_id = {}, {}
    for img in coco["images"]:
        images_by_filename[Path(img["file_name"]).name] = {"id": img["id"]}
        gt_by_image_id[img["id"]] = []
    worker_ids = {c["id"] for c in coco["categories"] if c["name"].lower() == "worker"}
    for ann in coco["annotations"]:
        if ann["category_id"] in worker_ids:
            gt_by_image_id.setdefault(ann["image_id"], []).append(
                {"category_id": 99, "bbox": ann["bbox"]})
    return images_by_filename, gt_by_image_id, {99: "person"}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    resultados = {"runs": {}, "scores": {}}
    t0 = time.time()

    for spec in RUNS:
        print(f"[{spec['name']}] ...", flush=True)
        run_id, s = run_one(spec)
        d = s.get("summary") or {}
        resultados["runs"][spec["name"]] = {
            "run_id": run_id, "units": d.get("units_processed"),
            "detections": d.get("total_detections"),
            "by_label": d.get("detections_by_label"),
        }
        print(f"   {d.get('units_processed')} imgs, por clase: {d.get('detections_by_label')}",
              flush=True)

    # --- Scoring A: machinery/vehicle con GT real sobre las 147 curadas
    dets = load_detections([
        MP / "runs" / resultados["runs"]["clase_nueva_bench_obra_val"]["run_id"] / "detections.jsonl",
        MP / "runs" / resultados["runs"]["clase_nueva_bench_obra_test"]["run_id"] / "detections.jsonl",
    ])
    imgs, gt, cats = gt_bench_obra_nuevas()
    for cname in ("machinery", "vehicle"):
        r = evaluate_class(cname, dets, imgs, gt, cats, iou_threshold=0.5)
        resultados["scores"][f"bench_obra/{cname}"] = r
        print(f"   AP@0.5 {cname}: {r['AP50']} (n_gt={r['n_gt']}, n_det={r['n_det']})")

    # --- Scoring B: person vs Worker en MOCS (ancla cross-dataset)
    dets_m = load_detections([
        MP / "runs" / resultados["runs"]["clase_nueva_mocs_valid"]["run_id"] / "detections.jsonl"])
    imgs_m, gt_m, cats_m = gt_mocs_person()
    r = evaluate_class("person", dets_m, imgs_m, gt_m, cats_m, iou_threshold=0.5)
    resultados["scores"]["mocs/person_vs_worker"] = r
    print(f"   AP@0.5 person vs Worker (MOCS): {r['AP50']} (n_gt={r['n_gt']}, n_det={r['n_det']})")

    # --- Maquinas en MOCS: tasas de deteccion (sin GT) por umbral
    stats = {}
    for cname in ("excavator", "dump_truck", "tower_crane"):
        por_img = {f: [d for d in ds if d.get("prompt_id") == cname]
                   for f, ds in dets_m.items()}
        stats[cname] = {
            "imgs_con_deteccion@0.30": sum(1 for v in por_img.values() if any(d["confidence"] >= .30 for d in v)),
            "imgs_con_deteccion@0.50": sum(1 for v in por_img.values() if any(d["confidence"] >= .50 for d in v)),
            "total_detecciones": sum(len(v) for v in por_img.values()),
        }
    resultados["scores"]["mocs/maquinas_sin_gt"] = {"imgs_total": len(dets_m), **stats}
    print(f"   maquinas MOCS (151 imgs): { {k: v['imgs_con_deteccion@0.50'] for k, v in stats.items()} } imgs con det>=0.5")

    resultados["wall_clock_s"] = round(time.time() - t0, 1)
    (OUT / "resultados.json").write_text(json.dumps(resultados, indent=2, ensure_ascii=False))
    print(f"\n{resultados['wall_clock_s']}s de pared -> {OUT/'resultados.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
