# Pase de la Etapa 6 — capturas de la consola · v1.4 → v1.5

> **Entregado el 2026-09-13 como SUGERENCIAS Y COMENTARIOS.** Nada en limpio: rechazar todas las
> sugerencias devuelve la v1.4 exacta (verificado).
> Guion: [`herramientas/pase_etapa6_v15_consola.py`](../../../../herramientas/archivado/pase_etapa6_v15_consola.py) ·
> Documento: `E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.5 (sugerencias sin aceptar).docx`

Punto de partida: la v1.4, que el usuario bajó de Google Docs con todas las sugerencias de la v1.3
aceptadas. El pedido: **agregar capturas de la consola, sin mucho texto y sin irse de más**.

---

## 1. Dónde van, y por qué ahí

**Una figura al cuerpo y tres a un anexo nuevo.** El reparto no es de comodidad:

| Decisión | Motivo |
|---|---|
| **No se toca §17.4** | Es donde la consola está descrita como componente, pero está **cerrada** (v1.15) y tiene su propio mapa de secciones. Abrirla obligaba a tocar su numeración y su serie de figuras. |
| **Figura 4.7 en §17.6.2** | El apartado afirma que cada ejecución queda identificada y su evidencia conservada. La pantalla de Evidencia es esa afirmación hecha visible. La serie del cuerpo se agotaba en la **4.6**, así que la 4.7 no renumera nada. |
| **Anexo G nuevo, no ampliar el B** | El Anexo B está amarrado por número a §17.1.4 y §17.4, y es todo tablas. Los seis anexos A–F **no tienen ninguna figura**: un anexo de figuras es un objeto nuevo y conviene que lo sea. |
| **La consola es el instrumento, no un resultado** | Por eso la mayoría va al anexo. Pero el tribunal **no puede abrir la consola** —no está desplegada—, así que el cuerpo se queda con una. |

**Costo total: +386 palabras (+4,1 %).** Prosa nueva: una oración en §17.6.2, un párrafo de entrada
en el Anexo G y cuatro pies de figura. Nada más.

---

## 2. Las cuatro figuras

| Fig | Pantalla | Qué vuelve visible | Tamaño |
|---|---|---|---|
| **4.7** | Evidencia | los resultados reportados y el recorrido del argumento; se lee del archivo curado **sin consultar servicios** | 14,0 × 10,1 cm |
| **G.1** | Corridas | el inventario agrupado por el resultado que lo cita, con su cifra y su clase | 13,5 × 14,1 cm |
| **G.2** | Detalle de corrida | la traza por cuadro, las detecciones con su confianza y el progreso de las condiciones | 12,0 × 14,5 cm |
| **G.3** | Detalle de experimento | métricas medidas, **la razón de las que no se pudieron medir**, alertas y trazabilidad | 13,2 × 14,5 cm |

Los anchos difieren a propósito: lo que se mantuvo constante es el **alto** (tope ~14,5 cm), que es
lo que gobierna el ritmo de la página con capturas verticales.

### Cómo se tomaron

Con `webconsole/tools/capture_console.mjs` —la herramienta que ya vive en el repo, no una
inventada— contra el BFF en `:8090` con los **tres servicios arriba**, sobre el material
conservado. Viewport 1440×1000 a factor 2, página completa, tema oscuro. El guion **recarga hasta
que el motor de detección responde y falla si no lo consigue**: ninguna captura salió con el
encabezado en «servicio caído», que es lo que había pasado en la primera pasada.

---

## 3. Lo que quedó afuera, con motivo

| Pantalla | Por qué no |
|---|---|
| **Plataforma** | Sin el compose de `infra/platform` arriba dice «la orquestación no está habilitada: la consola apunta a una instancia fija». Mostraría una limitación **del entorno de captura**, no de la plataforma. |
| **Conjuntos de prompts** | **Defecto de maquetado real**: la insignia de estado se alinea al ancho del nombre y se sale del borde de la tarjeta. Verificado a 1440, 1680, 1920 y 2200 px — no es cuestión de resolución. Publicarlo dejaría el defecto impreso en el informe. |
| **Comparar** | Sin corridas elegidas no muestra nada. |
| **Cámaras** | Credenciales RTSP en claro. |

---

## 4. Dos advertencias que van en el documento

1. **El indicador «mock» del encabezado** es el motor cargado al tomar la captura, **no** el modelo
   con que se produjo la corrida histórica (que es `grounding_dino`, y consta en el identificador
   de la corrida). Sin aclararlo, un lector puede entender que esas detecciones salieron de un
   modelo simulado. Va en la nota de la **Figura G.2**.
   *No se cargó el modelo campeón para la captura*: pide RAM que WSL hoy no tiene sobrada
   (3 GB disponibles de 7) y el riesgo de tumbar el entorno no lo paga un detalle de encabezado.
2. **La suma de los grupos no es el total de corridas**: una corrida citada por dos resultados
   aparece en los dos. La pantalla ya lo dice al pie; la nota de la **Figura G.1** lo repite.

---

## 5. Compuertas

```
rechazar todas las sugerencias → texto idéntico (65.576 car.) · tablas 18 → 18
                                 figuras 0 → 0 · párrafos 719 → 719   ✓
integridad OPC                 → paquete íntegro                      ✓
vista aceptada                 → 4 imágenes resueltas, pies y notas en su lugar ✓
```

⚠ **Defecto encontrado y corregido durante el pase.** La primera versión anclaba el Anexo G
*después* del último párrafo del documento. Al rechazar, un párrafo insertado se fusiona con el
**siguiente**; el último no tenía con quién, y sobrevivía vacío: la compuerta daba texto idéntico
pero **719 → 720 párrafos**. El texto coincidía, así que era invisible salvo en el conteo. Anclado
en `u156`, el último se fusiona con el párrafo vacío de cierre y la compuerta cierra exacta.

---

## 6. Pendiente para el usuario

- **El índice de figuras del maestro** no se tocó: al integrar, las entradas 4.7 y G.1–G.3 hay que
  darlas de alta ahí.
- **El defecto de maquetado de Conjuntos de prompts** sigue en la consola. No se arregló: no era lo
  pedido y habría exigido un commit.
- Si más adelante se levanta el compose completo, **la pantalla de Plataforma es la quinta captura
  natural** y entra en el Anexo G sin tocar nada más.
