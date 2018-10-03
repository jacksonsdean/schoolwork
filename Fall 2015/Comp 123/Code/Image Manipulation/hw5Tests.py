"""
----------------------------------------------------------------------
Homework 5 testing file

Includes functions to test each program in Homework 5.
----------------------------------------------------------------------
"""

from hw5Code import *

# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.

p1 = makePicture('MediaSources/shops.jpg')
p2 = makePicture('MediaSources/swan.jpg')
p3 = makePicture('MediaSources/passionFlower.jpg')
p4 = makePicture('MediaSources/redMotorcycle.jpg')


def runTests():
    """Uncomment the tests here that you want to run."""
    #testSimplify()
    #testColorShiftSquare()
    #testCheckerboard()
    print("DONE WITH ALL TESTS.")

  
  
  
  
# ========================================================================



# ==========================================================================================
# Tests for simplify


def testSimplify():
    print("--------------------------------------")
    print("Testing simplify:             CHECK VISUALLY")
    
    testColors1 = [red, green, blue, yellow, pink, white, black, 
                  makeColor(105, 30, 157), # purple
                  makeColor(245, 17, 30)] # orange 
    testColors2 = [green, makeColor(76, 133, 16), # dark green
                   makeColor(166, 237, 90), # light green
                   makeColor(120, 106, 196), # dark periwinkle
                   makeColor(89, 31, 84), # berry
                   white, black, blue]
    
    p1Res = simplify(p1, testColors1)
    show(p1Res)
    
    p2Res = simplify(p2, testColors1)
    show(p2Res)
    
    p3Res = simplify(p3, testColors2) 
    show(p3Res)
    
    p4ResA = simplify(p4, [black, makeColor(64, 64, 64), makeColor(128, 128, 128),
                           makeColor(192, 192, 192), white])
    show(p4ResA)

    p4ResB = simplify(p4, testColors2)
    show(p4ResB)

    print("    Should display 5 windows:")
    print("        First is a highly purple version of shops")
    print("        Second is a purple, black, and white swan")
    print("        Third is a green, purple/blue passionflower")
    print("        Fourth is a grayscale version of red motorcycle")
    print("        Fourth is a green/purple/blue version of red motorcycle")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(p1Res)
    hide(p2Res)
    hide(p3Res)
    hide(p4ResA)
    hide(p4ResB)






# ========================================================================
# Tests for colorShiftSquare

def testColorShiftSquare():
    print("--------------------------------------")
    print("Testing colorShiftSquare:             CHECK VISUALLY")


    newp4 = copyPicture(p4)
    show(newp4)
    colorShiftSquare(newp4, 30, getHeight(p4) - 70, 50)
    show(newp4)
    colorShiftSquare(newp4, 150, 150, 250)
    show(newp4)
    colorShiftSquare(newp4, 400, 400, 400)
    show(newp4)
    colorShiftSquare(newp4, -5, -5, 30)
    show(newp4)
    print("    Should modify red motorcycle to have:")
    print("      smallish square in lower left corner")
    print("      biggish square toward middle")
    print("      large square but goes off lower-right end")
    print("      partial square in upper left corner, starts offscreen: no error!")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(newp4)




# ==========================================================================================
# Tests for checkerboard


def testCheckerboard():
    print("--------------------------------------")
    print("Testing checkerboard:             CHECK VISUALLY")
    

    p1Check = checkerboard(p1, 10)
    show(p1Check)
    
    p3Check = checkerboard(p3, 171)
    show(p3Check)
    
    p4Check = checkerboard(p4, 70)
    show(p4Check)
    

        
    print("    Should display 3 pictures:")
    print("        The shops picture with very small squares")
    print("        The passionflower with large squares")
    print("        the red motorcycle with medium squares")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")
    hide(p1Check)
    hide(p3Check)
    hide(p4Check)



    
    
# ========================================================================



runTests()