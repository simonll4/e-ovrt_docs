#!/bin/bash
# 110 — Campaña gen. 3 del estrato B: I1 (scene) + I2 (subject) + Nivel A, con
# `v03_c02` incorporado al banco (doc 110).
#
# QUÉ HACE, de punta a punta y sin intervención:
#   0. deriva la lista de clips del MANIFEST del banco (bloque B, state gt_ready)
#      => cuando entren los 9 clips que faltan del lote, este mismo script los toma
#         sin editar nada
#   1. preflight del banco: validate_clip_gt + freeze sha256 (falla cerrado)
#   2. levanta media-plane :8080 + control-plane :8081 si no están arriba
#   3. FASE SCENE (I1): inferencia fresca de TODOS los clips en UNA sesión
#   4. verifica DETERMINISMO contra la gen. 2 (doc 109) en los clips que ya estaban
#   5. FASE SUBJECT (I2): reusa las cajas de la fase scene (sin inferencia nueva)
#   6. agrega ambas campañas a metrics.json (guardando la gen. 2 al lado)
#   7. NIVEL A: estrato B (5 clips) + consolidado con el piloto (9 clips)
#   8. imprime qué quedó y qué hay que escribir a mano
#
# POR QUÉ RE-CORRER LOS 5 Y NO SOLO EL NUEVO: una campaña citable tiene UNA
# procedencia (un hardware, una sesión, un prompt set congelado). Mezclar la
# inferencia de anteayer con la de hoy en la misma tabla es exactamente el desorden
# que el doc 109 §1 vino a arreglar. El costo es GPU y `v06_c01` lo domina (~33 min
# de los ~45); el resto es minutos.
#
# Uso:
#   bash docs/operacion/datos/110-estrato-b-gen3.sh
#   CLIPS=v03_c02 bash docs/operacion/datos/110-estrato-b-gen3.sh   # solo el nuevo
#                                                                   # (cifras NO citables
#                                                                   #  como campaña: dos
#                                                                   #  procedencias)
# Reanudable: el runner saltea los clips que ya tienen eval en resultados.json.
set -uo pipefail

DS=/home/simonll4/projects/e-ovrt_datasets
CP=/home/simonll4/projects/e-ovrt_control-plane
ES=/home/simonll4/projects/e-ovrt_experimental-setup
DATOS="$(cd "$(dirname "$0")" && pwd)"
OUT="$DATOS/110-estrato-b-gen3"
GEN2="$DATOS/109-estrato-b-final"
RUNNER="$DATOS/102-ciclo-internet-runner.py"
BANK="$DS/datasets/processed/clip_bench"
I1="$ES/results/clip_bench/i1_gdinotiny560_v2short_scene_internet"
I2="$ES/results/clip_bench/i2_gdinotiny560_v2short_subject_internet"

fatal() { echo "[FATAL] $*" >&2; exit 1; }
paso()  { echo; echo "════ $* ════"; }

# ── 0. lista de clips: del manifest, no de una constante ──────────────────────
paso "0. clips del estrato B con GT en el banco"
if [ -n "${CLIPS:-}" ]; then
  echo "    lista FORZADA por env: $CLIPS"
  echo "    ⚠ una corrida parcial NO es la campaña: sus cifras conviven con otra"
  echo "      procedencia y no se pueden fusionar en la misma tabla (doc 109 §1)."
else
  CLIPS=$(python3 - "$BANK/manifest.yaml" <<'PY'
import sys, yaml
m = yaml.safe_load(open(sys.argv[1]))
ids = [c["clip_id"] for c in m["clips"]
       if c.get("block") == "B" and c.get("state") == "gt_ready"]
print(",".join(sorted(ids)))
PY
)
  [ -n "$CLIPS" ] || fatal "el manifest no tiene clips de bloque B en gt_ready"
  echo "    $CLIPS"
fi
N_CLIPS=$(awk -F, '{print NF}' <<<"$CLIPS")
echo "    manifest.yaml sha256: $(sha256sum "$BANK/manifest.yaml" | cut -c1-16)…"

# ── 1. preflight del banco ────────────────────────────────────────────────────
paso "1. preflight del banco (falla cerrado)"
cd "$DS" || fatal "no está $DS"
python3 datasets/scripts/bench/validate_clip_gt.py \
    --manifest "$BANK/manifest.yaml" --base-dir "$BANK" | tail -3 \
  || fatal "validate_clip_gt falló"
( cd "$BANK" && sha256sum -c clip_bench.sha256 > /tmp/110-freeze.txt 2>&1 )
echo "    freeze: $(grep -c ': OK$' /tmp/110-freeze.txt) OK / $(grep -c 'FAILED' /tmp/110-freeze.txt) FAILED"
grep -q FAILED /tmp/110-freeze.txt && fatal "el freeze del banco no verifica"
for c in ${CLIPS//,/ }; do
  for f in "$BANK/gt/$c.json" "$BANK/annotations/$c.xml" "$DS/datasets-videos/clips/$c.mp4"; do
    [ -f "$f" ] || fatal "falta $f"
  done
done
echo "    artefactos completos para los $N_CLIPS clips"

# ── 2. servicios ──────────────────────────────────────────────────────────────
paso "2. servicios (media-plane :8080 · control-plane :8081)"
if curl -sf -m 4 http://127.0.0.1:8080/readyz >/dev/null 2>&1; then
  echo "    ya estaban arriba: $(curl -s -m 4 http://127.0.0.1:8080/readyz)"
else
  bash "$DATOS/91-arrancar-servicios.sh" || fatal "no levantaron los servicios"
fi
curl -s -m 4 http://127.0.0.1:8080/readyz | grep -q "gdino-tiny-560" \
  || echo "    ⚠ el modelo cargado NO parece gdino-tiny-560 — la campaña exige el campeón"

# ── 3. FASE SCENE (I1) ────────────────────────────────────────────────────────
paso "3. FASE SCENE (I1) — inferencia fresca, $N_CLIPS clips, una sesión"
mkdir -p "$OUT/scene"
python3 "$RUNNER" --fase scene --clips "$CLIPS" --out-dir "$OUT/scene" \
  || fatal "la fase scene falló (ver $OUT/scene/resultados.json)"

# ── 4. determinismo contra la gen. 2 ──────────────────────────────────────────
paso "4. determinismo vs gen. 2 (doc 109) en los clips que ya estaban"
python3 - "$OUT/scene/resultados.json" "$GEN2/scene/resultados.json" <<'PY'
import hashlib, json, sys
from pathlib import Path
MP = Path("/home/simonll4/projects/e-ovrt_media-plane/runs")

def mapa(p):
    p = Path(p)
    if not p.exists():
        return {}
    return {r["clip_id"]: r["media_run_id"] for r in json.loads(p.read_text())
            if r.get("media_run_id")}

def huella(run_id):
    f = MP / run_id / "detections.jsonl"
    h = hashlib.sha256()
    n = 0
    with f.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            d = json.loads(line)
            # solo la sustancia: frame + cajas. Ignora run_id/timestamps de pared.
            h.update(json.dumps([d.get("frame_index"), d.get("detections")],
                                sort_keys=True).encode())
            n += 1
    return h.hexdigest(), n

nuevo, viejo = mapa(sys.argv[1]), mapa(sys.argv[2])
comunes = sorted(set(nuevo) & set(viejo))
if not comunes:
    print("    (sin clips en común con la gen. 2 — nada que comparar)")
for c in comunes:
    a, na = huella(nuevo[c]); b, nb = huella(viejo[c])
    veredicto = "IDÉNTICO" if (a == b) else "DIFIERE"
    print(f"    {c}: {veredicto}  ({na} vs {nb} frames)")
    if a != b:
        print("      ⚠ la inferencia NO es reproducible entre sesiones: decirlo en el")
        print("        doc antes de comparar gen.2 con gen.3 clip a clip.")
nuevos = sorted(set(nuevo) - set(viejo))
if nuevos:
    print(f"    clips nuevos en esta gen.: {', '.join(nuevos)}")
PY

# ── 5. FASE SUBJECT (I2) ──────────────────────────────────────────────────────
paso "5. FASE SUBJECT (I2) — reusa las cajas de la fase scene (sin GPU)"
mkdir -p "$OUT/subject"
python3 "$RUNNER" --fase subject --clips "$CLIPS" --out-dir "$OUT/subject" \
    --scene-dir "$OUT/scene" \
  || fatal "la fase subject falló (ver $OUT/subject/resultados.json)"

# ── 6. agregación de las dos campañas ─────────────────────────────────────────
paso "6. agregación -> metrics.json (la gen. 2 queda al lado como metrics.gen2.json)"
for par in "scene:$I1" "subject:$I2"; do
  fase=${par%%:*}; dest=${par#*:}
  [ -d "$dest" ] || fatal "no existe la campaña $dest"
  [ -f "$dest/metrics.json" ] && [ ! -f "$dest/metrics.gen2.json" ] \
    && cp "$dest/metrics.json" "$dest/metrics.gen2.json"
  python3 datasets/scripts/bench/aggregate_clip_campaign.py \
      --evals-dir "$OUT/$fase" --gt-dir "$DS/datasets-videos/gt" \
      --campaign "$dest/campaign.yaml" --out "$dest/metrics.json" \
    || fatal "la agregación de $fase falló"
  echo "    -> $dest/metrics.json"
done

# ── 7. NIVEL A ────────────────────────────────────────────────────────────────
paso "7. Nivel A (estado por persona, stride 15) — estrato B y consolidado"
python3 - "$OUT/scene/resultados.json" "$DATOS/105-piloto-scene-clips/resultados.json" \
         "$OUT/runs-map-estratob.json" "$OUT/runs-map-consolidado.json" <<'PY'
import json, sys
from pathlib import Path
def mapa(p):
    p = Path(p)
    return ({r["clip_id"]: r["media_run_id"] for r in json.loads(p.read_text())
             if r.get("media_run_id")} if p.exists() else {})
b = mapa(sys.argv[1]); piloto = mapa(sys.argv[2])
Path(sys.argv[3]).write_text(json.dumps(b, indent=2))
Path(sys.argv[4]).write_text(json.dumps({**b, **piloto}, indent=2))
print(f"    runs-map: estrato B {len(b)} clips · consolidado {len(b)+len(piloto)}"
      f" (piloto {len(piloto)})")
PY
python3 datasets/scripts/bench/score_clip_person_state.py \
    --clips "$CLIPS" --runs-map "$OUT/runs-map-estratob.json" \
    --xml-dir "$BANK/annotations" --info-dir "$BANK/meta" \
    --out "$DATOS/110-nivel-a-estrato-b-gen3.json" --stride 15 \
  || fatal "Nivel A del estrato B falló"
CLIPS_CONS=$(python3 -c "
import json;m=json.load(open('$OUT/runs-map-consolidado.json'));print(','.join(sorted(m)))")
# El consolidado usa los dirs del LABORATORIO y no los del banco: los 4 clips del
# piloto están RETIRADOS del banco (_retired/piloto_2026-07-18/) y solo el lab tiene
# los 9 juntos, que es lo que --xml-dir/--info-dir exigen (un dir, no varios).
# Para los 5 del estrato B, lab y banco son BYTE A BYTE idénticos (verificado).
python3 datasets/scripts/bench/score_clip_person_state.py \
    --clips "$CLIPS_CONS" --runs-map "$OUT/runs-map-consolidado.json" \
    --xml-dir "$DS/datasets-videos/corrected" --info-dir "$DS/datasets-videos/clips" \
    --out "$DATOS/110-nivel-a-consolidado.json" --stride 15 \
  || echo "    ⚠ el consolidado falló. El de estrato B SÍ quedó — el consolidado se
      regenera aparte sin re-inferir nada."

# ── 8. cierre ─────────────────────────────────────────────────────────────────
paso "8. listo — qué quedó"
cat <<EOF
  evidencia cruda   : $OUT/{scene,subject}
  campañas          : $I1/metrics.json
                      $I2/metrics.json   (gen. 2 preservada en metrics.gen2.json)
  Nivel A           : $DATOS/110-nivel-a-estrato-b-gen3.json
                      $DATOS/110-nivel-a-consolidado.json
  clips de la gen. 3: $CLIPS

  A MANO, después (doc 110 §5):
   1. campaign.yaml de I1 e I2: agregar la entrada \`generations: gen 3\` con la
      fecha, los $N_CLIPS clips y el manifest sha nuevo; actualizar gt_bank/gt_note.
   2. results/clip_bench/index.md y results/index.md: las filas de I1/I2.
   3. registry/clip_bench.md §2.1: sacar el aviso de "v03_c02 en ninguna campaña".
   4. docs/operacion/110: pegar las cifras y cerrar §4.
EOF
