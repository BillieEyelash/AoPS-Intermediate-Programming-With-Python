# If you ask them to turn left, 25% of the time they'll turn right instead
# if you ask them to turn right, 25% of the time they'll turn left instead.

# Python Class 2532
# Lesson 6 Problem 3
# Author: riatalwar (486154)

import turtle
import random

class MisbehavingTurtle(turtle.Turtle):

    def __init__(self):
        ''' Creates a new turtle '''
        turtle.Turtle.__init__(self)        # just a normal turtle

    def right(self, deg):
        ''' right() overrides the original turtle command,
        and only turns right 75% of the time '''
        randomNum = random.randint(1, 4)    # picks a random number
        if randomNum == 4:                  # turns in the wrong direction 1/4 of the time
            turtle.Turtle.left(self, deg)
        else:                               # otherwise goes in the right direction
            turtle.Turtle.right(self, deg)

    def left(self, deg):                    # same process as right() but the directions are swapped
        ''' left() overrides the original turtle command,
        and only turns left 75% of the time '''
        randomNum = random.randint(1, 4)
        if randomNum == 4:
            turtle.Turtle.right(self, deg)
        else:
            turtle.Turtle.left(self, deg)


# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)

# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)     # draws a nice octagon and square
spice = MisbehavingTurtle()
spice.color('red')
drawing_test(spice)     # goes in the wrong direction 25% of the time
wn.mainloop()
