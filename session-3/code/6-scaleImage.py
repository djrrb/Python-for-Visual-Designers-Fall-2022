newPage('Letter')

# define the image
myImage = ImageObject('black-raspberries.jpg')

# get the width and height as separate variables
# possibility #1 
myImageWidth = myImage.size()[0]
myImageHeight = myImage.size()[1]

# possibility #2
myImageWidth, myImageHeight = myImage.size()

with savedState():
    # figure out what number we would need to scale by
    # in order to make the width fit to the canvas
    myScaleMultiplier = width() / myImageWidth
    print(myScaleMultiplier)
    # perform the scale using that value
    scale(myScaleMultiplier)
    # draw the image to canvas
    image(myImage, (0, 0))

# exit the saved state to undo the scale
# and draw some text
fill(1)
stroke(0)
fontSize(100)
text('Raspberries', (20, 20))