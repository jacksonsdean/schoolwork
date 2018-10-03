import turtle

s = turtle.Screen()

t = turtle.Turtle()

t.ht()

t.speed(0)

x=0

coordList = []
for i in range(0,357,17):
    coordList.append(i)

rCoordList= coordList[::-1]

#print(coordList)
#print(rCoordList)

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
    
    
    

    
s.exitonclick()