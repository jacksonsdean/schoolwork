
from tkinter import *

# -----------------------------------------------------
# Global variables:

rootWin = None  # root window object
canvas = None   # canvas object
ballList = []   # global list containing ball information


# -----------------------------------------------------

def GUIMain():
    """Takes in no inputs, it sets up the GUI elements for this progrma,
    and then runs the event listener loop."""
    setupGUI()
    try:
        while True:
            moveBalls()                   # call local function to update ball positions
            rootWin.update_idletasks()   # redraw window
            rootWin.update()             # process user events
    except TclError:
        pass      # to avoid errors when the window is closed
    

def setupGUI():
    """Takes in no inputs and sets up the GUI elements for this program"""
    global rootWin   
    global canvas
    global ballList
    
    rootWin = Tk()
    rootWin.title("First Canvas example")
        
    # Create a canvas that is 500 by 500 pixels, with a yellow background
    canvas = Canvas(rootWin, bg="yellow", width = 500, height = 500, bd = 0)
    canvas.config(scrollregion = canvas.bbox(ALL))
    canvas.grid(row = 1, column = 1)
        
    # Make global variable called ballList, to hold information about
    # the balls being displayed.  Each entry in the list holds the ball's 
    # id number (assigned by the canvas widget when the ball is created) 
    # and how to move the ball

    ballList = []
    # Create the first, red, ball
    nextBall = canvas.create_oval(20, 40, 40, 60,
                                  fill = "red", outline = "black")
    ballList.append([nextBall, .5, .5])     # slow moving diagonally
    # Create the second, blue, ball
    nextBall = canvas.create_oval(70, 70, 90, 90,
                                  fill = "blue", outline = "black")
    ballList.append([nextBall, 1.8, .9])    # moves twice as far in x dim
    # Create the third, green, ball   
    nextBall = canvas.create_oval(100, 10, 120, 30,
                                  fill = "green", outline = "black")
    ballList.append([nextBall, 2, 3])    # moves very fast
        
    



def moveBalls():
    """Takes no inputs, and moves the balls in the ball list.  It bounces
    back when it reaches the walls of the canvas"""
    for ballInfo in ballList:
        ball = ballInfo[0]
        (x0, y0, x1, y1) = canvas.coords(ball)
        if x1 >= 500 or x0 <= 5:
            ballInfo[1] = - ballInfo[1]
        if y1 >= 500 or y0 <= 5:
            ballInfo[2] = - ballInfo[2]
        xDist = ballInfo[1]
        yDist = ballInfo[2]
        canvas.move(ball, xDist, yDist)    



# --- here it goes...
GUIMain()