"""¿Cuánto del SDR que sube al bajar la densidad es el detector y cuánto el instrumento?

En las campañas de tiempo real el SDR SUBE al bajar la densidad de evidencia
(escena: 0,698 a 30 fps -> 0,718 a 4,3 fps -> 0,736 a 2 fps). Leído ingenuamente
diría "el detector mejora cuando mira menos", que es absurdo. La sospecha es que
parte del efecto es del INSTRUMENTO: `_sdr_for_episode` funde tramos separados por
un hueco <= paso nominal, y el paso nominal es la mediana de gaps de la fuente. A
30 fps el paso es 33 ms y un parpadeo de 100 ms deja un hueco visible; a 2 fps el
paso es 500 ms y ese mismo parpadeo desaparece dentro de la tolerancia.

Este script lo separa: toma las MISMAS detecciones de T1 (stride 1) y las decima
sintéticamente 1 de cada N, recalculando el SDR de los mismos episodios del mismo
GT. Como las detecciones son idénticas, cualquier cambio es 100% del instrumento.
La diferencia contra el SDR medido en la campaña real de stride N es lo que
aporta la percepción.

Uso: 96-sdr-efecto-instrumento.py
"""
import json
import sys
from pathlib import Path
from statistics import mean

CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")

sys.path.insert(0, str(CP / "src"))
from eovrt_control.config import load_patterns_file  # noqa: E402
from eovrt_control.contracts.media import DetectionEvent  # noqa: E402
from eovrt_control.evaluation.temporal import (  # noqa: E402
    _nominal_step_ms, _positive_flags_for_source, _sdr_for_episode,
)

STRIDES = [1, 7, 15, 26]


class _Ep:
    """Episodio mínimo con la forma que `_sdr_for_episode` consume."""

    def __init__(self, d):
        self.episode_id = d.get("episode_id")
        self.start_ms = d["start_ms"]
        self.end_ms = d["end_ms"]
        self.condition_id = d.get("condition_id") or d.get("condition")


def _eventos(path: Path) -> list[DetectionEvent]:
    ev = []
    with path.open() as fh:
        for line in fh:
            if line.strip():
                ev.append(DetectionEvent.model_validate_json(line))
    ev.sort(key=lambda e: e.source.timestamp_ms or 0)
    return ev


def main():
    patterns = {p.condition_id: p for p in
                load_patterns_file(
                    CP / "configs/patterns/cr01_cr02_v2.yaml").pattern_set.patterns}
    proc = {x["clip_id"]: x["media_run_id"]
            for x in json.loads(
                (RES / "t1_gdinotiny560_v2short_scene/provenance.json").read_text())
            if x.get("media_run_id")}

    por_stride = {s: [] for s in STRIDES}
    por_cond = {s: {} for s in STRIDES}

    for clip_id, run_id in sorted(proc.items()):
        gt_path = DS / "datasets-videos/gt" / f"{clip_id}.json"
        det_path = MP / "runs" / run_id / "detections.jsonl"
        if not gt_path.exists() or not det_path.exists():
            continue
        gt = json.loads(gt_path.read_text())
        episodios = [_Ep(e) for e in (gt.get("episodes") or [])]
        if not episodios:
            continue
        eventos = _eventos(det_path)
        if not eventos:
            continue

        for s in STRIDES:
            sub = eventos[::s]
            if len(sub) < 2:
                continue
            paso = _nominal_step_ms(sub)
            for ep in episodios:
                pat = patterns.get(ep.condition_id)
                if pat is None:
                    continue
                flags = _positive_flags_for_source(sub, pat)
                sdr, _ = _sdr_for_episode(sub, flags, ep, paso)
                if sdr is not None:
                    por_stride[s].append(sdr)
                    por_cond[s].setdefault(ep.condition_id, []).append(sdr)

    print("SDR recalculado sobre las MISMAS detecciones de T1, decimadas 1 de cada N.")
    print("Todo cambio acá es del instrumento: las detecciones no cambian.\n")
    print("| stride | fps eq | n episodios | SDR (instrumento) | CR-01 | CR-02 |")
    print("|---|---|---|---|---|---|")
    base = None
    for s in STRIDES:
        xs = por_stride[s]
        if not xs:
            continue
        m = mean(xs)
        if s == 1:
            base = m
        c1 = por_cond[s].get("CR-01") or []
        c2 = por_cond[s].get("CR-02") or []
        print(f"| {s} | {30/s:.2f} | {len(xs)} | {m:.3f}"
              + (f" ({m-base:+.3f})" if s != 1 else " (ref)")
              + f" | {mean(c1):.3f} | {mean(c2):.3f} |")

    out = Path(__file__).parent / "96-sdr-efecto-instrumento.json"
    out.write_text(json.dumps(
        {str(s): {"sdr_medio": mean(por_stride[s]) if por_stride[s] else None,
                  "n": len(por_stride[s]),
                  "por_condicion": {c: mean(v) for c, v in por_cond[s].items()}}
         for s in STRIDES}, indent=2, ensure_ascii=False))
    print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
