from imageTools import *

def simpleBlend(pic1, pic2):
    if getHeight(pic1) != getHeight(pic2) or getWidth(pic1) != getWidth(pic2):
        raise ValueError("Pictures different sizes") 
    
    w = getWidth(pic1)
    h = getHeight(pic1)
    
    
    pic3 = makeEmptyPicture(w,h)
    
    for x in range(w):
        for y in range(h):
            px1 = getPixel(pic1, x, y)
            px2 = getPixel(pic2, x, y)
            px3 = getPixel(pic3, x, y)
            
            r = (getRed(px1) + getRed(px2)) //2
            g = (getGreen(px1) + getGreen(px2)) //2
            b = (getBlue(px1) + getBlue(px2)) //2
            
            setColor(px3,makeColor(r,g,b)) 
    return pic3

p1 = makePicture("MediaSources/church.jpg")
p2 = makePicture("MediaSources/garden.jpg")
p3 = makePicture("MediaSources/bigben.jpg")
p4 = makePicture("MediaSources/beach.jpg")
#explore(simpleBlend(p1, p2))

def blend(pic1,pic2):
    w = min(getWidth(pic1), getWidth(pic2))
    h = min(getHeight(pic1), getHeight(pic2))
    
    pic3 = makePicture(w,h)
    
    for x in range(w):
        for y in range(h):
            px1 = getPixel(pic1, x, y)
            px2 = getPixel(pic2, x, y)
            px3 = getPixel(pic3, x, y)
            
            r = (getRed(px1) + getRed(px2)) //2
            g = (getGreen(px1) + getGreen(px2)) //2
            b = (getBlue(px1) + getBlue(px2)) //2
            
            setColor(px3,makeColor(r,g,b))    
            
    return pic3

#explore(blend(p3,p4))

def weightedBlend(pic1,pic2,wgt1):
    w = min(getWidth(pic1), getWidth(pic2))
    h = min(getHeight(pic1), getHeight(pic2))  
    pic3 = makePicture(w,h)
    if not 0<=wgt1<1.0:
        raise ValueError("wgt1 bad size")
    wgt2 = 1.0 - wgt1
    
    for x in range(w):
        for y in range(h):
                px1 = getPixel(pic1, x, y)
                px2 = getPixel(pic2, x, y)
                px3 = getPixel(pic3, x, y)    
    
                r = ((wgt1 * getRed(px1)) + (wgt2*getRed(px2))) //2
                g = ((wgt1*getGreen(px1)) + (wgt2*getGreen(px2))) //2
                b = ((wgt1*getBlue(px1)) + (wgt2*getBlue(px2))) //2
                setColor(px3,makeColor(r,g,b))
    return pic3


#explore(weightedBlend(p3,p4,0.5))