from items import Sword

class Entity:
    hp = 999
    proper = False
    def damage(self, attack):
        pre = self.hp
        if self.hp > 0:
            self.hp -= attack
            if self.hp > 0 and self.proper == False:
                print("The " + self.name + " has " + str(self.hp) + " hp.")
            if self.hp >0 and self.proper == True:
                print(self.name + " has " + str(self.hp) + " hp.")
            elif self.hp <= 0 and self.proper == False:
                print("You have killed the " + self.name + ".")
            elif self.hp <= 0 and self.proper == True:
                print("You have killed " + self.name + ".")
        elif self.proper == True:
            print(self.name + " is already dead.")
        else:
            print("The " + self.name + " is already dead.")
        return (pre - self.hp)


class Player(Entity):
    gold = 0
    inventory = {
        "sword": Sword()
    }
    name = "Hero #7781"
    hp = 20
    attack = 1
    desc = "A dashing hero."
    location = "Dungeon"


class Goblin(Entity):
    name = "Goby"
    proper = False
    true_name = "goblin"
    hp = 5
    attack = 1
    desc = 'It is a stout, green, humanoid.'
    location = "Dungeon"

    #def __init__(self):
    #    print("A wild Goblin has appeared!")