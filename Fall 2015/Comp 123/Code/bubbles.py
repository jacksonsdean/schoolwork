import turtle
import random
s = turtle.Screen()
tlist=list()


maggie = turtle.Turtle(shape="blank")
glenn = turtle.Turtle(shape="blank")
tlist=[glenn, maggie]


glenn.speed(100)
maggie.speed(100)
for n in range(15):
    
    for i in range(30):
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