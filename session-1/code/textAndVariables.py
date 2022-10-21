# this is my script to draw some text
myInch = 72
myTotalColors = 255
newPage(8.5*myInch, 11*myInch) # make a new page
print('hello world') # print to the console
fontSize(100) # change the font size
fill(47/myTotalColors, 165/myTotalColors, 151/myTotalColors) # change the color
text('hello world', (0, 0)) # draw the text