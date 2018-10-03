
# Change the filename below to match your solution file's name

from hw2Code import *


import turtle


# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    #testStarOutline()
    testDrawStairs()
    print("DONE WITH ALL TESTS.")



# ==========================================================================================
# Tests for starOutline

def testStarOutline():
    """Testing program for the starOutline program"""
    
    print("--------------------------------------")
    print("Testing starOutline:         CHECK VISUALLY")
    
    gridOfStars()
    spiralOfStars(5)
    spiralOfStars(15)

    win1 = turtle.Screen()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t2.up()
    t2.goto(-250, 0)
    t2.color('red')
    t2.down()
    starOutline(t1, 50)
    starOutline(t2, 90)
    win1.exitonclick()
    
    print("    Four windows:")
    print("      First: grid of star shapes")
    print("      Second: spiral of star shapes with angle 5")
    print("      Third: spiral of star shapes with angle 25")
    print("      Fourth: two star shapes, small back one in middle, large red one to left.")
    print("--------------------------------------")    
    input("Hit return/enter to go on.")




# ==========================================================================================
# Tests for drawStairs

def testDrawStairs():
    """Testing program for the drawStairs function."""
    
    print("--------------------------------------")
    print("Testing drawStairs:                  CHECK VISUALLY")
    
    
    win1 = turtle.Screen()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.speed(0)
    t2.speed(0)
    t1.color('green')
    t2.color('blue')
    t2.up()
    t2.goto(-200, 0)
    t2.setheading(90)
    t2.down()
    drawStairs(t1, 10, 15)
    drawStairs(t2, 3, 50)
    t1.up()
    t1.goto(200, 0)
    t1.setheading(0)
    t1.color('yellow')
    t1.down()
    drawStairs(t1, 1, 20)
    win1.exitonclick()

    rainbowStairs()
    
    print("    Two windows:")
    print("        First: Should show three stairs, on the left a blue upside-down one")
    print("               with 3 steps, in the middle a green one, and a one-step yellow")
    print("               one on the right (just a square)")
    print("        Second: Should show a spiral of stairs, five steps each, in rainbow colors")
    print("--------------------------------------")    
    input("Hit return/enter to go on.")
        


def rainbowStairs():
    """Takes in no inputs, and displays a turtle graphics screen. The turtle
    in it draws rotated stair shapes in a grid"""
    scr = turtle.Screen()
    ted = turtle.Turtle()
    ted.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for currColor in colors:
        ted.up()
        ted.color(currColor)
        ted.down()
        drawStairs(ted, 5, 30)
        ted.left(60)
    scr.exitonclick()


# Always runs the runTests function
runTests()