
from tkinter import *
import random

# -----------------------------------------------------
# Global variables:

rootWin = None
canvas = None
ballCollection = {}
selectedBall = None


# -----------------------------------------------------

def GUIMain():
    """Takes in no inputs, it sets up the GUI elements for this progrma,
    and then runs the event listener loop."""
    setupGUI()
    try:
        while True:
            moveBalls()  # call local function to update ball positions
            rootWin.update_idletasks() # redraw window
            rootWin.update() # process user events
    except TclError:
        pass # to avoid errors when the window is closed
    

def setupGUI():
    """Takes in no inputs and sets up the GUI elements for this program"""
    global rootWin   
    global canvas
    global ballCollection

    rootWin = Tk()
    rootWin.title("Second Canvas example")
        
        
    # Create a canvas object that is 500 by 500 pixels wide, with a yellow background
    canvas = Canvas(rootWin, bg="yellow",width = 500, height = 500, bd = 0)
    canvas.grid(row = 1, column = 1)
    # Show all of the canvas
    canvas.config(scrollregion = canvas.bbox(ALL))

    # Bind the canvas and main window to respond to mouse button and keyboard entry
    canvas.bind("<Button-1>", chooseBall)
    rootWin.bind("<Up>", userMoveBall)
    rootWin.bind("<Down>", userMoveBall)
    rootWin.bind("<Left>", userMoveBall)
    rootWin.bind("<Right>", userMoveBall)
        
    # Create an instance variable to hold which ball the user has selected
    selectedBall = None
        
    # Save info about the balls.  This randomizes the balls, and their speeds,
    # and uses a dictionary keyed by the ID from the canvas.  Each entry in the
    # dictionary is also a dictionary, with separate keys values for each feature
    ballCollection = {}
    for ballColor in ['red', 'green', 'blue', 'LightBlue', 'LightGreen']:
        nextDict = {}
        xStart = random.randint(20, 480)
        yStart = random.randint(20, 480)
        deltaX = random.randint(1, 2)
        deltaY = random.randint(1, 2)
        nextBall = canvas.create_oval(xStart,yStart, xStart+20, yStart+20,
                                      fill = ballColor, outline = "black")
        nextDict['xDist'] = deltaX
        nextDict['yDist'] = deltaY
        nextDict['moving'] = True
        ballCollection[nextBall] = nextDict
        
        

def moveBalls():
    """Takes no inputs, and moves the balls in the ball list.  It bounces
    back when it reaches the walls of the canvas"""
    for ballId in ballCollection:
        ballInfo = ballCollection[ballId]
        if ballInfo['moving']:
            (x0, y0, x1, y1) = canvas.coords(ballId)
            if x1 >= 500 or x0 <= 5:
                ballInfo['xDist'] = - ballInfo['xDist']
            if y1 >= 500 or y0 <= 5:
                ballInfo['yDist'] = - ballInfo['yDist']
            canvas.move(ballId, ballInfo['xDist'], ballInfo['yDist'])    
          
                 
# --------------------------------------------------------------------------
# Below here are the callback methods for the canvas to respond to mouse 
# and key inputs

def chooseBall(event):
    """Callback function, takes in an event object that describes the event
    that triggered the callback.  In this case, we use the event to find the
    location where the mouse was, and then we see if there is a ball near the spot.
    If so, then we make that the "selected ball" and put its movements under the
    control of the user.  If the user clicked on the ball that they had previously
    selected, this acts as a toggle and un-selects the ball, letting it resume
    free movement"""
    
    global selectedBall
    global ballCollection
    global canvas
    
    x = event.x
    y = event.y
    # find any canvas objects overlapping a 10x10 region around the mouse click
    ballSet = canvas.find_overlapping(x-5, y-5, x+5, y+5)
    
    if selectedBall != None:
        ballInfo = ballCollection[selectedBall]
        ballInfo['moving'] = True
        selectedBall = None
    elif len(ballSet) > 0:
        selectedBall = ballSet[0]
        ballInfo = ballCollection[selectedBall]
        ballInfo['moving'] = False
            



def userMoveBall(event):
    """A callback function assigned to keys the user might hit.  It does nothing if
    the user has not selected a ball by clicking on it.  If there is a selected
    ball, then it looks at which key was hit (responding to the arrow keys) to
    determine which direction to move the ball."""
    
    global selectedBall
    global canvas
    
    if selectedBall != None:
        userKey = event.char
        if event.keysym == 'Up':
            canvas.move(selectedBall, 0, -5)
        elif event.keysym == 'Down':
            canvas.move(selectedBall, 0, 5)
        elif event.keysym == 'Left':
            canvas.move(selectedBall, -5, 0)
        elif event.keysym == 'Right':
            canvas.move(selectedBall, 5, 0)
        



# --- here it goes...

GUIMain()
