---
author: "Christian Poveda"
date: 2020-02-10
linktitle: "Taller 1"
title: "Taller 1"
summary: "Diagramas de flujo y complejidad"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Debe ser entregado de forma escrita el 2020-02-17 al comienzo de la clase.

# Temática
En su nuevo trabajo como ingeniero de investigación y desarrollo del [Organismo Internacional de Energía Atómica (OEIA)](https://es.wikipedia.org/wiki/Organismo_Internacional_de_Energ%C3%ADa_At%C3%B3mica) se le ha designado investigar un método mas eficiente para almacenar deshechos radiactivos. Gracias al arduo trabajo de sus colegas, el OEIA ha creado un robot controlado de manera remota para transportar los deshechos radiactivos, evitando afectar la salud de los empleados que trabajan en la industria nuclear. Por protocolo, los deshechos radiactivos se encuentran almacenados en barriles, los cuales están puestos en línea recta uno detrás de otro.

Este robot es un prototipo y solo es capaz de realizar algunas instrucciones básicas:

- Almacenar la posición del barril que tiene al frente en su memoria.
- Medir la [dosis de radiación ionizante](https://es.wikipedia.org/wiki/Sievert) producida por el barril que tiene al frente y guardar el valor en su memoria.
- Moverse a una posición almacenada en su memoria.
- Incrementar o disminuir alguno de los valores en memoria por `1`.
- Decidir si un valor en memoria es mayor o igual a otro.
- Intercambiar dos barriles si tiene almacenadas sus posiciones.

Su trabajo consiste en escribir algoritmos para que este prototipo pueda optimizar el orden de subida de los barriles a un camión de carga, el cual los transportará a su lugar de deposito final.

A continuación tiene dos problemas que debe resolver. Para ambos problemas:

1. Describa algoritmo de su solución usando diagramas de flujo.
2. Calcule la complejidad temporal del algoritmo teniendo en cuenta sólo el número de comparaciones entre dos valores como función del número de barriles.

Como convención, se dirá que la fila de barriles se encuentra de izquierda a derecha. En ambos problemas, el robot comienza justo al lado del barril del extremo izquierdo y el número de barriles se representa con la variable `n`. Asuma además que cada barril ocupa `1` unidad de distancia.

# Problema 1: Búsqueda del mínimo

La primera tarea a la que debe enfrentarse es encontrar la posición del barril con la menor dosis de radiación. Para así darle menor prioridad a la hora de transportarlo.

# Problema 2: Organizando los barriles

El camión que transporta los barriles no puede llevar todos los barriles al tiempo, por lo que el robot debe organizar los barriles en una linea recta de acuerdo a la dosis de radiación de forma ascendente (El mayor barril a la derecha, y el menor barril a la izquierda).

Para este problema, además de las instrucciones básicas, puede utilizar su algoritmo anterior para encontrar el máximo entre el grupo de barriles que el robot tiene a su derecha como si fuese una instrucción más.
