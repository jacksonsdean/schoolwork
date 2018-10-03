

from imageTools import *

# ----------------------------------------------------------
# Start with streakRight, make a copy, create streakDown

def streakRight(pic):
    """Takes an input picture and copies it. It then changes the right half
    of the picture to be a streaking of the colors in the middle column. It
    returns the new picture."""
    newPic = copyPicture(pic)
    wid = getWidth(newPic)
    hgt = getHeight(newPic)
    midpt = wid // 2
    for x in range(midpt+1, wid):
        for y in range(hgt):
            origPix = getPixel(newPic, midpt, y)
            pix = getPixel(newPic, x, y)
            setColor(pix, getColor(origPix))
    return newPic

def streakDown(pic):
    """Takes an input picture and copies it. It then changes the lower half
    of the picture to be a streaking of the colors in the middle column. It
    returns the new picture."""
    newPic = copyPicture(pic)
    wid = getWidth(newPic)
    hgt = getHeight(newPic)
    midpt = hgt // 2
    for x in range(wid):
        for y in range(midpt+1, hgt):
            origPix = getPixel(newPic, x, midpt)
            pix = getPixel(newPic, x, y)
            setColor(pix, getColor(origPix))
    return newPic


    
# ----------------------------------------------------------
# Put definition of completeMirror here
def completeMirror(pic):
    """takes a picture and then copies the right half to a new picture and then copies that half again reversed to the left half of a picture, like a mirror. returns new picture"""
    w = getWidth(pic) * 2 
    h = getHeight(pic)
    ow = getWidth(pic)
    newPic = makeEmptyPicture(w,h)
    for x in range(w//2):
        for y in range(h):
            col = getColor(getPixel(pic,x,y))
            setColor(getPixel(newPic,x,y),col)
            
    for x in range(ow-1):
        for y in range(h):
            col = getColor(getPixel(pic, ow-x-1,y))
            setColor(getPixel(newPic,ow+x,y),col)
                      
    
    return newPic
    
    



# ----------------------------------------------------------
# Test calls


if __name__ == '__main__':
    # set up pictures to use
    pic1 = makePicture('gorge.jpg')
    pic2 = makePicture('arch.jpg')
    show(pic1)
    show(pic2)
    
    
    # streakRight:
    #pic3 = streakRight(pic1)
    #show(pic3)
    #pic4 = streakRight(pic2)
    #show(pic4)
    
    # streakDown:
    #pic5 = streakDown(pic1)
    #show(pic5)
    #pic6 = streakDown(pic2)
    #show(pic6)
    #pic7 = streakDown(pic3)  #streak on top of streak
    #show(pic7)

    # completeMirror:
    pic8 = completeMirror(pic1)
    show(pic8)
    pic9 = completeMirror(pic2)
    show(pic9)