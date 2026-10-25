# Plan director · Célula IA 2026

> 🧭 **Documento en construcción.** Base de coordinación del portafolio de IA de Hitofusion. La estructura propone prácticas de gestión alineadas con PMBOK; no constituye una aprobación del plan ni una certificación de cumplimiento.

## 🎯 Visión y objetivos {#vision}

Impulsar la hiperproductividad de Hitofusion, investigar y desarrollar agentes, y unificar las iniciativas de inteligencia artificial de la empresa.

### Objetivos del plan

- Establecer los lineamientos fundamentales de la célula.
- Compartir definiciones y criterios de trabajo.
- Construir una hoja de ruta común para todos los proyectos.

**Estado:** borrador inicial. Línea base, indicadores y metas: **por definir y aprobar**.

## 🗂️ Alcance y portafolio {#portafolio}

El alcance inicial comprende hiperproductividad interna, I+D en agentes y unificación de las IA. El siguiente inventario reproduce las iniciativas del borrador; no afirma que estén iniciadas o aprobadas.

| Ámbito | Iniciativa | Situación documentada |
| --- | --- | --- |
| Interno | [Atención al cliente · JZ1](#j1-calidad) | Asistencia implementada; mejoras de calidad por definir |
| Interno | Soporte · JZ2 | Identificada; alcance y estado por relevar |
| Interno | [Migrador](#migrador) | En construcción; todavía no debe ser tomada |
| Interno | [Implementador y posimplementación](#post-implementacion) | Etapa 2: requisitos y contexto por documentar; alcance por definir |
| Transversal | Iniciativa para toda la empresa | Por definir; Ale la trabajará inicialmente |
| Externo | APX y JZ plataforma | Identificada; alcance y estado por relevar |
| Externo | Ambiente de desarrollo de sistemas en general | Referencias del borrador: Kelo, Guille, Hito, devman; alcance por relevar |

> 💡 **Lectura del portafolio:** una iniciativa identificada no equivale a un proyecto autorizado. Cada proyecto necesita acordar su resultado, responsable, recursos y criterio de aceptación.

### J1 · Calidad de respuestas por WhatsApp {#j1-calidad}

La asistencia de primera línea de J1 (JZ1 en el inventario) está implementada; esta iniciativa propone mejorar la calidad de la conversación actual, no crear otro proyecto de asistencia.

**Objetivo:** acordar un estándar de calidad de Hito para respuestas concretas y pertinentes.

**Alcance propuesto:**

- Definir entre **10–20 casos de uso core**, con la calidad esperada explícita para cada uno.
- Lograr un comportamiento robusto en los casos de uso no core.
- Prever el aporte de MAPE-K a la mejora continua; su integración no está implementada como parte de esta iniciativa.

**Pendiente:** definir el alcance, los umbrales de calidad y las decisiones técnicas. No se asignan responsables ni se comprometen fechas.

**Separación de alcance:** mejorar la conversación actual es distinto de la aplicación web de diagnóstico de la tarea 39775.

**Seguimiento:** [tarea 39784 · J1 · Calidad de respuestas](https://www.hitofusion.com/web#id=39784&cids=10&menu_id=114&action=198&active_id=378&model=project.task&view_type=form).

### Agente migrador {#migrador}

> Esta tarea está en construcción y todavía no debe ser tomada.

**Objetivo:** asistir en la migración de Odoo, como parte de la iniciativa Migrador ya inventariada.

**Alcance:** pendiente de más detalles. La documentación detallada y las referencias requieren acceso autorizado en Odoo.

**Seguimiento:** [tarea 39779 · Agente migrador](https://www.hitofusion.com/web#id=39779&cids=10&menu_id=114&action=198&active_id=378&model=project.task&view_type=form).

### Agente post implementación · Etapa 2 {#post-implementacion}

**Objetivo:** continuar el trabajo de postimplementación asociado al agente de implementación, relevando las necesidades de clientes e implementadores. Atender esas necesidades es una aspiración, no un compromiso de alcance ilimitado ni una afirmación de que ya estén todas identificadas. El nombre de la etapa no implica que la anterior haya concluido.

**Estado:** requisitos y contexto pendientes de documentar; no se afirma que la implementación haya comenzado.

**Trabajo inicial:** documentar los requisitos y el contexto; a partir de ellos, definir objetivos, alcance y exclusiones, y tareas.

**Pendiente:** acordar alcance, funciones, estrategia e implementación técnica. No hay responsables asignados ni fechas comprometidas para esta etapa.

**Seguimiento:** [tarea 39786 · Agente post implementación · Etapa 2](https://www.hitofusion.com/web#id=39786&cids=10&menu_id=114&action=198&active_id=378&model=project.task&view_type=form).

## Capacidades transversales para agentes {#capacidades}

MAPE-K y Testing son capacidades propuestas para servir a varios agentes del portafolio, **no nuevos proyectos independientes**. Sus requisitos iniciales están registrados en Odoo; el alcance detallado y las decisiones técnicas siguen pendientes. No se afirma que su implementación haya comenzado. No hay herramientas seleccionadas, responsables asignados ni fechas comprometidas para estas capacidades.

### MAPE-K · supervisión, auditoría y alertas

**Objetivo:** investigar una capacidad de supervisión de agentes que permita observar su funcionamiento, auditar resultados y definir alertas ante comportamientos problemáticos. Un caso a relevar es el agente que repite preguntas sin dar una respuesta ni generar un ticket.

**Fases iniciales propuestas:**

1. Investigar MAPE-K y relevar necesidades de supervisión comunes a varios agentes.
2. Acordar el alcance inicial y los criterios para auditar y alertar.
3. Diseñar la solución y evaluar alternativas técnicas.
4. Implementar y validar lo que se apruebe, después de esas definiciones.

**Pendiente:** precisar qué observar, qué situaciones requieren alertas y cómo evaluar los resultados; decidir arquitectura y herramientas sin anticipar su elección.

**Seguimiento:** [tarea 39776 · MAPE-K](https://www.hitofusion.com/web#id=39776&cids=10&menu_id=114&action=198&active_id=378&model=project.task&view_type=form).

### Testing · simulaciones repetibles y regresión

**Objetivo:** definir una capacidad de pruebas para varios agentes mediante simulaciones de usuarios repetibles y pruebas de regresión. Debe permitir evaluar casos como las preguntas reiteradas sin respuesta o ticket y comparar resultados al cambiar un agente.

**Fases iniciales propuestas:**

1. Relevar necesidades y estudiar la referencia existente de J1.
2. Acordar escenarios, alcance y criterios de aceptación de las pruebas.
3. Diseñar el enfoque de simulación y regresión; evaluar herramientas.
4. Implementar y validar el alcance aprobado.

**Pendiente:** definir qué agentes y flujos cubrir inicialmente, qué resultados comparar y qué tecnología usar. La referencia no implica una elección técnica para esta capacidad.

**Referencia disponible:** [guía del simulador de conversaciones de tickets de J1](https://github.com/hito2026/hito-celulaia-proyectos2026/blob/main/docs/j1/jinzo-whatsapp-ticket-simulator.md). Documenta un simulador preexistente del flujo de tickets, **no la implementación de la nueva aplicación de diagnóstico**. Se publica como referencia documental; sus comandos y resultados de pruebas pertenecen al proyecto de origen y no se han ejecutado ni validado en esta publicación.

**Seguimiento:** [tarea 39777 · Testing](https://www.hitofusion.com/web#id=39777&cids=10&menu_id=114&action=198&active_id=378&model=project.task&view_type=form).

## 👥 Gobierno y responsabilidades {#gobierno}

### Organización indicada en el borrador

| Persona | Función expresada | Pendiente de precisar |
| --- | --- | --- |
| Ale | Director general; inicialmente también PM | Dedicación y facultades de aprobación |
| Fran | Toma proyectos para llevarlos adelante | Proyectos asignados y responsabilidades |
| Gena | Toma proyectos para llevarlos adelante | Proyectos asignados y responsabilidades |

### Acuerdos de gobierno propuestos

- Identificar patrocinador, interesados y responsable de cada proyecto.
- Acordar quién propone, quién ejecuta y quién aprueba; registrar una matriz RACI.
- Registrar decisiones, dependencias y cambios antes de modificar una línea base aprobada.
- Definir cadencia de seguimiento, canal de comunicación y escalamiento.

Estos acuerdos son **propuestas por validar**, no nuevas asignaciones.

## 🧩 Ficha de proyecto {#ficha}

Plantilla propuesta para completar cada iniciativa antes de incorporarla a una línea base.

| Elemento de gestión | Información que se debe acordar |
| --- | --- |
| Justificación y beneficios | Problema, resultado esperado, beneficiarios e indicador de valor |
| Acta de constitución | Patrocinador, PM, autorización y objetivos medibles |
| Alcance | Entregables, exclusiones, requisitos y criterios de aceptación |
| Trabajo | EDT/WBS y paquetes de trabajo con responsables |
| Cronograma | Hitos, estimaciones, dependencias y fechas aprobadas |
| Costos y recursos | Presupuesto, capacidad disponible y necesidades de adquisición |
| Calidad | Definición de terminado, pruebas y evidencia de aceptación |
| Riesgos | Probabilidad, impacto, respuesta y responsable |
| Interesados y comunicación | Necesidades, frecuencia, canal y decisiones requeridas |
| Cambios y cierre | Aprobaciones, transferencia operativa y lecciones aprendidas |

**Estado común inicial:** todos los campos que no estén respaldados por el borrador siguen pendientes. No hay presupuestos, fechas ni metas aprobadas en esta versión.

## 🗺️ Hoja de ruta {#ruta}

Secuencia de trabajo **propuesta, sin fechas comprometidas**. La prioridad relativa de las iniciativas todavía debe acordarse.

1. **Relevar:** completar el inventario, necesidades e interesados.
2. **Definir:** redactar actas, alcance, beneficios y criterios de aceptación.
3. **Priorizar:** contrastar valor, esfuerzo, riesgos y dependencias con la capacidad disponible.
4. **Planificar:** acordar responsables, EDT, hitos, costos y líneas base.
5. **Ejecutar y controlar:** entregar resultados y comparar avances con lo aprobado.
6. **Cerrar y aprender:** validar beneficios, transferir operación y registrar aprendizajes.

## 📊 Seguimiento y control {#seguimiento}

Tablero propuesto para las reuniones de seguimiento; frecuencia y responsables por acordar.

| Dimensión | Evidencia esperada | Situación inicial |
| --- | --- | --- |
| Valor | Indicador y beneficio observado por proyecto | Por definir |
| Alcance y calidad | Entregables aceptados y pruebas | Sin línea base |
| Plazos | Hitos previstos y reales | Sin fechas acordadas |
| Costos y capacidad | Presupuesto y dedicación real | Por estimar |
| Riesgos y bloqueos | Registro con responsable y respuesta | Por construir |

### Riesgos a evaluar, no incidentes confirmados

- Superposición entre iniciativas y dependencias no relevadas.
- Capacidad insuficiente frente a la demanda del portafolio.
- Uso de datos sensibles o accesos no autorizados en soluciones de IA.
- Calidad de respuestas de agentes y supervisión humana insuficiente.

> 🔒 **Documentación pública:** no incorporar credenciales, datos de clientes, información personal sensible ni detalles confidenciales. Los registros restringidos deben mantenerse fuera de este repositorio público.

## ✅ Decisiones pendientes {#decisiones}

- [ ] Validar objetivos, alcance y definiciones comunes de la célula.
- [ ] Definir la iniciativa transversal que Ale trabajará inicialmente.
- [ ] Relevar el estado real de cada iniciativa y sus dependencias.
- [ ] Acordar patrocinadores, responsables y capacidad de Fran y Gena.
- [ ] Aprobar prioridades, presupuesto, hitos e indicadores de beneficio.
- [ ] Acordar cadencia de seguimiento y circuito de aprobación de cambios.

## 📚 Referencias y mantenimiento {#referencias}

- **Fuente inicial:** [borrador original](plan_directo/borrador_original.md), conservado sin modificaciones.
- **Marco de referencia:** [PMBOK · Project Management Institute](https://www.pmi.org/standards/pmbok). La edición y el grado de adaptación deberán acordarse; no se reproduce contenido normativo del estándar.
- **Fuente editable del sitio:** `plan_directo/plan_director.md`. Los cambios publicados en `main` actualizan la documentación mediante GitHub Pages.
- **Control documental:** el historial de Git registra versiones; las propuestas no se convierten en decisiones aprobadas sin dejar constancia explícita.
