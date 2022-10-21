myPageCount = 10
myPageRange = range(myPageCount)

for myPage in myPageRange:
    # make a new page
    print(myPage)
    newPage('LetterLandscape')
    # draw the background
    fill(0)
    rect(0, 0, width(), height())
    # set a random fill color
    fill(random(), random(), random())
    # draw a shape
    oval(0, 0, width(), height())
    myFileName = 'ovals_' + str(myPage) + '.png'
    saveImage(myFileName)
print('done')
