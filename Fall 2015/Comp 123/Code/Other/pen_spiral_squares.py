from turtle_main import *
from random import randint

s2 = turtle.Screen()
turt2 = turtle.Turtle()
turt2.speed(0)
turt2.color("darkred")
turt2.hideturtle()

for i in range(170):
    turt2.pu()
    turt2.pensize(randint(1,5))
    turt2.right(123)
    turt2.forward(i/3)
    turt2.pd()
    drawSquare(turt2, 170)
  


print(turt2.getcanvas())

s2.exitonclick()