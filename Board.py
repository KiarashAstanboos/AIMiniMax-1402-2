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
        self.board[player2.row][player2.column] = 22
        self.board[player1.row][player1.column] = 11

        self.player1 = player1
        self.player2 = player2

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

        self.board[player.row][player.column] = 0
        cango, jump = self.canGo(player, direction)
        if cango:
            if direction == 'up':
                if jump:
                    player.row -= 4
                else:
                    player.row -= 2

            elif direction == 'down':

                if jump:
                    player.row += 4
                else:
                    player.row += 2

            elif direction == 'right':

                if jump:
                    player.column += 4
                else:
                    player.column += 2

            elif direction == 'left':

                if jump:
                    player.column -= 4
                else:
                    player.column -= 2
        self.board[player.row][player.column] = int(player.name[-1] * 2)

    def canGo(self, player, direction) -> (bool, bool):
        if direction == 'up':
            if self.valid(player.row - 2, player.column) and self.board[player.row - 2][
                player.column] == 0:  # age block khali bood
                return (self.board[player.row - 1][player.column] == -1, False)  ## ham valid bashe ham wall nabashe
            elif self.valid(player.row - 4, player.column):  # age player dige bood
                return (self.board[player.row - 3][player.column] == -1, True)
            else:
                return (False, False)
        elif direction == 'down':
            if self.valid(player.row + 2, player.column) and self.board[player.row + 2][
                player.column] == 0:
                return (self.board[player.row + 1][player.column] == -1, False)
            elif self.valid(player.row + 4, player.column):
                return (self.board[player.row + 3][player.column] == -1, True)
            else: return(False,False)

        elif direction == 'right':
            if self.valid(player.row, player.column + 2) and self.board[player.row][
                player.column + 2] == 0:
                return (self.board[player.row][player.column + 1] == -1, False)
            elif self.valid(player.row, player.column + 3):
                return (self.board[player.row][player.column + 3] == -1, True)
            else:
                return (False, False)
        elif direction == 'left':
            if self.valid(player.row, player.column - 2) and self.board[player.row][
                player.column - 2] == 0:
                return (self.board[player.row][player.column - 1] == -1, False)
            elif self.valid(player.row, player.column - 4):
                return (self.board[player.row][player.column - 3] == -1, True)
            else:
                return (False, False)
        else:
            raise  Exception('inavlid input')
