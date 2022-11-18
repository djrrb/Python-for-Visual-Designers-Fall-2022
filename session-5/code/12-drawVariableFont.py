# set the font and fontsize
myFontPath = 'CondorVariable-VF.ttf'
myFontSize = 300

# how may frames
myPageCount = 10

# get the font variations, including min and max
font(myFontPath)
fontSize(myFontSize)
myVariations = listFontVariations()
myMin = myVariations['wght']['minValue']
myMax = myVariations['wght']['maxValue']
myXHeight = fontXHeight()

# set weight 
myWeight = myMin

# loop through each page
for myPage in range(myPageCount):
    # make a new page
    newPage()
    # make a white background
    fill(1)
    rect(0, 0, width(), height())
    # set fill to black
    fill(0)
    

    myString = FormattedString(
        'hip', 
        font=myFontPath, 
        fontSize=myFontSize,
        fontVariations={'wght': myWeight}
    )

    # move to center, and offset for half the x-height
    translate(width()/2, height()/2-myXHeight/2)

    # draw the text in the center
    text(myString, (0, 0), align="center")
    
    # augment weight
    myWeight += 100


