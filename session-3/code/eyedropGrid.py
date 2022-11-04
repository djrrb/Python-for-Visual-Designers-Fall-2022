myImage = ImageObject('black-raspberries.jpg')
newPage(*myImage.size())

myColCount, myRowCount = 31, 25
myShapeWidth = width()/myColCount
myShapeHeight = height()/myRowCount
print(myShapeWidth, myShapeHeight)

for myRowNumber in range(myRowCount):
    myY = myRowNumber * myShapeHeight
    for myColNumber in range(myColCount):
        myX = myColNumber * myShapeWidth
        myEyedropColor = imagePixelColor(myImage, (myX, myY))
        fill(*myEyedropColor)
        oval(myX, myY, myShapeWidth, myShapeHeight)

# myX, myY = (200, 180)

# 

# image(myImage, (0, 0))

# 
# oval(myX, myY, 500, 500)

