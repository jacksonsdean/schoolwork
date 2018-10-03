""" =====================================================
Exam 5 Code file
Jackson!
=========================================================
"""


import random
from tkinter import *

# -------------------------------------------------------
# Question 1: The knock knock joke GUI

# Global variables
mainWin = None
joker = None
victim = None
count = 1


def knockKnockGui():
    """Sets up and runs the GUI for the knock knock joke game."""
    global mainWin
    global joker
    global victim
    global count
    mainWin = Tk()
    
    count = 1
    
    joker = Label(text = "Knock Knock");joker.grid(row=0,column = 1)

    victim = Button(text = "Who's there?", command =victimResponse); victim.grid(row=2,column=1)
    
    mainWin.mainloop()
    
def victimResponse():
    """A callback function for the joke victim's button, it checks what the
    button currently says and updates the label and button to the correct
    next step in the game. It also updates the count variable to keep track
    of how many times the cycle has repeated. At the end, it calls the
    destroy method to end the program."""
    global mainWin
    global joker
    global victim
    global count 
    
    if victim['text'] == "Who's there?":
        randVal = random.randint(1, 3)
        if count > 2 and randVal == 1:
            joker['text'] = 'Orange'
            victim['text'] = 'Orange who?'
        else:
            joker['text'] = "Banana"
            victim['text'] = "Banana who?"
            count = count + 1
    elif victim['text'] == 'Banana who?':
        joker['text'] = 'Knock Knock'
        victim['text'] = "Who's there?"
    elif victim['text'] == 'Orange who?':
        joker['text'] = "Orange you glad I didn't say banana?"
        victim['text'] = 'Groan'
    elif victim['text'] == 'Groan':
        mainWin.destroy()
        
        
    
# -------------------------------------------------------
# Question 2: Recursive Towers of Hanoi

    
def towers(startT, goalT, spareT, N):
    """Takes in descriptors for the three posts, and how many rings are being moved. 
    It assumes that there are N rings on the startT post, and it wans to move all
    N rings to the goalT post. It may use the spareT post to hold rings along the way.
    It prints the sequence of moves, in order, to solve the problem for any value of N."""
    if N == 1:
        print("Move ring from", startT, "to", goalT)
    else:
        towers(startT, spareT, goalT, N-1)
        print("Move ring from", startT, "to", goalT)        
        towers(spareT, goalT, startT, N-1)
 
 
if __name__ == '__main__':          
    # Run the GUI
    #knockKnockGui()             
    
    # Run towers program
    towers('A', 'C', 'B', 3)

