import copy
from Player import Player
from Board import Board
from Action import doAction
from utility import utility


class AI:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def choose_action(self, board, player, opponent, max_depth):
        best_action = self.minimax(
            copy.deepcopy(board),
            copy.copy(player),
            copy.copy(opponent),
            max_depth,
        )

        return best_action

    def deepCopy(self, player, opponent, board) -> tuple[Player, Player, Board]:
        player_copy = copy.deepcopy(player)
        opponent_copy = copy.deepcopy(opponent)
        next_board = copy.deepcopy(board)
        next_board.player1 = player_copy
        next_board.player2 = opponent_copy

        return player_copy, opponent_copy, next_board


    def succesors(self, board: Board, player: Player, opponent: Player, reverse=False):
        if (reverse):
            actions = opponent.getValidActions(board)
        else:
            actions = player.getValidActions(board)

        result = []
        for action in actions:
            player_copy, opponent_copy, next_board = self.deepCopy(player, opponent, board)

            if (reverse):
                doAction(action, opponent_copy, next_board)
            else:
                doAction(action, player_copy, next_board)

            result.append({'board': next_board, 'player': player_copy, 'opponent': opponent_copy, 'action': action})

        return result

    def minimax(self, board: Board, player: Player, opponent: Player, depth):
        """
        Return the best action
        """

        pass

    def max(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):
        """
        choose the best state from succesors and return it and its value
        """
        pass

    def min(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):
        """
        choose the worst state from succesors and return it and its value
        """
        pass
