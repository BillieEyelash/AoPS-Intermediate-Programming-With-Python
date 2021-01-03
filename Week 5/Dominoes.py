# Python Class 2532
# Lesson 5 Problem 4
# Author: riatalwar (486154)

import random

class Domino:

    def __init__(self, side1, side2):
        self.sides = [side1, side2]

    def __str__(self):
        strsides = [str(side) for side in self.sides]
        return ' - '.join(strsides)

    def is_match(self, chain):
        ends = chain.get_ends()
        return self.sides[0] in ends or self.sides[1] in ends

    def reverse(self):
        self.sides.reverse()

class Player:

    def __init__(self, DominoSet, name):
        self.tiles = [DominoSet.pop() for d in range(7)]
        self.name = name

    def __str__(self):
        tiles = [str(tile) for tile in self.tiles]
        return self.name + ': ' + ', '.join(tiles)

    def take_turn_player(self, chain):
        print('\n\nHere is the chain:\n', chain)
        print('\nIt is ' + self.name + "'s turn.")
        print('Here are your tiles:')
        for tile in self.tiles:
            print(tile)
        matches = self.get_matches(chain)
        if self.cannot_play(chain):
            print('\nYou cannot play so you must pass.')
            input('Press enter to continue. ')
            return
        print('\nHere are all the matches:')
        for i in range(len(matches)):
            print(str(i + 1) + ': ' + str(matches[i]))
        choice = 0
        while choice < 1 or choice > len(matches):
            choicestr = input("Which do you want to play? ")
            if choicestr.isdigit():
                choice = int(choicestr)

        tileChoice = matches[choice - 1]
        self.play_tile(chain, tileChoice)
        input('Press enter to continue. ')

    def take_turn_computer(self, chain):
        print('\n\nHere is the chain:\n', chain)
        print('\nIt is ' + self.name + "'s turn.")
        print(self.name, 'has', len(self.tiles), 'tiles.')
        matches = self.get_matches(chain)
        if self.cannot_play(chain):
            print('\nThe computer cannot play.')
            input('Press enter to continue. ')
            return
        choice = random.randint(0, len(matches) - 1)
        tileChoice = matches[choice]
        self.play_tile(chain, tileChoice)
        print('The computer played', tileChoice)
        input('Press enter to continue. ')

    def take_turn(self, chain):
        if self.name.startswith('computer'):
            self.take_turn_computer(chain)
        else:
            self.take_turn_player(chain)

    def cannot_play(self, chain):
        matches = self.get_matches(chain)
        return len(matches) == 0

    def get_matches(self, chain):
        return [tile for tile in self.tiles if tile.is_match(chain)]

    def play_tile(self, chain, tile):
        self.tiles.remove(tile)
        left, right = chain.get_ends()
        if left in tile.sides:
            if left == tile.sides[0]:
                tile.reverse()
            chain.add_tile('left', tile)
        else:
            if right == tile.sides[1]:
                tile.reverse()
            chain.add_tile('right', tile)

    def has_won(self):
        return len(self.tiles) == 0

    def has_domino(self, a=6, b=6):
        for tile in self.tiles:
            if tile.sides == [a, b] or tile.sides == [b, a]:
                return True
        return False

    def get_domino(self, a=6, b=6):
        if self.has_domino(a, b):
            for tile in self.tiles:
                if tile.sides == [a, b] or tile.sides == [b, a]:
                    return tile

class DominoChain:

    def __init__(self):
        self.chain = []

    def __str__(self):
        chain = [str(tile) for tile in self.chain]
        return ', '.join(chain)

    def get_ends(self):
        if len(self.chain) == 0:
            return 6, 6
        left = self.chain[0].sides[0]
        right = self.chain[-1].sides[1]
        return left, right

    def add_tile(self, location, tile):
        if location == 'left':
            self.chain.insert(0, tile)
        else:
            self.chain.append(tile)

def nobody_can_play(players, chain):
    cantPlay = 0
    for p in players:
        if p.cannot_play(chain):
            cantPlay += 1
    return cantPlay == 4

def play_dominoes():
    chain = DominoChain()
    DominoSet = []
    start = 0
    for i in range(7):
        for j in range(start, 7):
            DominoSet.append(Domino(i, j))
        start += 1
    random.shuffle(DominoSet)

    players = [Player(DominoSet, input('Enter your name: '))]
    computerPlayers = [Player(DominoSet, 'computer ' + str(i + 1)) for i in range(3)]
    players.extend(computerPlayers)
    for player in players:
        print(player)
    startingPlayer = [player for player in players if player.has_domino()][0]
    startingPlayer.play_tile(chain, startingPlayer.get_domino())
    print(startingPlayer.name, 'has started the game!')
    input('Press enter to continue: ')
    currentPlayerNum = (players.index(startingPlayer) + 1) % len(players)

    while True:
        player = players[currentPlayerNum]
        if nobody_can_play(players, chain):
            print('Nobody can play, so', players[currentPlayerNum - 1].name, 'wins!')
            break
        player.take_turn(chain)
        if player.has_won():
            print(player.name, 'has won!')
            break
        currentPlayerNum = (currentPlayerNum + 1) % len(players)

play_dominoes()
