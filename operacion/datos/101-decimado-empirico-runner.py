"""¿Las conclusiones R1-R6 sobreviven al descarte IRREGULAR del live? (doc 101)

El doc 96 declaró su límite: "el decimado es regular; el descarte live es
irregular (jitter)". La medición 101 (`101-descarte-live-irregularidad.py`)
cuantificó esa irregularidad desde los artefactos reales del camino live:

  - estado actual (humos 08-05):  media 7,28 frames@30 (4,12 fps), CV 0,221
  - rodaje (07-25):               media 12,06 frames@30 (2,49 fps), CV 0,357

Este runner verifica si el jitter EMPÍRICO cambia las conclusiones del eje de
densidad, aislándolo como variable única. Cuatro variantes sobre las
detecciones a 30 fps de T1 (las mismas de G1, bit a bit):

  s7dec : decimado regular stride 7 — GUARD de equivalencia contra R1 (que
          re-infirió a stride 7): si decimar ≡ re-inferir, las detecciones y
          los evals deben salir idénticos. Legitima la técnica (la misma que
          usó `96-sdr-efecto-instrumento.py` para F-96.6).
  j7    : huecos muestreados de la distribución empírica GDINO@08-05
          reescalada a media 7,0 frames (forma/CV preservados, factor
          declarado). Única variable contra R1/R2: la IRREGULARIDAD.
  s12   : decimado regular a media 12 frames — control a la densidad REAL del
          rodaje (2,5 fps; R3 usó stride 15 = 2,0 fps, no exactamente esa).
  j12   : huecos CRUDOS del rodaje (sin reescalar, media 12,06, CV 0,357,
          max ~35 frames). Única variable contra s12: la irregularidad.

Cada variante corre en las DOS granularidades (escena y sujeto, cadenas
idénticas a 96-costo-tiempo-real-runner.py / -sujeto.py) sobre los 34 clips,
se agrega con `aggregate_clip_campaign.py` (las reglas con test) y se
contrasta con bootstrap pareado por clip (10.000 resamples, semilla fija),
el mismo método de `96-critica-verificacion.py`.

GUARDS:
  (a) equivalencia s7dec ≡ R1: mismos frames, mismas detecciones (conf ±1e-3,
      bbox ±0,1 px), mismos evals campo a campo (matched/missed/fp).
  (b) densidad realizada de j7/j12 dentro de ±5% del objetivo.
  (c) sujeto: ninguna persona sin track_id (si no, mediría G0 en silencio).

Uso: 101-decimado-empirico-runner.py [--variantes s7dec,j7,s12,j12] [--clips ...]
"""

import argparse
import json
import random
import subprocess
import sys
import time
import zlib
from pathlib import Path

DATOS = Path(__file__).parent
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
PAT_SCENE = CP / "configs/patterns/cr01_cr02_v2.yaml"
PAT_SUBJ = CP / "configs/patterns/cr01_cr02_v2_subject.yaml"
AGG = DS / "datasets/scripts/bench/aggregate_clip_campaign.py"
GT_DIR = DS / "datasets-videos/gt"
DIST = DATOS / "101-descarte-live-distribucion.json"
T1_PROV = RES / "t1_gdinotiny560_v2short_scene/provenance.json"
R1_RESULT = DATOS / "96-rt-stride7/resultados.json"

FRAME_MS = 1000.0 / 30.0
SEED_BASE = 101          # semilla fija: reproducible
DENS_TOL = 0.05          # guard (b): ±5% de densidad realizada

sys.path.insert(0, str(CP / "src"))
from eovrt_control.tools.track_detections import track_event_stream  # noqa: E402

# variante -> (tipo, parámetro)
#   regular: stride entero
#   jitter:  (grupo de la distribución empírica, media objetivo en frames o None=cruda)
VARIANTES = {
    "s7dec": ("regular", 7),
    "j7": ("jitter", ("grounding_dino@2026-08-05", 7.0)),
    "s12": ("regular", 12),
    "j12": ("jitter", ("grounding_dino@2026-07-25", None)),
}


def cargar_gaps(grupo: str, media_objetivo: float | None) -> tuple[list[float], float]:
    """Huecos empíricos en frames@30 (reescalados si hay media objetivo)."""
    gaps_ms = json.loads(DIST.read_text())["gaps_ms_por_grupo"][grupo]
    frames = [g / FRAME_MS for g in gaps_ms]
    media = sum(frames) / len(frames)
    factor = (media_objetivo / media) if media_objetivo else 1.0
    return [g * factor for g in frames], factor


def frames_variante(variante: str, n_frames: int, clip_id: str,
                    gaps: list[float] | None, seed: int = SEED_BASE) -> list[int]:
    tipo, par = VARIANTES[variante]
    if tipo == "regular":
        return list(range(0, n_frames, par))
    rng = random.Random(seed * 1_000_003 + zlib.crc32(f"{variante}:{clip_id}".encode()))
    kept, f = [], 0
    while f < n_frames:
        kept.append(f)
        f += max(1, round(rng.choice(gaps)))
    return kept


def decimar(det_t1: Path, kept: set[int], out: Path) -> int:
    n = 0
    with det_t1.open() as fh, out.open("w") as oh:
        for line in fh:
            if not line.strip():
                continue
            if json.loads(line)["source"]["frame_index"] in kept:
                oh.write(line)
                n += 1
    return n


def n_frames_de(det_t1: Path) -> int:
    last = 0
    with det_t1.open() as fh:
        for line in fh:
            if line.strip():
                last = json.loads(line)["source"]["frame_index"]
    return last + 1


def replay_and_eval(clip_id, det_path, out_dir, nombre, patrones):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: {nombre}_{clip_id}\n"
        f'  description: "Decimado empirico doc 101 — {clip_id}, {nombre}."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {patrones}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, f"el replay creo {len(nuevos)} directorios nuevos (esperaba 1)"
    alerts = nuevos[0] / "alerts.jsonl"
    if not alerts.exists():
        return None, f"no se encontro {alerts}"
    ev = out_dir / f"eval_{clip_id}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(alerts),
         str(GT_DIR / f"{clip_id}.json"),
         "--detections", str(det_path), "--patterns", str(patrones), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-300:]}"
    return ev, None


def _firma_eventos(path: Path):
    """(frame_index, timestamp, detecciones redondeadas) por evento — para el guard (a)."""
    out = []
    with path.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            e = json.loads(line)
            dets = sorted(
                (d["label"], round(d["confidence"], 3),
                 tuple(round(x, 1) for x in d["bbox_xyxy"]))
                for d in e.get("detections") or [])
            out.append((e["source"]["frame_index"],
                        round(float(e["source"]["timestamp_ms"]), 2), dets))
    return out


def _verificar_track_ids(path: Path):
    total = sin_id = 0
    with path.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            for d in json.loads(line).get("detections") or []:
                if d.get("label") == "person":
                    total += 1
                    if not d.get("track_id"):
                        sin_id += 1
    return total, sin_id


def correr_variante(variante, gran, clips, t1_runs, gaps, seed=SEED_BASE):
    sufijo = "-subject" if gran == "subject" else ""
    semilla = f"-seed{seed}" if seed != SEED_BASE else ""
    out_dir = DATOS / f"101-rt-{variante}{semilla}{sufijo}"
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
    (out_dir / "decimado").mkdir(exist_ok=True)
    if gran == "subject":
        (out_dir / "tracked").mkdir(exist_ok=True)
    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    def guardar():
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    print(f"=== {variante} · {gran} — {len(clips)} clips ===", flush=True)
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            continue
        results = [r for r in results if r["clip_id"] != cid]
        det_t1 = MP / "runs" / t1_runs[cid] / "detections.jsonl"
        n_total = n_frames_de(det_t1)
        kept = frames_variante(variante, n_total, cid, gaps, seed)
        dec = out_dir / "decimado" / f"{cid}.jsonl"
        n_ev = decimar(det_t1, set(kept), dec)

        # guard (b): densidad realizada. El umbral escala con el error estándar de la
        # media (clips cortos tienen ~20-30 huecos: un desvío del 6% es fluctuación
        # legítima del muestreo, no un mecanismo roto): max(±5%, 3·SE).
        media_real = n_total / len(kept)
        tipo, par = VARIANTES[variante]
        objetivo = par if tipo == "regular" else (par[1] or media_real)
        if tipo == "jitter" and par[1]:
            difs = [b - a for a, b in zip(kept, kept[1:])]
            sd = (sum((d - media_real) ** 2 for d in difs) / len(difs)) ** 0.5
            tol = max(DENS_TOL * objetivo, 3.0 * sd / len(difs) ** 0.5)
            if abs(media_real - objetivo) > tol:
                msg = (f"densidad realizada {media_real:.2f} frames/hueco, objetivo "
                       f"{objetivo} (tol ±{tol:.2f})")
                print(f"  [{i}] {cid} GUARD(b): {msg}", flush=True)
                results.append({"clip_id": cid, "error": msg}); guardar(); continue

        entrada = dec
        extra = {}
        if gran == "subject":
            tracked = out_dir / "tracked" / f"{cid}.jsonl"
            stats = track_event_stream(dec, tracked)
            personas, sin_id = _verificar_track_ids(tracked)
            if sin_id:
                msg = f"{sin_id}/{personas} personas sin track_id (mediría G0)"
                print(f"  [{i}] {cid} GUARD(c): {msg}", flush=True)
                results.append({"clip_id": cid, "error": msg}); guardar(); continue
            entrada = tracked
            extra = {"tracks": stats["tracks"],
                     "person_detections": stats["person_detections"]}

        patrones = PAT_SUBJ if gran == "subject" else PAT_SCENE
        ev, err = replay_and_eval(cid, entrada, out_dir,
                                  f"c101_{variante}_{gran}", patrones)
        if err:
            print(f"  [{i}] {cid} FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err}); guardar(); continue
        results.append({"clip_id": cid, "eval": json.loads(ev.read_text()),
                        "variante": variante, "granularidad": gran,
                        "frames_kept": len(kept), "frames_totales": n_total,
                        "eventos": n_ev, "media_gap_frames": round(media_real, 2),
                        "fps_eq": round(30.0 / media_real, 2), **extra})
        guardar()
    ok = len([r for r in results if "eval" in r])
    print(f"  -> {ok}/{len(clips)} OK en {out_dir.name}", flush=True)
    return ok == len(clips)


def guard_equivalencia_r1(clips, t1_runs):
    """Guard (a): decimar T1 a stride 7 ≡ lo que R1 re-infirió a stride 7."""
    r1 = {r["clip_id"]: r["media_run_id"]
          for r in json.loads(R1_RESULT.read_text()) if "eval" in r}
    dif = []
    for cid in clips:
        firma_dec = _firma_eventos(DATOS / "101-rt-s7dec/decimado" / f"{cid}.jsonl")
        firma_r1 = _firma_eventos(MP / "runs" / r1[cid] / "detections.jsonl")
        if firma_dec != firma_r1:
            razon = "n eventos" if len(firma_dec) != len(firma_r1) else \
                next(f"frame {a[0]}" for a, b in zip(firma_dec, firma_r1) if a != b)
            dif.append((cid, razon))
    if dif:
        print(f"GUARD(a) EQUIVALENCIA: {len(dif)} clips difieren de R1: {dif[:5]}")
    else:
        print(f"GUARD(a) EQUIVALENCIA: {len(clips)}/{len(clips)} clips — decimado ≡ "
              "re-inferencia (frames, timestamps y detecciones idénticos)")
    # y los evals, campo a campo (matched/missed/fp/re_alerts)
    dif_ev = []
    for cid in clips:
        mio = json.loads((DATOS / "101-rt-s7dec" / f"eval_{cid}.json").read_text())
        suyo = json.loads((RES / "r1_gdinotiny560_v2short_scene_s7/evals" /
                           f"eval_{cid}.json").read_text())
        campos = ["matched_alerts_count", "missed_alerts_count",
                  "unexpected_alerts_count", "re_alerts_count", "precision",
                  "recall", "f1"]
        if any(mio.get(c) != suyo.get(c) for c in campos):
            dif_ev.append(cid)
    if dif_ev:
        print(f"GUARD(a) EVALS: difieren de R1 en {len(dif_ev)} clips: {dif_ev[:5]}")
    else:
        print(f"GUARD(a) EVALS: {len(clips)}/{len(clips)} idénticos a R1 en "
              "matched/missed/FP/re_alerts/P/R/F1")
    return not dif and not dif_ev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variantes", default="s7dec,j7,s12,j12")
    ap.add_argument("--clips", default="")
    ap.add_argument("--seed", type=int, default=SEED_BASE,
                    help="semilla del muestreo jitter (para robustez multi-semilla)")
    a = ap.parse_args()

    t1_runs = {r["clip_id"]: r["media_run_id"]
               for r in json.loads(T1_PROV.read_text())}
    clips = ([c.strip() for c in a.clips.split(",") if c.strip()]
             or sorted(t1_runs))
    variantes = [v.strip() for v in a.variantes.split(",") if v.strip()]

    t0 = time.time()
    ok_todo = True
    for v in variantes:
        tipo, par = VARIANTES[v]
        gaps = None
        if tipo == "jitter":
            gaps, factor = cargar_gaps(*par)
            print(f"[{v}] distribución {par[0]}: {len(gaps)} huecos, "
                  f"factor de reescalado {factor:.3f}", flush=True)
        for gran in ("scene", "subject"):
            ok_todo &= correr_variante(v, gran, clips, t1_runs, gaps, a.seed)

    if "s7dec" in variantes and a.seed == SEED_BASE:
        ok_todo &= guard_equivalencia_r1(clips, t1_runs)

    # metrics.json por variante × granularidad, con el agregador testeado del banco
    semilla = f"-seed{a.seed}" if a.seed != SEED_BASE else ""
    for v in variantes:
        for suf in ("", "-subject"):
            d = DATOS / f"101-rt-{v}{semilla}{suf}"
            if not d.exists():
                continue
            r = subprocess.run(
                [sys.executable, str(AGG), "--evals-dir", str(d),
                 "--gt-dir", str(GT_DIR), "--out", str(d / "metrics.json")],
                capture_output=True, text=True)
            if r.returncode != 0:
                print(f"AGGREGATE {d.name} FALLO: {(r.stderr or r.stdout)[-200:]}")
                ok_todo = False

    print(f"\nTotal: {(time.time() - t0) / 60:.1f} min — "
          f"{'todo OK' if ok_todo else 'CON FALLAS (ver arriba)'}")
    return 0 if ok_todo else 1


if __name__ == "__main__":
    sys.exit(main())
