# make a variable to define how many times we want to loop
myPageCount = 10
# convert that number to a range of numbers, starting at 0
myPageRange = range(myPageCount)

# loop through each item in a sequence
# the syntax is "for item in sequence:"
#    'item' is a new variable we define to represent the current item 
#    'sequence' is the sequence we will loop through 
#    end the line with a colon and indent the following line
#    all indented code will be run once per loop
# dedenting ends the loop, all future code will be run once

for myPage in myPageRange:
    # all indented code will be run once for each item
    
    # print the page number to the console (starting at 0)
    print(myPage)
    # make a new page on the canvas
    newPage('LetterLandscape')
    
    # draw a background by drawing a rectangle the size of the canvas
    
    # set the color to black 
    # (black is the default color, so this is a formality)
    fill(0)
    rect(0, 0, width(), height())
    
    # now set a random fill color
    fill(random(), random(), random())
    # draw an oval the full size of the canvas
    oval(0, 0, width(), height())
    
    # save individual frames
    # define a filename that incorporates the page number
    # we need to convert the page number to a string using the str() function
    myFileName = 'ovals_' + str(myPage) + '.png'
    
    # save the current page as a png 
    # (this is indented so one image gets saved for each frame)
    saveImage(myFileName)

# dedent...now this code only runs once

# save the full animation
saveImage('oval-animation.gif')

# also save it as a PDF
saveImage('oval-animation.pdf')

# print done to the console in case we want to
# confirm we ran through the script successfully
print('done')
