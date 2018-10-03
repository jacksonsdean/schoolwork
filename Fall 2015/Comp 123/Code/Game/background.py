from tkinter import *
from PIL import *

root = Tk()
c = Canvas(root,width=800,height=600)
im = PhotoImage(file="water.gif")
c.create_image(0,0,anchor=NW,image=im)
c.pack()

root.mainloop()