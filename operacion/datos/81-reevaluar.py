"""Re-evalua los clips ya corridos desde sus artefactos guardados.

La inferencia (GPU) NO se repite: alerts.jsonl y detections.jsonl ya existen.
Solo se vuelve a correr `evaluate-alerts`, que es CPU. Sirve para aplicar fixes
del evaluador sin re-correr la campana.
"""
import json, subprocess, sys
from pathlib import Path

CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
GT = Path("/home/simonll4/projects/e-ovrt_datasets/datasets-videos/gt")
PAT = CP / "configs/patterns/cr01_cr02_v2.yaml"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else
           "/tmp/claude-1000/-home-simonll4-projects/fed555a9-e337-416c-acf7-7c38d107d7a2/scratchpad/ciclo_out")

res = json.loads((OUT / "resultados.json").read_text())
n_ok = n_err = 0
for r in res:
    if "eval" not in r:
        continue
    cid = r["clip_id"]
    alerts = r["eval"]["alerts_path"]
    det = r["eval"].get("detections_path")
    ev = OUT / f"eval_{cid}.json"
    cmd = [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", alerts,
           str(GT / f"{cid}.json"), "--patterns", str(PAT), "-o", str(ev)]
    if det:
        cmd += ["--detections", det]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=str(CP))
    if p.returncode != 0:
        print(f"  {cid}: FALLO {(p.stderr or p.stdout)[-200:]}"); n_err += 1; continue
    r["eval"] = json.loads(ev.read_text()); n_ok += 1

(OUT / "resultados.json").write_text(json.dumps(res, indent=2, ensure_ascii=False))
print(f"re-evaluados: {n_ok}, errores: {n_err}")
