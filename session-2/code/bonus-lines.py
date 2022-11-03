# will draw one big circle, made up of how many little circles
myCircleCount = 30

myBigRadius = 300 # how big to make the big circle
mySmallRadius = 150 # how big to make the small circles

# little circles will be made up of spokes originating from the center
# what will vary is how many lines make up a circle
myMinSpokeCount = 3 # 3 in original animation
myMaxSpokeCount = 36 # 36 in original animation

# build up a sequence going from minSpokes to maxSpokes
# convert it to a list
mySequence = list(range(myMinSpokeCount, myMaxSpokeCount, 1))
# then add another list going from max to min so it increases AND decreases
mySequence += list(range(myMaxSpokeCount, myMinSpokeCount, -1))

# get the line count value as each item in the squence
for mySpokeCount in mySequence:
    
    newPage()
    
    # draw a black background
    rect(0, 0, width(), height())
    
    # do the canvas settings
    stroke(1)
    strokeWidth(1)
    fill(None)
    
    # move to the center of the canvas
    translate(width()/2, height()/2)
    
    # now draw a bunch of small circles in a big circle
    for myCircleNumber in range(myCircleCount):
        # save the state so we can forget all the little rotations happening in the microcosm of the circle
        with savedState():
            # move away from the center from the big circle
            translate(0, myBigRadius)
            # now draw a little circle made up of "spokes" from the center
            for myLineNumber in range(mySpokeCount):
                line((0, 0), (0, mySmallRadius))
                rotate(360/mySpokeCount)
            # dedent once to end circle loop
        # dedent again to exit saved state
        # now we are back dealing with the big circle
        rotate(360/myCircleCount)
        # rotate to drw the next little circle
        
# at the very end, save the image
saveImage('spokes.gif')