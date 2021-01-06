# Python Class 2532
# Lesson 7 Problem 6
# Author: riatalwar (486154)

import turtle
import random

class PlayerTurtle(turtle.Turtle):

    def __init__(self):
        ''' Creates a SuperAwesomeTurtle '''
        turtle.Turtle.__init__(self)

        # set up widgets
        self.getscreen().onkey(self.faster,'Up')
        self.getscreen().onkey(self.slower,'Down')
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.quit,'q')
        self.getscreen().onkey(self.left,'Left')
        self.getscreen().onkey(self.right,'Right')

        self.speed = 0
        self.goforward()

    def goforward(self):
        ''' Continuously goes forward
            at a specific speed '''
        self.forward(self.get_speed())
        self.getscreen().ontimer(self.goforward, 40)

    def faster(self):
        if self.get_speed() < 5:
            self.speed += 1

    def slower(self):
        self.speed -= 1

    def stop(self):
        ''' Stops the turtle '''
        self.speed = 0

    def quit(self):
        ''' Ends the program '''
        self.getscreen().bye()

    def left(self):
        ''' Turns left 60 degrees '''
        turtle.Turtle.left(self, 90)

    def right(self):
        ''' Turns right 60 degrees '''
        turtle.Turtle.right(self, 90)

    def get_speed(self):
        ''' Returns speed '''
        return self.speed


class BadTurtle(turtle.Turtle):

    def __init__(self):
        ''' Creates a SuperAwesomeTurtle '''
        turtle.Turtle.__init__(self)

        self.speed = random.choice([4, 8, 16, 20, 32, 40, 80])
        self.mileage = 0

    def forward(self):
        ''' Continuously goes forward
            at a specific speed '''
        if self.get_mileage() % 800 == 0 and self.get_mileage() != 0:
            self.right(180)
        turtle.Turtle.forward(self, self.get_speed())
        self.mileage += self.get_speed()
        self.getscreen().ontimer(self.forward, 40)

    def get_speed(self):
        ''' Returns speed '''
        return self.speed

    def get_mileage(self):
        return self.mileage

def play_turtle_game():
    player = PlayerTurtle()
    player.shape('turtle')
    player.penup()
    player.goto(-600, 0)

    #for i in range(10):
    #    bad = BadTurtle()
    #    bad.color('red')
    #    bad.penup()
    #    bad.goto(100*(i - 4), 400)
    #    bad.right(90)
    #    bad.forward()

#    badTurtles = [BadTurtle() for i in range(10)]
#    x = -500
#    for turtle in badTurtles:
#        turtle.penup()
#        turtle.color('red')
#        turtle.goto(x, 400)
#        turtle.right(90)
#        x += 100
#    for turtle in badTurtles:
#        turtle.forward()

play_turtle_game()
wn = turtle.Screen()
wn.listen()
wn.mainloop()
