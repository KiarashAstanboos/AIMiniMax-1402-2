from Player import Player
from Board import Board
from Action import Action, doAction
from AI import AI

size = 7
depth = 4
# player2 = Player(8, 'player 2', 0, size - 1)
# player1 = Player(8, 'player 1', size * 2 - 2, size - 1)
player2 = Player(8, 'player 2', 4, size - 1)
player1 = Player(8, 'player 1',4, 4)

board = Board(size, player1, player2)
board.addWall(5,7,'vertical')
board.addWall(3,7,'horizontal')
board.displayboard()

print('up'+str(board.canGo(player1,'up')))
print('down'+str(board.canGo(player1,'down')))
print('right'+str(board.canGo(player1,'right')))
print('left'+str(board.canGo(player1,'left')))

print('rightUp'+str(board.canGo(player1,'rightUp')))
print('upRight'+str(board.canGo(player1,'upRight')))
print('leftUp'+str(board.canGo(player1,'leftUp')))
print('upLeft'+str(board.canGo(player1,'upLeft')))
print('downRight'+str(board.canGo(player1,'downRight')))
print('rightDown'+str(board.canGo(player1,'rightDown')))
print('leftDown'+str(board.canGo(player1,'leftDown')))
print('downLeft'+str(board.canGo(player1,'downLeft')))
print('p2')
print('up'+str(board.canGo(player2,'up')))
print('down'+str(board.canGo(player2,'down')))
print('right'+str(board.canGo(player2,'right')))
print('left'+str(board.canGo(player2,'left')))

print('rightUp'+str(board.canGo(player2,'rightUp')))
print('upRight'+str(board.canGo(player2,'upRight')))
print('leftUp'+str(board.canGo(player2,'leftUp')))
print('upLeft'+str(board.canGo(player2,'upLeft')))
print('downRight'+str(board.canGo(player2,'downRight')))
print('rightDown'+str(board.canGo(player2,'rightDown')))
print('leftDown'+str(board.canGo(player2,'leftDown')))
print('downLeft'+str(board.canGo(player2,'downLeft')))



# Round=0
#
# print()
# print()
# print()
#
# player1_ai = AI()
# player2_ai = AI()
#
# isPalyer1 = True
#
# while True:
#     if isPalyer1:
#         ai_action = player1_ai.choose_action(board, player1, player2, depth)
#
#         doAction(ai_action, player1, board)
#
#         if ai_action.direction == "vertical":
#             print(f"AI {player1.name} chose to place a vertical wall at [{ai_action.row}][{ai_action.column}]:")
#             print()
#         elif ai_action.direction == "horizontal":
#             print(f"AI {player1.name} chose to place a horizontal wall at [{ai_action.row}][{ai_action.column}]:")
#             print()
#         else:
#             print(
#                 f"AI {player1.name} chose to go {ai_action.direction}:"
#             )
#             print()
#
#     else:
#         ai_action = player2_ai.choose_action(board, player2, player1, depth)
#
#         doAction(ai_action, player2, board)
#
#         if ai_action.direction == "vertical":
#             print(f"AI {player2.name} chose to place a vertical wall at [{ai_action.row}][{ai_action.column}]:")
#             print()
#         elif ai_action.direction == "horizontal":
#             print(f"AI {player2.name} chose to place a horizontal wall at [{ai_action.row}][{ai_action.column}]:")
#             print()
#         else:
#             print(
#                 f"AI {player2.name} chose to go {ai_action.direction}:"
#             )
#             print()
#
#     board.displayboard()
#
#     if player1.terminal_test():
#         print(f"{player1.name} wins!")
#         exit()
#     if player2.terminal_test():
#         print(f"{player2.name} wins!")
#         exit()
#
#     isPalyer1 = not isPalyer1
#     Round+=1
#     print("Round: " + str(Round))

