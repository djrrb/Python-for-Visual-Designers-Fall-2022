# how many shpaes to draw
myShapeCount = 20
# how tall to draw the shape
# start with a big number
# we will make them shorter over time
myShapeHeight = 1100
# the basic length of the handle
# we will randomize based on this value
myBaseHandle = 500

# loop through a number of shapes
for myShapeNumber in range(myShapeCount):

    # each shape will have a random handle length for both sides of the curve
    myHandle = randint(-myBaseHandle,myBaseHandle)
    myHandle2 = randint(-myBaseHandle, myBaseHandle)

    # define the bezier path
    myPath = BezierPath()

    # move to bottom left 
    myPath.moveTo((0, 0))
    # draw a line to the bottom right
    myPath.lineTo((width(), 0))
    # draw a line up
    myPath.lineTo((width(), myShapeHeight))
    # draw curve across top of shape
    myPath.curveTo(
        ((width(), myShapeHeight+myHandle)), # first handle
        ((0, myShapeHeight+myHandle2)), # second handle
        ((0, myShapeHeight)), # destination point
        )
    # close path
    myPath.closePath()

    # set a random fill color that is semitransparent
    fill(random(), random(), random(), .5)
    #blendMode('lighten')
    drawPath(myPath)
    
    # for each shape, make it a little shorter
    # so we can see shapes behind it as well
    myShapeHeight -= 50