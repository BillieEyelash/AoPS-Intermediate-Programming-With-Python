# Python Class 2532
# Lesson 7 Problem 1
# Author: riatalwar (486154)

import turtle
import random

# you should add handlers
def move():
    tRed.forward(random.randint(1, 50))
    tBlue.forward(random.randint(1, 50))
    tGreen.forward(random.randint(1, 50))

def left():
    tRed.left(15)
    tBlue.left(30)
    tGreen.left(40)

def right():
    tRed.right(15)
    tBlue.right(30)
    tGreen.right(40)
# set up window and turtles
wn = turtle.Screen()
tRed = turtle.Turtle()
tRed.color('red')
tBlue = turtle.Turtle()
tBlue.color('blue')
tGreen = turtle.Turtle()
tGreen.color('green')

wn.onkey(move, 'Up')
wn.onkey(right, 'Right')
wn.onkey(left, 'Left')

# listen and run
wn.listen()
wn.mainloop()
