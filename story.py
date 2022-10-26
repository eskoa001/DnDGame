import sys
from time import sleep
import inquirer
import main
def typewriter(text):
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
    print()

classSelect = [
    inquirer.List(
        "class",
        message="who am i?",
        choices=["Dwarf", "Giant", "Human"],
    ),
]

mission = [
    inquirer.List(
        "mission",
        message="where are you going?",
        choices=["In the forrest to slay the beast", "Up over the hills to save the princess", "Gazing at the starlight for eternity"],
    ),
]

fight = [
    inquirer.List(
        "fight",
        message="would you like to fight for the hanour of choosing your own name?",
        choices=["Yes", "No"],
    ),
]


typewriter("U wake up, watching the night sky float above u")
typewriter("The circumstances makes u think of existencial questions...")

player = main.Character(inquirer.prompt(classSelect)["class"])

typewriter("as you ponder on the mysteries of life, someone interupts you")
typewriter("Soldier: Hey you! What are you doing out here in these dangerous lands?")

mission = inquirer.prompt(mission)["mission"]

if(mission!="In the forrest to slay the beast"):
    typewriter("I wouldn't advise soing that, you know what...")
    typewriter("I will personally take the creative freedom to choose for you")

typewriter("Soldier: Ahhh, so you are going in the forrest to slay the beast, good luck my dear friend, but be careful of the branches that may fall on your head. I've heard it from Vemund, a grave soldier that fell in battle long ago")

print("\n")
print("*imagine pokemon music playing in the background*")
typewriter("*A wild Giant appears!!!")
print("\n")

enemy = main.Character("Giant")


while enemy.health > 0 and player.health > 0:
    print("The enemy attacks:")
    guess = int(input("Guess his number between 0 and 100 to dodge: \n"))
    attack = enemy.attack(player,guess)
    if(attack > 0):
        typewriter(f"The enemy hit you for {attack} damage")
        typewriter(f"You now have {player.health} health left")
    else: 
        typewriter("Master ninja, you dodged the attack")
    if player.isdead():
        print("\n")
        typewriter("All great travels must end somehwere... this is the end for yours")
        break
    attack = player.attack(enemy)
    print("\n")
    print("You strike back:")
    if(attack > 0):
        typewriter(f"You hit the enemy for {attack} damage")
        typewriter(f"The enemy now has {enemy.health} health left")
    else: 
        typewriter("Too slow! That attack didn't hit at all!")
    if(enemy.isdead()):
        print("\n")
        typewriter("With a sharp blow from your weapon, th eenemy is slain before you.")
    print("\n")


typewriter(f"Strager: that was great battle {player.name}")
answer = inquirer.prompt(fight)["fight"]

if(answer == "Yes"):
    typewriter(f"You are now fighting for the right to choose your own name!!")
    typewriter(f"While going up against the evil name calling man, you notice something on the ground")
    typewriter(f"Woooow (insert emotion), is that the super op, health and attack boosting swooord!")
    typewriter(f"You pick it up, and notices that your health and attack power improve")
    player.health += 250
    player.strength += 25
    enemy = main.Character("Human")

    while enemy.health > 0 and player.health > 0:
        print("The enemy attacks:")
        guess = int(input("Guess his number between 0 and 100 to dodge: \n"))
        attack = enemy.attack(player,guess)
        if(attack > 0):
            typewriter(f"The enemy hit you for {attack} damage")
            typewriter(f"You now have {player.health} health left")
        else: 
            typewriter("Master ninja, you dodged the attack")
        if player.isdead():
            print("\n")
            typewriter("All great travels must end somehwere... this is the end for yours")
            break
        attack = player.attack(enemy)
        print("\n")
        print("You strike back:")
        if(attack > 0):
            typewriter(f"You hit the enemy for {attack} damage")
            typewriter(f"The enemy now has {enemy.health} health left")
        else: 
            typewriter("Too slow! That attack didn't hit at all!")
        if(enemy.isdead()):
            print("\n")
            typewriter("With a sharp blow from your weapon, the enemy is slain before you.")
            typewriter("You may now choose your name...")
            typewriter("In the next edition of this game given that I add that feature")
        print("\n")
else: 
      typewriter(f"Wooow, you're suuch a coward {player.name}") 
