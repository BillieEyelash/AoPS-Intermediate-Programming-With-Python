# Python Class 2532
# Lesson 4 Problem 4
# Author: riatalwar (486154)

import random
from collections import Counter
class Die:
    '''Die class'''

    def __init__(self,sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        if isinstance(sidesParam,int):
            sidesParam = range(1,sidesParam+1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        self.top = random.choice(self.sides)
        return self.top

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

    def flip(self):
        ''' Flips the die onto the opposite side '''
        self.top = self.sides[len(self.sides) - self.sides.index(self.top) - 1]

def find_most_common(tops):
    topsNoW = [t for t in tops if t != 'W']
    return Counter(topsNoW).most_common(1)[0][0]

def calculate_final_score(tops, goal):
    score = tops.count(goal) + tops.count('W')
    if score == len(tops):
        return 'You win!'
    return 'Sorry, you only got ' + str(score) + ' out of ' + str(len(tops)) + '.'

def reroll(tops, goal, die):
    for i in range(len(tops)):
        if tops[i] not in (goal, 'W'):
            die.roll()
            tops[i] = die.get_top()

def europadice():
    die = Die([1, 2, 3, 4, 'W'])
    tops = [die.roll() for i in range(10)]
    goal = find_most_common(tops)
    print(*tops)
    print('Your goal is:', goal)
    for r in ['Reroll #1', 'Reroll #2', 'Reroll #3']:
        input(r + ' Press ENTER to reroll.')
        reroll(tops, goal, die)
        print(*tops)
    print(calculate_final_score(tops, goal))

europadice()


def test_find_most_common():
    print()
    print(find_most_common([1]) == 1)
    print(find_most_common([1, 'W']) == 1)
    print(find_most_common([1, 'W', 'W']) == 1)
    print(find_most_common([1, 2, 2]) == 2)
    print(find_most_common([1, 2, 3, 1]) == 1)

def test_calculate_final_score():
    print()
    print(calculate_final_score([1], 1) == 'You win!')
    print(calculate_final_score([1], 2) == 'Sorry, you only got 0 out of 1.')
    print(calculate_final_score([1, 1], 1) == 'You win!')
    print(calculate_final_score([1, 2], 1) == 'Sorry, you only got 1 out of 2.')

def test():
    test_find_most_common()
    test_calculate_final_score()

#test()
