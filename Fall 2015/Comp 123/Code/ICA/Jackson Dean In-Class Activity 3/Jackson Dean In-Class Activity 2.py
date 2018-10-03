import turtle
import random

#Part 1:

print("4 + 9 =", 4+9, "type is:",type(4+9))
print("4 + 9.0 =", 4+9.0, "type is:",type(4+9.0))
print("3.2 - 1.1 =", 3.2-1.1, "type is:",type(3.2-1.1))
print("3 - 1 =", 3-1, "type is:", type(3-1))
print("3 - 1.0 =", 3-1.0, "type is:", type(3-1.0))
print("4 * 5 =", 4*5, "type is:", type(4*5))
print("4 * 6.5 =", 4*6.5, "type is:", type(4*6.5))
print("25 / 3 =", 25/3, "type is:", type(25/3))
print("25 / 3.0 =", 25/3.0, "type is:", type(25/3.0))
print("25 // 3 =", 25//3, "type is:", type(25//3))
print("25.0 // 3.0 =", 25.0//3.0, "type is:", type(25.0//3.0))
print("25 % 3 =", 25%3, "type is:", type(25%3))
print("40 % 11.0 =", 40%11.0, "type is:", type(40%11.0))
print("3^2 =", 3**2, "type is:", type(3**2))
print("2.0^3 =", 2.0**3, "type is:", type(2.0**3))




#Part 2:

banannaLen = 15.5
numBanannas = input("How many banannas do you have?")

totalLen = float(numBanannas) * banannaLen/100

print("If you had", numBanannas,"banannas of length", banannaLen,', you would have', totalLen, "meters of bananna.")



#BUBBLES:


tlist=list()
s = turtle.Screen()

maggie = turtle.Turtle(shape="blank")
glenn = turtle.Turtle(shape="blank")
tlist=[glenn, maggie]


glenn.speed(100)
maggie.speed(100)    
for i in range(50):
    for item in tlist: 
        item.up()
        item.goto(random.randrange(-500,500),random.randrange(-400,400))
        item.down()        
        de=("%02x"%random.randint(0,255))
        re=("%02x"%random.randint(0,255))
        we=("%02x"%random.randint(0,255))
    
        color="#"+re+we+we        
        item.color(color)
        #item.left(random.randrange(-180,180))
        item.left(i)
        #item.forward(i)
        item.circle(i**1.1)

s.exitonclick()