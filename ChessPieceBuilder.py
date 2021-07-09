from ChessPieces import *


class ChessPieceBuilder:
    def __init__(self, value=0, color=0):
        self.__value = value
        self.__color = color

    def set_value(self, value):
        self.__value = value

    def set_color(self, color):
        self.__color = color

    def build(self):
        if self.__value == 0:
            return Empty()
        if self.__value == 1:
            return Pawn(self.__color)
        if self.__value == 2:
            return Knight(self.__color)
        if self.__value == 3:
            return Bishop(self.__color)
        if self.__value == 4:
            return Rook(self.__color)
        if self.__value == 5:
            return Queen(self.__color)
        if self.__value == 6:
            return King(self.__color)
