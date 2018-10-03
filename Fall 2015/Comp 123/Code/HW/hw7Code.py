

import random
from tkinter import *




def runGuis():
    """This function runs the two GUIs that are in this file. It is called at\
    the very end of the file. You can comment or uncomment each call as you 
    wish."""
    #randomColorGUI() 
    ballGameGo()
    
    
# ==================================================================
# Question 1

# ---------------------------------------
# Global Variables
mainWindow = None

# ---------------------------------------
# GUI functions

def randomColorGUI():
    """calls the setup function and runs the main loop"""
    global mainWindow
    setupRandomColorGUI()
    mainWindow.mainloop()
      
def setupRandomColorGUI():
    """configures the window and sets up buttons and widgets for random colors"""
    global mainWindow
    mainWindow.config(bg="lightgreen")
    mainWindow.title("Random Color GUI")
    mainWindow.minsize(100,100)
    
    titleLabel = Label(text = "Random Colors", font = 30,relief = RIDGE ); titleLabel.grid(row = 0)
    quitButton = Button(text = "Quit", command = quit1); quitButton.grid(row = 2)
    cColorButton = Button(text = "Change Color", command = changeColor); cColorButton.grid(row = 1)

    
    
    
    

def quit1():
    """quits"""
    global mainWindow
    mainWindow.destroy()
    
def changeColor():
    """chanegs the color"""
    mainWindow.config(bg = makeRandomColor())
        

def makeRandomColor():
    """Generates random red, green, and blue channel values, and then makes
    a color string suitable for tkinter to interpret."""
    redVal = random.randrange(256)
    greenVal = random.randrange(256)
    blueVal = random.randrange(256)
    return makeTkColor( (redVal, greenVal, blueVal))

    

def makeTkColor(colorTuple):
    """Takes in a tuple containing red, green, and blue channel values, and
    makes a color string that tkinter can interpret correctly."""
    return "#%02x%02x%02x" % colorTuple
mainWindow = Tk()

randomColorGUI()


# ==================================================================
# Question 2

# ---------------------------------------
# Global Variables

# Widget variables
mainWindow = None
ballField = None


# Reference to the ball in the Canvas
ballObj = None

# Globals that hold the values that control the ball's movement
moveDir = [1, 0]
speedMult = 1
moveCount = 0
numCollisions = 0

# Global for the background color, updated when collisions occur
origBackColor = (135, 206, 250)
backColor = origBackColor

#labels:
speedLabel = None
colLabel = None

# ---------------------------------------
# GUI functions


def ballGameGo():
    """Main function, calls the setup helper that creates all the GUI elements,
    and then calls the ballMoveMainLoop to set the event-driven part going."""
    setupMoverGUI()
    ballMoveMainLoop()
    
    
    
def setupMoverGUI():
    """Takes no inputs, and sets up widgets for ball game. Creates main\
    window, title label, instructions label, and a frame where will will
    place labels to show the number of collisions with the walls, and the
    reset button."""
    
    global mainWindow
    global ballField
    global backColor
    global ballObj
    global colLabel
    global speedLabel
    
    mainWindow = Tk()
    mainWindow.title("Ball Mover Game")
        
                
    # set up title label
    titleLabel = Label(mainWindow, text = "Ball Mover Game",
                       font = "Courier 20 bold", relief = RAISED,
                       justify = CENTER, bd = 5)
    titleLabel.grid(row = 1, column = 1, padx = 15, pady = 15)
        
    # set up instructions label
    instructions = """Change the ball's direction: 
    q  w  e
     \\ | / 
     a---d
     / | \\
    z  x  c
     Don't let it hit the walls!"""
    
    instrLabel = Label(mainWindow, text = instructions, 
                       font = "Courier 14", relief = RAISED,
                       justify = CENTER, bd=2, padx = 5, pady = 5)
    instrLabel.grid(row = 2, rowspan=2, column = 1, padx=10, pady=10)

    # set up collisions frame
    collisFrame= Frame(mainWindow, bd=2, relief=RAISED, padx=5, pady=5)
    collisFrame.grid(row=2, column= 2, padx=20, pady=10)

    # here add contents of collisFrame: four labels and a button (two of
    # labels must be global)
    
    colTextLabel = Label(collisFrame, text = "Collisions", font = ("Courier", 16, "bold")); colTextLabel.grid(row = 0,column = 0)
    
    colLabel = Label(collisFrame, text = "0", font = ("Courier", 16, "bold")); colLabel.grid(row = 1,column = 0)
    
    speedTextLabel = Label(collisFrame, text = "Speed", font = ("Courier", 16, "bold")); speedTextLabel.grid(row = 0,column = 1)
    
    speedLabel = Label(collisFrame, text = "1", font = ("Courier", 16, "bold")); speedLabel.grid(row = 1,column = 1)
    
    resetButton = Button(collisFrame,command = resetGame, text = "Reset Game", font = ("Courier", 16, "bold")); resetButton.grid(row = 3,column = 0,columnspan = 2)
    
    
    

    # set up quit button
    quitButton = Button(mainWindow, text = "Quit",
                       font = "Courier 16", command = quit)
    quitButton.grid(row = 1, column = 2, padx = 10, pady = 10)                 

    # set up ball field canvas
    ballField = Canvas(mainWindow, bd = 2, relief=RAISED,
                       width=500, height = 500)
    ballField.config(bg = makeTkColor(backColor))
    ballField.grid(row = 4, column = 1, columnspan=3, padx = 10)
    ballField.config(scrollregion=ballField.bbox(ALL))

    # place the ball in the middle of the field
    ballObj = ballField.create_oval((250, 250), (270, 270), fill="red")

    # bind the main window to respond to the nine keys for ball movement
    for c in 'qweasdzxcQWEASDZC':
        mainWindow.bind(c, changeDirection)
                                                
        

   

def ballMoveMainLoop():
    """Takes the place of the built-in mainloop method. This performs
    the same tasks as mainloop, but it includes a call to moveBall, which updates
    the position of the ball in the field. That allows for the ball to move
    without the user doing anything."""
    global mainWindow
    try:
        while True:
            moveBall()               # my function to animate the ball
            mainWindow.update_idletasks() # redraw
            mainWindow.update() # process events
    except TclError:
        pass # to avoid errors when the window is closed



def moveBall():
    """Updates the ball's position. It must calculate how far the ball is to
    move, and then check if the movement would cause a collision with a wall. 
    If it does, then the ball doesn't move in that direction. 
    If no collision occurs, then the ball is moved.
    If a collision occurs, then the collision count must be updated, as must
    the label that displays the collision count. It also darkens the color of
    the background.
    This function also increments the move counter. If it reaches 200, then
    the speed is increased, and the new speed must be displayed."""
    global ballField
    global backColor
    global ballObj
    global moveDir
    global speedMult
    global moveCount
    global numCollisions
    global speedLabel
    global colLabel
    
    # Determine how far the ball should move in the x and y directions
    [ulx, uly, lrx, lry] = ballField.coords(ballObj)
    xDist = speedMult * moveDir[0]/10
    yDist = speedMult * moveDir[1]/10
    
    # Check to see if the ball will collide with a wall. If so, then
    # change its direction of movement and set the collided flag to true,
    # and don't move in that direction
    collided = False
    if (lrx + xDist >= 500) or (ulx + xDist < 5):
        moveDir[0] = -moveDir[0]
        collided = True
        xDist = 0
    if (lry + yDist >= 500) or (uly + yDist < 5):
        moveDir[1] = -moveDir[1]
        collided = True
        yDist = 0
    
    # if the ball hit a wall, then add one to the number of collisions
    if collided:
        numCollisions = numCollisions + 1
        colLabel.config(text = str(numCollisions))
        backColor = darkenColor(backColor)
        ballField.config(bg = makeTkColor(backColor))
    
    # Move the ball
    ballField.move(ballObj, xDist, yDist)
    
    # Add one to the count of moves. If the count passes 200
    # then increase the speed multiplier by one and reset the
    # count of moves to zero
    moveCount = moveCount + 1
    if moveCount >= 20000:
        speedMult = speedMult + 1
        speedLabel.config(text = str(speedMult))
        moveCount = 0


        
                
def quit():
    """A callback function for the Quit button. 
    Stops the program and closes the main window"""
    global mainWindow
    
    mainWindow.destroy()


        
def resetGame():
    """A callback function for the Reset Game button.
    Sets the speed multiplier back to 1, and the counter back to zero, and updates
    everything."""
    global numCollisions
    global speedMult 
    global speedLabel
    global colLabel
    global origBackColor
    global backColor
    
    numCollisions = 0
    speedMult = 1
    
    speedLabel.config(text = speedMult)
    colLabel.config(text = numCollisions)
    backColor = origBackColor  
    ballField.config(bg = makeTkColor(backColor))
    
    
    
    
def changeDirection(event):
    """Callback for key binding. Responds to each keystroke by changing direction of
    ball's movement, OR its color."""
    global ballObj
    global moveDir
    
    c = event.char.lower()
    
    if c == "q":
        moveDir = [-1,-1]
    elif c == "w":
        moveDir =[0,-1]
    elif c == "e":
        moveDir =[1,-1]        
    elif c == "a":
        moveDir =[-1,0]  
    elif c == "d":
        moveDir =[1,0] 
    elif c == "z":
        moveDir =[-1,1] 
    elif c == "x":
        moveDir =[0,1] 
    elif c == "c":
        moveDir =[1,1] 
        
    elif c == "s":
        ballField.itemconfig(ballObj, fill = (makeRandomColor()))
        
def darkenColor(colorTuple):
    """Given a tuple containing RGB values, this should decrease each channel
    value by 5, making sure it does not go below zero. It should return a
    new tuple containing the new values."""
    newColor = []
    for c in colorTuple:
        c += -5
        if c <=0:
            c = 0
        newColor.append(c)
    r = newColor[0] 
    g = newColor[1]
    b = newColor[2] 
    

    return (r, g, b)
        
    
# ==================================================================
# GUI script.. call to start programs


# Uncomment the following to run this program
runGuis()

