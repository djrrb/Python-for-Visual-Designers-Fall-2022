# simple eyedrop grid

# define the image
myImage = ImageObject('black-raspberries.jpg')
# set the canvas to the image size
newPage(*myImage.size())

# decide how many rows and columns our grid will have
myColCount, myRowCount = 33, 25
# determine the width and height of each cell of the grid
myShapeWidth = width()/myColCount
myShapeHeight = height()/myRowCount
print(myShapeWidth, myShapeHeight)

# loop through the rows
for myRowNumber in range(myRowCount):
    # figure out the y position by
    # multiply row number by shape height
    myY = myRowNumber * myShapeHeight
    # loop through the columns
    for myColNumber in range(myColCount):
        # do the same for the columns
        myX = myColNumber * myShapeWidth
        # get the eyedrop color at that position on the image
        myEyedropColor = imagePixelColor(myImage, (myX, myY))
        # set the fill color
        fill(*myEyedropColor)
        # draw our shape at that position
        oval(myX, myY, myShapeWidth, myShapeHeight)