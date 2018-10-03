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
    colors = ["red","yellow","blue","salmon","peachpuff","orange","black","brown","green","violet","purple"]
   
    for cmd in instructions:
        #print(angle)
        t.color(random.choice(colors))
        
        if cmd == "F":
            t.fd(dist)
        elif cmd == "+":
            t.left(angle)
        elif cmd == "-":
            t.right(angle)

def main():
    inst = createLSystem(8, "FXF++FF++FF")
    print(inst)
    #F++F++F
    #B+B-F++F     //120
    
    t = turtle.Turtle()
    s = turtle.Screen()
    s.screensize(canvwidth=100000, canvheight=100000, bg=None)
    t.pu()
    #t.left(90)
    t.forward(-600)
    t.right(90)
    t.back(-400)
    t.left(90)
    #t.forward(200)
    
    t.pd()
    t.speed(0)
    
    drawLSystem(t,inst,60,2)
    t.ht()
    
    if 1 == 0:
        s.exitonclick()
   
    
main()

        
    