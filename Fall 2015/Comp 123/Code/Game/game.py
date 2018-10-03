from tkinter import *
import enemy
import player_class

class Game:
    def __init__(self,master):
        #setup canvas-------------------------
        
        for widget in root.winfo_children():
            widget.destroy()
            
        self.canvas_width = 800;  self.canvas_height = 600
        
        self.c = Canvas(width=self.canvas_width, height=self.canvas_height)
        grass_bg = PhotoImage(file="Images/grass.png", width = self.canvas_width, height = self.canvas_height)
        grass_bg = grass_bg.zoom(2)
        
        self.canvas_bg = self.c.create_image(0,0,image = grass_bg)

        
        self.c.grid(row = 1, column=0)
        
        
        
        #setup infobar-------------------------
        self.infobar = Frame(root, bg ="grey", height = 30)
        self.infobar.grid(row = 0, column=0)
        h_sprite = PhotoImage(file="Images/heart.jpg")
        enemy.Squirrel(self,.5)
        #Player(self)
        root.mainloop()


global root 
root=Tk()     
app=Game(root)