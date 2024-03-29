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

    def succusors(self, board: Board, player: Player, opponent: Player, reverse=False):
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
        alpha = -100000000
        beta = 100000000
        value, move = self.max(board, player, opponent, depth, alpha, beta)

        return move['action']

    def max(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):
        if depth == 0: return utility(board, player, opponent), None

        possible_states = self.succusors(board, player, opponent)
        beststate = None
        bestvalue = self.MIN_VALUE
        for state in possible_states:
            temp, bb = self.min(state['board'], state['player'], state['opponent'], depth - 1, alpha, beta)

            if bestvalue < temp:
                bestvalue = temp
                beststate = state

            if bestvalue >= beta: return bestvalue, beststate
            alpha = max(alpha, bestvalue)

        return bestvalue, beststate

    def min(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):

        if depth == 0: return utility(board, player, opponent), None

        possible_states = self.succusors(board, player, opponent, True)
        beststate = None
        bestvalue = self.MAX_VALUE
        for state in possible_states:
            temp, bb = self.max(state['board'], state['player'], state['opponent'], depth - 1, alpha, beta)

            if bestvalue > temp:
                bestvalue = temp
                beststate = state

            if bestvalue <= alpha : return bestvalue , beststate
            beta = min(beta , bestvalue)

        return bestvalue, beststate
