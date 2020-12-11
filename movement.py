from dungeonmap import DungeonMap


class Movement:
    def __init__(self, b):
        self.start = [0, 0]
        self.goal = [b, b]
        self.player = [0, 0]

    def move_player(self, d, b):
        x = self.player[0]
        y = self.player[1]

        if d == 'r':
            self.player[0] += 1
            print("player position:", self.player)

        elif d == 'l':
            self.player[0] -= 1
            print("player position:", self.player)

        elif d == 'u':
            self.player[1] -= 1
            print("player position:", self.player)

        elif d == 'd':
            self.player[1] += 1
            print("player position:", self.player)

        else:
            print("Wrong command ! ")

        if self.player == self.goal:
            print("You made it to the end!")

        if (self.player[1] < 0):
            print("Outside bounds Y")
            self.player[1] += 1
            print("Bringing you back to position: ", self.player)

        if (self.player[1] > b):
            print("Outside bounds Y")
            self.player[1] -= 1
            print("Bringing you back to position: ", self.player)

        if (self.player[0] < 0):
            print("Outside bounds X")
            self.player[0] += 1
            print("Bringing you back to position: ", self.player)

        if (self.player[0] > b):
            print("Outside bounds X")
            self.player[0] -= 1
            print("Bringing you back to position: ", self.player)


def ok():
    b = int(input("How big do you want your map? "))
    c = Movement(b)
    a = DungeonMap(b)

    while c.player != c.goal:
        d = input("Which way? (r, l, u, d)  >>")
        c.move_player(d, b)
        a.display_map()
