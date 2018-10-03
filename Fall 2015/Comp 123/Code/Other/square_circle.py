from turtle_main import *

s = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()

for i in range(360):
    turt.right(1)
    drawSquare(turt, 150)
    
s.exitonclick()