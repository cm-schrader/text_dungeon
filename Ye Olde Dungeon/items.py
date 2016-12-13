import random

class Item:
    def put(self, container):
        self.holder = container

class Weapon(Item):
    attack = 1
    rng = 0
    crit = 0
    location = "Dungeon"

    def strike(self):
        random.seed = random.randint
        vary1 = (self.attack - self.rng)
        vary2 = (self.attack + self.rng)
        if random.randrange(0,100) < self.crit:
            dmg = int((self.attack + self.rng) * 1.5)
            print("You land a flawless strike.")
        else:
            dmg = random.randrange(vary1, vary2)
        return dmg


class Sword(Weapon):
    name = "Broad Sword"
    true_name = "Sword"
    attack = 3
    rng = 1
    crit = 3
    location = "Dungeon"


class Flask(Item):
    name = "flask"
    true_name = "flask"
    cont = "empty"
    location = "Dungeon"

    #def __init__(self):
    #    desc = ('It is filled with ' + self.cont)

    @property
    def desc(self):
        if self.cont is None:
            return "It is empty."
        else:
            return "It is filled with " + self.cont + "."

    def fill(self, liquid):
        self.cont = liquid


