import turtle 
import random

#Sierpinski sieve
#n = 6
#axiom = FXF++FF++FF
#rule = F -> FF , X -> ++FXF--FXF--FXF++
#angle = 60°
#s = 1 / 2
#d = 1.5849...


def createLSystem (iterations, axiom):
    startStr = axiom
    endStr = ""
    for i in range(iterations):
        endStr = processStr(startStr)
        startStr = endStr
    return endStr

def processStr(sStr):
    eStr = ""
    for char in sStr:
        eStr = eStr + applyRules(char)
    print(eStr)
    return eStr

def applyRules(char):
    newChar = ""
    if char == "F":
        newChar = "FF" #------------RULE 1------------#
    elif char == "X":
        newChar = "++FXF--FXF--FXF++" #------------RULE 2------------#
    else:
        newChar = char
    return newChar

def drawLSystem(t, instructions, angle, dist):
   
    for cmd in instructions:
      
        if cmd == "F":
            t.fd(dist)
        elif cmd == "+":
            t.left(angle)
        elif cmd == "-":
            t.right(angle)

def main():
    inst = createLSystem(6, "FXF++FF++FF")
    print(inst)
    #F++F++F
    #B+B-F++F     //120
    
    t = turtle.Turtle()
    s = turtle.Screen()
    s.screensize(canvwidth=100000, canvheight=100000, bg=None)
    
    t.color("white")
    s.bgcolor("black")
    
    t.pu()
    #t.left(90)
    t.goto(-400,-200)
    #t.forward(200)
    
    t.pd()
    t.speed(0)
    
    drawLSystem(t,inst,60,6.28318530718)
    t.ht()
    
    if 1 == 0:
        s.exitonclick()
   
    
main()

        
    
