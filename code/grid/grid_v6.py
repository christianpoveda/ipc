import turtle

turtle.speed(5)

n = 5
l = 50

def pintar_linea(tamano):
  turtle.forward(tamano)
  turtle.left(180)
  turtle.forward(tamano)

def moverse(tamano, total):
  turtle.penup()
  turtle.right(90)
  turtle.forward(tamano/total)
  turtle.right(90)
  turtle.pendown()

def pintar_lineas(tamano, total):
  lineas = 0
  while lineas < total:
    # pintar una linea y volver
    pintar_linea(tamano)
    # moverse para pintar la siguiente linea
    moverse(tamano, total)
    # aumentar el numero de lineas
    lineas = lineas + 1
  pintar_linea(tamano)

pintar_lineas(l, n)
turtle.left(90)
pintar_lineas(l, n)
