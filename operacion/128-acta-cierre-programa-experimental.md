# 128 — Acta de cierre del programa experimental E-OVRT-VDP (2026-08-21)

- **Qué es:** la declaración formal, pedida por el usuario el 2026-08-21, de que **el
  programa experimental de la tesis está COMPLETO**: no queda ningún experimento abierto,
  en cola ni diferido-con-retorno. Lo que resta hasta la defensa es **verificación de
  plataforma, procedencia, material de defensa y redacción** — nada que produzca una cifra
  nueva. Esta acta reemplaza a `operacion/121` como **foto de estado vigente** (aquella
  sigue siendo válida como registro del 08-15, con la salvedad de que su §2/§3 sobre
  fine-tuning quedó superado por los docs 123 y 127).
- **Criterio heredado del doc 119:** ninguna fila sin comando corrido. Las verificaciones
  del §3 se ejecutaron hoy, 2026-08-21.
- **Marco de lectura (doc 62):** los números son EL DATO de una combinación bajo un
  protocolo, no un aprobado/fallado. Un NO-GO pre-registrado es un resultado.

---

## 1. El mapa completo: todo frente experimental, su constancia y su salida citable

| Frente | Estado | Constancia | Salida citable |
|---|---|---|---|
| Selección de modelos S1/S2 | ✅ cerrado 07-23 | doc 64 | campeón `gdino-tiny-560` (mejor mAP50 en núcleo curado Y bench completo); `gdino-base-560` especialista CR-01 |
| Bench de imágenes `bench_v3` | ✅ congelado 07-23, regenerable byte a byte desde 08-19 | docs 63/66/126; manifiesto con sha256 por fuente | 6.477 imgs / 3 fuentes independientes; métricas SIEMPRE por estrato + agregado |
| Rodaje (bloques A+B, EBE live) | ✅ cerrado 07-25 | doc 71 | 6 corridas live, `bus_dropped_events = 0` |
| GT de video (rodaje) | ✅ cerrado 08-03 | doc 80 | 34 clips / 35 episodios (34 evaluables); GT humano ⇒ se reporta como RESULTADO |
| Ejes E-DIR/E-IND (prompts congelados) | ✅ acta 07-29 | doc 76 | `edir_v1`/`eind_v1` frozen con sha256; F-83.6 (E-DIR recupera 18,5 %) |
| Cadena T→P→D (campañas del banco) | ✅ cerrado 08-05 | docs 83–90, 92, 98 | **cifras = SOLO los 4 índices de `experimental-setup/results/`**; G1 0,930 el mejor del banco; E-IND 0,789; conclusiones = escala AF-1…AF-11 (doc 98) |
| Lote de internet (estrato B) + revisión ciega | ✅ cerrado 08-09 | docs 102→113 | banco vigente 32/15/47 (manifest `3f14f50a…`); la revisión ciega tumbó 5/7 declaraciones de episodio y quedó documentada |
| Costo del tiempo real (R1–R6) | ✅ cerrado | doc 96 | F-96.4: la ganancia de la identidad excluye el cero en las 4 densidades |
| EBE blindado (claqueta, hardware real) | ✅ cerrado 08-05, **no se re-rueda** | doc 101 | F-101.8: G2A se mide desde el dequeue; vidrio→alerta = `capture_to_host` + G2A |
| Distribución de alertas (spec 45) | ✅ implementada y verificada 08-12/18 | docs 114/118/124/125; ADR-016/019/020 | MQTT QoS 1 + ledger; p95 64,534 ms (n=460); servicio HTTP `:8082` |
| **Fine-tuning — jornada E-04 completa** | ✅ **cerrada 08-21** | docs 100/117/120/**123**/**127**; ADR-017 | T1 NO-GO · T2 NO-GO · T3 causa técnica; **curva capacidad/retención de 3 puntos**; F-127.1 (estructural, no capacidad) y F-127.2 (erosión OV global) |
| Deploy integral (13 servicios, Compose) | ✅ definido y validado por config | doc 126 | ⚠ **builds + smoke integral PENDIENTES** — ver §4; es verificación de plataforma, no experimento |

## 2. Por qué no queda ningún experimento que valga la pena correr

Recorrido explícito de los caminos restantes, cada uno con su causa (detalle en doc 127 y
en la conversación de cierre del 08-21):

1. **Más brazos de fine-tuning** (tercer LR, tier intermedio, run largo del `auto`):
   erosionan la pre-registración (serían ajuste post-hoc tras ver dos fallos), responden
   una pregunta que ya está respondida desde dos direcciones (F-127.1), y el análisis
   F-127.2 muestra que el mecanismo de fallo es deriva global — no lo corrige un
   optimizador. **T2 fue el último brazo contra `bench_v3` por firma previa.**
2. **Más datos de entrenamiento**: `shel5k`/`chv` son estratos del bench (usarlos
   contamina el instrumento) y recolectar es semanas. Es exactamente la causa
   "condicionada por datos" de ADR-017 — fortaleza del relato, no hueco.
3. **PEFT/LoRA**: el paso correcto de un programa de investigación posterior — **trabajo
   futuro con causa real**, documentable sin correrlo (§18/19 del informe).
4. **Re-correr campañas del banco / nuevas combinaciones**: los congelamientos son
   explícitos (banco 47, GT humano, EBE "no se re-rueda") y ninguna cifra pendiente
   cambia una conclusión (doc 98 §7).
5. **Nuevos modelos al catálogo**: la selección S1/S2 cerró con criterio pre-registrado;
   reabrirla es otro proyecto.

## 3. Verificaciones ejecutadas hoy (2026-08-21)

| Verificación | Comando | Resultado |
|---|---|---|
| Cifras citables (4 índices + procedencia) | `python3 operacion/datos/96-verificar-indices.py` | ✅ "Todo verificado" (35 docs de procedencia presentes) |
| Project kit vigente | `python3 herramientas/generar_project_kit.py --check` | ✅ OK (regenerado hoy tras la propagación del cierre T2) |
| Suite de finetuning | `pytest finetuning/tests/` | ✅ 46 passed |
| Evaluaciones T2 (one-shot) | evaluadores congelados con sha256 de TODOS los insumos | ✅ ambas corridas con cobertura completa y 0 errores (doc 127 §3) |
| Backup evidencia T2 | `sha256sum -c MANIFEST.sha256` (27 archivos) | ✅ limpio |

Suites de referencia previas (no re-corridas hoy; última foto en doc 97 y CRONOLOGIA):
plataforma 2.203 tests al 08-15, webconsole backend 643, experimental-setup 88.

## 4. Qué queda hasta la defensa — y de quién es

**Nada de esta lista produce una cifra experimental nueva.** En orden sugerido:

✎ **2026-08-21 (segunda decisión del usuario): el informe va primero.** Todo lo que no
sea redactar el informe —smoke integral de Docker, C1, V2, latencia pareada— se difiere
**a después de la entrega**, para la ventana en que se esperan las correcciones del
jurado. La lista queda reordenada en consecuencia:

| # | Ítem | Tipo | Dueño | Cuándo |
|---|---|---|---|---|
| 1 | **F — pase de redacción**: aplicar las unidades AJ-*/R-*/PODA sobre el entregable | redacción | usuario + colegas + Claude | **AHORA — es el único frente activo** |
| — | *(insumos de redacción: todos cerrados)* | — | — | ✅ datos, decisiones, **materiales: 17 tablas + 6 figuras**, kit regenerado |
| 2 | **Builds + smoke integral de `infra/platform`** (13 servicios; daemon Docker apagado) | verificación de plataforma | usuario enciende Docker + sesión conjunta (⚠ disco/WSL: doc 126, nunca Capa 3 autónoma) | post-entrega |
| 3 | **C1** — URLs y licencias de los 18 `clip.yaml` | procedencia | usuario | post-entrega (⚠ no borrar `scripts/downloads/` antes) |
| 4 | **E** — video de defensa V2 | material de defensa | usuario | post-entrega |
| 5 | Latencia pareada de los 3 brazos FT (con corriente) | dato descriptivo **opcional** | usuario decide | post-entrega; no cambia ningún veredicto |
| 6 | Commits/push del cierre del 08-21 | git | usuario | cuando quiera |

**Materiales del informe — cerrados el 2026-08-21.** Las cinco figuras que faltaban
(`FIG-A` §17.4.1 · `FIG-B`, `FIG-C`, `FIG-F` §17.5 · `FIG-E` §17.3.8.2) están producidas
en [`informe/figuras/`](../informe/figuras/README.md), en PNG 300 dpi + SVG, con
generadores reproducibles que leen del artefacto y fallan si la cifra no coincide con el
índice publicado. Con las 17 tablas —que ya estaban en disco— **no falta ningún material
para redactar**. Tres advertencias de cita quedaron registradas en ese README: el módulo
de distribución va en línea **continua** (la nota al pie de `94` §4 quedó falsa), el
**orden de arranque es el inverso del flujo de datos**, y la máquina de estados tiene
**cinco** estados con la reapertura hacia `candidate`.

## 5. Regla de salida

Desde esta acta, **cualquier experimento nuevo requiere reapertura explícita** con nueva
pre-registración (el mecanismo que D-FT-14 demostró viable) — no se reabre por deriva. La
energía del proyecto pasa entera al informe: las decisiones están en los ADR (serie
proyecto 001…020) y el tablero 117; los experimentos en sus constancias (§1); los
resultados en los 4 índices y la síntesis. El informe se redacta **autocontenido** (GUIA
§3.1): esta acta es para los redactores y la defensa, nunca una referencia citada en el
texto entregable.
