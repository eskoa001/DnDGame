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


typewriter("U wake up, watching the night sky float above u")
typewriter("The circumsatances makes u think of existencial questions...")

player = main.Character(inquirer.prompt(classSelect)["class"])

typewriter("as you ponder on the mysteries of life, someone interupts you")
typewriter("Soldier: Hey you! What are you doing out here in these dangerous lands?")

mission = inquirer.prompt(mission)["mission"]

if(mission!="In the forrest to slay the beast"):
    typewriter("as we the devs, creator of this world, that means you. Didn't have enough time to create more scenarios...")
    typewriter("I will personally take the creative freedom to choose for you")

typewriter("Soldier: Ahhh, so you are going in the forrest to slay the beast, good luck my dear friend, but be careful of the branches that may fall on your head. I've heard it from Vemund, a grave soldier that fell in battle long ago")

print("\n")
print("*imagine pokeman music playing in the background*")
typewriter("*A wild Giant appears!!!")
print("\n")

enemy = main.Character("Giant")

while enemy.health > 0 and player.health > 0:
    attack = enemy.attack(player)
    print("The enemy attacks:")
    if(attack > 0):
        typewriter(f"The enemy hit you for {attack} damage")
        typewriter(f"You now have {player.health} health left")
    else: 
        typewriter("Master ninja, you dodged the attack")
    attack = player.attack(enemy)
    print("\n")
    print("You strike back:")
    if(attack > 0):
        typewriter(f"You hit the enemy for {attack} damage")
        typewriter(f"The enemy now has {enemy.health} health left")
    else: 
        typewriter("Too slow! That attack didn't hit at all!")
    print("\n")
   