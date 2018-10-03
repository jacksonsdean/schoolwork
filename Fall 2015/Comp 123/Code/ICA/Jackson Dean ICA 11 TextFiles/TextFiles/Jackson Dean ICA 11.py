# Jackson Dean ICA 11 TextFiles

def printAbbrev(file):
    print('----------printAbbrev----------')
    inFile = open(file,'r')
    for line in inFile:
        line = line.strip()
        line = line[0:20]
        print(line)
    inFile.close()
        
printAbbrev("alice.txt")


def upToPeriod(file):
    inFile = open(file, 'r')
    retTxt = "" 
    txt = inFile.read()
    for char in txt:
        if char != '.':
            retTxt = retTxt + char 
        else:
            break        
    retTxt = retTxt.strip()+"."
    inFile.close()
    return retTxt
    
        
print('----------upToPeriod----------\n',upToPeriod("mockingbird.txt"))

def writeToN(n,file):
    inFile = open(file,"w")
    
    
