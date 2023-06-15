# Simple number guessing game.
# Input a range, and guess the random number within the range.

import random

# Initial setup. Taking input, choosing random num, declaring variables
minRange = int(input('Enter minimum of the range: '))
maxRange = int(input('Enter maximum of the range: '))
num = random.randint(minRange, maxRange)

count = 0
win = False

# Game logic
while count < 5:
    # Checks if the guess is in range
    guess = 0
    inRange = False
    while not inRange:
        guess = int(input('Make your guess: '))
        if guess > maxRange or guess < minRange:
            print('Guess not in range. Guess again')
        else:
            inRange = True
    # Checks if the guess is smaller, larger, or equal.
    if guess < num:
        print('The number is larger.')
    elif guess > num:
        print('The number is smaller.')
    else:
        win = True
        break
    count += 1
    chances = 5 - count
    print('You have ', chances, 'guesses remaining\n')

# Win or lose statement
if count <= 5 and win:
    print('You win!')
else:
    print('You lose :(. The number was ', num)
