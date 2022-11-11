

myRingSize = 200
myRingCount = 10

myCircleRadius = 50
myCircleCount = 15

def myOvalOriginal():
    oval(
        -myCircleRadius/2, 
        -myCircleRadius/2+myRingSize, 
        myCircleRadius, 
        myCircleRadius
    )
    
def myOval():
    
    # polygon(
    #     (0, myRingSize),
    #     (myCircleRadius/2, myCircleRadius+myRingSize),
    #     (myCircleRadius, myRingSize),
    #     )
    
    with savedState():
        translate(0, myRingSize)
        polygon(
            (0, 0),
            (myCircleRadius/2, myCircleRadius),
            (myCircleRadius, 0),
            )


translate(width()/2, height()/2)

def myRing():
    fill(0)
    for myCircleNumber in range(myCircleCount):
        myOval()
        rotate(360/myCircleCount)


for myRingNumber in range(myRingCount):
    myRing()
    myRingSize += 70
    myCircleCount += 7

       