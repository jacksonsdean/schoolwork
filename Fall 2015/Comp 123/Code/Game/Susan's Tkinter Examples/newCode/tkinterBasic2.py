
from tkinter import *

# -----------------------------------------------------
# Global variables:

_rootWin = None

# -----------------------------------------------------

def GUIMain():
    """The main program first sets up the GUI elements, and then runs
    the event listener loop for the main window."""
    setupGUI()
    _rootWin.mainloop()
    
    
def setupGUI():
    """Takes in no inputs and sets up the GUI elements for this program"""
    global _rootWin

    _rootWin = Tk()
    _rootWin.title("Second example")
        
    # Create a title label.
    titleLabel = Label(_rootWin, text = "Welcome to my program!",
                       font = "Arial 20 bold", relief = GROOVE,
                       justify = CENTER)
    titleLabel.grid(row = 0, column = 0, columnspan = 3)
        
    # Create a Button object for a quit button
    quitButton = Button(_rootWin, text = "Quit",
                        font = "Arial 16", command = quit)
    quitButton.grid(row = 1, column = 1)
        
    # Create a frame to hold a set of labels.  
    labelFrame = Frame(_rootWin, bg="LightBlue", borderwidth=3, 
                       relief = GROOVE, padx=10, pady=10)
    labelFrame.grid(row = 2, columnspan = 3)
        
    # These 9 labels belong to the labelFrame.  
    label00 = Label(labelFrame, text = "A", font = "Arial 14", padx=5, pady=5)
    label01 = Label(labelFrame, text = "B", font = "Arial 14", padx=5, pady=5)
    label02 = Label(labelFrame, text = "C", font = "Arial 14", padx=5, pady=5)
    label10 = Label(labelFrame, text = "D", font = "Arial 14", padx=5, pady=5)
    label11 = Label(labelFrame, text = "E", font = "Arial 14", padx=5, pady=5)
    label12 = Label(labelFrame, text = "F", font = "Arial 14", padx=5, pady=5)
    label20 = Label(labelFrame, text = "G", font = "Arial 14", padx=5, pady=5)
    label21 = Label(labelFrame, text = "H", font = "Arial 14", padx=5, pady=5)
    label22 = Label(labelFrame, text = "I", font = "Arial 14", padx=5, pady=5)
    label00.grid(row = 0, column = 0)
    label01.grid(row = 0, column = 1)
    label02.grid(row = 0, column = 2)
    label10.grid(row = 1, column = 0)
    label11.grid(row = 1, column = 1)
    label12.grid(row = 1, column = 2)
    label20.grid(row = 2, column = 0)
    label21.grid(row = 2, column = 1)
    label22.grid(row = 2, column = 2)
        
        

# This is a "callback" method attached to the quit button.  It destroys
# the main window, which thus ends the program
def quit():
    _rootWin.destroy()


# --- here it goes...

GUIMain()