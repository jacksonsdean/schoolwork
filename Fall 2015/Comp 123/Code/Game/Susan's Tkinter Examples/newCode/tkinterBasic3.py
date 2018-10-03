
from tkinter import *

# -----------------------------------------------------
# Global variables:

rootWin = None
frame = None
userInputEntry = None
turtlePic = None
imgLabel = None


# -----------------------------------------------------

def GUIMain():
    """Takes in no inputs, it sets up the GUI elements for this progrma,
    and then runs the event listener loop."""
    setupGUI()
    rootWin.mainloop()
    

def setupGUI():
    """Takes in no inputs and sets up the GUI elements for this program"""
    global rootWin   
    global frame
    global userInputEntry
    global turtlePic
    global imgLabel
        
    rootWin = Tk()
    rootWin.title("Entry example")
    
    turtlePic = PhotoImage(file = "greenTurtle.gif")
    imgLabel = Label(rootWin, image = turtlePic)
    imgLabel.grid(row = 0, column = 0)
        
    # Create a frame to hold the label and entry
    frame = Frame(rootWin, padx=10, pady=10)
    frame.grid(row = 1, column = 0)   
        
    # Create a label to ask the question
    instrLabel = Label(frame, text="Do you like green eggs and ham?",
                       relief=RAISED,
                       padx=5, pady=5)
    instrLabel.grid(row=0,column=0)
        
    # Make an entry for the user to type in
    userInputEntry = Entry(frame, width=10, relief=RAISED)
    userInputEntry.grid(row=0, column = 3)
        
    # When the user hits return or tab while in the entry box, this callback
    # will be triggered.
    userInputEntry.bind("<Return>", respond)
    userInputEntry.bind("<Tab>", respond)
        


def respond(event):
    """Takes an event object as input, and is the callback for the user's input
    box.  It reads the text in the box through the StringVar, and changes 
    the color of the frame to green or blue depending on the text"""
    userText = userInputEntry.get()  # get text from Entry widget
    userInputEntry.delete(0,END)     # clear text in Entry widget
    if 'yes' in userText.lower(): 
        frame['bg'] = 'Green'
    else:
        frame['bg'] = 'Blue'
        

# --- here it goes...
GUIMain()