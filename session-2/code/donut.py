newPage(2000, 1000)
myDonutThickness = 200
myDonutWidth = 300
myDonutHeight = myDonutWidth
oval(
    0, 
    0, 
    myDonutWidth, 
    myDonutHeight
)
fill(1)
# oval(x, y, w, h)
oval(
    myDonutThickness, 
    myDonutThickness, 
    myDonutWidth-myDonutThickness*2, 
    myDonutHeight-myDonutThickness*2
)