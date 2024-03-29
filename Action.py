import Player



class Action:
    def __init__(self, row, column, direction):
        self.row = row
        self.column = column
        self.direction = direction



def doAction(action: Action, player: Player, board ):
    if action.direction == "up":
        player.doGo(board, 'up')
    elif action.direction == "down":
        player.doGo(board, 'down')
    elif action.direction == "right":
        player.doGo(board, 'right')
    elif action.direction == "left":
        player.doGo(board, 'left')
    elif action.direction == "horizontal":
        player.doBuild(board, action.row, action.column, 'horizontal')
    elif action.direction == "vertical":
        player.doBuild(board, action.row, action.column, 'vertical')





