# 09 — Pase de tablas y lectura de cierre (2026-08-21)

- **Qué es:** una revisión de punta a punta del informe pedida por el usuario, con dos
  encargos: (a) confirmar que **todo está listo para redactar y cerrar**, y (b) sacar las
  tablas que no aportan y dejar **las justas y necesarias**.
- **Método:** relevamiento del entregable completo (las 81 tablas), del set de ajustes, de
  los redlines y del gobierno, más verificación por comando de lo que se afirma acá.
  Ninguna fila de este documento se escribió sin mirar el archivo.
- **Estatuto:** este documento **propone**; nada se aplica desde acá. Cada bloque tiene su
  casilla de decisión, como el doc 07.

---

## 0. El hallazgo que reencuadra el pedido

El informe tiene hoy **81 tablas numeradas** (61 en el cuerpo, 21 en los anexos, más el
glosario). Y de esas 81, **ninguna contiene un resultado medido por este proyecto**: son
literatura citada, inventario de datos o artefactos de diseño.

> **Todo el tramo experimental llega al informe sin una sola tabla previa.** Las 17 tablas
> de §17.5 —las que el pedido invita a recortar— serían **las primeras del documento que
> muestran lo que el trabajo midió**.

Eso invierte el problema. La sobrecarga de tablas es real, pero **no está donde parece**:
está en §15, §16, §17.1, §17.3 y los anexos, que acumulan 81 tablas de contexto y diseño.
La sección de resultados todavía no existe. Recortar ahí sería recortar la tesis.

**Criterio que se sigue en todo este documento, y que no invento — ya está firmado**
(D-P2-1, pase 2 de §17.3/§17.4, 2026-08-20):

> Una tabla se justifica cuando **se consulta, no se lee**: filas estrictamente paralelas
> sobre los mismos atributos, celdas cortas, y el valor está en comparar *entre* filas.
> Dos columnas = una lista con bordes · dos filas = una oración · una columna que dice lo
> mismo en todas las celdas sobra · celdas de más de ~120 caracteres = prosa en grilla.

Lo que este pase agrega es **aplicarlo donde todavía no se aplicó**: al resto del informe
y a las tablas de resultados que aún no se escribieron.

---

## 1. Veredicto de aptitud: ¿está todo listo para redactar?

**Sí para los insumos. No para el estado del documento.** El detalle importa porque los
dos bloques se confunden fácil.

### Listo y verificado hoy

| Insumo | Estado | Cómo se verificó |
|---|---|---|
| Datos experimentales | cerrados, sin frentes abiertos | acta `operacion/128` |
| Cifras citables | los 4 índices verifican | `96-verificar-indices.py` → «Todo verificado» |
| Materiales | 17 tablas + 6 figuras, todas con artefacto | figuras producidas 08-21 |
| Decisiones de redacción | D-A/B/C, D-P2-1, D1–D4 firmadas | docs 122, pase 1 y 2 |
| Aparato bibliográfico | **sano** — 144 referencias, 407 citas APA autor-año en el cuerpo | conteo sobre §15/§16 |
| Kit para los redactores externos | vigente y regenerable | `--check --etapa all` (arreglado hoy, ver §4) |

### No listo — y es el trabajo que falta

1. **Cero de las 109 unidades está aplicada al `.docx`.** Existe el relevamiento completo
   y, en varios casos, el texto listo para pegar; no existe la aplicación. §17.3 y §17.4
   son la excepción parcial: tienen el pase 1 aplicado (v1.1 / v1.2) y el **pase 2 escrito
   y sin aplicar**.
2. **§17.4, §17.5, §17.6 y §18 están vacías.** Es el 100 % del tramo experimental y el
   cierre. Es la mayor parte del trabajo de redacción que queda.
3. **Hay material "listo para pegar" con contenido vencido** (§3). Si se pega tal cual,
   entra al informe una afirmación falsa.
4. **Un redline no está saldado** por la tabla que debía saldarlo (§3).

---

## 2. §17.5 — las 17 tablas de resultados, una por una

Aplicación mecánica de D-P2-1 al inventario de `gobierno/99` §1. **Saldo: de 17
propuestas, 7 quedan como tabla en el cuerpo, 6 pasan a prosa, 3 van al Anexo D y 1 se
elimina.**

### 2.1 Quedan como tabla — son el capítulo

| Tabla | Por qué se queda | Ajuste que necesita |
|---|---|---|
| **T-68** campañas de Nivel B | Es *la* tabla del capítulo: el contraste entre filas **es** el experimento | ⚠ **recortar de 13 a ~8 columnas** (ver 2.5) |
| **T-72** selección de modelos sobre `bench_v3` | Sostiene la elección del campeón; matriz modelo × estrato genuina | — |
| **T-73** AP por clase y por estrato | La asimetría estructural es un hallazgo, no un anexo | — |
| **T-74** Nivel A: E-DIR vs E-IND con IC | Matriz de comparación con intervalos: se consulta | — |
| **T-75** latencia y tiempo real | Sostiene la afirmación de tiempo real | **absorber T-85** como una fila más |
| **T-78** composición del banco de clips | Metodología que el lector consulta al leer cualquier cifra | — |
| **T-79** composición de `bench_v3` por estrato | Ídem | — |

### 2.2 Pasan a prosa — por corolario 2 de D-P2-1 ("dos filas = una oración")

| Tabla | Qué contiene realmente | Qué gana en prosa |
|---|---|---|
| **T-76** integridad del acople EBE | tres hechos binarios (0 huecos de secuencia, paridad idéntica, cierre 1:1) | una oración afirmativa pesa más que tres celdas que dicen «sí» |
| **T-77** costo de una clase nueva | cuatro números (0 entrenamientos · 48 líneas · 9 minutos · AP 0,662) | es el argumento de extensibilidad: en prosa se lee como afirmación, en tabla como dato suelto |
| **T-83** Nivel A sobre video | cuatro números cuyo valor es el **contraste** (F1 0,031/0,018 en video contra 0,408/0,479 en imágenes) | el contraste se enuncia; una tabla de 2×2 lo esconde |
| **T-84** revisión ciega del GT | una proporción (5 de 7 declaraciones eran error de anotación) | **es un resultado de calidad de la referencia humana**, no una nota al pie: merece párrafo propio |
| **T-85** latencia de notificación | un solo número (p95 64,534 ms, n = 460) | una tabla de un dato no es una tabla; va como fila de T-75 |
| **T-82** estrato B (I1/I2) | dos episodios evaluables | 🔴 **el argumento más fuerte del pase**: la regla prohíbe rankear con n = 2, y **una tabla comparativa invita exactamente a ese error**. En prosa se enuncia lo robusto —la asimetría de falsos positivos 26 vs 323 (12×)— sin ofrecer un ranking que no se sostiene |

### 2.3 Van al Anexo D — el detalle exhaustivo, que ya tiene su lugar

El Anexo D («Métricas, instrumentación y bitácora experimental») existe y es el destino
natural. Mover ahí no es esconder: es separar lo que se **argumenta** de lo que se
**consulta**.

| Tabla | Por qué al anexo |
|---|---|
| **T-69** desglose por escenario P1–P9 | 9 filas × métricas: es material de consulta, no de lectura |
| **T-70** desglose por condición CR-01/CR-02 | dos filas; o se funde como agrupación dentro de T-68, o acompaña a T-69 |
| **T-71** eje de densidad R1–R6 | **FIG-B ya lo muestra**: la figura da la forma, el anexo los valores exactos |

> ⚠ **La regla que gobierna este movimiento, y que no se puede violar:** «se reporta por
> estrato y por escenario, nunca sólo el agregado» (limitación L5). Mover la tabulación
> exhaustiva al anexo la respeta **sólo si** en el cuerpo queda enunciado, en prosa, todo
> contraste por estrato que cambie una conclusión. Criterio explícito a aplicar:
> **si el estrato cambia la lectura, va al cuerpo; si sólo agrega precisión, va al anexo.**

### 2.4 Se elimina del informe

**T-81 — «ADR → dónde se declara en el informe»**. Es una tabla de navegación interna, y
los ADRs **no se mencionan en el informe** por la regla de autocontención. Es material de
trabajo del equipo, no del entregable. Se conserva donde está; no entra al capítulo.

### 2.5 El defecto de forma que hay que arreglar sí o sí

La tabla fuente de T-68 tiene **13 columnas** (`#` · `campaign_id` · Modelo · Prompts ·
Gran. · Recall · Prec. · F1 · `t_alert` · TTFD · SDR · FP neg. · Hallazgo). **A 16 cm de
ancho eso es ilegible.** Recorte propuesto, sin perder un dato:

- `campaign_id` → **a la nota al pie** (es donde la regla de verificabilidad lo pide).
- `Hallazgo` → **a la prosa** que rodea la tabla; es una columna de texto largo, o sea
  prosa en grilla por corolario 4.
- `Modelo` + `Prompts` → una sola columna «variante», porque sólo dos campañas se apartan
  de la combinación base.
- `SDR` y `TTFD` → **al Anexo D**. El SDR además arrastra la advertencia de que no se
  compara entre cadencias; sacarlo del cuerpo elimina de raíz la tentación.

Queda: **campaña · variante · granularidad · R · P · F1 · `t_alert` · FP negativos** — ocho
columnas, publicable, y el contraste entre filas sigue intacto.

```
DECISIÓN §2 → [ ] acepto  [ ] modifico  [ ] rechazo
```

---

## 3. Lo que no se puede pegar tal como está

Tres cosas que se filtrarían al informe si el material se usa sin revisar. **Esto es lo
que el pedido "que no se nos pase nada" tenía que encontrar.**

1. 🔴 **Contenido vencido en una tabla lista para pegar.** La tabla de capacidades y
   brechas del material de Etapa 3 declara, en su fila de fine-tuning, que «resta emitir
   la autorización y el RUN manual». Eso era cierto el 2026-08-13. Hoy **la jornada
   completa cerró**: T1 NO-GO, T2 NO-GO, T3 con causa técnica. Pegar esa fila mete una
   afirmación falsa en el informe. **Reescribirla con la curva de tres puntos.**
2. 🔴 **Un identificador de clip retirado.** El ejemplo de evento de percepción del mismo
   material usa como `source_id` un clip que fue **retirado del banco**. El propio
   material lo marca con una advertencia sin resolver. Cambiar el ejemplo por un clip
   vigente antes de pegarlo.
3. 🟠 **Un redline sin saldar.** El redline de registro de alcance exige que cada capacidad
   quede **anclada a su regla de exclusión**, «para que se lea como alcance declarado y no
   como omisión». La tabla que debía saldarlo **no contiene ni un solo código de
   exclusión**. O se agrega la columna, o se declara explícitamente que el anclaje se
   resolvió en otra sección — pero no puede quedar como está y darse por cerrado.

```
DECISIÓN §3 → [ ] acepto  [ ] modifico  [ ] rechazo
```

---

## 4. Las 81 tablas existentes: dónde está la grasa de verdad

Un pase anterior relevó la **forma** de todas las tablas y recomendó **no abrir** este
frente, con dos argumentos: que el costo de renumerar supera la ganancia, y que fuera de
§17.3 «ninguna de esas tablas presenta el problema de duplicación entre tablas vecinas».

**El segundo argumento no se sostiene, y el primero cambió de signo.** Aquel relevamiento
declaraba explícitamente ser «de forma, **sin** revisión de contenido». Hecha la revisión
de contenido, aparecen duplicaciones reales:

| Duplicación | Estado |
|---|---|
| «Umbrales orientativos por severidad» aparece **dos veces**, en §17.1.7.9 y en el Anexo D — mismo título, mismas filas, mismos valores; la del anexo es superconjunto | ✅ **verificado por comando** |
| Los dos backlogs de §17.3.17 comparten **esquema idéntico** de cinco columnas, y su propia columna `Prioridad` ya distingue lo que la partición en dos tablas pretende distinguir | ✅ **verificado por comando** |
| Cobertura por condición (§17.1.6.5) contra su gemela del Anexo C | 🟡 relevado, confirmar al aplicar |
| Síntesis de modelos OVD de §15.2.3.1 ⊂ la del Anexo A (6 filas contra 12) | 🟡 relevado, confirmar al aplicar |
| Jerarquía de métricas de §17.1.7.9 contra las tres tablas de detalle del Anexo D | 🟡 relevado, confirmar al aplicar |

Y el argumento del costo se invirtió: aquel pase dijo que, de abrirse, **debía hacerse
antes** que él para renumerar una sola vez. **Ese pase todavía no se aplicó.** La ventana
que se daba por cerrada sigue abierta, y es hoy.

### Pero la mayor parte se resuelve sola

**No hace falta un pase de tablas dedicado para §15 y §16.** Las unidades de poda ya
programadas eliminan o comprimen las secciones que contienen las tablas problemáticas: al
podar el bloque de streaming y servidores, el de MOT y el de convergencias, **sus tablas
caen con ellas**. Duplicar el trabajo en dos pases sería exactamente el error que el
manual advierte: corregir algo que después se elimina.

**Recomendación:** no abrir un pase de tablas separado. En cambio:

- **(a)** Incorporar D-P2-1 como criterio explícito **dentro de cada pase de sección**, que
  es como ya se aplican las podas y los ajustes.
- **(b)** Tratar aparte **sólo las duplicaciones verificadas**, porque no las resuelve
  ninguna poda: son tablas que sobreviven en dos lugares distintos. Eliminar una copia no
  pierde ningún dato y es la ganancia más barata del documento.
- **(c)** Proteger intactos los catálogos y contratos que el resto del documento referencia
  por número: matriz de evidencias normativas, catálogos de condiciones y patrones,
  decisiones arquitectónicas, fronteras informacionales, contratos mínimos, catálogo de
  prompts.

```
DECISIÓN §4 → [ ] acepto  [ ] modifico  [ ] rechazo
```

---

## 5. Ideas que nadie pidió y conviene considerar

1. **El desbalance tabla/figura es de 81 a 2.** El informe tiene ochenta y una tablas y
   **dos figuras**. Eso, más que la cantidad de tablas, explica por qué se lee denso: no
   hay ningún respiro visual en 127.000 palabras. Las seis figuras nuevas mejoran el
   tramo experimental, pero §15/§16/§17.1 siguen sin una sola. **Antes de sacar tablas de
   esas secciones, vale preguntarse cuál de ellas quiere ser una figura** — un esquema de
   la brecha entre literatura y problema, por ejemplo, resuelve en una imagen lo que hoy
   son cuatro tablas de «brechas» con el mismo encabezado.
2. **Las cuatro tablas de brechas son una sola tabla.** Hay cuatro tablas distintas con el
   encabezado «brecha · descripción · implicación» (OVD, seguimiento, ético-legal,
   transversal), 21 filas entre todas, y una de ellas ya se declara la integradora.
   Consolidarlas en una matriz con columna de dominio ahorra tres tablas y **mejora** el
   argumento: la convergencia de brechas es justamente lo que justifica el trabajo.
3. **La regla de estilo choca con la salida propuesta, y hay que elegir.** El brief dice
   «no usar viñetas donde el informe usa prosa; el capítulo 17 es mayormente prosa con
   tablas numeradas». Varias unidades del pase 2 convierten tablas **a viñetas**. Con el
   brief en la mano, la conversión por defecto debería ser **a prosa**, y las viñetas
   reservarse para enumeraciones genuinamente cortas y paralelas. Conviene decidirlo una
   vez, no tabla por tabla.
4. **El orden de aplicación importa más que la lista.** Aplicar el pase 2 de §17.3/§17.4
   antes de resolver §4 obliga a renumerar dos veces. Y aplicar cualquier poda de §15/§16
   después de escribir §17.5 obliga a revisar las referencias cruzadas. El orden barato es:
   duplicaciones verificadas → pase 2 → podas por sección → escritura de §17.4/§17.5/§17.6.
5. **La numeración conviene congelarla al final.** Con ~17 tablas saliendo y ~13 entrando,
   cualquier número escrito en prosa hoy se rompe. Mientras dure el pase, referirse a las
   tablas por su **título**, no por su número, y numerar en una única pasada al cierre.

```
DECISIÓN §5 → [ ] acepto  [ ] modifico  [ ] rechazo
```

---

## 6. Ejecutado hoy (no requiere decisión)

- **Arreglado el generador del kit.** Apuntaba a un archivo movido a `archivado/` y
  `--check --etapa all` fallaba, con lo que la puerta de cierre del kit no podía correrse.
  Ahora incluye el pase 1 (cuyas decisiones siguen rigiendo) **y** el pase 2, y verifica en
  verde con los ocho archivos de knowledge.
- **Aclarada la aparente contradicción entre dos reglas** que hoy pueden frenar a un
  redactor externo: la autocontención prohíbe mencionar documentación interna, y otra regla
  exige que toda tabla de resultados lleve su identificador de campaña o el digest del
  banco al pie. **No se contradicen:** la nota al pie identifica el *artefacto* (qué
  corrida, qué digest), nunca *dónde vive el archivo*. Queda registrado en el documento de
  Etapa 5.

---

## 7. Qué verifiqué corriendo el comando

| Afirmación | Verificación |
|---|---|
| 126.787 palabras escritas | `wc -w` sobre los seis archivos del entregable |
| 81 tablas, ninguna de resultados propios | relevamiento fila por fila del entregable completo |
| 2 figuras referenciadas en todo el informe | conteo de referencias «Figura N» |
| Aparato bibliográfico sano | 144 referencias · 407 citas autor-año en §15 y §16 |
| «Umbrales por severidad» duplicada | comparación de ambas tablas: mismo título y mismos valores |
| Los dos backlogs comparten esquema | encabezados idénticos de cinco columnas |
| T-68 tendría 13 columnas | encabezado de la tabla fuente |
| Las cifras citables verifican | verificador de índices en verde |
| El kit vuelve a verificar | `--check --etapa all` en verde tras el arreglo |
