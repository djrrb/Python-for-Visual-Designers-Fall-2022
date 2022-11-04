# this time we will figure out the row and col
# count 
myImage = ImageObject('black-raspberries.jpg')
# get the size of the image as two separate variables for width and height
myImageWidth, myImageHeight = myImage.size()
# define a static shape width and height
myShapeWidth = 50
myShapeHeight = 50
# figure out how many whole shapes will fit in the image
# this may not add up exactly to the image size
myColCount = int(myImageWidth // myShapeWidth)
myRowCount = int(myImageHeight // myShapeHeight)
print(myColCount, myRowCount)
# define our new page based on the size of the grid
# not the size of the image
newPage(myColCount*myShapeWidth, myRowCount*myShapeHeight)

# loop through rows
for myRowNumber in range(myRowCount):
    # calculate y position
    myY = myRowNumber * myShapeHeight
    # loop through columns
    for myColNumber in range(myColCount):
        # calculate x position
        myX = myColNumber * myShapeWidth
        # get pixel color at that position
        myEyedropColor = imagePixelColor(myImage, (myX, myY))
        # set the fill color
        fill(*myEyedropColor)
        # draw the oval
        oval(myX, myY, myShapeWidth, myShapeHeight)
