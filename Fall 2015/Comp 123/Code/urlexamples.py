

import urllib.request

def getWebText(url):
    """Takes in a string that contains a URL, and reads the contents of that page,
    converting the results to be a Python string, and returning that string"""
    page = urllib.request.urlopen(url)
    data = page.read()
    text = data.decode()
    return text



def printLines(text):
    """ Takes in a string and prints it line by line"""
    lines = text.split('\n')
    for line  in lines:
        if "<li>" in line:
            print(line.rstrip())

    
#printLines('text\nto be printed\n as a basic\n test\n')
#t1 = getWebText("http://www.macalester.edu/~fox/simpledoc.html")
#printLines(t1)
#t2 = getWebText("http://www.macalester.edu/~fox")
#printLines(t2)
#t3 = getWebText("http://www.nytimes.com")
#printLines(t3)

    
def justText(text):
    """Takes in a string of HTML text and loops through the positions 
    in the string. It keeps a flag
    variable, inText, that indicates when the characters from the HTML
    page are regular text, and when it is reading characters from a tag. 
    When it is reading regular text, it adds the characters to the output
    string. It skips the characters from tags.  It returns the resulting
    string of regular text."""
    inText = True
    outputText = ""
    for pos in range(len(text)):
        if text[pos] == "<":
            inText = False
        elif text[pos] == ">":
            inText = True
        elif inText == True:
            outputText = outputText + text[pos]
    return outputText

def justParagraphs(text):
    inP = True
    outputText = ""
    for pos in range(len(text)):
        if text[pos] == "<":
            inText = False
        elif text[pos] == ">":
            inText = True
        elif inText == True:            
            if text[pos:pos+4] == '</p>':          
                inP = True
                
        if inP and inText:
            outputText = outputText + text[pos]
        if text[pos] == "<" and text[pos+1] == "/" and text[pos+2]=="p":
            inP = False
    return outputText

#basicTest = justText('<h1>heading</h1> and then some text and then <strong>bold text</strong>')
#print(basicTest)
#t1 = getWebText("http://www.macalester.edu/~fox/simpledoc.html")
#t1a = justText(t1)
#print(t1a)
#t2 = getWebText("http://www.macalester.edu/~fox")
#t2a = justText(t2)
#print(t2a)
#t3 = getWebText("http://www.nytimes.com")
#t3a = justText(t3)
#print(t3a)

basicTest = justParagraphs('<p>heading</p> and then some text and then <strong>bold text</strong>')
print(basicTest)



