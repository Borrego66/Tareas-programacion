## 1. Conceptos básicos

* ¿Qué es un sensor? Es el dispositivo encargado de darle sensibilidad a la maquina osea se encarga de medir y de avisar si hay un cambio fisico o quimico por ejemplo calor, luz, distancia o presión y luego las convuierte en señales electricas.
* ¿Qué es un actuador? Es el encargado de hacer las cosas si los sensores son los ojos el actuador son los musculos lo cuales reciben la señal electrica y lo transforma en una accion fisica como giro o empuje.
* Diferencias: Mientras el sensor interpreta y manda señales el actuador ejecuta lo que las señales le indican
* Función en un sistema mecatrónico: Permite que el sistema actue de manera independiente sin intervencion manual
* Ejemplo sencillo (Foco de proximidad):
* Sensor:Es el encargado de mandar señales en caso de que algo intervenga en su campo de vision
* Actuador:Seria el foco el cual al recibir la señal electrica este se prenderia


## Investigación de sensores

| Tipo de sensor | Variable que mide | Principio de funcionamiento | Ejemplo comercial | Aplicación real |
| --- | --- | --- | --- | --- |
| Temperatura | Nivel de calor | Termistor / Termopar: Su resistencia eléctrica cambia proporcionalmente según el calor ambiente, o generan milivoltios al calentar dos metales distintos. | LM35, DHT11, PT100 | Control térmico en hornos industriales o climatización. |
| Luz | Intensidad luminosa  | Fotorresistencia / Fotodiodo: La incidencia de luz excita electrones, disminuyendo la resistencia eléctrica o generando una pequeña corriente. | LDR GL5528 | Encendido automático del alumbrado público al anochecer. |
| Proximidad | Presencia de un objeto cercano sin contacto | Inductivo / Capacitivo: Generan un campo electromagnético o eléctrico; si un objeto interrumpe el campo, altera su oscilación y dispara una señal. | Sensor Inductivo LJ12A3-4-Z/BX | Detección de piezas metálicas en bandas transportadoras. |
| Distancia | Longitud entre el sensor y un obstáculo | Tiempo de vuelo : Emite un pulso  y cuenta los microsegundos que tarda en rebotar y regresar al receptor. | HC-SR04  | Sensores de reversa y estacionamiento en automóviles. |
| Presión | Fuerza ejercida sobre un área | Piezorresistivo: Utiliza un diafragma que se deforma con la presión, estirando resistencias internas y cambiando su conductividad. | BMP280, MPX2010 | Altímetros en drones o monitoreo de neumáticos. |
| Humedad | Vapor de agua en el aire | Capacitivo: Utiliza un material dieléctrico  entre dos placas. Al absorber agua, cambia la capacitancia del circuito. | DHT22, SHT31 | Estaciones meteorológicas e invernaderos automatizados. |
| Posición | Ángulo o ubicación lineal exacta | Óptico / Magnético : Un disco con ranuras corta un haz de luz al girar. Contando los "cortes", se sabe exactamente cuánto ha rotado. | Encoder Rotativo E6B2-CWZ6C | Conocer el ángulo exacto de la articulación de un brazo robótico. |
| velocidad o movimiento | Aceleración lineal y rotación | Sistemas MEMS : Micro-masas de silicio suspendidas en resortes que se desplazan por inercia al moverse, cambiando la capacitancia. | MPU6050  | Estabilización de vuelo en drones o rotación de pantalla en celulares. |
|Fuerza o peso | Fuerza mecánica, deformación | Galga extensiométrica: Un alambre muy fino en zig-zag adherido a un metal. Cuando el metal se dobla por el peso, el alambre se estira y aumenta su resistencia. | Celda de carga HX711 | Básculas industriales y balanzas electrónicas de supermercado. |
![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4jUgD2-aJ911r4eiHayQH-zH2THAAvRxb1SU9Fw4__w&s=10)

## Clasificación de sensores

### Analógicos vs. Digitales:
* La característica que los clasifica es la naturaleza de la señal de salida que entregan.
* Los sensores analógicos entregan un rango continuo de valores (por ejemplo, de 0 a 3 voltios), lo que permite interpretar infinitas variaciones intermedias. Los *digitales* procesan internamente la lectura y entregan datos discretos, ya sea en forma de pulsos (0 y 1) o mediante un protocolo de comunicación de datos listo para el microcontrolador (I2C, SPI).


* De contacto vs. Sin contacto:
* La característica es la necesidad de interacción física mecánica con el objeto medido.
* Los de *contacto* (como un final de carrera o una celda de carga) requieren tocar físicamente el objeto para medir deformación, tope o temperatura directa. Los *sin contacto* (ultrasónicos, ópticos, infrarrojos) utilizan ondas sonoras, campos magnéticos o luz para detectar características a distancia, sin desgaste mecánico.


* Activos vs. Pasivos:
* La característica es si el sensor requiere aportar energía externa (emisión) para realizar la medición.
* Los sensores activos emiten energía hacia el entorno (como un pulso láser en un LiDAR o ultrasonido) y miden el reflejo. Los sensores *pasivos* no emiten nada, simplemente reciben la energía del entorno natural (como un termopar recibiendo calor o una LDR recibiendo luz ambiental).



## Investigación de actuadores

| Actuador | Energía utilizada | Movimiento | Ventaja | Limitación | Aplicación |
| --- | --- | --- | --- | --- | --- |
| Motor DC | Eléctrica | Rotatorio continuo | Control muy sencillo y económico, alta velocidad. | No tiene precisión de posición por sí solo (gira libremente). | Tracción en ruedas de robots móviles o ventiladores. |
| Servomotor | Eléctrica | Rotatorio angular preciso (ej. 0° a 180°) | Mantiene una posición angular exacta sin sistemas externos (retroalimentación interna). | Movimiento limitado (la mayoría no giran 360° continuos). | Dirección de vehículos RC o dedos de prótesis robóticas. |
| Motor paso a paso | Eléctrica | Rotatorio en fracciones discretas (pasos continuos) | Giro de 360° continuos con altísima precisión de posición y torque a bajas RPM. | Puede perder pasos ("desincronizarse") si se somete a mucha carga física repentina. | Movimiento de ejes y extrusores en impresoras 3D. |
| Solenoide| Eléctrica | Lineal corto (empuje/tirón) | Respuesta prácticamente instantánea. | Carrera física muy corta (escasos centímetros o milímetros). | Pestillos de cerraduras electrónicas inteligentes. |
| Cilindro neumático | Aire comprimido (Neumática) | Lineal | Muy rápidos, limpios y no generan chispas eléctricas. | Requiere compresores, válvulas y mangueras voluminosas. | Expulsión o empuje de piezas defectuosas en fábricas. |
| Cilindro hidráulico| Aceite a presión (Hidráulica) | Lineal | Produce fuerzas brutales capaces de mover toneladas. | Lentos, sucios (riesgo de fuga de aceite), mantenimiento costoso. | Maquinaria pesada como excavadoras o prensas industriales. |
![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm4juSZEQn_KgL2KDFGozgOeS1lv2eeznlDgH_DMxFHCmG9Gbjkfo1Vvw&s=10)
## Comparación de actuadores

* Motor DC y servomotor:
* Diferencia: El motor DC gira continuamente mientras tenga energía; el servomotor se mueve a un ángulo específico ordenado y se detiene allí manteniendo fuerza.
* Elección: Para hacer girar la hélice de un barco a control remoto, elegiría el Motor DC (necesita rotación continua a altas RPM). Para mover el timón del mismo barco, elegiría el Servomotor (necesito fijarlo exactamente a 15° a la izquierda).


* Servomotor y motor paso a paso:
* Diferencia: Ambos son precisos, pero el servo usa un sensor interno para saber siempre dónde está (lazo cerrado) con giro limitado. El motor paso a paso gira 360° continuos recibiendo secuencias eléctricas precisas, pero no sabe si un obstáculo lo frenó (lazo abierto).
* Elección: Para una articulación de brazo robótico industrial elegiría el Servomotor (si choca con algo, corrige su posición automáticamente). Para una fresadora CNC elegiría un Motor paso a paso (requiere rotar tornillos sin fin dando cientos de vueltas continuas con precisión micrométrica).


* Actuador neumático y actuador hidráulico:
* Diferencia: El neumático usa aire, siendo muy veloz y limpio pero con fuerza moderada. El hidráulico usa líquidos (incompresibles), siendo más lento pero generando fuerzas inmensas.
* Elección: Para una empacadora de alimentos que debe sellar 100 cajas por minuto, usaría el Neumático (rápido y el aire no contamina la comida). Para levantar plataformas de 5 toneladas de vehículos, usaría el Hidráulico (el aire cedería por el peso, el líquido no).



## Sensores y actuadores en un sistema real

Sistema seleccionado: Robot Móvil Autónomo (AGV - Vehículo de Guiado Automático para Almacenes)

* Sensor 1: LiDAR 2D (Sensor de Distancia/Mapeo). Escanea 360° a su alrededor para detectar paredes y obstáculos, enviando el mapa al cerebro del robot.
* Sensor 2: Encoders ópticos (Posición/Velocidad). Van pegados a las ruedas traseras. Miden cuántas vueltas exactas han dado las ruedas para que el robot sepa la distancia real recorrida (Odometría).
* Sensor 3: Bumper de impacto (Final de carrera mecánico). Va en la defensa delantera. Si el robot choca suavemente contra algo imprevisto, este sensor mecánico corta la energía por seguridad.
* Actuador 1: Motor DC Derecho (con caja reductora). Proporciona la tracción de la rueda derecha.
* Actuador 2: Motor DC Izquierdo (con caja reductora). Proporciona la tracción de la rueda izquierda. La combinación de velocidad de ambos motores le permite girar y avanzar.
* Actuador 3: Alarma acústica (Buzzer/Sirena). Emite un sonido físico de advertencia cuando el robot va en reversa.


## ¿Que componente usarias en las siguientes situaciones?

Detectar si una persona se encuentra frente a una puerta automática:El sensor de proximidad
el cual lo hace atraves de un campo magnetico que cuando es itervenido se activa

Medir la temperatura dentro de un salón: Un termo par

Detectar el nivel de agua de un depósito:Usando un Piezorresistivo poniendolo al fondo del deposito

Mover una rueda de un robot móvil: Usando un motor DC

Controlar con precisión el ángulo de una pequeña articulación robótica:

Empujar una pieza en una línea de producción: Usando un cilindro neumatico el cual funciona con aire comprimido

Medir la distancia entre un robot y una pared: Sensor de distacia el cual manda un pulso y cuenta cuanto tarda en que regrese

Detectar si una habitación está iluminada: Una foto resistecia la cual mide la intensidad de los fotones

## Reflexión final 

Es muy importante saber los tipos de sensores y actuadores ya que gracias a ellos es como se conforma un ambiente automatico osea que no tenga interferecia manual por ejemplo la puerta de proximidad consta de un y de un sensor actuadore un motor DC el cual se encarga de abrir las puertas y un sensor de proximidad el cual se encarga de avisar cuando abrir las puertas es asi como sin un interferencia manual funciona.Ahora imaginalo a mas escala por ejemplo un tinaco el cual solo empiece a llenarse cuando este por la mitad como se daria cuenta con sensor de presion el cual le indicaria a un cervo motor cuando abrir la llave de paso para que se llene este.En resumen es importante saber que componentes llevan hacia la automatizacion ya que gracias a estos podemos hacer trabajos mas sencillos y sin esfuerzo.

## Referencias

[1] R. Siegwart, I. R. Nourbakhsh y D. Scaramuzza, *Introduction to Autonomous Mobile Robots*, 2.ª ed. Cambridge, MA, EE. UU.: MIT Press, 2011. [En línea]. Disponible: [https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/](https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/)

[2] B. Siciliano, L. Sciavicco, L. Villani y G. Oriolo, *Robotics: Modelling, Planning and Control*. Londres, Reino Unido: Springer, 2009. [En línea]. Disponible: [https://link.springer.com/book/10.1007/978-1-84628-642-1](https://link.springer.com/book/10.1007/978-1-84628-642-1)

[3] Texas Instruments, "LM35 Precision Centigrade Temperature Sensors", Hoja de datos, Oct. 2017. [En línea]. Disponible: [https://www.ti.com/lit/ds/symlink/lm35.pdf](https://www.ti.com/lit/ds/symlink/lm35.pdf)

[4] W. Bolton, *Mecatrónica: Sistemas de control electrónico en la ingeniería mecánica y eléctrica*, 5.ª ed. Ciudad de México, México: Alfaomega, 2013. [En línea]. Disponible: [https://books.google.com.mx/books?id=f_oRngEACAAJ](https://www.google.com/search?q=https://books.google.com.mx/books%3Fid%3Df_oRngEACAAJ)