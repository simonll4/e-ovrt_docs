"""Fase D — Fase 1 (Nivel A): inferencia de los brazos E-IND y E-DIR sobre el bench.

Pre-registro: docs/nucleo/04 §7 Fase 1. La variable unica es la ESTRATEGIA de prompts;
modelo, fuente, resolucion y umbrales de inferencia se mantienen fijos.

Brazos:
  E-IND (eind_v1)  — 3 clases canonicas en UN caption (su forma desplegada).
  E-DIR (edir_v1)  — 6 formulaciones, UNA CORRIDA POR VARIANTE (caption aislado).
                     Aislar la variante es lo que permite atribuir el resultado a la
                     formulacion y no al amontonamiento del caption; el caveat de
                     regimen asimetrico vs E-IND se declara en el campaign.yaml.

Estratos y por que cada uno:
  bench_obra (196 imgs raw -> 147 curadas)  CR-01 y CR-02. Unico estrato con GT de
                                            chaleco a nivel persona (negativos
                                            explicitos NO-Safety Vest del raw).
  shel5k     (5000 imgs)                    CR-01 solamente. No anota chaleco, por eso
                                            las variantes CR-02 no se corren aca.

Uso: python3 83-fase-d-nivel-a-runner.py [--only-arm eind|edir] [--dry-run]
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
OUT = Path(__file__).parent / "83-fase-d-nivel-a"

# Estratos: (id, carpeta de imagenes, condiciones con GT a nivel persona)
STRATA = [
    ("bench_obra_val", DS / "datasets/raw/construction_site_safety/valid/images", {"CR-01", "CR-02"}),
    ("bench_obra_test", DS / "datasets/raw/construction_site_safety/test/images", {"CR-01", "CR-02"}),
    ("shel5k", DS / "datasets/raw/shel5k/9rcv8mm682-4/Safety Helmet Wearing Dataset/Images", {"CR-01"}),
]

# --- Brazo E-IND: eind_v1 congelado (sha256 7a0126f4...), las 3 clases en un caption.
EIND = {
    "arm": "eind",
    "prompt_set_id": "eind_v1",
    "conditions": {"CR-01", "CR-02"},
    "classes": [
        {"id": "person", "phrasings": {"default": ["person"]}},
        {"id": "helmet", "phrasings": {"default": ["helmet"]}},
        {"id": "vest", "phrasings": {"default": ["vest"]}},
    ],
}

# --- Brazo E-DIR: edir_v1 congelado (sha256 a1278d0c...), una corrida por variante.
# Los dos diagnostic_template (enabled_by_default: false) NO entran: son sondas del eje
# de presencia, no candidatas a evidencia de ausencia (decision registrada en el doc 83).
EDIR_VARIANTS = [
    ("cr01_neg", "CR-01", "syntactic_negation", "person without hard hat"),
    ("cr01_spec", "CR-01", "specificity", "construction worker without safety helmet"),
    ("cr01_obs", "CR-01", "observable_state", "person with bare head on construction site"),
    ("cr02_neg", "CR-02", "syntactic_negation", "person without safety vest"),
    ("cr02_spec", "CR-02", "specificity", "construction worker without reflective vest"),
    ("cr02_obs", "CR-02", "observable_state", "person without bright colored safety clothing"),
]


def _post(path, body):
    req = urllib.request.Request(
        MEDIA + path, method="POST", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def _get(path):
    with urllib.request.urlopen(MEDIA + path, timeout=120) as r:
        return json.loads(r.read())


def wait_ready(timeout_s=600):
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        try:
            _get("/readyz")
            return True
        except (urllib.error.URLError, urllib.error.HTTPError, OSError):
            time.sleep(3)
    return False


def run_one(job):
    """Dispara una corrida y espera a que termine. Devuelve (run_id, status, summary)."""
    body = {
        "ingest": {"plugin": "image_folder", "config": {"path": str(job["path"])}},
        "prompts": {
            "set_inline": {"id": job["prompt_set_id"], "classes": job["classes"]},
            "active_ids": [c["id"] for c in job["classes"]],
        },
        "run": {"name": job["name"], "save_previews": False},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(5)
        s = _get(f"/api/runs/{run_id}")
        st = (s.get("status") or s.get("state") or "").lower()
        if st in ("completed", "finished", "succeeded", "failed", "error", "stopped", "cancelled"):
            return run_id, st, s


def build_jobs(only_arm=None):
    jobs = []
    for stratum_id, path, conds in STRATA:
        if only_arm in (None, "eind"):
            jobs.append({
                "arm": "eind", "variant": "eind_v1_full", "condition": "both",
                "stratum": stratum_id, "path": path,
                "prompt_set_id": "eind_v1", "classes": EIND["classes"],
                "name": f"faseD_eind_{stratum_id}",
            })
        if only_arm in (None, "edir"):
            for vid, cond, strategy, phrase in EDIR_VARIANTS:
                # Una variante solo corre donde su condicion tiene GT a nivel persona:
                # correrla sin GT quema GPU y produce un numero que nadie puede leer.
                if cond not in conds:
                    continue
                jobs.append({
                    "arm": "edir", "variant": vid, "condition": cond, "strategy": strategy,
                    "stratum": stratum_id, "path": path, "prompt_set_id": "edir_v1",
                    "classes": [{"id": vid, "phrasings": {"default": [phrase]}}],
                    "name": f"faseD_edir_{vid}_{stratum_id}",
                })
    return jobs


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-arm", choices=["eind", "edir"], default=None)
    ap.add_argument("--dry-run", action="store_true")
    # El runner no sabe que modelo tiene cargado el servicio (EOVRT_MODEL_REF es del
    # proceso del media-plane): para una replica con otro modelo, apuntar a OTRO
    # out-dir — la clave de reanudacion es (arm, variant, stratum) y con el mismo
    # dir la replica se "saltearia" todo creyendo que ya corrio.
    ap.add_argument("--out-dir", type=Path, default=OUT)
    a = ap.parse_args()
    OUT = a.out_dir

    jobs = build_jobs(a.only_arm)
    n_imgs = {s: len(list(p.glob("*"))) for s, p, _ in STRATA}
    total = sum(n_imgs[j["stratum"]] for j in jobs)
    print(f"{len(jobs)} corridas, {total} inferencias en total")
    for j in jobs:
        print(f"  {j['arm']:5} {j['variant']:14} {j['stratum']:16} {n_imgs[j['stratum']]:>5} imgs")
    if a.dry_run:
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    res_path = OUT / "runs.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    # Reanudable: la clave es (arm, variant, stratum), no el nombre del run.
    hechos = {(r["arm"], r["variant"], r["stratum"]) for r in results if r.get("run_id")}

    if not wait_ready():
        print("el media-plane no quedo ready", file=sys.stderr)
        return 1

    t0 = time.time()
    for i, j in enumerate(jobs, 1):
        key = (j["arm"], j["variant"], j["stratum"])
        if key in hechos:
            print(f"[{i}/{len(jobs)}] {j['name']} — ya hecho, se saltea", flush=True)
            continue
        print(f"[{i}/{len(jobs)}] {j['name']} ({n_imgs[j['stratum']]} imgs) ...", flush=True)
        t1 = time.time()
        try:
            run_id, st, summary = run_one(j)
        except Exception as e:
            print(f"    FALLO: {e}", flush=True)
            results.append({**{k: j[k] for k in ("arm", "variant", "condition", "stratum")},
                            "error": str(e)})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
            continue
        rec = {k: j[k] for k in ("arm", "variant", "condition", "stratum")}
        # GET /api/runs/{id} anida los conteos en `summary`; leerlos del nivel de
        # arriba devuelve None en silencio y deja la procedencia sin numeros.
        detail = summary.get("summary") or {}
        rec.update({
            "run_id": run_id, "status": st, "prompt_set_id": j["prompt_set_id"],
            "phrases": [p for c in j["classes"] for p in c["phrasings"]["default"]],
            "units_processed": detail.get("units_processed"),
            "total_detections": detail.get("total_detections"),
            "seconds": round(time.time() - t1, 1),
        })
        results.append(rec)
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"    {st} en {rec['seconds']}s — {rec['total_detections']} det "
              f"[{(time.time()-t0)/60:.0f} min transcurridos]", flush=True)

    print(f"\n{len([r for r in results if r.get('run_id')])}/{len(jobs)} corridas OK -> {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
