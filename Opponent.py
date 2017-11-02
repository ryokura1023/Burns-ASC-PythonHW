#!usr/bin/python

import random

class Opponent():
        def __init__(self):
                self.name = ""

class Status(Opponent):
        def __init__(self):
                super().__init__()
                self.HP = ""
                self.MP = ""

class Skill(Opponent):
        def __init__(self):
                super().__init__()
                self.skill = []
                self.damage = []
                self.energy = []


def  Select():

        global O_name,O_HP,O_MP
        global O_skill,O_damage,O_energy

        print "Here is the list of player, please choose one."
        print "1.Hisoka"
        print "2.Chrollo"
        print "3.Illumi"
        print "4.Meruem"

        num = raw_input("> ")

        if num == "Hisoka":
                Hisoka = Opponent()
                Hisoka.name = "Hisoka"
                O_name = Hisoka.name
                Hisoka.HP = 800
                O_HP = Hisoka.HP
                Hisoka.MP = 20
                O_MP = Hisoka.MP
                Hisoka.skill = ["Trump", "Texture Surprise", "Bungee Gum"]
                O_skill = Hisoka.skill
                Hisoka.damage = [random.randint(10,50), random.randint(100,150), random.randint(400,500)]
                O_damage = Hisoka.damage
                Hisoka.energy = [0, 5, 20]
                O_energy = Hisoka.energy

        elif num == "Chrollo":
                Chrollo = Opponent()
                Chrollo.name = "Chrollo"
                O_name = Chrollo.name
                Chrollo.HP = 700
                O_HP = Chrollo.HP
                Chrollo.MP = 30
                O_MP = Chrollo.MP
                Chrollo.skill = ["Ben's knife", "Bandit's secret", "Paired Destruction"]
                O_skill = Chrollo.skill
                Chrollo.damage = [random.randint(50,100), random.randint(150,200), random.randint(200,300)]
                O_damage = Chrollo.damage
                Chrollo.energy = [0, 5, 15]
                O_energy = Chrollo.energy

        elif num == "Illumi":
                Illumi = Opponent()
                Illumi.name = "Illumi"
                O_name = Illumi.name
                Illumi.HP = 850
                O_HP = Illumi.HP
                Illumi.MP = 30
                O_MP = Illumi.MP
                Illumi.skill = ["Body Alternation", "Corpse Control", "Using Needlemen"]
                O_skill = Illumi.skill
                Illumi.damage = [random.randint(50,100), random.randint(100,200), random.randint(250,300)]
                O_damage = Illumi.damage
                Illumi.energy = [0, 5, 20]
		O_energy = Illumi.energy

        elif num == "Meruem":
                Meruem = Opponent()
                Meruem.name = "Meruem"
                O_name = Meruem.name
                Meruem.HP = 900
                O_HP = Meruem.HP
                Meruem.MP = 20
                O_MP = Meruem.MP
                Meruem.skill = ["Tail attack", "Eat", "Rage Blast"]
                O_skill = Meruem.skill
                Meruem.damage = [random.randint(50,70),random.randint(100,120),random.randint(200,220)]
                O_damage = Meruem.damage
                Meruem.energy = [0,3,7]
                O_energy = Meruem.energy

        else:
                print "There is no charactor, please try again!"
                Select()

        print "-" * 10
        print "You choose %s, he has HP:%d and MP:%d" % (O_name,O_HP,O_MP)
        print "%s has skills below" % O_name
        print "1. %s (using %d MP)" % (O_skill[0],O_energy[0])
        print "2. %s (using %d MP)" % (O_skill[1],O_energy[1])
        print "3. %s (using %d MP)" % (O_skill[2],O_energy[2])
        print "-" * 10
        val = raw_input("If you want to choose other charactor, please press q botton : ")
        if val == "q" or val == "Q":
                print "-" * 10
                Select()
        else:
                print "-" * 10
                print "Ok, you choose %s as opponent!!" % O_name

