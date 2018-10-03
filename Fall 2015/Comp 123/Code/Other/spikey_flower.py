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
    sideLen1=120
    angle1=40
    angle2=60    
    angle3 =  180 - (angle1 + angle2)
    
    
    sideLen2 =  ((math.sin(angle1)*sideLen1)/math.sin(angle2))
    
    sideLen3 = ((math.sin(angle2)*sideLen2)/math.sin(angle1))
 
       
    turt.forward(sideLen1)
    turt.left(angle1)
    turt.forward(sideLen2)
    turt.left(angle2)
    turt.forward(sideLen3)
    turt.left(angle3)
   
  
s.exitonclick()