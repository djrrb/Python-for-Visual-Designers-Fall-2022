
myImage = ImageObject('black-raspberries.jpg')
newPage(*myImage.size())

myShapeWidth = 50
myShapeHeight = 50
myColCount = int(width() // myShapeWidth)
myRowCount = int(height() // myShapeHeight)
print(myColCount, myRowCount)

for myRowNumber in range(myRowCount):
    myY = myRowNumber * myShapeHeight
    for myColNumber in range(myColCount):
        myX = myColNumber * myShapeWidth
        myEyedropColor = imagePixelColor(myImage, (myX, myY))
        fill(*myEyedropColor)
        oval(myX, myY, myShapeWidth, myShapeHeight)
