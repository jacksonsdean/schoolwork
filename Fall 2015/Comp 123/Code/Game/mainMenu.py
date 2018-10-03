from tkinter import *
import sys
class mainMenu:
    def __init__(self,master):
        root = master
        frame = Frame(root, width = 800, height = 600, bg = "light blue", padx = 0, pady = 0)
        
        adventure_img = PhotoImage(file="Images/scotty_adv.png")
        adventure_img = adventure_img.zoom(3)
        
        adventure_title = Label(frame, image = adventure_img)
        
        new_game_button = Button(frame, text = "New Game",
                                font = "Arial 40 bold",
                                bg = "lightgrey",
                                bd = 5,
                                relief = GROOVE,
                                activebackground = "orange",
                                width = 12,
                                command = self.clickNewGame
                                )
        
        instructions_button = Button(frame, text = "Instructions",
                                    font = "Arial 40 bold",
                                    bg = "lightgrey",
                                    bd = 5,
                                    relief = GROOVE,                                    
                                    activebackground = "orange",
                                    width = 12,
                                    command = self.clickInstructions
                                    )
        
        credits_button = Button(frame, text = "Credits",
                                font = "Arial 40 bold",
                                bg = "lightgrey",
                                bd = 5,
                                relief = GROOVE,
                                activebackground = "orange",
                                width = 12,                                
                                command = self.clickCredits
                                ) 
        
        quit_button= Button(frame, text = "Quit",
                               font = "Arial 40 bold",
                               bg = "lightgrey",
                               bd = 5,
                               relief = GROOVE,
                               activebackground = "orange",
                               width = 12,                               
                               command = self.clickQuit
                               )
           
           
        adventure_title.grid(row = 0, column = 1)
        
        new_game_button.grid(row = 1, column = 1)
        instructions_button.grid(row = 2, column = 1)
        credits_button.grid(row = 3, column = 1)
        quit_button.grid(row = 4, column = 1)
        frame.pack()
        
        root.mainloop()
    
    

  
    
    def clickNewGame(self):
        game(master=root)
        
    def clickInstructions(self):
        print("instructions")
        
    def clickCredits(self):
        print("credits")
        
    def clickQuit(self):
        print("quit")
        root.destroy()
        
    
class game:
    def __init__(self,master):
        print("game")
        
        
        
        
root=Tk()
mainMenu(master=root)


   