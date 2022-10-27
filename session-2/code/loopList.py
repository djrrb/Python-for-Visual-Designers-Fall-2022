myGroceryList = ['banana', 'apple', 'orange', 'grapefruit']
numericList = [10, 5, 20345, 2359, 2420, 102]
thingsOnMyDesk = ['pen', 'computer', 'book']
# for item in sequence
for myFood in myGroceryList:
    # slice: myFood[0]
    # len()
    print(myFood, len(myFood), myFood[-1])
    for myFoodCharacter in myFood:
        print('\t', myFoodCharacter)
print(len(myGroceryList))
print('----')
print(myGroceryList[2][0])