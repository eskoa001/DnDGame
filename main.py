from random import randint

class Character():
    hp = {"Dwarf": 100, "Human":300, "Giant": 1000} # any range
    ag = {"Dwarf": 80, "Human":40, "Giant": 10} # [0,100)
    df = {"Dwarf": 70, "Human":30, "Giant": 20} # [0,100)
    sk = {"Dwarf": 70, "Human":60, "Giant": 10} # [0,100)
    sr = {"Dwarf": 30, "Human":60, "Giant": 60} # any range
    lk = {"Dwarf": 70, "Human":30, "Giant": 5} # [0,100)
    nm = {"Dwarf": "Bob the dwarf", "Human": "Ben Dover", "Giant": "Hugh Mongous"}

    def __init__(s,species:str,):
        s.health = Character.hp[species] 
        s.agility = Character.ag[species]  # lower chance of getting hit
        s.defense = Character.df[species]  # getting less critical hit
        s.skill = Character.sk[species]  # higher chance of giving hit
        s.strength = Character.sr[species]  # giving more crital hit
        s.luck = Character.lk[species]  # multiplier
        s.name = Character.nm[species] #birth given name

    def dodge(s,enemyskill,guess=randint(0,100)):
        return abs(randint(0,100)+randint(0,enemyskill) - guess) <= randint(0,s.agility)

    def defend(s,dmg):
        s.health -= round(dmg*(1-s.defense/100))
        s.health=max(s.health,0)
        return round(dmg*(1-s.defense/100))

    def isdead(s):
        return s.health <= 0

    def attack(s,enemy):
        if(enemy.dodge(s.luck)):
            return 0
        else:
            return enemy.defend(s.strength+s.strength*randint(0,s.luck)/10)
