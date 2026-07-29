# 77 — Secuencia git de cierre (receta para el usuario)

- **Última actualización:** 2026-07-29
- **Propósito:** la secuencia exacta, repo por repo, para saldar la deuda git del
  doc 75 §3.1: commitear el trabajo del 29/07, llevar `main` al estado que se
  defiende, respaldar la rama huérfana y borrar `mati`. **Todo esto lo ejecutás
  vos** (regla vigente: Claude no commitea ni pushea). Los mensajes de commit son
  sugerencias — sin `Co-Authored-By`.
- **Precondición:** las suites están verdes al 2026-07-29 (datasets 188 /
  control-plane 251 / BFF 586). Si tocás algo antes de commitear, re-corré la del
  repo tocado.

## 0. Qué hay sin commitear en cada repo (foto 2026-07-29)

| Repo | Rama actual | Sin commitear |
|---|---|---|
| datasets | `feature/datasets-v2-setup` | correctitud (person_gt curado, freeze verificable, evaluate_bench), `build_clip_bench`, kit auditoría, registries/documentation |
| control-plane | `feature/control-service` | deprecación v1 + migración replay_dbe, ADRs 0006–0012 nuevos, `progress.md`, reporte reubicado a `docs/reportes/` |
| experimental-setup | `feature/webconsole-consola-tesis` | congelamiento edir/eind + safety_vest, espejo `comparative`, cableado FAR/censura en `report.py` (+gate v1), `docs/prompt-sets.md`, README |
| media-plane | `feature/inference-service` | `CLAUDE.md` (3.12), `docs/implementation-status.md` actualizado |
| docs | `main` (sin remote) | docs 75/76/77, índice, GUIA-CIERRE §4 |

## 1. datasets

```bash
cd ~/projects/e-ovrt_datasets
python3 -m pytest datasets/tests/ -q          # esperado: 188 passed
git add -A && git commit -m "fix(bench): person_gt curado, freeze verificable, denominadores CR-01/FAR y ensamblador clip_bench"
git checkout main && git merge feature/datasets-v2-setup
git push origin main && git push origin feature/datasets-v2-setup
git checkout feature/datasets-v2-setup        # volver a la rama de trabajo
```

## 2. control-plane

```bash
cd ~/projects/e-ovrt_control-plane
.venv/bin/python -m pytest -q --ignore=tests/labs   # esperado: 251 passed
git add -A && git commit -m "docs+config: deprecar pattern set v1, migrar replay_dbe a v2, ADRs 0006-0012 y progress"
git checkout main && git merge feature/control-service
git push origin main && git push origin feature/control-service
# mati está 100% integrada (verificado: ancestro de HEAD, 0 commits exclusivos)
git branch -d mati && git push origin --delete mati
git checkout feature/control-service
```

## 3. experimental-setup

```bash
cd ~/projects/e-ovrt_experimental-setup
( cd webconsole/backend && .venv/bin/python -m pytest -q )   # esperado: 586 passed
git add -A && git commit -m "feat(report)+prompts: congelar edir_v1/eind_v1 (acta 76), FAR/censura al reporte con gate v1, docs veraces"

# PRIMERO el respaldo de la rama huérfana (88 commits SOLO locales, riesgo de pérdida):
git push origin feature/webconsole-rediseno-fundacion

# El worktree residual (sus 11 untracked ya están commiteados en la rama tesis — verificado 07-28):
git worktree remove --force .worktrees/rediseno-fundacion-corridas

git checkout main && git merge feature/webconsole-consola-tesis
git push origin main && git push origin feature/webconsole-consola-tesis
git checkout feature/webconsole-consola-tesis
```

## 4. media-plane (incluye la decisión de la rama perf)

La rama `perf/producer-pil-roundtrip` = `feature/inference-service` + 1 commit
(`3deb64c`, F-RT5: +18% fps, −14,4% latencia, p=0,0195, salida byte-idéntica → no
exige re-validar mAP; doc 73 §10). **Mergearla es la recomendación registrada**; si
preferís no hacerlo, saltá esas dos líneas y el resto vale igual.

```bash
cd ~/projects/e-ovrt_media-plane
git add -A && git commit -m "docs: implementation-status al día (646 tests, features de julio) y venv 3.12"

git merge perf/producer-pil-roundtrip          # fast-forward (estás en feature/inference-service)
git worktree remove .claude/worktrees/pil-roundtrip
git branch -d perf/producer-pil-roundtrip && git push origin --delete perf/producer-pil-roundtrip

git checkout main && git merge feature/inference-service
git push origin main && git push origin feature/inference-service
git checkout feature/inference-service
make test                                       # suite completa post-merge (F-RT5 trae 9 tests propios)
```

Nota: `main` local ya tenía 17 commits no pusheados de julio — el `push origin main`
de arriba los sube junto con el merge.

## 5. docs (sin remote — backup a otro disco)

```bash
cd ~/projects/docs
git add -A && git commit -m "operacion: 75 (pendientes de cierre), 76 (acta edir/eind), 77 (secuencia git)"
# Backup completo del repo a otro disco (decisión vigente: sin remote en GitHub):
git bundle create /ruta/al/otro/disco/docs-2026-07-29.bundle --all
git bundle verify /ruta/al/otro/disco/docs-2026-07-29.bundle
```

## 6. Verificación final (2 min)

```bash
for r in e-ovrt_datasets e-ovrt_control-plane e-ovrt_experimental-setup e-ovrt_media-plane; do
  echo "== $r"; git -C ~/projects/$r status -sb; git -C ~/projects/$r log origin/main..main --oneline | wc -l
done
# esperado: working trees limpios y 0 commits locales sin pushear sobre origin/main
```

Con esto, quien clone `origin/main` de cualquiera de los 4 repos obtiene el sistema
que se defiende, y el doc 75 §3.1 queda saldado.
