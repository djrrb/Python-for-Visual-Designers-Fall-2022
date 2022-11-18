myShapeHeight = 100
myHandle = randint(-100, 100)
myHandle2 = randint(-100, 100)

myPath = BezierPath()

myPath.moveTo((0, 0))
myPath.lineTo((width(), 0))
myPath.lineTo((width(), myShapeHeight))
myPath.curveTo(
    ((width(), myShapeHeight+myHandle)), # first handle
    ((0, myShapeHeight+myHandle2)), # second handle
    ((0, myShapeHeight)), # destination point
    )
myPath.closePath()


stroke(1, 0, 0)
strokeWidth(10)

drawPath(myPath)