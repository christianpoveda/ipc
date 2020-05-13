---
author: "Christian Poveda"
date: 2020-05-01
linktitle: "Taller 5"
title: "Taller 5"
summary: "Algoritmos voraces"
weight: 20
---

# Instrucciones
- Este taller puede ser realizado de forma individual o de a parejas.
- Debe ser entregado al correo electrónico
  [christian.poveda+ipc_taller05@correo.usa.edu.co](mailto:christian.poveda+ipc_taller05@correo.usa.edu.co)
  a mas tardar el 2020-05-13 al comienzo de la clase, de acuerdo a lo
  establecido en el syllabus respecto al método de entrega.

# Enunciado

El proposito de este taller es resolver el problema de la cobertura máxima, el
cual es una variación del problema de la cobertura visto en clase.

Partiremos del mismo escenario del problema original. Se desea lanzar un nuevo
programa de radio y, para garantizar su éxito, se ha decidido que este se
publicará en distintas emisoras para maximizar la cobertura de éste. Hay en
total `n` emisoras distintas, donde cada una de estas cubre algunos
departamentos del pais. Sin embargo, esta vez el presupuesto es limitado y solo
es posible pagar un máximo de `k` emisoras con `k < n`.

A partir de este escenario usted debe:

1. Proponer un algoritmo voraz para resolver el problema.

2. Modificar el código que se encuentra junto a las grabaciones de la clase con fecha 2020-05-04 y adaptarlo al nuevo problema.

3. Resolver la siguiente instacia del problema para `k = 4`:

```python
emisoras = {
    Emisora("Radio roja", {"Antioquía", "Bolívar"}),
    Emisora("Radio naranja", {"Valle del Cauca", "Cundinamarca"}),
    Emisora("Radio amarilla", {"Cundinamarca", "Atlántico", "Córdoba"}),
    Emisora("Radio verde", {"Cesar", "Santander"}),
    Emisora("Radio azul", {"Guajira", "Cauca", "Tolima"}),
    Emisora("Radio violeta", {"Nariño", "Cauca", "Tolima"}),
}
```
