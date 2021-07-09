from Board import Board
import asyncio

# Основная часть программы для тестирования методов классов.
b = Board()
while True:
    asyncio.run(b.startGame())
