# Python Class 2532
# Lesson 4 Problem 3
# Author: riatalwar (486154)

import random
class Pokemon:

    def __init__(self, name, health, att, defense):
        self.name = name
        self.health = health
        self.att = att
        self.defense = defense

    def __str__(self):
        string = self.name + ' has ' + str(self.health) + ' health, ' + str(self.att) + ' attack strength, and ' + str(self.defense) + ' defense.'
        return string

    def calculate_damage(self, opponent):
        return ((12 * self.att) / (5 * opponent.defense)) * random.uniform(0.85, 1.0)

    # TODO: SIMPLIFY
    # TODO: TESTS
    def attack(self, opponent):
        if self.health > 0 and opponent.health > 0:
            damage = self.calculate_damage(opponent)
            opponent.health -= damage
            opponent.health = round(opponent.health)
            print(self.name, 'did', round(damage), 'damage.')
            if opponent.health <= 0:
                print(opponent.name, 'has fainted.')
                opponent.health = 0
        elif opponent.health < 1:
            print(opponent.name, 'has already fainted.')
        else:
            print(self.name, 'cannot attack because they have fainted.')

b = Pokemon('Bulbasaur', 45, 49, 49)

c = Pokemon('Charmander', 39, 52, 43)

for i in range(17):
    c.attack(b)
    print(b, c)
    b.attack(c)
    print(b, c)
