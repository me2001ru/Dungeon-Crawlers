"""
Objective: 
    -create menu
    -save game
    -load game
"""
import time
text0 = "Welcome user!"
text1 = "Are you ready to play?..."
text2 = "Ok.. let's begin, shall we!"
text3 = "Opting out?...."
text4 = "Create new player (N) / Load player (L)"
text5 = "Option N/A.\nTry again..."


def print_sexy_text(my_string):
    print()
    for position in my_string:
        print(position, end='', flush=True)
        time.sleep(.05)
    time.sleep(0.5)


def create_new_character():
    print("Ok. Lets create a new Hero for you !")


def load_character():
    print("Ok. Loading your Hero...")


print_sexy_text(text0)
print_sexy_text(text1)

user_entry = input("\nIf so, press C to continue.\n>>").upper()

if user_entry == 'C':
    print_sexy_text(text2)
else:
    print_sexy_text(text3)


input_not_fulfilled = True
while input_not_fulfilled:
    # user promp to create or load character
    print_sexy_text(text4)
    user_entry2 = input("\n>>").upper()

    if user_entry2 == 'N':
        input_not_fulfilled = False
        # call function for New Character
        create_new_character()

    elif user_entry2 == 'L':
        input_not_fulfilled = False
        # call function for Load
        load_character()

    else:
        print_sexy_text(text5)
