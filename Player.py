from Action import Action
from Board import Board
import copy
import typing


class Player:
    def __init__(self, walls, name, startingRow, startingColumn):
        self.walls = walls
        self.name = name
        self.row = startingRow
        self.column = startingColumn
        if self.name == 'player 1':
            self.goalRow = 0
        else:
            self.goalRow = startingColumn * 2


    def getValidActions(self, board: Board) -> typing.List[
        Action]:
        available_actions = []
        cango1, jump = board.canGo(self, 'up')
        cango2, jump = board.canGo(self, 'down')
        cango3, jump = board.canGo(self, 'right')
        cango4, jump = board.canGo(self, 'left')

        if cango1: available_actions.append(Action(None, None, 'up'))
        if cango2: available_actions.append(Action(None, None, 'down'))
        if cango3: available_actions.append(Action(None, None, 'right'))
        if cango4: available_actions.append(Action(None, None, 'left'))

        if self.walls > 0:
            for i in range(1, board.size, 2):
                for j in range(1, len(board.board[i]), 2):
                    if board.canPlaceWall(i, j, 'vertical'):
                        board_copy = copy.deepcopy(board)
                        board_copy.addWall(i, j, 'vertical')
                        if not board_copy.checkForTrap():  available_actions.append(Action(i, j, 'vertical'))
                    if board.canPlaceWall(i, j, 'horizontal'):
                        board_copy2 = copy.deepcopy(board)
                        board_copy2.addWall(i, j, 'horizontal')
                        if not board_copy2.checkForTrap(): available_actions.append(Action(i, j, 'horizontal'))
        return available_actions

    def doGo(self, board: Board, direction):

        board.go(self, direction)

    def doBuild(self, board: Board, row, column, direction):
        board.addWall(row, column, direction)
        self.walls -= 1


    def terminal_test(self):
        if self.goalRow == self.row:
            return True
        else:
            return False
