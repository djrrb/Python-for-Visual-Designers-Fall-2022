# make as string that is a delimeter
myString = ','

# have a list
myList = ['apples', 'oranges', 'bananas']

# make a string that joins the list together
# with the delimiter in between
print(myString.join(myList))

# we can also join a list into a string by building it up in a loop

# make an empty string
myString = ''
# loop through list
for myItem in myList:
    # augment string by adding the item and a delimieter
    myString += myItem + ';'
    
print(myString)