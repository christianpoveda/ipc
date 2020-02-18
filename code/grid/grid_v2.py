import turtle

lineas = 0

while lineas < 4:
  # pintar una linea y volver
  turtle.forward(100)
  turtle.left(180)
  turtle.forward(100)

  # moverse para pintar la siguiente linea
  turtle.penup()
  turtle.right(90)
  turtle.forward(25)
  turtle.right(90)
  turtle.pendown()

  # aumentar el numero de lineas
  lineas = lineas + 1

turtle.forward(100)
turtle.left(180)
turtle.forward(100)

turtle.left(90)
lineas = 0

while lineas < 4:
  # pintar una linea y volver
  turtle.forward(100)
  turtle.left(180)
  turtle.forward(100)

  # moverse para pintar la siguiente linea
  turtle.penup()
  turtle.right(90)
  turtle.forward(25)
  turtle.right(90)
  turtle.pendown()

  # aumentar el numero de lineas
  lineas = lineas + 1

turtle.forward(100)
turtle.left(180)
turtle.forward(100)
