from ChessPiece import ChessPiece


class Empty(ChessPiece):

    def __init__(self, ):
        ChessPiece.__init__(self, 0)
        self.value = 0
        self.IMG = ' '

    def movesAvailable(self, x1, y1, x2, y2):
        return False

    def makeMove(self, x, y):
        pass


class Pawn(ChessPiece):  # Класс Пешки

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 1
        self.IMG = ('♙', '♟')

    def movesAvailable(self, x1, y1, x2, y2):
        if ((self.color.value == 2 and y1 - y2 == 1) or (self.color.value == 1 and y2 - y1 == 1)) and x1 == x2:
            return True
        else:
            return False

    def makeMove(self, x, y):
        return x, y - 1


class Knight(ChessPiece):  # Класс Коня

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 2
        self.IMG = ('♘', '♞')

    def movesAvailable(self, x1, y1, x2, y2):
        if (abs(y2 - y1) == 2 and abs(x2 - x1) == 1) or (abs(y2 - y1) == 1 and abs(x2 - x1) == 2):
            return True
        else:
            return False

    def makeMove(self, x, y):
        pass


class Bishop(ChessPiece):  # Класс Слона

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 3
        self.IMG = ('♗', '♝')

    def movesAvailable(self, x1, y1, x2, y2):
        if abs(x2 - x1) == abs(y2 - y1):
            return True
        else:
            return False

    def makeMove(self, x, y):
        pass

class Rook(ChessPiece):  # Класс Ладьи

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 4
        self.IMG = ('♖', '♜')

    def movesAvailable(self, x1, y1, x2, y2):
        if (y2 == y1 and x1 != x2) or (y2 != y1 and x1 == x2):
            return True
        else:
            return False

    def makeMove(self, x, y):
        pass

class Queen(ChessPiece):  # Класс Ферзя

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 5
        self.IMG = ('♕', '♛')

    def movesAvailable(self, x1, y1, x2, y2):
        if ((y2 == y1 and x1 != x2) or (y2 != y1 and x1 == x2)) or (abs(x2 - x1) == abs(y2 - y1)):
            return True
        else:
            return False

    def makeMove(self, x, y):
        pass

class King(ChessPiece):  # Класс Короля

    def __init__(self, color):
        ChessPiece.__init__(self, color)
        self.value = 6
        self.IMG = ('♔', '♚')

    def movesAvailable(self, x1, y1, x2, y2):
        if abs(y2 - y1) == 1 or abs(x2 - x1) == 1:
            return True
        else:
            return False

    def makeMove(self, x, y):
        pass