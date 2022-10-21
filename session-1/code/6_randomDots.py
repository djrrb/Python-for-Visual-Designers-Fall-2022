# determine how many shapes we will draw
myShapeCount = 10
# convert that number into a range of numbers between 0 and myShapeCount
myShapeRange = range(myShapeCount)

# loop through the range
# my shape number will be equal to whatever shape we’re currently on in the sequence
for myShapeNumber in myShapeRange:
    # print it to canvas just because
    print(myShapeNumber)
    
    # define myX and myY variables as random coordinates on the canvas
    # the random() function returns a number between 0 and 1
    # so random()*width() is a random x value on the canvas
    # and random()*height() is a random y value
    myX = random()*width()
    myY = random()*height()
    
    # print the x, y coordinates we will draw at
    print(myX, myY)
    
    # draw the oval at myX and myY
    # it will be 100pt wide and 100pt high
    # i can subtract the radius
    # to draw from the center 
    # rather than the lower left
    oval(myX-50, myY-50, 100, 100)