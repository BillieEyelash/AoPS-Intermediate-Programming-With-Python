# Python Class 2532
# Lesson 1 Problem 3
# Author: riatalwar (486154)

def find_double_perfect():
    for n in range(121, 1000):
        divisors = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                divisors.append(i)
        if sum(divisors) == 2 * n:
            return n

print(find_double_perfect())
