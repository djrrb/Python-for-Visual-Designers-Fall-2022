# how many shapes to draw
myShapeCount = 50
# move to half the height
translate(0, height()/2)

for myShapeNumber in range(myShapeCount):
    # get our progress through the cycle
    # as a number between 0 and 1
    myProgress = myShapeNumber/myShapeCount
    # 2 * pi is a full circle
    # the sin() function gives us a number between +1 and -1
    mySinValue = sin(2 * pi * myProgress)
    # get our yOffset by multiplying the sine value by half the height
    # positive numbers will be above the center
    # negative numbers will be below the center
    yOffset = mySinValue * height()/2
    oval(-20, yOffset-20, 40, 40)
    # move to the right for the next shape
    translate(width()/(myShapeCount-1))