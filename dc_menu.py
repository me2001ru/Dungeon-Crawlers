"""
Objective:
    -create menu
    -save game
    -load game
"""
import time
import json
import sys
import os
from characters_temp import Knight, Wizard, Thief

text0 = "Welcome user!"
text1 = "Are you ready to play?..."
text2 = "Ok.. let's begin, shall we!"
text3 = "Opting out?...."
text4 = "Create new player (N) / Load player (L)"
text5 = "Option N/A.\nTry again..."


def print_appealing_text(my_string):
    print()
    for position in my_string:
        print(position, end='', flush=True)
        # !!!! don't forget to change value to 0,05 after testing !!!!
        time.sleep(.001)
    time.sleep(0.5)


def load_character():
    if os.path.getsize("characters_list.json") != 0:
        with open("characters_list.json", "r") as input_file:
            data = json.load(input_file)

            characters_list = []
            for an_object in data["Heros"]:
                attribute_list = list(an_object.values())

                # change attribute_list[3] to set appointed health-status when loaded in.
                if attribute_list[1] == "Knight":
                    characters_list.append(Knight(attribute_list[0], attribute_list[1], attribute_list[2],
                                                  attribute_list[3], attribute_list[4], attribute_list[5], attribute_list[6]))
                elif attribute_list[1] == "Wizard":
                    characters_list.append(Wizard(attribute_list[0], attribute_list[1], attribute_list[2],
                                                  attribute_list[3], attribute_list[4], attribute_list[5], attribute_list[6]))
                elif attribute_list[1] == "Thief":
                    characters_list.append(Thief(attribute_list[0], attribute_list[1], attribute_list[2],
                                                 attribute_list[3], attribute_list[4], attribute_list[5], attribute_list[6]))

            # storing names of characters that are, in reserved_names list
            reserved_names = []
            for individual in characters_list:
                individual_attributes = list(individual.__dict__.values())
                reserved_names.append(individual_attributes[0])

    else:
        # Nothing to load
        characters_list = []
        reserved_names = []

    return characters_list, reserved_names


def create_new_character(reserved_names):
    print("Ok. Lets create a new Hero for you !")
    # List All Heros, when user has made pick, instantiate object.
    try:
        hero_selection = int(
            input("1.The Knight !\n2.Wizard\n3.The Thief\n>>"))
    except Exception as e:
        print(e)

    name_occupied = True
    while name_occupied:
        hero_name = input("Give your hero a name: ")

        # checks in list if name is already taken
        if hero_name not in reserved_names:
            name_occupied = False
        else:
            print("Name N/A... choose different name please")

    if hero_selection == 1:
        new_character = Knight(hero_name, "Knight", 5, 9, 6, 4, "Shield Block")
    elif hero_selection == 2:
        new_character = Wizard(hero_name, "Wizard", 6,
                               4, 9, 5, "Blinding Light")
    elif hero_selection == 3:
        new_character = Thief(hero_name, "Thief", 7, 5, 5, 7, "Critical Hit")
    else:
        print_appealing_text(text5)

    print(f"Hero is now created! You hero is: {new_character.name}")
    print(new_character)

    return new_character


def retrieve_my_saved_character(characters_list, reserved_names):
    print("---------SAVED HERO OPTIONS---------")
    for count, char in enumerate(reserved_names, 1):
        print(count, char)
    my_char = int(input("\nWhich is your saved character? "))

    game_character = characters_list[my_char-1]
    return game_character


def choose_map_function():
    print("-----------MAP SELECTION------------")
    print("Let's pick a map now!")
    print("Game size: \n- Small\n- Medium or\n- Large")


def save_character(characters_list):
    data = {}
    data["Heros"] = []

    # converting each object to dict-form

    def convert_to_dict(individual):
        individual = individual.__dict__
        return individual

    # converts data to dict and save in "Hero"
    for individual in characters_list:
        dict_individual = individual.__dict__
        data["Heros"].append(dict_individual)

    # saving data into characters_list.json
    with open("characters_list.json", "w") as output_file:
        json.dump(data, output_file, indent=4)


def quit_game(characters_list):
    if len(characters_list) > 0:
        # diverts to save_character function if list of characters not empty
        save_character(characters_list)

    print("QUITING", end="")
    for index in range(4):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()


def start_game():
    print_appealing_text(text2)

    # # Read in the saved heros
    loaded_list_tuple = load_character()
    characters_list = loaded_list_tuple[0]
    reserved_names = loaded_list_tuple[1]
    print()
    # only prints names of characters loaded into game, for confiramtion it worked.
    for test in characters_list:
        print(test.__repr__())

    input_not_fulfilled = True
    while input_not_fulfilled:
        # user promp to create or load character
        print_appealing_text(text4)
        user_entry2 = input("\n>>").upper()

        if user_entry2 == 'N':
            input_not_fulfilled = False

            # call function for New Character
            game_character = create_new_character(reserved_names)
            characters_list.append(game_character)

        elif user_entry2 == 'L':
            input_not_fulfilled = False

            # call function for Load
            game_character = retrieve_my_saved_character(
                characters_list, reserved_names)

        else:
            print_appealing_text(text5)

    # Once Hero created/loaded, now user chooses map size HERE
    input(
        f"OK {game_character.name}, ready for the next step? If so, press enter\n>>")

    # call map-function here, Skickar till Lennarts funktion.
    map_size_choice()

    # If user leaves map, dies or manually wants to quit: quit_game function is called
    quit_game(characters_list)


def main():

    print_appealing_text(text0)
    print_appealing_text(text1)

    user_entry = input("\nIf so, press C to continue.\n>>").upper()

    if user_entry == 'C':
        start_game()
    else:
        print_appealing_text(text3)
        sys.exit(0)


if __name__ == "__main__":
    main()
