# Python Class 2532
# Lesson 3 Problem 5
# Author: riatalwar (486154)
# Fill the jar:
    # the jar is completely filled with water.
# Empty the jar:
    # the jar is emptied completely and contains no water.
# Pour into the other jar:
    # water is poured from jar A into jar B until either:
    # (1) jar A runs out of water and is empty;
    # (2) jar B becomes full, and jar A contains any leftover water. Notice that no water is lost while pouring,
    # we are not allowed to pour "halfway" -- we must pour until either the source jar is empty or the destination jar is full (whichever happens first).

# Write a new Python class called Jar to simulate a jar from this puzzle.
    # constructor method to create a new empty jar (where the capacity of the jar is passed as a parameter),
    # a string conversion method to return the status of a jar (for example, "a 3-liter jar with 2 liters of water")
    # method for each of the three operations listed above.

# Then, write a program that creates two jars of sizes 3-liters and 5-liters,
# perform the necessary operations to result in the 5-liter jar containing exactly 4 liters of water.

class Jar:

    def __init__(self, capacity):
        self.capacity = capacity
        self.liters = 0

    def __str__(self):
        return str(self.capacity) + '-liter jar with ' + str(self.liters) + ' liters'

    def fill_jar(self):
        self.liters = self.capacity

    def empty_jar(self):
        self.liters = 0

    def pour(self, otherJar):
        while self.liters > 0 and otherJar.liters < otherJar.capacity:
            self.liters -= 1
            otherJar.liters += 1

liter5 = Jar(5)
liter3 = Jar(3)
print(liter5, '||', liter3)
liter5.fill_jar()
print(liter5, '||', liter3)
liter5.pour(liter3)
print(liter5, '||', liter3)
liter3.empty_jar()
print(liter5, '||', liter3)
liter5.pour(liter3)
print(liter5, '||', liter3)
liter5.fill_jar()
print(liter5, '||', liter3)
liter5.pour(liter3)
print(liter5, '||', liter3)
