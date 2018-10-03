"""
----------------------------------------------------------------------
Homework 4 code
<your name here>
----------------------------------------------------------------------
"""


import math
import turtle
import time

# ----------------------------------------------------------------------
# Question 1
# interleave

def interleave(lst1, lst2):
    """Takes in two lists, and builds a new list as its value. The new list
    has the elements from the two input lists, alternating. Any leftover
    values if one list is longer than the other are appended at the end."""
    if len(lst1) == 0:
        return lst2[:]
    elif len(lst2) == 0:
        return lst1[:]
    else:
        myAns = interleave(lst1[1:], lst2[1:])
        return [lst1[0], lst2[0]] + myAns


# Draw happy robots for interleave(['a', 'b', 'c'], [6, 8, 10, 12]) =>
          #interleave(['a','b','c'], [6,8,10,12] ) =>
               #interleave(['b','c'],[8,10,12]) =>
                     #interleave(['c'],[10,12]) =>
                            #interleave([],[12]) =>
                        #myAns = [12]    <=
                    #myAns = ['c',10,12] <= 
              #myAns = ['b',8,'c',10,12] <=
        #myAns = ['a',6,'b',8,'c',10,12] <=



# ----------------------------------------------------------------------
# Question 2
# isPalindrome

# debug isPalindrome below


def isPalindrome(strng):
    """Takes in a string and returns True if the string is a palindrome, and
    false otherwise. For simplicity, this string must be an exact palindrome.
    This function will return false if given a string that is a palindrome
    only if you ignore spacing, capitalization, and punctuation. Hence: "able
    was i ere i saw elba" will be seen as a palindrome, but "Madam, I'm
    Adam!" will not be seen as a palindrome by this function."""
    length = len(strng)
    if length <= 1: #should be <= because 1 char strings are palindromes
        return True#should return and not print
    elif strng[0] != strng[-1]:
        return False
    else:
        return isPalindrome(strng[1:length-1])#should be len-1 because the fucntion should take the second character to the second to last character each time
 
 

def isPalindromeAlt(strng):
    if strng[::-1].lower() == strng.lower():
        return True
    else:
        return False


# ----------------------------------------------------------------------
# Question 3
# Koch Curve

# put your definition of kochCurve here
def kochCurve(koch, dist, reps):
    """takes a turtle, distance and the recurring number of reps
    the last rep (base case) just draws a line
    while reps is greater than one, draws a single segment of the koch curve by calling the function"""
    tDis = dist/3
    if reps <= 1:
        koch.fd(dist)
    elif dist < 1:
        print("dist too short")
        return None
    elif reps > 1:
        kochCurve(koch,tDis,reps-1);koch.left(60); kochCurve(koch,tDis,reps-1);koch.right(120); kochCurve(koch,tDis,reps-1);koch.left(60); kochCurve(koch,tDis,reps-1)

    



        
def runKochCurve(startReps, endReps):
    """Tests the Koch curve function from the starting number
    of repetitions input up to but not including the endReps number
    of repetitions. It pauses for 2 seconds between each curve."""
    s = turtle.Screen()
    drawt = turtle.Turtle()
    labelt = turtle.Turtle()
    for r in range(startReps, endReps):
        drawt.reset()
        labelt.reset()
        drawt.speed(0)
        labelt.speed(0)
        labelt.hideturtle()
        labelt.up()
        labelt.goto(-100, 300)
        labelt.write("Koch curve, reps = " + str(r), font = ("Arial", 16, "bold"))
        drawt.up()
        drawt.backward(300)
        drawt.down()
        
        kochCurve(drawt, 600, r)
        
        time.sleep(2.0)
    
    s.exitonclick()
    

    
    
# ----------------------------------------------------------------------
# Question 3 EXTRA CREDIT!!
# Koch polygon

# put your definition of kochPolygon here



def runKochPoly(sides, sideLen, startReps, endReps):
    """Takes in parameters to specify the size of the polygon (number of
    sides and side length) and also the starting and ending number of
    recursive repetitions, and it repeatedly draws the Koch polygon for each
    number of reps from startReps up to but not including the endReps number
    of repetitions."""
    s = turtle.Screen()
    drawt = turtle.Turtle()
    labelt = turtle.Turtle()
    for r in range(startReps, endReps):
        drawt.reset()
        labelt.reset()
        drawt.speed(0)
        labelt.speed(0)
        labelt.hideturtle()
        labelt.up()
        labelt.goto(-200, 300)
        labelt.write("Koch polygon, sides = " + str(sides) + ", reps = " + str(r), font = ("Arial", 16, "bold"))
        drawt.up()
        drawt.goto(-(sideLen / 2), 100)
        drawt.down()
        
        kochPolygon(drawt, sides, sideLen, r)
        
        time.sleep(2.0)
    s.bgcolor("lightsalmon")
    s.exitonclick()


# ----------------------------------------------------------------------
# Question 5
# Dragon of Eve

# put your definition of dragonOfEve here
def dragonOfEve(t, dist,reps):
    """Takes a turtle, distance and the recurring number of repetitions
    and then draws one iteration of the dragon of eve fractal, 
    calling itself to draw the individual segments of the fractal"""
    if reps <= 1:
        t.fd(dist)
    elif dist < 1:
        print("dist too short")
        return None
    else:
        dist2 = dist/(math.sqrt(2))
        t.left(90)
        dragonOfEve(t,dist/2,reps-1)

        t.right(135)

        dragonOfEve(t,dist2,reps-1)

        t.pu(); t.left(45)
        t.fd(dist/2)
        
        t.pd();t.right(180)
        dragonOfEve(t,dist/2,reps-1)
        
        t.pu(); t.left(180); t.fd(dist/2);t.pd()
        
        

def runDragonOfEve(startR, endR):
    """Takes two inputs, the starting number of recursive levels and the
    ending number of recursive levels, and it draws the Dragon of Eve fractal
    for each rep value, sleeping for 2 seconds between the end of one and the 
    start of the next."""
    s = turtle.Screen()
    drawt = turtle.Turtle()
    labelt = turtle.Turtle()
    for r in range(startR, endR):
        drawt.reset()
        labelt.reset()
        drawt.speed(0)
        labelt.speed(0)
        labelt.hideturtle()
        labelt.up()
        labelt.goto(-100, 300)
        labelt.write("Dragon of Eve, reps = " + str(r), font = ("Arial", 16, "bold"))
        drawt.up()
        drawt.backward(150)
        drawt.down()
        
        dragonOfEve(drawt, 300, r)
        
        time.sleep(2.0)
    s.bgcolor("lightsalmon")
    s.exitonclick()

#runDragonOfEve(15,16)