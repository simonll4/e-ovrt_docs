"""Campaña R — el costo del tiempo real sobre el banco del rodaje.

Las 6 campañas del banco (docs 81/84/85/87/88/89) corrieron TODAS `path: DBE`,
`stride: 1`: 30 inferencias por segundo de video. El camino live no puede hacer
eso — durante el rodaje GDINO rindió 1,2–2,6 fps con 92–94% de frames
descartados (doc 71) y el techo de esta máquina tras F-RT5 es 3,75–4,42 fps
(doc 73). O sea: todo el resultado del banco se midió con ~7 a 25x más
evidencia por segundo de la que el tiempo real entrega, y cuánto de ese
rendimiento sobrevive a la restricción NO estaba medido en ninguna parte.

Esta campaña lo mide. Variable única contra T1: la DENSIDAD DE EVIDENCIA.
Mismo modelo (campeón gdino-tiny-560), mismo prompt set congelado, mismo
pattern set oficial, mismo GT, mismo evaluador.

  stride  7 -> 4,29 fps  = el techo de HOY (post F-RT5: 3,75–4,42)
  stride 15 -> 2,00 fps  = lo que EFECTIVAMENTE corrió en vivo en el rodaje

Por cada clip:  media-plane POST /api/runs (video_file, rate_control.stride)
             -> detections.jsonl
             -> control-plane replay (cr01_cr02_v2, granularidad escena)
             -> evaluate-alerts vs gt/<clip>.json (+SDR/TTFD con --detections)
             -> eval_<clip>.json

GUARD (la lección del `no_track_id` de G1): si el stride no se aplicara, la
campaña mediría T1 creyendo medir tiempo real y el error no se vería en ningún
lado. Se verifica por clip que los frames procesados sean ~n_frames/stride.

Uso: 96-costo-tiempo-real-runner.py --stride N [--clips a_p1_c02,...] [--out-dir DIR]
"""
import argparse, json, subprocess, sys, time, urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
PATTERNS = CP / "configs/patterns/cr01_cr02_v2.yaml"
MANIFEST = DS / "datasets/processed/clip_bench/manifest.yaml"

# Prompt set CONGELADO cr01_cr02_v2_short (frozen_sha256 df81fd48...) — idéntico
# al de T1 y al de toda evaluación de bench. Inline, igual que el runner del 81.
PROMPTS = {
    "set_inline": {
        "id": "cr01_cr02_v2_short",
        "classes": [
            {"id": "person", "phrasings": {"default": ["person"]}},
            {"id": "helmet", "phrasings": {"default": ["helmet"]}},
            {"id": "vest", "phrasings": {"default": ["vest"]}},
        ],
    },
    "active_ids": ["person", "helmet", "vest"],
}

# Tolerancia del guard de stride: el muestreo es range(0, n, stride), así que el
# conteo esperado es ceil(n/stride). Se admite +-2 frames por bordes de decode.
GUARD_TOL = 2


def _post(path, body):
    req = urllib.request.Request(MEDIA + path, method="POST",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def _get(path):
    with urllib.request.urlopen(MEDIA + path, timeout=60) as r:
        return json.loads(r.read())


def _banco() -> dict:
    """clip_id -> (n_frames esperado, fps) desde el manifest congelado del banco."""
    import yaml
    out = {}
    for c in yaml.safe_load(MANIFEST.read_text())["clips"]:
        fps = c["fps"]
        out[c["clip_id"]] = (round(c["duration_ms"] / 1000 * fps), fps)
    return out


def media_run(clip_id, stride):
    body = {
        "ingest": {"plugin": "video_file", "config": {
            "path": str(DS / "datasets-videos/clips" / f"{clip_id}.mp4"),
            "source_id": clip_id,
        }},
        "prompts": PROMPTS,
        "run": {"name": f"rt_s{stride}_{clip_id}", "save_previews": False,
                "stride": stride},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(2)
        s = _get(f"/api/runs/{run_id}")
        st = (s.get("status") or s.get("state") or "").lower()
        if st in ("completed", "finished", "succeeded", "failed", "error",
                  "stopped", "cancelled"):
            # El summary viene ANIDADO en la respuesta de /api/runs/{id}. El runner
            # del doc 81 leía el nivel de arriba, por eso su campo `frames` quedó
            # en null en toda la campaña T1.
            return run_id, st, (s.get("summary") or {})


def replay_and_eval(clip_id, det_path, out_dir, stride):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_rt_s{stride}_{clip_id}\n"
        f'  description: "Costo del tiempo real — {clip_id}, stride {stride}, '
        'pattern set oficial v2, granularidad escena."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    # Identificar el run del control por DIFERENCIA de directorios, no por mtime
    # (trampa del doc 81: el mtime cruzaba alertas de un clip con el GT de otro).
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, (f"el replay creo {len(nuevos)} directorios nuevos (esperaba 1): "
                      f"{[p.name for p in nuevos]}")
    alerts = nuevos[0] / "alerts.jsonl"
    if not alerts.exists():
        return None, f"no se encontro {alerts}"
    ev = out_dir / f"eval_{clip_id}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(alerts),
         str(DS / "datasets-videos/gt" / f"{clip_id}.json"),
         "--detections", str(det_path), "--patterns", str(PATTERNS), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-300:]}"
    return ev, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stride", type=int, required=True)
    ap.add_argument("--clips", default="")
    ap.add_argument("--out-dir", default="")
    a = ap.parse_args()

    out_dir = Path(a.out_dir or (Path(__file__).parent / f"96-rt-stride{a.stride}"))
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)

    banco = _banco()
    clips = ([c.strip() for c in a.clips.split(",") if c.strip()]
             or sorted(p.stem for p in (DS / "datasets-videos/gt").glob("a_p*.json")))

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    def guardar():
        # Incremental: una corrida larga no puede perder todo por un fallo tardío.
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    fps_eq = 30.0 / a.stride
    print(f"=== stride {a.stride} (~{fps_eq:.2f} fps equivalentes) — {len(clips)} clips ===",
          flush=True)

    t_camp = time.time()
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            print(f"[{i}/{len(clips)}] {cid} — ya evaluado, se saltea", flush=True)
            continue
        results = [r for r in results if r["clip_id"] != cid]
        t0 = time.time()
        print(f"[{i}/{len(clips)}] {cid} ...", flush=True)
        try:
            run_id, st, summary = media_run(cid, a.stride)
        except Exception as e:
            print(f"    MEDIA FALLO: {e}", flush=True)
            results.append({"clip_id": cid, "error": f"media: {e}"}); guardar(); continue
        if st not in ("completed", "finished", "succeeded"):
            print(f"    MEDIA estado={st}", flush=True)
            results.append({"clip_id": cid, "error": f"media estado {st}"}); guardar(); continue

        frames = summary.get("units_processed")
        aplicado = ((summary.get("run_descriptor") or {}).get("rate_control")
                    or {}).get("stride")
        fps_efectivo = summary.get("fps_effective")

        # GUARD del stride, por partida doble: sin esto, un stride que no se
        # aplica mide T1 en silencio y la campaña entera reportaría el resultado
        # equivocado (la lección del `no_track_id` de G1, doc 89).
        # (a) el descriptor de la corrida declara el stride que realmente rigió
        if aplicado != a.stride:
            msg = f"stride NO aplicado: run_descriptor dice {aplicado}, pedí {a.stride}"
            print(f"    GUARD: {msg}", flush=True)
            results.append({"clip_id": cid, "error": msg}); guardar(); continue
        # (b) y el conteo de unidades procesadas lo confirma de forma independiente
        n_total, _ = banco.get(cid, (None, None))
        if n_total:
            esperado = -(-n_total // a.stride)     # ceil(n/stride)
            if frames is None or abs(frames - esperado) > GUARD_TOL:
                msg = (f"conteo inconsistente: {frames} frames procesados, "
                       f"esperaba ~{esperado} (n={n_total}, stride={a.stride})")
                print(f"    GUARD: {msg}", flush=True)
                results.append({"clip_id": cid, "error": msg}); guardar(); continue

        det = MP / "runs" / run_id / "detections.jsonl"
        if not det.exists():
            results.append({"clip_id": cid, "error": "sin detections.jsonl"}); guardar(); continue
        ev, err = replay_and_eval(cid, det, out_dir, a.stride)
        dt = time.time() - t0
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err}); guardar(); continue
        e = json.loads(ev.read_text())
        results.append({"clip_id": cid, "media_run_id": run_id, "eval": e,
                        "frames": frames, "frames_totales": n_total,
                        "stride": a.stride, "fps_eq": round(fps_eq, 2),
                        "fps_effective": fps_efectivo,
                        "seconds": round(dt, 1)})
        guardar()
        ok = len([r for r in results if "eval" in r])
        print(f"    OK en {dt:.1f}s ({frames} frames de {n_total}) -> {ev.name}   "
              f"[{ok} listos, {(time.time()-t_camp)/60:.0f} min]", flush=True)

    guardar()
    ok = len([r for r in results if "eval" in r])
    print(f"\n{ok}/{len(clips)} clips OK en {(time.time()-t_camp)/60:.1f} min")
    print(f"-> {res_path}")
    return 0 if ok == len(clips) else 1


if __name__ == "__main__":
    sys.exit(main())
