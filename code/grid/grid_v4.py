import turtle

def pintar_linea():
  turtle.forward(100)
  turtle.left(180)
  turtle.forward(100)

def moverse():
  turtle.penup()
  turtle.right(90)
  turtle.forward(25)
  turtle.right(90)
  turtle.pendown()

def pintar_lineas():
  lineas = 0
  while lineas < 4:
    # pintar una linea y volver
    pintar_linea()
    # moverse para pintar la siguiente linea
    moverse()
    # aumentar el numero de lineas
    lineas = lineas + 1
  pintar_linea()

pintar_lineas()
turtle.left(90)
pintar_lineas()
