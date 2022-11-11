# savedState() allows our canvas state to travel back in time

# the canvas state starts out with a font size of 10 and a black fill

fontSize(20)
text('getting started', (200, 60))
oval(50, 50, 100, 100)

# now let's make a saved state and do some other canvas transformations
with savedState():
    fill(1, 0, 0) # make it red
    rect(0, 0, 100, 100) # draw a rectangle
    rotate(15) # rotate
    fontSize(100) # enlarge text
    text('hello world!', (200, 200)) # draw text
# once we dedent we are back to the way it was before
# small text, black fill
text('this is more text', (200, 500))