---
author: "Christian Poveda"
date: 2020-02-19
linktitle: Funciones y abstracción
title: Funciones y abstracción
summary: "Notas de clase sobre funciones y abstracción"
weight: 30
---

En las clases anteriores hemos aprendido cómo hacer tareas repetitivas usando
ciclos. Para ver esto en acción, haremos un programa usando `turtle` que pinte
una cuadricula de `4x4`, siguiendo el algoritmo que habíamos hecho en la clase
anterior. A continuación, tenemos el diagrama de flujo de nuestro algoritmo:

Sin embargo `turtle` no sabe ejecutar las acciones `pintar linea horizontal` o
`pintar linea vertical`. Recordemos que nuestra tortuga solo sabe como moverse
hacia adelante, girar,  y decidir si usar o no el lápiz.

Adicionalmente, tampoco tenemos claro que tan grande debe ser nuestra
cuadrícula, ¿Debe ocupar toda la pantalla?. Mientras tanto haremos que nuestra
cuadricula mida `100x100` unidades de distancia.

Primero pintaremos una linea horizontal que mide `100`:

```python
import turtle

turtle.forward(100)
```

Ahora hagamos que nuestra tortuga vuelva a su posición inicial:

```python
import turtle

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
```

Para pintar la siguiente linea, necesitamos que nuestra tortuga se mueva 25
unidades de distancia hacia arriba, pero sin usar el lápiz (para evitar
confundirnos):

```python
import turtle

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)

# Moverse hacia arriba
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()
```

Además nos hemos encargado de que la tortuga gire hacia la derecha para que
pueda pintar la siguiente linea en la posición correcta.

Ahora tenemos que pintar 4 líneas mas, ingenuamente pensaríamos que la mejor manera sería copiando y pegando el código:

```python
import turtle

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)

# Moverse hacia arriba
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)

# Moverse hacia arriba
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)

# Moverse hacia arriba
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)

# Moverse hacia arriba
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
```

Nótese que no decidimos movernos hacia arriba luego de pintar la quinta línea,
dado que no pretendemos pintar más lineas hacia arriba.

Pero este código es demasiado largo ¡y aún nos falta pintar las líneas
verticales!. Además, si quisiéramos cambiar la longitud de las líneas,
tendríamos que reemplazar los valores `100` y `25` en todas partes.

Afortunadamente podemos hacer uso de un ciclo para evitar repetir una y otra
vez las mismas instrucciones. Dado que queremos pintar y movernos hacia arriba
4 veces (la quinta linea es pintada por aparte), necesitamos llevar cuenta de
esto usando una variable, la cual llamaremos `lineas`:

```python
import turtle

lineas = 0

while lineas < 4:
    # Pintar una linea y volver
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()

    # Contar una linea más
    lineas = lineas + 1

# Pintar una linea y volver
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
```

Esto está mucho mejor, hemos evitado escribir muchas instrucciones repetidas.
