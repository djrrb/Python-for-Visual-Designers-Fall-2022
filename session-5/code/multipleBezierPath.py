myShapeCount = 10
myShapeHeight = 1000
myBaseHandle = 500
for myShapeNumber in range(myShapeCount):

    
    myHandle = randint(-myBaseHandle,myBaseHandle)
    myHandle2 = randint(-myBaseHandle, myBaseHandle)

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


    #stroke(1, 0, 0)
    #strokeWidth(10)

    fill(random(), random(), random(), .5)
    #blendMode('lighten')
    drawPath(myPath)
    
    myShapeHeight -= 100