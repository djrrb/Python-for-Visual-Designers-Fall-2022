myImage = ImageObject('black-raspberries.jpg')
newPage(*myImage.size())

myColCount, myRowCount = 31, 25
myBaseShapeSize = 90
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

for myRowNumber in range(myRowCount):
    myY = myRowNumber * myCellHeight
    for myColNumber in range(myColCount):
        myX = myColNumber * myCellWidth
        myEyedropColor = imagePixelColor(myImage, (myX, myY))
        fill(*myEyedropColor)
        myIntensitySum = myEyedropColor[0] + myEyedropColor[1] + myEyedropColor[2]
        myIntensityValue = 1 - (myIntensitySum / 3)
        myShapeSize = myBaseShapeSize * myIntensityValue
        myXOffset = (myCellWidth - myShapeSize)/2
        myYOffset = (myCellHeight - myShapeSize)/2
        
        oval(myX+myXOffset, myY+myYOffset, myShapeSize, myShapeSize)
