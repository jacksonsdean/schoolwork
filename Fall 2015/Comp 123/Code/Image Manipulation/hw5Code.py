""" =======================================================================
File: hw5Code.py
Author: Jackson 

Contains solutions and test calls for Homework 5.
===========================================================================
"""


# =============================
# Import section

from imageTools import *



# =============================
# Function definition section


# -------------------------------------------------------------------------
# Question 1


def findClosestColor(newColor, colorList):
    """Takes in a color object and a list of color objects. It compares newColor
    to each color in the colorList, and keeps track of the most similar color
    from the color list (the one where distance is smallest). It returns the
    most similar color from the colorList."""
    currClosest = colorList[0]
    currDist = distance(newColor, currClosest)
    for col in colorList:
        nextDist = distance(newColor, col)
        if nextDist < currDist:
            currClosest = col
            currDist = nextDist
    return currClosest



def testFindClosestColor():
    """Tests the findClosestColor function by making a series of calls
    and checking that the returned value is as expected."""
    
    print("--------------------------------------")
    print("Testing findClosestColor:")

    allOk = True
    colors1 = [red, green, blue, yellow, pink, white, black]
    colors2 = [green, makeColor(76, 133, 16), # dark green
               makeColor(166, 237, 90), # light green
               makeColor(120, 106, 196), # dark periwinkle
               makeColor(89, 31, 84), # berry
               white, black, blue]
    colors3 = [red]
    colors4 = [makeColor(100,100,100),red,blue]
    colors5 = [makeColor(100,100,100),red,blue]
    colors6 = [makeColor(100,100,100),red,blue]
    colors7 = [makeColor(101,101,101),red,blue]
    colors8 = [makeColor(210, 210, 210)]
    
    # Test 1
    c1 = findClosestColor(makeColor(240, 15, 30), colors1)
    if c1 != red:
        print("Called: findClosestColor(makeColor(240, 15, 30), colors1)")
        print("Expected result", red, 'but actual result was', c1)
        allOk = False
    
    ## --- add more tests like the one above, using both colors1 and colors2, as well
    ## --- as additional color lists of your own making.
    
    # test 2
    c3 = findClosestColor(makeColor(100,100,100),colors3)
    if c3 != red:
        print("Called: findClosestColor(makeColor(100,100,100), colors3)")
        print("Expected result", red, 'but actual result was', c3)
        allOk = False
    #test 3
    c4 = findClosestColor(makeColor(100,100,100),colors4)
    if c4 != makeColor(100,100,100):
        print("Called: findClosestColor(makeColor(100,100,100), colors4)")
        print("Expected result", makeColor(100,100,100), 'but actual result was', c4)
        allOk = False
    #test 4
    c5 = findClosestColor(blue,colors5)
    if c5 != blue:
        print("Called: findClosestColor(blue, colors5)")
        print("Expected result", makeColor(100,100,100), 'but actual result was', c5)
        allOk = False
    #test 5
    c6 = findClosestColor(makeColor(100,100,100),colors7)
    if c6 != makeColor(101,101,101):
        print("Called: findClosestColor(101,101,101, colors6)")
        print("Expected result", makeColor(101,101,101), 'but actual result was', c6)
        allOk = False   
    #test 6 
    c7 = findClosestColor(makeColor(100,100,100),colors7)
    if c7 != makeColor(101,101,101):
        print("Called: findClosestColor(blue, colors7)")
        print("Expected result", makeColor(210,210,210), 'but actual result was', c7)
        allOk = False  
        
    if allOk:
        print()
        print("findClosestColor passed all tests!")

    print("--------------------------------------")    


    
# -------------------------------------------------------------------------
# Question 2

# Put your definition of simplify here
def simplify(pic, colorList):
    """Takes a picture and makes a copy, then changes every pixel's color to the closest color in the list"""
    newPic = copyPicture(pic)
    for px in getPixels(newPic):
        setColor(px,findClosestColor(getColor(px),colorList))
        
        
    
    return newPic


# use test calls in the section at the bottom of the file, or add your own THERE


# -------------------------------------------------------------------------
# Question 3
    
# Put your definition of colorShiftSquare here

def colorShiftSquare(pic, inpx, inpy, size):
    """Takes a picture, (x,y), and a size and then switches the RGB values for a square at thatr (x,y) and of that size"""
    w = getWidth(pic)
    h = getHeight(pic)
    for x in range(size):
        for y in range(size):
            if inpx < 0 or inpy < 0:
                inpx = 0
                inpy = 0
            if x+inpx >= w or x+inpx<0:
                continue            
            if y+inpy >= h or y+inpy<0:
                continue
            px = getPixel(pic, inpx + x, inpy + y)
            r = getGreen(px)
            g = getBlue(px)
            b = getRed(px)
            setColor(px, makeColor(r,g,b))
    return pic

# use test calls in the section at the bottom of the file, or add your own THERE
    


# -------------------------------------------------------------------------
# Question 4


def checkerboard(pic, sqSize):
    """Takes in a picture and a square size, and it makes a copy of the input
    picture. It then modifies the new picture to have a checkerboard pattern,
    were every other square region has been color-shifted. Teach region's
    size is given by the sqSize input, and the upper-left corner region
    should be color-shifted."""
    newP = copyPicture(pic)
    cntX = 0
    for startX in range(0, getWidth(newP), sqSize):
        cntY = 0
        for startY in range(0, getHeight(newP), sqSize): #forgot RANGE, needs to be a iterable list of ints
            if (cntX % 2) == (cntY % 2):
                colorShiftSquare(newP, startX, startY, sqSize) #should be newPic, not pic to change the final picture
                show(newP) 
        
            cntY = cntY + 1
        cntX = cntX + 1
    return newP #return should be outside of for loop

    

# =============================
# Script/test call section


# change the path to the files below to make them work for you, I assumed you
# would temporarily make MediaSources a subfolder of the working folder.

if __name__ == '__main__':
    pic1 = makePicture("MediaSources/shops.jpg")
    pic2 = makePicture("MediaSources/swan.jpg")
    pic3 = makePicture("MediaSources/passionflower.jpg")
    #show(pic1)
    #show(pic2)
    #show(pic3)
    
    
    ## Call to findClosestColor tester
    #testFindClosestColor()
    
    ## Calls to simplify 
    #colorList = [red, green, blue, yellow, pink, white, black, 
                 #makeColor(105, 30, 157), # purple
                 #makeColor(245, 17, 30)]  # orange

    #newP1 = simplify(pic1, colorList)
    #newP2 = simplify(pic2, colorList)
    #newP3 = simplify(pic3, [green, makeColor(76, 133, 16), # dark green
                            #makeColor(166, 237, 90), # light green
                            #makeColor(120, 106, 196), # dark periwinkle
                            #makeColor(89, 31, 84), # berry
                            #white, black, blue])
    #show(newP1)
    #show(newP2)
    #show(newP3)
    
    ## Calls to colorShiftSquare
    #pic3Copy = copyPicture(pic3)
    #midx = getWidth(pic3) // 2
    #midy = getHeight(pic3) // 2
    #colorShiftSquare(pic3Copy, 10, 10, 50)
    #colorShiftSquare(pic3Copy, midx, midy, 300)
    #colorShiftSquare(pic3Copy, 10, 200, 100)
    #show(pic3Copy)
    
    ## Tests for checkerboard
    #p1Check = checkerboard(pic1, 20)
    #show(p1Check)
    #p3Check = checkerboard(pic3, 100)
    #show(p3Check)

    
    
