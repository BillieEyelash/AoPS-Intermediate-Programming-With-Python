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

class HighJumpFrame(Frame):
    '''frame for a game of HighJump'''

    def __init__(self, master, name):
        '''HighJump(master,name) -> HighJumpFrame
        creates a new HighJump frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self, text=name, font=('Arial', 16)).grid(columnspan=2, sticky=W)
        # set up attempt, score, and high score labels
        self.attemptLabel = Label(self, text='Attempt #1', font=('Arial', 16))
        self.attemptLabel.grid(row=0, column=2, columnspan=2, sticky=E)
        self.heightLabel = Label(self, text='Height: 10', font=('Arial', 16))
        self.heightLabel.grid(row=0, column=4, columnspan=2, sticky=W)
        self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 16))
        self.scoreLabel.grid(row=0, column=6, columnspan=2, sticky=W)

        # initialize game data
        self.height = 10      # keeps track of height
        self.attempt = 1      # keeps track of attempt number
        self.score = 0    # keeps track of high score
        # set up dice
        self.dice = []
        for n in range(5):
            self.dice.append(GUIDie(self))
            self.dice[n].grid(row=1, column=n)

        # set up roll and skip buttons
        self.rollButton = Button(self, text='Jump', command=self.roll)
        self.rollButton.grid(row=1, column=6, columnspan=2)
        self.skipButton = Button(self, text='Skip', state=DISABLED, command=self.skip)
        self.skipButton.grid(row=2, column=6, columnspan=2)

    def roll(self):
        '''HighJumpFrame.roll()
        handler method for the roll button click'''
        height = 0
        for die in self.dice:
            die.roll()
            height += die.get_top()
        if height > self.height:
            self.attempt = 1
            self.score = self.height
            self.height += 2
            self.skipButton['state'] = ACTIVE
        elif self.attempt > 2:
            self.rollButton['state'] = DISABLED
            self.skipButton['state'] = DISABLED
            self.attemptLabel['text'] = 'Game Over'
        else:
            self.attempt += 1
            self.skipButton['state'] = DISABLED

        self.attemptLabel['text'] = 'Attempt #' + str(self.attempt)
        self.scoreLabel['text'] = 'Score: ' + str(self.score)
        self.heightLabel['text'] = 'Height: ' + str(self.height)

    def skip(self):
        '''HighJumpFrame.skip()
        handler method for the Skip button click'''
        self.height += 2
        self.heightLabel['text'] = 'Height: ' + str(self.height)


# play the game
name = input("Enter your name: ")
root = Tk()
root.title('HighJump')
game = HighJumpFrame(root, name)
game.mainloop()
