"""
============================================================================
finalCode.py

This file will contain your answers for the "ordinary python" questions.
============================================================================
"""


import turtle
import math
import random


# ==========================================================================
# Question 1

# put your definition of containsI here
def containsI(lst):
    """takes a list as an input, builds a new list containing only strings in the first list that contain an 'i' or 'I'"""
    newlst = []
    for item in lst:
        if 'i' in item.lower():
            newlst = newlst+[item]
    return newlst



# ==========================================================================
# Question 2


# put your definition of coolSpiral1 here
def coolSpiral1(t, dist,reps):
    """Takes a turtle object, a dist and the number of reps and draws a cool sprial using those parameters"""
    addDist = dist
    for i in range(reps):
        t.fd(dist)
        t.right(89.5)
        dist +=addDist
    


# ==========================================================================
# Question 3


def findPosition(keyword, filename):
    """Takes in a string keyword and a filename, and it looks for the keyword in
    the text of the file. It returns a tuple, with the line number (starting with 1) and character
    number within the line (also starting with 1), of the start of the keyword."""
    fObj = open(filename, 'r')
    lineNum = 1
    for line in fObj:
        if keyword in line:
            pos = line.find(keyword)
            return(lineNum, pos) #Doesn't need to add one, 0 is the position of the first character 
        lineNum +=1 #Linenum counter should increase after the program reads every line
    fObj.close()
    return (-1, -1) # if word never found
    
 
    
# ==========================================================================
# Question 6

# Uncomment this when ready to work on it.

        
def keepPositives(numList):
    """Takes in a list of numbers, and recursively builds an answer list
    that contains only those number from the original that are greater than
    zero."""
    if len(numList) == 0: #== to compare, = to set
        return []
    elif numList[0] > 0:
        recResult = keepPositives(numList[1:])
        return [numList[0]] + recResult  #can't add a int and a list, numlist[0] needs to be made to a list
    else:
        recResult = keepPositives(numList[1:])#should omit only the first value in the list, because it has already been checked
        return recResult
 
        
    
if __name__ == '__main__':
    print("Go!")
    
    ## Question 1 test calls
    #res1 = containsI(['camel', 'chimp', 'lion', 'bear', 'penguin', 'moose'])
    #print(res1, "   should be    ", ['chimp', 'lion', 'penguin'])
    #res2 = containsI(['I', 'XV', 'VII', 'mmxv', 'iii'])
    #print(res2, "   should be    ", ['I', 'VII', 'iii'])
    #res3 = containsI(['apple', 'peach', 'lemon', 'cherry'])
    #print(res3, "   should be    ", ['apple', 'peach', 'lemon', 'cherry'])
    
    
    ## Question 2 test call
    #s = turtle.Screen()
    #tess = turtle.Turtle()
    #tess.speed(0)
    #coolSpiral1(tess, 2, 400)
    #s.exitonclick()
    
    ## Question 3 test calls
    #pos1 = findPosition("Anne", "TextFiles/persuasion.txt")
    #print("Anne occurs at", pos1, "in Persuasion.")
    #pos2 = findPosition("Ishmael", "TextFiles/mobydick.txt")
    #print("Ishmael occurs at", pos2, "in Moby Dick.")
    #pos3 = findPosition("bank", "TextFiles/alice.txt")
    #print("bank occurs at", pos3, "in Alice in Wonderland.")
    #pos4 = findPosition("Frederick", "TextFiles/alice.txt")
    #print("Frederick occurs at", pos4, "in Alice... in other words, it isn't there")
 
 
     ## Question 6 test calls
    #res1 = keepPositives([1, -2, 3, -4, 5])
    #print(res1, "  should be  ", [1, 3, 5])
    #res2 = keepPositives([-2, -4, -6])
    #print(res2, "  should be  ", [])
    #res3 = keepPositives([5832])
    #print(res3, "  should be  ", [5832])
    
    