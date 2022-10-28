
# make a new page
newPage('Letter')

# define some variables
myShapeCount = 10 # how many shapes to draw
myShapeSequence = range(myShapeCount) # get a sequence from 0–10
# how wide should each shape be? 
# the full canvas width divided by the number of shapes
myWidth = width()/myShapeCount 
# how tall should each shape be? the full canvas height
myHeight = height() 
# define our starting shape position
myX = 0 
# define the color values for our starting color
myR = 1
myG = 0
myB = 0

# loop through the sequence
for myShapeNumber in myShapeSequence:
    # myShapeNumber will equal 0, 1, 2, 3 . . .
    print('shape number', myShapeNumber, '| myX', myX)
    # set the fill to our RGB value
    fill(myR, myG, myB)
    # draw the rectangle
    rect(myX, 0, myWidth, myHeight)
    
    # now that we've drawn the rectangle
    # augment our variables so the next one is diferent
    
    # move the x position to the right by one shape width
    myX += myWidth
    # using += is the same as saying
    # myX = myX + myWidth
    
    # add a bit to the green value
    # 1/myShapeCount will make the value go from 0 to 1 across the page
    myG += 1/myShapeCount