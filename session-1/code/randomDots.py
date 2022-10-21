myShapeCount = 10
myShapeRange = range(myShapeCount)

for myShapeNumber in myShapeRange:
    print(myShapeNumber)
    myX = random()*width()
    myY = random()*height()
    print(myX, myY)
    oval(myX-50, myY-50, 100, 100)