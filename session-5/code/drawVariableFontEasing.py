from easing_functions import *


myFontPath = 'CondorVariable-VF.ttf'
myFontSize = 300


myPageCount = 10

font(myFontPath)
fontSize(myFontSize)
myVariations = listFontVariations()
myMin = myVariations['wght']['minValue']
myMax = myVariations['wght']['maxValue']
myXHeight = fontXHeight()



for myDirection in range(2):
    
    if myDirection == 0:
        myMin = myVariations['wght']['minValue']
        myMax = myVariations['wght']['maxValue']
        myWidthMin = myVariations['wdth']['minValue']
        myWidthMax = myVariations['wdth']['maxValue']
    else:
        myMax = myVariations['wght']['minValue']
        myMin = myVariations['wght']['maxValue']
        myWidthMin = myVariations['wdth']['maxValue']
        myWidthMax = myVariations['wdth']['minValue']
    
    myEasing = SineEaseOut(myMin, myMax, myPageCount)
    myWidthEasing = SineEaseIn(myWidthMin, myWidthMax, myPageCount)
    
    for myPage in range(myPageCount):
        newPage()
        fill(1)
        rect(0, 0, width(), height())
        fill(0)
        myWeight = myEasing.ease(myPage)
        myWidth = myWidthEasing.ease(myPage)
        myString = FormattedString('hip', font=myFontPath, fontSize=myFontSize, fontVariations={'wght': myWeight, 'wdth': myWidth})
    
    

        translate(width()/2, height()/2-myXHeight/2)

        text(myString, (0, 0), align="center")
    

saveImage('animate.gif')