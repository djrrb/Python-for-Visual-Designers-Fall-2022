# import easing_functions
# print(dir(easing_functions))
# print(easing_functions.SineEaseIn)

myPageCount = 10
myMin = 200
myMax = 900

from easing_functions import SineEaseIn
myEasing = SineEaseIn(myMin, myMax, myPageCount)
for myPageNumber in range(myPageCount):
    print(myPageNumber, myEasing.ease(myPageNumber))