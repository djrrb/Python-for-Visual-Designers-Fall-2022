myImage = ImageObject('black-raspberries.jpg')

myX, myY = (200, 180)

myEyedropColor = imagePixelColor(myImage, (myX, myY))

image(myImage, (0, 0))

fill(*myEyedropColor)
oval(myX, myY, 500, 500)

