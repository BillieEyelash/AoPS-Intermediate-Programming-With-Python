# Python Class 2532
# Lesson 1 Problem 4a
# Author: riatalwar (486154)

import random
def guessing_game(guess, number):
    '''Returns whether the user's guess is
    too low, too high, or correct.'''
    if guess == number:
        return 'Correct!'
    elif guess < number:
        return 'Sorry, ' + str(guess) + ' is too low.'
    else: # guess > number
        return 'Sorry, ' + str(guess) + ' is too high.'

def run():
    '''Calls guessing_game() until the answer is correct
    and keeps track of the number of guesses.'''
    print("I'm thinking of a number between 0 and 100.")
    randomNumber = random.randint(0, 100)
    numGuesses = 0
    while True:
        guess = guessing_game(int(input()), randomNumber)
        print(guess)
        numGuesses += 1
        if guess == 'Correct!':
            print('It took you', numGuesses, 'guesses')
            break

def test():
    '''Runs several test cases.'''
    print(guessing_game(25, 50) == 'Sorry, 25 is too low.')
    print(guessing_game(75, 50) == 'Sorry, 75 is too high.')
    print(guessing_game(50, 50) == 'Correct!')

run()
