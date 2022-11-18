# keep track of how many times we roll
myAttempts = 0

# roll the first time
myDice1 = randint(1, 6)
myDice2 = randint(1, 6)

# declare the while loop
# as long as we don’t roll snake eyes, keep rolling
while (myDice1 == 1 and myDice2 == 1) is False:
    # augment attempt count
    myAttempts += 1
    # roll the dice
    myDice1 = randint(1, 6)
    myDice2 = randint(1, 6)
    # print the results
    print('Attempt', myAttempts, ':', myDice1, myDice2)
    
# once we roll snake eyes the loop will stop
print('It took me', myAttempts, 'tries to roll snake eyes.')