"""Auditoría de cumplimiento del diseño de organización del doc 109.

Verifica las reglas que el doc 109 §2 fijó, contra el estado real del disco. No
asume nada: cada regla se comprueba.
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

P = Path('/home/simonll4/projects')
DS = P/'e-ovrt_datasets'; BANK = DS/'datasets/processed/clip_bench'
LAB = DS/'datasets-videos'; RES = P/'e-ovrt_experimental-setup/results'
fallos = []


def check(cond, regla, detalle=""):
    print(("  ok   " if cond else "  FAIL ") + regla + (f"  — {detalle}" if detalle else ""))
    if not cond:
        fallos.append(regla)


print("== R1. Tres estratos de material, cada uno en su lugar")
man = yaml.safe_load((BANK/'manifest.yaml').read_text())
por_bloque = {}
for c in man['clips']:
    por_bloque.setdefault(c['block'], []).append(c['clip_id'])
check(len(por_bloque.get('A', [])) == 34, "Bloque A = 34 clips del rodaje",
      f"{len(por_bloque.get('A', []))}")
check(len(por_bloque.get('B', [])) == 13, "Bloque B = 13 clips del lote",
      f"{len(por_bloque.get('B', []))}")
piloto = list((BANK/'_retired/piloto_2026-07-18/gt').glob('*.json'))
check(len(piloto) == 4, "Piloto = 4 clips, fuera del banco, en _retired/", f"{len(piloto)}")
check(not any(c['clip_id'].startswith('video') for c in man['clips']),
      "ningún clip piloto se coló al banco de Nivel B")

print("\n== R2. Campaña citable vs evidencia exploratoria (doc 109 §2.2)")
for camp in sorted((RES/'clip_bench').iterdir()):
    if not camp.is_dir():
        continue
    faltan = [f for f in ('campaign.yaml', 'metrics.json') if not (camp/f).exists()]
    check(not faltan, f"campaña {camp.name} tiene sus artefactos", f"faltan {faltan}" if faltan else "")
expl = list((P/'docs/operacion/datos').glob('10*-*'))
check(not any((d/'campaign.yaml').exists() for d in expl if d.is_dir()),
      "ninguna carpeta exploratoria se disfraza de campaña")

print("\n== R3. Fuente de verdad de las anotaciones (registry §2.2)")
check((BANK/'annotations').is_dir(), "annotations/ del banco existe")
r = subprocess.run(['git', 'check-ignore', '-q', str(LAB/'corrected')], cwd=DS)
check(r.returncode == 0, "datasets-videos/corrected/ está gitignorado (es working copy)")
con_corr = [p for p in (BANK/'meta').glob('*.clip.yaml')
            if 'attribute_corrections' in p.read_text()]
for m in con_corr:
    cid = m.name.replace('.clip.yaml', '')
    rc = subprocess.run([sys.executable, str(DS/'datasets/scripts/videogt/apply_attribute_corrections.py'),
                         '--xml', str(BANK/'annotations'/f'{cid}.xml'),
                         '--clip-yaml', str(m), '--check'],
                        capture_output=True, cwd=DS).returncode
    check(rc == 0, f"correcciones firmadas de {cid} aplicadas en el banco")

print("\n== R4. Integridad lab ↔ banco")
import hashlib
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
desalineados = []
for c in por_bloque.get('B', []):
    a, b = LAB/'corrected'/f'{c}.xml', BANK/'annotations'/f'{c}.xml'
    if a.exists() and b.exists() and sha(a) != sha(b):
        desalineados.append(c)
check(not desalineados, "corrected/ del lab == annotations/ del banco", f"{desalineados}")
gt_desal = [c for c in por_bloque.get('B', [])
            if json.loads((BANK/'gt'/f'{c}.json').read_text())['provenance']['xml_sha256']
            != sha(BANK/'annotations'/f'{c}.xml')]
check(not gt_desal, "provenance.xml_sha256 de cada GT == su XML del banco", f"{gt_desal}")

print("\n== R5. Exclusiones declaradas, nunca silenciosas")
excl = [p for p in LAB.glob('v*.clip.yaml') if 'excluded: true' in p.read_text()]
sin_gt = [p.name.replace('.clip.yaml', '') for p in LAB.glob('v*.clip.yaml')
          if not (LAB/'gt'/p.name.replace('.clip.yaml', '.json')).exists()]
check(len(sin_gt) == len(excl),
      "todo clip del lote sin GT tiene su exclusión declarada",
      f"sin GT: {sin_gt} | declarados: {[p.name for p in excl]}")
for p in excl:
    y = yaml.safe_load(p.read_text())
    check(all(k in y for k in ('excluded_reason', 'excluded_by', 'excluded_at')),
          f"{p.name} declara causa, firma y fecha")

print("\n== R6. El banco es reportable y verificable")
cbm = json.loads((BANK/'clip_bench_manifest.json').read_text())
check(cbm['reportable'] is True, "banco reportable")
check(cbm['manifest_yaml_sha256'] == sha(BANK/'manifest.yaml'),
      "sha del manifest.json == manifest.yaml real")
r = subprocess.run(['sha256sum', '-c', 'clip_bench.sha256'], cwd=BANK, capture_output=True, text=True)
check(r.returncode == 0, f"freeze verificado ({r.stdout.count(': OK')} archivos)")

print()
if fallos:
    print(f"❌ {len(fallos)} regla(s) incumplida(s):")
    for f in fallos:
        print("   -", f)
    sys.exit(1)
print("✅ la organización del doc 109 se cumple en todos sus puntos")
