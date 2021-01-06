# Python Class 2532
# Lesson 5 Problem 3
# Author: riatalwar (486154)

import random
from collections import Counter
class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9
      color: string'''

    def __init__(self, rank, color):
        '''UnoCard(rank, color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        return(str(self.color) + ' ' + str(self.rank))

    def is_match(self, other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        return (self.color == other.color) or (self.rank == other.rank) or ('wild' in str(self.rank))

    def set_color_if_wild(self, player):
        if str(self.rank).startswith('wild'):
            if player.name.startswith('computer'):
                colors = [c.color for c in player.hand if 'wild' not in str(c.rank)]
                color = Counter(colors).most_common(1)[0][0]
                self.color = color
                return
            color = None
            while color not in ['red', 'blue', 'green', 'yellow']:
                color = input('What color do you want? ').lower()
            self.color = color


class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0, color))  # one 0 of each color
            self.deck.append(UnoCard('wild', None))
            self.deck.append(UnoCard('wild draw four', None))
            for i in range(2):
                for n in range(1, 10):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n, color))
                for ac in ['skip', 'reverse', 'draw two']:
                    self.deck.append(UnoCard(ac, color))
        random.shuffle(self.deck)  # shuffle the deck
        while str(self.deck[-1].rank).startswith('wild'):
            random.shuffle(self.deck)

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with ' + str(len(self.deck)) + ' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self, pile):
        '''UnoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        if len(self.deck) != 0:
            return
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self, deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has ' + str(self.pile[-1]) + ' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self, card):
        '''UnoPile.add_card(card) -> None
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self, name, deck):
        '''UnoPlayer(name, deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self, deck, pile):
        '''UnoPlayer.draw_card(deck, pile) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        if deck.is_empty():
            deck.reset_deck(pile)
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self, card, pile):
        '''UnoPlayer.play_card(card, pile) -> None
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)

    def pick_card_computer(self, matches, nextPlayer):
        matchesRank = [match.rank for match in matches]
        matchesColor = [match.color for match in matches]
        if len(matches) == 1:
            return matches[0]
        if len(nextPlayer.hand) <= 2:
            if 'draw four wild' in matchesRank:
                return matches[matchesRank.index('draw four wild')]
            elif 'draw two' in matchesRank:
                return matches[matchesRank.index('draw two')]
            elif 'skip' in matchesRank:
                return matches[matchesRank.index('skip')]
            elif 'reverse' in matchesRank:
                return matches[matchesRank.index('reverse')]
        colors = [c.color for c in self.hand if 'wild' not in str(c.rank)]
        bestColors = Counter(colors).most_common()
        for color, count in bestColors:
            if color in matchesColor:
                return matches[matchesColor.index(color)]

    def pick_card_player(self, matches):
        for index in range(len(matches)):
            # print the playable cards with their number
            print(str(index + 1) + ": " + str(matches[index]))
        # get player's choice of which card to play
        choice = 0
        while choice < 1 or choice > len(matches):
            choicestr = input("Which do you want to play? ")
            if choicestr.isdigit():
                choice = int(choicestr)
        return matches[choice - 1]

    def pick_card(self, matches, nextPlayer):
        if self.name.startswith('computer'):
            return self.pick_card_computer(matches, nextPlayer)
        return self.pick_card_player(matches)

    def draw_computer(self, deck, pile):
        print(self.name, "can't play, so it has to draw.")
        newcard = self.draw_card(deck, pile)
        if newcard.is_match(pile.top_card()): # can be played
            print(self.name, "played a", newcard)
            newcard.set_color_if_wild(self)
            self.play_card(newcard, pile)
            print(self.name, 'played a', newcard)
            return newcard.rank
        else:   # still can't play
            print(self.name, "still can't play.")
            return None

    def draw_player(self, deck, pile):
        print("You can't play, so you have to draw.")
        input("Press enter to draw.")
        newcard = self.draw_card(deck, pile)
        print("You drew: " + str(newcard))
        if newcard.is_match(pile.top_card()): # can be played
            print("Good -- you can play that!")
            newcard.set_color_if_wild(self)
            self.play_card(newcard, pile)
            print(self.name, 'played a', newcard)
            return newcard.rank
        else:   # still can't play
            print("Sorry, you still can't play.")
            return None

    def draw(self, deck, pile):
        if self.name.startswith('computer'):
            return self.draw_computer(deck, pile)
        return self.draw_player(deck, pile)

    def take_turn(self, deck, pile, nextPlayer):
        '''UnoPlayer.take_turn(deck, pile) -> None
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        # print player info
        print("It's " + self.name + "'s turn.")
        print(pile)
        if 'computer' not in self.name:
            print("Your hand: ")
            print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.is_match(topcard)]
        if len(matches) > 0:
            cardChoice = self.pick_card(matches, nextPlayer)
            cardChoice.set_color_if_wild(self)
            self.play_card(cardChoice, pile)
            print(self.name, 'played a', cardChoice)
            cardChoiceRank = cardChoice.rank
        else:  # can't play
            cardChoiceRank = self.draw(deck, pile)
        input('Press enter to continue: ')
        return cardChoiceRank

def check_and_take_turn(playerList, deck, pile, currentPlayerNum, lastCard):
    player = playerList[currentPlayerNum]
    if lastCard == 'skip':
        print(player.name, 'has been skipped.')
        lastCard = None
    elif lastCard == 'draw two':
        print(player.name, 'must draw two cards.')
        for i in range(2):
            player.draw_card(deck, pile)
        lastCard = None
    elif lastCard == 'wild draw four':
        print(player.name, 'must draw four cards.')
        for i in range(4):
            player.draw_card(deck, pile)
        lastCard = None
    elif lastCard == 'reverse':
        playerList.reverse()
        lastCard = None
        currentPlayerNum = (playerList.index(player) + 1) % len(playerList)
    else:
        lastCard = playerList[currentPlayerNum].take_turn(deck, pile, (playerList[(currentPlayerNum + 1) % len(playerList)]))
    return currentPlayerNum, lastCard

def play_uno(numPlayers):
    '''play_uno(numPlayers) -> None
    plays a game of Uno with numPlayers'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []
    computerCount = 1
    for n in range(numPlayers):
        # get each player's name, then create an UnoPlayer
        name = input('Player #' + str(n + 1) + ', enter your name or enter "computer" to create a computer player: ')
        if name.lower() == 'computer':
            name = 'computer ' + str(computerCount)
            computerCount += 1
        playerList.append(UnoPlayer(name, deck))
    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers)
    # play the game
    lastCard = None
    while True:
        # print the game status
        print('\n-------\n')
        for player in playerList:
            print(player)
        print('\n-------\n')
        # take a turn
        currentPlayerNum, lastCard = check_and_take_turn(playerList, deck, pile, currentPlayerNum, lastCard)
        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing!")
            break
        # go to the next player
        currentPlayerNum = (currentPlayerNum + 1) % numPlayers

play_uno(4)
