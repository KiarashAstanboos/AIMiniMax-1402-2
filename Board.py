class Board:
    # const
    # Empty_block = 0
    # Empty_Wall = -1
    # walled = 1
    # Player1 = 11
    # Player2 = 22

    def __init__(self, size) -> None:

        self.size = size * 2 - 1

        self.board = [[-1] * self.size for _ in range(self.size)]
        for i in range(0, len(self.board), 2):
            for j in range(0, len(self.board[i]), 2):
                self.board[i][j] = 0
        self.board[0][size - 1] = 22
        self.board[self.size - 1][size - 1] = 11  # TODO mokhtasat player bayad az objecctesh gerefte beshe

        # self.player1 = player1
        # self.player2 = player2

    def display_board(self):
        for indexR, r in enumerate(self.board):

            for indexC, c in enumerate(r):
                if c == 0:
                    print("█", end=" ")
                elif c == -1:
                    print(' ', end=" ")
                elif c == 1:
                    if indexR % 2 == 0:
                        print('|', end=" ")
                    else:
                        if indexC % 2 != 0:
                            print('•', end=" ")
                        else:
                            print('\u2014', end=" ")
                else:
                    print(str(c)[0], end=" ")
            print()

    def valid(self, row, col):
        """
        Returns true if the given row and col represent a valid location on
        the konane board.
        """
        return row >= 0 and col >= 0 and row < self.size and col < self.size

    def can_Place_Wall(self, row, column, direction: str):
        if row % 2 == 0 or column % 2 == 0 or not self.valid(row, column) or self.board[row][column] != -1:
            raise Exception('invalid cordinates')
            return False
        else:
            if direction == 'vertical':
                return (self.valid(row + 1, column) and self.valid(row - 1, column) \
                        and self.board[row + 1][column] == -1 and self.board[row - 1][column] == -1)


            elif direction == 'horizontal':
                return (self.valid(row, column + 1) and self.valid(row, column - 1) \
                        and self.board[row][column + 1] == -1 and self.board[row][column - 1] == -1)


            else:
                raise Exception('invalid direction!')

    def add_Wall(self, row, column, direction: str):
        if self.can_Place_Wall(row, column, direction):
            if direction == 'vertical':
                self.board[row][column] = 1
                self.board[row + 1][column] = 1
                self.board[row - 1][column] = 1
            else:
                self.board[row][column] = 1
                self.board[row][column + 1] = 1
                self.board[row][column - 1] = 1

    def go(self, player,
           direction):  # TODO class player bayad takmil she vase in. bade piade sazi 'PLAYER' debug beshe.
                        #TODO Board bayad update beshe: jaye qablish block khali va jaye jadidesh ham esmesh biad
        if direction == 'up':
            if self.valid(player.row - 1, player.column):
                player.row -= 1
            else:
                raise Exception('cant go this direction!')
        elif direction == 'down':
            if self.valid(player.row - 1, player.column):
                player.row += 1
            else:
                raise Exception('cant go this direction!')
        elif direction == 'right':
            if self.valid(player.row - 1, player.column):
                player.column += 1
            else:
                raise Exception('cant go this direction!')
        elif direction == 'left':
            if self.valid(player.row - 1, player.column):
                player.column -= 1
            else:
                raise Exception('cant go this direction!')
        else: raise Exception('invalid input')


pass

Board = Board(9)
# Board.display_board()
Board.add_Wall(1, 1, 'vertical')
Board.add_Wall(3, 3, 'horizontal')
Board.display_board()
