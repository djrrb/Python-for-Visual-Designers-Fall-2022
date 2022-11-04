newPage(1000, 1000)

myColCount, myRowCount = 10, 10
myGridSize = 100
myPatternSize = 200
# scale to fit pattern in the grid
myScaleValue = myGridSize/myPatternSize

def myPattern():
    # this pattern is NOT responsive
    # no variables or anything relative
    # but I know it covers a roughly 200x200 area
    # so I can scale it to fit my grid
    fill(.5, 0, 0)
    oval(18, 18, 100, 100)
    fill(.25, 0, 0)
    oval(130, 130, 75, 75)
    fill(.75, 0, 0)
    oval(130, 100, 25, 25)
    oval(100, 130, 25, 25)
    oval(180, 210, 25, 25)
    oval(210, 180, 25, 25)
    oval(180, 100, 25, 25)
    oval(100, 180, 25, 25)
    oval(130, 210, 25, 25)
    oval(210, 130, 25, 25)


rect(0, 0, width(), height())

for myRowNumber in range(myRowCount):
    myY = myRowNumber * myGridSize
    for myColNumber in range(myColCount):
        myX = myColNumber * myGridSize
        with savedState():
            translate(myX, myY)
            scale(myScaleValue)
            myPattern()