from turtle_main import *

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()




for i in range(200):
    t.pu()
    t.forward(8)
    t.pd()
    drawOctagon(t,80)
    t.left(i)
    
s.exitonclick()