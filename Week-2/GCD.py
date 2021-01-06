# Python Class 2532
# Lesson 2 Problem 1
# Author: riatalwar (486154)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(abs(a - b), min([a, b]))


def test():
    print(gcd(0, 0) == 0)
    print(gcd(1, 0) == 1)
    print(gcd(0, 1) == 1)
    print(gcd(0, 2) == 2)
    print(gcd(2, 2) == 2)
    print(gcd(2, 3) == 1)
    print(gcd(6, 4) == 2)

test()
