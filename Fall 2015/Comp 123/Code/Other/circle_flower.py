import turtle




s = turtle.Screen()


turt = turtle.Turtle()

turt.speed(0)
turt.hideturtle()
for i in range (500):
    turt.pu()
    turt.right(45)
    turt.forward(i/2)
    turt.pd()
    turt.circle(i*3)

s.exitonclick()