
newPage()
# make some variables for the donut
# these can be relative to the page size using width() or height()
# or they can be static values
myDonutThickness = height()/4
myDonutWidth = width()
myDonutHeight = height()

# draw a big oval
# oval(x, y, w, h)
oval(
    0, 0, 
    myDonutWidth, 
    myDonutHeight
)
# switch to white
fill(1)
# now draw the smaller oval
# the key is to change the size and position of this oval
# so it has thickness on all sides
oval(
    myDonutThickness, # move x to create left side of donut
    myDonutThickness, # move y to create bottom side of donut
    myDonutWidth-myDonutThickness*2,  # draw shape narrower to create right side of donut
    myDonutHeight-myDonutThickness*2 # draw shape shorter to create top side of donut
)

saveImage('donut.png')