from DungeonWorld import DungeonMap
from pickle_menu import *
from monster_treasure import *
from fight_adi import *


class Movement:
    def __init__(self, startzone, endzone):
        self.start = (startzone[0], startzone[1])
        self.goal = endzone
        self.player = startzone
        self.walls = (0, 0)
        self.clean = ("\n" * 100)
        self.banana = 0

    def move_player(self, d, startzone, mapsize, a, in_game_char, all_obj):
        x = self.player[0]
        y = self.player[1]
        pos = startzone

        if d == 'd':
            pos = (x + 1, y)
            print(self.clean)
            banner_text("You move to the right...\n")
            time.sleep(1)

        elif d == 'a':
            pos = (x - 1, y)
            print(self.clean)
            banner_text("You move to the left...\n")
            time.sleep(1)

        elif d == 'w':
            pos = (x, y - 1)
            print(self.clean)
            banner_text("You take the stairs up...\n")
            time.sleep(1)

        elif d == 's':
            pos = (x, y + 1)
            print(self.clean)
            banner_text("You take the stairs down...\n")
            time.sleep(1)

        else:
            pos = self.player

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print(self.clean)
            banner_text("You have made it to a very large mechanical door of sort, with a lever right next to it...\n")
            banner_text('"This must be the exit!" You think to yourself\n')
            time.sleep(1)
            last_choice = int(input("But do you greed more treasure or leave with what you have?\n1 = Stay\n2 = Leave\n"))

            # NEEDS TRY/EXCEPT
            if last_choice == 1:
                banner_text("You have decided to stay and return to the previous room...")
                input()
                self.player = (x, y)
                pos = self.player
                print(self.clean)

            else:
                banner_text("You pull the lever and is met with fresh air and sound of nature, you leave the dungeon into the sunshine")
                input()
                self.banana = 5
                quit_game()

        if (pos[1] < 0) or (pos[0] < 0) or (pos[0] > (mapsize - 1)) or (pos[1] > (mapsize - 1)):
            print(self.clean)
            banner_text("As you leave the room, darkness sweeps over you! When you finally manage to find your bearings, your back in the previous room again...")
            time.sleep(1)
            print(self.clean)
            self.player = (x, y)
            pos = self.player
        else:
            victory = False
            goldpls = 0
            if a.board[self.player[1]][self.player[0]] == "+":
                handle = HandleFunc()
                monst = handle.ShuffleMonster()

                for i in monst:
                    if i != None:
                        banner_text("Something is in this room, prepare for combat...\n\n\n\n")
                        time.sleep(1)
                        victory = fightOrFlight(i, in_game_char)
                        goldpls += 1

                if (victory == True or goldpls == 0):
                    handle2 = ShuffleTest()
                    loot = handle2.ShuffleBro()
                    summa = sum(loot)
                    handle3 = Handle()
                    # all_obj = handle3.load_pickle()

                    for i in all_obj:
                        if i.name == in_game_char.name:
                            in_game_char.wallet += summa
                    handle3.edit_char(all_obj)

                    print(self.clean)
                    banner_text("You search the entire room for valuables...")
                    time.sleep(2)
                    if summa != 0:
                        banner_text("you have found some loot!")
                        print("\nLOOT & VALUE from this room")
                        if loot[0] > 0:
                            print(f'\nCoins: {loot[0]}')
                        if loot[1] > 0:
                            print(f'Money pouch: {loot[1]}')
                        if loot[2] > 0:
                            print(f'Gold Jewelry: {loot[2]} ')
                        if loot[3] > 0:
                            print(f'Gems: {loot[3]}')
                        if loot[4] > 0:
                            print(f'Small Treasure Chest: {loot[4]}')
                        print(f'\nTotal riches collected here: {summa}')
                        input("Press any key to continue...")
                    else:
                        banner_text("you found nothing of value in the room and carry on!")
                        time.sleep(2)

                else:
                    banner_text("You retreat back so you receive no treasure!")
                    self.player = (x, y)
                    pos = self.player

            a.board[self.goal[1]][self.goal[0]] = "E"
            a.board[self.player[1]][self.player[0]] = "O"
            a.board[y][x] = "-"
            a.board[self.start[1]][self.start[0]] = "S"


def ok(mapsize, startzone, endzone, in_game_char, all_obj):
    c = Movement(startzone, endzone)
    a = DungeonMap(mapsize)
    in_game_char = in_game_char

    while c.banana != 5:
        print(c.clean)
        print("Theres light emitting from rooms, both left and right of your location...")
        print("but also above and below as you spot a staircase")
        a.display_map()
        d = input("Which way? (d, a, w, s)  \n>>")
        c.move_player(d, startzone, mapsize, a, in_game_char, all_obj)
