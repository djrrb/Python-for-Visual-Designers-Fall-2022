
myShapeCount = 54 # how many shapes to draw?
myPageCount = 180 # how many pages or frames to draw
myRotateValue = 0 # what should the starting rotation value be? (0 is upright)

# do our loop
for myPageNumber in range(myPageCount):
    # for each item in the loop, make a new page
    newPage()
    
    # if we want, draw a white backround 
    # we don’t need to do this if we fill the shapes
    #fill(1)
    #rect(0, 0, width(), height())
    
    # move to the center of the canvas
    translate(width()/2, height()/2)
    
    # start our loop
    for myShapeNumber in range(myShapeCount):
        
        # if our number/2 is equal to the integer of our number/2, it is even
        if myShapeNumber/2 == int(myShapeNumber/2):
            fill(0) # if it is even, make it black
        elif myShapeNumber / 5 == int(myShapeNumber/5):
            fill(0, 0, 1) # if it is odd and divisible by 5, make it blue
        else:
            fill(1, 0, 0) # in all other cases, make it red
            
        # draw the full-page rectangle from the center
        # subtracting half of width and height from x and y
        rect(-width()/2, -height()/2, width(), height())
        # scale down each time
        scale(.95)
        # rotate by myRotateValue each time
        rotate(myRotateValue)
    print(myRotateValue)
    # dedent to exit the shape loop, now we are back in the page loop
    # increase the rotateValue so that the next page will rotate a bit more 
    # by setting this to 360/page count, the total rotation over all frames will be a full circle, 360°
    myRotateValue += 360/myPageCount

# dedent to exit the page loop
# now that we have all the pages, save the animation
saveImage('spiral.gif')
