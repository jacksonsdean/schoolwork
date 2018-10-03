import turtle
s = turtle.Screen()

turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()

for i in range (500):
    turt.pu()
    turt.right(46)
    turt.forward(i/3)
    turt.pd()
    turt.forward(120)
    turt.left(60)
    turt.forward(120)
    turt.left(60)
    turt.forward(120)
    turt.left((180-(60+60)))
