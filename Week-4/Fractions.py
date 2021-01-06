# Python Class 2532
# Lesson 4 Problem 6
# Author: riatalwar (486154)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(abs(a - b), min([a, b]))

class Fraction:
    '''represents fractions'''

    def __init__(self, num, denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0:
            raise ZeroDivisionError
        g = gcd(abs(num), abs(denom))
        num //= g
        denom //= g

        if denom < 0:
            num *= -1
            denom *= -1
        self.num = num
        self.denom = denom

    def __str__(self):
        ''' Converts a fraction to a string '''
        return str(self.num) + '/' + str(self.denom)

    def __float__(self):
        ''' Converts a fraction to a float '''
        return self.num / self.denom

    def __add__(self, frac):
        ''' Finds the sum of two fractions '''
        n = self.num * frac.denom + frac.num * self.denom
        d = self.denom * frac.denom
        return Fraction(n, d)

    def __sub__(self, frac):
        ''' Finds the difference of two fractions '''
        n = self.num * frac.denom - frac.num * self.denom
        d = self.denom * frac.denom
        return Fraction(n, d)

    def __mul__(self, frac):
        ''' Finds the product of two fractions '''
        n = self.num * frac.num
        d = self.denom * frac.denom
        return Fraction(n, d)

    def __truediv__(self, frac):
        ''' Finds the quotient of two fractions '''
        n = self.num * frac.denom
        d = self.denom * frac.num
        return Fraction(n, d)


    def __eq__(self, frac):
        ''' Checks if two fractions are equal '''
        return self.num == frac.num and self.denom == frac.denom

def test_init():
    print('__INIT__')
    print(str(Fraction(1, 1)) == '1/1')
    print(str(Fraction(2, 2)) == '1/1')
    print(str(Fraction(2, 6)) == '1/3')
    print(str(Fraction(-2, 6)) == '-1/3')
    print(str(Fraction(-2, -6)) == '1/3')
    print(str(Fraction(2, -6)) == '-1/3')
    print(str(Fraction(10,-60)) == '-1/6')
    print(str(Fraction(-24,-48)) == '1/2')


def test_float():
    print('FLOAT')
    p = Fraction(1,2)
    x = float(p)
    print(x == 0.5)

def test_add():
    print()
    print('ADDITION')
    p = Fraction(3,6)
    q = Fraction(10,-60)
    s = Fraction(-1, 2)
    t = Fraction(2, 3)
    print(str(p + q) == '1/3')
    print(str(p + p) == '1/1')
    print(str(p + s) == '0/1')
    print(str(p + t) == '7/6')

def test_sub():
    print()
    print('SUBTRACTION')
    p = Fraction(3,6)
    q = Fraction(10,-60)
    print(str(p - p) == '0/1')
    print(str(p - q) == '2/3')
    print(str(q - p) == '-2/3')

def test_mult():
    print()
    print('MULTIPLICATION')
    p = Fraction(3,6)
    q = Fraction(10,-60)
    r = Fraction(0, 1)
    print(str(p * q) == '-1/12')
    print(str(p * p) == '1/4')
    print(str(p * r) == '0/1')

def test_div():
    print()
    print('DIVISION')
    p = Fraction(3,6)
    q = Fraction(10,-60)
    r = Fraction(-24,-48)
    print(str(p / q) == '-3/1')
    print(str(p / r) == '1/1')
    print(str(q / r) == '-1/3')

def test_eq():
    print()
    print('EQUAL')
    p = Fraction(3,6)
    q = Fraction(10,-60)
    r = Fraction(-24,-48)
    print((p == r) == True)
    print((p == q) == False)
    print((r == q) == False)

def test():
    test_init()
    test_float()
    test_add()
    test_sub()
    test_mult()
    test_div()
    test_eq()
    print()
    print(str(Fraction(1, 2) + (Fraction(2, 3) - Fraction(1, 3)) * Fraction(3, 4) / Fraction(1, 2)) == '1/1')

test()
