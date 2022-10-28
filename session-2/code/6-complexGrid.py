from random import random, choice
newPage(1000, 1000)
myRowCount = 10
myColCount = 10
myX = 0
myY = 0
myShapeSize = 100
myWiggle = 25
# define a list of characters to choose from
myCharacterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# do our first loop
for myRowNumber in range(myRowCount):
    print('start my row loop')
    # do our second loop
    for myColNumber in range(myColCount):
        print('\tdraw a shape')
        fill(random(), random(), random())
        # draw a shape, adding a random amount of wiggle to all four corners
        rect(
            myX+randint(-myWiggle, myWiggle),  # x
            myY+randint(-myWiggle, myWiggle),  # y
            myShapeSize+randint(-myWiggle, myWiggle),  # width
            myShapeSize+randint(-myWiggle, myWiggle) # height
        ) # runs 100 times
        
        # draw a center dot in red
        fill(1, 0, 0)
        myCenter = myShapeSize/2 # find the center of each cell
        myOvalRadius = 10 # how big should our dot be
        # draw an oval to show the center of each cell
        oval(
            myX+myCenter-myOvalRadius, 
            myY+myCenter-myOvalRadius, 
            myOvalRadius*2,
            myOvalRadius*2
            )
        #fontSize(100)
        #text(choice(myCharacterList), (myX+myCenter, myY), align="center")
        myX += 100 # runs 100 times
    print('offset for the next row')
    myY += 100 # runs 10 times
    myX = 0
print('done')
saveImage('complexGrid.png')