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
anterior: Pintar primero `5` líneas horizontales y luego `5` líneas verticales.

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

Esto está mucho mejor, hemos evitado escribir muchas instrucciones repetidas. Sin embargo, para pintar las lineas horizontales necesitaríamos duplicar de nuevo este código.

Para evitar este problema utilizaremos funciones. En pocas palabras, una función es un conjunto de instrucciones cuyo propósito es realizar una actividad específica.

Para definir una función basta con usar la palabra clave `def`, por ejemplo si queremos definir una función que se encargue de pintar una linea, podemos escribir:

```python
import turtle

def pintar_linea():
    # Pintar una linea y volver
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

lineas = 0

while lineas < 4:
    pintar_linea()

    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()

    # Contar una linea más
    lineas = lineas + 1

pintar_linea()
```

Ahora cada vez que escribamos `pintar_linea()`, Python correrá el código que se encuentra dentro de la definición de la función. Es importante que los nombres de nuestras funciones no contengan espacios, igual que los nombres de las variables.

Dado que ya logramos abstraer la acción de pintar una linea a una función, hagamos lo mismo para "moverse hacia arriba":

```python
import turtle

def pintar_linea():
    # Pintar una linea y volver
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

def moverse():
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()

lineas = 0

while lineas < 4:
    pintar_linea()
    moverse()
    # Contar una linea más
    lineas = lineas + 1

pintar_linea()
```

Todo se ve bastante bien, nuestro código es mucho mas claro ahora. Ahora veremos como hacer uso de un nuevo concepto que va de la mano con las funciones: parámetros. Las funciones pueden recibir parámetros, los cuales son variables especiales que son reemplazadas por los valores que deseemos al momento de ejecutar la función.

En este caso, usaremos parámetros para poder cambiar el tamaño de la caja que queremos pintar sin tener que reemplazar todos los `100` que hemos escrito.

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse():
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()

lineas = 0

while lineas < 4:
    pintar_linea(100)
    moverse()
    # Contar una linea más
    lineas = lineas + 1

pintar_linea(100)
```

De hecho, también necesitamos cambiar la función `moverse` para que reciba por parámetro la distancia que la tortuga debe moverse

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

lineas = 0

while lineas < 4:
    pintar_linea(100)
    moverse(25)
    # Contar una linea más
    lineas = lineas + 1

pintar_linea(100)
```

La ventaja de haber hecho esto, es que podemos usar una variable para almacenar
la longitud de las líneas al comienzo de nuestro código y luego utilizarla como
parámetro en nuestras funciones:

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

longitud = 100

lineas = 0

while lineas < 4:
    pintar_linea(longitud)
    moverse(longitud / 4)
    # Contar una linea más
    lineas = lineas + 1

pintar_linea(longitud)
```

Aun mas, podemos tomar el ciclo que tenemos y ponerlo en una función nueva
encargada de pintar varias líneas

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

def pintar_lineas(longitud):
    lineas = 0

    while lineas < 4:
        pintar_linea(longitud)
        moverse(longitud / 4)
        # Contar una linea más
        lineas = lineas + 1

    pintar_linea(longitud)

pintar_lineas(100)
```

Además podemos añadir un parámetro más a `pintar_lineas`, para personalizar
cuantas lineas queremos pintar

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

def pintar_lineas(longitud, cuantas):
    lineas = 0

    while lineas < cuantas:
        pintar_linea(longitud)
        moverse(longitud / cuantas)
        # Contar una linea más
        lineas = lineas + 1

    pintar_linea(longitud)

pintar_lineas(100, 4)
```

Funciona bastante bien, pero estamos siendo imprecisos con el parámetro
`cuantas`. Estamos pintando en total `5` líneas si `cuantas` vale `4`.
Arreglemos esto haciendo uso de las operaciones aritméticas que ya sabemos

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

def pintar_lineas(longitud, cuantas):
    lineas = 0

    while lineas < cuantas - 1:
        pintar_linea(longitud)
        moverse(longitud / (cuantas - 1))
        # Contar una linea más
        lineas = lineas + 1

    pintar_linea(longitud)

pintar_lineas(100, 5)
```

Ahora por fin podemos terminar de pintar nuestra cuadrícula escribiendo muy
poco código. Para hacer las lineas horizontales haremos un pequeño truco. Si
ejecutamos nuestro programa y giramos la pantalla 90 grados a la izquierda,
veremos 5 lineas verticales. Esto quiere decir que si hacemos que la tortuga
gire 90 grados a la izquierda y llamamos `pintar_lineas(100, 5)` de nuevo,
habremos pintado 4 lineas verticales.

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

def pintar_lineas(longitud, cuantas):
    lineas = 0

    while lineas < cuantas - 1:
        pintar_linea(longitud)
        moverse(longitud / (cuantas - 1))
        # Contar una linea más
        lineas = lineas + 1

    pintar_linea(longitud)

pintar_lineas(100, 5)
turtle.left(90)
pintar_lineas(100, 5)
```

Genial! Para terminar, escribamos una función capaz de pintar una cuadrícula

```python
import turtle

def pintar_linea(longitud):
    # Pintar una linea y volver
    turtle.forward(longitud)
    turtle.right(180)
    turtle.forward(longitud)

def moverse(distancia):
    # Moverse hacia arriba
    turtle.penup()
    turtle.right(90)
    turtle.forward(distancia)
    turtle.right(90)
    turtle.pendown()

def pintar_lineas(longitud, cuantas):
    lineas = 0

    while lineas < cuantas - 1:
        pintar_linea(longitud)
        moverse(longitud / (cuantas - 1))
        # Contar una linea más
        lineas = lineas + 1

    pintar_linea(longitud)

def pintar_cuadricula(longitud, cuadros):
    pintar_lineas(longitud, cuadros + 1)
    turtle.left(90)
    pintar_lineas(longitud, cuadros + 1)

pintar_cuadricula(100, 4)
```

Necesitamos pintar una linea mas que el número de cuadros que queremos hacer,
justo como lo habíamos pensado en el tablero! Ahora podemos pintar una
cuadrícula de cualquier tamaño con cualquier número de cuadros que queramos.
