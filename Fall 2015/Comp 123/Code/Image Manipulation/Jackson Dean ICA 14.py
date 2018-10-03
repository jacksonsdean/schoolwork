from imageTools import *

pic = makePicture("MediaSources/horse.jpg")

def grayscale(pic):
  newPic = copyPicture(pic)
  for pixel in getPixels(newPic):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    lumin = (r + g + b) / 3
    setColor(pixel, makeColor(lumin, lumin, lumin))
  show(newPic) 
  return newPic

def weightedScale(pic,w1,w2,w3):
  newPic = copyPicture(pic)
  for pixel in getPixels(newPic):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    lumin = (w1*r + w2*g + w3*b) / 3
    setColor(pixel, makeColor(lumin, lumin, lumin))
  return newPic

#explore(weightedScale(pic,3,.5,2))

def makeNeg(pic):
  for pixel in getPixels(pic):
    r = (255-getRed(pixel))
    g = (255-getGreen(pixel))
    b = (255-getBlue(pixel))
    setRed(pixel,r)
    setGreen(pixel,g)
    setBlue(pixel,b)
  return(pic)
    
    
explore(makeNeg(pic))
   
    
    
    