# make a new page
newPage('LetterLandscape')
# define a shape size
myShapeSize = 300
# move our (0, 0) location to the center of the canvas
translate(width()/2, height()/2)

# draw the rectangle from the center
# by subtracting half the width and height from the x and y positions
rect(
    -myShapeSize/2, # x
    -myShapeSize/2, # y
    myShapeSize, # w
    myShapeSize # h
    )