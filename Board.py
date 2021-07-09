from ChessPieces import *
from MixinClasses.PrintNameMixin import PrintNameMixin
from exceptions import *
import random
import asyncio
import sys
import keyboard


class Board(PrintNameMixin):

    def __init__(self):  # Конструктор класса Board
        self.board = [[Empty() for j in range(8)] for i in range(8)]
        self.board[0][1] = Pawn(1)
        self.board[1][1] = Pawn(1)
        self.board[2][1] = Pawn(1)
        self.board[3][1] = Pawn(1)
        self.board[4][1] = Pawn(1)
        self.board[5][1] = Pawn(1)
        self.board[6][1] = Pawn(1)
        self.board[7][1] = Pawn(1)
        self.board[0][6] = Pawn(2)
        self.board[1][6] = Pawn(2)
        self.board[2][6] = Pawn(2)
        self.board[3][6] = Pawn(2)
        self.board[4][6] = Pawn(2)
        self.board[5][6] = Pawn(2)
        self.board[6][6] = Pawn(2)
        self.board[7][6] = Pawn(2)
        self.board[0][0] = Rook(1)
        self.board[1][0] = Knight(1)
        self.board[2][0] = Bishop(1)
        self.board[3][0] = Queen(1)
        self.board[4][0] = King(1)
        self.board[5][0] = Bishop(1)
        self.board[6][0] = Knight(1)
        self.board[7][0] = Rook(1)
        self.board[0][7] = Rook(2)
        self.board[1][7] = Knight(2)
        self.board[2][7] = Bishop(2)
        self.board[3][7] = Queen(2)
        self.board[4][7] = King(2)
        self.board[5][7] = Bishop(2)
        self.board[6][7] = Knight(2)
        self.board[7][7] = Rook(2)
        self.printBoard()

    # @reg_decorator
    def printBoard(self):  # Метод вывода поля в консоль
        print("     1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0, 8):
            print("-" * 37)
            print(chr(i + 97), end=" | ")
            for j in range(0, 8):
                item = self.board[i][j]
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 37)

    def getPosition(self, message):
        print({0}, format(message))
        pos1, pos2 = input().split()
        x1 = ord(pos1[0]) - 97
        y1 = ord(pos1[1]) - 49
        x2 = ord(pos2[0]) - 97
        y2 = ord(pos2[1]) - 49

    def pieceByPosition(self, x, y):  # Метод определения фигуры по заданным координатам
        item = self.board[x][y]
        print(str(item))
        self.print_name(item.value)

    async def EnemyMove(self):
        tx = random.randint(0, 7)
        ty = random.randint(0, 7)
        while not isinstance(self.board[tx][ty], Pawn) or self.board[tx][ty].color.value == 1:
            tx = random.randint(0, 7)
            ty = random.randint(0, 7)
        self.board[self.board[tx][ty].makeMove(tx, ty)[0]][self.board[tx][ty].makeMove(tx, ty)[1]] = self.board[tx][ty]
        self.board[tx][ty] = Empty()
        print("Enemy's turn...")
        await asyncio.sleep(2)

    async def movePiece(self):  # Метод передвижения фигуры
        try:
            while True:
                if keyboard.is_pressed('Esc'):
                    print("Thanks for playing!")
                    sys.exit(0)
                if keyboard.is_pressed('ENTER'):
                    coordInput = input()
                    break
            if coordInput.count(" ") == 1 and len(coordInput) == 5:
                pos1, pos2 = coordInput.split(" ")
                if len(pos1) == 2 and len(pos2) == 2 and "a" <= pos1[0] <= "h" and "a" <= pos2[0] <= "h" and "1" <= \
                        pos1[1] <= "8" and "1" <= pos2[1] <= "8" and pos1 != pos2:
                    x1 = ord(pos1[0]) - 97
                    y1 = ord(pos1[1]) - 49
                    x2 = ord(pos2[0]) - 97
                    y2 = ord(pos2[1]) - 49
                    try:
                        if isinstance(self.board[x1][y1], Empty):
                            raise EmptyCellException(x1, y1)
                        else:
                            if self.board[x1][y1].movesAvailable(x1, y1, x2, y2) and self.board[x1][
                                y1].color.value == 1 and self.board[x2][y2].color.value != self.board[x1][
                                y1].color.value:
                                self.board[x2][y2] = self.board[x1][y1]
                                self.board[x1][y1] = Empty()
                                raise UserTurnIsOver()
                            else:
                                print("Move is not available!")
                                await self.movePiece()
                    except EmptyCellException as error:
                        print(error.msg)
                        await self.movePiece()
                else:
                    raise IncorrectInputException()
            else:
                raise IncorrectInputException()
        except IncorrectInputException as error:
            print(error.msg)

    async def startGame(self):
        userTurn = asyncio.create_task(self.movePiece())
        enemyTurn = asyncio.create_task(self.EnemyMove())
        try:
            await userTurn
        except UserTurnIsOver:
            await enemyTurn
        self.printBoard()
