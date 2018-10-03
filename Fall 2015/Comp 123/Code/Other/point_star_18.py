import turtle
import random
s=turtle.Screen()
t=turtle.Turtle()
t.speed(0)
t.shape("blank")

color = ["darkred"]
t.color("darkred")
for i in range(1,286):
   t.color(random.choice(color))
   t.left(10)
   if i < 40:
      t.circle(5)
   t.right(150)
   t.forward(i*2)

t.right(140)
t.forward(i)



s.exitonclick()