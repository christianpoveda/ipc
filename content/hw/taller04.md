---
author: "Christian Poveda"
date: 2020-04-01
linktitle: "Taller 4"
title: "Taller 4"
summary: "Teoría de grafos"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Debe ser entregado al correo electrónico
  [christian.poveda+ipc_taller04@correo.usa.edu.co](mailto:christian.poveda+ipc_taller02@correo.usa.edu.co)
  a mas tardar el 2020-04-15 al comienzo de la clase, de acuerdo a lo
  establecido en el syllabus respecto al método de entrega.

# Enunciado

Para cada uno de los problemas de este taller:

a. Modelar las entidades del problema como un grafo. Debe mencionar
explícitamente que representan tanto los nodos como las aristas del grafo.

b. Traduzca el problema a un problema sobre el grafo que construyó.

c. Dibuje el grafo que representa su problema (puede apoyarse en [esta](https://csacademy.com/app/graph_editor/) herramienta).

c. Resuelva el problema de grafos asociado al problema original y traduzca la
solución de vuelta al contexto del problema.

# Problemas

1. Alicia, Beto, Camila, David, Enrique, Francisco y Gabriela han decidido
salir a comer y el restaurante al que van solo tiene mesas redondas. Algunos de
los integrantes tienen problemas entre ellos y por lo tanto no les gustaría
sentarse uno al lado del otro:
    - Alicia no se quiere sentar al lado de Beto o Camila.
    - Beto no se quiere sentar al lado de Camila, Enrique o Gabriela.
    - Camila no se quiere sentar al lado de David o Gabriela.
    - Enrique no se quiere sentar al lado de Gabriela.


Encuentre, si es posible, una forma en la que todos se puedan sentar y a la vez
todos estén a gusto con sus restricciones.

2. Usted se encuentra trabajando en el diseño de una nueva refinería de
   petroleo y es necesario minimizar el espacio requerido para la refinería.
   Después de haber estudiado el proceso de refinamiento, usted ha encontrado
   que estas son las entradas y salidas de cada proceso de refinamiento:

- Destilación atmosférica: Se destila petróleo crudo para obtener nafta,
  keroseno diesel, gas residual y residuos atmosféricos
- Hidroteatro: Transforma el nafta en gasolina.
- Destilador de vacío: A partir de los residuos atmosféricos se produce aceite
  pesado y aceite liviano.
- Craqueo catalítico: A partir de aceite liviano se produce nafta y butileno.
- Hidrocraqueo: A partir de aceite pesado se produce diésel, gasolina y butano.
- Alquilación: A partir de butano y butileno se produce gasolina.
- Procesamiento de gas: A partir del gas residual se produce butano.
- Mezcla de gasolina: Se reúne toda la gasolina producida.
- Recolección de diésel: Se reúne todo el diésel producido.
- Recolección de queroseno: Se reúne todo el queroseno producido.

¿Cómo puede organizar usted las etapas de refinamiento para que todas las
tuberías que conectan las distintas etapas vayan en el mismo sentido?

3. Usted se encuentra visitando Europa y necesita viajar de Berlin a Zagreb. A continuación encuentra el costo de un tiquete de tren entre dos ciudades, usted puede tomar cualquier ruta de tren en el sentido que desee:

| Ruta                | Valor del tiquete |
|---------------------|-------------------|
| Berlín - Bruselas   | 60                |
| Berlín - Copenhague | 20                |
| Zagreb - Bruselas   | 160               |
| Bruselas - París    | 50                |
| Zagreb - Copenhague | 180               |
| Zagreb - Tallin     | 90                |
| París - Zagreb      | 100               |
| Copenhague - Tallin | 40                |
| Tallin - Paris      | 30                |

¿Cuál es la ruta menos costosa?
