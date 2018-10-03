# my file
fileIn = open("alice.txt", 'r')
line1 = fileIn.readline()
print(line1)
line2 = fileIn.readline()
print(line2)
allTheRest = fileIn.read()
print( len(allTheRest), allTheRest[0:20] )


def printAbbrev(filename):
    f = open(filename, 'r')
    for line in f:
        print(line[0:20])
    f.close()
    