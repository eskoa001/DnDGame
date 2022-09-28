from random import randint

class Character():
    hp = {'d': 100, 'h':500, 'g': 2000} # any range
    ag = {'d': 80, 'h':40, 'g': 10} # [0,100)
    df = {'d': 70, 'h':30, 'g': 20} # [0,100)
    sk = {'d': 70, 'h':60, 'g': 10} # [0,100)
    sr = {'d': 30, 'h':60, 'g': 60} # any range
    lk = {'d': 80, 'h':30, 'g': 5} # [0,100)

    def __init__(s,species:chr,):
        s.health = Character.hp[species] 
        s.agility = Character.ag[species]  # lower chance of getting hit
        s.defense = Character.df[species]  # getting less critical hit
        s.skill = Character.sk[species]  # higher chance of giving hit
        s.strength = Character.sr[species]  # giving more crital hit
        s.luck = Character.lk[species]  # multiplier

    def dodge(s,enemyskill):
        return randint(0,100)+randint(0,enemyskill)<=s.agility

    def defend(s,dmg):
        s.health -= dmg*(1-s.defense/100)
        return dmg*(1-s.defense/100)

    def isdead(s):
        return s.health <= 0

    def attack(s,enemy):
        if(enemy.dodge(s.luck)):
            return 0
        else:
            return enemy.defend(s.strength+s.strength*randint(0,s.luck)/10)

a = Character("g")
b = Character("d")
for i in range(20):
    print(b.attack(a))
    if(a.isdead()):
        print("ohno")
        break
    print(a.attack(b))
    if(b.isdead()):
        print("OHNO")
        break

    
