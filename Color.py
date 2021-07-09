class Color(object):  # Специальный класс Color, с помощью которого была
    # Empty = 0                                                 # реализовано отношение композиции. Объект класса Color
    # White = 1                                                 # создается внутри класса ChessPiece и отвечает за цвет
    # Black = 2                                                 # фигуры

    def __init__(self, color):
        self.value = color