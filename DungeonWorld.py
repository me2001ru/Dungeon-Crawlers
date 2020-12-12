class DungeonMap:
    def __init__(self, size):
        self.board = []
        self.create_map(size)

    def create_map(self, size):
        for width in range(size):
            self.board.append([])
            for height in range(size):
                self.board[width].append("+")

    def display_map(self):
        for row in self.board:
            print(" ".join(row))
