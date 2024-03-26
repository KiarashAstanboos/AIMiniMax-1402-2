from Player import Player
from Board import Board

size = 9
player2 = Player(10, 'player 2', 0, size - 1)
player1 = Player(10, 'player 1', size * 2 - 2, size - 1)

board = Board(size, player1, player2)
# Board.display_board()
board.addWall(1, 1, 'vertical')
board.addWall(3, 3, 'horizontal')
board.displayboard()
valid=player1.getValidActions(board)
print (valid)

