"""
============================================================================
finalImages.py

This file will contain your answers for the "imageTools" question.
============================================================================
"""

from imageTools import *

# ==========================================================================
# Question 4

# put your definition of quarterPic here
def quarterPic(img):
    """Takes an image and creates a new empty image, then super inefficiently copies the first image with half width and height onto the new image four times"""  
    w = getWidth(img)
    h = getHeight(img)
    newPic = makeEmptyPicture(w,h)
    for x in range(w//2):
        for y in range(h//2):
                px = getPixel(img,x*2,y*2)
                newPx = getPixel(newPic,x,y)
                col = getColor(px)
                setColor(newPx,col)
                
    for x in range(w//2):
        for y in range(h//2):
                px = getPixel(img,x*2,y*2)
                newPx = getPixel(newPic,x+w//2,y+h//2)
                col = getColor(px)
                setColor(newPx,col)
                
    for x in range(w//2):
        for y in range(h//2):
                px = getPixel(img,x*2,y*2)
                newPx = getPixel(newPic,x,y+h//2)
                col = getColor(px)
                setColor(newPx,col) 
                
    for x in range(w//2):
        for y in range(h//2):
                px = getPixel(img,x*2,y*2)
                newPx = getPixel(newPic,x+w//2,y)
                col = getColor(px)
                setColor(newPx,col)     
    return newPic

        
    
if __name__ == '__main__':
    
    # Question 3 test calls
    #pic1 = makePicture("butterfly2.jpg")
    #pic2 = makePicture("daisies.jpg")
    #pic3 = makePicture("horse.jpg")
    #show(pic1)
    #show(pic2)
    #show(pic3)
    
    #res1 = quarterPic(pic1)
    #show(res1)
    #res2 = quarterPic(pic2)
    #show(res2)
    #res3 = quarterPic(pic3)
    #show(res3)

    