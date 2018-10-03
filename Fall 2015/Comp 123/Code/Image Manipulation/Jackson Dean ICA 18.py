from imageTools import *

threshold = int(input("THRESHOLD: "))
#~90


def subBackground(fpic, obpic, bpic, threshold):
    
    w = min(getWidth(fpic), getWidth(bpic))
    h = min(getHeight(fpic), getHeight(bpic))
    
    npic = makePicture(w,h)
    
    for x in range(w):
        for y in range(h):
            
            fpx = getPixel(fpic, x, y)
            obpx = getPixel(obpic, x, y)
            bpx = getPixel(bpic, x , y)
            npx = getPixel(npic, x, y)
            
            fcol = getColor(fpx)
            obcol = getColor(obpx)
            bcol = getColor(bpx)
            
            
            if distance(fcol,obcol)<threshold:
                setColor(npx, bcol)
            else:
                setColor(npx, fcol)
                
    return npic
    

foregroundPicture = makePicture("SusanStudents/Jackson.jpg")
backgroundPicture = makePicture("SusanStudents/Backgrounds/moon.jpg")
oldBackgroundPicture = makePicture("SusanStudents/EmptyChair.jpg")

#newPicture = subBackground(foregroundPicture,  oldBackgroundPicture , backgroundPicture , threshold)
#explore(newPicture)

#savePicture(newPicture, "tmp.jpg")



def chromSub(fpic, bpic):
    w = min(getWidth(fpic), getWidth(bpic))
    h = min(getHeight(fpic), getHeight(bpic))
    
    npic = makePicture(w,h)
    
    for x in range(w):
        for y in range(h):
            fpx = getPixel(fpic,x,y)
            nbpx = getPixel(bpic,x,y)
            npx = getPixel(npic,x,y)
            
            r = getRed(fpx)
            g = getGreen(fpx)
            b = getBlue(fpx)
            
            if g > r and g > b:
                setColor(npx, getColor(fpx))
                
    return npic


newPicture = subBackground(foregroundPicture,  oldBackgroundPicture , backgroundPicture)
