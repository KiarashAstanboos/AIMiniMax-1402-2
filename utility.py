from Board import Board
from Player import Player
import numpy as np


def utility(board: Board, player: Player, opponent: Player):
    if player.terminal_test():
        return 1000000

    value = 9 - int(np.abs(player.row - player.goalRow))
    value += int(np.abs(opponent.row - opponent.goalRow)) - 9

    if opponent.name == 'player 2':
        if not board.canGo(opponent, 'down'):
            value += 100000
    else:
        if not board.canGo(opponent, 'up'):
            value += 100000

    return value
