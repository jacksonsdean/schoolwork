from imageTools import *
import math
import os.path

def scaleDown(pic,f=2):
    
    w = math.ceil(getWidth(pic)/f)
    h = math.ceil(getHeight(pic)/f)

    newPic = makeEmptyPicture(w,h)    
    for x in range(w):
        for y in range(h):
            npx = getPixel(newPic,x,y)
            px = getPixel(pic,x*f,y*f) 
                       
            setColor(npx,getColor(px))            
           
            
    return newPic

def scaleUp(pic,f=2):
    w = getWidth(pic)*f
    h = getHeight(pic)*f 
    newPic = makeEmptyPicture(w,h)
    
    for x in range(w):
        for y in range(h):
            newPx = getPixel(newPic,x,y)
            color = getColor(getPixel(pic, x//f,y//f))
            setColor(newPx, color)
    
    return newPic
                        
def checkFile(filename):
    if os.path.isfile(filename):
        overwrite = input("file already exists, overwrite? \ny/n: ").lower()
    else:
        overwrite = "nf"
    return overwrite

def saveFile(pic,filename):
    savePicture(pic, filename)
    print("saved.")
      

def main():
    res = input("""type 'u' for scale up or 'd' for scale down:\n""").lower()
    if not (res == "u" or res == "d"):
        print("invalid input")
        input("press any key to continue...")
        main()
        return 0
    
    print("pick an image to scale\n")
    pic = makePicture(pickAFile())
    factor = input("type the factor to scale by:\n")
    print("scaling.......\n")
    
    try:
        int(factor)
    except ValueError:
        print("scale factor must be an INT")
        input("press any key to continue...")
        main()
        return 0
    
    factor=int(factor)
    
    if res == "d":
        newPic = scaleDown(pic,factor)
    elif res == "u":
        newPic = scaleUp(pic,factor)
        
    filename = input("new file name:\n")
    
    if not ".jpg" in filename:
        filename = filename + ".jpg"
        
    print("\nsaving....")
    n=0
    
    while n != 1:
        overwrite = checkFile(filename)
        if overwrite == "y":
            saveFile(newPic,filename)
            n=1
        elif overwrite == "nf":
            saveFile(newPic,filename)
            n=1            
        elif overwrite == "n":
            print("canceling....\n\n")
            n=1
            main()
            return 0
        else:
            n=0
    explore(makePicture(filename))          
main()