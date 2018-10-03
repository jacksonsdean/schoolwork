# ====================================================================
#
#  Homework 2 solutions
#  Jackson
# ====================================================================


# --- NOTE FROM SUSAN ABOUT LAYOUT OF FILE:
# --- Notice how I organized this file. This is a good organization
# --- for your homework files.
# --- * First, all import statements at the top
# --- * Next the function definitions for the questions, in order
# --- * At the bottom of the file, a script section. I am using the
# ---   strange-looking if statement. Any statements inside that if
# ---   statement are performed when you run your file. But they are
# ---   not performed when your file is imported into my testing
# ---   file, which is nice. Feel free to make changes, additions
# ---   or to comment out parts of the script section.


import math
import turtle

# --------------------------------------------------------------------
# Question 1


def proc1(x):
    print(3 * x)
    

def proc2(x):
    return 3 * x



# The first function call will not return the value of 3*x and is therefore unusable by the rest of the program. As a result, R1 will not be assigned to the value of 3*x. The Second function call does return the value of 3*x but does not print it. R2 will equal 15.



# --------------------------------------------------------------------
# Question 2

# def tells python that this line defines a function
# proc2 is the name of that function
# the open parenthesis tells python that this is the start of the parameter list
# x is the parameter that must be passed to proc2
# the close parenthesis tells python that this is the end of the parameter list.
# the colon tells python that everything after this point indented is the body of the function proc2 and should be run when the function is called.
# indention tells python that this line is part of the function body
# return tells python to bring the statement after return outside of the function. This ends the body of the function.
# 3*x multiplies 3 times the argument that was passed to the function when it was called.



# --------------------------------------------------------------------
# Question 3

# put your definition of starOutline here Include a descriptive comment as a
# triple-quoted string right after the def line

def starOutline(turt, sideLen):
    """Create a five pointed star outline at the current location and heading using the input turt and sideLen"""
    for i in range(5):
        turt.forward(sideLen)
        turt.right(120)
        turt.forward(sideLen)
        turt.left(48)




# Functions that use starOutline to draw more interesting pictures:

def gridOfStars():
    """Takes in no inputs, and displays a turtle graphics screen. The turtle
    in it draws 9 star shapes in a grid"""
    scr = turtle.Screen()
    #ted = turtle.Turtle(z)
    ted = turtle.Turtle()
    ted.speed(0)
    for coord in [(0, 0), (-200, 0), (-200, -200), 
                  (0, -200), (200, -200), (200, 0), 
                  (200, 200), (0, 200), (-200, 200)]:
        ted.up()
        ted.goto(coord)
        ted.down()
        starOutline(ted, 60)
    scr.exitonclick()


def spiralOfStars(angle):
    """Takes in one input, an angle, and displays a turtle graphics screen. It then
    draws a series of star shapes, each one rotated by the input angle,
    and a bit bigger than the previous."""
    scr = turtle.Screen()
    tad = turtle.Turtle()
    tad.speed(0)
    for size in range(20, 200, 10):
        starOutline(tad, size)
        tad.left(angle)
    scr.exitonclick()


# --------------------------------------------------------------------
# Question 4

# Uncomment this when you are ready to work on it

def drawStairs(turt, numSteps, stepSize):
    """Takes in three inputs: a turtle, the number of steps in th

e staircase,
    and the size of each step (same vertical and horizontal). It draws a
    staircase with the given number of steps. The bottom step starts where
    the turtle is, with the steps parallel to the turtle's current heading.
    Steps are a fixed height and width, and the steps are colored and filled
    in with the turtle's current color."""
    turt.speed(0)
    turt.begin_fill()
    for i in range(numSteps):
        turt.left(90)
        turt.forward(stepSize) #Typo s=S
        turt.right(90) #indentation was wrong
        turt.forward(stepSize)
    turt.right(90)
    turt.forward( numSteps * stepSize ) # Semantic, +=*
    turt.right(90)
    turt.forward( numSteps * stepSize )
    turt.right(180)
    turt.end_fill()







# --------------------------------------------------------------------
# Script with calls to functions


if __name__ == '__main__':
    # Calls for question 1+2
    r1 = proc1(5)
    r2 = proc2(5)
    print(r1, r2)    
    
    # Calls for question 3
    neighb = turtle.Screen()
    neighb.bgcolor('lavender')
    larissa = turtle.Turtle()
    starOutline(larissa, 150)
    neighb.exitonclick()
    gridOfStars()
    spiralOfStars(-10)
    

    # Calls for question 4
    # shadedStars()
    s=turtle.Screen()
    t=turtle.Turtle()
    drawStairs(t, 15,20)
    s.exitonclick()
 


#--------------------------------------------------------------------
#For fun:

s = turtle.Screen()
turt = turtle.Turtle()

turt.speed(0)
turt.hideturtle()
for i in range (80):
    turt.pu()
    turt.right(90)
    turt.forward(i/3)
    turt.pd()
    starOutline(turt,i*2)
    

s.exitonclick()

s2 = turtle.Screen()

t = turtle.Turtle()

t.ht()

t.speed(0)

x=0

coordList = []
for i in range(0,357,17):
    coordList.append(i)

rCoordList= coordList[::-1]


for i in coordList:
    t.pu()
    t.goto(0,i)
    t.pd()
    #t.dot()
    t.goto(-rCoordList[x],0)
    x=x+1     
    
    
x=0
for i in coordList:
    t.pu()
    t.goto(i,0)
    t.pd()
   #t.dot()
    t.goto(0,rCoordList[x])
    x=x+1    
        
x=0
for i in coordList:
    t.pu()
    t.goto(0,-i)
    t.pd()
    #t.dot()  
    t.goto(-rCoordList[x],0)
    x=x+1    
    
    
x=0
for i in coordList:
    t.pu()
    t.goto(i,0)
    t.pd()
    #t.dot()
    t.goto(0,-rCoordList[x])
    x=x+1
    
    
    
s2.exitonclick()