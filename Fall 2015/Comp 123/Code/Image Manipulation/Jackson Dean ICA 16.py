from imageTools import *
import math

def scaleDown(pic):
    
    w = math.ceil(getWidth(pic)/2)
    h = math.ceil(getHeight(pic)/2)

    newPic = makeEmptyPicture(w,h)    
    for x in range(w):
        for y in range(h):
            npx = getPixel(newPic,x,y)
            px = getPixel(pic,x*2,y*2) 
                       
            setColor(npx,getColor(px))            
           
            
    return newPic
sel = input("type u for scale up, type d for scale down: ")
print("pick an image")
pic = makePicture(pickAFile())
if sel == "u":
    newPic = scaleDown(pic)
elif sel =="d":
    newPic = scaleUp(pic)
else:
    print("invalid input")
filename = input("New File name: ")

filename = filename + ".jpg"
print("saving....")

savePicture(newPic, filename)
print("saved.")
explore(newPic)



def scaleUp(pic):
    w = getWidth(pic)*2
    h = getHeight(pic)*2
  
    newPic = makeEmptyPicture(w,h)    
    for x in range(w):
        for y in range(h):
            npx = getPixel(newPic,x,y)
            px = getPixel(pic,math.ceil(x/2),math.ceil(y/2))                 
            setColor(npx,getColor(px))            
             
              
        return newPic    
            
