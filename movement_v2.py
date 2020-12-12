from DungeonWorld import DungeonMap


class Movement:
    def __init__(self, startzone, endzone):
        self.start = (startzone[0], startzone[1])
        self.goal = endzone
        self.player = startzone
        self.walls = (0, 0)

    def move_player(self, d, startzone, mapsize, a):
        x = self.player[0]
        y = self.player[1]
        pos = startzone

        if d == 'r':
            pos = (x + 1, y)
            # REMOVE ME DEV TEXT
            print(pos)
            print("pos")
            print(self.player)
            print("player")
            print(self.goal)

        elif d == 'l':
            pos = (x - 1, y)
            # REMOVE ME DEV TEXT
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        elif d == 'u':
            pos = (x, y - 1)
            # REMOVE ME DEV TEXT
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        elif d == 'd':
            pos = (x, y + 1)
            # REMOVE ME DEV TEXT
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        else:
            pass

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print("You made it to the end!")

        if (pos[1] < 0) or (pos[0] < 0) or (pos[0] > (mapsize - 1)) or (pos[1] > (mapsize - 1)):
            print("Outside bounds!")
            self.player = (x, y)
            pos = self.player
        else:
            a.board[self.goal[1]][self.goal[0]] = "E"
            a.board[self.player[1]][self.player[0]] = "O"
            a.board[y][x] = "-"
            a.board[self.start[1]][self.start[0]] = "S"


'''
    def placemonster(self):
        for i in range(b + 2):
            randcordx = randint(1, b - 2)
            randcordy = randint(1, b - 2)
            print(f'{randcordx},{randcordy}')
            a.board[randcordx][randcordy] = "O"
        a.display_map()
'''


def ok(mapsize, startzone, endzone):
    c = Movement(startzone, endzone)
    a = DungeonMap(mapsize)

    while c.player != c.goal:
        a.display_map()
        d = input("Which way? (r, l, u, d)\n")
        c.move_player(d, startzone, mapsize, a)
