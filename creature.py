class Creature:
    """Klasse til at repræsenterer en karakter eller et monster i spillet"""
    def __init__(self, name, hp_max, defence, strength, initiative):
        """name angiver karakterens navn"""
        self.name = name
        self.hp = hp_max
        self.hp_max = hp_max
        self.strength = strength
        self.defence = defence
        self.initiative = initiative
        print("Creating " + self.name + ": ")
        print("Hit Points = " + str(self.hp))
        print("Defence = " + str(self.defence))
        print("")


    def takeDamage(self, hpDamage):
        """hpDamage angiver hvor meget skade karakteren tager og tjekker at hp >= 0"""
        self.hp = max(self.hp - hpDamage, 0)


    def heal(self, hpRestored):
        if self.hp + hpRestored <= self.hp_max:
            self.hp += hpRestored
        else:
            self.hp = self.hp_max


    def isAlive(self):
        """Returns True if character is alive, otherwise False."""
        return self.hp > 0


