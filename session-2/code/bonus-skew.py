# how many shapes to draw?
myShapeCount = 100

# make a black background
rect(0, 0, width(), height())

# set some default formatting
# no fill, 1pt stroke
fill(None)
strokeWidth(1)

# move to teh center of the canvas
translate(width()/2, height()/2)

# loop through the shapes
for myShapeNumber in range(myShapeCount):
    # set the stroke color to a random color
    stroke(random(), random(), random())
    # draw an oval 
    oval(-400, -400, 800, 800)
    # skew the canvas by 1 degree each time
    skew(1)