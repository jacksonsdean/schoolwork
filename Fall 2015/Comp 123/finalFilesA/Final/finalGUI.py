"""
============================================================================
finalGUI.py

This file will contain your answers for the GUI question, Question 5
============================================================================
"""


from tkinter import *

# ---------------------------------------
# Global Variables

mainWin = None
redDisplay = None  # Label widget to display red channel value
greenDisplay = None  # Label widget to display green channel value
blueDisplay = None  # Label widget to display blue channel value

# The current RGB values (initially bright red):
redVal = 255    
greenVal = 0
blueVal = 0


# ---------------------------------------
# GUI functions

   

def colorPickGUI():
    """creates the main window for the gui and adds all of the displays and buttons"""
    global mainWin
    global redVal
    global greenVal
    global blueVal
    global redDisplay
    global greenDisplay
    global blueDisplay
    
    
    mainWin = Tk()
    mainWin.title("Color Display")
    setBackground(redVal, greenVal, blueVal)


    upRed = Button(mainWin, text = "Increase Red", command = incrRed); upRed.grid(row = 0, column = 0, padx = 10, pady = 10)
   
    downRed = Button(mainWin, text = "Decrease Red", command = decrRed); downRed.grid(row = 2, column = 0, padx = 10, pady = 10)
    
    redDisplay = Label(mainWin, text = str(redVal))
    redDisplay.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    greenDisplay = Label(mainWin, text = str(greenVal)); greenDisplay.grid(row = 1, column = 1, padx = 10, pady = 10)    
      
    upGreen = Button(mainWin, text = "Increase Green", command = incrGreen); upGreen.grid(row = 0, column = 1, padx = 10, pady = 10)    
    
    downGreen = Button(mainWin, text = "Decrease Green", command = decrGreen); downGreen.grid(row = 2, column = 1, padx = 10, pady = 10)    
    
    blueDisplay = Label(mainWin, text = str(blueVal)); blueDisplay.grid(row = 1, column = 2, padx = 10, pady = 10)  
    
    upBlue = Button(mainWin, text = "Increase Blue", command = incrBlue); upBlue.grid(row = 0, column = 2, padx = 10, pady = 10)
    
    downBlue = Button(mainWin, text = "Decrease Blue", command = decrBlue); downBlue.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    # add the remaining buttons and labels here. See my global variables for help.
    
    
    # line below should be last line in colorPickGUI
    mainWin.mainloop()


def incrRed():
    """Callback function for the Increase Red button. It increases the red value
    by 5, making sure it doesn't go over 255. It then updates the redDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global redVal
    global redDisplay
    redVal = redVal + 5
    if redVal > 255:
        redVal = 255
    redDisplay['text'] = str(redVal)
    setBackground(redVal, greenVal, blueVal)

def decrRed():
    """Callback function for the Decrease Red button. It decreases the red value
    by 5, making sure it doesn't go under 0. It then updates the redDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global redVal
    global redDisplay
    redVal = redVal - 5
    if redVal < 0:
        redVal = 0
    redDisplay['text'] = str(redVal)
    setBackground(redVal, greenVal, blueVal)
    
def incrGreen():
    """Callback function for the Increase Green button. It increases the green value
    by 5, making sure it doesn't go over 255. It then updates the greenDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global greenVal
    global greenDisplay
    greenVal = greenVal + 5
    if greenVal > 255:
        greenVal = 255
    greenDisplay['text'] = str(greenVal)
    setBackground(redVal, greenVal, blueVal)

def decrGreen():
    """Callback function for the Decrease Green button. It decreases the green value
    by 5, making sure it doesn't go under 0. It then updates the greenDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global greenVal
    global greenDisplay
    greenVal = greenVal - 5
    if greenVal < 0:
        greenVal = 0
    greenDisplay['text'] = str(greenVal)
    setBackground(redVal, greenVal, blueVal)

def incrBlue():
    """Callback function for the Increase Blue button. It increases the blue value
    by 5, making sure it doesn't go over 255. It then updates the blueDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global blueVal
    global blueDisplay
    blueVal = blueVal + 5
    if blueVal > 255:
        blueVal = 255
    blueDisplay['text'] = str(blueVal)
    setBackground(redVal, greenVal, blueVal)
    
    
def decrBlue():
    """Callback function for the Decrease Blue button. It decreases the blue value
    by 5, making sure it doesn't go under 0. It then updates the blueDisplay label
    to show the new value, and updates the main window's background color."""
    global mainWin
    global blueVal
    global blueDisplay
    blueVal = blueVal - 5
    if blueVal < 0:
        blueVal = 0
    blueDisplay['text'] = str(blueVal)
    setBackground(redVal, greenVal, blueVal)


def setBackground(r, g, b):
    """Sets the main window's background to the input RGB color value."""
    global mainWin
    mainWin.config(bg= makeTkColor( (r, g, b) ))
    

def makeTkColor(colorTuple):
    """Takes in a tuple containing red, green, and blue channel values, and
    makes a color string that tkinter can interpret correctly."""
    return "#%02x%02x%02x" % colorTuple




# ---------------------------------------
# Main script


colorPickGUI()





