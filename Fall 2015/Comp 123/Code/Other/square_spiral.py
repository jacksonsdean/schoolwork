from turtle_main import *

s = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()

for i in range(170):
    turt.pu()
    turt.right(46)
    turt.forward(i/3)
    turt.pd()
    drawSquare(turt, 170)
    
    
s.exitonclick()


s2 = turtle.Screen()
turt2 = turtle.Turtle()
turt2.speed(0)
turt2.color("darkred")
turt2.hideturtle()

for i in range(170):
    turt2.pu()
    turt2.right(123)
    turt2.forward(i/3)
    turt2.pd()
    drawSquare(turt2, 170)
    print(i)
    
s2.exitonclick()