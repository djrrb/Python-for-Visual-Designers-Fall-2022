myShapeCount = 100
myShapeRadius = 50

myImage = ImageObject()

with myImage:
    for myShapeNumber in range(myShapeCount):
        with savedState():
            translate(randint(0, width()), randint(0, height()))
            oval(
                -myShapeRadius, 
                -myShapeRadius, 
                myShapeRadius*2, 
                myShapeRadius*2
            )
            
myImage.bumpDistortion((width()/2, height()/2), 500)
image(myImage, (0, 0))