# define a list, this is a sequence of objects
myGroceryList = ['banana', 'apple', 'orange', 'grapefruit']

# for item in sequence
print('how many items in our list?', len(myGroceryList))
print('now loop through our list:')
for myFood in myGroceryList:
    # myFood = 'banana', then 'apple', then 'orange'...
    # print the food, the character count of the food, and the last letter of the food (using a slice)
    print('\t', myFood, len(myFood), myFood[-1])
    # now loop through each character in the food name and print that individually
    for myFoodCharacter in myFood:
        print('\t\t', myFoodCharacter)