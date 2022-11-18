# where is the word list located
myWordListPath = '/usr/share/dict/words'

# open the path as a file
with open(myWordListPath, encoding="utf-8") as myFile:
    
    # we want a list of words
    # we have two options:
    
    # 1) read as string and convert to list
    #myText = myFile.read()
    #print(type(myText))
    #print(len(myText))
    #myLines = myText.split('\n')
    
    # 2) read as list using the file readlines() method
    myLines = myFile.readlines()
    
    print(len(myLines))
    
    # shuffle the list
    shuffle(myLines)
    
    # define an empty formatted string
    myString = FormattedString('', fontSize=50, lineHeight=50, font='Comic Sans MS')
    # loop through each word in the list (but only the first 50 items)
    for myLine in myLines[:50]:
        myString.append(
            myLine.strip() + ' ' , # add the line and a space, stripping excess whitespace
            fill=(random(), random(), random()), # set a random fill color
            font=choice(installedFonts())  #set a random font
        )
    
    # draw a textbox with the string
    myMargin = 50
    #rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
    textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
    