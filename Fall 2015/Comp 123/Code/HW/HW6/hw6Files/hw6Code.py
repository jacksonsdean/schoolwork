""" =======================================================================
File: hw6Code.py
Author: Your name here

Contains solutions and test calls for Homework 6.
===========================================================================
"""


# =============================
# Import section

from imageTools import *
import PIL
import numpy


# =============================
# Function definition section


# -------------------------------------------------------------------------
# Question 1

def squash3(pic):
    """Takes in a picture and makes a new picture whose height
    is 1/3 of the original, but whose width is the same as the original.
    It then creates a squashed version of the original picture by scaling
    down only in the y direction. It returns the new picture."""
    wid = getWidth(pic)
    hgt = getHeight(pic)
    newW = wid
    newH = hgt // 3 #needs integer division
    newPic = makePicture(newW, newH) #makePicture takes width and then height
    for x in range(newW):
        for y in range(newH):
            newPix = getPixel(newPic, x, y) #newPix should take the pixel from the new picture
            oldPix = getPixel(pic, x, 3*y)
            setColor(newPix, getColor(oldPix))#set color takes a pixel object, not a picture
    return newPic



    
# -------------------------------------------------------------------------
# Question 2

# Put your definition of freeRotate here

def freeRotate(pic, angle, rotX, rotY):
    """Takes a picture, angle and the center of rotation as an input. Uses a function to calculate the old x and y of each pixel then copies that color to a pixel in the new image"""
    w = getWidth(pic)
    h = getHeight(pic)
    
    nPic = makePicture(w,h)
    
    for x in range(w):
        for y in range(h):
            oldXY = computeOldXY(angle,rotX,rotY,x,y)
            oX = oldXY[0]
            oY = oldXY[1]
            if oX >= w or oY >= h or oX <= 0 or oY <= 0:
                continue
            
            oPx = getPixel(pic, oX,oY)
            nPx = getPixel(nPic,x,y)
            
            setColor(nPx, getColor(oPx))

    return nPic

# use test calls in the section at the bottom of the file, or add your own THERE


def computeOldXY(angle, rotX, rotY, newX, newY):
    """Takes in an angle of rotation, the (x, y) for the center of
    rotation, and the (x, y) for the location in the new, rotated image,
    and it computes and returns the (x, y) location in the original image."""
    diffX = newX - rotX
    diffY = newY - rotY
    cosOfAng = math.cos(math.radians(-angle))
    sinOfAng = math.sin(math.radians(-angle))
    oldX = (cosOfAng * diffX) - (sinOfAng * diffY) + rotX
    oldY = (sinOfAng * diffX) + (cosOfAng * diffY) + rotY
    oldX = int(round(oldX))  # convert the (x, y) into integers
    oldY = int(round(oldY))
    return (oldX, oldY)





# -------------------------------------------------------------------------
# Question 3
    
# Put your definition of varyBlend here

def varyBlend(pic1,pic2):
    w = min(getWidth(pic1), getWidth(pic2))
    h = min(getHeight(pic1), getHeight(pic2))  
    pic3 = makePicture(w,h)
    weight = 1
    step = 1/w
    
    
    for x in range(w):
        weight+=-step
        for y in range(h):
                px1 = getPixel(pic1, x, y)
                px2 = getPixel(pic2, x, y)
                px3 = getPixel(pic3, x, y)    
    
                r = ((weight * getRed(px1)) + ((1-weight)*getRed(px2))) //2
                g = ((weight*getGreen(px1)) + ((1-weight)*getGreen(px2))) //2
                b = ((weight*getBlue(px1)) + ((1-weight)*getBlue(px2))) //2
                setColor(px3,makeColor(r,g,b))
                
    return pic3


# use test calls in the section at the bottom of the file, or add your own THERE
    


# -------------------------------------------------------------------------
# Question 4

# Put your definition of floodFill here
def floodFill(pic, startX, startY, col):
    nPic = copyPicture(pic)
    w = getWidth(nPic)
    h = getHeight(nPic)
    
    baseColor = getColor(getPixel(nPic,startX,startY))
   
    queue = [(startX,startY)]
    visited = {(startX, startY):True}
    
    px = getPixel(nPic, startX, startY)
    setColor(px, col) 
    i=0
    while len(queue) > 0:
        currX = queue[0][0]
        currY = queue[0][1]
        del queue[0]  
        adj = [(currX - 1, currY), (currX + 1, currY), (currX, currY - 1), (currX, currY + 1)]
        px = getPixel(nPic, currX,currY)
        oCol = getColor(px)
        if distance(oCol,baseColor) <= 100:
            setColor(px,col)
        for p in adj:
            x1 = p[0]
            y1 = p[1]
            if x1 >= w or x1 <= 0 or y1 >= h or y1 <= 0:
                continue
            elif not ((x1,y1) in visited.keys()):
                coordTup = (x1,y1)
                queue.append(coordTup)
                visited.update({(coordTup):True})
            
    return nPic


# use test calls in the section at the bottom of the file, or add your own THERE
    


    

# =============================
# Script/test call section


# change the path to the files below to make them work for you, I assumed you
# would temporarily make MediaSources a subfolder of the working folder.

if __name__ == '__main__':
    pic1 = makePicture("MediaSources/fish.jpg")
    pic2 = makePicture("MediaSources/passionflower.jpg")
    pic3 = makePicture("MediaSources/blackcat.jpg")
    pic4 = makePicture("MediaSources/greekruins.jpg")
    
    
    ## Call to squash3
    #sq1 = squash3(pic3)
    #explore(sq1)
    #sq2 = squash3(pic1)
    #explore(sq2)
    
    
    ## Calls to freeRotate
    #rot1 = freeRotate(pic4, 75, 100, 100)
    #explore(rot1)
    #rot2 = freeRotate(pic2, -190, 250, 250)
    #explore(rot2)
    
    ## Calls to varyBlend
    #vb1 = varyBlend(pic1, pic3)
    #explore(vb1)
    #vb2 = varyBlend(pic4, pic2)
    #explore(vb2)
    
    ## Tests for floodFill
    ff1 = floodFill(pic4, 10, 10, green)
    explore(ff1)
    #ff2 = floodFill(pic1, 10, 10, green)
    #explore(ff2)
    
    
