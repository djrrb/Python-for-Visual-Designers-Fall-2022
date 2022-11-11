# make a custom function that contains some code
def myFancyFunction():
    # this draws a polygon
    polygon((950, 200), (20, 20), (100, 960), (800, 800))
    # sets the fill
    fill(0, 1, 0)
    # and draws the oval
    oval(20, 20, 500, 500)

# now I have a shortcut to run that code whenever i want
myFancyFunction()
# make a new page
newPage()
# run the code again
myFancyFunction()
# make a new page and run it smaller, still works!
newPage()
scale(.5)
translate(500, 500)
myFancyFunction()