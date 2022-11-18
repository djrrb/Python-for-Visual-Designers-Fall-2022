
# how tall to draw the shape
myShapeHeight = 100
# how big to make the handles
myHandle = randint(-200, 200)
myHandle2 = randint(-200, 200)

# create a bezier path
myPath = BezierPath()

# move our current location to the lower left
myPath.moveTo((0, 0))
# draw a horizontal line across the bottom
myPath.lineTo((width(), 0))
# draw a line up to myShapeHeight
myPath.lineTo((width(), myShapeHeight))
# now draw the curve
myPath.curveTo(
    ((width(), myShapeHeight+myHandle)), # first handle
    ((0, myShapeHeight+myHandle2)), # second handle
    ((0, myShapeHeight)), # destination point
    )
# complete the path
myPath.closePath()

# set some formatting
stroke(1, 0, 0)
strokeWidth(10)

# draw the path
drawPath(myPath)