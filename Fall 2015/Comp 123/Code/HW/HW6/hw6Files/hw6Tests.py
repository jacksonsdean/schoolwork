"""
----------------------------------------------------------------------
Homework 6 testing file

Includes functions to test each program in Homework 6.
----------------------------------------------------------------------
"""

from hw6Code import *

# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.

p1 = makePicture('MediaSources/fish.jpg')
p2 = makePicture('MediaSources/passionflower.jpg')
p3 = makePicture("MediaSources/blackcat.jpg")
p4 = makePicture("MediaSources/greekruins.jpg")



def runTests():
    """Uncomment the tests here that you want to run."""
    #testSquash3()
    #testFreeRotate()
    #testVaryBlend()
    testFloodFill()
    print("DONE WITH ALL TESTS.")



# ==========================================================================================
# Tests for squash3

def testSquash3():
    print("--------------------------------------")
    print("Testing squash3:")

    
    r1 = squash3(p1)
    show(r1)
    r2 = squash3(p2)
    show(r2)
    r3 = squash3(p3)
    show(r3)

    print("    Should display three windows(!):")
    print("        1. The fish picture, squashed in vertical to 1/3")
    print("        2. The passionflower picture, squashed in vertical to 1/3")
    print("        3. The black cat picture, squashed in vertical to 1/3")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(r1)
    hide(r2)
    hide(r3)

 

# ==========================================================================================
# Tests for freeRotate

def testFreeRotate():
    print("--------------------------------------")
    print("Testing freeRotate:")

    allOk = True
    w1 = getWidth(p1)
    h1 = getHeight(p1)
    
    r1 = freeRotate(p1, 90, w1//2, h1//2)
    show(r1)
    r2 = freeRotate(p1, 90, 300, 200)
    show(r2)
    r3 = freeRotate(p1, 45, w1//2, h1//2)
    show(r3)
    r4 = freeRotate(p1, -45, 0, 0)
    show(r4)
    r5 = freeRotate(p1, -180, w1//2, h1//2)
    show(r5)
    r6 = freeRotate(p1, 30, w1//2, h1//2)
    show(r6)
    r7 = freeRotate(p1, -30, w1//2, h1//2)
    show(r7)

    print("    Should display six windows(!):")
    print("        1. a 90 degree rotate right with center as axis")
    print("        2. a 90 degree rotate right with (300, 200) as axis, shifted right")
    print("        3. a 45 degree rotate right with center as axis")
    print("        4. a 45 degree rotate left with corner as axis, only see lower left corner")
    print("        5. a 180 degree rotate upside down with center as axis")
    print("        6. a 30 degree rotate right with center as axis")
    print("        7. a 30 degree rotate left with center as axis")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(r1)
    hide(r2)
    hide(r3)
    hide(r4)
    hide(r5)
    hide(r6)
    hide(r7)



# ==========================================================================================
# Tests for varyBlend

def testVaryBlend():
    print("--------------------------------------")
    print("Testing varyBlend:")

    
    r1 = varyBlend(p1, p2)
    show(r1)
    r3 = varyBlend(p1, p4)
    show(r3)
    r4 = varyBlend(p2, p3)
    show(r4)
    r5 = varyBlend(p2, p4)
    show(r5)
    r7 = varyBlend(p4, p2)
    show(r7)

    print("    Should display five windows(!):")
    print("        1. The fish picture blended with a the passionflower")
    print("        2. The fish picture blended with the greek ruins")
    print("        3. The passionflower picture blended with the black cat")
    print("        4. The passionflower blended with the greek ruins")
    print("        5. The greek ruins blended with the passionflower")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(r1)
    hide(r3)
    hide(r4)
    hide(r5)
    hide(r7)


# ==========================================================================================
# Tests for floodFill

def testFloodFill():
    print("--------------------------------------")
    print("Testing floodFill:")

    allOk = True

    r1 = floodFill(p4, 10, 10, cyan)
    show(r1)
    r2 = floodFill(p4, 270, 170, red)        
    show(r2)
    r3 = floodFill(p4, 120, 180, makeColor(145, 225, 180))
    show(r3)
    r4 = floodFill(p1, 200, 300, makeColor(139, 69, 19))
    show(r4)
    r5 = floodFill(p2, 10, 10, blue)
    show(r5)

    print("    Should display five windows:")
    print("        1. Ruins, most of sky should be cyan, except for patch on right by steps")
    print("        2. Ruins, most of ruins should be red, except lower left corner")
    print("        3. Ruins, leftmost window should be green (except bottom)")
    print("        4. Fish, turns stone brown")
    print("        5. Passionflower, most of background turns blue")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(r1)
    hide(r2)
    hide(r3)
    hide(r4)
    hide(r5)




# ==================================================================


runTests()
