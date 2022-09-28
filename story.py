import sys
from time import sleep
import inquirer

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

typewriter






answers = inquirer.prompt(questions)

print(answers)

typewriter("U wake up, the abando")
