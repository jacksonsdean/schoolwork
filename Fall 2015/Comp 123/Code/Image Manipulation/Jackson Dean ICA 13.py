from imageTools import *

img = makePicture("MediaSources/horse.jpg")

print(getWidth(img))
print(getHeight(img))
    
px1 = getPixel(img, 25, 100)

print(getColor(px1))

setBlue(px1, 255)
setRed(px1, 0)
setGreen(px1, 0)

def changeRed(pic, factor):
   for pix in getPixels(pic):
      redVal = getRed(pic)
      newVal = factor * redVal
      setRed(pic, newVal)
      
def changeBlue(pic, factor):
   for pix in getPixels(pic):
      blueVal = getBlue(pic)
      newVal = factor * blueVal
      setBlue(pic, newVal)  
      
def changeGreen(pic, factor):
   for pix in getPixels(pic):
      greenVal = getGreen(pic)
      newVal = factor * greenVal
      setGreen(pic, newVal)    
   
def fixGreen(pic, val):
   for px in getPixels(img):
      setGreen(px,val)
        
for px in getPixels(img):
   changeRed(px, 2.0)
   
repaint(img)
explore(img)