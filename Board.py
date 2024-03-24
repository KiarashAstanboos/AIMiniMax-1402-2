class Board:
    # const
    # Empty_block = 0
    # Empty_Wall = -1
    # walled = 1
    # Player1 = 11
    # Player2 = 22

    def __init__(self, size) -> None:

        self.size = size*2-1

        self.board = [[-1] * self.size for _ in range(self.size)]
        for i in range(0, len(self.board), 2):
            for j in range(0, len(self.board[i]), 2):
                self.board[i][j] = 0
        self.board[0][size-1]=22
        self.board[self.size-1][size-1] =11


        # self.player1 = player1
        # self.player2 = player2

    def display_board(self):
        for r in self.board:

            for c in r:
                if c ==0:print("█", end="")
                elif c== -1 :print(' ', end="")
                elif c==1 :
                    if r%2==0:print('|', end="")
                    else:print('-', end="")
                else: print(c, end="")
            print()





Board=Board(9)
Board.display_board()
