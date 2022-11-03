# will draw one big circle, made up of how many little circles
myCircleCount = 8

myBigRadius = 300 # how big to make the big circle

# little circles will be made up of spokes originating from the center
# what will vary is how many lines make up a circle
myMinSmallRadius = 0 
myMaxSmallRadius = 1000

# how much length to add to the radius per frame
myStepIncrease = 70
# and how much to take away (twice as fast?)
myStepDecrease = -myStepIncrease * 2

# how many spokes to draw at the beginning vs the end
myMinSpokeCount = 3
myMaxSpokeCount = 36

# loop through how many spokes to draw
for mySpokeCount in range(myMinSpokeCount, myMaxSpokeCount):
    # build up a sequence going from minSpokes to maxSpokes
    # convert it to a list
    mySequence = list(range(myMinSmallRadius, myMaxSmallRadius, myStepIncrease))
    # then add another list going from max to min so it increases AND decreases twice as fast
    mySequence += list(range(myMaxSmallRadius, myMinSmallRadius, myStepDecrease))

    # get the line count value as each item in the squence
    for mySmallRadius in mySequence:
    
        newPage()
        frameDuration(1/20)
    
        # draw a black background
        rect(0, 0, width(), height())
    
        # do the canvas settings
        stroke(1)
        strokeWidth(1)
        fill(1)
    
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
                    # add a little oval to the end of the line so we can see it grow more easily
                    oval(0-2, mySmallRadius-2, 4, 4)
                    rotate(360/mySpokeCount)
                # dedent once to end circle loop
            # dedent again to exit saved state
            # now we are back dealing with the big circle
            rotate(360/myCircleCount)
            # rotate to drw the next little circle
        
# at the very end, save the image
saveImage('increaseSpokes.gif')