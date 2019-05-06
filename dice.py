import random as rnd

def dice4():
    return rnd.randrange(1,4,1)


if __name__ == "__main__":
    print("4d: " + str(dice4()))
