import random
from characters_adi import *
from monster_treasure import *


def monster(mon):
    if (mon.monster == 'GiantSpider'):
        # mon_stat = {'monster': 'Giant spider', 'stats':(7, 1, 1, 3)}
        mon_stat = mon.monster_stats()
    elif (mon.monster == 'Troll'):
        # mon_stat = {'monster': 'Troll', 'stats':(4, 2, 3, 3)}
        mon_stat = mon.monster_stats()
    elif (mon.monster == 'Skeletton'):
        # mon_stat = {'monster': 'Skeleton', 'stats':(6, 3, 4, 4)}
        mon_stat = mon.monster_stats()
    elif (mon.monster == 'Orc'):
        # mon_stat = {'monster': 'Orc', 'stats':(2, 4, 7, 2)}
        mon_stat = mon.monster_stats()
    return mon_stat


def character(char):

    if (char.character == 'Knight'):
        # char_stat = {'character': 'Paladin', 'stats': (5, 9, 6, 4), 'special': 'shield'}
        char_stat = char.all_stats()
    elif (char.character == 'Wizard'):
        # char_stat = {'character': 'Wizard', 'stats': (6, 4, 9, 5), 'special': 'flashlight'}
        char_stat = char.all_stats()
    elif (char.character == 'Thief'):
        # char_stat = {'character': 'Rogue', 'stats': (7, 5, 5, 7), 'special': 'doubleDamage'}
        char_stat = char.all_stats()
    return char_stat


def rngjesus(att, agi):
    damage = 0
    luck = 0
    while(att > 0):
        damage += random.randint(1, 7)
        att -= 1
    while(agi > 0):
        luck += random.randint(1, 7)
        agi -= 1
    if (damage >= luck):
        print(f"damage: {damage} luck: {luck}")
        return True
    else:
        print(f"damage: {damage} luck: {luck}")
        return False


def charAttack(mon, char, mon_hp):
    dialog2 = f"{character(char)['character']} attacks the {monster(mon)['monster']} and deals 1 damage\n"
    dialog5 = f"{character(char)['character']} deals double damage\n"
    dialog9 = f"{monster(mon)['monster']} meet its end by the hand of the {character(char)['character']}\n"
    dialog10 = f"{monster(mon)['monster']} dodges {character(char)['character']}s attack\n"

    rogueSpecial = 1  # random.randint(1,2)
    if (rogueSpecial == 1):
        rng = True
    else:
        rng = False

    if (character(char)['special'] == 'Critical Hit' and rng == True):
        if (rngjesus(character(char)['attack'], monster(mon)['agility']) == True):  # mon_hp -= character(char)['stats'][2] * 2
            mon_hp -= 2
            if (mon_hp <= 0):
                print(dialog5)  # Character deals double damage
                print(dialog9)  # Monster dies
                # break
            else:
                print(dialog5)  # Character deals double damage
                print(f"Hp left: {mon_hp}\n")
        else:
            print(dialog10)  # Monster dodges attack
    else:
        if (rngjesus(character(char)['attack'], monster(mon)['agility']) == True):
            mon_hp -= 1
            if (mon_hp == 0):
                print(dialog2)  # Character attacks normally
                print(dialog9)  # Monster dies
                # break
            else:
                print(dialog2)  # Character attacks normally
                print(f"Hp left: {mon_hp}\n")
        else:
            print(dialog10)  # Monster dodges attack
    return mon_hp


def monAttack(initiative, mon, char, special, char_hp):
    dialog3 = f"{monster(mon)['monster']} takes the initiative and attack first\n"
    dialog4 = f"{character(char)['character']} blocks attack with his shield\n"
    dialog7 = f"{character(char)['character']} takes 1 damage but still stands\n"
    dialog8 = f"{character(char)['character']} takes 1 damage and meet his end\n"
    dialog11 = f"{character(char)['character']} dodges {monster(mon)['monster']}s attack\n"
    dialog12 = f"{monster(mon)['monster']} attacks {character(char)['character']} 1 damage\n"

    if (initiative == 'first'):
        print(dialog3)  # Monster attacks first
        if (character(char)['special'] == 'Shield Block' and special == True):
            print(dialog4)  # Character blocks attack
            special = False
        else:
            if (rngjesus(monster(mon)['attack'], character(char)['agility']) == True):  # Throw dice, mon attack / char agil
                char_hp -= 1
                if (char_hp == 0):
                    print(dialog8)  # Character dies
                    # break
                print(dialog7)  # Character takes damage
                print(f"Hp left: {char_hp}\n")
            else:
                print(dialog11)
    else:
        if (character(char)['special'] == 'Shield Block' and special == True):
            print(dialog4)  # Character blocks attack
            special = False
            if (rngjesus(monster(mon)['attack'], character(char)['agility']) == True):
                char_hp -= 1
                if (char_hp == 0):
                    print(dialog8)  # Character dies
                    # break
                else:
                    print(dialog12)
                    print(f"Hp left: {char_hp}\n")
            else:
                print(dialog11)
        else:
            if (rngjesus(monster(mon)['attack'], character(char)['agility']) == True):
                char_hp -= 1
                if (char_hp == 0):
                    print(dialog8)  # Character dies
                    # break
                else:
                    print(dialog12)
                    print(f"Hp left: {char_hp}\n")
            else:
                print(dialog11)
    return {'hp': char_hp, 'special': special}


def fightOrFlight(mon, char):
    #rngjesus(mon, char)
    special = True
    mon_initiative = False  # If true, monster starts every round
    if (rngjesus(monster(mon)['initiative'], character(char)['initiative']) == True):
        mon_initiative = True

    chanceToFlee = character(char)['agility'] * 10
    fleeRND = random.randint(0, 100)
    if (chanceToFlee <= fleeRND):
        successfulEscape = True
    else:
        successfulEscape = False

    mon_hp = monster(mon)['endurance']
    char_hp = character(char)['endurance']

    dialog1 = f"You encounter a {monster(mon)['monster']}\n"
    dialog6 = f"{character(char)['character']} brights up the room with a spell\n"
    print(dialog1)  # Character encounters a monster

    while (mon_hp > 0 and char_hp > 0):
        print(f"Monster HP: {mon_hp}  Character HP: {char_hp}")
        while True:
            choise = input(f"Will you attack (a) or run (r)? \n")
            if (choise != 'a' and choise != 'r'):
                print("answer should be 'a' or 'r' ")
                continue
            else:
                break

        if (choise == 'a'):  # Character attacks

            if (mon_initiative == True):
                char_hp = monAttack('first', mon, char, special, char_hp)['hp']
                special = monAttack('second', mon, char, special, char_hp)['special']
                if (char_hp > 0):
                    mon_hp = charAttack(mon, char, mon_hp)
                else:
                    break
            else:
                mon_hp = charAttack(mon, char, mon_hp)
                if (mon_hp > 0):
                    char_hp = monAttack('second', mon, char, special, char_hp)['hp']
                    special = monAttack('second', mon, char, special, char_hp)['special']
                else:
                    break

        elif (choise == 'r'):  # Character tries to run
            if (character(char)['special'] == 'Blinding Light' and special == True):
                chanceToFlee = 8
                print(dialog6)  # Character use flashlight to escape
                special = False
                break
            if (successfulEscape == True):
                print("your escape was successful")

            else:
                print("You cant run from this battle, fight!")


# tr = Troll | sk = Skeleton | sp = Giant spider | or = Orc
# pl = Paladin | wi = Wizard | ro = Rogue
'''
def main():
    rndMon = random.randint(0,5)
    if rndMon == 1:
        mon = GiantSpider()
    elif rndMon == 2:
        mon = Skeletton()
    elif rndMon == 3:
        mon = Orc()
    else:
        mon = Troll()
    choice = int(input("Choose what you want to be:\n 1. Knight, 2. Wizard, 3. Thief\n : "))
    if choice == 1:
        username = input("You choice was to become a Knight! Enter username for your Knight: ")
        champ = Knight(username)
        fightOrFlight(mon, champ)
    if choice == 2:
        username = input("You choice was to become a Wizard! Enter username for your Wizard: ")
        champ = Wizard(username)
        fightOrFlight(mon, champ)
    if choice == 3:
        username = input("You choice was to become a Thief! Enter username for your Thief: ")
        champ = Thief(username)
        fightOrFlight(mon, champ)
    # name = input("Name: ")
    # champ = Knight(name)
    # fightOrFlight('or', champ)


if __name__ == "__main__":
    main()
'''
