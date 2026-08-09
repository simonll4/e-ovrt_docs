"""Taxonomia de las fallas de una campaña de clips, verificada contra el GT.

El agregado (`aggregate_clip_campaign.py`) dice CUANTO falla una combinacion; esto
dice POR QUE. Se hizo a mano tres veces (doc 81 §5, doc 84 F-84.5, humo de D1) con
el mismo criterio; aca queda como herramienta para que la lectura de dos campañas
sea comparable y no dependa de rehacer la clasificacion.

Clasifica cada alerta inesperada contra los episodios del GT:

  prematura_pre_roll   alerta de la MISMA condicion que llega ANTES del borde de
                       matching (start_ms + persistencia + tolerancia). El modelo ve
                       la violacion durante el tramo que el anotador marco como
                       "cumple". Doble castigo: el episodio cuenta missed Y la alerta
                       unexpected.
  cruzada_de_condicion alerta de una condicion que NO tiene episodio en ese clip.
                       Firma de la granularidad de escena (F-81.2a): el motor acumula
                       "alguien sin X" y en multitud los sujetos se relevan.
  tardia               alerta de la misma condicion posterior al cierre de la ventana
                       (y del span del episodio: no es re_alert, ADR-011).
  sin_episodio_activo  el resto (clip negativo, o fuera de todo episodio conocido).

Uso:
  python3 85-mecanismo-de-fallas.py --evals-dir <dir> [--label T1] [--evals-dir2 <dir> --label2 D1]
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

GT_DIR = Path("/home/simonll4/projects/e-ovrt_datasets/datasets-videos/gt")

# Persistencia del pattern set oficial (v2 y edir_v1 comparten timings a proposito).
PERSISTENCIA_MS = {"CR-01": 4000.0, "CR-02": 7000.0}
# Tolerancia de bordes declarada por el GT (F-EV2). Se lee del GT si esta.
TOLERANCIA_DEFAULT_MS = 500.0


def _gt_de(clip_id: str) -> dict:
    return json.loads((GT_DIR / f"{clip_id}.json").read_text())


def clasificar(eval_path: Path) -> list[dict]:
    """Una fila por alerta inesperada del clip, con su clasificacion y distancia."""
    e = json.loads(eval_path.read_text())
    clip_id = e["scenario_id"]
    if not (e.get("unexpected_alerts") or []):
        return []
    gt = _gt_de(clip_id)
    fps = gt.get("fps") or 30.0
    tol = (gt.get("annotation") or {}).get("start_end_tolerance_ms", TOLERANCIA_DEFAULT_MS)
    episodios = defaultdict(list)
    for ep in gt.get("episodes") or []:
        episodios[ep["condition_id"]].append((ep["start_ms"], ep["end_ms"]))

    filas = []
    for alerta in e["unexpected_alerts"]:
        cond = alerta["condition_id"]
        t_ms = (alerta["frame_index"] / fps) * 1000.0
        mismos = episodios.get(cond) or []
        if not mismos:
            tipo, delta = ("cruzada_de_condicion" if episodios else "sin_episodio_activo"), None
        else:
            persist = PERSISTENCIA_MS.get(cond, 4000.0)
            # Borde inferior de la ventana de matching de cada episodio.
            bordes = [(s + persist - tol, e_, s) for s, e_ in mismos]
            # El episodio mas cercano en el tiempo.
            borde_inf, fin, inicio = min(bordes, key=lambda b: abs(b[0] - t_ms))
            if t_ms < borde_inf:
                tipo, delta = "prematura_pre_roll", borde_inf - t_ms
            elif t_ms > fin + tol:
                tipo, delta = "tardia", t_ms - fin
            else:
                tipo, delta = "sin_episodio_activo", None
        # Escenario: del nombre en el rodaje (`a_pX_cYY`); si el naming no lo trae
        # (clips del lote de internet, `vNN_cNN`), del propio GT. ✎ doc 107.
        m_esc = re.search(r"_p(\d)_", clip_id)
        escenario = m_esc.group(1) if m_esc else str(gt.get("scenario", "?")).lstrip("P")
        filas.append({
            "clip_id": clip_id, "escenario": escenario,
            "condicion": cond, "t_s": round(t_ms / 1000.0, 1),
            "tipo": tipo, "delta_s": round(delta / 1000.0, 1) if delta is not None else None,
        })
    return filas


def resumen(evals_dir: Path, label: str) -> dict:
    filas = []
    for ev in sorted(Path(evals_dir).glob("eval_*.json")):
        filas.extend(clasificar(ev))
    tipos = Counter(f["tipo"] for f in filas)
    prem = [f["delta_s"] for f in filas if f["tipo"] == "prematura_pre_roll"]
    print(f"\n===== {label}  ({len(filas)} alertas inesperadas)")
    for tipo, n in tipos.most_common():
        print(f"  {tipo:22} {n:>3}")
    if prem:
        print(f"  prematuras: adelanto {min(prem):.1f}–{max(prem):.1f} s "
              f"(mediana {sorted(prem)[len(prem)//2]:.1f} s)")
    por_esc = Counter(f"P{f['escenario']}" for f in filas)
    print(f"  por escenario: {dict(sorted(por_esc.items()))}")
    return {"label": label, "filas": filas, "tipos": dict(tipos)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evals-dir", required=True, type=Path)
    ap.add_argument("--label", default="campaña")
    ap.add_argument("--evals-dir2", type=Path)
    ap.add_argument("--label2", default="campaña 2")
    ap.add_argument("--detalle", action="store_true", help="una linea por alerta")
    a = ap.parse_args()

    r1 = resumen(a.evals_dir, a.label)
    if a.detalle:
        for f in r1["filas"]:
            print(f"    {f['clip_id']:12} {f['condicion']} @{f['t_s']:>6}s  {f['tipo']}"
                  + (f" (+{f['delta_s']}s)" if f["delta_s"] is not None else ""))
    if a.evals_dir2:
        r2 = resumen(a.evals_dir2, a.label2)
        print(f"\n===== contraste {a.label} vs {a.label2}")
        for tipo in sorted(set(r1["tipos"]) | set(r2["tipos"])):
            print(f"  {tipo:22} {r1['tipos'].get(tipo,0):>3} -> {r2['tipos'].get(tipo,0):>3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
