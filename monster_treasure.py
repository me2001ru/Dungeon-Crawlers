import random


class Monster:
    def __init__(self, monster, initative, endurance, attack, agility, common):
        self.monster = monster
        self.initiative = initative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.common = common

    def monster_stats(self):
        monster_stats = self.__dict__
        return monster_stats

    def ShuffleMonster(self):

        a = GiantSpider()
        b = Skeletton()
        c = Orc()
        d = Troll()

        shuffle_spider = [a, None]
        shuffle_skeletton = [b, None]
        shuffle_orc = [c, None]
        shuffle_troll = [d, None]

        random_spider = random.choices(shuffle_spider, weights=[20, 80], k=1)
        random_skeletton = random.choices(shuffle_skeletton, weights=[15, 85], k=1)
        random_orc = random.choices(shuffle_orc, weights=[10, 90], k=1)
        random_troll = random.choices(shuffle_troll, weights=[0.05, 95], k=1)
        shuffled_monsters = random_spider + random_skeletton + random_orc + random_troll
        return shuffled_monsters


class HandleFunc(Monster):
    def __init__(self):
        pass


class GiantSpider(Monster):
    def __init__(self):
        super().__init__('GiantSpider', 7, 1, 2, 3, 0.20)


class Skeletton(Monster):
    def __init__(self):
        super().__init__('Skeletton', 4, 2, 3, 3, 0.15)


class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 6, 3, 4, 4, 0.10)


class Troll(Monster):
    def __init__(self):
        super().__init__('Troll', 2, 4, 7, 2, 0.05)


class Treasures:
    def __init__(self, treasure, value):
        self.treasure = treasure
        self.value = value

    def ShuffleBro(self):
        coins = Treasures("Coins", 2)
        money_pouch = Treasures("Money pouch", 6)
        gold_jewelry = Treasures("Gold Jewelry", 10)
        gems = Treasures("Gems", 14)
        small_treasure_chest = Treasures("Small treasure chest", 20)

        shuffle_coins = [coins.value, 0]
        shuffle_money_pouch = [money_pouch.value, 0]
        shuffle_gold_jewelry = [gold_jewelry.value, 0]
        shuffle_gems = [gems.value, 0]
        shuffle_small_treasure_chest = [small_treasure_chest.value, 0]

        random_coins = random.choices(shuffle_coins, weights=[40, 60], k=1)
        random_money_pouch = random.choices(shuffle_money_pouch, weights=[20, 80], k=1)
        random_gold_jewelry = random.choices(shuffle_gold_jewelry, weights=[15, 85], k=1)
        random_gems = random.choices(shuffle_gems, weights=[10, 90], k=1)
        random_treasure_chest = random.choices(shuffle_small_treasure_chest, weights=[5, 95], k=1)
        x = random_coins + random_money_pouch + random_gold_jewelry + random_gems + random_treasure_chest
        return x


class ShuffleTest(Treasures):
    def __init__(self):
        pass
