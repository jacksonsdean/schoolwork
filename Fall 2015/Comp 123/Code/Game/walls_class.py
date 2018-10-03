from tkinter import*

c=Canvas(height=600, width=800, bg='orange')
c.grid(row=0, column=0)

class Wall:
    def __init__(self, startx, starty, endx, endy):
        
        wallLenx = endx-startx
        wallLeny = endy - starty
        x = startx
        y = starty
        x1 = startx+25
        y1 = starty+25
        
        distx = wallLenx//25
        disty = wallLeny//25
        stepx = 25
        stepy = 25
        
        if distx < 0:
            stepx = -1*stepx
        if disty < 0:
            stepy = -1*stepy
        
        if distx == 0:
            stepx = 0
        if disty == 0:
            stepy = 0
            
        for i in range(max(distx,disty)):
            sqWall =c.create_rectangle(x, y, x1, y1, fill='blue')
            strng= str((x, y))
            c.create_text(x+25,y+30, text=strng, font=('arial',7))
            x+=stepx;y+=stepy;x1+=stepx;y1+=stepy
        
#EDGE WALLS:---------------------------------------------------------
walls = {
    "topwall": Wall(startx=0, starty=0, endx=800, endy=0),
    "rightwall1": Wall(775, 0,775,275),
    "rightwall2": Wall(775,325,775,600),
    "bottomwall": Wall(0, 575,775,575),
    "leftwall1": Wall(0,25, 0,275),
    "leftwall2": Wall(0,325, 0,575),

#INTERIOR WALLS-----------------------------------------------------
    "wall1": Wall(25,250,300,250),
    "wall2": Wall(300,250,300,325),

}

root=Tk()
root.mainloop()