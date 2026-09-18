# Análisis y propuesta de desarrollo — §14.4 «Costos asociados al proyecto» y §17.2 «Costos asociados»

- **Fecha:** 2026-09-11
- **Estado:** análisis previo a redacción. **Ninguna sección escrita todavía.**
- **Alcance:** las dos secciones de costos del informe: la del plan de trabajo (§14.4) y la
  del desarrollo del producto (§17.2).
- **Ficha de ajustes que cubre:** **AJ-0.05** (Etapa 0) — *«Hueco abierto, no relevado.
  Nadie contrastó todavía los costos declarados contra lo efectivamente gastado.»*
- **Bloqueado por:** ocho datos que sólo puede aportar el usuario (§5 de este documento).

---

## 1. Qué pide cada sección

| Sección | Ubicación | Qué exige el formato institucional |
|---|---|---|
| **§14.4** Costos asociados al proyecto | dentro de §14 Plan de trabajo | Gastos para la realización del trabajo: movilidad, alquiler de VPS, licencias de software, suscripciones, impresiones, etc. |
| **§17.2** Costos asociados | dentro de §17 Desarrollo del producto | **Evaluación económica y financiera**: costos totales (inversión inicial, recursos humanos, infraestructura, equipamiento, operación y mantenimiento), fuentes de financiamiento, ahorros o ingresos esperados |

## 2. Estado actual en el informe (verificado)

Las dos secciones existen como huecos declarados:

- `96a-informe-v11-frontmatter-intro-objetivos-plan.md:441` → **§14.4** dice
  `[Se completará más adelante.]`
- `archivado/96b-informe-v11-17-1-consolidacion-metodologica.md:1328` → **§17.2** dice
  `[Pendiente]`, ubicada entre §17.1 (consolidación metodológica) y §17.3 (diseño
  arquitectónico).

Ninguna sección vigente del informe remite a §17.2, así que **escribirla no obliga a tocar
nada ya cerrado**.

### 2.1. Las tres restricciones que condicionan la redacción

**(a) Numeración de tablas — decide el formato de cada sección.**
Del inventario de `00-lo-que-resta.md` §4.1 (re-verificado el 09-07 sobre las cinco
versiones vigentes):

| Tramo | Tablas |
|---|---|
| §11–§14 | **1** (glosario) |
| §15 + §16 | 2–11 |
| *hueco* | **12–15 — reservados justo para §17.2, que hoy no tiene tablas** |
| §17.1 | 16–35 |

⇒ **§14.4 va en prosa y lista, sin tabla numerada** (una tabla ahí corre la numeración de
§15/§16, que están cerradas). **§17.2 puede usar hasta cuatro tablas: 12, 13, 14 y 15.**

**(b) Reglas del pase de redacción** (`ajustes/08-manual-de-aplicacion.md`):
- **Autocontención**: el informe no referencia jamás documentación local de desarrollo
  (ni docs, ni ADRs, ni fichas, ni índices).
- **Voz (D-P3-9)**: presente para lo que existe; lo normativo y lo no ejercido no se toca.
- **Cifras verificables**: toda cifra rastrea a un respaldo. Las de costos **no salen de
  `results/`** ⇒ hay que crearles un respaldo propio (ver §4.3).

**(c) AJ-0.05 pide contraste previsto vs. gastado**, no una tabla de precios inventada.

## 3. Inventario real del proyecto (lo ya afirmable sin preguntar)

| Dimensión | Dato verificado | Fuente |
|---|---|---|
| Equipo humano | 3 integrantes (Carrizo, Guillaumet, Llamosas) + 1 tutor (García Mattio) | portada del informe |
| Plan temporal | 6 etapas, 35–43 semanas (4–5 · 5–6 · 7–9 · 10–12 · 4–5 · 5–6) | §14.2 |
| Gantt declarado | 31/10/25 → 21/08/26 | Figura 1 (⚠ vencido, AJ-0.03) |
| Duración real | hasta defensa ~fin sept 2026 ⇒ ~48 semanas | cronología |
| Nodo de procesamiento (CPN) | Notebook HP · AMD Ryzen 5 8645HS · RTX 4060 Laptop 8 GB · 32 GB DDR5 · 1 TB NVMe | Tabla B.1 |
| Nodo de borde (EN) | Luxonis OAK-D Pro PoE (Series 2), PoE 802.3af Class 3 | Tabla B.2 |
| Nodo de entrenamiento (TN) | Clúster **Mendieta (CCAD-UNC)** · 19 nodos · 2×A30 24 GB · asignación mínima ½ nodo | Tabla B.4 |
| Cómputo en clúster consumido | 7 jobs Slurm citados (`1166552`, `1166583`, `1167640`, `1167864`, `1167979`, `1167980`, `1167982`); full T1 = **13 min**; presupuesto pre-registrado T1 1–3 GPU-h, T2 4–10, T3 8–24 | `operacion/100`, `123`, `127`, `contingencia/20` |
| Otro hardware | switch PoE + 2 cables de red; 1 cámara RTSP vía DVR preexistente | guion de rodaje |
| **VPS / nube** | **Ninguno.** Cero menciones de VPS, EC2, AWS, GCP o Azure en todo el set documental | grep exhaustivo |
| **Licencias de software** | **Cero pagas.** Stack íntegramente abierto | — |
| Licencias de datos | CC BY 4.0 (construction_site_safety, ppe_siabar, SHEL5K, COCO anot.), grant informal + cita (CHV), AGPL-3.0 (Construction-PPE), Apache-2.0 (varios pesos) | `license_registry.md` |
| Almacenamiento / respaldo | **Cuenta gratuita de Drive** (todo entra) + GitHub gratuito | `operacion/126` |
| Trabajo de campo | 1 jornada de rodaje guionado (25/07/26) con **2 actores** + 1 piloto (18/07/26); utilería: cascos y chalecos | `operacion/69`, `71` |
| Energía | única medición: **30,7 W p50** de GPU en corrida realtime | `operacion/73` |

## 4. Propuesta de desarrollo

### 4.1. Ubicación: dejar §17.2 donde está

**Recomendación: no mover la sección.** Tres razones:

1. **La secuencia se lee natural** si la primera oración la explicita: §17.1 fija qué se
   mide y con qué infraestructura → **§17.2 cuánto cuesta y quién lo financia** → §17.3
   cómo se construye. Es el orden clásico de formulación de proyectos
   (metodología → evaluación económica → diseño → implementación).
2. **Mover la sección obliga a renumerar** §17.3, §17.4 y §17.5, que están cerradas y
   tienen mapas de secciones y 26 redlines colgando de su numeración actual.
3. **Los cuatro números de tabla libres (12–15) caen exactamente ahí.**

**Único cambio de título sugerido:**
`17.2. Costos asociados` → **`17.2. Costos asociados: evaluación económica y financiera`**,
para que el título anuncie lo que el formato pide.

### 4.2. Reparto de contenido sin duplicar

| | §14.4 | §17.2 |
|---|---|---|
| **Mirada** | del plan: gastos directos para poder hacer el trabajo | del producto: costo total del sistema, financiamiento y ahorros |
| **Unidad** | gasto de bolsillo | costo valorizado (incluye lo preexistente y lo aportado en especie) |
| **Formato** | prosa + lista por categoría, **sin tabla numerada** | 5 subsecciones + **Tablas 12–15** |
| **Extensión** | ~300 palabras | ~1.200–1.500 palabras |
| **Enlace** | remite a §17.2 para el desglose cuantificado; **no repite números** | se apoya en §14.4 sin re-listar categorías |

### 4.3. §14.4 — estructura propuesta

1. **Párrafo de encuadre.** Proyecto autofinanciado por los integrantes. El costo directo
   es bajo **por decisión de diseño**: el despliegue corre sobre equipamiento propio y el
   cómputo pesado se deriva al clúster institucional.
2. **Lista por categoría del formato**, cada una con su realidad:
   - **Movilidad** — tutorías presenciales y traslado a la jornada de rodaje.
   - **Alquiler de VPS** — *ninguno*, con la justificación en una oración (la plataforma
     es de despliegue local y el entrenamiento usa infraestructura institucional).
   - **Licencias de software** — *cero*: stack abierto de punta a punta; los conjuntos de
     datos se usan bajo licencias abiertas con atribución.
   - **Suscripciones** — las efectivamente pagadas *(dato pendiente del usuario)*.
   - **Impresiones y encuadernación** — copias del informe final *(dato pendiente)*.
   - **Consumibles del trabajo de campo** — elementos de protección de utilería, cables.
3. **Cierre.** Total previsto + remisión a §17.2 para la evaluación económica completa.

### 4.4. §17.2 — estructura propuesta (5 subsecciones, Tablas 12–15)

**17.2.1. Enfoque y supuestos de la estimación.**
Qué se cuenta y cómo: **gasto efectivo** separado de **costo valorizado**; horizonte igual
a la duración del proyecto; moneda y fecha de referencia declaradas. Una oración explica
por qué **no hay VAN ni TIR**: es un prototipo experimental sin flujo de ingresos, y el
formato pide *estimar e identificar*, no modelar rentabilidad.

**17.2.2. Inversión inicial y equipamiento — Tabla 12.**
Columnas: *ítem · condición (comprado / preexistente / prestado) · gasto efectivo · valor
de referencia*. Filas: nodo de procesamiento, OAK-D Pro PoE, switch PoE y cables, cámara
RTSP del DVR, utilería de rodaje.

**17.2.3. Recursos humanos — Tabla 13.**
Horas de los tres integrantes por etapa, derivadas del plan de §14.2 y ajustadas a la
duración real, más horas de tutoría. **Dos variantes posibles** (decide el usuario):
valorizadas a una tarifa de referencia declarada, o presentadas sólo en horas.

**17.2.4. Infraestructura, operación y mantenimiento — Tabla 14.**
Horas de GPU en Mendieta a **costo cero institucional**, con un precio de referencia de
mercado al lado para dimensionar el aporte en especie. Energía e internet. Almacenamiento
y repositorios gratuitos. Licencias en cero, con la nota sobre **AGPL-3.0** para un
eventual despliegue comercial.

**17.2.5. Financiamiento, ahorros e ingresos — Tabla 15 (resumen).**
- **Fuentes**: aporte propio de los integrantes + aportes en especie (clúster CCAD-UNC,
  tutoría institucional, equipamiento propio).
- **Ingresos esperados**: ninguno — y decirlo explícitamente.
- **Ahorros como costos evitados y medidos**: licencias en cero por stack abierto;
  hardware de consumo en lugar de servidor dedicado; y **el argumento fuerte de la tesis**
  — detección open-vocabulary **sin entrenar**, respaldado por resultados propios (los
  brazos de ajuste fino no superaron al modelo base, y agregar una condición nueva costó
  minutos de configuración en vez de un ciclo de reentrenamiento).
- **Cierre**: costo de replicar **una unidad mínima de despliegue** (un nodo de
  procesamiento + una cámara PoE + un switch). Es el número que un tribunal quiere ver.

### 4.5. Respaldo verificable de las cifras

Las cifras de costos no rastrean a `results/`. Para no romper la regla P1 del manual,
propongo un **CSV de respaldo con fuente por fila** (ítem, categoría, monto, moneda,
fecha, origen del dato: factura / presupuesto / precio de lista / estimación declarada),
ubicado junto al resto de la evidencia del informe. Así toda cifra de §17.2 tiene de dónde
salir y AJ-0.05 se cierra con constancia.

## 5. Datos que faltan — sólo los puede aportar el usuario

1. **Equipamiento comprado.** OAK-D Pro PoE: ¿comprada, prestada o de la empresa? Precio,
   fecha, quién pagó. Ídem switch PoE, cables, trípodes, cámara del DVR. Upgrades de la
   notebook (RAM, disco), si los hubo.
2. **Notebook.** Precio y fecha de compra, **o** declararla como equipo preexistente sin
   costo incremental.
3. **Horas.** Dedicación semanal promedio por integrante (o por etapa) y frecuencia de
   tutorías. Si se valoriza en dinero: qué tarifa de referencia usar.
4. **Movilidad.** Dónde fue el rodaje y el piloto, cuántos viajes a la sede por tutorías,
   medio de transporte.
5. **Suscripciones pagas** durante el proyecto (asistentes de código con IA,
   almacenamiento, otras) y si se declaran o no.
6. **Impresiones.** Cuántas copias exige la institución; costo de impresión y
   encuadernación.
7. **Moneda.** Pesos, dólares, o dólares con equivalente en pesos a una fecha declarada.
8. **Formato institucional.** Si existe el documento con la plantilla, pasarlo para
   respetar cualquier tabla o rótulo exigido.

**Lo que puedo obtener yo, sin preguntar:**
- Total de horas de GPU consumidas en Mendieta (`sacct` sobre los 7 jobs).
- Estimación de energía del equipo local, a partir de la potencia medida y las horas de
  corrida registradas.

## 6. Efectos colaterales a tener presentes

- **AJ-0.03 (Gantt vencido)** queda tocado de refilón: §14.4 y §17.2 usan la duración
  **real** del proyecto para calcular horas, no la del Gantt. Conviene resolver ambos en
  el mismo pase de Etapa 0, o §14.3 y §14.4 se contradicen entre sí.
- **Tabla A.1 / anexos**: ninguna tabla de costos necesita anexo nuevo. Todo entra en
  Tablas 12–15.
- **Sin impacto** sobre §15, §16, §17.1, §17.3, §17.4 ni §17.5: ninguna las remite.

---

## 7. ✎ Misma jornada — datos recibidos, decisiones y borradores escritos

**Respuestas del usuario (2026-09-11):**

| Pregunta | Respuesta |
|---|---|
| Equipamiento | OAK-D Pro PoE **prestada por el tutor**; cámara RTSP **propia** |
| Notebook | **Propia** (preexistente) |
| Horas | **~8 h semanales por integrante** |
| Movilidad | **Un solo traslado** al local de **Steel Brox S.R.L.**, donde además **prestaron casco y chaleco** |
| Impresiones | **No hay** (entrega digital) |
| Moneda | **Pesos argentinos** |
| Mendieta | **Incluir** las horas de GPU |
| Sin respuesta | suscripciones · tarifa de referencia · frecuencia de tutorías · formato institucional |

**Decisiones tomadas para redactar (todas revisables):**

1. **§17.2 se queda donde está y conserva el título institucional «Costos asociados»**; la
   primera subsección anuncia la «evaluación económica y financiera».
2. **Dos magnitudes separadas en todo el capítulo: gasto efectivo vs. costo valorizado.**
   Lo preexistente y lo prestado va a **valor de referencia** (precio de lista, fuente y fecha),
   nunca a gasto. Sin depreciación ni prorrateo, para no agregar complejidad.
3. **RRHH por integrante, no por etapa**: el Gantt tiene huecos entre fases (35 semanas
   activas en 42 calendario) y un desglose por etapa inventaría precisión. Previsto 42 sem /
   ejecutado 48 sem × 8 h × 3 = 1.008 h / 1.152 h.
4. **Tarifa de referencia**: mediana bruta junior **Sysarmy 2026.01 = ARS 1.538.500/mes**
   (vía Teclab) ÷ 160 h = **ARS 9.616/h**. El usuario no fijó tarifa; ésta es la propuesta.
5. **Tutoría**: aporte en especie **no cuantificado** (sin dato de frecuencia).
6. **Suscripciones: asumido ninguna paga** — marcado `[confirmar]` en §14.4. Si hubo planes
   pagos de asistentes de IA, el formato los pide explícitamente.
7. **Tipo de cambio**: BNA minorista venta **10/09/2026 = ARS 1.535/USD**.
8. **Sin VAN/TIR**, declarado con causa en 17.2.1.
9. **Mendieta valorizado como "marginal"** sin precio de nube concreto (1,2 GPU-h no cambian
   el orden de magnitud; poner un precio de alquiler sería una estimación fuera de contexto).
10. **Respaldo de cifras**: `docs/operacion/datos/costos-proyecto-2026-09-11.csv` (32 filas,
    fuente y fecha por fila) — cierra la regla P1 para esta sección y da constancia a AJ-0.05.

**Cifras nuevas verificadas en la jornada** (detalle y comandos en las notas editoriales del
borrador de §17.2): Mendieta **1,195 GPU-h** en 15 jobs (10 con GPU, 6 completados) ·
cómputo local **34,35 h** en 472 corridas · notebook **ARS 2.719.999** (HP, con IVA) ·
OAK-D Pro PoE **US$ 579 = ARS 888.765** · AF-4 (48 líneas, 9 min, AP 0,662) confirmada en
`results/bench_imagenes/index.md` §4.

**Hallazgo colateral:** la Tabla B.1 declara **32 GB (2 × 16)** y el modelo de fábrica trae
**16 GB (2 × 8)** ⇒ hubo una ampliación de RAM que nadie declaró. Si se compró para el
proyecto es **gasto efectivo** y hay que ponerle monto.

**Entregables de la jornada:**
- `desarrollando/borrador-14-4-costos-asociados.md` — v0.1
- `desarrollando/borrador-17-2-costos-asociados.md` — v0.1, Tablas 12–15
- `docs/operacion/datos/costos-proyecto-2026-09-11.csv` — respaldo
- **`desarrollando/E-OVRT-VDP_Secciones_14.4_y_17.2_Costos_Asociados_v0.1.docx`** — el
  documento de trabajo que pidió el usuario (sólo las dos secciones, sin notas editoriales).
  Generado con **`herramientas/generar_docx_costos.py`** sobre una copia vaciada del maestro,
  así hereda sus estilos reales: títulos `Ttulo2/Ttulo3`, `Normal` con sangría de primera
  línea, leyendas `Descripcin` con campo SEQ, tablas con bordes APA y **las dos tablas anchas
  (12 y 13) en secciones horizontales**, igual que el maestro. Los 9 marcadores `[confirmar]`
  / `[monto]` van **resaltados en amarillo**. Pesa 6 MB por las fuentes embebidas del maestro
  (a propósito). El verificador `verificar_entregable.py` da 2 "fallas" de numeración
  («§14 arranca en 4», «§17 arranca en 2») que son **falsos positivos**: el documento es un
  recorte de dos secciones, no un capítulo completo. Para regenerarlo tras editar los
  borradores: `python3 herramientas/generar_docx_costos.py` (requiere `python-docx`).

**Pendientes del usuario para cerrar la v1.0** (marcados en los borradores): monto del
traslado · sede de Steel Brox visitada · RAM ampliada ¿comprada? · propietario del switch PoE
y del cable M12 · suscripciones pagas sí/no · tutoría ¿cuantificar? · alta de 4 referencias
nuevas en el listado global (HP, Luxonis, Teclab/Sysarmy, tipo de cambio).
