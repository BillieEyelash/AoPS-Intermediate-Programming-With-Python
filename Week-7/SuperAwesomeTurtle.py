# Python Class 2532
# Lesson 7 Problem 5 Part (b)
# Author: riatalwar (486154)

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):
        ''' Creates a SuperAwesomeTurtle '''
        turtle.Turtle.__init__(self)

        # set up widgets
        self.getscreen().onkey(self.go_faster,'Up')
        self.getscreen().onkey(self.go_slower,'Down')
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

    def go_faster(self):
        ''' Increase turtle speed by
            25 units per minutes '''
        self.speed += 1

    def go_slower(self):
        ''' Decrease turtle speed by
            25 units per minutes '''
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

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()
