from Action import Action
from Board import Board
import typing


class Player:
    def __init__(self, walls, name, startingRow, startingColumn):
        self.walls = walls
        self.name = name
        self.row = startingRow
        self.column = startingColumn

    # TODO yek rah baraye residan be maqsad handle nashode!
    def getValidActions(self, board: Board) -> typing.List[
        Action]:  # TODO motmaen nistam doroste meqdar dehim ya na. bayad be can go player pas dade beshe
        available_actions = []
        if board.canGo(self, 'up'): available_actions.append(Action(None, None, 'up'))
        if board.canGo(self, 'down'): available_actions.append(Action(None, None, 'down'))
        if board.canGo(self, 'right'): available_actions.append(Action(None, None, 'right'))
        if board.canGo(self, 'left'): available_actions.append(Action(None, None, 'left'))

        if self.walls > 0:
            for i in range(1, len(board), 2):
                for j in range(1, len(board[i]), 2):
                    if board.canPlaceWall(i, j, 'vertical'): available_actions.append(Action(i, j, 'vertical'))
                    if board.canPlaceWall(i, j, 'horizontal'): available_actions.append(Action(i, j, 'horizontal'))

    def doGo(self, board:Board,direction): # TODO motmaen nistam doroste meqdar dehim ya na. bayad be  go player pas dade beshe

        board.go(self,direction)
    def doBuild(self,board,row,column,direction):
        board.addWall(row,column,direction)
        self.walls-=1