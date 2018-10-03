import turtle

strng = input("What is your name: ")

s= turtle.Screen()
turt = turtle.Turtle()
#turt.hideturtle()

def drawHello():
    hTurt = turtle.Turtle()
    hTurt.pu()
    hTurt.hideturtle()
    hTurt.goto(-150,185)
    hTurt.write("Hello", align = "center",font=("Arial", 80,"normal"))


    
def drawLetters(t):
    t.pu()
    t.backward(250)
    turt.speed(.99)
    for l in strng:
         t.write((l),move=True,align="center",font=("Helvetica",110,"bold")) 
         t.pd()
         t.forward(40)
    t.write("!",move=True, align="center",font=("Helvetica",110,"bold"))
         
    
drawHello()
drawLetters(turt)
s.exitonclick()
    
    