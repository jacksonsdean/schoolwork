
def printEveryOther(i):
    """One input x: must be an integer >= 0. Prints every other value from x down to zero"""
    while i >= 0:    
        print(i)
        i = i - 5
    print("Done!")
    
def squareUserNums():
  userInp = input("Enter the next number (negative to quit): ")
  userNum = int(userInp)
  while userNum >= 0:
    print(userNum, "squared is", userNum ** 2)
    userInp = input("Enter the next number (negative to quit): ")
    userNum = int(userInp)
    #Omitting these lines causes an infinite loop because there is nothing in the while loop body to break the loop
    
def sumToN(topNum):
  """Takes in a number and computes and returns the sum of the numbers
  from zero to the input number."""
  currVal = 0   # the loop variable
  total = 0    # the accumulator variable
  while currVal < topNum:
    total = total + currVal # add next value to accumulator
    currVal = currVal + 1  # update the loop variable
    print("total:", total)
    print("currVal:",currVal)
  return total

def addUserNums():
    sum = 0
    uInp = int(input("Enter a number to add:"))
    while uInp >= 0:
        sum = sum + uInp
        print("New sum:", sum)
        uInp = int(input("Enter a number to add:"))
        

def squareUserNums2():  
  while True:
    userInp = input("Enter the next number (negative to quit): ")
    userNum = int(userInp)      
    if userNum < 0:
        break
    print(userNum, "squared is", userNum ** 2)
    

    
def main():
    printEveryOther(51)
    squareUserNums()
    sumToN(60)
    addUserNums()
    squareUserNums2()
main()
    
    

