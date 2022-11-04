# define the image as a variable
# using the ImageObject object type
myImage = ImageObject('black-raspberries.jpg')

# ask the image what size it is
print(myImage.size())

# draw the image to canvas
image(myImage, (0, 0))