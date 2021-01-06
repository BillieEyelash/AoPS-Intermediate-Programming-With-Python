from tkinter import Label, Frame, Button, Canvas, Tk, messagebox

class CheckersSquare(Canvas):
    ''' CheckersSquare is a square in a game of checkers '''

    def __init__(self, master, bgcolor, player, coords):
        Canvas.__init__(self, master, width=50, height=50, bg=bgcolor)
        self.grid(row=coords[0], column=coords[1])
        self.coords = coords
        self.highlighted = False
        self.player = player
        self.place_piece(player)                  # places a tile if necessary
        self.bind('<Button>', master.take_turn)   # when clicked it will call the take_turn() method from master


    def place_piece(self, player, isKing=False):
        ''' self.place_piece(color)
        places a piece of a specified color'''
        self.delete_piece()    # removes existing pieces
        if player == None:     # doesn't add anything if there isn't a player
            return
        colors = ['red', 'white']
        self.create_oval(10, 10, 44, 44, fill=colors[player]) # place new piece
        self.player = player   # updates player attribute
        self.set_king(isKing)

    def delete_piece(self):
        ''' self.delete_piece() removes any
        pieces on the CheckersSquare '''
        ovalList = self.find_all() # finds all pieces
        for oval in ovalList:      # deletes all pieces
            self.delete(oval)
        self.player = None         # updates player attribute

    def highlight(self):
        ''' self.highlight() highlights self black '''
        self['highlightbackground'] = 'black'
        self.highlighted = True

    def unhighlight(self):
        ''' self.unhighlight() removes any highlights '''
        self['highlightbackground'] = 'white'
        self.highlighted = False

    def is_highlighted(self):
        ''' self.is_highlighted() ->
        returns if the square is highlighted '''
        return self.highlighted

    def get_player(self):
        ''' self.get_player() -> the player on the square '''
        return self.player

    def get_coords(self):
        ''' self.get_coords() -> the location of the square '''
        return self.coords

    def set_king(self, isKing):
        text = self.create_text(27, 34, font=('Times', 30), text=['', '*'][isKing])

class CheckersBoard:
    ''' CheckersBoard represents a game of checkers '''

    def __init__(self):
        self.board = {}    # keeps track of players' locations
        self.kings = {}    # keeps track of kings' locations
        for row in range(8):
            for column in range(8):
                # sets up starting positions
                if row < 3 and (row + column) % 2 == 0:
                    player = 0
                elif row > 4 and (row + column) % 2 == 0:
                    player = 1
                else:
                    player = None
                self.board[(row, column)] = player
                self.kings[(row, column)] = False # no kings at the beginning
        self.currentPlayer = 0 # starting player

    def get_square(self, coords):
        ''' self.get_square(row, column) ->
        self.board[(row, column)] if valid '''
        if coords in self.board.keys():
            return self.board[coords]
        return None

    def get_board(self):
        ''' self.get_board() -> all the
        coords, player in self.board '''
        return self.board.items()

    def try_move(self, coords1, coords2):
        ''' self.try_move(coords1, coords2) -> if move from
        coords1 to coords2 is valid and updates board '''
        if self.is_valid(coords1, coords2):                            # checks if is valid move
            if self.can_jump() and not self.is_jump(coords1, coords2): # if can jump but not jumping move isn't valid
                return False
            self.move_piece(coords1, coords2)                          # otherwise update the board
            if self.is_jump(coords1, coords2):                         # if the move is a jump delete middle piece
                self.board[(coords1[0] + coords2[0]) // 2, (coords1[1] + coords2[1]) // 2] = None
            return True
        return False

    def is_valid(self, coords1, coords2):
        ''' self.is_valid checks if moving a tile
        from (coords1) to (coords2) is valid '''
        if [coords1[0] < coords2[0], coords1[0] > coords2[0]][self.get_current_player()] or self.is_king(coords1): # moving in the right direction
            if self.get_square(coords1) == self.get_current_player() and self.get_square(coords2) == None:  # current square is filled and other is empty
                if abs(coords1[0] - coords2[0]) == 1 and abs(coords1[1] - coords2[1]) == 1 or self.is_jump(coords1, coords2): # only moving by one unit or is jump
                    return True
        return False

    def is_jump(self, coords1, coords2):
        ''' self.is_jump() -> move is a jump '''
        if abs(coords1[0] - coords2[0]) == 2 and abs(coords1[1] - coords2[1]) == 2:     # if two units diagonally
            midCoords = (coords1[0] + coords2[0]) // 2, (coords1[1] + coords2[1]) // 2  # the coords of the square inbetween
            return self.get_square(midCoords) == ((self.get_current_player() + 1) % 2)  # if is the opposite color
        return False

    def get_current_player(self):
        ''' self.get_current_player() -> current player '''
        return self.currentPlayer

    def move_piece(self, coords1, coords2):
        ''' self.move_piece(coords1, coords2) ->
        moves a piece from coords1 to coords2 '''
        self.board[coords1], self.board[coords2] = None, self.get_square(coords1) # swap values
        # if king at coords1 or coords2 becomes a king
        if self.is_king(coords1) or self.get_current_player() == 0 and coords2[0] == 7 or self.get_current_player() == 1 and coords2[0] == 0:
            self.kings[coords1] = False
            self.kings[coords2] = True

    def game_over(self):
        ''' self.game_over() -> if game is
        over and only one color is left '''
        # if next player has no remaining pieces
        if list(self.board.values()).count((self.get_current_player() + 1) % 2) == 0:
            return True
        # if the player has no remaining moves
        elif len(self.get_valid_moves()) == 0:
            self.currentPlayer = (self.get_current_player() + 1) % 2
            return True
        return False

    def is_king(self, coords):
        ''' self.is_king() -> if
        a square contains a king '''
        return self.kings[coords]

    def get_valid_moves(self):
        ''' self.get_valid_moves() ->
        all possible moves for currentPlayer '''
        validMoves = [(coords1, coords2) for coords2 in self.board.keys() for coords1 in self.board.keys() if self.is_valid(coords1, coords2)]
        return validMoves

    def get_jumps(self):
        ''' self.get_jumps() ->
        all possible jumpd for currentPlayer '''
        validMoves = self.get_valid_moves()
        # checks which of the valid moves are jumps
        jumps = [(coords1, coords2) for coords1, coords2 in validMoves if self.is_jump(coords1, coords2)]
        return jumps

    def can_jump(self):
        ''' self.cen_jump() -> if currentPlayer
        has any possible jumps '''
        return len(self.get_jumps()) > 0

    def can_jump_from(self, coords):
        ''' self.can_jump_from() -> if player
        can jump from a certain square '''
        jumps = self.get_jumps()                        # all possible jumps
        jumpsStart = [coords1 for coords1, coords2 in jumps]  # checks if a jump can be made from this point
        return coords in jumpsStart


class CheckersFrame(Frame):
    ''' CheckersFrame is a frame in a game of checkers '''

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.board = CheckersBoard()
        self.squares = {}
        # create UI and store all the squares
        colors = ['dark green', 'blanched almond']
        for coords, player in self.board.get_board():
            i = (coords[0] + coords[1]) % 2
            self.squares[coords] = CheckersSquare(self, colors[i], player, coords) # calls take_turn when clicked

        # keeps track of whose turn it is
        self.turnLabel = Label(self, text='Turn: ', font=('Arial', 12))
        self.turnLabel.grid(row=9, column=1)
        self.turnSquare = CheckersSquare(self, 'light gray', 0, (9, 2))
        # displays any necessary messages
        self.messageLabel = Label(self, text='', font=('Arial', 12))
        self.messageLabel.grid(row=9, column=3, columnspan=5)

    def take_turn(self, event):
        ''' self.take_turn() takes a turn for a player '''
        clickedSquare = self.squares[event.widget.get_coords()] # get the clicked square
        self.messageLabel['text'] = ''                          # reset message label
        for coords, square in self.squares.items():             # iterate over squares to check f any are highlighted
            if not square.is_highlighted():
                continue
            square.unhighlight()
            isJump =  self.board.is_jump(square.get_coords(), clickedSquare.get_coords()) # recalls if the move is a jump
            if self.board.try_move(square.get_coords(), clickedSquare.get_coords()):      # tries the move, and tests if it is valid
                self.update_frame()
            # checks if game over and displays winner if so
                if self.board.game_over():
                    messagebox.showinfo('Checkers', ['Red', 'White'][self.board.get_current_player()] + ' wins!', parent=self)
                    quit()
                # sees if move is a jump and should be continued
                if isJump and self.board.can_jump_from(clickedSquare.get_coords()):
                    self.messageLabel['text'] = 'You must continue your jump.'  # sets message and does not move to next player
                    return

                self.goto_next_player()
                return
            # mandatory jump so will not go to next player's turn
            elif self.board.can_jump():
                self.messageLabel['text'] = 'You must jump.'
                return

        # highlights square if it matches the current player
        if clickedSquare.get_player() == self.board.get_current_player():
            clickedSquare.highlight()
        else:   # displays invalid input message
            self.messageLabel['text'] = 'This move is not valid.'

    def update_frame(self):
        ''' self.update_frame() updates the frame
        based off of the board positions '''
        for coords, player in self.board.get_board():
            self.squares[coords].place_piece(player, self.board.is_king(coords)) # updates piece positions and king status

    def goto_next_player(self):
        ''' self.goto_next_player() goes to the next
        player and updates the turn indicator '''
        self.board.currentPlayer = (self.board.get_current_player() + 1) % 2
        self.turnSquare.place_piece(self.board.get_current_player())


def play_checkers():
    ''' play_checkers() sets up a game of checkers '''
    root = Tk()
    root.title('Checkers')
    checkers = CheckersFrame(root)
    checkers.mainloop()

play_checkers()
