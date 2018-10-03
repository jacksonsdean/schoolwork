import turtle
from turtle_main import *



s = turtle.Screen()
turt = turtle.Turtle()

turt.speed(0)
turt.hideturtle()
for i in range (80):
    turt.pu()
    turt.right(90)
    turt.forward(i/3)
    turt.pd()
    starOutline(turt,i*2)
    

s.exitonclick()