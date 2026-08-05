"""Guard de comparabilidad: ¿el código de HOY reproduce las métricas de T1?

Las campañas de referencia (T1 08-03 23:02, G1 08-04 19:08) se evaluaron con el
control-plane de esas fechas. Después vino `5327080` (08-04 16:38), que cambió el
despacho de evaluadores y toca `_positive_flags_for_source` — el que deriva
SDR/TTFD. Su mensaje afirma "los SDR de las campañas eind no cambian", pero
contrastar la campaña de tiempo real contra números producidos por OTRO
evaluador mezclaría dos efectos (densidad de evidencia + versión del código) y
el resultado no significaría nada.

Este script lo verifica en vez de creerlo: re-corre replay + evaluate-alerts con
el código actual sobre las MISMAS detecciones de T1 y compara campo a campo
contra el eval guardado.

Uso: 96-verificar-comparabilidad-t1.py [--clips a,b,c]
"""
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
T1 = RES / "t1_gdinotiny560_v2short_scene"
PATTERNS = CP / "configs/patterns/cr01_cr02_v2.yaml"

CAMPOS = ["precision", "recall", "f1", "avg_sdr", "avg_ttfd_ms",
          "matched", "missed", "unexpected", "re_alerts",
          "applicability_state", "evaluable_episodes"]


def rehacer(clip_id: str, run_id: str, work: Path):
    det = MP / "runs" / run_id / "detections.jsonl"
    if not det.exists():
        return None, f"no existen las detecciones de T1: {det}"
    cfg = work / f"{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: verif_t1_{clip_id}\n"
        f'  description: "Guard de comparabilidad — {clip_id}."\n'
        f"input:\n  type: media_jsonl\n  path: {det}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {work / 'runs'}\n"
        "  save_alerts_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    before = {p.name for p in (work / "runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-200:]}"
    nuevos = [p for p in (work / "runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, f"replay creo {len(nuevos)} dirs"
    ev = work / f"eval_{clip_id}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts",
         str(nuevos[0] / "alerts.jsonl"),
         str(DS / "datasets-videos/gt" / f"{clip_id}.json"),
         "--detections", str(det), "--patterns", str(PATTERNS), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-200:]}"
    return json.loads(ev.read_text()), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clips", default="")
    a = ap.parse_args()

    proc = {x["clip_id"]: x["media_run_id"]
            for x in json.loads((T1 / "provenance.json").read_text())
            if x.get("media_run_id")}
    clips = [c.strip() for c in a.clips.split(",") if c.strip()] or sorted(proc)

    work = Path(tempfile.mkdtemp(prefix="verif_t1_"))
    (work / "runs").mkdir(parents=True, exist_ok=True)

    iguales = distintos = fallos = 0
    for cid in clips:
        guardado_p = T1 / "evals" / f"eval_{cid}.json"
        if not guardado_p.exists() or cid not in proc:
            continue
        guardado = json.loads(guardado_p.read_text())
        nuevo, err = rehacer(cid, proc[cid], work)
        if err:
            print(f"{cid}: FALLO — {err}")
            fallos += 1
            continue
        difs = [(k, guardado.get(k), nuevo.get(k)) for k in CAMPOS
                if guardado.get(k) != nuevo.get(k)]
        if difs:
            distintos += 1
            print(f"{cid}: DIFIERE")
            for k, v0, v1 in difs:
                print(f"    {k}: guardado={v0}  hoy={v1}")
        else:
            iguales += 1
            print(f"{cid}: ok")

    print(f"\n{iguales} idénticos · {distintos} difieren · {fallos} fallos "
          f"(de {len(clips)} pedidos)")
    if distintos or fallos:
        print("\n⚠️  La comparación contra T1/G1 NO es limpia con los números "
              "guardados: hay que RE-EVALUAR las referencias con el código de hoy.")
        return 1
    print("\n✅ El código de hoy reproduce T1 exacto: comparar la campaña de "
          "tiempo real contra los números guardados es limpio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
