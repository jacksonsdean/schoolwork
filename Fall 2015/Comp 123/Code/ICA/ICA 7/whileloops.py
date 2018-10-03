""" ==================================================
File: whileloops.py
Author: Susan Fox
Date:  Spring 2013

This file contains examples of while and for loops for the Iteration
activity.  """


# ====================================================
# Simple while loop examples


def printEveryOther(x):
    """One input x: must be an integer >= 0. Prints every other value from x down to zero"""
    while x >= 0:      # x is the loop variable
        print(x)
        x = x - 2
    # when indentation stops, while loop is over
    print("Done!")



def squareUserNums():
    """Reads in numbers from the user, stopping when the user
    enters a negative number. For each user number, it prints the
    number and the square of the number."""
    userInp = input("Enter the next number (negative to quit): ")
    userNum = int(userInp)
    while userNum >= 0:
        print(userNum, "squared is", userNum ** 2)
        userInp = input("Enter the next number (negative to quit): ")
        userNum = int(userInp)
        

 
        
def sumToN(topNum):
    """Takes in a number and computes and returns the sum of the numbers
    from zero to the input number."""
    currVal = 0  # loop variable
    total = 0    # accumulator variable
    while currVal <= topNum:
        total = total + currVal
        currVal = currVal + 3
    return total



def nextWord(text):
    """Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next sequence
    of characters up to a space, tab, or newline."""
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":
            break
        else:
            wordStr = wordStr + ch
    return wordStr



if __name__ == '__main__':
    print("------------------------------")
    print("Sample calls to printEveryOther:")
    print("printEveryOther(11) does:")
    printEveryOther(11)
    print("printEveryOther(4) does:")
    printEveryOther(4)

    print("------------------------------")
    print("Sample call to squareUserNums:")
    squareUserNums()

    print("------------------------------")
    print("Sample calls to sumToN:")
    print("sumToN(3) does:")
    print(sumToN(3))
    print("sumToN(100) does:")
    print(sumToN(100))
    
    print("------------------------------")
    print("Sample calls to nextWord:")
    print("nextWord('Friends, Romans, countrymen') does:")
    print(nextWord('Friends, Romans, countrymen'))
    print("nextWord('Bananas and apples') does:")
    print(nextWord('Bananas and apples'))
    print("nextWord('Frederick!') does:")
    print(nextWord('Frederick!'))


