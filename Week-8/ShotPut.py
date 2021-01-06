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

class ShotPutFrame(Frame):
    '''frame for a game of Shot Put'''

    def __init__(self, master, name):
        '''ShotPutFrame(master,name) -> ShotPutFrame
        creates a new Shot Put frame
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
        self.attempt = 0      # keeps track of attempt number
        self.highScore = 0    # keeps track of high score
        self.dieNum = 0       # keeps track of which die you're on
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, -6], ['black'] * 5 + ['red']))
            self.dice[n].grid(row=1, column=n)
        # set up roll and stop buttons
        self.rollButton = Button(self, text='Roll', command=self.roll)
        self.rollButton.grid(row=2, columnspan=1)
        self.stopButton = Button(self, text='STOP', state=DISABLED, command=self.stop)
        self.stopButton.grid(row=3, columnspan=1)

    def roll(self):
        '''ShotPutFrame.roll()
        handler method for the roll button click'''
        self.dice[self.dieNum].roll()                         # roll die
        self.attemptScore += self.dice[self.dieNum].get_top() # increase score
        self.scoreLabel['text'] = 'Score: ' + str(self.attemptScore)
        if self.dieNum < 7:                                   # checks if turn is over
            self.dieNum += 1                                  # goes to next die
            self.rollButton.grid(row=2, column=self.dieNum, columnspan=1)
            self.stopButton.grid(row=3, column=self.dieNum, columnspan=1)
        else:
            self.after(5000, self.stop)

        if self.stopButton['state'] == DISABLED :
            self.stopButton['state'] = ACTIVE

    def stop(self):
        '''ShotPutFrame.stop()
        handler method for the STOP button click'''
        if self.attemptScore > self.highScore: # resets high score if necessary
            self.highScore = self.attemptScore
            self.highScoreLabel['text'] = 'High Score: ' + str(self.highScore)
        self.attemptScore = 0                  # resets attempt score to 0
        self.scoreLabel['text'] = 'Score: 0'
        self.attempt += 1                      # goes to next attempt
        self.attemptLabel['text'] = 'Attempt #' + str(self.attempt)
        self.dieNum = 0
        self.rollButton.grid(row=2, column=self.dieNum, columnspan=1)
        self.stopButton.grid(row=3, column=self.dieNum, columnspan=1)
        for die in self.dice:
            die.erase()
        if self.attempt > 2:
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.attemptLabel['text'] = 'Game over'
        self.stopButton['state'] = DISABLED


# play the game
name = input("Enter your name: ")
root = Tk()
root.title('Shot Put')
game = ShotPutFrame(root, name)
game.mainloop()
