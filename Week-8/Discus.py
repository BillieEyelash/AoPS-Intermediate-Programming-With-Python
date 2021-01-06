from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self, master, valueList, colorList)
        self.frozen = False

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.frozen

    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        if self.is_frozen():
            self.frozen = False
            self.configure(bg='white')
        else:
            self.frozen = True
            self.configure(bg='gray')

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if self.is_frozen() == False:
            GUIDie.roll(self)

class DiscusFrame(Frame):
    '''frame for a game of Discus'''

    def __init__(self, master, name):
        '''Discus(master,name) -> DiscusFrame
        creates a new Discus frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self, text=name, font=('Arial', 16)).grid(columnspan=2, sticky=W)
        # set up attempt, score, and high score labels
        self.attemptLabel = Label(self, text='Attempt #1', font=('Arial', 16))
        self.attemptLabel.grid(row=0, column=2, columnspan=2, sticky=E)
        self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 16))
        self.scoreLabel.grid(row=0, column=4, columnspan=2, sticky=W)
        self.highScoreLabel = Label(self, text='High Score: 0', font=('Arial', 16))
        self.highScoreLabel.grid(row=0, column=6, columnspan=2, sticky=W)

        # initialize game data
        self.attemptScore = 0 # keeps track of score per attempt
        self.attempt = 1      # keeps track of attempt number
        self.highScore = 0    # keeps track of high score
        # set up dice
        self.dice = []
        self.freezeButtons = []
        for i in range(5):
            self.dice.append(GUIFreezeableDie(self, [1, 2, 3, 4, 5, 6], ['red', 'black'] * 3))
            self.dice[i].grid(row=1, column=i)
            self.freezeButtons.append(Button(self, text='Freeze', state=DISABLED, command=lambda n=i: self.freeze(n)))
            self.freezeButtons[i].grid(row=2, column=i)

        # set up roll and stop buttons
        self.rollButton = Button(self, text='Roll', command=self.roll)
        self.rollButton.grid(row=1, column=6, columnspan=2)
        self.stopButton = Button(self, text='Stop', state=DISABLED, command=self.stop)
        self.stopButton.grid(row=2, column=6, columnspan=2)

    def roll(self):
        '''DiscusFrame.roll()
        handler method for the roll button click'''
        self.attemptScore = 0
        isFoul = True
        allFrozen = True
        for n in range(5):
            self.dice[n].roll()                 # roll die
            if self.dice[n].get_top() % 2 == 0: # increase score if even
                self.attemptScore += self.dice[n].get_top()
                self.freezeButtons[n]['state'] = ACTIVE
                if self.dice[n].is_frozen() == False:
                    isFoul = False
            if self.dice[n].is_frozen() == False:
                allFrozen = False

        if isFoul:
            self.stopButton['text'] = 'FOUL'
            self.stopButton['command'] = self.foul
            while self.stopButton['state'] == ACTIVE:
                continue
        if allFrozen:
            self.stop()
        self.scoreLabel['text'] = 'Score: ' + str(self.attemptScore)
        self.stopButton['state'] = ACTIVE
        self.rollButton['state'] = DISABLED

    def stop(self):
        '''DiscusFrame.stop()
        handler method for the Stop button click'''
        if self.attemptScore > self.highScore: # resets high score if necessary
            self.highScore = self.attemptScore
            self.highScoreLabel['text'] = 'High Score: ' + str(self.highScore)
        self.attemptScore = 0                  # resets attempt score to 0
        self.scoreLabel['text'] = 'Score: 0'
        self.attempt += 1                      # goes to next attempt
        self.attemptLabel['text'] = 'Attempt #' + str(self.attempt)
        for n in range(5):
            self.dice[n].erase()                         # roll die
            if self.dice[n].is_frozen():
                self.dice[n].toggle_freeze()
            self.freezeButtons[n]['state'] = DISABLED
        if self.attempt > 3:
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.attemptLabel['text'] = 'Game over'
        self.stopButton['state'] = DISABLED
        self.rollButton['state'] = ACTIVE

    def freeze(self, id):
        '''DiscusFrame.stop()
        handler method for the Freeze button click'''
        self.rollButton['state'] = ACTIVE
        self.dice[id].toggle_freeze()

    def foul(self):
        self.stopButton['text'] = 'Stop'
        self.stopButton['command'] = self.stop
        self.stop()


# play the game
name = input("Enter your name: ")
root = Tk()
root.title('Discus')
game = DiscusFrame(root, name)
game.mainloop()
