import creature
import random as rnd
import monsters.orc as orc



def create_monster_xp(hero_xp):
    return round(pow(1.2, hero_xp)+5) + rnd.randrange(-5, 5, 1)


class RandomMonster(creature.Creature):
    def __init__(self, hero_xp):
        """name angiver karakterens navn"""

        hp = create_monster_xp(hero_xp)
        defence = 5 # TODO
        strength = 1 # TODO
        initiative = 1 # TODO

        name = rnd.choice(["Orc", "Troll", "Gnome"])
        creature.Creature.__init__(self, name, hp, defence, strength, initiative)






if __name__ == "__main__":
    randomMonster = RandomMonster(0)
    randomMonster2 = RandomMonster(10)
    randomMonster3 = RandomMonster(25)
    print("Creating an Orc...")
    anOrc=orc.Orc()


