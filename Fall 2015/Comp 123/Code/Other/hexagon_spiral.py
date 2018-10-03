from turtle_main import *

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()





for i in range(200):
    t.pu()
    t.forward(i/2)
    t.pd()
    t.left(46)
    drawHexagon(t,150)
    
s.exitonclick()