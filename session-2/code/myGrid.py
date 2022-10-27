newPage(1000, 1000)
myRowCount = 10
myColCount = 10
myX = 0
myY = 0
for myRowNumber in range(myRowCount):
    print('start my row loop')
    for myColNumber in range(myColCount):
        print('\tdraw a shape')
        oval(myX, myY, 100, 100) # runs 100 times
        myX += 100 # runs 100 times
    print('offset for the next row')
    myY += 100 # runs 10 times
    myX = 0
print('done')