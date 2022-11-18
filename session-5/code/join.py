myString = ','

myList = ['apples', 'oranges', 'bananas']

print(myString.join(myList))

myString = ''
for myItem in myList:
    myString += myItem + ';'
    
print(myString)