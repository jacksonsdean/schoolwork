# ====================================================================
#
#  Homework 3 tests
#
# ====================================================================

# Change the filename below to match your solution file's name

from hw3Code import *

import turtle
import random

# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    #testFilterInRange()
    #testFollowPath()
    testDrawRandSpiral()
    print("DONE WITH ALL TESTS.")
        
        

# ==========================================================================================
# Tests for filterInRange

def testFilterInRange():
    """Tests the filterInRange function. Note that details about specific test calls
    are only printed if the function FAILS the test."""
    print("--------------------------------------")
    print("Testing filterInRange:")
    allOk = True

    # Test 1
    resList = filterInRange(10, 20, [1, 3, 8, 12, 13, 17, 19])
    
    if resList != [12, 13, 17, 19]:
        print("Called: filterInRange(10, 20, [1, 3, 8, 12, 13, 17, 19])")
        print("Expected:", [12, 13, 17, 19], "   but function returned:", resList)
        allOk = False
    
    # Test 2
    resList = filterInRange(0, 10, [5, 0, -2, 23, -5, 41, 2, 10])
    if resList != [5, 0, 2, 10]:
        print("Called: filterInRange(0, 10, [5, 0, -2, 23, -5, 41, 2, 10])")
        print("Expected:", [5, 0, 2, 10], "   but function returned:", resList)
        allOk = False

    # Test 3
    resList = filterInRange(5, 2, [1, 3, 8, 12, 13, 17, 19])
    if resList != []:
        print("Called: filterInRange(5, 2, [1, 3, 8, 12, 13, 17, 19])")
        print("Expected:", [], "   but function returned:", resList)
        allOk = False

    # Test 4
    resList = filterInRange(10, 20, [-10, -15, -20, -25, 25, 30, 50])
    if resList != []:
        print("Called: filterInRange(10, 20, [-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", [], "   but function returned:", resList)
        allOk = False

    print()
    if allOk:
        print("filterInRange PASSED ALL TESTS!")
    else:
        print("filterInRange FAILED ONE OR MORE TEST!")
    print("--------------------------------------") 
    input("Press a key to go on: ")
        #    
    

# ==========================================================================================
# Tests for followPath

def testFollowPath():
    print("--------------------------------------")
    print("Testing followPath:       CHECK VISUALLY")
    
    
    sss = turtle.Screen()
    sss.bgcolor('lightblue')
    ttt = turtle.Turtle()
    ttt.speed(0)
    followPath(ttt, "FFFFFL FFFFFFFL FFFFFL FFFFFFFL JJLJ FFFR FFR FFFR FFR")
    sss.exitonclick()
    
    sss = turtle.Screen()
    sss.bgcolor('black')
    ttt = turtle.Turtle()
    ttt.speed(0)
    cols = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'cyan']
    followPath(ttt, "JJJ R JJJ L ignores the rest fblrj", -100)
    for col in cols:
        ttt.color(col)
        followPath(ttt, "FLFRFR FLFRFR FLFRFR FLFRFR")
        followPath(ttt, "JJumpump JJumpump")
    ttt.color("white")
    followPath(ttt, "JJ L JJJ R", -150)
    for d in range(10, 51, 5):
        followPath(ttt, "FFL-" * 8, d, 45)
    
    sss.exitonclick()

    
    print("    Two windows:")
    print("      First: rectangle drawn counterclockwise, with a smaller rectangle clockwise inside")
    print("      Second: Black background, 7 T shapes near top, nested octagons in lower middle")
    print("--------------------------------------")    
    input("Press a key to go on: ")

    

# ==========================================================================================
# Tests for drawRandSpiral

def testDrawRandSpiral():
    print("--------------------------------------")
    print("Testing drawRandSpiral:       CHECK VISUALLY")
    
    wn1 = turtle.Screen()
    tom = turtle.Turtle()
    tom.speed(0)
    tom.color("purple")
    drawRandSpiral(tom, 25, 90)
    wn1.exitonclick()
    
    wn1 = turtle.Screen()
    harry = turtle.Turtle()
    harry.speed(0)
    harry.color("sea green")
    harry.up()
    harry.goto(-200, 200)
    harry.down()
    drawRandSpiral(harry, 16, 70, 10)
    harry.up()
    harry.goto(200, 200)
    harry.down()
    drawRandSpiral(harry, 16, 110, 20)
    harry.up()
    harry.goto(-200, -200)
    harry.down()
    drawRandSpiral(harry, 16, 90)
    harry.up()
    harry.goto(200, -200)
    harry.down()
    drawRandSpiral(harry, 16, 45, 15)
    wn1.exitonclick()
    
    print("    Two windows:")
    print("      First: purple square random spiral")
    print("      Second: a smaller spiral in each of four corners, matching the four in the assignment")
    print("--------------------------------------")    
    input("Press a key to go on: ")


    


# Remove the # from the following lines to run the tests for each problem
#testfilterInRange()
#testRaindrop()
#testLetItRain()

   



# ========================================================================



runTests()