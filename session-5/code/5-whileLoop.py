# a simple while loop
# add contents to a string until the string length exceeds 100
myString = 'hello '

# as long as the condition in the while loops is true
# the indented code will loop
while len(myString) < 100:
    # augment string
    myString += 'more '
    print(len(myString), myString)

# once the string length exceeds 100, the loop is stopped
print('done')