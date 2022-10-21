# make a variable to define how many times we want to loop
myPageCount = 10
# convert that number to a range of numbers, starting at 0
myPageRange = range(myPageCount)

# loop through each item in a sequence
# "for item in sequence:"
#    'item' is a new variable we define to represent the current item 
#    'sequence' is the sequence we will loop through 
#    end the line with a colon and indent the following line
#    all indented code will be run once per loop
# dedenting ends the loop

for myPageNumber in myPageRange:
    # all indented code will be run once for each item
    # ten times total
    print(myPageNumber)
