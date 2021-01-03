# Python Class 2532
# Lesson 4 Problem 2
# Author: riatalwar (486154)
import random
class Die:
    '''Die class'''

    def __init__(self, sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        if isinstance(sidesParam,int):
            sidesParam = range(1, sidesParam +1 )
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

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self, value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

    def flip(self):
        ''' Flips the die onto the opposite side '''
        self.top = self.sides[len(self.sides) - self.sides.index(self.top) - 1]

def test():
    s2 = Die(2)
    s2.set_top(1)
    s2.flip()
    print(s2.get_top() == 2)
    s2.flip()
    print(s2.get_top() == 1)

    s5 = Die(5)
    s5.set_top(3)
    s5.flip()
    print(s5.get_top() == 3)

    s6 = Die()
    s6.set_top(3)
    s6.flip()
    print(s6.get_top() == 4)
    s6.flip()
    print(s6.get_top() == 3)

    s4 = Die(['a', 'b', 'c', 'd'])
    s4.set_top('b')
    s4.flip()
    print(s4.get_top() == 'c')

test()
