import turtle

n = 5

def pintar_linea():
  turtle.forward(100)
  turtle.left(180)
  turtle.forward(100)

def moverse(total):
  turtle.penup()
  turtle.right(90)
  turtle.forward(100/total)
  turtle.right(90)
  turtle.pendown()

def pintar_lineas(total):
  lineas = 0
  while lineas < total:
    # pintar una linea y volver
    pintar_linea()
    # moverse para pintar la siguiente linea
    moverse(total)
    # aumentar el numero de lineas
    lineas = lineas + 1
  pintar_linea()

pintar_lineas(n)
turtle.left(90)
pintar_lineas(n)
