from reader import exe, interpret
from props import *
from entitys import *
from items import *



def load(save):
    """
    Loads a save file by executing all of its actions.
    :param save: The file to be loaded
    :return: None
    """
    file = open(save, "r")
    events = file.read
    file.close()
    events = str(events)
    for action in events:
        exe(action[0], verbs, action[2], exceptions, action[1])



def words(words):
    return (None, None, None, words)
def descriptor(descriptor):
    return (None, None, descriptor)
def subject(subject):
    return (None, subject)
def noun(noun):
    return (None, noun, None)
def verb(verb):
    return (verb, None, None)

def say(act):
        cont = str(act[3])
        print(Player.name + ': ' + cont)
def attack(act):
        enemy = act[1]
        global ran
        if enemy in nouns:
            if act[6] is not None:
                nouns[enemy].damage(act[6])
                return
            if act[2] == "with":
                try:
                    if act[4] in Player.inventory:
                        damage = nouns[act[4]].strike()
                        ran = nouns[enemy].damage(damage)
                        return ran
                    else:
                        print("You do not have that.")
                except:
                    print("You cannot attack that.")
            else:
                try:
                    nouns[enemy].damage(1)
                    ran = 1
                    return ran
                except:
                    print("You cannot attack that.")
        else:
            print("That does not exist.")
def loot(act):
        target = act[1]
        if nouns[target].hp <= 0:
            Player.gold += random.randrange(3, 15)
            print("You now have " + str(Player.gold) + " gold.")
        else:
            print("You cannot loot that.")
def help(*args):
        print(verbs.keys())
        print(nouns.keys())
def search(act):
        present = list()
        if act[2] == "at":
            print(nouns[act[1]].desc)
        else:
            for noun in nouns:
                try:
                    if nouns[noun].location is Player.location:
                        present.append(noun)
                except:
                    None
            for noun in present:
                print("There is a " + nouns[noun].true_name + " named " + nouns[noun].name + ".")
                print(nouns[noun].desc + "\n")
        del present
def spawn_goblin(act):
        if act[1] is not None:
            title = act[1]
        else:
            title = act[3]
        nouns[title] = Goblin()
        nouns[title].name = title
        nouns[title].proper = True
def spawn_flask(act):
        nouns['flask'] = Flask()
        Flask.cont = act[2]
def spawn_puddle(*args):
        nouns['puddle'] = puddle()
def spawn_sword(*args):
    nouns['sword'] = Sword()
def fill(act):
        try:
            if act[2] == "with":
                if act[1] in nouns:
                    nouns[act[1]].cont = (nouns[act[4]].true_name)
                    print(nouns[act[1]].desc)
                else:
                    print("You cannot do that.")
            else:
                raise SyntaxError("That does not make sense.")
        except Exception as e:
            print(e)
def invetory(*args):
    print("Gold: " + str(Player.gold))
    print("Items: ")
    for item in Player.inventory:
        print("\n     " + Player.inventory[item].name)
def drop(act):
    if act[1] in Player.inventory:
        del Player.inventory[act[1]]
        print("You have dropped the " + act[1] + ".")
    else:
        print("You cannot do that.")
def pick(act):
    if nouns[act[1]].location == Player.location:
        if act[1] in Player.inventory:
            print("You already have that.")
            return
        Player.inventory[act[1]] = nouns[act[1]]
        print("You have picked up the " + act[1] + ".")
    else:
        print("You cannot pick that up.")
def check(act):
    print("1" + str(act[0]), "2" + str(act[1]), "3" + str(act[2]), "4" + str(act[3]), "5" + str(act[4]))
def again(act):
    #try:
        line = ((act_log[len(act_log)-1])[0])
        exe(line, verbs, nouns, exceptions, act[4])
    #except(IndexError):
     #   print("You haven't done anything yet.")


verbs = {
    "say": say,
    "examine": search,
    "attack": attack,
    "search": search,
    "look": search,
    "loot": loot,
    "help": help,
    "spawn_goblin": spawn_goblin,
    "inventory": invetory,
    "fill": fill,
    "check": check,
    "drop": drop,
    "pick": pick,
    "grab": pick,
    "take": pick,
    "get": pick,
    "again": again,
    "repeat": again,
    "rep": again
}
exceptions = ("say", "check")
nouns = {
    "ooze": "ooze"
}

print("You awaken to find yourself in a dungeon.  \nThere is a GOBLIN, a FLASK, and a PUDDLE.\nAll you have is your trusty SWORD.")
spawn_goblin(subject("goblin"))
Player = Player
spawn_flask(words(None))
spawn_puddle(None)
spawn_sword(None)
prev_input = None
act_log = list()
ran = None


#load("save1.txt")
save = open("save1.txt", 'w')

while True:
    #try:
        line = input(": ")
        exe(line, verbs, nouns, exceptions, None)
        log = interpret(line, verbs, nouns, exceptions, ran)
        if verbs[log[0]] == again:
            act_log.append(((act_log[len(act_log)-1])[0], ran, nouns))
        else:
            act_log.append((line, ran, nouns))
        print(ran)
        ran = None
        print(act_log)
        save.write(str(act_log[(len(act_log)-1)]) + "\n")
        if "###" in log:
            break
    #except Exception as e:
        #print(e)

save.close()