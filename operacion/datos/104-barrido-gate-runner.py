"""Barrido del gate de juzgabilidad — `min_subject_area_px`, que YA ES CONFIG.

Contexto (doc 103 §7): la evidencia de ausencia de E-IND colapsa con la escala del
sujeto. El pattern set oficial expone `evidence.min_subject_area_px`, y está en
**400 px² (≈20×20 px: prácticamente sin gate)** porque se calibró para el rodaje,
donde la mediana de altura de person es 716–839 px y no hacía falta. Este barrido
lo re-calibra para el régimen del estrato B. **Es configuración, no capacidad nueva
(ADR-015 intacto): el knob existe y `spatial_absence.py` ya lo aplica.**

CRITERIO DEL PUNTO DE OPERACIÓN, DECLARADO ANTES DE MIRAR MÉTRICAS DE ALERTA:
el gate se fija donde la curva de percepción medida (asociación de `vest` por
altura del sujeto, `103-diagnostico-juzgabilidad.py`) cruza el 50% — banda
160–220 px ⇒ H=160 px ⇒ con el aspect ratio mediano medido (w/h = 0,411 en v06)
≈ **10.500 px²**. Los otros dos valores son sensibilidad a cada lado, no candidatos.

Variable única: `min_subject_area_px`. Todo lo demás (timings 4000/7000, regiones,
confianzas, modelo, prompts) queda intacto. Cero inferencia nueva: reusa las
detecciones de I1 (scene) y los streams trackeados de I2 (subject).

LIMITACIÓN QUE VA AL DOC: la calibración usa el mismo estrato que motivó la
hipótesis ⇒ es IN-SAMPLE. Sirve para caracterizar el mecanismo y la sensibilidad,
no para declarar un umbral de producción; eso exige clips frescos.

Uso: 104-barrido-gate-runner.py [--gates 400,6000,10500,16500]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

DATOS = Path(__file__).parent
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
OUT = DATOS / "104-barrido-gate"

CLIPS = ["v04_c01", "v06_c01", "v10_c01"]
BASE_PATTERNS = {
    "scene": CP / "configs/patterns/cr01_cr02_v2.yaml",
    "subject": CP / "configs/patterns/cr01_cr02_v2_subject.yaml",
}
# scene = detecciones crudas de I1; subject = streams ya trackeados de I2
STREAMS = {
    "scene": lambda cid: _i1_detections(cid),
    "subject": lambda cid: DATOS / "102-i2-internet-subject-clips/tracked" / f"{cid}.jsonl",
}


def _i1_detections(cid):
    res = json.loads((DATOS / "102-i1-internet-scene-clips/resultados.json").read_text())
    run_id = {r["clip_id"]: r.get("media_run_id") for r in res}[cid]
    return Path("/home/simonll4/projects/e-ovrt_media-plane/runs") / run_id / "detections.jsonl"


def patterns_with_gate(base: Path, area_px: float, dst: Path) -> Path:
    doc = yaml.safe_load(base.read_text())
    for p in doc["pattern_set"]["patterns"]:
        p["evidence"]["min_subject_area_px"] = float(area_px)
    doc["pattern_set"]["id"] = f"{doc['pattern_set']['id']}_gate{int(area_px)}"
    doc["pattern_set"]["description"] = (
        f"BARRIDO doc 104 — variante de {base.name} con min_subject_area_px="
        f"{int(area_px)} (baseline oficial: 400). Variable única. Exploratorio, "
        f"calibración in-sample sobre el estrato B; NO es pattern set de plataforma."
    )
    dst.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))
    return dst


def replay_and_eval(cid, det, patterns, out_dir, tag):
    cfg = out_dir / f"replay_{cid}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: gate_{tag}_{cid}\n"
        f'  description: "barrido gate juzgabilidad {tag} — doc 104"\n'
        f"input:\n  type: media_jsonl\n  path: {det}\n"
        f"patterns:\n  file: {patterns}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_alerts_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: ERROR\n")
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-200:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, f"replay creo {len(nuevos)} dirs (esperaba 1)"
    ev_path = out_dir / f"eval_{cid}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(nuevos[0] / "alerts.jsonl"),
         str(DS / "datasets-videos/gt" / f"{cid}.json"),
         "--detections", str(det), "--patterns", str(patterns), "-o", str(ev_path)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-200:]}"
    return json.loads(ev_path.read_text()), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gates", default="400,6000,10500,16500")
    a = ap.parse_args()
    gates = [float(g) for g in a.gates.split(",")]

    filas = []
    print(f"{'gran':>8} {'gate px2':>9} {'clip':>9} {'match':>6} {'miss':>5} "
          f"{'FP':>5} {'re_al':>6}")
    for gran in ("scene", "subject"):
        for g in gates:
            out_dir = OUT / gran / f"g{int(g)}"
            (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
            pat = patterns_with_gate(BASE_PATTERNS[gran], g,
                                     out_dir / f"patterns_gate{int(g)}.yaml")
            tot = {"matched": 0, "missed": 0, "fp": 0}
            for cid in CLIPS:
                det = STREAMS[gran](cid)
                ev, err = replay_and_eval(cid, det, pat, out_dir, f"{gran}_g{int(g)}")
                if err:
                    print(f"{gran:>8} {int(g):>9} {cid:>9}  ERROR {err}")
                    continue
                m, mi = ev["matched_alerts_count"], ev["missed_alerts_count"]
                fp, re_ = ev["unexpected_alerts_count"], ev["re_alerts_count"]
                print(f"{gran:>8} {int(g):>9} {cid:>9} {m:>6} {mi:>5} {fp:>5} {re_:>6}")
                tot["matched"] += m; tot["missed"] += mi; tot["fp"] += fp
                filas.append({"granularity": gran, "gate_px2": g, "clip": cid,
                              "matched": m, "missed": mi, "fp": fp, "re_alerts": re_})
            print(f"{gran:>8} {int(g):>9} {'TOTAL':>9} {tot['matched']:>6} "
                  f"{tot['missed']:>5} {tot['fp']:>5}")
            print()
    (OUT / "resumen.json").write_text(json.dumps(filas, indent=2, ensure_ascii=False))
    print(f"-> {OUT}/resumen.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
