---
author: "Christian Poveda"
date: 2020-04-14
linktitle: "Examen 2"
title: "Examen 2"
summary: "Examen sobre dividir y conquistar, programación orientada por objetos y teoría de grafos"
weight: 20
---

# Instrucciones

- Este examen puede ser realizado de forma individual o de a parejas.
- Debe ser entregado al correo electrónico
  [christian.poveda+ipc_examen02@correo.usa.edu.co](mailto:christian.poveda+ipc_examen02@correo.usa.edu.co)
  a mas tardar el 2020-04-22 al comienzo de la clase, de acuerdo a lo
  establecido en el syllabus respecto al método de entrega.

# Enunciado

El propósito de este taller es escribir una herramienta que le permita
encontrar un orden topológico para cualquier grafo y utilizar dicha herramienta
para resolver algunos problemas. Extienda el siguiente programa como se
menciona en la sección de ejercicios y luego resuelva los problemas en la
sección de problemas.

```python
class Nodo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.vecinos = []

    def agregar_vecino(self, indice_vecino):
        self.vecinos.append(indice_vecino)

    def __repr__(self):
        return "Nodo(" + str(self.contenido) + ")"


class Grafo:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, contenido):
        self.nodos.append(Nodo(contenido))

```

# Representación

El programa que se le entrega cuenta con dos clases:

- La clase `Grafo` con un único atributo `nodos`, el cual es una lista que
  contiene objetos de clase `Nodo`.
- La clase `Nodo` la cual tiene dos atributos: `contenido`, el cual representa
  el contenido puntual del nodo, y `vecinos` el cual es una lista con los
  índices de los vecinos del nodo. Estos indices se toman respecto a la lista
  de nodos que contiene la clase `Grafo`.

A manera de ejemplo, el siguiente grafo

![](../../images/graph.png)

Se debe representar de la siguiente manera

| Indice | Contenido | Vecinos     |
|--------|-----------|-------------|
| `0`    | `"A"`     | `[1, 6]`    |
| `1`    | `"B"`     | `[2, 4, 5]` |
| `2`    | `"C"`     | `[3]`       |
| `3`    | `"D"`     | `[]`        |
| `4`    | `"E"`     | `[]`        |
| `5`    | `"F"`     | `[]`        |
| `6`    | `"G"`     | `[5]`       |


# Ejercicios

1. Escriba una función `repetir`, la cual recibe dos argumentos `veces` y
   `valor`. Esta función debe retornar una lista de `veces` elementos donde
   todos los elementos son iguales a `valor`. Por ejemplo, `repetir(3, "Hola")`
   debe retornar `["Hola", "Hola", "Hola"]`.

2. Agregue un método `indice_nodo` a la clase `Grafo`. Este método recibe un
   argumento adicional `contenido` y debe retornar el indice del nodo con
   contenido igual a `contenido`. Si no hay un nodo cuyo contenido sea igual a
   `contenido`,  debe retornar `None`. Caso de prueba

```python
grafo = Grafo()

grafo.agregar_nodo("A")
grafo.agregar_nodo("B")

print(grafo.indice_nodo("A")) # Debe imprimir `0`
print(grafo.indice_nodo("B")) # Debe imprimir `1`
print(grafo.indice_nodo("C")) # Debe imprimir `None`
```

3. Agregue un método `agregar_arista` a la clase `Grafo`. Este método recibe
   dos argumentos adicionales `contenido_desde` y `contenido_hasta`. Además,
   este método debe encontrar un nodo con contenido igual a `contenido_desde` y
   agregar a la lista de vecinos el indice del nodo con contenido igual a
   `contenido_hasta`.

```python
grafo = Grafo()

grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_nodo("C")

grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")

print(grafo.nodos[0].vecinos) # Debe imprimir `[1, 2]`
```

Los puntos 4 y 5 implementan el algoritmo de orden topológico que se expuso en
clase. Es conveniente realizar estos dos puntos teniendo en cuenta esta
explicación. Usted puede realizar una implementación alternativa del algoritmo
o incluso implementar un algoritmo distinto si así lo desea.

4. Agregue un método `visitar` a la clase `Grafo`. Este método recibe tres
   argumentos adicionales: un entero `indice` y dos listas `visitados` y
   `orden`. Este método debe realizar las siguientes operaciones:

    a. Cambiar el valor de `visitados` en el indice `indice` por `True`.

    b. Obtener el nodo con indice `indice` dentro de la lista de nodos del
    grafo.

    c. Para cada indice `vecino` de los vecinos del nodo encontrado en la parte
    (b) revisar si la lista `visitados` tiene en la posición `vecino` el valor
    `False`. Si es así, llamar el método `visitar` usando como argumentos
    `vecino`, `visitados` y `orden`.

    d. Insertar el nodo encontrado en la parte (b) a la lista `orden` en la
    posición 0.

5. Agregue un método `orden_topologico` a la clase `Grafo`. Este método no
   tiene argumentos adicionales y debe:

   a. Crear una lista `visitados` la cual tiene `n` elementos, todos iguales a
   `False`.

   b. Crear una lista `orden` vacía.

   c. Para cada entero `i` desde `0` hasta `n`. Si `visitados` en la posición
   `i` es `False`, llamar el método `visitar` con argumentos `i`, `visitados` y
   `orden`.

   d. Retornar `orden`.

   Donde `n` es el número de nodos en el grafo.

Si todos los métodos y funciones que se le han pedido en esta sección son
correctos, el método `orden_topologico` debe retornar una lista con los nodos
del grafo en orden topológico.

# Problemas
Haciendo uso de la clase `Grafo`:

6. Encuentre un orden de ejecución para las tareas en la siguiente lista de
   restricciones:
    - Para ir al parque debo alistar a mi perro.
    - Para alistar a mi perro debo haber terminado mi tarea y haberme vestido.
    - Para haberme vestido debo haberme bañado.
    - Para hacer mi tarea debo haber organizado el escritorio.

7. Resuelva el problema 2 del taller 4.
