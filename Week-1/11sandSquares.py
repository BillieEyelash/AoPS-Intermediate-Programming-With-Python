# Python Class 2532
# Lesson 1 Problem 2
# Author: riatalwar (486154)

# There are two 3-digit numbers n having the property
# that n is divisible by 11 and
# n/11 is equal to the sum of the squares of the digits of n.
# Find both values of n. You may submit them in either order.
def find_numbers():
    numbers = []
    for n in range(99, 1000, 11):
        sumOfSquares = ((n // 100) ** 2) + (((n // 10) % 10) ** 2) + ((n % 10) ** 2)
        if n / 11 == sumOfSquares:
            numbers.append(n)
    return numbers

print(find_numbers())
