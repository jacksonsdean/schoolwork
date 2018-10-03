


def letterFreq(file):
    inFile = open(file,"r")
    fileTxt = inFile.read().lower()
    alphaDict = {}
    for i in fileTxt:
        if i.isalpha():
            if not(i in alphaDict):
                alphaDict[i] = 1
            else:
                alphaDict[i] = alphaDict[i] + 1
    inFile.close()
    return alphaDict

#print(letterFreq("mobydick.txt"))

def wordCount(file):
    inFile = open(file,"r")
    fileWords = inFile.read().lower().split()
    alphaDict = {}
    for i in fileWords:
        if i.isalpha():
            if not(i in alphaDict):
                alphaDict[i] = 1
            else:
                alphaDict[i] = alphaDict[i] + 1
    inFile.close()
    return alphaDict

print(wordCount("mobydick.txt"))
