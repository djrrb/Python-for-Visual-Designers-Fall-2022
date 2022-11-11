#myShapeCount = 10

Variable([
    # create a variable called 'h'
    # and the related ui is a Slider.
    dict(name="myShapeCount", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=100,
                minValue=0,
                maxValue=200)),
    # create a variable called 'useColor'
    # and the related ui is a CheckBox.
    dict(name="drawOval", ui="CheckBox"),
    # create a variable called 'c'
    # and the related ui is a ColorWell.
    dict(name="myColor", ui="ColorWell")
    ], globals())

myShapeCount = int(myShapeCount)

for myShapeNumber in range(myShapeCount):
    myX = width()*random()
    myY = height()*random()
    fill(myColor)
    if drawOval:
        oval(myX, myY, 20, 20)
    else:
        rect(myX, myY, 20, 20)