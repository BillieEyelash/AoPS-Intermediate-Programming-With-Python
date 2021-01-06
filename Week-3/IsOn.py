# Python Class 2532
# Lesson 3 Problem 3 Part (b)
# Author: riatalwar (486154)
# Write a method r.is_on(p,q) that returns True if the point represented by r is on the line through points p and q, and False if it is not.

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

    def is_on(self, p, q):
        ''' Calculate whether I am on the line pq '''
        return self.slope(p) == p.slope(q)

def test():
    p = Point(0,0)
    q = Point(3,6)
    r = Point(1,2)
    s = Point(2,3)
    print(r.is_on(p,q) == True)   # should be True
    print(s.is_on(p,q) == False)   # should be False
test()
