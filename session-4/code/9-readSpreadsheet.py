# import csv module
import csv

# filename
myFileName = 'Fantasy Conference - Sheet 1.csv'

# open the file with UTF-8 encoding
# create the myFile variable to represent the file
with open(myFileName, encoding='utf-8') as myFile:
    # read as plaintext
    #myText = myFile.read()
    #print(myText)
    
    # read as CSV
    myCSVReader = csv.reader(myFile)
    # loop through the reader object
    for myRow in myCSVReader:
        # unpack the rows into separate variables
        myName, myAffiliation, myRole = myRow
        # print a cell from each row
        print(myName)