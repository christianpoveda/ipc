---
author: "Christian Poveda"
date: 2020-02-24
linktitle: Recursión y llamado a funciones
title: Recursión y llamado a funciones
summary: "Notas de clase sobre recursión y llamado a funciones"
weight: 20
---

# Un repaso sobre funciones

Como vimos la clase anterior, las funciones nos permiten agrupar secuencias de
instrucciones para poder abstraer comportamientos específicos. Hay dos procesos
fundamentales para hacer uso de funciones:

- Definición: El el proceso en el cual se define que secuencia de instrucciones
  conforman una función, también se le suele dar un nombre a la función y si se
  desea, uno o mas parámetros.

- Invocación o llamado: Es el proceso en el cual se declara que se hará uso de
  una función ya definida, es decir, se declara que se deben ejecutar las
  instrucciones que conforman la función.

# Entrada y salida

Como bien sabemos, las funciones pueden recibir parámetros lo cual permite
tener un control mas fino sobre el comportamiento de estas. Los parámetros
pueden ser pensados como las entradas de la función, son el insumo que la
función requiere para de hecho poder ejecutar las instrucciones que le
corresponden.

De la misma manera, una función tiene una salida, la cual se conoce como el
retorno de la función. Este retorno es utilizado para que una función no solo
ejecute un conjunto de acciones, sino que al terminar esta ejecución, devuelva
un valor.

Para representar las entradas y salida de una función usando diagramas de
flujo, suelen utilizarse cajas con forma de paralelogramo:

![](../../images/flowchart_io.svg)

A continuación podemos ver una representación de la misma función `promedio` en
Python:

```python
def promedio(a, b):
    m = (a + b) / 2
    return m
```

Noten como las entradas de la función se encuentran entre paréntesis junto al
nombre de la función, mientras que la salida de la función se especifica
haciendo uso de la palabra clave `return`.

En Python y otros lenguajes, una función no ejecuta ninguna instrucción que se
encuentre después del retorno. Por ejemplo, al ejecutar el siguiente programa:

```python
def cuadrado(x):
    return x * x
    print("Hola")

print(cuadrado(5))
```

se imprimirá `25` pero no `Hola`.


# Recursión

dado que una función puede llamar a otras funciones dentro de su definición. De
hecho es posible escribir funciones que se llamen a si mismas, este tipo de
funciones se conocen como funciones recursivas

```python
def hola_por_siempre():
    print("Hola")
    hola_por_siempre()

hola_por_siempre()
```

La recursión suele usarse como una alternativa a los ciclos. Para entender
mejor como se utilizan las funciones recursivas, tratemos de entender que hace
la siguiente función:

```python
def carl(a, b):
    if a < b:
        return a + carl(a + 1, b)
    else:
        return a
```

por ejemplo si ejecutamos `carl(1, 4)`, esta retornaría `1 + carl(2, 4)`, es
decir ahora debe ejecutarse `carl(2, 4)` y sumarle su resultado a `1`. Al
ejecutar `carl(2, 4)` esta retornaría `2 + carl(3, 4)`, luego ahora debe
ejecutarse `carl(3, 4)` y su resultado debe sumarse a `2` para obtener el
resultado de `carl(2, 4)`, lo cual a la vez debe sumarse a `1` para obtener el
resultado de `carl(1, 4)`. Hagamos el proceso completo de forma ordenada:

- `carl(1, 4)` retorna `1 + carl(2, 4)`, es necesario ejecutar `carl(2, 4)`.
- `carl(2, 4)` retorna `2 + carl(3, 4)`, es necesario ejecutar `carl(2, 4)`.
- `carl(3, 4)` retorna `3 + carl(4, 4)`, es necesario ejecutar `carl(2, 4)`.
- `carl(4, 4)` retorna `4`, no es necesario ejecutar mas instrucciones.

Luego, podemos finalmente saber cual es el valor retornado por `carl(1, 4)`:

- `carl(3, 4)` retorna `3 + 4`, dado que `carl(4, 4)` retorna `4`.
- `carl(2, 4)` retorna `2 + 3 + 4`, dado que `carl(3, 4)` retorna `3 + 4`.
- `carl(1, 4)` retorna `1 + 2 + 3 + 4`, dado que `carl(2, 4)` retorna `2 + 3 +
  4`.

En conclusión `carl(1, 4)` retorna `10`, la suma de todos los números entre `1`
y `4`. De hecho `carl(a, b)` retorna la suma de todos los números entre `a` y
`b`. Tratemos de examinar mas a conciencia el comportamiento de esta función.
`carl(a , b)` aparentemente retorna la suma de todos los números entre `a` y
`b`, esto lo hace comparando `a` con `b`:

- si `a` es menor a `b`, entonces se retorna `a +  carl(a + 1, b)`, es decir,
  `a` mas la suma de todos los números entre `a + 1` y `b`
- por otro lado, si `a` es mayor o igual a `b`, simplemente se retorna `a.`

En otras palabras, esta función fue escrita basándose en la idea de que sumar
todos los números entre `a` y `b` es lo mismo que primero sumar todos los
números entre `a + 1` y `b` y luego a eso se le debe sumar `a`, excepto en el
caso cuando `a` y `b` son iguales, dado que en tal caso la suma de todos los
números entre `a` y `a` es simplemente `a`.

Ahora, es perfectamente posible escribir otra función que haga lo mismo usando
solamente `ciclos`:

```python
def fred(a, b):
    suma = a
    while a < b:
        a = a + 1
        suma = suma + a
    return suma
```

Sin embargo, ninguna solución es mejor que la otra, simplemente son soluciones
distintas.
