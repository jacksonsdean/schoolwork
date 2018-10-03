from turtle_main import *

s = turtle.Screen()

turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()



for i in range (195):
    turt.pu()
    turt.right(46)
    turt.forward(i/3)
    turt.pd()
    draw60Triangle(turt,150)
   
s.exitonclick()  
