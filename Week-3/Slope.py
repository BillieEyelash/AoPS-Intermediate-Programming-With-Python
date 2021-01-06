# Python Class 2532
# Lesson 3 Problem 3 Part (a)
# Author: riatalwar (486154)
# what if the slope is negative
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope(self, otherPoint):
        ''' Calculate the slope from myself to otherPoint '''
        x = self.x - otherPoint.x
        if x == 0:
            return 'undefined'
        y = self.y - otherPoint.y
        return y/x

def test():
    p = Point(1,-2)
    q = Point(3,5)
    r = Point(3,7)
    print(p.slope(q) == 3.5)  # should be 3.5
    print(q.slope(p) == 3.5)  # should be 3.5
    print(q.slope(r) == 'undefined')  # should print "undefined"
test()
