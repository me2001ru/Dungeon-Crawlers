import time
import pickle
from dungeonmap import DungeonMap
from movement import *
from characters_pickle_design import *


def map_function():
    ok()


def quit_game():

    print("QUITING", end="")
    for index in range(4):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()


def start_game():
    input("\nWelcome user..to...THE DUNGEON-CRAWLER...!\nPress ENTER to START GAME")

    game = Handle()
    all_obj = game.load_pickle()
    reserved_name = []
    for obj in all_obj:
        reserved_name.append(obj.name)

    input_not_fulfilled = True
    while input_not_fulfilled:
        # user prompt to create or load character
        user_entry2 = input("Create new player (N) / Load player (L)  >>").upper()

        if user_entry2 == 'N':
            input_not_fulfilled = False

            hero_selection = int(input("Pick your Hero\n1.The Knight !\n2.Wizard\n3.The Thief\n>>"))
            name_occupied = True
            while name_occupied:
                hero_name = input("Give your hero a name: ")

                # checks in list if name is already taken or name length not longer then 10 spaces
                if hero_name not in reserved_name and len(hero_name) < 10:
                    name_occupied = False
                else:
                    print("Name taken or too long (MAX 9 characters allowed)")

            # Hero object created and given its name
            if hero_selection == 1:
                in_game_char = Knight(hero_name)
            elif hero_selection == 2:
                in_game_char = Wizard(hero_name)
            elif hero_selection == 3:
                in_game_char = Thief(hero_name)
            else:
                print("Option N/A.\nTry again...")

            # Sparar gubbe (till nästa gång)
            game.save(in_game_char)
            print("OK '" + in_game_char.name + "' let's go!")

        elif user_entry2 == 'L':
            input_not_fulfilled = False

            print("\n\t\t---------SAVED HERO OPTIONS---------")
            print("{:>6}{:>10}{:>15}{:>10}{:>10}{:>10}{:>14}{:>13}\n".format("Name", "Type", "Initiative", "Health", "Attack", "Agility", "Specialty", "Money"))
            for count, obj in enumerate(all_obj, 1):
                print(count, obj)

            my_char = int(input("CHOOSE SAVED CHARACTER BY NUMBER  >>"))
            in_game_char = all_obj[my_char - 1]
            print("Chosen character: ", in_game_char.name)

        else:
            print("Option N/A.\nTry again...")

    map_function()

    quit_game()


if __name__ == "__main__":
    start_game()
