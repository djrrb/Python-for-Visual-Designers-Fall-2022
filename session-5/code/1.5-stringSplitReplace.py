# make a string with a delimiter
myString = """apples,oranges,bananas,pears"""

# we can replace items in the string
print(myString.replace('oranges', 'grapefruit').replace('a', '?'))

# we can look for things in the string
print('Bananas' in myString)

# we can find the position of the first use of a word
print('find', myString.find('orange'))

# we can split the string into a list by feeding .split() the delimiter to split by
myList = myString.split(',')
print(len(myList), 'items in list')
print(myList)

# and we can loop through that list
for myItem in myList:
    print('this is an item:', myItem)
    