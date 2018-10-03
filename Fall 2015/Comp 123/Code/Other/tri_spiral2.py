from turtle_main import *

s = turtle.Screen()

turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()
turt.pensize(1)
for i in range (90):
    turt.pu()
    turt.forward(i/2)
    turt.pd()
    draw60Triangle(turt,120)
    turt.left(i//29)
   
s.exitonclick()  

