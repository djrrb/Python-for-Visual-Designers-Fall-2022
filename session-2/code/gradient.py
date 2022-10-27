newPage('Letter')
myShapeCount = 4
myShapeSequence = range(myShapeCount)
myWidth = width()/myShapeCount
myHeight = height()
myR = 1
myG = 0
myB = 0
myX = 0

for myShapeNumber in myShapeSequence:
    print(myShapeNumber)
    fill(myR, myG, myB)
    # rect(x, y, w, h)
    rect(myX, 0, myWidth, myHeight)
    print(myX, 'this is myX')
    myX += myWidth
    # this is the same as
    # myX = myX + myWidth
    myG += 1/myShapeCount