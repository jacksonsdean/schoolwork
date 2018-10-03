from tkinter import*


class Obstacle(object):
    #make very general so many obstacles can have dif attributes
    #e.g. 1. cant move thru. 2. Causes damage. 3. spawns door or enemy etc
    
    """An obstacle for the player. Obstacles have the
    following properties:

    Attributes:
        noPass: Can the player pass through this obstacle?
        Dmg: If the player touches the obstacle, does it cause damage?
        spawn: If the player touches the obstacle, does it spawn an enemy?
    """    
    
    #True or False could turn the attribute on or off. Like: (spikes, noPass=True, Dmg=True, spawn=False) (wall, noPass=True, Dmg=False, spawn=False)
    
    def __init__(self, noPass, Dmg, spawn):
        
        self.root = Tk()
        self.canvas = Canvas(self.rootWin, width =800, height = 600,)        
        
    
    #def noPass
        
    #def Dmg
        
    
    def wall():
        self.canvas.create_oval(oval_x1,oval_y1,oval_x2,oval_y2, outline = "white", width = 5, fill = "lightblue")
        
        
def wall(pos):
    #grid? 
    #rectangle
    c.

    
#setup window and start------------------------------        
root = Tk()
root.title("Scoty's Adventure")
root.config(bg = "grey", width = 800, height = 600)
root.resizable(width=FALSE, height=FALSE)
