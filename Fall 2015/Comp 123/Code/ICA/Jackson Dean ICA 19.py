from tkinter import *

class Main:
    def __init__(self,master):
        
        self.master = master
        
        self.master.title("Button and Label GUI")
     
        
        self.quitButton = Button(text="QUIT", command = self.quit); self.quitButton.grid(row=0, column = 2)
        self.helloButton = Button(text = "HELLO", command = self.hello); self.helloButton.grid(row = 0, column = 0)
        self.goodbyeButton = Button(text = "GOODBYE", command = self.goodbye); self.goodbyeButton.grid(row=0,column=1)
        self.label = Label(text="Welcome"); self.label.grid(row=0,column=3)
        
        
        self.master.mainloop()
        
    def quit(self):
        self.master.destroy()
    def hello(self):
        self.label['text'] = "Hello"
    def goodbye(self):
        self.label['text'] = "Goodbye"
        
        
class Reverse:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(text="reversed text:"); self.label1.pack()
        self.label2 = Label(text=""); self.label2.pack()
        self.entry = Entry();self.entry.pack()
        self.revButton = Button(text="REVERSE", command = self.entryResponse); self.revButton.pack()
        
        self.quitButton = Button(text="QUIT", command = self.quit); self.quitButton.pack()
        
        
        master.bind('<Return>', self.entryResponse)
        master.bind('<Tab>', self.entryResponse)
        
        master.mainloop()
        
    def entryResponse(self,event=None):
        text = self.entry.get()
        revText = text[::-1].lower()
        self.label2['text'] = revText
        
    def quit(self):
        self.master.destroy()
    
        
root = Tk()        
app = Main(root)

root2 = Tk()
app2 = Reverse(root2)