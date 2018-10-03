from tkinter import *

class Game:
    def __init__(self,master=""):
        #setup canvas-------------------------
        
        for widget in root.winfo_children():
            widget.destroy()
            
        Game.canvas_width = 800;  Game.canvas_height = 600
        
        Game.c = Canvas(width=Game.canvas_width, height=Game.canvas_height, bg = "dark grey")
        #grass_bg = PhotoImage(file="Images/grass.png", width = Game.canvas_width, height = Game.canvas_height)
        #grass_bg = grass_bg.zoom(2)
        
        #self.canvas_bg = self.c.create_image(0,0,image = grass_bg)

        
        Game.c.grid(row = 1, column=0)
        
        #setup---------------------------------
        Game.items = []
        
        #setup infobar-------------------------
        self.infobar = Frame(root, bg ="grey", height = 30)
        self.infobar.grid(row = 0, column=0)
        h_sprite = PhotoImage(file="Images/heart.jpg")
        
        player = Player(self)
        Game.items.append(player)
                 
        
        try:
            while True:
                self.update_canvas()
        except TclError:
            print("END")
            pass
        

            
    def update_canvas(self):
        for i in range(len(Game.items)):
            Game.items[i].animate()
          
            
            
            root.update_idletasks() # redraw window
            root.update() # process user events
            
        
        
        
        
class Player:
    def __init__(self, parent):
        self.parent = parent
        Game = self.parent
        self.scot_r = PhotoImage(file='images/scot_r.gif')
        self.scot_l = PhotoImage(file="Images/scot_l.gif")
        self.scot_r = self.scot_r.zoom(2)
        self.scot_l = self.scot_l.zoom(2)
        
        self.dirs={}
        self.dirs["RIGHT"] = False
        self.dirs["LEFT"] = False
        self.dirs["UP"] = False
        self.dirs["DOWN"] = False
        
        
        self.lastDir = 1
        
        self.scot = Game.c.create_image(50,50,image=self.scot_r) 
        
        
        #BINDINGS---------------------------------   
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Up>', self.up)
        root.bind('<Down>', self.down)
        root.bind('<space>', self.shoot)
        
        #direction------------------------------
        self.dirX = 1
        self.dirY = 1
    
        
        
        
    #movement---------------------------------
    def left(self,event):
        Game = self.parent
        self.dirs["LEFT"] = True
        #self.dirX+=-1
        #self.dirY+=0
       
    def right(self,event):
        Game = self.parent
        self.dirs["RIGHT"]  = True
        #self.dirX+=1
        #self.dirY+=0

    def up(self,event):
        Game = self.parent
        self.dirs["UP"] = True
        #self.dirY+=-1
        #self.dirX+=0

    def down(self,event):
        Game = self.parent
        self.dirs["DOWN"] = True
        #self.dirY+=1
        #self.dirX+=0

    #move----------------------------------
    def animate(self):
        Game = self.parent
        if self.dirs["RIGHT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_r)
            self.lastDir = 1
        elif self.dirs["LEFT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_l)
            self.lastDir = -1
            
        if self.dirs["RIGHT"]  and not(self.dirs["LEFT"] or self.dirs["UP"] or self.dirs["DOWN"]):
            Game.c.move(self.scot, 4, 0)
            for direction in self.dirs:
                self.dirs[direction] = False
        elif self.dirs["LEFT"] and not(self.dirs["RIGHT"]  or self.dirs["UP"] or self.dirs["DOWN"]):
            Game.c.move(self.scot, -4, 0)
            for direction in self.dirs:
                self.dirs[direction] = False
        elif self.dirs["UP"] and not(self.dirs["LEFT"] or self.dirs["RIGHT"]  or self.dirs["DOWN"]):
            Game.c.move(self.scot, 0, -4)
            for direction in self.dirs:
                self.dirs[direction] = False
        elif self.dirs["DOWN"] and not(self.dirs["RIGHT"]  or self.dirs["LEFT"] or self.dirs["UP"]):
            Game.c.move(self.scot, 0, 4)
            for direction in self.dirs:
                self.dirs[direction] = False
        elif self.dirs["RIGHT"]  and self.dirs["UP"] and not (self.dirs["LEFT"] or self.dirs["DOWN"]):
            Game.c.move(self.scot, 0, 4)
            for direction in self.dirs:
                self.dirs[direction] = False
            
            
        #Game.c.move(self.scot, self.dirX*4, self.dirY*4)
        #self.dirX=0;self.dirY=0
        
            
    
    #Shoot----------------------------------
    
    def shoot(self,event):
        Game = self.parent
        coords = Game.c.coords(self.scot)
        x = coords[0]
        y = coords[1]   
        
        self.org = Projectile(Game,"orange",x,y,self.lastDir*1) 
        Game.items.append(self.org)
        if x > Game.canvas_width or y > Game.canvas_height:
            self.org.delete()
                    
        if x < 0 or y < 0:
            self.org.delete()         
                   
        Game.c.after(2000,self.org.delete) 
        
        
        o_coords = Game.c.coords(self.org)
        
        #ox = o_coords[0]
        #oy = o_coords[1]             
             
       
                    
       
        
        

root = Tk()
app = Game()

        
