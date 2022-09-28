from random import randint

class Character():
    hp = {"Dwarf": 100, "Human":500, "Giant": 2000} # any range
    ag = {"Dwarf": 80, "Human":40, "Giant": 10} # [0,100)
    df = {"Dwarf": 70, "Human":30, "Giant": 20} # [0,100)
    sk = {"Dwarf": 70, "Human":60, "Giant": 10} # [0,100)
    sr = {"Dwarf": 30, "Human":60, "Giant": 60} # any range
    lk = {"Dwarf": 80, "Human":30, "Giant": 5} # [0,100)

    def __init__(s,species:str,):
        s.health = Character.hp[species] 
        s.agility = Character.ag[species]  # lower chance of getting hit
        s.defense = Character.df[species]  # getting less critical hit
        s.skill = Character.sk[species]  # higher chance of giving hit
        s.strength = Character.sr[species]  # giving more crital hit
        s.luck = Character.lk[species]  # multiplier

    def dodge(s,enemyskill):
        return randint(0,100)+randint(0,enemyskill)<=s.agility

    def defend(s,dmg):
        s.health -= round(dmg*(1-s.defense/100))
        return round(dmg*(1-s.defense/100))

    def isdead(s):
        return s.health <= 0

    def attack(s,enemy):
        if(enemy.dodge(s.luck)):
            return 0
        else:
            return enemy.defend(s.strength+s.strength*randint(0,s.luck)/10)
