class Board:
    # const
    # Empty_block = 0
    # Empty_Wall = -1
    # walled = 1
    # Player1 = 11
    # Player2 = 22

    def __init__(self, size, player1, player2) -> None:

        self.size = size * 2 - 1

        self.board = [[-1] * self.size for _ in range(self.size)]
        for i in range(0, len(self.board), 2):
            for j in range(0, len(self.board[i]), 2):
                self.board[i][j] = 0
        self.board[0][size - 1] = 22
        self.board[self.size - 1][size - 1] = 11  # TODO mokhtasat player bayad az objecctesh gerefte beshe

        # self.player1 = player1
        # self.player2 = player2

    def displayboard(self):
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

    def valid(self, row, col) -> bool:
        """
        Returns true if the given row and col represent a valid location on
        the Quoridor board.
        """
        return row >= 0 and col >= 0 and row < self.size and col < self.size

    def canPlaceWall(self, row, column, direction: str) -> bool:
        if row % 2 == 0 or column % 2 == 0 or not self.valid(row, column) or self.board[row][column] != -1:
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

    def addWall(self, row, column, direction: str):
        if self.canPlaceWall(row, column, direction):
            if direction == 'vertical':
                self.board[row][column] = 1
                self.board[row + 1][column] = 1
                self.board[row - 1][column] = 1
            else:
                self.board[row][column] = 1
                self.board[row][column + 1] = 1
                self.board[row][column - 1] = 1
        # TODO Jump handle nashode. 'canGo' ham bayad edit beshe

    def go(self, player,
           direction):
        # TODO Board bayad update beshe: jaye qablish block khali va jaye jadidesh ham esmesh biad
        if self.canGo(player, direction):
            if direction == 'up':

                player.row -= 2

            elif direction == 'down':

                player.row += 2

            elif direction == 'right':

                player.column += 2

            elif direction == 'left':

                player.column -= 2

        pass

    def canGo(self, player, direction) -> bool:
        if direction == 'up':
            return self.valid(player.row - 2,
                              player.column) and self.board[player.row - 1][player.column] == -1  ## ham valid bashe ham wall nabashe

        elif direction == 'down':
            return self.valid(player.row + 2, player.column) and self.board[player.row + 1][player.column] == -1
        elif direction == 'right':
            return self.valid(player.row + 2, player.column) and self.board[player.row ][player.column+1] == -1

        elif direction == 'left':
            return self.valid(player.row - 2, player.column) and self.board[player.row ][player.column-1] == -1

        else:
            raise Exception('invalid input')



