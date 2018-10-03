from tkinter import*

c=Canvas(height=600, width=800, bg='orange')
c.grid(row=0, column=0)
x=0;y=0;x1=25;y1=25
wallLen=31
wallLen2=23
class Wall:
    def __init__(self, x, y, x1, y1):
        sqWall =c.create_rectangle(x, y, x1, y1, fill='blue')
        strng= str((x, y))
        c.create_text(x+25,y+30, text=strng, font=('arial',7))
        


for i in range(wallLen):
    Wall(x, y, x1, y1)
    x+=25;y+=0;x1+=25;y1+=0
for i in range(wallLen2-3):
    if y==275:
        y+=75;y1+=75    
    Wall(x, y, x1, y1)
    y+=25;y1+=25
for i in range(wallLen):
    Wall(x, y, x1, y1)
    x-=25;y+=0;x1-=25;y1+=0
for i in range(wallLen2):
    if y==325:
        y-=75;y1-=75

    Wall(x, y, x1, y1)
    y-=25;y1-=25
    
for i in range(1):
    x=25;y=200;x1=50;y1=225
    for j in range(10):
        Wall(x+(25*j),y,x1+(25*j),y1)
    for j in range(3):
        Wall(275,y+(25*j),300,y1+(j*25))
        

root=Tk()
root.mainloop()