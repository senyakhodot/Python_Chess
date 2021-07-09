def convertCoord(x, y):
    return chr(x + 97) + chr(y + 49)


class EmptyCellException(Exception):
    def __init__(self, x, y):
        self.msg = f"There's no chess piece in cell {convertCoord(x, y)}!"


class IncorrectInputException(Exception):
    def __init__(self):
        self.msg = "Incorrect input!"


class TurnNotOver(Exception):
    def __init__(self):
        self.msg = "Enemy's turn..."

    def __str__(self):
        return self.msg


class UserTurnIsOver(Exception):
    pass
