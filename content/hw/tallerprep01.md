---
author: "Christian Poveda"
date: 2020-02-28
linktitle: "Taller de preparación (Primer examen)"
title: "Taller de preparación (Primer examen)"
summary: "Taller de preparación para el primer examen"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Este taller no tiene fecha de entrega ni calificación. Sin embargo será el
  material principal a discutir durante la clase de repaso del 2020-03-02.
- Para todos los ejercicios trate de seguir la metodología propuesta en clase:
    - Primero haga un par de ejemplos en lápiz y papel para formular una
      solución.
    - Luego trate de extrapolar sus soluciones particulares a un algoritmo
      genérico usando un diagrama de flujo o escribiendo informalmente los
      pasos a seguir.
    - Finalmente haga el proceso de traducción a código.
- Recuerde apoyarse en el material del curso que se encuentra en el
  [syllabus](../../syllabus), incluyendo la bibliografía.

# Enunciado

1. Una fecha mágica es una fecha en la cual el día, multiplicado por el mes da
   como resultado los últimos dos dígitos del año. Por ejemplo, el 10 de junio
   de 1960 es una fecha mágica. Escriba una función con tres parámetros: `dia`,
   `mes` y `año`, la cual imprime un mensaje diciendo si la fecha es mágica o
   no. Como ayuda se le entrega la siguiente función que toma un año y retorna
   los dos últimos dígitos de este:

    ```python
    def dos_digitos(año):
        return año % 100
    ```

2. Usando `turtle`, escriba una función que recibe como parámetro un número
   `n`, capaz de dibujar un polígono regular de `n` lados (Pista: la suma de
   los ángulos internos de cualquier polígono debe sumar 360 grados).

3. En este ejercicio escribiremos una función capaz de reversar una lista.

    a. Escriba una función `transladar` que reciba como parámetros una lista
    `lista` y un índice `indice`, capaz de transladar el último elemento de
    `lista` a la posición `indice`. Para comprobar la validez de su solución
    puede utilizar el siguiente caso de prueba:

    ```python
    lista = ["Hugo", "Paco", "Luis"]

    transladar(lista, 0)
    print(lista) # Debe imprimir ["Luis", "Hugo", "Paco"]

    transladar(lista, 1)
    print(lista) # Debe imprimir ["Luis", "Paco", "Hugo"]

    transladar(lista, 2)
    print(lista) # Debe imprimir ["Luis", "Paco", "Hugo"]
    ```

    b. Haciendo uso de la función `transladar` escriba una función `reversar`
    con un único parámetro `lista`, la cual invierta el orden de `lista`. Para
    comprobar la validez de su solución puede utilizar el siguiente caso de
    prueba:

    ```python
    lista = ["Hugo", "Paco", "Luis", "Donald", "Daisy"]

    reversar(lista)
    print(lista) # Debe imprimir ["Daisy", "Donald", "Luis", "Paco", "Hugo"]
    ```

4. Escriba una función `total`, la cual recibe como parámetro una lista de
   números `lista` y retorna la suma total de todos sus elementos. Escriba la
   función tanto de forma recursiva como usando ciclos.
