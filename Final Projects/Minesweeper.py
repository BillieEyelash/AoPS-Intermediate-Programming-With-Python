from tkinter import Canvas, Frame, Label, Tk, messagebox
import random

class MinesweeperTile(Label):
    ''' Tile in a game of Minesweeper '''

    def __init__(self, master, bomb=False, value=''):
        Label.__init__(self, master, width=2, text='', font=('Arial', 12), relief='raised')
        self.flagged = False
        self.bomb = bomb
        self.exposed = False
        self.value = value

    def expose(self):
        ''' self.expose() exposes a tile
        if it is not a bomb '''
        if self.is_bomb() == False:     # only expose tiles that aren't bombs
            # sets the text color based on the colormap
            colormap = ['black', 'blue', 'darkgreen', 'red', 'purple', 'maroon',' cyan', 'black', 'dim gray']
            self['relief'] = 'sunken'   # sunken appearence
            self['bg'] = 'grey'         # changes the background color to grey
            self['fg'] = colormap[self.value]
            self['text'] = self.value   # reveals the number of nearby bombs
            if self.is_blank():         # no text if blank
                self['text'] = ''
            self.exposed = True
            self.flagged = False        # if exposing a flagged tile

    def flag(self):
        ''' self.flag() marks a tile as flagged '''
        if not self.is_exposed(): # can only flag non-exposed tiles
            self['text'] = '*'
            self.flagged = True

    def is_flagged(self):
        ''' self.is_flagged() returns True if self
        is flagged or False if it is not '''
        return self.flagged

    def is_bomb(self):
        ''' self.is_bomb() returns True if self
        is a bomb or False if it is not '''
        return self.bomb

    def is_exposed(self):
        ''' self.is_exposed() returns True if self
        is exposed or False if it is not '''
        return self.exposed

    def is_blank(self):
        ''' self.is_blank() returns True if self
        is blank and not a bomb, or False otherwise '''
        return self.value == 0 and not self.is_bomb()

class MinesweeperFrame(Frame):
    ''' Frame for a game of Minesweeper '''

    def __init__(self, master, rows, columns, numBombs):
        Canvas.__init__(self, master)
        self.grid()
        # set the bomb label
        self.bombsLeft = numBombs      # keeps track of the remaining bombs
        self.bombLabel = Label(text=self.bombsLeft, font=('Arial', 24))
        self.bombLabel.grid(row=rows, columnspan=columns)
        self.tiles = {}
        self.rows = rows
        self.columns = columns

        # creates a list of numBombs Trues and the rest False and scrambles it
        bombsList = numBombs * [True] + (rows * columns - numBombs) * [False]
        random.shuffle(bombsList)
        # creates a dict of bomb location based off of rows and columns
        bombsDict = {(r, c): bombsList[self.columns * r + c] for c in range(self.columns) for r in range(self.rows)}

        for row in range(self.rows):
            for column in range(self.columns):
                bombCount = self.count_bombs(row, column, bombsDict)    # counts surrounding bombs
                # create and grid tile
                self.tiles[(row, column)] = MinesweeperTile(self, value=bombCount, bomb=bombsDict[(row, column)])
                self.tiles[(row, column)].grid(row=row, column=column)
                self.tiles[(row, column)].bind('<Button-1>', lambda e, r=row, c=column: self.expose(r, c)) # set up left click
                self.tiles[(row, column)].bind('<Button-2>', lambda e, r=row, c=column: self.flag(r, c))   # set up right click
                self.tiles[(row, column)].bind('<Button-3>', lambda e, r=row, c=column: self.flag(r, c))   # set up right click

    def count_bombs(self, row, column, bombsDict):
        ''' self.count_bombs() counts the number of
        surrounding bombs for bombsDict[(row, column)] '''
        bombCount = 0
        for r in range(row - 1, row + 2):           # goes over surrounding rows
            for c in range(column - 1, column + 2): # surrounding columns
                if (r, c) in bombsDict and bombsDict[(r, c)]:
                    bombCount += 1                  # increases bombCount if a valid location and a bomb
        return bombCount

    def expose(self, row, column):
        ''' self.expose() exposes a tile '''
        if self.tiles[(row, column)].is_bomb():    # if a bomb is clicked player loses
            for tile in self.tiles.values():
                if tile.is_bomb():                 # marks all bombs
                    tile['bg'] = 'red'             # changes background to red
                    tile.flag()                    # flags bombs
            messagebox.showerror('Minesweeper', 'KABOOM! You lose.', parent=self)
            quit()                                 # ends game when player clicks OK

        if self.tiles[(row, column)].is_flagged(): # if tile is flagged increase num of bombs left
            self.bombsLeft += 1
            self.bombLabel['text'] = self.bombsLeft

        self.recursive_expose(row, column)         # exposes tile and sets off autoreveal if necessary

        if self.all_exposed():                     # if all tiles are exposed player wins
            messagebox.showinfo('Minesweeper', 'Congratulations -- you won!',parent=self)
            quit()                                 # ends game when player clicks OK

    def recursive_expose(self, row, column):
        ''' recursive_expose() exposes a tile and the
        surrounding tiles until there are no adjacent blank tiles '''
        self.tiles[(row, column)].expose()
        if not self.tiles[(row, column)].is_blank():    # base case
            return
        for r in range(row - 1, row + 2):               # iterate over surrounding tiles
            for c in range(column - 1, column + 2):
                # only expose hidden and valid tiles
                if (r, c) in self.tiles and not self.tiles[(r, c)].is_exposed():
                    self.recursive_expose(r, c)

    def flag(self, row, column):
        ''' self.flag() flags self.tiles[(row, column)] '''
        if self.tiles[(row, column)].is_flagged() == False: # only flags unflagged tiles
            self.tiles[(row, column)].flag()    # flags tile
            self.bombsLeft -= 1                 # displays the updated num of remaining bombs
            self.bombLabel['text'] = self.bombsLeft

    def all_exposed(self):
        ''' self.all_exposed() returns True if all
        normal tiles are exposed, or False if not '''
        for tile in self.tiles.values(): # iterates over tiles
            if not tile.is_bomb() and not tile.is_exposed():
                return False             # if any normal tile isn't exposed return False
        return True                      # if none are not exposed return True

def play_minesweeper(rows, columns, bombs):
    ''' play_minesweeper(rows, columns, bombs) plays a game
    Minesweeper with the specified rows, columns, and bombs '''
    root = Tk()
    root.title('Minesweeper')
    MinesweeperFrame(root, rows, columns, bombs)
    root.mainloop()

play_minesweeper(12, 10, 15)
