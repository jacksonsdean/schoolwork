
from tkinter import *
import random

# -----------------------------------------------------
# Global variables:

_rootWin = None
_canvas = None
_ball = None
# -----------------------------------------------------



def GUIMain():
    setupGUI()
    moveBall()
    _rootWin.mainloop()
        
    
    
def setupGUI():
    """Takes in no inputs and sets up the GUI elements for this program"""
    global _rootWin
    global _canvas
    global _ball
    
    _rootWin = Tk()
    _rootWin.title("Third Canvas example: timing")
    
    # Create a canvas object that is 500 by 500 pixels wide, with a yellow background
    _canvas = Canvas(_rootWin, bg="yellow",width = 500, height = 500, bd = 0)
    _canvas.grid(row = 1, column = 1)
    # Show all of the canvas
    _canvas.config(scrollregion= _canvas.bbox(ALL))


    # Create a global variable to hold the ball's id
    _ball = _canvas.create_oval(250, 250, 260, 260, fill = 'blue')
                
        

def moveBall():
    """Takes no inputs, and moves the ball in the ball list.  It bounces
    back when it reaches the walls of the canvas"""
    _canvas.move(_ball, 10, 0)    
    _rootWin.after(2000, moveBall)
                


# --- here it goes...
GUIMain()
