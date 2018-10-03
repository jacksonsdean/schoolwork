import math

def smallestDiff(x, y, z):
    print('smallestDiff inputs:', x, y, z) 
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    minDiff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', minDiff)
    return minDiff
smallestDiff(32,43,90)

# Local environment smallestDiff
#    x        32
#    y        43
#    z        90
#    diff1    11
#    diff2    47
#    diff3    58
#    minDiff  11

def addTax(price, taxRate):
    print("addTax inputs:", price, taxRate)
    taxAmt = price * taxRate
    print("return value:",price+taxAmt)
    return price + taxAmt
addTax(25.99,0.0725)

# Local environment addTax
#    price    25.99
#    taxRate  0.0725
#    taxAmt   1.884275


def fireStations(widEW, widNS):
    cityArea = widEW * widNS
    stations = cityArea / 5
    return math.ceil(stations)

print("St. Paul Firestations:",fireStations(11,8.5))
print("Northfield Firestations:",fireStations(3,4))
print("Rochester Firestations:",fireStations(10,12.5))

def ave3(x,y,z):   
    average = (x + y + z)/3
    print("Average of", x,",",y,"and",z,"=",average)
    return average
ave3(2,3.0,4.0)


