from abc import ABC, abstractmethod
from Color import Color



class ChessPiece(ABC):  # Базовый класс для всех фигур.
    __IMG = None  # Поле, отвечающее за изображение фигуры, которое будет

    # назначено в конструкторе класса конкретной фигуры.

    def __init__(self, color):
        self.__color = Color(color)  # Создание объекта класса Color
        self.__value = 0

    def __str__(self):
        if self.__color.value == 0:
            return self.__IMG
        else:
            return self.__IMG[self.color.value - 1]

    def checkMove(self, x1, y1, x2, y2):
        if self.movesAvailable(x1, y1, x2, y2):
            print("The move is available!")
        else:
            print("The move is not available!")

    @abstractmethod
    def movesAvailable(self, x1, y1, x2, y2):
        pass

    @abstractmethod
    def makeMove(self, x, y):
        pass

    @property
    def IMG(self):
        return self.__IMG

    @property
    def value(self):
        return self.__value

    @property
    def color(self):
        return self.__color

    @IMG.setter
    def IMG(self, value):
        self.__IMG = value

    @value.setter
    def value(self, value):
        self.__value = value


