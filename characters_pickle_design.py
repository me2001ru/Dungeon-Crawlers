import json
import pickle


class Characters:
    def __init__(self, name, character, initiative, endurance, attack, agility, special, wallet):
        self.name = name
        self.character = character
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special
        self.wallet = wallet

    def all_stats(self):  # function that prints out all-stats of object
        allstats = self.__dict__
        return allstats

    def __repr__(self):
        return "{:<10}{:<13}{:<13}{:<10}{:<10}{:<8}{:<19}{:<13}".format(self.name, self.character, self.initiative, self.endurance, self.attack, self.agility, self.special, self.wallet)

    def load_pickle(self):  # load pickle file that collects all characters
        char_list = []
        with open("saved_characters.pkl", "rb") as fp:
            try:
                while True:
                    loaded_file = pickle.load(fp)
                    char_list.append(loaded_file)
            except:
                pass
        return char_list

    def save(self, character):  # save characters in pickle file
        char_list = []
        with open("saved_characters.pkl", "rb") as fp:
            try:
                while True:
                    loaded_file = pickle.load(fp)
                    char_list.append(loaded_file)
            except:
                pass
        with open("saved_characters.pkl", "wb") as pf:
            for i in char_list:
                index = char_list.index(i)
                pickle.dump(char_list[index], pf)
            pickle.dump(character, pf)


class Handle(Characters):  # Class that can later be assigned to a variable, enables you to use all inherited functions inside of parent-class.
    def __init__(self):
        pass


class Knight(Characters):  # The characters
    def __init__(self, name):
        super().__init__(name, "Knight", 5, 9, 6, 4, "Shield Block", 0)


class Wizard(Characters):
    def __init__(self, name):
        super().__init__(name, "Wizard", 6, 4, 9, 5, "Blinding Light", 0)


class Thief(Characters):
    def __init__(self, name):
        super().__init__(name, "Thief", 7, 5, 5, 7, "Critical Hit", 0)
