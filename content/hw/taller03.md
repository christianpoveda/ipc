---
author: "Christian Poveda"
date: 2020-03-25
linktitle: "Taller 3"
title: "Taller 3"
summary: "Programación orientada por objetos"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Debe ser entregado al correo electrónico
  [christian.poveda+ipc_taller03@correo.usa.edu.co](mailto:christian.poveda+ipc_taller03@correo.usa.edu.co)
  a mas tardar el 2020-04-01 al comienzo de la clase, de acuerdo a lo
  establecido en el syllabus respecto al método de entrega.

# Enunciado

Usando como base el siguiente código:

```python
from datetime import date

class Tarea:
  def __init__(self, descripcion, vencimiento):
    self.descripcion = descripcion
    self.terminada = False
    self.vencimiento = vencimiento

  def terminar(self):
    self.terminada = True

  def esta_vencida(self):
    return self.vencimiento < date.today()

  def esta_terminada(self):
    return self.terminada


class Manejador:
  def __init__(self):
    self.tareas = []
```

Realice los siguientes ejercicios:

1. Dentro de la clase `Tarea`:

    1.1. Escribir un método `__lt__` que recibe como parámetro adicional otra tarea y retorna `True` si la fecha de vencimiento de la tarea actual es menor que la de la otra tarea.

    Caso de prueba:
    ```python
    tarea1 = Tarea("Preparar el almuerzo", date(2020, 1, 10))
    tarea2 = Tarea("Hacer compras", date(2020, 1, 11))

    print(tarea1 < tarea2) # Imprime `True`
    print(tarea2 < tarea1) # Imprime `False`
    print(tarea1 < tarea1) # Imprime `False`
    ```

    1.2. Escribir un método `__repr__`, sin parámetros adicionales, el cual retorna un string con una representación del objeto que incluya la descripción y la fecha de vencimiento.

    Caso de prueba:
    ```python
    tarea1 = Tarea("Preparar el almuerzo", date(2020, 1, 10))

    print(tarea1) # Imprime `Preparar el almuerzo (vence el 2020-01-10)`
    ```

    Pista: utilice `str(objeto)` para obtener una representación como string de los objetos que necesite.


2. Dentro de la clase `Manejador`:

    2.1. Escriba un método `agregar_tarea` con un parámetro adicional `tarea`, el cual agrega `tarea` al final de la lista de tareas dentro de `Manejador`.

    Caso de prueba:
    ```python
    tarea = Tarea("Preparar el almuerzo", date(2020, 1, 10))

    manejador = Manejador()
    manejador.agregar_tarea(tarea)

    print(manejador.tareas) # Imprime `[Preparar el almuerzo (vence el 2020-01-10)]`
    ```
    2.2. Escriba un método `terminar_tarea` con un parámetro adicional `indice`, el cual marca como terminada la tarea que se encuentre en la posición dada por `indice` dentro de la lista de tareas.

    Caso de prueba:
    ```python
    tarea = Tarea("Preparar el almuerzo", date(2020, 1, 10))

    manejador = Manejador()
    manejador.agregar_tarea(tarea)
    manejador.terminar_tarea(0)

    print(manejador.tareas[0].esta_terminada()) # Imprime `True`
    ```

    2.3. Escriba un método `tarea_mas_urgente` el cual busca la tarea con la menor fecha de vencimiento.

    Caso de prueba:
    ```python
    tarea1 = Tarea("Preparar el almuerzo", date(2020, 1, 10))
    tarea2 = Tarea("Hacer compras", date(2020, 1, 11))

    manejador = Manejador()
    manejador.agregar_tarea(tarea1)
    manejador.agregar_tarea(tarea2)

    print(manejador.tarea_mas_urgente()) # Imprime `Preparar el almuerzo (vence el 2020-01-10)`
    ```

    Pista: Gracias al punto 1.1, es posible comparar dos tareas por su fecha de vencimiento usando `tarea1 < tarea2`. Por esto, encontrar la tarea mas urgente es lo mismo que buscar la "mínima" tarea dentro de la lista de tareas.

    2.4. Escriba un método `tareas_sin_terminar` el cual retorna una lista con las tareas que no se han marcado como terminadas.
    Caso de prueba:
    ```python
    tarea1 = Tarea("Preparar el almuerzo", date(2020, 1, 10))
    tarea2 = Tarea("Hacer compras", date(2020, 1, 11))

    manejador = Manejador()
    manejador.agregar_tarea(tarea1)
    manejador.agregar_tarea(tarea2)

    manejador.terminar_tarea(0)

    print(manejador.tareas_sin_terminar()) # Imprime `[Hacer compras (vence el 2020-01-11)]`
    ```
