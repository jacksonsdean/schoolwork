import turtle
import random
import math



def starOutline(turt, sideLen):
    """Create a five pointed star outline at the current location and heading using the input turt and sideLen"""
    for i in range(5):
        turt.forward(sideLen)
        turt.right(120)
        turt.forward(sideLen)
        turt.left(48)
        
def gridOfStars(t):
    """Takes in no inputs, and displays a turtle graphics screen. The turtle
    in it draws 9 star shapes in a grid"""
    for coord in [(0, 0), (-200, 0), (-200, -200), 
                  (0, -200), (200, -200), (200, 0), 
                  (200, 200), (0, 200), (-200, 200)]:
        t.up()
        t.goto(coord)
        t.down()
        starOutline(t, 60)
   


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
    
    
def drawSquare(t, sideLen):
    for i in range (4):
        t.forward(sideLen)
        t.right(90)
        
def drawTriangle(t, z, a, b=90):
    c =  180 - (a + b)
    
    #    x/sin(b) = y/sin(a) = z/sin(c) 
    
    y =  abs((math.sin(a)*z)/math.sin(c))
    
    x = abs((math.sin(b)*z)/math.sin(c))
    
    print("angle1:",a,"\n","angle2:",b,"\n","angle3:", c,"\n","z:",z,"\n","y:",y,"\n","x:",x)
    
    t.forward(z)
    t.left(180-b)
    t.forward(y)
    t.left(180-c)
    t.forward(x)
    t.left(180-a)
    
def draw60Triangle(t,sideLen):
    t.forward(sideLen)
    t.left(120)
    t.forward(sideLen)
    t.left(120)
    t.forward(sideLen)
    
def drawHexagon(t,sideLen):
    for i in range(6):
        t.forward(sideLen)
        t.left(60)

def drawOctagon(t,sideLen):
    for i in range(8):
            t.forward(sideLen)
            t.left(45)    