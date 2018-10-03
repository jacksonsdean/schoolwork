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
        app = Game(master=root)
        
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
    def __init__(self,master):
        Game.ticks = 0
        Game.pause = False
        
        def pause():
            print("pause")
            if Game.pause:
                Game.pause = False
            else:
                Game.pause = True
                    
        def mainMenu():
            print("main menu")
                     
        def quit():
            print("quit")
            root.destroy()                
        
        #setup canvas-------------------------
        for widget in root.winfo_children():
            widget.destroy()
            
        Game.canvas_width = 800;  Game.canvas_height = 600
        
        Game.c = Canvas(width=Game.canvas_width, height=Game.canvas_height, bg = "orange")
        
        Game.c.grid(row = 1, column=0)
        
        #setup---------------------------------
        Game.items = []
        
        #setup infobar-------------------------
        Game.infobar = Frame(root, bg ="grey", height = 30)
        Game.infobar.grid(row = 0, column=0)
        h_sprite = readImage("Images/heart.jpg")
        h_label = Label(Game.infobar, image = h_sprite)
        h_label.grid(row = 1, column = 1)
        pause_button = Button(Game.infobar, text="PAUSE", command=pause)
        pause_button.grid(row = 1, column = 3)
        mainMenu_button=Button(Game.infobar, text="MAIN MENU", command=mainMenu)
        mainMenu_button.grid(row = 1, column = 4)
        quit_button = Button(Game.infobar, text="QUIT", command=quit)
        quit_button.grid(row = 1, column = 5)        
          
        #setup enemies--------------------------
        enemy1 = Squirrel(self,x=600,y=200,speedX=1,speedY = 1, shotFreq = 100)
        #enemy2 = Squirrel(self, 200,200,0,1,120)  
        
        Game.items.append(enemy1)
        #Game.items.append(enemy2)
        
        turret1 = Turret(450,400, 300)
        Game.items.append(turret1)
        
        Game.projs = []
        
        Game.player = Player(self)
        Game.items.append(Game.player)
        
        #OTHER OBJS:--------------------------------------------
        Game.key1 = Key(360,400)
        Game.bp1 = Bagpipe(100,100)
        
        #SETUP WALLS:--------------------------------------------------------
        
        #EDGE WALLS:---------------------------------------------------------
        Game.walls = {
            "w1": Wall(startx=0, starty=0, endx=800, endy=0,tag="w1"), #topwall
            "w2": Wall(775, 0,775,250,"w2"), #rightwalltop
            "w3": Wall(775,325,775,600,"w3"), #rightwallbottom
            "w4": Wall(0, 575,775,575,"w4"), #bottomwall
            "w5": Wall(0,25, 0,250,"w5"), #leftwalltop
            "w6": Wall(0,325, 0,575,"w6"), #leftwallbottom
            "wOut": Wall(-25,0,-25,575,"wOut"),
        
        #INTERIOR WALLS-----------------------------------------------------
            "w7": Wall(25,225,200,225,"w7"),
            "w8": Wall(200,225,200,325,"w8"),
            "w9": Wall(25,400,200,400,"w9"),
            "w10": Wall(200,400,200,500,"w10"), 
            
            "w11": Wall(300,150,300,450,"w11"), #grille topwall
            "w11.5": Wall(400,150,400,200, "w11.5"),
            "w12": Wall(325,150,425,150,"w12"), #grille leftwall
            "w13": Wall(475,150,475,450,"w13"), #grille rightwall
            "w14": Wall(325,425,475,425,"w14"), #grille bottomwall
            "w19": Wall(400,275,400,450,"w19"),
            
            "w15": Wall(650,100,650,175,"w15"),
            "w16": Wall(650,175,775,175,"w16"),
            
            "w17": Wall(650,375,650,575,"w17"),
            "w18": Wall(650,375,725,375,"w18"),
            
            
            #DOOR:
            "d1": Door(775,250,"d1"),      
        }
        
        Game.door = Game.walls["d1"]
        
        for key in Game.walls.keys():
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3]
            
        Game.wallObjs = []
        for wall in Game.walls.values():
            Game.wallObjs.append(wall.obj) 
        
        try:
            while True:
                self.update_canvas()
        except TclError:
            print("END")
            pass
            
    def update_canvas(self):
        if not Game.pause:
            Game.ticks +=1            
            for i in range(len(Game.items)):
                time.sleep(.01)
                Game.items[i].update()
            
        root.update_idletasks() # redraw window
        root.update() # process user events
        
class Player:
    def __init__(self, parent):
        self.parent = parent
        Game = self.parent
        self.scot_r = readImage("Images/scot_r.gif",2) #PhotoImage(file='images/scot_r.gif')
        self.scot_l = readImage("Images/scot_l.gif",2) #PhotoImage(file="Images/scot_l.gif")
        
        self.dirs={}
        self.dirs["RIGHT"] = False
        self.dirs["LEFT"] = False
        self.dirs["UP"] = False
        self.dirs["DOWN"] = False
        
        self.ableToShoot = True
        self.fireRate = 100
        self.lastDir = 1
        self.mx = 1
        self.my= 1
        self.key_pickup = False
        
        self.lastTicks = Game.ticks
        
        self.hitbox = Game.c.create_rectangle(3,255,32,320,fill='',outline='black')
        self.scot = Game.c.create_image(18,280,image=self.scot_r,tag = self) 
        self.playerBox = Game.c.bbox(self.scot)
        self.playerCoords = Game.c.coords(self.scot)
            
    #BINDINGS---------------------------------   
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Up>', self.up)
        root.bind('<Down>', self.down)
        root.bind('<space>', self.shoot)
        root.bind('<P>',Game.pause)
     
    def key(event):
        print("key")
    #movement---------------------------------
    def left(self,event):
        Game = self.parent
        self.dirs["LEFT"] = True
        self.mx = -1
        self.my = 0
       
    def right(self,event):
        Game = self.parent
        self.dirs["RIGHT"]  = True
        self.mx = 1
        self.my = 0

    def up(self,event):
        Game = self.parent
        self.dirs["UP"] = True
        self.my = 1
        self.mx = 0

    def down(self,event):
        Game = self.parent
        self.dirs["DOWN"] = True
        self.my = -1
        self.mx = 0

    #move----------------------------------
    def update(self):
        Game = self.parent
        self.playerBox = Game.c.bbox(self.scot)
        self.playerCoords = Game.c.coords(self.scot)
        player_coords = self.playerCoords
        playerx = self.playerCoords[0]
        playery = self.playerCoords[1]
        self.ableToShoot = True
        key_pickup = False
        col = False
        
        self.right_collision = False
        self.left_collision = False
        self.up_collision = False
        self.down_collision = False
          
        
        if self.dirs["RIGHT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_r)
            self.lastDir = 1
        elif self.dirs["LEFT"]:
            Game.c.itemconfigure(self.scot, image= self.scot_l)
            self.lastDir = -1
            
    #COLLISION-------------------------------------------------------
    
        for key in Game.walls.keys():
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3]
            #LEFT:
            if abs(playerx - wallX2)<=13:
                if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                    self.left_collision=True
            #RIGHT      
            if abs(playerx - wallX1)<=13:
                if wallY1<= playery-20 <= wallY2 or wallY1<=playery+35 <=wallY2:
                    self.right_collision=True
            #UP        
            if abs(playery - wallY2)<=25:
                if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                    self.up_collision=True
            #DOWN        
            if abs(playery - wallY1)<=40:
                if wallX1<= playerx-6 <= wallX2 or wallX1<=playerx+6 <=wallX2:
                    self.down_collision=True
                    
        #END GAME CHECK:
        if playerx > 800:
            for widget in root.winfo_children():
                widget.destroy()
            app = WinScreen()

        self.collision()

#MOVE----------------------------------------------------------------------------------
        #for dr in self.dirs.values():
            #if dr:
                #Game.c.move(self.scot,5*self.mx,5*self.my)
        
        if self.dirs["RIGHT"] and self.dirs["UP"] and not(self.right_collision or self.up_collision):
            Game.c.move(self.scot, 5, 5); Game.c.move(self.hitbox, 5, 5)
        if self.dirs["LEFT"] and self.dirs["UP"] and not(self.left_collision or self.up_collision):
            Game.c.move(self.scot, -5, 5); Game.c.move(self.hitbox, -5, 5)
        if self.dirs["RIGHT"] and self.dirs["DOWN"] and not(self.down_collision or self.right_collision):
            Game.c.move(self.scot, 5, -5); Game.c.move(self.hitbox, 5, -5)
        if self.dirs["LEFT"] and self.dirs["DOWN"] and not(self.down_collision or self.left_collision):
            Game.c.move(self.scot, 0, 5); Game.c.move(self.hitbox, -5, 5)
        
        
               
        if self.dirs["RIGHT"] and not(self.right_collision):
            Game.c.move(self.scot, 5, 0); Game.c.move(self.hitbox, 5, 0)

        if self.dirs["LEFT"] and not(self.left_collision):
            Game.c.move(self.scot, -5, 0); Game.c.move(self.hitbox, -5, 0)
        if self.dirs["UP"] and not(self.up_collision):
            Game.c.move(self.scot, 0, -5); Game.c.move(self.hitbox, 0, -5)
        if self.dirs["DOWN"] and not(self.down_collision):
            Game.c.move(self.scot, 0, 5); Game.c.move(self.hitbox, 0, 5)
                
                
    
        for direction in self.dirs:
            self.dirs[direction] = False       
           
        
    def collision(self):
        x = self.playerCoords[0]
        y = self.playerCoords[1]
        playerCoords = Game.c.bbox(self.hitbox)
        
        overlapping = Game.c.find_overlapping(playerCoords[0],playerCoords[1],playerCoords[2],playerCoords[3]) 
        
        
        for obj in overlapping:
            if obj == Game.key1.obj:
                Game.key1.pickup()
            if obj == Game.bp1.obj:
                Game.bp1.pickup()            
            if obj in Game.projs:
                if Game.c.gettags(obj) != ('orange',):
                    self.die()
            #if obj in Game.wallObjs:
                #print(obj)
                #if Game.c.coords(obj)[0] > x:
                    #self.right_collision = True
                #if Game.c.coords(obj)[0] < x:
                    #self.left_collision = True
                #if Game.c.coords(obj)[1] > y:
                    #self.down_collision = True
                #if Game.c.coords(obj)[1] < y:
                    #self.up_collision = True
                                                
    #Shoot----------------------------------
    
    def shoot(self,event):
        Game = self.parent
        coords = Game.c.coords(self.scot)
        
        x = coords[0]
        y = coords[1]   
        if Game.ticks-self.lastTicks>self.fireRate:
            self.org = Projectile(Game,"orange",x,y,self.lastDir*1,0) 
            Game.items.append(self.org)
            if x > Game.canvas_width or y > Game.canvas_height:
                self.org.delete()
                        
            if x < 0 or y < 0:
                self.org.delete()  

            self.lastTicks = Game.ticks
            
        
    def die(self):
        Game.c.coords(self.scot,18,275)
        Game.c.coords(self.hitbox,3,250,32,315)
        
        if self.key_pickup:
            Game.key1.drop()
       
        
class Squirrel:
    def __init__(self,parent,x=0,y=0,speedX=0, speedY=2, shotFreq = 400):
        self.parent = parent
        Game = self.parent
        #setup Squirrel---------------------------
        self.r_sprite = readImage("Images/squirrel_r.gif", 2)
        self.l_sprite = readImage("Images/squirrel_l.gif", 2)
        
        self.obj = Game.c.create_image(x,y,image = self.l_sprite,tag = "Squirrel")
        
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
       
    
    def update(self):
        Game = self.parent
        
        #vars---------------------
        deltay=self.speedY
        deltax=self.speedX
        coords = Game.c.coords(self.obj)
        x = coords[0]
        y = coords[1]
        
        #check boundries--------------------------
        #if x+self.width>float(Game.c["width"]):
            #self.dirX=-1
            #Game.c.itemconfigure(self.obj, image= self.l_sprite)
        #if x-self.width<0:
            #self.dirX=1 
            #Game.c.itemconfigure(self.obj, image= self.r_sprite)
        #if y+self.height>float(Game.c["height"]):
            #self.dirY=-1
        #if y-self.height<0:
            #self.dirY=1
            
        for key in Game.walls.keys():
            Game.wallBBOX = Game.c.bbox(key)
            wallX1 = Game.wallBBOX[0]
            wallY1 = Game.wallBBOX[1]
            wallX2 = Game.wallBBOX[2]
            wallY2 = Game.wallBBOX[3]
            
            #LEFT
            if abs(x - wallX2)<=5:
                if wallY1<= y-5 <= wallY2 or wallY1<=y+5 <=wallY2:
                    self.dirX = self.dirX*-1
            #RIGHT      
            if abs(x - wallX1)<=5:
                if wallY1<= y-5 <= wallY2 or wallY1<=y+5 <=wallY2:
                    self.dirX = self.dirX*-1
            #UP        
            if abs(y - wallY2)<=5:
                if wallX1<= x-5 <= wallX2 or wallX1<=x+5 <=wallX2:
                    self.dirY = self.dirY*-1
            #DOWN        
            if abs(y - wallY1)<=5:
                if wallX1<= x-5 <= wallX2 or wallX1<=x+5 <=wallX2:
                    self.dirY = self.dirY*-1
            
            
        #movement------------------------
        Game.c.move(self.obj,self.dirX*deltax,self.dirY*deltay)
        if self.dirX > 0:
            Game.c.itemconfigure(self.obj, image= self.r_sprite)
        elif self.dirX < 0:
            Game.c.itemconfigure(self.obj, image= self.l_sprite)
            
        
        if self.n%self.shotFreq == 0:
            self.popcorn = Projectile(Game,"popcorn",x,y,self.dirX,self.dirY/6)
            Game.items.append(self.popcorn)
        
        self.n+=1
        if self.n > 8000:
            self.n = 0
            
class Turret:
    def __init__(self,x,y,fireRate):
        self.obj = Game.c.create_rectangle(x-8, y-8, x+8, y+8,fill="red",tag = self)
        self.fireRate = fireRate
        self.n = 0
        
    def update(self):
        coords = Game.c.coords(self.obj)
        x = coords[0]
        y = coords[1]
        
        self.n += 1
        
        if self.n%self.fireRate == 0:
            shot = Projectile(Game, "popcorn",x+8,y-8,0,-1)
            Game.items.append(shot)
            Game.projs.append(shot)
            
        if self.n>8000:
            self.n = 0
            
class Projectile:
    def __init__(self,parent,projType,x,y,dirX,dirY):
        Projectile.parent = parent
        Game = self.parent
        self.dirX = dirX
        self.dirY = dirY
        self.deleted = False
        
        if projType == "popcorn":
            self.sprite = readImage("Images/popcorn.gif") #PhotoImage(file="Images/popcorn.gif") 
        elif projType == "orange":
            self.sprite = readImage("Images/orange.gif") #PhotoImage(file="Images/orange.gif") 
        else:
            self.sprite = readImage("Images/orange.gif") #PhotoImage(file="Images/orange.gif") 
            
        self.obj = Game.c.create_image(x,y,image = self.sprite,tag = projType)
        Game.projs.append(self.obj)
        
        self.n = 0
        
    def update(self): 
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
            if abs(projx - wallX2)<=6:
                if wallY1<= projy-10 <= wallY2 or wallY1<=projy+17 <=wallY2:
                    self.dirX = self.dirX*-.1
                    self.dirY = self.dirY*-1
                    break
            #RIGHT      
            if abs(projx - wallX1)<=10:
                if wallY1<= projy-4 <= wallY2 or wallY1<=projy+4 <=wallY2:
                    self.dirX = self.dirX*-.1
                    self.dirY = self.dirY*-1
                    break
            #UP        
            if abs(projy - wallY2)<=12:
                if wallX1<= projx-3 <= wallX2 or wallX1<=projx+3 <=wallX2:
                    self.dirY = self.dirY*-.1
                    self.dirX = self.dirX*.1
                    break
            #DOWN        
            if abs(projy - wallY1)<=20:
                if wallX1<= projx-3 <= wallX2 or wallX1<=projx+3 <=wallX2:
                    self.dirY = self.dirY*-.1
                    self.dirX = self.dirX*.1
                    break
        
        Game.c.move(self.obj,self.dirX*6,6*self.dirY)
        
        self.n +=1
        if self.n > 60:
            self.delete()
        
        
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
            self.obj =Game.c.create_rectangle(x, y, x1, y1, fill='blue', tag = tag)
            x+=stepx;y+=stepy;x1+=stepx;y1+=stepy

class Key():
    def __init__(self,x,y):
        
        self.sprite = readImage("Images/key.gif", 1)
        self.obj = Game.c.create_image(x,y,image=self.sprite, tag = "key") 
        self.keyBBOX = Game.c.bbox(self.obj)
    def pickup(self):
        Game.door.opn()
        Game.c.delete(self.obj)
        #MAKE THE GROUND MOVE:
        #Game.infobar.config(bg="blue")
        #k_sprite = readImage("Images/key.gif",1)
        #k_label = Label(Game.infobar, image = k_sprite,height=20,width=20)
        #k_label.grid(row = 1, column = 2)
    def drop(self):
        Game.player.key_pickup = False
        Game.key1 = Key(360,400)
        Game.door.close()
        
class Door():
    def __init__(self,x,y,tag):
        self.x = x
        self.y = y
        self.obj =Game.c.create_rectangle(x, y, x+25, y+75, fill='brown',tag = tag)
        
    def opn(self):
        Game.c.delete(self.obj)
        Game.walls["d1"] = Door(825,800,"d1")
        
    def close(self):
        Game.c.delete(self.obj)
        Game.walls["d1"] = Door(self.x, self.y,"d1")
        
class Bagpipe():
    def __init__(self,x,y):
        self.obj = Game.c.create_oval(x-10,y-10,y+10,y+10,fill="blue", tag = "bagpipe")
        
    def pickup(self):
        Game.player.fireRate = Game.player.fireRate/4
        Game.c.delete(self.obj)
    
class WinScreen():
    print("You win")
    #root.config(bg = 'blue', text = "YOU WIN!")
          
#setup window and start------------------------------        
root = Tk()
root.title("Scoty's Adventure")
root.config(bg = "grey", width = 800, height = 600)
root.resizable(width=FALSE, height=FALSE)
app = MainMenu(master=root)