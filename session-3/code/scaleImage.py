newPage('Letter')

myImage = ImageObject('black-raspberries.jpg')

print(myImage.size())

# possibility #1 
myImageWidth = myImage.size()[0]
myImageHeight = myImage.size()[1]

# possibility #2
myImageWidth, myImageHeight = myImage.size()
myScaleMultiplier = width() / myImageWidth
print(myScaleMultiplier)

with savedState():
    rotate(10)
    scale(myScaleMultiplier)
    image(myImage, (0, 0))

fill(1)
stroke(0)
fontSize(100)
text('My Raspberries', (0, 0))