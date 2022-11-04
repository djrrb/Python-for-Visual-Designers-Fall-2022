# define an image
myImage = ImageObject('black-raspberries.jpg')

# run some filters
myImage.kaleidoscope()
myImage.sepiaTone(2)
#myImage.colorPosterize(2)
#myImage.gaussianBlur()
myImage.CMYKHalftone(width=10)

# set the canvas to the image size
# unpack the (width, height) tuple to send each to newPage separately
newPage(*myImage.size())
# draw the edited image to canvas
image(myImage, (0, 0))
