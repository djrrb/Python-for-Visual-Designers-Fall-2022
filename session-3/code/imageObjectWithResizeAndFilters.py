myImage = ImageObject('black-raspberries.jpg')
#myImage.kaleidoscope()

print(myImage.size())
newPage(*myImage.size())
myImage.sepiaTone(2)
#myImage.colorPosterize(2)
#myImage.gaussianBlur()

myImage.CMYKHalftone(width=10)
image(myImage, (0, 0))
