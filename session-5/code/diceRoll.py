myAttempts = 0

myDice1 = randint(1, 6)
myDice2 = randint(1, 6)

while (myDice1 == 1 and myDice2 == 1) is False:
    myAttempts += 1
    myDice1 = randint(1, 6)
    myDice2 = randint(1, 6)
    print(myAttempts, myDice1, myDice2)
    
print('It took me', myAttempts, 'tries to roll snake eyes.')