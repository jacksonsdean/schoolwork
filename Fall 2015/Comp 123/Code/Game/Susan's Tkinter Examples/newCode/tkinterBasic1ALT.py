
from tkinter import *

# -----------------------------------------------------
# Global variables:

rootWin = None

# -----------------------------------------------------

def GUIMain():
    """Takes in no inputs, it sets up the GUI elements for this progrma,
    and then runs the event listener loop."""
    
    global rootWin
    
    # create the main GUI window
    rootWin = Tk()
    rootWin.title("First example")
    
    # create a label to hold a welcome message
    titleLabel = Label(rootWin)
    titleLabel['text'] = "Welcome to my program"
    titleLabel['font'] = "Arial 20 bold"
    titleLabel['relief'] = GROOVE
    titleLabel['justify'] = CENTER
    # place label inside window
    titleLabel.grid(row = 0, column = 0, columnspan = 3)
        
    # set up a button as a local variable (doesn't need to be accessed)
    quitButton = Button(rootWin)
    quitButton['text'] = "Quit"
    quitButton['font'] = "Arial 16"
    quitButton['command'] = quit
    quitButton.grid(row = 1, column = 1)

    # start the event listener loop going
    rootWin.mainloop()
    

def quit():
    """This is a callback method attached to the quit button.
    It destroys the main window, which ends the program"""
    rootWin.destroy()



# --------------------------------
# Below here is the script part, which creates the object and sets it running
GUIMain()