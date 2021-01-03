# Python Class 2532
# Lesson 1 Problem 4b
# Author: riatalwar (486154)

def get_next_guess(guess, previousGuess, lowHigh):
    '''Gets the next guess by taking the average of the guess and
    the guess +/- the different between the guess and previous guess'''
    if lowHigh == 'low':
        nextGuess = (guess + (guess + abs(guess - previousGuess))) // 2 + 1
        if nextGuess > 100:
            nextGuess = 100
        return nextGuess
    elif lowHigh == 'high':
        nextGuess = (guess + (guess - abs(guess - previousGuess))) // 2
        if nextGuess < 0:
            nextGuess = 0
        return nextGuess

def run():
    '''Counts the number of guesses and keeps calling and
    printing get_next_guess until the answer is correct'''
    previousGuess = 0
    guess = 50
    numGuesses = 0
    print('Think of a number between 0 and 100.')
    while True:
        print('I guess', guess)
        lowHigh = input('Is my guess low, high, or correct? ')
        numGuesses += 1
        if lowHigh == 'correct':
            print('It took me', numGuesses, 'guesses.')
            break
        previousGuess, guess = guess, get_next_guess(guess, previousGuess, lowHigh)

run()

# ask user to think of a randomNumber
# guess 50
# if high guess 25
# if low guess 75
# previous guess = 50
# current = 75/25
