# where is the word list located
myWordListPath = '/usr/share/dict/words'

# keep track of page number
myPageNumber = 1

# open the path as a file

with open(myWordListPath, encoding="utf-8") as myFile:
    # read file as a list of lines
    myLines = myFile.readlines()
    # shuffle the list
    # define an empty formatted string
    myString = FormattedString('', fontSize=50, lineHeight=50, font='Comic Sans MS')
    # loop through a part of the list and and add words
    # to build up formatted string
    for myLine in myLines[:200]:
        myString.append( 
            myLine.strip() + ' ' , 
            fill=(random(), random(), random()), 
            font=choice(installedFonts()) )
    
    myMargin = 50
    #rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
    
    # as long as the formatted string myString has contents
    # keep making new pages and drawing our text box
    while myString:
        newPage()
        # reset the myString variable to equal the overflow
        # as returned by textBox()
        myString = textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
        # also draw a page number in the bottom right
        fontSize(20)
        text('Page '+str(myPageNumber), (width()-myMargin, myMargin), align="right")
        # augment page number
        myPageNumber += 1
    

    
    