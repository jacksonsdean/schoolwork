from imageTools import *

def tintedSquare(pic, upperLeftX, upperLeftY, sideLen, color):
    for x in range(upperLeftX, upperLeftX + sideLen):
        for y in range(upperLeftY, upperLeftY + sideLen):
            pixel = getPixel(pic, x, y);setColor(pixel, makeColor(((getRed(pixel) + getRed(color))//2),((getGreen(pixel) + getGreen(color))//2),((getBlue(pixel) + getBlue(color))//2)))
            
p1 = makePicture("MediaSources/statue.jpg"); tintedSquare(p1, 10, 10, 100, red);tintedSquare(p1, 200, 110, 100, makeColor(50, 5, 180));tintedSquare(p1, 300, 200, 40, green); explore(p1)

def copyPicInto(smPic, bPic, startX, startY):
    if getWidth(smPic) > getWidth(bPic) or getHeight(smPic) > getHeight(bPic):
        return null
    else:
        show(smPic)
        show(bPic)
        for y in range(getPixels(smPic)):
            for x in range(getPixels(smPic)):
                sPx = getPixel(smPic, x, y)
                bPx = getPixel(bPic, x, y)
                setColor(bPx, getColor(sPx))
                
        
smPic = makePicture("MediaSources/greenTurtle.jpg")
bPic = makePicture("MediaSources/jungle.jpg")
copyPicInto(smPic, bPic, 25, 25)
copyPicInto(smPic, bPic, 200, 200)
copyPicInto(smPic, bPic, 300, 200)
show(bPic)