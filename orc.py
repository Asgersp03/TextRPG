import creature

class Orc(creature.Creature):
    """Klasse til at repræsenterer en karakter i spillet"""
    def __init__(self):
        """name angiver karakterens navn"""
        creature.Creature.__init__(self, "Orc", 15, 5, 1, 5)

