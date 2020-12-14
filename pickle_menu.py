import time
import pickle
from DungeonWorld import DungeonMap
from movement_v2 import *
# from characters_pickle_design import *
from characters_adi import *


def banner_text(text):
    for index in text:
        print(index, end='', flush=True)
        time.sleep(0.03)


def map_function(in_game_char, all_obj):
    # MENY SAKER TILL MAPS
    print("\n---MAP SECTION---")
    ask = True
    while ask:
        banner_text("How big do you want your map?\n4x4, 5x5 or 8x8? >>")
        try:
            mapsize = int(input()[0])
            if mapsize == 4 or mapsize == 5 or mapsize == 8:
                ask = False
            else:
                print("Must be 4, 5 or 8... Try again...", end=" ")
        except Exception:
            print("-Exception- Entry must begin with a number...Try again...", end=" ")

    banner_text("\nWhich corner do you want to start in?\nTop Left \t= 1\nBottom Left \t= 2\nTop Right \t= 3\nBottom Left \t= 4\n>>")
    corner = int(input())
    if corner == 1:
        startzone = (0, 0)
        endzone = (mapsize - 1, mapsize - 1)

    elif corner == 2:
        startzone = (0, mapsize - 1)
        endzone = (mapsize - 1, 0)

    elif corner == 3:
        startzone = (mapsize - 1, 0)
        endzone = (0, mapsize - 1)

    elif corner == 4:
        startzone = (mapsize - 1, mapsize - 1)
        endzone = (0, 0)

    # in_game_char latest value to been changed !
    ok(mapsize, startzone, endzone, in_game_char, all_obj)


def quit_game():

    print("QUITING", end="")
    for index in range(4):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()


def new_player_function(reserved_name, game):
    # ------ NEW PLAYER FUCNTION START -----

    banner_text("--------------PICK YOUR HERO--------------")
    time.sleep(0)
    hero_selection = int(input("\n1.The Knight !\n2.Wizard\n3.The Thief\n>>"))
    name_occupied = True
    while name_occupied:
        banner_text("Give your hero a name >>")
        hero_name = input()

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

    return in_game_char

    # ------ NEW PLAYER FUCNTION END -----


def load_player(all_obj):
    # ------ LOAD PLAYER FUCNTION START -----

    print("\n\t\t\t---------SAVED HERO OPTIONS---------")
    print("{:>6}{:>10}{:>15}{:>10}{:>10}{:>10}{:>14}{:>13}\n".format("Name", "Type", "Initiative", "Health", "Attack", "Agility", "Specialty", "Money"))
    for count, obj in enumerate(all_obj, 1):
        print(count, obj)

    try:
        banner_text("CHOOSE SAVED CHARACTER BY NUMBER  >>")
        my_char = int(input())
        in_game_char = all_obj[my_char - 1]
        print("\nChosen character: ", in_game_char.name)
    except Exception:
        print("\nIncorrect value passed forgiven alternatives... u suck!")
        in_game_char = load_player(all_obj)

    return in_game_char

    # ------ LOAD PLAYER FUCNTION END -----


def start_game():
    banner_text("\nWelcome to THE DUNGEON-CRAWLER !\nPress ENTER to START GAME")
    input()

    game = Handle()
    all_obj = game.load_pickle()
    reserved_name = []
    for obj in all_obj:
        reserved_name.append(obj.name)

    input_not_fulfilled = True
    while input_not_fulfilled:
        # user prompt to create or load character
        banner_text("Create new player (N) / Load player (L)  >>")
        user_entry2 = input().upper()

        if user_entry2 == 'N':
            input_not_fulfilled = False
            in_game_char = new_player_function(reserved_name, game)

        elif user_entry2 == 'L':
            input_not_fulfilled = False

            if len(all_obj) == 0:
                banner_text("NO player to choose from.... REDIRECTING TO CREATE NEW PLAYER")
                banner_text("...\n")
                # DIRECT TO NEW PLAYER FUNCTION
                in_game_char = new_player_function(reserved_name, game)

            else:
                in_game_char = load_player(all_obj)

        else:
            print("Option N/A.\nTry again...")

    map_function(in_game_char, all_obj)

    # quit_game(in_game_char)


if __name__ == "__main__":
    start_game()
