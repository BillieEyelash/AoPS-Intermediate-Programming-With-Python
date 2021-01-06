# Python Class 2532
# Lesson 4 Problem 5
# Author: riatalwar (486154)

import random

class Die:
    '''Die class'''

    def __init__(self,sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sidesParam,int):
            sidesParam = range(1,sidesParam+1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return str(self.numSides)+'-sided die with '+str(self.top)+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rerolls = 5

    def __str__(self):
        return self.name + ": score " + str(self.score) + ', rerolls ' + str(self.rerolls)

    def take_turn(self):
        die1 = Die([1, 2, 3, 4, 5, -6])
        die2 = Die([1, 2, 3, 4, 5, -6])
        print('\nIt is', self.name + "'s turn.")
        while True:
            input("Press enter to roll.")
            die1.roll()
            die2.roll()
            roundScore = die1.get_top() + die2.get_top()
            print("You rolled", die1.get_top(), "and", die2.get_top(), 'for a total of', roundScore)
            if self.rerolls == 0:
                print("You're out of rerolls so you have to keep this.")
                break

            response = ''
            while response not in ['y','n']:
                response = input("Do you want to reroll (y/n)? ").lower()

            if response == 'n':
                break
            self.rerolls -= 1
            print("OK, you have", self.rerolls, "rerolls left.")

        self.score += roundScore

def print_scores(playerList):
    for player in playerList:
        print(player)

def decathlon_400_meters():
    '''decathlon_400_meters()
    plays a multi-player version of Reiner Knizia's 400 Meters'''
    numPlayers = int(input('Enter number of players: '))
    playerList = []
    for i in range(numPlayers):
        name = input('Player ' + str(i + 1) + ', enter your name: ')
        playerList.append(Player(name))
    for round in range(1, 5):
        print('\n\n' + 'Round #' + str(round))
        for i in range(numPlayers):
            print_scores(playerList)
            playerList[i].take_turn()
    print('\nFinal Scores:')
    print_scores(playerList)
decathlon_400_meters()
