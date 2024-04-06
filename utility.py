from Board import Board
from Player import Player
import numpy as np


def utility(board: Board, player: Player, opponent: Player):
    value = 0
    if player.terminal_test():
        value += 1000000

    value += board.shortestPath(opponent) - board.shortestPath(player) * 1.1

    return value
