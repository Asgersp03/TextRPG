import creature

class Character(creature.Creature):
    """Klasse til at repræsenterer en karakter i spillet"""
    def __init__(self, name):
        """name angiver karakterens navn"""
        creature.Creature.__init__(self, name, 15, 1, 5, 5)


        self.xp = 0 # ud af uendelig
        print("Karakteren " + self.name + " er oprettet: ")
        print("Hit Points = " + str(self.hp))
        print("Experience Points = " + str(self.xp))
        print("")





