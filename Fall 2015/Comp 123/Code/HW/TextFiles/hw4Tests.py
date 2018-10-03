
# If your code is saved in a file called something other than hw8Code, change
# the module name below to match your filename

from hw4Code import *

import math



# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    testPigLatin()
    testMakeUnique()
    testCountCapitalWords()
    testConnectTheDots()
    x = input("done")
    print(x)
    print("DONE WITH ALL TESTS.")


# ========================================================================
# Tests for pigLatin

def testPigLatin():
    print("--------------------------------------")
    print("Testing pigLatin:")
    
    allOk = True

    # This will only print a message if the answer is wrong
    w1 = pigLatin('cat')
    if w1 != 'atcay':
        print("Called: pigLatin('cat')")
        print("Expected result", 'atcay', 'but actual result was', w1)
        allOk = False
    w2 = pigLatin('dog')
    if w2 != 'ogday':
        print("Called: pigLatin('dog')")
        print("Expected result", 'ogday', 'but actual result was', w2)
        allOk = False
    w3 = pigLatin('sprite')
    if w3 != 'itespray':
        print("Called: pigLatin('sprite')")
        print("Expected result", 'itespray', 'but actual result was', w3)
        allOk = False
    w4 = pigLatin('airplane')
    if w4 != 'airplaneway':
        print("Called: pigLatin('airplane')")
        print("Expected result", 'airplaneway', 'but actual result was', w4)
        allOk = False
    w5 = pigLatin('import')
    if w5 != 'importway':
        print("Called: pigLatin('import')")
        print("Expected result", 'importway', 'but actual result was', w5)
        allOk = False
    w6 = pigLatin('nymph')
    if w6 != 'nymphway':
        print("Called: pigLatin('nymph')")
        print("Expected result", 'nymphway', 'but actual result was', w6)
        allOk = False
    w7 = pigLatin('psst')
    if w7 != 'psstway':
        print("Called: pigLatin('psst')")
        print("Expected result", 'psstway', 'but actual result was', w7)
        allOk = False
    w8 = pigLatin('yurt')
    if w8 != 'urtyay':
        print("Called: pigLatin('yurt')")
        print("Expected result", 'urtyay', 'but actual result was', w8)
        allOk = False


    if allOk:
        print("pigLatin passed all tests!")
    print("--------------------------------------")
    input("Press a key to go on: ")
    

    

# ========================================================================
# Test for makeUnique

def testMakeUnique():
    print("--------------------------------------")
    print("Testing uniqueValues:")
    
    allOk = True
    

    # This will only print a message if the answer is wrong
    lst1 = [5, 1, 6, 1, 2, 6, 3, 4, 1, 6, 9]
    makeUnique(lst1)
    right1 = [1, 2, 3, 4, 5, 6, 9]
    if lst1 != right1:
        print("Called makeUnique(lst1)")
        print("Expected lst1 =", right1, "but lst1 =", lst1)
        allOk = False       
    lst2 = []
    makeUnique(lst2)
    right2 = []
    if lst2 != right2:
        print("Called makeUnique(lst2)")
        print("Expected lst2 =", right2, "but lst2 =", lst2)
        allOk = False       
    lst3 = [3828]
    makeUnique(lst3)
    right3 = [3828]
    if lst3 != right3:
        print("Called makeUnique(lst3)")
        print("Expected lst3 =", right3, "but lst3 =", lst3)
        allOk = False       
    lst4 = [100, 99, 98, 97, 96, 95]
    makeUnique(lst4)
    right4 = [95, 96, 97, 98, 99, 100]
    if lst4 != right4:
        print("Called makeUnique(lst4)")
        print("Expected lst4 =", right4, "but lst4 =", lst4)
        allOk = False       
    lst5 = [50, 50, 50, 50, 50, 50, 50, 50]
    makeUnique(lst5)
    right5 = [50]
    if lst5 != right5:
        print("Called makeUnique(lst5)")
        print("Expected lst5 =", right5, "but lst5 =", lst5)
        allOk = False       
    

    if allOk:
        print("makeUnique passed all tests!")
    print("--------------------------------------")
    input("Press a key to go on: ")
    



# ========================================================================
# Tests for countCapitals

def testCountCapitalWords():
    print("--------------------------------------")
    print("Testing countCapitalWords:")
    
    allOk = True
    
    
    def tester(filename, expectedDict):
        actualDict = countCapitalWords(filename)
        if actualDict != expectedDict:
            print("Called: countCapitalWords(" + filename + ")")
            print("Expected:")
            for k in expectedDict:
                print("   ", k, expectedDict[k])
            print("But function returned:")
            for k in actualDict:
                print("   ", k, actualDict[k])
            return False
        else:
            return True
        
    # Only prints a message if a call fails
    
    expAlice = {'Alice': 2}
    allOk = allOk and tester("TextFiles/alice.txt", expAlice)

    expLadle = {'LADLE': 1, 'Rotten': 10, 'Soda': 1, 'Dun': 3, 'Hut': 9, 'WANTS': 1,
                'Wan': 1, 'Shaker': 1, 'Comb': 1, 'Yonder': 1, 'Tick': 1, 'Disk': 1,
                'O': 5, 'Hoe-cake': 1, 'A': 3, 'TERM': 1, 'LIFT': 1, 'PAWN': 1,
                'Den': 1, 'Daze': 1, 'Battered': 2, 'Inner': 2, 'DARE': 1, 'MURAL': 1,
                'Ladle': 10, 'Heifer': 1, "Grammar's": 1, 'HOE': 1, 'GULL': 1,
                "Hut's": 1, 'Water': 1, 'Grammar': 3, 'Putty': 1, 'Rat': 10,
                'Armor': 2, 'Wail': 1, 'Honor': 1, 'Wares': 1, 'Evanescent': 1,
                'Oil': 3, 'WORSTED': 1}
    allOk = allOk and tester("TextFiles/ladlerat.txt", expLadle)



    
    if allOk:
        print("countCapitalWords passed all tests!")
    print("--------------------------------------")       




# ========================================================================
# Tests for connectTheDots

def testConnectTheDots():
    print("--------------------------------------")
    print("Testing connectTheDots:   Check results visually!")
    
    
    connectTheDots([(-200, 0), (0, -200), (200, 0), (0, 200), (-200, 0),
                    (-100, 100), (-100, -100), (100, -100), (100, 100), (-100, 100)],
                   "red")
    
    sqrt3 = math.sqrt(3)
    sqrt2 = math.sqrt(2)
    circlePoints = [(-1, 0), (-sqrt3/2, -1/2), (-sqrt2/2, -sqrt2/2), (-1/2, -sqrt3/2),
                    (0, -1), (1/2, -sqrt3/2), (sqrt2/2, -sqrt2/2), (sqrt3/2, -1/2),
                    (1, 0), (sqrt3/2, 1/2), (sqrt2/2, sqrt2/2), (1/2, sqrt3/2),
                    (0, 1), (-1/2, sqrt3/2), (-sqrt2/2, sqrt2/2), (-sqrt3/2, 1/2),
                    (-1, 0)]
    head = [(200 * pt[0], 200 * pt[1]) for pt in circlePoints]
    eyes = [(-100, 100), (-130, 100), (-130, 70), (-100, 70), (-100, 100),
            (100, 100), (130, 100), (130, 70), (100, 70), (100, 100)]
    smile = [(100, -70), (0, -140), (-100, -70)]
    face = head + eyes + smile
    connectTheDots(face)
    sinList = [(x, 20 * math.sin(x / 5)) for x in range(-250, 251, 1)]
    connectTheDots(sinList, "green")

    
    print("    Three windows:")
    print("      First: draws a red diamond with a square inside it.")
    print("      Second: draws a smiley face.")
    print("      Third: draws a green sine wave.")
    print("--------------------------------------")    
    input("Press a key to go on: ")

    
    print("--------------------------------------")       



# ========================================================================



runTests()




