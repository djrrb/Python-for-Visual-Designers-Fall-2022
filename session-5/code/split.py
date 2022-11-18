myString = """apples,oranges,bananas,pears"""

myList = myString.split(',')
print(len(myList))
print(myList)

for myItem in myList:
    print('this is an item:', myItem)
    