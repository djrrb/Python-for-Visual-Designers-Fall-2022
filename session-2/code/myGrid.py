from random import random, choice
newPage(1000, 1000)
myRowCount = 10
myColCount = 10
myX = 0
myY = 0
myShapeSize = 100
myWiggle = 25
myCharacterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



for myRowNumber in range(myRowCount):
    print('start my row loop')
    for myColNumber in range(myColCount):
        print('\tdraw a shape')
        fill(random(), random(), random())
        rect(
            myX+randint(-myWiggle, myWiggle),  # x
            myY+randint(-myWiggle, myWiggle),  # y
            myShapeSize+randint(-myWiggle, myWiggle),  # width
            myShapeSize+randint(-myWiggle, myWiggle) # height
        ) # runs 100 times
        fill(1, 0, 0)
        myCenter = myShapeSize/2
        myOvalRadius = 10
        oval(
            myX+myCenter-myOvalRadius, 
            myY+myCenter-myOvalRadius, 
            myOvalRadius*2,
            myOvalRadius*2
            )
        fontSize(100)
        #text(choice(myCharacterList), (myX, myY))
        myX += 100 # runs 100 times
    print('offset for the next row')
    myY += 100 # runs 10 times
    myX = 0
print('done')