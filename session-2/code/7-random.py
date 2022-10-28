# import the shuffle function from the random library 


myString = 'abcdefghijklmnopqrstuvwxyz'
myList = list(myString)

print(myList)
print('')

shuffle(myList)
print('shuffle our list')
print(myList)

print('\nchoose an item at random from our list:')
print(choice(myList))

