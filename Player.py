from Action import Action
from Board import Board
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

    # TODO yek rah baraye residan be maqsad handle nashode!
    def getValidActions(self, board: Board) -> typing.List[
        Action]:
        available_actions = []
        if board.canGo(self, 'up'): available_actions.append(Action(None, None, 'up'))
        if board.canGo(self, 'down'): available_actions.append(Action(None, None, 'down'))
        if board.canGo(self, 'right'): available_actions.append(Action(None, None, 'right'))
        if board.canGo(self, 'left'): available_actions.append(Action(None, None, 'left'))

        if self.walls > 0:
            for i in range(1, board.size, 2):
                for j in range(1, len(board.board[i]), 2):
                    if board.canPlaceWall(i, j, 'vertical'): available_actions.append(Action(i, j, 'vertical'))
                    if board.canPlaceWall(i, j, 'horizontal'): available_actions.append(Action(i, j, 'horizontal'))
        return available_actions

    def doGo(self, board: Board, direction):

        board.go(self, direction)

    def doBuild(self, board: Board, row, column, direction):
        board.addWall(row, column, direction)
        self.walls -= 1

    def checkForWall(self, row, column):  # for pathToOtherSide
        if row == 2:
            return (1, 0)
        elif row == -2:
            return (-1, 0)
        elif column == -2:
            return (0, -1)
        elif column == 2:
            return (0, 1)

    def pathToOtherSide(self, board: Board) -> bool:
        stack = [(self.row, self.column)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if x == self.goalRow:
                return True  # Player reached the goal
            if (x, y) in visited:
                continue  # Skip already visited nodes
            visited.add((x, y))

            # Check all adjacent cells
            for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                new_xW,new_yW=self.checkForWall(dx,dy)
                new_xW, new_yW=x + new_xW, y + new_yW
                new_x, new_y = x + dx, y + dy
                if board.valid(new_x, new_y) and board.board[new_xW][new_yW]==-1:
                    stack.append((new_x, new_y))  # Add legal moves to the stack

        return False  # No path found

    def terminal_test(self):
        if self.goalRow == self.row:
            return True
        else:
            return False