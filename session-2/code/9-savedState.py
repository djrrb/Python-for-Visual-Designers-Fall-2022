# set up the page
newPage('LetterLandscape')
myShapeSize = 200 # how big will the centered shape be?
fontSize(50)

# save our state
with savedState():
    # the following transformations will only apply to indented code
    translate(width()/2, height()/2)
    
    rect(
        -myShapeSize/2, # x
        -myShapeSize/2, # y
        myShapeSize, # w
        myShapeSize # h
        )
    # we can draw other stuff too and the translate still applies
    fill(1, 0, 0)
    oval(0, 0, 200, 200) 

# once we dedent we exit the saved state
# our fill is back to black
# our position is back to the bottom left
oval(0, 0, 200, 200) 

# center some text by drawing its x at width()/2 and setting the align argument to "center"
text('hello world', (width()/2, 0), align='center')