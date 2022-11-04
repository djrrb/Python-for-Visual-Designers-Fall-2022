
myShapeCount = 100
myShapeRadius = 50

# define an empty image
myImage = ImageObject()

# use "with" to draw line art our image
with myImage:
    # draw a bunch of circles at random placements
    for myShapeNumber in range(myShapeCount):
        with savedState():
            translate(randint(0, width()), randint(0, height()))
            fill(random(), random(), random())
            oval(
                -myShapeRadius, 
                -myShapeRadius, 
                myShapeRadius*2, 
                myShapeRadius*2
            )
            
# apply a filter to our image
myImage.bumpDistortion((width()/2, height()/2), 500)
# draw the image
image(myImage, (0, 0))