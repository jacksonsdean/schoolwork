

def everyOther(list1):
    """takes a list as an input and returns a new list with every other value from first list"""
    list2 = list1[0::2]
    return list2

print("every other:",everyOther([1,2,3,4,5,6]))

def listAddOne(list1):
    """takes a list as an input and then adds one to each value in the list, building a new list and returning it"""
    list2 =[]
    n = 0
    for i in list1:        
        iValue = list1[n]
        newI = iValue + 1       
        list2.append(newI)
        n=n+1
    return list2
        
print("addOne:", listAddOne([1,2,3,4,5,6]))


def swapEnds(list1):
    """takes a list as an input, and then switches the first and last values"""
    list0v = list1[0]
    listEv = list1[-1]
    list1.remove(list1[0])
    list1.remove(list1[-1])
    list1.append(list0v)
    list1.insert(0,listEv)
    return list1
    
print("swapEnds:", swapEnds([1,2,3,4,5,6]))

def removeNegs(list1):
    """takes a list as an input and removes the negative values"""
    n=0
    while n < len(list1):
        if not list1[n] >= 0:
            list1.remove(list1[n])
        n=n+1
            
    return list1
    
    
    
print("removeNegs:",removeNegs([-2,-1,0,1,2,3,4]))

