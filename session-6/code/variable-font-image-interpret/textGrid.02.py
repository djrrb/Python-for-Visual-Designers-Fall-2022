myImagePath = 'images/diseno-sin-titulo-1-3-cke.jpg'
myFontPath = 'Input[ital,wdth,wght,MONO,SRIF].ttf'
myText = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tellus ex, dapibus in lacinia at, tincidunt sit amet lectus. Nam eget neque eget ipsum pellentesque viverra. Nulla ac pulvinar elit. Morbi quis nulla ultricies, rhoncus velit nec, hendrerit nulla. Aenean at laoreet nibh. Aliquam malesuada metus sit amet urna porta finibus. Vivamus tempor vestibulum maximus. Nulla blandit nulla vel lorem aliquet venenatis. Morbi facilisis magna erat, a hendrerit diam euismod sit amet. Curabitur vestibulum quam at ipsum vulputate dapibus. Etiam consequat blandit facilisis.

Aliquam malesuada ullamcorper justo, sed ornare nisi congue venenatis. In quis nulla scelerisque, dignissim libero ac, tristique ligula. Praesent rutrum justo massa, ac ultricies sapien posuere tempor. Integer eget imperdiet odio. Vivamus a est at nibh fringilla ullamcorper nec et purus. Sed maximus magna sem. Suspendisse vitae pellentesque justo, at commodo enim.

In aliquam varius metus eget vulputate. Donec vel gravida est. Praesent ipsum ipsum, mattis in luctus at, aliquam in metus. Donec facilisis et sapien ac accumsan. Aenean dictum nisl nec maximus vestibulum. Donec porta posuere volutpat. Aenean sapien libero, faucibus in pulvinar eget, rutrum eget tellus. Suspendisse vitae rutrum diam, non rhoncus erat.

Phasellus id diam faucibus, convallis massa in, porttitor lectus. Donec pretium, elit sed egestas imperdiet, dolor tortor maximus ex, in tincidunt nulla lectus at ante. Pellentesque non ornare neque, quis tempor sapien. Aenean eleifend quis risus et facilisis. Integer ligula ante, semper eget vestibulum eu, accumsan non ante. Aenean eu mauris a lacus laoreet congue ut vitae ante. Nam ac blandit sapien.

In nec purus vitae dui suscipit porta a vel nisi. Nulla lectus mi, consequat non tellus nec, ullamcorper efficitur ante. Aenean ultrices ligula quis diam sollicitudin, et pellentesque tellus eleifend. Morbi consectetur congue luctus. Nunc quis libero et ante interdum rutrum eu quis odio. In vestibulum vehicula neque, eget tristique enim blandit ultricies. Proin vitae velit ipsum. Proin hendrerit porttitor ornare. Aenean at nisl et arcu varius tincidunt. """ * 100


myText = myText.replace(' ', '')
myText = myText.upper()

myImage = ImageObject(myImagePath)
newPage(*myImage.size())
fill(0)

rect(0, 0, width(), height())

myCellWidth = width()/60
myCellHeight = myCellWidth

myDebug = False


#if myDebug:
#    image(myImage, (0, 0))

myRowCount = ceil(height()/myCellHeight)
myColCount = ceil(width()/myCellWidth)
print(myRowCount, myColCount)

myShapeCount = 0

for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        myX = myColNumber*myCellWidth
        myY = myRowNumber*myCellHeight
        
        myColor = imagePixelColor(myImage, (myX, myY))
        myR, myG, myB, myA = myColor
        myGreyValue = (myR+myG+myB) / 3
        
        
        #myAverageImage = myImage.areaAverage((0, 0, 100, 100))
        #print(myAverageImage)
        
        with savedState():
            #fill(0, .5)
            #fill(*myColor)
            if myDebug: 
                stroke(1, 0, 0)
                strokeWidth(1)
            fill(None)
            oval(myX, myY, myCellWidth, myCellHeight)
            
        
        myLetter = myText[myShapeCount]
        print(myRowNumber, myColNumber, myLetter)
        font(myFontPath)
        fontSize(myCellHeight)
        
        myFontVariations = listFontVariations()
        myMinValue = myFontVariations['wght']['minValue']
        myMaxValue = myFontVariations['wght']['maxValue']
        myAxisRange = myMaxValue - myMinValue
        
        myInvertedGreyValue = 1-myGreyValue
        fill(myGreyValue)
        myWeightValue = myMinValue+myAxisRange*myGreyValue
        
        fontVariations(MONO=1, wght=myWeightValue)
        text(myLetter, (myX+myCellWidth/2, myY-fontDescender()), align="center")
        
        myShapeCount += 1

