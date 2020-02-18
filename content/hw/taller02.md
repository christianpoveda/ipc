---
author: "Christian Poveda"
date: 2020-02-18
linktitle: "Taller 2"
title: "Taller 2"
summary: "Funciones y abstracción"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Debe ser entregado al correo electrónico
  [christian.poveda+ipc_taller02@correo.usa.edu.co](mailto:christian.poveda+ipc_taller02@correo.usa.edu.co)
  a mas tardar el 2020-02-24 al comienzo de la clase, de acuerdo a lo
  establecido en el syllabus respecto al método de entrega.

# Enunciado

Escriba una función `pintar_cuadricula(n, base)` la cual dibuja una cuadrícula de `nxn` cuadrados, cuya base total mide `base`.

Para esto debe basarse en la función `pintar_cuadro(base)` capaz de dibujar un cuadrado cuya base mide `base`, la cual se encuentra en el bloque de código a continuación:

```python
import turtle

def pintar_cuadro(base):
  lados = 0
  while lados < 4:
    turtle.forward(base)
    turtle.left(90)
    lados += 1

pintar_cuadro(100)
```
