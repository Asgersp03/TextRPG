import verden

from character import Character
from monster_generator import RandomMonster


gamemap = verden.Verden()

player = Character("Asger")

print("Asgers starter med XP = " + str(player.xp))

randomMonster = RandomMonster(player.xp)

gameover = False

# Game loop
while not gameover:
    # TODO: Tilføj en evt. event

    # Print description
    gamemap.printDescription()
    # Print options
    gamemap.printOptions()
    svar = input(">>")


    # TODO: Håndter handling

    # Check player character status
    if not player.isAlive():
        gameover = True
