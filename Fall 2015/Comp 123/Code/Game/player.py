from tkinter import*
import time
root = Tk()
c=Canvas(root,width=800,height=600)
scotIMG = PhotoImage(file='scot_r.png')
scot = c.create_image(50,50,image=scotIMG)

#class player:
    

#movement---------------------------------
def left(event):
    for i in range(1):
        c.move(scot, -10, 0)
        c.update()
        dirX=-2
    return dirX
   
def right(event):
    for i in range(1):
        c.move(scot, 10, 0)
        c.update()
        dirX=2
    return dirX
   
def up(event):
    for i in range(1):
        c.move(scot, 0, -10)
        c.update()
        dirY=-2
    return dirY        
    
def down(event):
    for i in range(1):
        c.move(scot, 0, 10)
        c.update()
        dirY=2
    return dirY       
        
#direction------------------------------

#Shoot----------------------------------
canvas_width = 800;  canvas_height = 600
def shoot(event):
    coords = c.coords(scot)
    ex = coords[0]
    ey = coords[1]   
    o_sprite = PhotoImage(file="orange.png")        
    org = c.create_image(ex,ey,image = o_sprite)
    
    for n in range(75):
        coords = c.coords(org)
        x = coords[0]
        y = coords[1]             
        time.sleep(.005) 
        c.move(org,dirX,dirY) 
        if x > canvas_width or y > canvas_height:
                c.delete(org)
                break
        if x < 0 or y < 0:
                c.delete(org) 
                break
        c.update()
    c.delete(org)





#BINDINGS---------------------------------   
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<space>', shoot)

c.pack()
root.mainloop()