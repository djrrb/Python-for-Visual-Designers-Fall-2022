# adapted from Aasawari’s script

# the radius of each ring
myRingSize = 200
# how many rings to draw
myRingCount = 10

# the size of each shape
myCircleRadius = 50 
# how many shapes per ring
myCircleCount = 15

# originally our shape was a circle
# define a function for that
def myOvalOriginal():
    oval(
        -myCircleRadius/2, 
        -myCircleRadius/2+myRingSize, 
        myCircleRadius, 
        myCircleRadius
    )
    
# define a function for the triangle shape
def myOval():
    
    # polygon(
    #     (0, myRingSize),
    #     (myCircleRadius/2, myCircleRadius+myRingSize),
    #     (myCircleRadius, myRingSize),
    #     )
    
    # enter a saved state and move from the center to the edge of the ring
    with savedState():
        translate(0, myRingSize)
        # now draw the triangle
        polygon(
            (0, 0), # bottom left
            (myCircleRadius/2, myCircleRadius), # top center
            (myCircleRadius, 0), # bottom right
            )


# myRing will draw a single ring of shapes
def myRing():
    fill(0)
    for myCircleNumber in range(myCircleCount):
        myOval()
        rotate(360/myCircleCount)

# now draw the canvas
# move to the center
translate(width()/2, height()/2)

# draw a certain number of rings
for myRingNumber in range(myRingCount):
    # draw the ring
    myRing()
    # now make the ring bigger
    myRingSize += 70
    # and increase the number of shapes per ring
    myCircleCount += 7

       