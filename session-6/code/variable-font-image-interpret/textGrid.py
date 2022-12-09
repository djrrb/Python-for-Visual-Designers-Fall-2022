myImagePath = 'images/Berninapass_1877_Siegfriedkarte.jpg'


myImage = ImageObject(myImagePath)
newPage(*myImage.size())

myCellWidth = width()/10
myCellHeight = myCellWidth



image(myImage, (0, 0))

myRowCount = ceil(height()/myCellHeight)
myColCount = ceil(width()/myCellWidth)
print(myRowCount, myColCount)

for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        print(myRowNumber, myColNumber)
        myX = myColNumber*myCellWidth
        myY = myRowNumber*myCellHeight
        with savedState():
            fill(0, .5)
            oval(myX, myY, myCellWidth, myCellHeight)

