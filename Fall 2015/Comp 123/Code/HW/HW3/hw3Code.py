# ====================================================================
#
#  Homework 3 solutions
#  Jackson
# ====================================================================


import turtle
import random


# ==============================================================
# Question 1

#definition of filterInRange:

def filterInRange(low, high, numList):
    """takes inputs of high/low limits and a list, and then builds a new list consisting of only the numbers between the limits""" 
    numList2=[]
    for num in numList:
        if low <= num <= high:
            numList2.append(num)  
    return numList2

# ==============================================================
# Question 2
def countEvens(numList):
    """Takes in a list of numbers. It counts how many numbers in the list are
    even numbers, and returns that value at the end."""
    if type(numList) == list:
        count = 0
        for num in numList:
            if type(num) not in (int, float):
                print("Value in list expected to be a number, but was ", str(type(num)))
                return "ERROR"
            elif num % 2 == 0:
                count += 1
        return count
    else:
        print("Expected input to be a list, but it was actually " + str(type(numList)))
        return "ERROR"
    

def testCountEvens():
    """a test function to determine if countEvens() does what it should in all instances"""
    allOk = True
    # Test 1 some values are positive
    retCount = countEvens([1, 3, 8, 12, 13, 17, 19])
    if retCount != 2:
        print("Called: countEvens([1, 3, 8, 12, 13, 17, 19])")
        print("Expected:", 2,"   but function returned:", retCount)
        allOk = False
    # Test 2 some values are negative
    retCount = countEvens([5, 0, -2, 23, -5, 41, 2, 10])
    if retCount != 4:
        print("Called: countEvens([5, 0, -2, 23, -5, 41, 2, 10])")
        print("Expected:", 4, "   but function returned:", retCount)
        allOk = False
    # Test 3 values are in increasing order
    retCount = countEvens([1, 3, 8, 12, 13, 17, 19])
    if retCount != 2:
        print("Called: countEvens([1, 3, 8, 12, 13, 17, 19])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False
    # Test 4 values are in random order
    retCount = countEvens([-10, 15, 2, 17, 25, 7, 3])
    if retCount != 2:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False
    # Test 5 values are in decreasing order
    retCount = countEvens([100, 45, 17, 8, 3])
    if retCount != 2:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False 
    # Test 6 some values are floating-point
    retCount = countEvens([100.0, 45, 17.1, 8, 3])
    if retCount != 2:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False 
    # Test 7 some values are integers
    retCount = countEvens([100.0, 45, 17.1, 8, 3])
    if retCount != 2:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False     
    # Test 8 all values are even
    retCount = countEvens([2,4,6,8,10])
    if retCount != 5:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 5, "   but function returned:", retCount)
        allOk = False     
    # Test 9 all values are odd
    retCount = countEvens([1,3,5,7,9])
    if retCount != 0:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 0, "   but function returned:", retCount)
        allOk = False     
    # Test 10 some values are even and some are odd
    retCount = countEvens([1,2,3,4,5,6,7,8])
    if retCount != 4:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 4, "   but function returned:", retCount)
        allOk = False  
    # Test 11 the first value is even
    retCount = countEvens([2,3,4,5,6,7,8])
    if retCount != 4:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 4, "   but function returned:", retCount)
        allOk = False  
    # Test 12 the last value is even
    retCount = countEvens([2,3,4,5,6,7,8])
    if retCount != 4:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 4, "   but function returned:", retCount)
        allOk = False          
    # Test 13 the list has only one value
    retCount = countEvens([2])
    if retCount != 1:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 1, "   but function returned:", retCount)
        allOk = False   
    # Test 14 the list has more than one value
    retCount = countEvens([2,3,4])
    if retCount != 2:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 2, "   but function returned:", retCount)
        allOk = False    
    # Test 15 the list has no values
    retCount = countEvens([])
    if retCount != 0:
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", 0, "   but function returned:", retCount)
        allOk = False 
    # Test 16 the input is not a list
    retCount = countEvens("not a list")
    if retCount != "ERROR":
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", "ERROR", "   but function returned:", retCount)
        allOk = False 
    # Test 17 the input list contains a non-list as a value
    retCount = countEvens([1,"two",3,4,5])
    if retCount != "ERROR":
        print("Called: countEvens([-10, -15, -20, -25, 25, 30, 50])")
        print("Expected:", "ERROR", "   but function returned:", retCount)
        allOk = False     

    print()
    if allOk:
        print("countEvens PASSED ALL TESTS!")
    else:
        print("countEvens FAILED ONE OR MORE TEST!")
    print("--------------------------------------") 
    input("Press a key to go on: ")
       
    
# ==============================================================
# Question 3

#definition of followPath:

def followPath(t,s,d=20,a=90):
    """a function that takes the inputs of turtle, string, distance and angle and then uses the inputed string to move the turtle on a given path."""
    for ch in s:
        if ch == "F":
            t.fd(d)
        elif ch =="B":
            t.fd(-d)
        elif ch == "J":
            t.pu()
            t.fd(d)
            t.pd()
        elif ch == "R":
            t.right(a)
        elif ch == "L":
            t.left(a)
        else:
            ch = ch



    
    


# ==============================================================
# Question 4

#definition of drawRandSpiral:

def drawRandSpiral (t, numE, a, maxChange=10):
    """this function takes the inputs of turtle, number of edges, angle and max change and creates a random spiral with the inputs"""
    changeList = [5,maxChange,5]
    #for i in range(numE):
        
    change = changeList[0]
    for i in range(numE):
        t.fd(change)
        t.left(a)
        change = change + random.choice(changeList)
        print(change)        

# --------------------------------------------------------------------
# Script with calls to functions


if __name__ == '__main__':
    # Calls for question 1
    nums1 = [1, 3, 8, 12, 13, 17, 19, 22, 25]
    ans1 = filterInRange(10, 20, nums1)
    print("ans1 =", ans1)
    nums2 = [5, 0, -2, 23, -5, 41, 2]
    ans2 = filterInRange(0, 10, nums2)
    print("ans2 =", ans2)
    
    # Calls for question 2
    testCountEvens()
    
    #Calls for question 3
    wn = turtle.Screen()
    amy = turtle.Turtle()
    followPath(amy, "FFFFLL FFRR FFFFRR FFLL FFFFLL L FFFFFFF L FF L FFFFFFF LLL", 20, 45)
    wn.exitonclick()
    
    #Calls for question 4
    wn = turtle.Screen()
    beth = turtle.Turtle()
    drawRandSpiral(beth, 30, 90)
    wn.exitonclick()