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
    turt.circle(i*2)

s.exitonclick()