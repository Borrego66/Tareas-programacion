# Conceptos basicos sobre robotica

## ¿Que es un robot movil, que lo diferencia y en que puede afectar el tipo de rueda selecto?

Un robot movil es una **maquina programada** la cual sigue inidicaciones atravez de un codigo prestablecido o constante el cual le da indicaciones de movimiento ya sea cordenadas, o de avanzar o no. Este se diferencia a un estatico ya que posee la capacidad de desplasarze en un entorno infinito dependiendo de las capacidades de este a eso se le llama sistema de locomocion el cual es un conjunto de mecanismos mecanicos y de propulsion encargados de mover el cuerpo del robot por ejemplo
* Ruedas
* Orugas
* Patas 

Estos se encargan de sostener el peso del robot de darle traccion y que mantenga su estabilidad.

Hay varios tipos de robots moviles como los **ackerman, diferenciales y omnidireccionales** los cuales son los mas interesantes ya que estos en un plano 2D pueden moverse hacia cualquier direccion sin cambiar su orientacion **gracias a sus ruedas conformadas por rodillos** las cuales le dan la posibilidad de hacerlo gracias a esta disposicion de ruedas a diferencia de otras como el **ackerman o el diferencial** por ejemplo el **ackerman es muy parecido al movimiento de un carro ya que dos de sus ruedas son de movimiento recto mientras las delanteras le dan la posibilidad de cambiar su direccion**, otro seria el **diferencial el cual esta conforme por dos ruedas la cual dependiendo hacia donde vaya le da mas pontecia a una rueda que otra de ahi viene el nombre de diferencial**
![imagen](https://www.fdatabot.com/wp-content/uploads/2026/06/differential-drive-vs-mecanum-vs-omni-wheel-robot-chassis-comparison.png)

## Robot diferencial con rueda de castor

### ¿Que es y por que esta conformado? 
Un robot diferencial esta conformado por dos ruedas las cuales son independientes una de otra osea que cada una puede mandar mas fuerza a una que otra osea que no hay un eje el cual las limite y la rueda de castor o rueda loca es la encargada de darle estabilidad al robot y no limitar su movilidad.

### ¿Entonces como se mueve? 
La manera en la que se moviliza el robot en linea recta es mandandole la misma fuerza hacia ambas ruedas (3,3) es como si fueras en un cayac para ir hacia adelante ocupas remar hacia ambos lados. 

¿Y como me muevo hacia otras direcciones?

Simple le mandas menos fuerza a una que a la otra por ejemplo si yo en un cayac remo mas fuerte del lado derecho que del izquierdo (2,3) me estaria desplazando hacia enfrente con una leve orientacion hacia la izquierda.

¿Y que sucederia si una llanta no se mueve?

Simple girarias hacia el lado contrario de la otra rueda volviendose la otra rueda en el eje de su giro. Por ejemplo estas en un cayac y no remas con los dos remos pues no hay desplazamiento hacia enfrente pero si lo hay hacia los lados, en este caso si solo remas del lado derecho y dejas el remo izquierdo en el agua el remo izquierdo (0,3) se volvera en el eje en el que girara el cayac osea si mandas fuerza hacia la derecha giraras a la izquierda.

¿Y que sucederia si una llanta se mueve hacia atras y la otra hacia delante?

Lo que sucederia es que se cancelarian haciendo que el robot en esta ocacion de vueltas en su propio eje y no en el de la rueda. Otra vez el ejemplo del cayac imaginate que son dos amigos ahora y ambos dan vuelta hacia el lado derecho (-3,3) lo que sucedaria es que se desplazarian en su mismo eje osea empezarian a dar vueltas.

![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbsZ6YRVWyOdTdqTz4NvKbnvCCWaZ8yWbz2x92UMChVQ&s=10)
### Tabla de movimientos de rueda
|Izquierda avanza|Derecha Avanza|Resultado|
|---|---|---|
|1|1|Se movera hacia enfrente|
|0|1|Girara hacia la derecha|
|1|0|Girara hacia la izquierda|
|1|-1|Dara vueltas en su propio eje hacia la derecha|
|-1|1|Dara vueltas en su propio eje hacia la derecha|
|-1|-1|Se movera hacia atras|

## Robots omnidireccionales con ruedas Omni Wheel

### Para empezar ¿Que es un robot omnidireccional?
Es un robot el cual puede ir hacia cualquier direccion y tu diras ¿y que con eso no puede hacer eso tambien el diferencial? Pues si y no pueden llegar al mismo lugar lo que lo diferencia es la eficiencia ya que el omni puede llegar ahi sin mover su chasis cosa que el diferencial tiene que hacer mientras el diferencial mueve su chasis para ir a la izquierda el omni no lo necesita ya que puede llegar al mismo punto sin mover ni una parte de su chasis 
### ¿Y como logra esto? 
Logra esto gracias a sus ruedas llamadas **omni wheel** las cuales son ruedas normales aparentemente pero tienen rodillos incorporados a 90° sin ofrecer ninguna inclinacion en ellas los cuales no son sometidos a fuerza por un motor directo a diferencia de una rueda normal ya que los rodillos son pasivos.Aun asi teniendo los rodillos puede generar tracion hacia adelante y hacia atras y moverse axialmente gracias a sus rodillos.
![Imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMRcJjn5Fk4be2i7KRBIppGw3Q7BI3AL3ewSSBIkCuHA&s=10)
Y tu diras okey por las ruedas ¿Pero como es posbile que haga esto solo con tres ruedas? Pues es gracias a su configuracion ya que cada rueda esta pocisionada a 120° una de otra apuntando sus ejes hacia el centro del robot
![Imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt1JzzwvNetXvYBuP3gP9YazrUkXK80lBHfTiLdcsNEA&s=10)
### ¿Y como se mueve?
* Hacia adelante/atras: Este es el mas sencillo la forma en la que lo hace es haciendo que una rueda se mueva solo atravez de sus rodillos (No tenga movimiento atravez del motor) mientras las otras dos se mueven en direcciones opuestas a la misma velocidad(0,-3,3) 

* Hacia el costado: La forma en la que se logra esto es numerando las ruedas por ejemplo la rueda uno sera la que este en el eje y la cual dara su maxima potencia mientras las otras dos iran negativamente contrarestando la rotacion del robot 
(3,-2,-2)

* Movimiento diagonal: Este se obtiene ajustando las velocidades de cada una usando una matriz de transformcaion trigonometrica. Asi haciendo que cada uno mande una mande cierta velocidad dependiendo del angulo deseado

Giro sobre su eje: Este es sin duda el mas simple solo tienen que ir todas las llantas a la misma velocidad en la misma direccion ya se a favor de las manesillas del reloj o en contra (3,3,3)

Diferentes velocidades: Cuando cada rueda tiene una velocidad diferente lo que sucedera es que empezara moverse realiza una combinacion de translacion en una direccion en especifico mientras hace una rotacion (hara un arco mientras gira en si mismo)

## Robot omnidireccional con ruedas Mecanum

### ¿Que es y como funciona un robot omnidireccional (mecanum)?
Este funciona gracias a sus ruedas las cuales contienen rodillos pasivos los cuales no son movidos por el motor directamnete si no que atravez del motor el cual mueve la rueda donde estan montados con la cualidad de que estan a 45° enves de a noventa como las wheel.
La gran diferencia entre estas y las otras es que gracias a su geometria de sus rodillos a 45° no se ven obligadas a pocisionarse de formas extrañas como las wheel si no que se pueden poner paralelas entre si y alineadas al chasis.


En este tipo de robots son necesarias 4 ruedas ya que gracias a ellas logra un equilibrio estable de los vectores de fuerza ya que las ruedas empujan en un angulo de 45° esto permite eparejarlas en diagonales cuando sus vectores se suman o restan
(esto logra que el robot puede ir solo para adelante,para el lado o solo rotacion)sin que el chasis se mueva

Es muy importante saber como colocar las ruedas ya que si se colocan mal no se lograria el objetivo de ellas que es cancelarse si no lo que conseguirian es que el robot no se mueva de manera lateral.Es por eso que las ruedas deben de colocarse de manera en que tenga un patron de x asi si podran cancelarse sus fuerza y provocar que avance lateralmente.

### ¿Y como deben combinarse las llantas para moverse en ciertas direcciones?

Combinación de Movimientos
El movimiento se logra mediante la suma vectorial de las fuerzas que cada rueda ejerce sobre el suelo:

Por ejemplo para avanzar hacia adelante o hacia atras las ruedas deben de avanzar en una diagonal deben ir hacia adelante mientras las otras hacia atras asi cancelando su movimiento lateral y avanzado solo hacia adelante (3,-3,3,-3)

Para avanzar lateralmente lo que se debe hacer es que todas las ruedas vayan a la misma velocidad lo que lograra que se cancele el moviemiento horizontal y se sumen los laterales logrando que el robot avance lateralmente.(3,3,3,3)


Movimiento diagonal: Si solo se encienden los motores de dos ruedas opuestas en diagonal , el robot avanzará en el ángulo de 45° que dictan los rodillos de esas ruedas activas. Por ejmplo si se movieran nada mas la delantera derecha y trasera izquierda (0,3,3,0)haria una diagonal hacia el lado derecho

Y para girar en su propio eje se logra moviendo todas las ruedas izquierdas hacia enfrente y contrariamente todas las derechas hacia atras(parecido a un robot diferencial)Por ejemplo moviendo las ruedas en favor o en contra de las manesillas del reloj logrando el giro en su propio eje.

![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_rgVZeUGBj9DhDsGuwOXCkztoWTScjyeIaWxmjSX_Eg&s=10)


## Tabla de Giros para Movimiento

| Movimiento | Delantera izquierda | Delantera derecha | Trasera izquierda | Trasera derecha |
| --- | --- | --- | --- | --- |
| Avanzar | 1 | -1 | -1 | 1 |
| Retroceder | -1 | 1 | 1 | -1 |
| **Desplazarse a la izquierda | -1 | -1 | -1 | -1 |
| Desplazarse a la derecha | 1 | 1 | 1 | 1 |
| Girar a la izquierda | 1 | -1 | 1 | -1 |
| Girar a la derecha | -1 | 1 | -1 | 1 |
| Diagonal Adelante-Derecha | 1 | 0 | 0 | 1 |
| Diagonal Adelante-Izquierda | 0 | 1 | 1 | 0 |

## Robot con dirección Ackermann

### ¿Que es un robot ackerman y que lo diferencia de los demas?
Los robots ackerman son carecterizdos por ser muy parecidos a los autmoviles ya que las dos ruedas traseras son fijas y las delanteras tienen una apertura de +- 45° aprox lo cual permite que el robot de vuelta normalmente estos suelen ser rectagulares. Normalmente la traccion suele ser aplicada a las ruedas traseras pero robots mas modernos la impementan en las cuatro ruedas.


### ¿Por que gira mas la rueda interior que la exterior?
Es por que la rueda al interior de la curva tiene un angulo mas cerrado que el exterior y es por eso que tiene que girar mas la exterior para compensar ya que si fueran a la misma velocidad derraparia el robot provocando que no tenga una direccion confiable  
La rueda que queda en el interior de la curva siempre gira más (tiene un ángulo más cerrado) que la rueda exterior.
### ¿Y como solucionan no tenener un diferecncial fisico?
El sistema interpreta el radio de giro haciendo calculos geometricos para despues mandar mas o menos fuerza a las llantas para asi poder dar una vuelta correcta.


### ¿Que es el Radio de Giro?
Es el espacio minimo que ocupa el robot para dar una vuelta en u cuanto mas giren las delanteras menos radio ocupa el giro.

### ¿Por que el robot no puede girar en su propio eje?
Es por que las llantas traseras son fijas lo que provoca que el robot no pueda.

### Entonces:
Los robots ackerman son los mas parecidos a los automoviles por que tienen dos ejes,uno fijo y el otro el cual tiene una direccion la cual permite el moviento de las ruedas y aparte de eso cuentan con un diferencial en este caso no es fisico pero cuenta con el si no no podria gentionar bien sus vueltas.

![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnPvbV39yNJt601QeqbpIoZCa4HkNnJh1pVxOl07rhmh9dfOWT4trf7od2&s=10)

## Comparación de configuraciones
NT=No tiene   
ST = Si tiene
|Configuracion|Numero tipico de ruedas|Movimiento lateral|Giro sobre su eje|Complejidad mecaninca|Complejidad de control|Aplicaciones|
|-|-|-|-|-|-|-|
|Diferencial|3|NT|ST|Poca|Poca|Rapidez y agilidad|
|Omni de 3 ruedas|3|ST|ST|Alta|Alta|Sirve para espacios semi accidentados|
|4 Ruedas mecanum|4|ST|ST|Media|Media|Eficiencia en espacios reducidos|
|Ackerman|4|NT|NT|Media|Poca|Velocidad en rectas o espacios abiertos|

### ¿Que robot usarias en los siguientes casos?
* Robot pequeño para aprender programación y control: Yo creo que el mas barato y sencillo de hacer seria un robot diferencial con rueda loca.
* Robot que necesita desplazarse dentro de un almacén con espacios reducidos: En este yo usaria un robot omni con llantas mecanum ya que es el mas agil en este tipo de situaciones.
* Plataforma que necesita moverse lateralmente sin cambiar su orientación: Aqui cualquier robot omnidireccional serian buenas elecciones aunque yo preferiria el mecanum por su facilidad en progrmarlo.
* Vehículo autónomo que debe circular de manera similar a un automóvil: Aqui claramente seria el ackerman ya que su geometria es muy parecida a la de un automovil.
* Robot para una competencia donde sea necesario cambiar rápidamente de dirección: Aqui sin duda seria un robot Diferencial ya que es el mas agil incluso es usado en competencias de seguidor de lineas
* Robot móvil sencillo que utilice únicamente dos motores: El diferencial.

## Análisis del movimiento

Para cada configuración responde:
### Diferencial
* ¿Qué debe hacer cada rueda para que el robot gire sobre su propio eje? Deben girar ambas a favor o encontra de las manesillas del reloj asi sumando sus fuerzas logrando que de vueltas 
### Omni
* ¿Por qué los rodillos permiten generar movimiento lateral? Gracias a que estan situados cada uno a 120° grados y sumandole el movimiento conjunto de las tres ruedas dos canceladose logra que la principal de la direccion y las otras solo sigan con los rodillos pasivamente 
### Mecanum
* ¿Por qué el robot puede desplazarse lateralmente aunque ninguna rueda esté orientada directamente hacia el costado? Es gracias a sus ruedas las cuales tienen rodillos integrados las cuales con la configuracion adecuada se cancela sus fuerzas verticales y empieza a moverse de manera horizontal 
### Ackermann
* ¿Por qué el vehículo necesita avanzar o retroceder para cambiar de posición lateral? Por que no tiene la capacidad de girar en su propio eje por ende tiene que girar la parte delantera de su chasis para poder cambiar su direccion.



## Aplicación en un robot real

### SHOME-VAC-PRO
Caracteristicas

* Steren
* Robot movil 
* Consta de dos Ruedas y una tercera de castor
* Sensor principal LiDAR es el sensor principal encargado del reconocimiento del espacio el cual esta situado en la parte superior del chasis
* Consta de sus dos lantas principales la independiete y dos cepillos uno principal y otro lateral los cuales giran para remover la suciedad 
* Se utiliza para limpiar un area asignada
![imagen](https://www.steren.com.mx/media/catalog/product/cache/bb0cad18a6adb5d17b0efd58f4201a2f/image/238291d52/robot-aspiradora-y-trapeadora-wi-fi-con-deposito-para-residuos.jpg)
[1] Steren, Manual de instrucciones SHOME-VAC-PRO, Steren. [En línea]. Disponible en: https://descargas.steren.com.mx/SHOME-VAC-PRO-instr.pdf. [Accedido: 11-oct-2026].
## Reflexión final

Escribe entre respondiendo:
* ¿Qué configuración te pareció más sencilla de comprender? El ackerman es ya que es parecido a los carros y se me hizo mas facil comprenderlo
* ¿Cuál ofrece mayor libertad de movimiento?Yo opino que el omni mecanum
* ¿Qué configuración utilizarías para construir tu primer robot móvil?El diferencial con rueda de castor
* ¿Por qué no existe una sola configuración de ruedas adecuada para todos los robots?Por que depende de lo que quieras lograr por ejemplo si fuera sumo yo usaria un diferencial ya que es rapido eh agil si fuera un carrera en linea recta usaria un ackerman y si fuera de eficiencia de movimiento en un esapacio cerrado o reducido usaria el omni mecanum

# Referencias

[1] R. Siegwart, I. R. Nourbakhsh, y D. Scaramuzza, *Introduction to Autonomous Mobile Robots*, 2.ª ed. Cambridge, MA, EE. UU.: MIT Press, 2011. [En línea]. Disponible en: [https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/](https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/)

[2] B. Siciliano, L. Sciavicco, L. Villani, y G. Oriolo, *Robotics: Modelling, Planning and Control*. Londres, Reino Unido: Springer, 2009. [En línea]. Disponible en: [https://link.springer.com/book/10.1007/978-1-84628-642-1](https://link.springer.com/book/10.1007/978-1-84628-642-1)

[3] P. Corke, *Robotics, Vision and Control: Fundamental Algorithms in MATLAB*, 2.ª ed. Cham, Suiza: Springer, 2017. [En línea]. Disponible en: [https://link.springer.com/book/10.1007/978-3-319-54413-7](https://link.springer.com/book/10.1007/978-3-319-54413-7)

[4] G. Campion, G. Bastin, y B. D'Andrea-Novel, "Structural properties and classification of kinematic and dynamic models of wheeled mobile robots," *IEEE Trans. Robot. Autom.*, vol. 12, no. 1, pp. 47–62, Feb. 1996, doi: 10.1109/70.481750. [En línea]. Disponible en: [https://ieeexplore.ieee.org/document/481750](https://www.google.com/search?q=https://ieeexplore.ieee.org/document/481750)
