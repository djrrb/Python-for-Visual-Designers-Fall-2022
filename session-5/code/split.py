myString = """apples,oranges,bananas,pears"""

print(myString.replace('oranges', 'grapefruit').replace('a', '?'))

print('Bananas' in myString)

print('find', myString.find('orange'))

myList = myString.split(',')
print(len(myList))
print(myList)

for myItem in myList:
    print('this is an item:', myItem)
    