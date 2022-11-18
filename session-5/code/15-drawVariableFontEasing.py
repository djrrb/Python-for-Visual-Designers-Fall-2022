# import easing functions
from easing_functions import *

# define font and size
myFontPath = 'CondorVariable-VF.ttf'
myFontSize = 300

# define number of frames
myPageCount = 20

# set canvas font and get info
# including variable axis min and max
# and x-height
font(myFontPath)
fontSize(myFontSize)
myVariations = listFontVariations()
myMin = myVariations['wght']['minValue']
myMax = myVariations['wght']['maxValue']
myXHeight = fontXHeight()


# we will run through loop twice
# once up and once down
for myDirection in range(2):
    
    # the first time the numbers go up
    if myDirection == 0:
        myMin = myVariations['wght']['minValue']
        myMax = myVariations['wght']['maxValue']
        myWidthMin = myVariations['wdth']['minValue']
        myWidthMax = myVariations['wdth']['maxValue']
    # otherwise the numbers go down
    else:
        myMax = myVariations['wght']['minValue']
        myMin = myVariations['wght']['maxValue']
        myWidthMin = myVariations['wdth']['maxValue']
        myWidthMax = myVariations['wdth']['minValue']
    
    # define our easing objects
    # min, max, duration
    myEasing = SineEaseOut(myMin, myMax, myPageCount)
    myWidthEasing = SineEaseIn(myWidthMin, myWidthMax, myPageCount)
    
    # loop through each page
    for myPage in range(myPageCount):
        # make a new page
        newPage()
        frameDuration(1/20)
        # white background
        fill(1)
        rect(0, 0, width(), height())
        fill(0)
        # get the weight and width values by feeding our easing objects
        # our page number, which represents how far we are
        # through the easing
        myWeight = myEasing.ease(myPage)
        myWidth = myWidthEasing.ease(myPage)
        
        # define the formatted string with those variable axis values
        myString = FormattedString(
            'hip', 
            font=myFontPath, 
            fontSize=myFontSize, 
            fontVariations={'wght': myWeight, 'wdth': myWidth}
        )
        # move to center minus half x-height
        translate(width()/2, height()/2-myXHeight/2)
        # draw the formatted string to canvas
        text(myString, (0, 0), align="center")
    
# save as an animated gif
saveImage('animate.gif')