import sys
from time import sleep
import inquirer
import main
def typewriter(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
    print()

classSelect = [
    inquirer.List(
        "class",
        message="which class is your character?",
        choices=["Dwarf", "Giant", "Human"],
    ),
]

answers = inquirer.prompt(classSelect)

selectedClass = answers["class"]

player = main.Character(selectedClass)

print(player.luck)




typewriter("U wake up, the abando")