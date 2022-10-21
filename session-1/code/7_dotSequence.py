# determine how many shapes we will draw
myShapeCount = 10
# convert that number into a range of numbers between 0 and myShapeCount
myShapeRange = range(myShapeCount)

# make variables for the x and y position that we will start at
myX = 0
myY = 0

# loop through the range
# my shape number will be equal to whatever shape we’re currently on in the sequence
for myShapeNumber in myShapeRange:
    # print it to canvas just because, and also the x and y coordinates
    print(myShapeNumber)
    print(myX, myY)
    # draw an oval at myX, myY
    oval(myX, myY, 100, 100)
    # now AUGMENT the x value using "+="
    # this takes the existing value of x and adds to it
    # so each time, the myX variable will increase
    # and the oval will be drawn to the right of the oval before it
    myX += 100