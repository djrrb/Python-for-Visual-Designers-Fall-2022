myShapeCount = 10
# make the range x
myShapeRange = range(myShapeCount)

myX = 0
myY = 0
for myShapeNumber in myShapeRange:
    print(myShapeNumber)
    print(myX, myY)
    oval(myX, myY, 100, 100)
    myX += 100