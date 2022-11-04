# load the image
myImage = ImageObject('black-raspberries.jpg')

# define an x and y position to eyedrop
myX, myY = (230, 130)

# get the (r,g,b,a) tuple for the color
# of the image at that position using
# imagePixelColor
myEyedropColor = imagePixelColor(myImage, (myX, myY))

# draw the image to canvas
image(myImage, (0, 0))

# set the fill color to our eyedrop color
# unpacking the rgba tuple
fill(*myEyedropColor)
# draw a rectangle showing the color at (myX, myY)
rect(myX, myY, 200, 200)

