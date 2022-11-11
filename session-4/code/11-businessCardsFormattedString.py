# get CSV library
import csv

myInch = 72 # inch constant
myFileName = 'Fantasy Conference - Sheet 1.csv' # CSV filename

# margins
myRightMargin = 15
myLeftMargin = 111

# debug variable
# True will show “guidelines”
myDebug = False

# open the file
with open(myFileName, encoding='utf-8') as myFile:
    # read it as a CSV object
    myCSVReader = csv.reader(myFile)
    # loop through each row
    for myRow in myCSVReader:
        # get each cell as a variable
        myName, myAffiliation, myRole = myRow
        # new page
        newPage(3.5*myInch, 2*myInch)
        # draw logo with localized formatting
        with savedState():
            scale(.1)
            translate(-90, 60)
            image('logo.png', (0, 0))
        
        if myDebug:
            # sketch text box
            fill(.9)
            rect(111, 20, width()-myLeftMargin-myRightMargin, 107)

        fill(0)
        # make a formatted string for the name
        # opentype features are a dictionary mapping feature tag to True/False value
        myString = FormattedString(
            myName +' 1234', 
            fill=(1, 0, 0), # red
            fontSize=15,
            font='Minion Pro', 
            openTypeFeatures={'smcp': True, 'c2sc': True, 'lnum': False, }
        )
        # now we can append text blocks with different formatting
        myString.append(
            '\n'+myAffiliation, 
            font=choice(installedFonts()),  # get a random font
            fill=(0, 0, 0), 
            fontSize=11.5, 
            tracking=.5, 
            paragraphTopSpacing=10
        )
        
        # draw the formatted string to canvas
        textBox(myString, (111, 20, width()-myLeftMargin-myRightMargin, 107))
        
        # draw the point where we will put the role
        if myDebug: oval(width()-myRightMargin-5, -5+10, 10, 10)
        
        # draw the role in the bottom right, indpendent from text box
        text(myRole, (width()-myRightMargin, 10), align="right")