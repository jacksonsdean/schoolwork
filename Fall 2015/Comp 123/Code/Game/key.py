
from tkinter import *
import time
import math
from PIL import Image         # Note new import
import PIL.ImageTk as ImageTk    # Note new import


class MainMenu:
    def __init__(self,master):
        root = master
        frame = Frame(root, width = 800, height = 600, bg = "light blue", padx = 0, pady = 0)
        
        adventure_img = readImage("Images/scotty_adv.gif", 3)
        
        adventure_title = Label(frame, image = adventure_img)
        
        new_game_button = Button(frame, text = "New Game",
                                font = "Arial 40 bold",
                                bg = "lightgrey",
                                bd = 5,
                                relief = GROOVE,
                                activebackground = "orange",
                                width = 12,
                                command = self.clickNewGame
                                )
        
        instructions_button = Button(frame, text = "Instructions",
                                    font = "Arial 40 bold",
                                    bg = "lightgrey",
                                    bd = 5,
                                    relief = GROOVE,                                    
                                    activebackground = "orange",
                                    width = 12,
                                    command = self.clickInstructions
                                    )
        
        credits_button = Button(frame, text = "Credits",
                                font = "Arial 40 bold",
                                bg = "lightgrey",
                                bd = 5,
                                relief = GROOVE,
                                activebackground = "orange",
                                width = 12,                                
                                command = self.clickCredits
                                ) 
        
        quit_button= Button(frame, text = "Quit",
                               font = "Arial 40 bold",
                               bg = "lightgrey",
                               bd = 5,
                               relief = GROOVE,
                               activebackground = "orange",
                               width = 12,                               
                               command = self.clickQuit
                               )
           
           
        adventure_title.grid(row = 0, column = 1)
        new_game_button.grid(row = 1, column = 1)
        instructions_button.grid(row = 2, column = 1)
        credits_button.grid(row = 3, column = 1)
        quit_button.grid(row = 4, column = 1)
        frame.pack()
        
        root.mainloop()
    
    

  
    
    def clickNewGame(self):
        Game(master=root)
        
    def clickInstructions(self):
        print("instructions")
        
    def clickCredits(self):
        print("credits")
        
    def clickQuit(self):
        print("quit")
        root.destroy()
        
    
    

def readImage(filename, zoom = 1):
    img1 = Image.open(filename)
    (imWid, imHgt) = img1.size
    img1 = img1.resize( (zoom * imWid, zoom * imHgt) )
    return ImageTk.PhotoImage(img1)
    


class Game:
    def __init__(self,master=""):
        #setup canvas-------------------------
        
        for widget in root.winfo_children():
            widget.destroy()
            
        Game.canvas_width = 800;  Game.canvas_height = 600
        
        Game.c = Canvas(width=Game.canvas_width, height=Game.canvas_height, bg = "orange")
        #grass_bg = PhotoImage(file="Images/grass.png", width = Game.canvas_width, height = Game.canvas_height)
        #grass_bg = grass_bg.zoom(2)
        
        #self.canvas_bg = self.c.create_image(0,0,image = grass_bg)

        
        Game.c.grid(row = 1, column=0)
        
        #setup---------------------------------
        Game.items = []
        
        #setup infobar-------------------------
        self.infobar = Frame(root, bg ="grey", height = 30)
        self.infobar.grid(row = 0, column=0)
        #h_sprite = PhotoImage(file="Images/heart.jpg")
        h_sprite = readImage("Images/heart.jpg")
        
        #setup enemies--------------------------
        #enemy1 = Squirrel(self,x=500,y=200,speedX=0,speedY = 3, shotFreq = 100)
        #enemy2 = Squirrel(self, 200,200,0,1,120)  
        #enemy3 = Squirrel(self, 300,200,0,2,324)
        #enemy4 = Squirrel(self,400,200,0,1.3,433)
        #enemy5 = Squirrel(self,500,200,0,1.6,544)
        #enemy6 = Squirrel(self,600,200,0,3,727)
        
        #Game.items.append(enemy1)
        #Game.items.append(enemy2)
        #Game.items.append(enemy3)
        #Game.items.append(enemy4)    
        #Game.items.append(enemy5)
        #Game.items.append(enemy6)
        
        player = Player(self)
        Game.items.append(player)
        
        
        
    #OTHER OBJS:
        Game.key1 = Key(200,200)
        
#SETUP WALLS:


        
        #EDGE WALLS:---------------------------------------------------------
        Game.walls = {
            "w1": Wall(startx=0, starty=0, endx=800, endy=0,tag="w1"), #topwall
            "w2": Wall(775, 0,775,250,"w2"), #rightwalltop
            "w3": Wall(775,325,775,600,"w3"), #rightwallbottom
            "w4": Wall(0, 575,775,575,"w4"), #bottomwall
            "w5": Wall(0,25, 0,250,"w5"), #leftwalltop
            "w6": Wall(0,325, 0,575,"w6"), #leftwallbottom
        
        #INTERIOR WALLS-----------------------------------------------------
            "w7": Wall(25,225,300,225,"w7"),
            "w8": Wall(300,225,300,325,"w8"),
            
            
            
            
        
        }
        
        for key in Game.walls.keys():
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3] 
           
           
        Game.door = Door(775,250)      
        
        try:
            while True:
                self.update_canvas()
        except TclError:
            print("END")
            pass
        

            
    def update_canvas(self):
        time.sleep(.01)
        for i in range(len(Game.items)):
            Game.items[i].animate()
          
            
            
        root.update_idletasks() # redraw window
        root.update() # process user events
            
        
        
class Player:
    def __init__(self, parent):
        self.parent = parent
        Game = self.parent
        self.scot_r = readImage("Images/scot_r.gif",2) #PhotoImage(file='images/scot_r.gif')
        self.scot_l = readImage("Images/scot_l.gif",2) #PhotoImage(file="Images/scot_l.gif")
        #self.scot_r = self.scot_r.zoom(2)
        #self.scot_l = self.scot_l.zoom(2)
        
        self.dirs={}
        self.dirs["RIGHT"] = False
        self.dirs["LEFT"] = False
        self.dirs["UP"] = False
        self.dirs["DOWN"] = False
        
        self.ableToShoot = True
        self.fireRate = 100
        self.lastDir = 1
        
        self.scot = Game.c.create_image(50,275,image=self.scot_r) 
        self.playerBox = Game.c.bbox(self.scot)
        self.playerCoords = Game.c.coords(self.scot)
            
        
        
    #BINDINGS---------------------------------   
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Up>', self.up)
        root.bind('<Down>', self.down)
        root.bind('<space>', self.shoot)
        
    #movement---------------------------------
    def left(self,event):
        Game = self.parent
        self.dirs["LEFT"] = True
       
    def right(self,event):
        Game = self.parent
        self.dirs["RIGHT"]  = True

    def up(self,event):
        Game = self.parent
        self.dirs["UP"] = True

    def down(self,event):
        Game = self.parent
        self.dirs["DOWN"] = True

    #move----------------------------------
    def animate(self):
        Game = self.parent
        self.playerBox = Game.c.bbox(self.scot)
        self.playerCoords = Game.c.coords(self.scot)
        player_coords = self.playerCoords
        playerx = self.playerCoords[0]
        playery = self.playerCoords[1]
        right_collision = False
        left_collision = False
        up_collision = False
        down_collision = False
        key_pickup=False
        
        if self.dirs["RIGHT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_r)
            self.lastDir = 1
        elif self.dirs["LEFT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_l)
            self.lastDir = -1

            
    #COLLISION----------------------------------------------------------
    
        for key in Game.walls.keys():
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3]
            
            #LEFT:
            if abs(playerx - wallX2)<=13:
                if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                    left_collision=True
            #RIGHT      
            if abs(playerx - wallX1)<=13:
                if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                    right_collision=True
            #UP        
            if abs(playery - wallY2)<=25:
                if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                    up_collision=True
            #DOWN        
            if abs(playery - wallY1)<=40:
                if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                    down_collision=True

        #MOVE----------------------------------------------------------------------------------
            
        if self.dirs["RIGHT"] and not(right_collision):
            Game.c.move(self.scot, 5, 0)
        elif self.dirs["LEFT"] and not(left_collision):
            Game.c.move(self.scot, -5, 0)
        elif self.dirs["UP"] and not(up_collision):
            Game.c.move(self.scot, 0, -5)
        elif self.dirs["DOWN"] and not(down_collision):
            Game.c.move(self.scot, 0, 5)
                
                
        elif self.dirs["RIGHT"] and self.dirs["UP"] and not(right_collision or up_collision):
            Game.c.move(self.scot, 5, 5)
        elif self.dirs["LEFT"] and self.dirs["UP"] and not(left_collision or up_collision):
            Game.c.move(self.scot, -5, 5)
        elif self.dirs["RIGHT"] and self.dirs["DOWN"] and not(down_collision or right_collision):
            Game.c.move(self.scot, 5, -5)
        elif self.dirs["LEFT"] and self.dirs["DOWN"] and not(down_collision or left_collision):
            Game.c.move(self.scot, 0, 5)
    
        for direction in self.dirs:
            self.dirs[direction] = False        
            
            
    #ITEM COLLISION-------------------------
        kbx = Game.key1.keyBBOX
        #LEFT:
        if abs(playerx - kbx[2])<=13:
            if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                key_pickup = True 
        #RIGHT      
        if abs(playerx - kbx[0])<=13:
            if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                key_pickup = True 
        #UP        
        if abs(playery - kbx[3])<=25:
            if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                key_pickup = True 
        #DOWN        
        if abs(playery - kbx[1])<=40:
            if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                key_pickup = True 

        if key_pickup:
            Game.key1.pickup()
    
        
    #Shoot----------------------------------
    
    def shoot(self,event):
        Game = self.parent
        coords = Game.c.coords(self.scot)
        
        x = coords[0]
        y = coords[1]   
        if self.ableToShoot:
            self.org = Projectile(Game,"orange",x,y,self.lastDir*1) 
            Game.items.append(self.org)
            if x > Game.canvas_width or y > Game.canvas_height:
                self.org.delete()
                        
            if x < 0 or y < 0:
                self.org.delete()         
                       
            #Game.c.after(2000,self.org.delete) 
            
            self.ableToShoot = False
            Game.c.after(self.fireRate, self.shotCooldown)
        
       
    def shotCooldown(self):
        self.ableToShoot = True
    def moveCooldown(self):
        self.ableToMove = True
       
        
        
    

        
class Squirrel:
    def __init__(self,parent,x=0,y=0,speedX=0, speedY=2, shotFreq = 400):
        self.parent = parent
        Game = self.parent
        #setup Squirrel---------------------------
        self.r_sprite = readImage("Images/squirrel_r.gif", 2) #PhotoImage(file="Images/squirrel_r.gif")
        self.l_sprite = readImage("Images/squirrel_l.gif", 2) #PhotoImage(file="Images/squirrel_l.gif")
        #self.r_sprite = self.r_sprite.zoom(2)
        #self.l_sprite = self.l_sprite.zoom(2)
        
        self.obj = Game.c.create_image(x,y,image = self.l_sprite)
        self.width = self.r_sprite.width()
        self.height = self.r_sprite.height()
        
       #state vars----------------------------------------------- 
        self.alive = True
        self.n = 0 
        self.dirY = 1
        self.dirX = -1  
        self.shotFreq = shotFreq
        self.shotRange = 1000
        self.speedX = speedX
        self.speedY = speedY
    
        
        
             
       
    
    def animate(self):
        Game = self.parent
        #vars---------------------
        deltay=self.speedY
        deltax=self.speedX

        coords = Game.c.coords(self.obj)
        x = coords[0]
        y = coords[1]
        
        
        #check boundries--------------------------
            
        if x+self.width>float(Game.c["width"]):
            self.dirX=-1
            Game.c.itemconfigure(self.obj, image= self.l_sprite)

        if x-self.width<0:
            self.dirX=1 
            Game.c.itemconfigure(self.obj, image= self.r_sprite)
            
        if y+self.height>float(Game.c["height"]):
            self.dirY=-1
                   

        if y-self.height<0:
            self.dirY=1        
            
        
        #movement------------------------
        Game.c.move(self.obj,self.dirX*deltax,self.dirY*deltay)
             
        
        if self.n%self.shotFreq == 0:
            self.popcorn = Projectile(Game,"popcorn",x,y,self.dirX)
            Game.items.append(self.popcorn)
            
            #Game.c.after(self.shotRange, self.popcorn.delete)
            
        self.n+=1
        
        if self.n > 8000:
            self.n = 0
            
            
        
class Projectile:
    def __init__(self,parent,projType,x,y,dirX):
        Projectile.parent = parent
        Game = self.parent
        self.dirX = dirX
        self.deleted = False
        
        if projType == "popcorn":
            self.sprite = readImage("Images/popcorn.gif") #PhotoImage(file="Images/popcorn.gif") 
        elif projType == "orange":
            self.sprite = readImage("Images/orange.gif") #PhotoImage(file="Images/orange.gif") 
        else:
            self.sprite = readImage("Images/orange.gif") #PhotoImage(file="Images/orange.gif") 
            
        
        self.obj = Game.c.create_image(x,y,image = self.sprite)
   
    def animate(self): 
        Game = Projectile.parent
        if not self.deleted:
            projx = Game.c.coords(self.obj)[0]
            projy = Game.c.coords(self.obj)[1]
        
        #COLLISION-----------------------------------------------------------
        
        for key in Game.walls.keys():
            if self.deleted:
                break
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3]
            if abs(projx - wallX2)<=13:
                if wallY1<= projy-20 <= wallY2 or wallY1<=projy+35 <=wallY2:
                    self.delete()
                    break
            #RIGHT      
            if abs(projx - wallX1)<=13:
                if wallY1<= projy-20 <= wallY2 or wallY1<=projy+35 <=wallY2:
                    self.delete()
                    break
            #UP        
            if abs(projy - wallY2)<=25:
                if wallX1<= projx-6 <= wallX2 or wallX1<=projx+6 <=wallX2:
                    self.delete()
                    break
            #DOWN        
            if abs(projy - wallY1)<=40:
                if wallX1<= projx-6 <= wallX2 or wallX1<=projx+6 <=wallX2:
                    self.delete()
                    break
            
        
        
        Game.c.move(self.obj,self.dirX*6,0)
        
        
        
        
        
        
    def delete(self): 
        Game = Projectile.parent
        try:
            Game.items.remove(self.obj)
        except ValueError:
            pass        
        self.deleted = True
        Game.c.delete(self.obj) 
        


class Wall:
    def __init__(self, startx, starty, endx, endy, tag):
        self.wallLenx = endx-startx
        self.wallLeny = endy - starty
        x = startx
        y = starty
        x1 = startx+25
        y1 = starty+25
        
        distx = self.wallLenx//25
        disty = self.wallLeny//25
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
            sqWall =Game.c.create_rectangle(x, y, x1, y1, fill='blue', tag = tag)
            x+=stepx;y+=stepy;x1+=stepx;y1+=stepy







class Key():
    def __init__(self,x,y):
        
        self.sprite = readImage("Images/key.gif", 1)
        self.obj = Game.c.create_image(x,y,image=self.sprite)
        self.keyBBOX = Game.c.bbox(self.obj)
        
    def pickup(self):
        Game.c.delete(self.obj) 
        Game.door.opn()
        
        
        
        
class Door():
    def __init__(self,x,y):
        self.obj =Game.c.create_rectangle(x, y, x+25, y+75, fill='brown')
        
    def opn(self):
        Game.c.delete(self.obj) 
        
        


                  
          
#setup window and start------------------------------        
root = Tk()
root.title("Scoty's Adventure")
root.config(bg = "grey", width = 800, height = 600)
root.resizable(width=FALSE, height=FALSE)

app = MainMenu(master=root)        
        