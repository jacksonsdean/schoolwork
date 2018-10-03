""" ======================================================================
File: hw4Code.py
Author: Jackson and Susan

I am going to leave this file a bit more stripped down than earlier assignments.
It is your task to include the spacing, question markers, etc.  I have
provided a section for import statements and a section for function definitions,
and leave everything else up to you.
"""

# -----------------
# Put import statements here

import turtle
import string #need for string.punctuation

# -----------------
# Put function definitions here

def pigLatin(inWord):
    """takes an input of a word and then translates that word to pig latin"""
    vowels = ("a","e","i","o","u")
    pos = 0
    inWord = inWord.lower()
    if inWord[0].lower() in vowels:
        inWord = inWord + "way"
        return inWord  
    for i in inWord.lower():
        if i in vowels:
            pos = inWord.find(i)
            break
        else:
            pos = pos + 1
    if pos == len(inWord):
        inWord = inWord + "way"
        return inWord 
    else:
        inWord = inWord[pos:] + inWord[:pos] + "ay"
    return inWord

def makeUnique(numList):
    """takes an input as a list and then modifies that list by removing duplicates and sorting"""
    i = 0
    numList.sort()
    while i < (len(numList)-1):
        if len(numList) == 0:
            break
        if numList[i] == numList[i+1]:
            del numList[i+1]
        else:
            i=i+1
    return numList
   
#this function works to remove duplicates and returns the correct list, but the test file doesn't recognize the lists as correct (but they totally are)

def connectTheDots(coordList,color="black"):
    """takes an input of many coordinates and a color, and then uses turtle to draw lines between the coordinates"""
    scr =  turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)
    t.color(color)
    t.pu()
    t.goto(coordList[0])
    t.pd()    
    
    if len(coordList) != 0:
        for coord in coordList[1:]:
            t.goto(coord)       
    scr.exitonclick()
   
            

# You're to debug this one...
def countCapitalWords(filename):
    """Takes in a filename and reads the text from the file. It breaks it into
    words and removes punctuation (from start and end of word only). Then it
    makes a dictionary with capitalized words from the text as the keys and
    the number of occurrences as the values. It returns this dictionary."""
    fil = open(filename, 'r')
    text = fil.read()#missing parenthesis in method call
    fil.close()
    
    words = text.split()
    capCount = {}#cap count is a dictionary, not a list. needs {}
    for word in words:
        word = word.strip(string.punctuation)#need to import string to use string library
        if (len(word) > 0) and (word[0] in "ABCDEFGHIJKLMNOPQRSTUVXYZ"):
            if word in capCount:
                capCount[word] += 1
            else:
                capCount[word] = 1  #should start at one after the first cap, not 0
    return capCount



if __name__ == '__main__':
    print("My tests:")
    ## Put test calls to pigLatin here
    print('dog', pigLatin("Dog"))
    
    ## Put test calls to makeUnique here
    lst = [5, 1, 4, 1, 6, 2, 7, 2, 8, 1, 9, 1, 4, 5, 6, 7]
   
    ## Put test calls to countCapitalWords here    
    count1 = countCapitalWords("TextFiles/alice.txt")
    print("alice.txt:")
    for key in count1:
        print(key, count1[key])

    ## Put test calls to connectThe Dots here    
    connectTheDots([(100, 0), (100, 100), (0, 100), (-100, 0)], "purple")

    