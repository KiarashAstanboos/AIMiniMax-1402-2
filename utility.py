from Board import Board
from Player import Player
import numpy as np


def utility(board: Board, player: Player, opponent: Player):
    value = 0
    if player.terminal_test():
        value += 1000000

    # value += 7 - int(np.abs(player.row - player.goalRow))
    # value += int(np.abs(opponent.row - opponent.goalRow)) - 7
    #
    # if opponent.name == 'player 2':
    #     cango, jump = board.canGo(opponent, 'down')
    #     if not cango:
    #         value += 100000
    # else:
    #     cango, jump = board.canGo(opponent, 'up')
    #     if not cango:
    #         value += 100000
    value += board.shortestPath(opponent) - board.shortestPath(player) *1.1

    return value
