# J1: casos observados y propuesta de diagnóstico

**Propuesta para discutir, no especificación aprobada.** Una aplicación breve puede
orientar consultas funcionales, reunir evidencia y derivar investigaciones técnicas,
sin modificar Odoo ni prometer una solución automática.

Referencia de trabajo: [tarea 39775](#tarea-39775).

## Qué respalda esta propuesta

Se recorrió el documento completo mediante lectura secuencial y análisis en memoria.
El original permanece privado: no se reproduce, adjunta ni enlaza desde este informe.
Las respuestas históricas del asistente **no son instrucciones verificadas ni verdad
diagnóstica**. El corpus tampoco es un benchmark diagnóstico validado.

| Cobertura | Resultado y alcance |
|---|---|
| Lectura estructural | 44.361 líneas; 2.017.671 bytes. |
| Segmentación | 429 secciones de nivel dos, todas con mensajes de usuario. |
| Marcadores de mensajes | 3.026 de usuario y 2.746 de asistente. Son bloques del formato, no turnos auditados individualmente. |
| Exploración acotada | 60 secciones elegidas pseudoaleatoriamente con semilla fija; contienen 442 bloques de usuario. |
| Material examinado en la muestra | Vocabulario temático permitido y señales de intención calculados sobre texto de usuario; no transcripciones completas ni adjuntos. |
| Barrido temático | Búsqueda de palabras y variantes predefinidas en los bloques de usuario de las 429 secciones. |

Las secciones se usan como unidades operativas de conversación, **no como personas
únicas ni sesiones independientes verificadas**. La muestra cubre aproximadamente
el 14 % de las secciones; no acredita una lectura semántica exhaustiva del corpus.
No se inspeccionaron imágenes, archivos adjuntos ni sistemas de clientes.

Los conteos siguientes son **coincidencias léxicas por sección**, no cantidades de
incidentes, frecuencia validada, gravedad ni tasa de resolución. Una sección puede
aparecer en varias familias; una mención puede ser contexto y no el problema central.
Los grupos usan alternativas de términos: por ejemplo, factura/comprobante para
facturación y stock/inventario para existencias. No se suman para obtener un total.
Las referencias a tickets o adjuntos tampoco prueban que haya evidencia disponible.

## Familias para preparar la aplicación

Son agrupaciones de señales observadas en consultas de usuarios. Los ejemplos son
**situaciones nuevas y sintetizadas** para diseñar el flujo, no relatos de incidentes
individuales ni citas. No incorporan detalles identificativos del material de origen.

| Familia y secciones con coincidencia | Ejemplo sintetizado | Orientación inicial |
|---|---|---|
| Facturación y circuito fiscal — 118 | Una factura no avanza a la validación esperada. | Distinguir estado del documento, configuración y respuesta fiscal; no volver a emitir para probar. |
| Pagos, recibos y contabilidad — 78 | Un pago registrado no se refleja como se esperaba en el saldo. | Separar registro, aplicación y conciliación; no corregir asientos desde el diagnóstico. |
| Ventas, pedidos, precios y monedas — 101 | El precio mostrado en un pedido difiere del esperado. | Revisar contexto funcional, lista y moneda; no asumir un defecto de cálculo. |
| Inventario y movimientos — 56 | La existencia visible no coincide con la esperada tras una entrega. | Distinguir ubicación, estado y movimientos; no ajustar existencias. |
| Compras, proveedores y contactos — 55 | No se encuentra un contacto al preparar una compra. | Orientar búsqueda y contexto antes de sugerir crear o duplicar registros. |
| Acceso, usuarios y permisos — 72 | Una opción no aparece para quien intenta operar. | Separar navegación y permisos; nunca pedir contraseñas ni ampliar accesos. |
| Informes, filtros y documentos — 45 | Un informe no incluye un registro esperado. | Revisar filtros y alcance; investigar técnicamente solo si persiste la discrepancia. |
| Conectividad, rendimiento e integración — 25 | Una operación no obtiene respuesta o tarda más de lo esperado. | Precisar alcance y momento; escalar si no existe acceso técnico autorizado. |

No hay base para ordenar estas familias como prioridades comerciales por volumen.
El barrido y la muestra no establecen causas raíz, soluciones correctas ni casos
resueltos. Las categorías pueden cambiar después de una codificación humana validada.

En las 60 secciones muestreadas hubo señales mecánicas de preguntas de procedimiento
en 24, de imposibilidad de operar en 15, de error o fallo en 14, de solicitud de cambio
en 10 y de referencias a adjuntos en 30. Se superponen y pueden tener falsos positivos.
Esto sugiere ofrecer tanto **«¿Cómo se hace?»** como **«Algo no funciona»**, sin
interpretar cualquier solicitud de cambio como autorización para ejecutarlo.

## Qué evidencia pedir y quién puede resolver

| Familia | Puede aportar el usuario, por canal protegido | Solo investigación técnica autorizada y de lectura |
|---|---|---|
| Facturación | Operación intentada, estado visible, mensaje depurado y pantalla concreta. | Estado real, validaciones y respuesta del servicio fiscal, sin secretos ni documentos completos. |
| Pagos y contabilidad | Resultado esperado, estado visible y si el pago ya figura registrado. | Relaciones entre registros y conciliaciones; revisión contable humana si hay implicaciones fiscales. |
| Ventas y precios | Pantalla, contexto de moneda/lista y diferencia cualitativa, sin importes innecesarios. | Reglas y configuración aplicables; confirmar qué explica la diferencia. |
| Inventario | Tipo de movimiento, estado y ubicación genérica si basta. | Movimientos y reservas pertinentes; no provocar nuevos movimientos. |
| Compras y contactos | Qué busca y desde qué operación, sin datos personales del contacto. | Visibilidad, relaciones y configuración; no crear registros de prueba. |
| Accesos | Opción ausente y si el problema afecta solo a su acceso. | Permisos efectivos en el ámbito autorizado; cambios a cargo del responsable humano. |
| Informes | Filtros, período relativo y resultado esperado, sin exportar datos masivos. | Dominio de consulta, alcance y consistencia de los registros necesarios. |
| Conectividad | Acción, alcance y momento aproximado del fallo. | Salud del servicio y registros técnicos mínimos; nunca volcar registros completos al chat. |

**Respuesta funcional:** explicar navegación, filtros, estados o conceptos con una
fuente funcional vigente. Presentar una hipótesis como hipótesis y pedir confirmación;
no asegurar una causa solo porque una respuesta histórica la mencione.

**Investigación técnica de solo lectura:** cuando la evidencia visible no alcanza,
consultar únicamente información necesaria dentro de una instancia ya autorizada.
Diferenciar dato observado, explicación probable y causa confirmada. Una explicación
no validada termina como pendiente, no como «resuelto».

**Escalamiento humano:** permisos, decisiones contables/fiscales, cambios, evidencia
contradictoria, datos sensibles o acceso técnico no disponible. La derivación conserva
lo ya reunido y dice qué falta, sin pedir que el usuario repita todo.

## Recorrido propuesto: hasta cinco pasos visibles

Son cinco etapas de interacción, **no cinco consultas técnicas ni una garantía de
diagnóstico**. Cada etapa puede tener subpreguntas o subcomprobaciones de lectura.
Si no aportan evidencia nueva o exceden el alcance autorizado, se detiene y deriva.

### 1. Elegir qué necesita

Opciones: **«Cómo se hace» · «Algo no funciona» · «Revisar un resultado» · «Otro»**.
Después, seleccionar una familia de la tabla o **«No sé»**. Recuperar el contexto
ya compartido desde WhatsApp, incluida una URL previa si existe.

Salida: orientar la consulta o pasar a precisar el síntoma. Si pide un cambio real,
registrar la necesidad y derivarla; no convertirla en una acción automática.

### 2. Ubicar la operación

Opciones: **«Estoy en la pantalla» · «No puedo entrar» · «No tengo el enlace»**.
Solo si hace falta localizar la operación y no hay una URL útil, pedir el enlace
concreto de la pantalla de Odoo. Si ya se aportó, reutilizarlo y confirmar únicamente
si cambió la pantalla o el contexto. Evitar reenviar enlaces con información sensible.

La URL es una pista de contexto: **no acredita identidad, empresa ni autorización**.
Un servicio controlado debe asociarla con una instancia previamente autorizada;
nunca usar su dominio como destino SSH arbitrario ni seguir enlaces externos libres.
Si no se puede establecer el ámbito autorizado, detener la investigación técnica.
Sin enlace, continuar orientación general o derivar; no bloquear toda ayuda funcional.

### 3. Precisar qué ocurre

Opciones: **«Aparece un error» · «Falta una opción» · «El resultado difiere» ·
«No sé cómo continuar»**. Preguntar qué esperaba y qué ve; según la familia, pedir
estado, filtros o momento aproximado. Solicitar mensaje depurado o captura recortada
solo si aporta información necesaria y existe un canal adecuado.

Reutilizar datos y URL de los pasos anteriores. No pedir contraseñas, tokens,
comprobantes completos, importes ni identidades para clasificar el síntoma.
Salida: responder funcionalmente si hay fundamento, investigar con autorización
si falta evidencia técnica, o detener y escalar si aparece información sensible.

### 4. Explicar o investigar sin modificar

Opciones: **«Ver orientación» · «Solicitar revisión de solo lectura» · «Hablar con soporte»**.
La selección expresa intención, pero no sustituye controles de autorización.
La revisión técnica exige identidad, ámbito y permisos verificados por un mecanismo
aprobado; si aún no existe, esta opción debe derivar a soporte, no abrir conexiones.

Si se habilita SSH, usar acceso preconfigurado, restringido y de solo lectura.
No instalar, reiniciar, ejecutar correcciones, editar configuración, emitir documentos,
conciliar ni modificar datos. Tampoco pedir al usuario que reproduzca una operación
que pueda duplicar registros o generar efectos fiscales para obtener evidencia.

Los subchequeos pueden volver a preguntas de los pasos 2 o 3 conservando lo reunido,
no pedir otra vez la URL salvo cambio real. Sin conexión SSH, sin permisos o ante
un dato sensible, detener los chequeos y preparar una derivación humana clara.
Una investigación inconclusa debe decirlo explícitamente.

### 5. Elegir cómo seguir y volver a WhatsApp

Mostrar un resumen breve: necesidad, evidencia mínima, comprobaciones realizadas,
conclusión o hipótesis, límites y próximo responsable.
Opciones: **«Me sirvió» · «Sigue igual» · «Necesito una persona» · «Salir»**.

«Me sirvió» registra confirmación del usuario, no prueba técnica de una reparación.
«Sigue igual» permite precisar el síntoma sin empezar de cero o derivar si no hay
nuevas comprobaciones seguras. «Necesito una persona» y los límites anteriores
cierran la automatización con escalamiento; «Salir» permite cerrar sin conclusión.

Ofrecer **«Volver a WhatsApp»** con continuidad del caso y un resumen mínimo,
mediante un mecanismo que no exponga datos sensibles en enlaces ni una sesión ajena.
Conservar el contexto necesario bajo acceso controlado, sin repetir registros técnicos,
secretos o enlaces privados en un mensaje público. La derivación debe indicar
que no hubo modificaciones y qué evidencia aún falta.

## Componentes conceptuales y alcance inicial

| Componente propuesto | Responsabilidad, sin decisión de tecnología |
|---|---|
| Entrada y continuidad | Recuperar el caso de WhatsApp y devolver un resumen con acceso controlado. |
| Guía de cinco etapas | Opciones simples, preguntas condicionales y reutilización del contexto. |
| Resolución de ámbito | Verificar identidad, autorización y correspondencia de instancia; validar enlaces como pistas. |
| Orientación funcional | Contenido revisado, con límites explícitos y sin usar respuestas históricas como autoridad. |
| Investigación de lectura | Subchequeos acotados, evidencia mínima y estados de acceso no disponible. |
| Derivación y trazabilidad | Registrar qué se observó, qué no se pudo verificar y quién continúa, sin secretos. |

**MVP propuesto:** clasificación de las familias observadas, orientación funcional
revisada, captura mínima de evidencia y derivación con continuidad a WhatsApp.
Preparar preguntas específicas para facturación, pagos, existencias y accesos porque
aparecen en el barrido y tienen señales en la muestra; esto no es un ranking validado.
Mantener «Otro» y soporte humano para no forzar categorías.

La investigación automática por SSH queda condicionada a validar permisos, acceso
real de solo lectura y un conjunto pequeño de comprobaciones revisadas.
Hasta entonces, el MVP puede reunir contexto y derivar la investigación a una persona.
Quedan fuera correcciones automáticas, cambios productivos, acceso arbitrario,
capacitación con transcripciones privadas y promesas de resolución para toda consulta.

## Decisiones abiertas antes de aprobar

- Validar las familias y preguntas con soporte y usuarios; codificar una muestra
  semánticamente y contrastar causas/resultados con evidencia, no con respuestas del bot.
- Definir identidad, autorizaciones por instancia y responsables del acceso técnico;
  aprobar qué subchequeos son realmente de solo lectura y cuándo deben detenerse.
- Acordar canal privado para capturas, retención, acceso y borrado de datos; decidir
  qué contexto mínimo vuelve a WhatsApp y cómo se vincula sin exposición.
- Elegir responsables y tiempos de escalamiento, fuentes funcionales revisadas y
  criterios de evaluación: utilidad, derivación segura y ausencia de modificaciones.

## Tarea 39775

Esta síntesis sirve de insumo de diseño para la tarea **39775**, no sustituye su
aprobación. La referencia remota y cualquier adjunto del original se gestionan en
Odoo por separado, únicamente con acceso privado verificado. Este documento público
no publica el original, sus ubicaciones privadas ni enlaces a instancias de clientes.
