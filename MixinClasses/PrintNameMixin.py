class PrintNameMixin:
    def print_name(self, value):
        if value == 0:
            print("This is an empty cell")
        elif value == 1:
            print("This is a pawn")
        elif value == 2:
            print("This is a knight")
        elif value == 3:
            print("This is a bishop")
        elif value == 4:
            print("This is a rook")
        elif value == 5:
            print("This is a queen")
        elif value == 6:
            print("This is a king")