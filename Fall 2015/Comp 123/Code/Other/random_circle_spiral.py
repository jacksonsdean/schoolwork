import turtle
from random import randint

s = turtle.Screen()
turt = turtle.Turtle()

degree = randint(1,360)
print("angle:",degree)

radius = randint(1,6)
print("radius:",radius)

dist = randint(0,7)
print("forward:",dist)

turt.speed(0)
turt.hideturtle()
for i in range (300):
    turt.pu()
    turt.right(degree)
    turt.forward(i/dist)
    turt.pd()
    turt.circle(radius*i)
    

s.exitonclick()

#fun:
#-----------
#angle: 177
#radius: 4
#forward: 2
#-----------
#angle: 36
#radius: 6
#forward: 6
#-----------
#angle: 6
#radius: 3
#forward: 7

#-----------
#angle: 318
#radius: 1
#forward: 7

#-----------
