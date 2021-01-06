# Python Class 2532
# Lesson 1 Problem 1 Part (b)
# Author: riatalwar (486154)

def calculate_score(numAnswered, numCorrect):
    '''Calculates the score'''
    return numCorrect * 6 + (25 - numAnswered) * 1.5

def run():
    '''Gets user input and prints the score'''
    numAnswered = int(input("Enter the number of questions answered: "))
    numCorrect = int(input("Enter the number of questions correct: "))
    score = calculate_score(numAnswered, numCorrect)

    print("The student's score is: " + str(score))

def test():
    '''Runs several test cases'''
    print(calculate_score(25, 1) == 6)
    print(calculate_score(25, 25) == 150)
    print(calculate_score(1, 1) == 42)
    print(calculate_score(2, 1) == 40.5)

run()
