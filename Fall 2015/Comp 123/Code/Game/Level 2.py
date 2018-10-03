from tkinter import *
import time
import math
from PIL import Image         # Note new import
import PIL.ImageTk as ImageTk    # Note new import


class MainMenu:
    def __init__(self,master):
        root = master
        for widget in root.winfo_children():
            widget.destroy()
        
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
        Game.paused = False
        Game.master = master
        Game.nextLevel = False
        
        #setup canvas-------------------------
        for widget in root.winfo_children():
            widget.destroy()
            
        Game.canvas_width = 800;  Game.canvas_height = 600
        
        Game.c = Canvas(width=Game.canvas_width, height=Game.canvas_height, bg = "orange")
        
        Game.c.grid(row = 1, column=0)
        
        #setup---------------------------------
        Game.items = []
        #Items in the Game.items list all have an item.update() function that is called once every tick.
        
        #setup infobar-------------------------
        Game.infobar = Frame(root, bg ="grey", height = 30)
        Game.infobar.grid(row = 0, column=0)
        Game.h_sprite = readImage("Images/heart.jpg")
        h_label = Label(Game.infobar, image = Game.h_sprite)
        h_label.grid(row = 1, column = 1)
        pause_button = Button(Game.infobar, text="PAUSE", command=Game.pause)
        pause_button.grid(row = 1, column = 3)
        mainMenu_button=Button(Game.infobar, text="MAIN MENU", command=self.mainMenu)
        mainMenu_button.grid(row = 1, column = 4)
        quit_button = Button(Game.infobar, text="QUIT", command=Game.quit)
        quit_button.grid(row = 1, column = 5)        
          
        #setup enemies--------------------------
        enemy1 = Squirrel(self,x=600,y=200,speedX=1,speedY = 1, shotFreq = 100)
        enemy2 = Squirrel(self, 200,200,0,1,120)  
        
        Game.items.append(enemy1)
        Game.items.append(enemy2)
        
        turret1 = Turret(450,400, 200)
        Game.items.append(turret1)
        
        Game.projs = []
        
        Game.player = Player()
        Game.items.append(Game.player)
        
        #OTHER OBJS:--------------------------------------------
        Game.key1 = Key(360,400)
        Game.bp1 = Bagpipe(100,100)
        Game.ignored_tags = [('enemy',),('player',),('popcorn',),('orange',),('key',),('bagpipe',) ]
        
        #SETUP WALLS:--------------------------------------------------------
        
        #EDGE WALLS:---------------------------------------------------------
        Game.walls = { #build wall dictionary
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
        
        #SET UP TABLES 
        
        t_sprite = readImage("Images/Tables.gif")        
        table = Game.c.create_image(50, 100,image = t_sprite)        
        
        
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
        
        try: #handle when the user closes the window.
            while True:
                if not Game.nextLevel:
                    self.update_canvas()    
        except TclError:
            pass
            
    def update_canvas(self):
        if not Game.paused:
            Game.ticks +=1  
            time.sleep(.005)
            if len(Game.items)==0:
                return
            for i in range(len(Game.items)):
                Game.items[i].update() #call the update function of every item that is updated every tick
                
            root.update_idletasks() # redraw window
        root.update() # process user events
        
    def pause():
        if Game.paused:
            Game.paused = False
        else:
            Game.paused = True
                
    def mainMenu(self):
        MainMenu(self.master)
                 
    def quit():
        root.destroy()
        
class Game2:
    def __init__(self):
        Game.nextLevel = False
        Game.c.delete("all")
        Game.c.create_rectangle(100,100,120,120)
        Game.c.config(bg = "brown")
        Game.player = Player()
        Game.items.append(Game.player)
        
        Game.walls={      
            "w1": Wall(startx=0, starty=0, endx=800, endy=0,tag="w1"), #topwall
            "w2": Wall(775, 0,775,250,"w2"), #rightwalltop
            "w3": Wall(775,325,775,600,"w3"), #rightwallbottom
            "w4": Wall(0, 575,775,575,"w4"), #bottomwall
            "w5": Wall(0,25, 0,250,"w5"), #leftwalltop
            "w6": Wall(0,325, 0,575,"w6"), #leftwallbottom
            "wOut": Wall(-25,0,-25,575,"wOut"),  
            
            #DOOR:
            "d1": Door(775,250,"d1"),      
        }
        
       
class Player:
    """Setup the player class, creates the game object, placing it on the canvas. Handles player movement and collisions. 
    Allows the player to shoot projectiles and die."""
    def __init__(self):
        self.scot_r = readImage("Images/scot_r.gif",2) #PhotoImage(file='images/scot_r.gif')
        self.scot_l = readImage("Images/scot_l.gif",2) #PhotoImage(file="Images/scot_l.gif")
        self.deleted = False
        self.speed = 1.5
        
        self.dirs={}
        self.dirs["RIGHT"] = False
        self.dirs["LEFT"] = False
        self.dirs["UP"] = False
        self.dirs["DOWN"] = False
        
        self.cols = {}
        self.cols["RIGHT"] = False
        self.cols["LEFT"] = False
        self.cols["UP"] = False
        self.cols["DOWN"] = False
        
        self.ableToShoot = True
        self.fireRate = 100
        self.lastDir = 1
        self.mx = 1
        self.my= 1
        self.key_pickup = False
        
        self.lastTicks = Game.ticks
        
        self.hitbox = Game.c.create_rectangle(3,255,32,320,fill='',outline='')
        self.scot = Game.c.create_image(18,280,image=self.scot_r,tag = "player") 
        self.playerBox = Game.c.bbox(self.scot)
        self.playerCoords = Game.c.coords(self.scot)
            
    #BINDINGS---------------------------------   
        root.bind('<space>', self.shoot)
        root.bind_all('<Key>', self.keyPressed)
        root.bind_all('<KeyRelease>', self.keyReleased)        
        
    def keyPressed(self,event):
        if event.keysym == 'Right' or event.keysym == 'd':
            self.dirs["RIGHT"]  = True
        if event.keysym == 'Left' or event.keysym == 'a':
            self.dirs["LEFT"] = True
        if event.keysym == 'Up' or event.keysym == 'w':
            self.dirs["UP"] = True
        if event.keysym == 'Down' or event.keysym == 's':
            self.dirs["DOWN"] = True
    
    def keyReleased(self,event):
        if event.keysym == 'Right' or event.keysym == 'd':
            self.dirs["RIGHT"]  = False
        if event.keysym == 'Left' or event.keysym == 'a':
            self.dirs["LEFT"] = False
        if event.keysym == 'Up' or event.keysym == 'w':
            self.dirs["UP"] = False
        if event.keysym == 'Down' or event.keysym == 's':
            self.dirs["DOWN"] = False
        if event.keysym == 'p':
            Game.pause()
         

    #move----------------------------------
    def update(self):
        if self.deleted:
            return
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
            
    #COLLISION?-------------------------------------------------------
        #self.check_collision()

    #MOVE----------------------------------------------------------------------------------              
        if self.dirs["RIGHT"] and not(self.cols["RIGHT"]):
            Game.c.move(self.scot, self.speed, 0); Game.c.move(self.hitbox, self.speed, 0)

        if self.dirs["LEFT"] and not(self.cols["LEFT"]):
            Game.c.move(self.scot, -self.speed, 0); Game.c.move(self.hitbox, -self.speed, 0)
        if self.dirs["UP"] and not(self.cols["UP"]):
            Game.c.move(self.scot, 0, -self.speed); Game.c.move(self.hitbox, 0, -self.speed)
        if self.dirs["DOWN"] and not(self.cols["DOWN"]):
            Game.c.move(self.scot, 0, self.speed); Game.c.move(self.hitbox, 0, self.speed)
        
        for col in self.cols:
            self.cols[col] = False
            
        if playerx > 800:
            Game.nextLevel = True
            for item in Game.items:
                item.deleted = True
            Game2()
        
    def check_collision(self):
        if self.deleted:
            return        
        x = self.playerCoords[0]
        y = self.playerCoords[1]
        playerCoords = Game.c.bbox(self.hitbox)
        
        overlapping = Game.c.find_overlapping(playerCoords[0],playerCoords[1],playerCoords[2],playerCoords[3])[1:]
        
        r_overlapping = Game.c.find_overlapping(playerCoords[0]+10,playerCoords[1]+5,playerCoords[2],playerCoords[3]-5)[2:]
        l_overlapping = Game.c.find_overlapping(playerCoords[0],playerCoords[1]+5,playerCoords[2]-10,playerCoords[3]-5)[2:]
        u_overlapping = Game.c.find_overlapping(playerCoords[0]+6,playerCoords[1],playerCoords[2]-6,playerCoords[3]-10)[2:]
        d_overlapping = Game.c.find_overlapping(playerCoords[0]+6,playerCoords[1]+10,playerCoords[2]-6,playerCoords[3])[2:]
        
        for obj in overlapping:
            if obj == Game.key1.obj:
                Game.key1.pickup()
                return
            elif obj == Game.bp1.obj:
                Game.bp1.pickup()
                return
            elif obj in Game.projs:
                if Game.c.gettags(obj) != ('orange',):
                    self.die()
                    return
            elif Game.c.gettags(obj) == ():
                self.die()
                return
            elif Game.c.gettags(obj) == ('heart',):
                Heart.pickup()
                return
                             
        for obj in r_overlapping:
            if Game.c.gettags(obj) not in Game.ignored_tags:
                self.cols["RIGHT"] = True
        for obj in l_overlapping:
            if Game.c.gettags(obj) not in Game.ignored_tags:
                self.cols["LEFT"] = True
        for obj in u_overlapping:
            if Game.c.gettags(obj) not in Game.ignored_tags:
                self.cols["UP"] = True
        for obj in d_overlapping:
            if Game.c.gettags(obj) not in Game.ignored_tags:
                self.cols["DOWN"] = True
        
    #Shoot----------------------------------
    
    def shoot(self,event):
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
        Game(Game.master)
        
        
class Squirrel:
    def __init__(self,parent,x=0,y=0,speedX=0, speedY=2, shotFreq = 400):
        self.parent = parent
        Game = self.parent
        #setup Squirrel---------------------------
        self.r_sprite = readImage("Images/squirrel_r.gif", 2)
        self.l_sprite = readImage("Images/squirrel_l.gif", 2)
        
        self.obj = Game.c.create_image(x,y,image = self.l_sprite,tag = "enemy")
        
        self.width = self.r_sprite.width()
        self.height = self.r_sprite.height()
        
       #state vars----------------------------------------------- 
        self.deleted = False
        self.n = 0 
        self.dirY = 1
        self.dirX = -1  
        self.shotFreq = shotFreq
        self.shotRange = 1000
        self.speedX = speedX
        self.speedY = speedY
        
        sBox = Game.c.bbox(self.obj)
        self.bufx = x - sBox[0]
        self.bufy = y-sBox[1]
        
    
    def update(self):
        if self.deleted:
            return
        Game = self.parent
        #vars---------------------
        deltay=self.speedY
        deltax=self.speedX
        
        coords = Game.c.coords(self.obj)
        x = coords[0]
        y = coords[1]
        self.x = x
        self.y = y
        
        #check if hit----------------------------------------------------------
        sbox = Game.c.bbox(self.obj)
        overlapping = Game.c.find_overlapping(sbox[0],sbox[1],sbox[2],sbox[3]) 
        overlapping = overlapping[1:]
        
        for obj in overlapping:
            if obj in Game.projs:
                if Game.c.gettags(obj) != ('popcorn',):
                    self.die()
        
   #MOVEMENT------------------------
        self.check_collision() #Checks if the player is colliding on any side, if they are, restricts movement in that direction.
        Game.c.move(self.obj,self.dirX*deltax,self.dirY*deltay)
        if self.dirX > 0:
            Game.c.itemconfigure(self.obj, image= self.r_sprite)
        elif self.dirX < 0:
            Game.c.itemconfigure(self.obj, image= self.l_sprite)
        
        if Game.ticks%self.shotFreq == 0:
            self.popcorn = Projectile(Game,"popcorn",x,y,self.dirX,self.dirY/6)
            Game.items.append(self.popcorn)
        
    def check_collision(self):
        if self.deleted:
            return
        
        sbox = Game.c.bbox(self.obj)
        r_overlapping = Game.c.find_overlapping(sbox[0]+10,sbox[1]+5,sbox[2],sbox[3]-5)[1:]
        l_overlapping = Game.c.find_overlapping(sbox[0],sbox[1]+5,sbox[2]-10,sbox[3]-5)[1:]
        u_overlapping = Game.c.find_overlapping(sbox[0]+6,sbox[1],sbox[2]-6,sbox[3]-10)[1:]
        d_overlapping = Game.c.find_overlapping(sbox[0]+6,sbox[1]+10,sbox[2]-6,sbox[3])[1:]

        for obj in r_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirX = -1
        for obj in l_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirX = 1
        for obj in u_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirY = 1   
        for obj in d_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirY = -1
                    
    def die(self): 
        """Called when the enemy collides with an object that kills them. Destroys the enemy object and prevents the Squirrel.update() function from moving the dead enemy"""

        self.deleted = True        
        Game.c.delete(self.obj)        
        heart = Heart(self.x,self.y)
            
class Turret:
    def __init__(self,x,y,fireRate):
        self.obj = Game.c.create_rectangle(x-8, y-8, x+8, y+8,fill="red",tag = "enemy")
        self.fireRate = fireRate
        self.deleted = False
        
    def update(self):
        if self.deleted:
            return
        coords = Game.c.coords(self.obj)
        x = coords[0]
        y = coords[1]
                
        if Game.ticks%self.fireRate == 0:
            shot = Projectile(Game, "popcorn",x+8,y-10,0,-1.1)
            Game.items.append(shot)
            Game.projs.append(shot)
            
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
            
        self.orange_l = readImage("Images/orange_l.gif")
        self.obj = Game.c.create_image(x,y,image = self.sprite,tag = projType)
        Game.projs.append(self.obj)
        
        self.n = 0
        
    def update(self): 
        Game = Projectile.parent
        if self.deleted:
            return
        projx = Game.c.coords(self.obj)[0]
        projy = Game.c.coords(self.obj)[1]
        
        if Game.c.gettags(self.obj) == ('orange',):
            if self.dirX < 0:
                Game.c.itemconfigure(self.obj, image= self.orange_l)
            elif self.dirX > 0:
                Game.c.itemconfigure(self.obj, image= self.sprite)
            
        pbox = Game.c.bbox(self.obj)
        
        if Game.c.gettags(self.obj) == ('orange',):
            r_overlapping = Game.c.find_overlapping(pbox[0]+30,pbox[1]+10,pbox[2],pbox[3]-10)[1:]
            l_overlapping = Game.c.find_overlapping(pbox[0],pbox[1]+10,pbox[2]-30,pbox[3]-10)[1:]
            u_overlapping = Game.c.find_overlapping(pbox[0]+3,pbox[1],pbox[2]-3,pbox[3]-3)[1:]
            d_overlapping = Game.c.find_overlapping(pbox[0]+3,pbox[1]+3,pbox[2]-3,pbox[3])[1:]
        
        else:
            r_overlapping = Game.c.find_overlapping(pbox[0]+8,pbox[1]-5,pbox[2],pbox[3]+5)[1:]
            l_overlapping = Game.c.find_overlapping(pbox[0],pbox[1]-5,pbox[2]-8,pbox[3]+5)[1:]
            u_overlapping = Game.c.find_overlapping(pbox[0]-3,pbox[1],pbox[2]+3,pbox[3]-10)[1:]
            d_overlapping = Game.c.find_overlapping(pbox[0]-3,pbox[1]+10,pbox[2]+3,pbox[3])[1:]
            
        
        
        for obj in r_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirX = -.1
        for obj in l_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirX = .1
        for obj in u_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirY = .1   
        for obj in d_overlapping:
            if not Game.c.gettags(obj) in Game.ignored_tags:
                self.dirY = -.1        
     
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

class Heart:
    def __init__(self,x,y):
        self.obj = Game.c.create_image(x,y,image=Game.h_sprite, tag="heart")
        self.keyBBOX = Game.c.bbox(self.obj)
    
    def pickup(self):
        Game.c.delete(self.obj)  
        
class WinScreen():
    def __init__(self):
        print("You win")
    #root.config(bg = 'blue', text = "YOU WIN!")
          
#setup window and start------------------------------        
root = Tk()
root.title("Scoty's Adventure")
root.config(bg = "grey", width = 800, height = 600)
root.resizable(width=FALSE, height=FALSE)
app = MainMenu(master=root)