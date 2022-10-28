
newPage(1000, 1000) # make a new page

# define some variables
myRowCount = 10 # how many rows to draw
myColCount = 10 # how many cols to draw
myX = 0 # where to start our X position
myY = 0 # where to start our Y position
myShapeSize = width()/myColCount # how big should each shape be?

# we will do two loops
# one for each row, and within that, one for each column
# there will be 10 rows and 100 individual cells
print('begin the loop, this runs 1 time')

# do the first loop for each row
for myRowNumber in range(myRowCount):
    print('\tstart my row loop, this runs 10 times')
    
    # do the second loop for each column in any given row
    for myColNumber in range(myColCount):
        print('\t\tdraw a shape, this runs 100 times')
        # set a random fill and draw the shape
        fill(random(), random(), random())
        oval(
            myX,  # x
            myY,  # y
            myShapeSize, # width
            myShapeSize # height
        ) # runs 100 times
        # move to the right before drawing the next shape
        myX += 100 # runs 100 times
    # dedenting exits the column loop
    print('\toffset for the next row, this runs 10 times')
    # at the end of the row, we want to move up 100
    # we also reset x to 0 so that the columns will stack
    myY += 100 # runs 10 times
    myX = 0
# dedenting ends the row loop, and we’re done
print('done, this runs one time')
saveImage('simpleGrid.png')