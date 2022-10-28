#rect(500, 500, 100, 100)
newPage('LetterLandscape')
myShapeSize = 260
fontSize(50)

with savedState():
    translate(width()/2, height()/2)
    rect(
        -myShapeSize/2, # x
        -myShapeSize/2, # y
        myShapeSize, # w
        myShapeSize # h
        )
fill(1, 0, 0)
oval(0, 0, 200, 200) 
text('hello world', (width()/2, 0), align='center')