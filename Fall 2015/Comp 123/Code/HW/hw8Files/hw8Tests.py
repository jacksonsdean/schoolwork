"""
----------------------------------------------------------------------
Homework 8 testing file

Includes functions to test each program in Homework 4.
----------------------------------------------------------------------
"""

import turtle

from hw8Code import *



# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    #testInterleave()
    #testIsPalindrome()
    #testKochCurve()
    #testKochPolygon()
    testDragonOfEve()
    print("DONE WITH ALL TESTS.")





# ========================================================================
# Tests for interleave

def testInterleave():
    print("--------------------------------------")
    print("Testing interleave:")

    allOk = True

    # Test 1
    r1 = interleave(['a', 'b', 'c'], [1, 3, 5, 7])
    correct1 = ['a', 1, 'b', 3, 'c', 5, 7]
    if r1 != correct1:
        print("Called: interleave(['a', 'b', 'c'], [1, 3, 5, 7])")
        print("Expected result", correct1, "but actual result was", r1)
        allOk = False
    
    # Test 2
    r2 = interleave([1, 2, 3], [4, 5]) 
    correct2 = [1, 4, 2, 5, 3]
    if r2 != correct2:
        print("Called: interleave([1, 2, 3], [4, 5])")
        print("Expected result", correct2, "but actual result was", r2)
        allOk = False

    # Test 3
    r3 = interleave([], ["happy", "day"])
    correct3 = ['happy', 'day']
    if r3 != correct3:
        print("Called: interleave([] ['happy', 'day'])")
        print("Expected result", correct3, "but actual result was", r3)
        allOk = False

    # Test 4
    r4 = interleave([55, 66], [])
    correct4 = [55, 66]
    if r4 != correct4:
        print("Called: interleave([55, 66] [])")
        print("Expected result", correct4, "but actual result was", r4)
        allOk = False
            

    if allOk:
        print()
        print("interleave passed all tests!")

    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")




# ========================================================================
# Tests for isPalindrome

def testIsPalindrome():
    print("--------------------------------------")
    print("Testing isPalindrome:")

    allOk = True

    # Test 1
    r1 = isPalindrome('Foobar')
    if r1 != False:
        print("Called: isPalindrome('Foobar')")
        print("Expected result", False, "but actual result was", r1)
        allOk = False
   
    # Test 2
    r2 = isPalindrome('madam')
    if r2 != True:
        print("Called: isPalindrome('madam')")
        print("Expected result", True, "but actual result was", r2)
        allOk = False

    # Test 3
    r3 = isPalindrome('amanaplanacanalpanama')
    if r3 != True:
        print("Called: isPalindrome('amanaplanacanalpanama')")
        print("Expected result", True, "but actual result was", r3)
        allOk = False

    # Test 4
    r4 = isPalindrome('')
    if r4 != True:
        print("Called: isPalindrome('')")
        print("Expected result", True, "but actual result was", r4)
        allOk = False
            
    # Test 5
    r5 = isPalindrome('AAAAAA')
    if r5 != True:
        print("Called: isPalindrome('AAAAAA')")
        print("Expected result", True, "but actual result was", r5)
        allOk = False
        
    # Test 6
    r6 = isPalindrome('banana ananana')
    if r6 != False:
        print("Called: isPalindrome('banana ananana')")
        print("Expected result", False, "but actual result was", r6)
        allOk = False

    # Test 7
    r7 = isPalindrome('x')
    if r7 != True:
        print("Called: isPalindrome('x')")
        print("Expected result", True, "but actual result was", r7)
        allOk = False

    # Test 8
    r8 = isPalindrome('by')
    if r8 != False:
        print("Called: isPalindrome('by')")
        print("Expected result", False, "but actual result was", r8)
        allOk = False

    if allOk:
        print("isPalindrome passed all tests!")

    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")



# ========================================================================
# Tests for kochCurve

def testKochCurve():
    print("--------------------------------------")
    print("Testing kochCurve:       CHECK VISUALLY")

    s = turtle.Screen()
    drawt = turtle.Turtle()
    labelt = turtle.Turtle()
    for r in range(1, 7):
        drawt.reset()
        labelt.reset()
        drawt.speed(0)
        labelt.speed(0)
        labelt.hideturtle()
        labelt.up()
        labelt.goto(100, 300)
        labelt.write("Koch curve, reps = " + str(r), font = ("Arial", 16, "bold"))
        drawt.up()
        drawt.goto(-300, 300)
        drawt.right(45)
        drawt.down()
        
        kochCurve(drawt, 700, r)
        
        time.sleep(2.0)
    s.bgcolor("lightsalmon")
    s.exitonclick()

    print("    One window, reset 6 times:")
    print("      1. straight line diagonally from upper left")
    print("      2. level 2 Koch curve diagonally from upper left")
    print("      3. level 3 Koch curve diagonally from upper left")
    print("      4. level 4 Koch curve diagonally from upper left")
    print("      5. level 5 Koch curve diagonally from upper left")
    print("      6. level 6 Koch curve diagonally from upper left")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")



# ========================================================================
# Tests for kochPolygon

def testKochPolygon():
    print("--------------------------------------")
    print("Testing kochPolygon:       CHECK VISUALLY")

    runKochPoly(3, 300, 1, 5)
    runKochPoly(4, 100, 5, 6)
    runKochPoly(8, 100, 2, 5)
    runKochPoly(2, 400, 1, 5)
    print("    Four windows:")
    print("      1. Big triangle levels 1 through 4")
    print("      2. Smallish square level 5")
    print("      3. Octagon with 100 sides, levels 2 through 4")
    print("      4. Two-sided line, long, levels 1 through 4")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")



# ========================================================================
# Tests for dragonOfEve

def testDragonOfEve():
    print("--------------------------------------")
    print("Testing dragonOfEve:       CHECK VISUALLY")
    s = turtle.Screen()
    drawt = turtle.Turtle()
    labelt = turtle.Turtle()
    for r in range(1, 7):
        drawt.reset()
        labelt.reset()
        drawt.speed(0)
        labelt.speed(0)
        labelt.hideturtle()
        labelt.up()
        labelt.goto(100, 300)
        labelt.write("Dragon of Eve, reps = " + str(r), font = ("Arial", 16, "bold"))
        drawt.up()
        drawt.goto(-150, -150)
        drawt.left(45)
        drawt.down()
        
        dragonOfEve(drawt, 300, r)
        
        time.sleep(2.0)
    s.bgcolor('lightgreen')
    s.exitonclick()
    print("    One windows, reset 6 times")
    print("      1. Dragon of Eve, level 1, diagonal from lower left")
    print("      2. Dragon of Eve, level 2, diagonal from lower left")
    print("      3. Dragon of Eve, level 3, diagonal from lower left")
    print("      4. Dragon of Eve, level 4, diagonal from lower left")
    print("      5. Dragon of Eve, level 5, diagonal from lower left")
    print("      6. Dragon of Eve, level 6, diagonal from lower left")
    print("--------------------------------------")    
    inp = input("Ready to go on? Type a key: ")


    

# ========================================================================



runTests()