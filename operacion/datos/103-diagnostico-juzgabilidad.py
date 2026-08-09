"""Diagnóstico del hallazgo 103: ¿dónde falla la cadena en el estrato B?

Tres mediciones sobre artefactos YA EXISTENTES (cero GPU, cero inferencia nueva):

  1. Tasa de asociación vest/helmet por TAMAÑO de sujeto (proxy: centro de la
     evidencia dentro de la caja del person), sobre las detecciones crudas de I1.
     Si la tasa colapsa con el tamaño ⇒ la "evidencia de ausencia" del motor es
     mayormente fallo de percepción a escala chica, no gente sin EPP.
  2. Contraste con un clip del rodaje (T1): distribución de alturas de person.
     Cuantifica el cambio de régimen (cercano/guionado vs lejano/real).
  3. Identidades del tracker vs personas del GT + altura del violador real
     matcheado (¿un gate por tamaño lo preservaría?).

Es un PROXY diagnóstico (la lógica real de regiones vive en el control-plane);
sirve para atribuir el mecanismo, no para producir métricas de campaña.
"""
import json
from collections import Counter
from pathlib import Path

DATOS = Path(__file__).parent
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")

BUCKETS = [(0, 80), (80, 120), (120, 160), (160, 220), (220, 320), (320, 10000)]


def bucket_label(h):
    for lo, hi in BUCKETS:
        if lo <= h < hi:
            return f"{lo}-{hi if hi < 10000 else '+'}"
    return "?"


def analyze_detections(path, max_events=None):
    """Por evento: para cada person, ¿hay vest/helmet con centro dentro de su caja?"""
    stats = {bucket_label(h): {"n": 0, "vest": 0, "helmet": 0}
             for h in [lo for lo, _ in BUCKETS]}
    heights = []
    n_ev = 0
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            ev = json.loads(line)
            dets = ev.get("detections") or []
            persons = [d for d in dets if d["label"] == "person"]
            others = [(d["label"], (d["bbox_xyxy"][0] + d["bbox_xyxy"][2]) / 2,
                       (d["bbox_xyxy"][1] + d["bbox_xyxy"][3]) / 2)
                      for d in dets if d["label"] in ("vest", "helmet")]
            for p in persons:
                x1, y1, x2, y2 = p["bbox_xyxy"]
                h = y2 - y1
                heights.append(h)
                b = stats[bucket_label(h)]
                b["n"] += 1
                # torso = mitad central vertical; upper = tercio superior
                if any(lbl == "vest" and x1 <= cx <= x2 and y1 + 0.2 * h <= cy <= y1 + 0.75 * h
                       for lbl, cx, cy in others):
                    b["vest"] += 1
                if any(lbl == "helmet" and x1 <= cx <= x2 and y1 - 0.1 * h <= cy <= y1 + 0.4 * h
                       for lbl, cx, cy in others):
                    b["helmet"] += 1
            n_ev += 1
            if max_events and n_ev >= max_events:
                break
    return stats, heights


def median(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


print("=" * 78)
print("1. ASOCIACIÓN vest/helmet POR ALTURA DEL SUJETO (detecciones crudas de I1)")
print("=" * 78)
i1 = {r["clip_id"]: r["media_run_id"]
      for r in json.loads((DATOS / "102-i1-internet-scene-clips/resultados.json").read_text())
      if r.get("media_run_id")}
for cid in ("v04_c01", "v06_c01", "v10_c01"):
    det = MP / "runs" / i1[cid] / "detections.jsonl"
    stats, heights = analyze_detections(det)
    print(f"\n--- {cid}  (mediana de altura person: {median(heights):.0f} px, "
          f"n detecciones person: {len(heights)})")
    print(f"  {'altura px':>10} {'n person':>9} {'% con vest':>11} {'% con helmet':>13}")
    for lo, hi in BUCKETS:
        b = stats[bucket_label(lo)]
        if not b["n"]:
            continue
        print(f"  {bucket_label(lo):>10} {b['n']:>9} "
              f"{100 * b['vest'] / b['n']:>10.1f}% {100 * b['helmet'] / b['n']:>12.1f}%")

print()
print("=" * 78)
print("2. CONTRASTE CON EL RODAJE (T1) — mismas clases, mismo modelo, otro régimen")
print("=" * 78)
t1 = {r["clip_id"]: r["media_run_id"]
      for r in json.loads((RES / "t1_gdinotiny560_v2short_scene/provenance.json").read_text())
      if r.get("media_run_id")}
for cid in ("a_p1_c02", "a_p7_c01", "a_p5_c01"):
    det = MP / "runs" / t1[cid] / "detections.jsonl"
    if not det.exists():
        print(f"  {cid}: detections de T1 ya no está en disco — se omite")
        continue
    stats, heights = analyze_detections(det)
    print(f"\n--- {cid} (rodaje)  (mediana altura person: {median(heights):.0f} px, "
          f"n: {len(heights)})")
    print(f"  {'altura px':>10} {'n person':>9} {'% con vest':>11} {'% con helmet':>13}")
    for lo, hi in BUCKETS:
        b = stats[bucket_label(lo)]
        if not b["n"]:
            continue
        print(f"  {bucket_label(lo):>10} {b['n']:>9} "
              f"{100 * b['vest'] / b['n']:>10.1f}% {100 * b['helmet'] / b['n']:>12.1f}%")

print()
print("=" * 78)
print("3. TRACKER Y VIOLADOR REAL")
print("=" * 78)
i2res = json.loads((DATOS / "102-i2-internet-subject-clips/resultados.json").read_text())
for r in i2res:
    if "eval" in r:
        print(f"  {r['clip_id']}: tracker produjo {r.get('tracks')} tracks "
              f"sobre {r.get('person_detections')} detecciones person")
# altura del sujeto del alert matcheado (el violador real), desde alerts de I2
for cid in ("v04_c01", "v06_c01"):
    ev = json.loads((DATOS / f"102-i2-internet-subject-clips/eval_{cid}.json").read_text())
    matched_ids = {m["alert_id"] for m in ev.get("matches", []) if isinstance(m, dict) and "alert_id" in m}
    alerts_path = ev["alerts_path"]
    with open(alerts_path) as f:
        for line in f:
            a = json.loads(line)
            if a["alert_id"] in matched_ids or (not matched_ids and False):
                bb = a["evidence"]["subject"]["bbox_xyxy"]
                print(f"  {cid}: alerta MATCHEADA {a['condition_id']} subject_key={a['subject_key']} "
                      f"altura sujeto={bb[3] - bb[1]:.0f} px conf={a['evidence']['subject']['confidence']}")
    if not matched_ids:
        print(f"  {cid}: (el eval no expone alert_id en matches — mostrar matches crudos)")
        print("   ", json.dumps(ev.get("matches", [])[:2], ensure_ascii=False)[:400])
