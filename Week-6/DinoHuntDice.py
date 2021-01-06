# Python Class 2532
# Lesson 6 Problem 5
# Author: riatalwar (486154)

import random

class Die:
    '''Die class'''

    def __init__(self, sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides, int):
            self.numSides = sides
            self.sides = list(range(1, sides + 1))
        else:  # use the list/tuple provided
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top.'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self, value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

class DinoDie(Die):
    '''implements one die for Dino Hunt'''

    def __init__(self, color):
        ''' Creates a DinoDie based off of color '''
        self.color = color
        self.numSides = 6
        if color == 'green':    # creates a green die
            self.sides = ['dinosaur', 'dinosaur', 'dinosaur', 'leaves', 'leaves', 'foot']
        if color == 'yellow':   # creates a yellow die
            self.sides = ['dinosaur', 'dinosaur', 'leaves', 'leaves', 'foot', 'foot']
        else:                   # creates a red die
            self.sides = ['dinosaur', 'leaves', 'leaves', 'foot', 'foot', 'foot']
        self.roll()             # rolls the die and sets self.top

    def __str__(self):
        ''' DinoDie -> str with color and self.top '''
        return 'A ' + self.color + ' die with a ' + self.get_top() + ' on top'

class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__(self, name):
        ''' Creates a DinoPlayer with a name and score '''
        self.name = name
        self.score = 0

    def __str__(self):
        ''' DinoPlayer -> str with name and self.score '''
        return self.name + ': ' + str(self.score)

    def get_score(self):
        ''' Gets the player's score '''
        return self.score

    def turn_is_over(self, dice): # checks whether their turn is over
        ''' Determines whether the player's turn is over '''
        if len(dice) == 0:        # no more die
            print('There are no more dice so you cannot reroll.')
            return True

        response = ''             # player doesn't want to continue
        while response not in ['y', 'n']:
            response = input('Do you want to reroll? (y/n) ')
        return response == 'n'

    def take_turn(self, dice):
        ''' Takes a turn '''
        print('\n--------------------\n\nIt is ' + self.name + "'s turn.\n" + str(self))
        rolledDice = []
        counter = {'dinosaur': 0, 'foot': 0}    # keeps track of how many feet and dinos the player has
        while True:
            rolls = random.sample(dice, 3)
            for die in rolls:
                die.roll()
                top = die.get_top()
                if top != 'leaves':    # adds die to rolledDice if it is a foot/dino
                    dice.remove(die)
                    rolledDice.append(die)
                    counter[top] += 1  # increases dino/foot count
                if len(dice) == 0:
                    break
            rolls = [str(die) for die in rolls]
            print('You rolled:\n' + '\n'.join(rolls))

            if counter['foot'] >= 3:    # checks is player has been stomped
                print('You have been stomped!')
                break

            if self.turn_is_over(dice): # if turn is over - increase score
                self.score += counter['dinosaur']
                break
        dice.extend(rolledDice)    # puts all the dice back into the original list
        print('Your score is', self.get_score())
        input('Press enter to continue: ')

def play_dino_hunt(numPlayers, numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    players = []                    # creates the players
    for i in range(numPlayers):
        players.append(DinoPlayer(input('Enter you name: ')))

    diceCount = {'green': 6, 'yellow': 4, 'red': 3}
    dice = []                       # creates the dice
    for color, count in diceCount.items():
        for i in range(count):
            dice.append(DinoDie(color))

    for i in range(numRounds):      # plays the rounds
        print('\n--------------------\n\nRound #' + str(i + 1))
        for player in players:      # print the scores
            print(player)
        for player in players:      # each player takes a turn
            player.take_turn(dice)

    print('\n--------------------\n\nHere are the final scores:')
    for player in players:          # print the final scores
        print(player)
    scores = [player.get_score() for player in players]
    winner = players[scores.index(max(scores))]     # calculate the winner
    print(winner.name, 'wins!')

play_dino_hunt(3, 3)
