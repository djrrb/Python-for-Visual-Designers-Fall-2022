# define a function with four arguments
# this way we can not worry about doing the math each time since myCenteredRect() will do it for us
def myCenteredRect(myX, myY, myW, myH):
    print(myX, myY, myW, myH)
    # draw a rect but subtract half the width and height from the x and y
    rect(
        myX-myW/2,
        myY-myH/2,
        myW,
        myH
        )

# move to the middle of the page
translate(width()/2, height()/2)

# use our special function
myCenteredRect(0, 0, 250, 250)

# draw a smaller rect, also from the center
fill(1, 0, 0)
myCenteredRect(0, 0, 80, 200)
