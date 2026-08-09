"""Barrido de los knobs restantes del pattern set contra el estrato B (doc 107).

Completa la matriz que el doc 104 dejó a medias: allá se barrió
`min_subject_area_px` (el gate); acá los otros dos knobs de `evidence` y el timing.
Todo configuración existente (ADR-015 intacto), granularidad `subject` (la única
viva en este régimen, F-104.2), streams trackeados de I2 (tiny) — cero inferencia.

Tres barridos de VARIABLE ÚNICA sobre `cr01_cr02_v2_subject`:

  A. `evidence.min_subject_confidence`      0,35 (=I2) → 0,40 / 0,45 / 0,50
     Los sujetos de los FP de I1 entraban con conf 0,39–0,40: ¿cuánto del flood son
     sujetos-fantasma de baja confianza?  Riesgo: matar al violador real.
  B. `evidence.min_absent_class_confidence` 0,25 (=I2) → 0,30 / 0,40 / 0,50
     MEDIDO ANTES DE BARRER: el stream tiene piso 0,30 en las 3 clases (box_threshold
     del modelo) ⇒ el baseline 0,25 ya acepta TODA la evidencia y **bajarlo es
     no-op**; 0,30 se incluye como control (debe reproducir I2 exacto). Subirlo
     RECHAZA evidencia débil de chaleco ⇒ predicción pre-registrada: FP SUBE (más
     ausencia fabricada); lo que mide es el acople alucinación↔supresión (F-104.4).
  C. `timing.confirm_after_ms` de CR-02     7000 (=I2) → 10000 / 12000
     Los tracks-fragmento del tracker duran poco: una persistencia mayor debería
     matarlos sin tocar al violador real (su episodio dura 13,1 s > 12 s).
     ⚠ Compatibilidad estilo F-DR9 verificada ANTES de correr: el GT clasifica
     episodio/sub-umbral con 7000; un motor a 12000 no puede confirmar violaciones
     reales de 7–12 s ⇒ falsos missed. Con ESTE GT no existen (episodios de 14,0 y
     13,1 s; sub-umbral máximo 1,4 s), así que el barrido es válido acá y NO
     generaliza a otro banco sin re-chequear. La ventana de matching del evaluador
     sale del GT (origin=gt_provenance), no del pattern set parcheado: correcto,
     las alertas se juzgan contra la semántica del GT.

Uso: 107-barrido-knobs-runner.py
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

DATOS = Path(__file__).parent
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
BASE = CP / "configs/patterns/cr01_cr02_v2_subject.yaml"
TRACKED = DATOS / "102-i2-internet-subject-clips/tracked"
OUT = DATOS / "107-barrido-knobs"
CLIPS = ["v04_c01", "v06_c01", "v10_c01"]

SWEEPS = [
    ("A_subj_conf", "evidence.min_subject_confidence", [0.40, 0.45, 0.50]),
    ("B_evid_conf", "evidence.min_absent_class_confidence", [0.30, 0.40, 0.50]),
    ("C_confirm_cr02", "timing.confirm_after_ms@CR-02", [10000.0, 12000.0]),
]


def patch_patterns(campo: str, valor: float, dst: Path) -> Path:
    doc = yaml.safe_load(BASE.read_text())
    seccion, _, resto = campo.partition(".")
    clave, _, solo_cond = resto.partition("@")
    for p in doc["pattern_set"]["patterns"]:
        if solo_cond and p["condition_id"] != solo_cond:
            continue
        p[seccion][clave] = valor
    doc["pattern_set"]["id"] += f"_{seccion[:4]}{int(valor*100) if valor<1 else int(valor)}"
    doc["pattern_set"]["description"] = (
        f"BARRIDO doc 107 — {campo}={valor} sobre cr01_cr02_v2_subject (variable "
        f"única). Exploratorio in-sample del estrato B; NO es pattern set de plataforma."
    )
    dst.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))
    return dst


def replay_and_eval(cid, det, patterns, out_dir, tag):
    cfg = out_dir / f"replay_{cid}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: knobs_{tag}_{cid}\n"
        f'  description: "barrido knobs doc 107 — {tag}"\n'
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
    ev = out_dir / f"eval_{cid}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts",
         str(nuevos[0] / "alerts.jsonl"),
         str(DS / "datasets-videos/gt" / f"{cid}.json"),
         "--detections", str(det), "--patterns", str(patterns), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-200:]}"
    return json.loads(ev.read_text()), None


def main():
    filas = []
    print(f"{'sweep':>14} {'valor':>7} {'clip':>9} {'match':>6} {'miss':>5} {'FP':>5} {'re_al':>6} {'t_alert':>9}")
    for sweep_id, campo, valores in SWEEPS:
        for v in valores:
            tag = f"{sweep_id}_{v}"
            out_dir = OUT / sweep_id / str(v)
            (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
            pat = patch_patterns(campo, v, out_dir / "patterns.yaml")
            tot = {"matched": 0, "missed": 0, "fp": 0}
            for cid in CLIPS:
                ev, err = replay_and_eval(cid, TRACKED / f"{cid}.jsonl", pat, out_dir, tag)
                if err:
                    print(f"{sweep_id:>14} {v:>7} {cid:>9}  ERROR {err}")
                    continue
                m, mi = ev["matched_alerts_count"], ev["missed_alerts_count"]
                fp, re_ = ev["unexpected_alerts_count"], ev["re_alerts_count"]
                ta = ev.get("avg_latency_ms_from_episode_start")
                print(f"{sweep_id:>14} {v:>7} {cid:>9} {m:>6} {mi:>5} {fp:>5} {re_:>6} "
                      f"{ta if ta is not None else '—':>9}")
                tot["matched"] += m; tot["missed"] += mi; tot["fp"] += fp
                filas.append({"sweep": sweep_id, "campo": campo, "valor": v, "clip": cid,
                              "matched": m, "missed": mi, "fp": fp, "re_alerts": re_,
                              "t_alert_ms": ta})
            print(f"{sweep_id:>14} {v:>7} {'TOTAL':>9} {tot['matched']:>6} "
                  f"{tot['missed']:>5} {tot['fp']:>5}")
            print()
    (OUT / "resumen.json").write_text(json.dumps(filas, indent=2, ensure_ascii=False))
    print(f"baseline (I2): matched=2 missed=0 FP=216 (196 pos + 20 neg)")
    print(f"-> {OUT}/resumen.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
