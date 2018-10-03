""" This file contains starter code for Homework 1
    Fall 2015

    Author: <your name here>
"""

import turtle
import math
import random


# -----------------------------------------------------
# Question 1: Put your script for the guinea pig problem here

buildingSize = 800   # square feet, size of building
cagePercent = 0.40   # percentage dedicated to cages
cageSize = 10.5      # square feet, minimum size of cage for 1-2 guinea pigs

gp_area = .4*buildingSize
num_pigs = gp_area//5.25
num_pigs2 = gp_area//10.5
print(num_pigs)
print(num_pigs2)





# -----------------------------------------------------
# Question 2: Find two bugs in the script below


scrn = turtle.Screen()
rick = turtle.Turtle()
rick.speed(100)

scrn.bgcolor("lemonchiffon")

rick.color("cornflowerblue")
rick.begin_fill()
rick.circle(50)
rick.end_fill() #syntax error: missing parentheses

rick.left(90) #should be 90 degrees

rick.color("palevioletred")
rick.begin_fill()
rick.circle(50)
rick.end_fill()

rick.left(90) #should be 90 degrees
rick.color("palegreen")
rick.begin_fill()
rick.circle(50)
rick.end_fill()

rick.left(90) #should be 90 degrees

rick.color("lightsalmon")
rick.begin_fill()
rick.circle(50)
rick.end_fill()

rick.left(90) #should be 90 degrees
rick.up()
rick.speed(10)
for n in range(200):
    rick.forward(50)
rick.clear()




# -----------------------------------------------------
# Question 3: Put your script to draw a tree here

s= turtle.Screen()
s.bgcolor("skyblue")

gt = turtle.Turtle()
gt.speed(0)
gt.shape("blank")
gt.pu()

gt.goto(-800,-300)
gt.color("darkgreen")
gt.pd()
gt.begin_fill()
gt.forward(1500)
gt.right(90)
gt.forward(200)
gt.right(90)
gt.forward(1500)
gt.right(90)
gt.forward(200)
gt.end_fill()
t = turtle.Turtle()
t.speed(0)
t.color("chocolate")
t.shape("blank")
t.right(90)
t.begin_fill()
for i in range(10):
    t.forward(35)
    t.left(4)
    
t.left(230)
t.forward(340)

t.left(230)
for i in range(10):
    t.forward(35)
    t.left(4)
t.right(90)
t.forward(100)
t.end_fill()
t.color("green")
t.pu
t.goto(-100,-60)
t.pd
t.pensize(40)
for i in range(200):
    t.left(i)
    t.pu
    t.forward(i+10)
    t.pd
    t.circle(70)
st = turtle.Turtle()

st.color("yellow")
st.shape("blank")
st.pensize(30)
st.pu()

st.goto(350,250)
st.shape("circle")
st.pd()
st.speed(0)
st.begin_fill()

st.circle(80)
st.end_fill()





s.exitonclick()





# -----------------------------------------------------
# Question 4: Put your script to draw circles here


sc =  turtle.Screen()
sc.bgcolor("white")

ct=  turtle.Turtle()
ct.speed(0)
for pos in [[-225, 225], [-225, -225], [225, -225], [225, 225]]:
    for i in range (21, 65, 5):
        ct.circle(i)
        ct.left(36)


#------------------------------------------------------
# Just for fun!
#rick.goto(0,200)
#rick.down()

#rick.speed(300)
#rick.shape("blank")

#scrn.bgcolor("peachpuff")

#rick.color("darkred")



#for i in range(2, 388, 2):
    #rick.right(i/2)
    #rick.forward(i)

#rick.pu() 
#rick.goto(-4,-29)
#rick.pd()
    
#rick.up()
#rick.goto(30,0)
#rick.down()
#rick.right(80)



scrn.exitonclick()

sc.exitonclick()
