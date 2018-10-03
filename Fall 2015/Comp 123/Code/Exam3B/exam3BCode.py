


from imageTools import *


# ----------------------------------------------------------
# Put definition of horizLine here (uncomment tests at bottom)

def horizLines(pic, color, dist):
    """takes a picture, color and distance as an input and then replaces the first row with the input color and then skips by the input distance each time, replacing the next row"""
    pic2 = copyPicture(pic)
    y= 0
    while y < getHeight(pic2):
        for x in range(getWidth(pic2)):
            px = getPixel(pic2,x,y)
            setColor(px,color)
        y = y + dist
        
    
    
    return pic2
    
    


# ----------------------------------------------------------
# Debug definition of blankBadWords here (uncomment tests at bottom)

def blankBadWords(text, badWordList):
    """Takes in a text (string) and a list of "bad words." It searches for all
    occurrences of each bad word in the text and replaces them by X's, one X for each
    character in the bad word. If bad words overlap, then the first one found will
    be replaced. Returns the new text at the end."""
    
    for badWord in badWordList:
        wordLen = len(badWord) #should be length of the badWord to replace with that number of X's
        blank = 'X' * wordLen
        while badWord in text:
            pos = text.find(badWord)
            upToWord = text[:pos] #missing a colon to tell python that the variable upToWord should be the string spliced up until the first occurance of the bad word
            afterWord = text[pos + wordLen:]
            text = upToWord + blank + afterWord
    return text #wrong indentation

                


# ----------------------------------------------------------
# Test calls (uncomment tests as needed)

    
if __name__ == '__main__':
    pic1 = makePicture("blueMotorcycle.jpg")
    show(pic1)

    # Test calls for horizLines
    np1 = horizLines(pic1, red, 20)
    show(np1)
    np2 = horizLines(pic1, cyan, 50)
    show(np2)
    np3 = horizLines(pic1, green, 5)
    show(np3)
    np4 = horizLines(pic1, pink, 1)
    show(np4)
    
    ## Test calls for blankBadWords
    puckSpeech = """If we shadows have offended,
     Think but this, and all is mended—
     That you have but slumbered here
     While these visions did appear.
     And this weak and idle theme,
     No more yielding but a dream,
     Gentles, do not reprehend.
     If you pardon, we will mend.
     And, as I am an honest Puck,
     If we have unearnèd luck
     Now to ’scape the serpent’s tongue,
     We will make amends ere long.
     Else the Puck a liar call.
     So good night unto you all.
     Give me your hands if we be friends,
     And Robin shall restore amends."""
    
    print(blankBadWords("A man, a plan, a canal: Panama!", ['an', 'ma']))
    print(blankBadWords("A man, a plan, a canal: Panama!", ['ma', 'an']))
    print(blankBadWords("A man, a plan, a canal: Panama!", []))
    print(blankBadWords("The quick brown fox jumps over the lazy dog", ['a', 'e', 'i', 'o', 'u']))
    print(blankBadWords(puckSpeech, ['weak', 'serpent', 'liar']))
    input("k? ")
