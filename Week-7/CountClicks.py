# Python Class 2532
# Lesson 7 Problem 3
# Author: riatalwar (486154)

from tkinter import *

class HelloWorldFrame(Frame):
    '''creates a hello world window'''

    def __init__(self,master):
        '''HelloWorldFrame()
        creates a new HelloWorldFrame'''
        Frame.__init__(self,master)  # set up as a Tk frame
        self.grid()  # place the frame in the root window
        # create a button
        self.button = Button(self,text='Click me!',command=self.increase_count)
        self.button.grid(row=0,column=0)
        # create a text display
        self.count = 0
        self.countLabel = Label(self,text=str(self.count) + ' clicks so far.')
        self.countLabel.grid(row=1,column=0)

    def increase_count(self):
        '''prints hello world message'''
        self.count += 1
        self.countLabel['text'] = str(self.count) + ' clicks so far.'

root = Tk()
hwf = HelloWorldFrame(root)
hwf.mainloop()
