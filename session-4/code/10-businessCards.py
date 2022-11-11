# import csv module
import csv

myInch = 72 # inch constant
myFileName = 'Fantasy Conference - Sheet 1.csv' # CSV filename

# some margin contsants
myRightMargin = 15
myLeftMargin = 111

# open the CSV file
with open(myFileName, encoding='utf-8') as myFile:
    # read the CSV file as a CSV object
    myCSVReader = csv.reader(myFile)
    # loop through each row in the CSV
    for myRow in myCSVReader:
        # unpack the columns into variables
        myName, myAffiliation, myRole = myRow
        # make a new page
        newPage(3.5*myInch, 2*myInch)
        # save our state so that logo formatting doesn’t apply anywhere else
        with savedState():
            scale(.1)
            translate(-90, 60)
            image('logo.png', (0, 0))
        # visualize our textbox
        fill(.9)
        rect(111, 20, width()-myLeftMargin-myRightMargin, 107)
        # do font formatting
        fill(0)
        fontSize(20)
        lineHeight(30)
        tracking(1)
        #text(myName, (0, 0))
        
        # use textBox(string, (x, y, w, h))
        textBox(myName, (111, 20, width()-myLeftMargin-myRightMargin, 107))