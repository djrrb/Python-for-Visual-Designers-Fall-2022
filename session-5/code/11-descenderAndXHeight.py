# draw stuff related to the font metrics
 
# define the font
myFontPath = 'Verdana'
# and  the font size
myFontSize = 300
# define a formatted string
myString = FormattedString('hip', font=myFontPath, fontSize=myFontSize)

# set the canvas font and fontsize so we can get information about the font
font(myFontPath)
fontSize(myFontSize)
# get information about the font like x-height and descender
myXHeight = fontXHeight()
myDescender = -fontDescender()
print(myXHeight, myDescender)

# move the text up by the descender value to create room
translate(0, myDescender)
fill(0, 1, 1)
# draw an oval at the x-height
oval(0, 0, 100, myXHeight)

# draw the text
text(myString, (0, 0), align="left")