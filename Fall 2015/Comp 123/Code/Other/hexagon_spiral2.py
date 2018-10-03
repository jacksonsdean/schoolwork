from turtle_main import *

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()



#colors = ["dark blue","medium blue","blue","dodger blue","deep sky blue","sky blue","light sky blue"]
colors = ["dark blue","medium blue", "blue"]
x=0
for i in range(1,200):
   
    t.color(colors[x])
    t.forward(i)
    t.left(91)
    drawHexagon(t,i)
    
    x = x + 1
    if x >= len(colors):
        x=0
    
s.exitonclick()


