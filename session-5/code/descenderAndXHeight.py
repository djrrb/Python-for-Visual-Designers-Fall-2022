myFontPath = 'Verdana'
myFontSize = 300
myString = FormattedString('hip', font=myFontPath, fontSize=myFontSize)

font(myFontPath)
fontSize(myFontSize)
myXHeight = fontXHeight()

#translate(width()/2, height()/2)
translate(0, -fontDescender())
oval(0, 0, 100, myXHeight)
text(myString, (0, 0), align="left")