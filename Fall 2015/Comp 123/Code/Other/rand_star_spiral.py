import turtle
from turtle_main import *
from random import randint

s = turtle.Screen()
turt = turtle.Turtle()

degree = randint(1,360)
print(degree)

turt.speed(0)
turt.hideturtle()
for i in range (80):
    turt.pu()
    turt.right(degree)
    turt.forward(i/3)
    turt.pd()
    starOutline(turt,i*2)
    

s.exitonclick()

#cool random spirals:
# 111
#