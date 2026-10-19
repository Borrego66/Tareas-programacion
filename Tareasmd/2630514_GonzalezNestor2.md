# Guía Integral de Metodologías Ágiles: Scrum, Kanban y Design Thinking


## Resumen 

El enfoque "ágil" en el desarrollo de proyectos y software surge como respuesta a los modelos tradicionales en cascada (Waterfall), los cuales resultaban rígidos y propensos al fracaso ante cambios en los requerimientos del cliente. La agilidad es una mentalidad basada en la entrega iterativa e incremental, la colaboración estrecha con el cliente y la adaptabilidad frente a la incertidumbre. Este documento cubre los principios fundamentales de la agilidad y profundiza en tres marcos de trabajo complementarios: **Scrum**, **Kanban**  y **Design Thinking**.

## Principios Ágiles

La agilidad se fundamenta en el Manifiesto Ágil, el cual prioriza 4 valores clave:

1. Individuos e interacciones sobre procesos y herramientas.
2. Software funcionando sobre documentación extensiva.
3. Colaboración con el cliente sobre negociación contractual.
4. Respuesta ante el cambio sobre seguir un plan.

Estos valores se apoyan en 12 principios que impactan la gestión del trabajo al descentralizar la toma de decisiones, fomentar equipos auto-organizados, promover entregas tempranas y frecuentes (para obtener feedback rápido), y mantener un ritmo de trabajo sostenible que garantice la calidad técnica.

## Panorama de Marcos Ágiles

* Scrum: Marco de trabajo iterativo e incremental basado en ciclos de tiempo fijo llamados *Sprints*. Cuándo elegirlo: En proyectos de desarrollo de productos con alta incertidumbre, donde se requiere estructura, retroalimentación frecuente y entregas periódicas.
* Kanban: Método visual para gestionar el trabajo a medida que fluye por un proceso. Cuándo elegirlo: En entornos de mantenimiento, soporte técnico o tareas con alta variabilidad donde los requerimientos llegan de forma continua y no se pueden empaquetar en Sprints cerrados.
Design Thinking: Metodología centrada en el usuario para resolver problemas complejos mediante la empatía y la experimentación. Cuándo elegirlo: En la fase de descubrimiento (Discovery), antes de programar, cuando el problema no está bien definido o se busca innovar radicalmente.

## 4. Ventajas y Riesgos (Trade-offs)

| Marco | Beneficios Principales | Limitaciones y Riesgos | Trade-offs Típicos |
| --- | --- | --- | --- |
| Agilidad | Alta adaptabilidad, mayor satisfacción del cliente. | Riesgo de "scope creep" (aumento descontrolado del alcance). | Flexibilidad vs. Predictibilidad estricta. |
| Scrum| Entregas predecibles, mejora continua estructurada. | Exceso de reuniones; rigidez dentro del Sprint. | Estructura iterativa vs. Capacidad de reacción inmediata. |
| Kanban | Flexibilidad total, optimización de cuellos de botella. | Falta de fechas límite claras si no se gestiona bien. | Flujo continuo vs. Tiempos fijos de entrega (Timeboxing). |
| Design Thinking| Reduce el riesgo de construir un producto que nadie quiere. | Puede consumir mucho tiempo antes de generar código. | Innovación y validación vs. Velocidad de inicio técnico. |



## Scrum

### Conceptos Base

Scrum es un marco ligero que ayuda a las personas, equipos y organizaciones a generar valor a través de soluciones adaptativas para problemas complejos. Su propósito es entregar incrementos de producto utilizables iterativamente.

### Roles

* Product Owner (PO): Maximiza el valor del producto. Gestiona el Product Backlog. *Error frecuente:* Ser un "dictador" sin escuchar al equipo o estar ausente.
* Scrum Master (SM): Líder servicial que asegura que Scrum se entienda y se aplique, eliminando impedimentos. *Error frecuente:* Actuar como jefe de proyecto tradicional que asigna tareas.
* Development Team: Profesionales auto-organizados que construyen el incremento. *Error frecuente:* Comprometerse a más trabajo del que pueden realizar por presión externa.

### Artefactos

* Product Backlog: Lista ordenada de todo lo que se sabe que es necesario para el producto.
* Sprint Backlog: Elementos seleccionados del Product Backlog para el Sprint, junto con el plan para entregarlos.
* Increment: La suma de todos los elementos completados durante un Sprint que aportan valor.
* Definition of Done (DoD) vs Criterios de Aceptación: El DoD es un estándar de calidad global para todo el producto (ej. "Todo código debe tener pruebas automatizadas al 80%"). Los Criterios de Aceptación son requisitos específicos de una historia de usuario particular (ej. "El botón debe ser verde y enviar un correo").

### Eventos

* Sprint: Contenedor de todos los eventos (1 a 4 semanas). 
* Antipatrón: Cambiar el objetivo del Sprint a la mitad.
* Sprint Planning:(Máx. 8h para un Sprint de 1 mes). El equipo define qué se hará y cómo. *Antipatrón:* El PO asigna tareas específicas a desarrolladores.
* Daily Scrum: (15 min). Sincronización diaria del equipo. Antipatrón: Convertirlo en una reunión de reporte de estado (status report) hacia el Scrum Master.
* Sprint Review: (Máx. 4h). Inspeccionar el incremento y adaptar el Product Backlog. *Antipatrón:* Mostrar diapositivas en lugar de software funcionando.
* Sprint Retrospective: (Máx. 3h). Inspeccionar cómo le fue al equipo e identificar mejoras. *Antipatrón:* Culparse mutuamente sin generar planes de acción concretos.

### Métricas

* Velocity: Cantidad de trabajo (puntos de historia) completado por Sprint. *No debe usarse* para comparar equipos.
* Burndown Chart: Gráfico que muestra el trabajo restante a lo largo del tiempo.
* Work In Progress (WIP): Cantidad de ítems en progreso simultáneamente.



## Kanban

### Fundamentos

Kanban se basa en visualizar el trabajo, limitar el trabajo en progreso (WIP), gestionar y medir el flujo, hacer explícitas las políticas del proceso, implementar bucles de retroalimentación y mejorar colaborativa y evolutivamente.

### Tablero Kanban y Límites WIP

Propuesta para un equipo de desarrollo de 4 personas:

* Backlog: (Sin límite)
* Ready / To Do: (Límite: 5)
* Doing: (Límite: 4) - 
* Razón: Evita el cambio de contexto; 1 tarea por desarrollador.
* Code Review: (Límite: 2) - *Razón:* Fuerce a revisar antes de seguir programando, evitando cuellos de botella.
* Done: (Sin límite)

### Métricas de flujo

* Lead Time: Tiempo total desde que el cliente hace la petición hasta que se le entrega.
* Cycle Time: Tiempo desde que el equipo empieza a trabajar en la petición hasta que la termina.
* Throughput: Cantidad de ítems completados en un periodo de tiempo.
* Diagrama de Flujo Acumulado (CFD): Gráfico de áreas que muestra la cantidad de tareas en cada estado a lo largo del tiempo. Se lee observando el grosor de las franjas: franjas ensanchándose indican un cuello de botella.

### Políticas y Clases de Servicio

* Clases de servicio:** Ayudan a priorizar. Ejemplos: *Expedite* (Incidencias críticas de producción; ignoran límites WIP), *Fixed Date* (Campañas de marketing), *Standard* (Historias de usuario normales).
Cuándo usar Kanban: Cuando el trabajo es reactivo (Soporte, DevOps), hay alta variabilidad en los requerimientos o madurez suficiente para no requerir los timeboxes rígidos de Scrum.



## Design Thinking

### Visión General

Es una metodología centrada en el ser humano que utiliza herramientas del diseño para integrar las necesidades de las personas, las posibilidades tecnológicas y los requisitos para el éxito empresarial. En software, asegura que estamos construyendo el producto correcto (Discovery) antes de construirlo correctamente (Delivery).

### Fases

1. Empatizar: Comprender a los usuarios. *Técnicas:* Entrevistas, observación. *Entregable:* Mapa de empatía.
2. Definir: Centrar el problema. *Técnicas:* POV (Point of View), User Personas. *Entregable:* Declaración clara del problema.
3. Idear: Generar soluciones. *Técnicas:* Brainstorming, Crazy 8s. *Entregable:* Lista de ideas filtradas.
4. Prototipar: Hacer tangibles las ideas. *Técnicas:* Wireframes de papel, maquetas en Figma. *Entregable:* Prototipo funcional (baja o media fidelidad).
5. Probar: Validar con usuarios. *Técnicas:* Pruebas de usabilidad. *Entregable:* Feedback documentado e iteración.

### Mini-caso: App para el comedor universitario

* Problema: Largas filas en el comedor universitario provocan que estudiantes lleguen tarde a clases.
* Empatizar: Entrevistas revelan que el problema es el proceso de pago.
* Definir: "Los estudiantes necesitan una forma de pre-ordenar y pagar para solo recoger la comida".
* Idear: Se proponen varias opciones; gana la idea de una app de "Scan & Go" o pre-pedido.
* Prototipar: Bocetos en papel (low-fi) dibujando pantallas de menú, carrito y código QR de recolección.
* Probar: Se muestra el papel a estudiantes simulando clics; se ajusta el diseño del menú por ser confuso.

### Relación con SDLC / Ágil

Design Thinking opera en el espacio del problema (Descubrimiento). Una vez que el prototipo se valida, las ideas se traducen en un Product Backlog. Scrum o Kanban toman el relevo en el espacio de la solución (Entrega), permitiendo construir el software de forma ágil basándose en hipótesis ya validadas.



## Conclusiones

En conclusion: ¿Para que sirve esto? pues simple es para mantener un area de trabajo limpio en este caso para programar codigo para una tarea claro en este caso no sera de un momento a otro si no que sera gradual y escogiendo las mejores partes de cada una de estas practicas para asi sentirse comodo a la hora de programar




## Referencias

[1] K. Beck *et al.*, "Manifesto for Agile Software Development", 2001. [En línea]. Disponible: [https://agilemanifesto.org/](https://agilemanifesto.org/)

[2] K. Schwaber y J. Sutherland, "La Guía de Scrum", Nov. 2020. [En línea]. Disponible: [https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-Latin-South-American.pdf](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-Latin-South-American.pdf)

[3] D. J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*. Sequim, WA, EE. UU.: Blue Hole Press, 2010. [En línea]. Disponible: [https://books.google.com/books?id=b4XyBQAAQBAJ](https://www.google.com/search?q=https://books.google.com/books%3Fid%3Db4XyBQAAQBAJ)

[4] T. Brown, "Design Thinking", *Harvard Business Review*, vol. 86, no. 6, pp. 84-92, Jun. 2008. [En línea]. Disponible: [https://hbr.org/2008/06/design-thinking](https://hbr.org/2008/06/design-thinking)

[5] I. Sommerville, *Software Engineering*, 10.ª ed. Boston, MA, EE. UU.: Pearson, 2015. [En línea]. Disponible: [https://www.pearson.com/en-us/subject-catalog/p/software-engineering/P200000003239](https://www.google.com/search?q=https://www.pearson.com/en-us/subject-catalog/p/software-engineering/P200000003239)