# Diseño comparativo de estrategias de detección: E-DIR vs E-IND (y convergencia)

- **Fecha:** 2026-07-06
- **Estado:** Investigación documental para decisión de núcleo (pre-registro del experimento)
- **Decisión que resuelve:** §9.1 de `02-revision-critica-etapa3-y-norte.md` — qué estrategia de detección es el núcleo validable para CR-01/CR-02
- **Referencias:** Etapa 3 §17.3.6.4 (Tabla 45), §17.3.8.3.3 (Tabla 47), §17.3.9.2; Sprint 2 (eval BENCH v2); relevamiento control-plane 2026-07-06

## 1. Objetivo y encuadre

Existen dos formas de producir la evidencia que alimenta los patrones PR-01/PR-02:

- **E-DIR** — el detector OVD responde directamente la pregunta de riesgo mediante
  prompts de ausencia o estado ("person without hard hat", "person with bare head").
  Es la estrategia que §17.3.9.2 adopta como núcleo.
- **E-IND** — el detector solo produce evidencia positiva (person, helmet, vest) y el
  plano de control **infiere** la ausencia espacialmente (¿hay casco cuyo centro caiga
  en la región superior del bbox de la persona?). Es la estrategia implementada y
  testeada en `e-ovrt_control-plane`.

Este documento desarrolla ambas documentalmente — fundamento, evidencia previa,
riesgos, requisitos — define una tercera vía de convergencia (E-HYB), y pre-registra
el protocolo y los criterios con los que se decidirá. La decisión final se toma con
datos, no por argumento, y queda registrada como ADR en el repo que corresponda.

**Qué NO está en discusión:** todo lo demás es común a ambos caminos — pipeline de
medios, contratos, bus, máquina de estados del patrón, métricas, EBE, distribución.
La estrategia es un punto de enchufe: prompt set (media-plane) + evaluador
(control-plane). Por eso la comparación es barata y no requiere dos ramas de código.

## 2. Dónde se enchufa cada estrategia (marco común)

```
                     media-plane                          control-plane
              ┌───────────────────────┐            ┌──────────────────────────┐
 prompt set ─►│ inferencia OVD        │─ eventos ─►│ evaluador ──► PatternEngine
              │ (vocabulario activo)  │            │ (produce PatternEvidence) │
              └───────────────────────┘            └──────────────────────────┘

 E-DIR: prompt set = frases de ausencia/estado   evaluador = direct_evidence (trivial)
 E-IND: prompt set = clases positivas            evaluador = spatial_absence (existe)
 E-HYB: prompt set = unión de ambos              evaluador = fusión (OR / votación)
```

La máquina de estados (candidate→confirmed→…), la histéresis, las alertas y las
métricas son idénticas en los tres casos: lo único que cambia es **cómo se genera la
`PatternEvidence`** de cada unidad visual.

## 3. Camino A — E-IND (evidencia positiva + inferencia espacial)

### 3.1 Fundamento

Descompone la condición en detecciones que los modelos OVD hacen bien (objetos
concretos: persona, casco, chaleco) y traslada la semántica de "ausencia" a una regla
geométrica explícita y auditable. La consulta al modelo nunca contiene negación.

### 3.2 Fortalezas

1. **Evita la debilidad de negación de los VLM** (ver §4.3): solo pide conceptos
   positivos, que es el régimen donde CLIP/GDINO fueron entrenados.
2. **Evidencia auditable y explicable**: la alerta se reconstruye como "persona en
   bbox X, región superior Y, ninguna detección de casco con centro en Y". Encaja
   con el requisito de trazabilidad causal (§17.3.9.3) mejor que un score opaco.
3. **Umbrales separables**: confianza de sujeto y de EPP se calibran por separado
   (ya parametrizado: `min_subject_confidence`, `min_absent_class_confidence`).
4. **Vocabulario activo chico y estable** (3 clases + alias), alineado con la
   recomendación del doc de mantener vocabulario reducido (§17.3.6.3).
5. **Ya implementada y testeada** (evaluador `spatial_absence`, 9/9 tests, fixture
   temporal validado con P/R/F1 = 1.0 en el caso sintético).
6. Reutiliza directamente el vocabulario canonical_v2 del repo datasets → el BENCH
   v2 puntúa sus insumos (AP de person/helmet/vest ya medidos en Sprint 2).

### 3.3 Debilidades y riesgos

*Actualización 2026-07-09:* la rama `mati` del control-plane (doc 01 §12) mitigó las
debilidades 1 y parte de 2 — matching bipartito 1:1 (elimina el robo de EPP entre
personas superpuestas), región adaptativa por pose (agachado/inclinado) y memoria de
cobertura (parpadeo/oclusión breve). **El experimento D1 debe correr con este motor**;
lo que sigue describe el estado previo y se conserva como registro de los modos de
falla que el diseño ya ataca.

1. **La regla espacial es una heurística**: región por ratios fijos del bbox. Falla
   esperable con posturas no erguidas (agachado, sentado), oclusiones parciales,
   personas truncadas por el borde del frame, ángulos cenitales, y solapamiento de
   personas (el casco de B cae en la región de A → falso negativo de CR-01 para A).
2. **Doble dependencia**: necesita que el modelo detecte bien *dos* clases. Si el
   recall de `vest` es bajo, E-IND produce falsos positivos de CR-02 (chaleco no
   detectado ⇒ "sin chaleco"). El falso negativo del EPP se convierte en falso
   positivo de la alerta — asimetría que hay que medir explícitamente.
3. Los ratios de región (upper_body 0–0.45, torso 0.25–0.85) están sin calibrar
   contra datos reales (pendiente declarado del repo).
4. No aprovecha nada de la capacidad open-vocabulary "composicional" del modelo —
   crítica posible del tribunal: "¿para esto necesitabas OVD?". Respuesta
   preparada: el OVD aporta el vocabulario sin reentrenar y la extensibilidad de
   condiciones; la composición semántica se demuestra justamente en E-DIR/R2.

### 3.4 Evidencia previa a favor

- Sprint 2: `person` y `helmet` con AP razonable en GDINO-tiny (mejor mAP global
  0.441); los insumos de E-IND son las clases *fuertes* del benchmark.
- La implementación completa existe; el riesgo de ejecución es ~cero.

### 3.5 Qué necesita para ser evaluada con rigor

- Scoring de **alertas** (no solo detecciones) sobre imágenes BENCH usando los
  atributos `has_helmet`/`has_vest` del GT a nivel persona (ya existen en el split
  BENCH): para cada persona GT, ¿E-IND predice bien su estado de EPP?
- Calibración de ratios/umbrales sobre la mitad de calibración de BENCH (ver §7 Fase 1, paso 3).
- Análisis de los modos de falla 3.3.1–3.3.2 con ejemplos concretos.

## 4. Camino B — E-DIR (prompts directos de ausencia / estado observable)

### 4.1 Fundamento y variantes

Usa la capacidad visión-lenguaje del OVD para consultar directamente la condición.
Dos sub-variantes que conviene tratar por separado porque tienen mecánica distinta:

- **E-DIR-neg** — negación explícita: "person without hard hat", "worker without
  reflective vest" (Tabla 45, eje "prompt directo de ausencia").
- **E-DIR-obs** — estado observable sin negación: "person with bare head on
  construction site", "person without bright colored safety clothing" → en la
  práctica, la clase `bare_head` del canonical_v2 es la materialización de esta
  variante para CR-01.

### 4.2 Fortalezas

1. **Simplicidad del plano de control**: la detección *es* la evidencia; el
   evaluador se reduce a filtrar por label+confianza (sin geometría, sin doble
   umbral, sin heurística de región).
2. **Es la promesa open-vocabulary en su forma más pura**: si funciona, es el
   resultado más interesante de la tesis ("el modelo entiende la condición").
3. Robusta a los modos de falla geométricos de E-IND (posturas, solapamiento):
   el modelo ve a la persona completa en contexto.
4. Extensible en el papel a condiciones que no se descomponen bien espacialmente.

### 4.3 Debilidades y riesgos

1. **Negación en VLMs — el riesgo central de E-DIR-neg.** La literatura converge en
   que los modelos contrastivos tipo CLIP (base de GDINO/YOLOE) tratan el texto
   como "bolsa de conceptos": son insensibles a orden y estructura (Yuksekgonul et
   al., 2023 — benchmark ARO, "bag-of-words behavior") y fallan sistemáticamente
   con negación (Alhamoud et al., 2025 — NegBench, "VLMs do not understand
   negation"; también VALSE, Parcalabescu et al., 2022, probing de existencia).
   Predicción concreta: "person without hard hat" activa los conceptos *person* y
   *hard hat* → riesgo de detectar justamente a las personas CON casco, o a todas.
   *(Verificar citas exactas antes de usarlas en el informe.)*
2. **Evidencia empírica propia ya en contra de E-DIR-obs**: Sprint 2 midió
   `bare_head` (la variante estado-observable) débil en los 5 modelos evaluados
   sobre BENCH v2. Es el dato más duro que existe hoy en esta comparación.
3. **Score no calibrable por componente**: un solo umbral opaco por frase; no se
   puede distinguir "no vio a la persona" de "no entendió la negación".
4. **Evidencia difícil de auditar**: la justificación de la alerta es "el modelo
   dijo 0.34 para esta frase" — más débil ante el requisito de reconstrucción
   causal del propio doc.
5. Vocabulario activo más grande (frases por condición + variantes) → más costo de
   inferencia en GDINO (tokens de texto) y más varianza entre formulaciones.

### 4.4 Evidencia previa

- En contra: Sprint 2 / `bare_head`; literatura de negación.
- A favor: no se probaron aún las formulaciones de negación de la Tabla 45 tal cual
  (Sprint 2 evaluó clases del vocabulario canónico, no frases compuestas). El doc
  merece que su estrategia se pruebe con sus propias formulaciones antes de
  descartarla — ese es precisamente el experimento.

### 4.5 Qué necesita para ser evaluada

- **Prompt set E-DIR** en `experimental-setup/prompts/` con las formulaciones de la
  Tabla 45 (CR-01: 3 ejes; CR-02: 3 ejes), versionado (costo: ~0, es YAML).
- **Scoring sobre BENCH** con los atributos por persona, con **matching por
  variante** (corrección de auditoría, ver doc 07/H1): las frases persona-céntricas
  ("person without hard hat") se matchean por IoU≥0.5 contra personas GT; las
  detecciones de parte (`bare_head` y equivalentes) se asocian si su **centro cae
  dentro de la región superior** del bbox de la persona — un IoU contra la persona
  completa las descartaría estructuralmente y sesgaría el experimento contra
  E-DIR-obs. Reutiliza `evaluate_bench.py`/`person_gt.json` con un mapeo de labels
  nuevo (trabajo chico en el repo datasets).
- **Evaluador `direct_evidence`** en el control-plane (~50 líneas: label match +
  umbral → `PatternEvidence`) para poder correr la cadena completa y comparar
  alertas — solo se construye si E-DIR sobrevive al scoring de detección.

## 5. Camino C — E-HYB (convergencia)

El usuario de las dos evidencias no es el detector sino el **patrón**: nada impide
que PR-01 acepte evidencia de ambas fuentes. Tres diseños de fusión, de menor a
mayor complejidad:

1. **E-HYB-or (unión):** la evidencia del patrón es válida si proviene de E-IND
   **o** de E-DIR (detección "person without helmet"/"bare_head" matcheada por IoU
   con el sujeto). Sube recall, baja precisión; la histéresis temporal filtra parte
   del ruido extra.
2. **E-HYB-and (confirmación cruzada):** E-IND es la señal primaria; una detección
   E-DIR concordante **acelera la confirmación** (p.ej. reduce `confirm_after_ms`)
   o refuerza el score del episodio. Sube precisión sin sacrificar el recall de
   E-IND. Es el diseño más defendible conceptualmente: "la heurística espacial
   decide, la señal semántica corrobora".
3. **E-HYB-vote (ponderación):** score del sujeto = combinación ponderada de ambas
   señales con pesos calibrados. Más potencia estadística, más difícil de explicar
   y calibrar con el tiempo disponible — **solo si los datos de la fase 1 muestran
   que las señales son complementarias** (errores no correlacionados).

E-HYB no es un tercer desarrollo: es configuración del patrón + una función de
fusión en el evaluador. Se decide *después* de ver los resultados individuales:
si E-DIR resulta inútil, E-HYB muere solo; si E-DIR es débil pero complementaria,
E-HYB-and es probablemente la conclusión del capítulo.

> **Ajuste 2026-07-09 (decisión del usuario, ADR-001):** E-HYB-or/and se corren en
> la Fase 2 **siempre** como rama experimental de primera clase — el umbral de
> complementariedad (>15%) deja de ser condición de ejecución y pasa a predicción a
> contrastar. E-HYB-vote sigue excluida (E-13). Los criterios de adopción del §8
> no cambian. **La bajada operativa completa está en el doc 12**: mecánica dual-run
> (fusión de corridas separadas, no vocabulario unión), gating por persona de la
> señal E-DIR, funciones de fusión pre-registradas (or / and con factor de ventana
> de confirmación) y medición en tres niveles.

## 6. Evidencia disponible hoy (punto de partida, no conclusión)

| Evidencia | Fuente | Lectura |
|---|---|---|
| GDINO-tiny mejor mAP (0.441) sobre BENCH v2; person/helmet detectables | Sprint 2 | Los insumos de E-IND son viables con el modelo elegido. |
| `bare_head` débil en los 5 modelos | Sprint 2 | E-DIR-obs parte con evidencia en contra para CR-01. |
| YOLOE-26l rápido pero sin vest/bare_head | Sprint 2 | Si el modelo final fuera YOLOE, E-DIR queda casi descartada y E-IND pierde CR-02 → refuerza a GDINO como baseline. |
| Fixture temporal sintético: P/R/F1 = 1.0 con E-IND | control-plane | La cadena E-IND funciona end-to-end (con identidad sintética). |
| Formulaciones E-DIR sin probar tal cual | Tabla 45 | El experimento tiene valor real; no está pre-decidido. |
| Literatura de negación en VLMs | ARO/NegBench/VALSE | Prior fuerte contra E-DIR-neg; citable en el informe. |

**Prior honesto:** E-IND parte como favorita (implementación + evidencia + literatura).
El experimento existe para (a) darle a E-DIR la oportunidad justa con sus propias
formulaciones, (b) cuantificar la brecha para el informe, y (c) detectar
complementariedad que habilite E-HYB. Cualquiera de los tres desenlaces es un
capítulo de resultados válido.

## 7. Protocolo experimental (pre-registrado)

**Time-box total: 2 semanas** de esfuerzo experimental (*✎ ADR-010: ya no es un
bloque contiguo de calendario — la Fase 1 corre en el tramo plataforma apenas
exista `edir_v1`; las Fases 2–3 corren en el tramo de evaluación, con el clip
bench*). Variables fijas en todas las
corridas: modelo (GDINO-tiny como baseline; opcional repetir con GDINO-base),
fuente (BENCH v2, 196 imgs), resolución, postproceso, umbrales de NMS. Variable
única: estrategia/prompt set (regla de comparabilidad §17.3.6.5).

### Fase 1 — Scoring de detección/estado sobre BENCH (días 1–4)

1. Cargar prompt set `edir_v1` (formulaciones Tabla 45, CR-01 y CR-02, 2–3 variantes por eje).
2. Correr BENCH con `eind_v1` (canonical: person/helmet/vest) y `edir_v1`.
3. **Partición calib/test:** los atributos por persona solo existen en BENCH, así
   que se divide BENCH en mitades estratificadas — umbrales/regiones se calibran en
   la mitad A y **todo lo reportado sale de la mitad B** (declarado en la config de
   corrida). No se calibra y evalúa sobre lo mismo.
4. Puntuar **a nivel persona** contra `has_helmet`/`has_vest`:
   - E-IND: aplicar `spatial_absence` offline sobre las detecciones → estado predicho por persona.
   - E-DIR: matching por variante (IoU≥0.5 para frases persona-céntricas; centro-en-región-superior para detecciones de parte como `bare_head`) → estado predicho.
5. Métricas por condición: precision/recall/F1 del estado "sin EPP", + curvas por umbral.
   **Reportar los conteos** de la clase positiva (personas sin casco / sin chaleco en
   la mitad de test) e intervalos por bootstrap: si n<30 por condición, el umbral de
   empate técnico del §8 se considera dentro del ruido y la Fase 2 (clips) pesa más
   en la decisión.
6. Análisis de errores: ¿los FP/FN de ambas estrategias caen en las mismas personas? (mide complementariedad para E-HYB).
7. Atajo: las corridas de Sprint 2 sobre BENCH pueden reutilizarse desde `runs/` para
   el scoring de E-IND sin re-inferir; solo `edir_v1` requiere inferencia nueva.

**Gate (ajustado 2026-07-09, ADR-001):** si el F1 de E-DIR < 50% del F1 de E-IND en
ambas condiciones, E-DIR se declara no viable **como candidata a núcleo** y se
documenta. La Fase 2 corre E-IND **más las fusiones E-HYB-or/and como rama
experimental en todos los casos** (valor de tesis R2); la complementariedad de
Fase 1 (>15% de los errores de E-IND recuperados por E-DIR) se reporta como
predicción contrastada, no condiciona la ejecución. Como candidata a *núcleo*,
E-HYB sigue atada a los criterios del §8.3.

### Fase 2 — Cadena completa sobre clips (días 5–10)

1. Con el clip bench (bloqueante de esta fase, no de la Fase 1; **desde ADR-010 su
   ejecución es del tramo final del proyecto** — la Fase 2 se corre entonces, la
   Fase 1 sobre BENCH puede correr apenas exista `edir_v1`): correr media-plane
   sobre clips + control-plane con cada estrategia sobreviviente.
2. Métricas: precision/recall/F1 de **alertas** vs GT temporal (evaluación a nivel episodio), latencia hasta alerta (frames y ms), re-alertas por episodio (ADR-011: se reportan como estabilidad, no como FP) y alertas inesperadas, oscilaciones candidate↔resolved por episodio.
3. Sensibilidad: 2–3 variantes de formulación E-DIR (si sigue viva) y 2 configuraciones de región E-IND, para el capítulo de sensibilidad al prompt.

### Fase 3 — Decisión y cierre documental (días 11–14)

1. Tabla comparativa final + análisis de fallas con ejemplos visuales (evidencia controlada, DA-09).
2. Decisión según §8, registrada como **ADR** ("Estrategia del núcleo validable") en el control-plane, referenciando este documento.
3. Conclusiones por camino (una sección por estrategia con veredicto y por qué) — insumo directo del capítulo R2 del informe.
4. Ajuste del texto de §17.3.9.2 del informe según el resultado.

## 8. Criterios de decisión (fijados antes de correr)

Se elige como **núcleo** la estrategia con mejor F1 de alertas sobre el clip bench,
con estos desempates y vetos, en orden:

1. **Veto de precisión:** una estrategia con precision de alertas < 0.5 no puede ser
   núcleo aunque gane en F1 (un sistema asistivo que alerta mal más de la mitad de
   las veces no es defendible).
2. **Empate técnico** (ΔF1 < 0.05): gana la de menor latencia de alerta; si persiste,
   gana E-IND por auditabilidad de evidencia y costo de vocabulario.
3. **E-HYB** solo se adopta como núcleo si supera a la mejor individual en F1 por
   ≥ 0.05 **y** su explicación cabe en un párrafo (criterio de defensa).
4. Pase lo que pase, la estrategia no elegida queda documentada como variante
   comparativa con sus números — nada se tira.
5. **Contingencia CR-02** (auditoría, doc 07/H7): si ninguna estrategia alcanza el
   veto de precisión para CR-02 (probable cuello: recall de `vest`, cuyo falso
   negativo se convierte en falso positivo de alerta en E-IND), el núcleo mínimo
   defendible es **CR-01 completo + CR-02 reportado con sus límites cuantificados**.
   Eso es un resultado del experimento, no un fracaso del protocolo.
   *Update 2026-07-09:* la asimetría ya tiene **confirmación empírica** — en el
   experimento real del 2026-06-26 (doc 01 §12.3), 65 de 82 alertas fueron CR-02
   dominadas por fallas de percepción/asociación con trabajadores que SÍ llevaban
   chaleco. Las mejoras del motor y el tuning (`vest_confidence` 0.20) atacan esto;
   la Fase 2 medirá cuánto queda.

6. **Notas operativas del protocolo (2026-07-09, rama `mati`):**
   - "Hiperparámetros congelados" (auditoría/§7) ahora significa también **congelar
     el tuning YAML de labs** (umbrales por clase, NMS, tracking) entre variantes de
     prompt — declararlo en la config de cada corrida.
   - **La generación de detecciones para la Fase 2 (clips) usa
     `eovrt-labs generate-detections`** (gdino + `--track` para ids estables), que
     ya emite `media.detection.v1` compatible — no hace falta el media-plane para
     los replays del experimento; el media-plane entra en R4/EBE.
   - El backend `yolo-ppe` habilita una **rama extra opcional del experimento**:
     misma cadena con detector supervisado — responde el Q&A "vs cerrado" (doc 09)
     con números propios. Nota de equidad: labs descarta las clases negativas del
     modelo (`no_helmet`); para una comparación completamente justa con el
     supervisado habría que considerar también su modo nativo con clases NO-*.

## 9. Trabajo mínimo para habilitar la comparación

| Tarea | Repo | Esfuerzo | ¿Bloquea? |
|---|---|---|---|
| Prompt set `edir_v1` (Tabla 45 → YAML) | experimental-setup | horas | Fase 1 |
| Scoring por persona (estado vs has_helmet/has_vest) para ambas estrategias | datasets | 1–2 días | Fase 1 |
| Corridas BENCH con ambos prompt sets | media-plane (existente) | horas | Fase 1 |
| Clip bench con GT temporal (8–15 clips) | datasets | ~1 semana, paralelizable | Fase 2 |
| Evaluador `direct_evidence` | control-plane | ~1 día | Fase 2 (solo si E-DIR pasa el gate) |
| Fusión E-HYB (or/and) | control-plane | 1–2 días | Solo si hay complementariedad |

Nada de esto toca contratos, bus ni arquitectura: la comparación corre íntegramente
sobre la plataforma actual.

## 10. Salidas documentales comprometidas

1. Este documento (protocolo pre-registrado) — congelado antes de correr.
2. `conclusiones-e-dir.md` y `conclusiones-e-ind.md` (o secciones de un único
   documento de resultados): números, ejemplos de falla, veredicto.
3. ADR de decisión de estrategia del núcleo.
4. Redlines para §17.3.9.2 del informe según el resultado.
