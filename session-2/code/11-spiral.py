# how many shapes to draw?
myShapeCount = 100

# move to the center of the canvas
translate(width()/2, height()/2)

# make the shape empty but define a stroke color (black) and stroke thickness
fill(None)
stroke(0)
strokeWidth(5)

# now loop through the range of our shape count
for myShapeNumber in range(myShapeCount):
    print(myShapeNumber)
    # each time in the loop draw a full page rectangle
    rect(-width()/2, -height()/2, width(), height())
    # each time we loop, scale the canvas so each successive rectangle is a little smaller
    scale(.96)
    # also rotate the canvas 3° each time 
    rotate(3)

