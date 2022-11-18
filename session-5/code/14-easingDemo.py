# import easing_functions
# print(dir(easing_functions))
# print(easing_functions.SineEaseIn)

# import one easing function
from easing_functions import SineEaseIn


# duration of easing
myPageCount = 10
# min value
myMin = 200
# max value
myMax = 900

# get an easing object with min, max, duration
myEasing = SineEaseIn(myMin, myMax, myPageCount)

# loop through each page number
for myPageNumber in range(myPageCount):
    # get easing value for that page number
    print(myPageNumber, myEasing.ease(myPageNumber))