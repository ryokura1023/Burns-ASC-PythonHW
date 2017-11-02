#!usr/bin/python

import random

class Player():
	def __init__(self):
		self.name = ""

class Status(Player):
	def __init__(self):
		super().__init__()
		self.HP = ""
		self.MP = ""

class Skill(Player):
	def __init__(self):
		super().__init__()
		self.skill = []
		self.damage = []
		self.energy = []


def  Select():

	global P_name,P_HP,P_MP
	global P_skill,P_damage,P_energy

	print "Here is the list of player, please choose one."
	print "1.Gon"
	print "2.Killua"
	print "3.Kurapika"
	print "4.Leorio"

	num = raw_input("> ")

	if num == "Gon":
		Gon = Player()
		Gon.name = "Gon"
		P_name = Gon.name
		Gon.HP = 800
		P_HP = Gon.HP
		Gon.MP = 20
		P_MP = Gon.MP
		Gon.skill = ["Fishing reel", "Rock Paper Scissors", "Transformation"]
		P_skill = Gon.skill
		Gon.damage = [random.randint(10,50), random.randint(100,150), random.randint(400,500)]
		P_damage = Gon.damage
		Gon.energy = [0, 5, 20]
		P_energy = Gon.energy

        elif num == "Killua":
                Killua = Player()
                Killua.name = "Killua"
                P_name = Killua.name
		Killua.HP = 700
                P_HP = Killua.HP
                Killua.MP = 30
                P_MP = Killua.MP
                Killua.skill = ["Yo-yo", "Using electrical aura", "Whirlwind"]
                P_skill = Killua.skill
                Killua.damage = [random.randint(50,100), random.randint(150,200), random.randint(200,300)]
                P_damage = Killua.damage
                Killua.energy = [0, 5, 15]
                P_energy = Killua.energy

        elif num == "Kurapika":
                Kurapika = Player()
                Kurapika.name = "Kurapika"
                P_name = Kurapika.name
                Kurapika.HP = 850
                P_HP = Kurapika.HP
                Kurapika.MP = 30
                P_MP = Kurapika.MP
                Kurapika.skill = ["Sorwd", "Chain jail", "Emperor time"]
                P_skill = Kurapika.skill
                Kurapika.damage = [random.randint(50,100), random.randint(100,200), random.randint(250,300)]
                P_damage = Kurapika.damage
                Kurapika.energy = [0, 5, 20]
                P_energy = Kurapika.energy

	elif num == "Leorio":
                Leorio = Player()
                Leorio.name = "Leorio"
                P_name = Leorio.name
                Leorio.HP = 900
                P_HP = Leorio.HP
                Leorio.MP = 20
                P_MP = Leorio.MP
                Leorio.skill = ["Injection", "Using aura", "Remote Punch"]
		P_skill = Leorio.skill
		Leorio.damage = [random.randint(50,70),random.randint(100,120),random.randint(200,220)]
		P_damage = Leorio.damage
		Leorio.energy = [0,3,7]
		P_energy = Leorio.energy

	else:
		print "There is no charactor, please try again!"
		Select()

	print "-" * 10
	print "You choose %s, he has HP:%d and MP:%d" % (P_name,P_HP,P_MP)
	print "%s has skills below" % P_name
	print "1. %s (using %d MP)" % (P_skill[0],P_energy[0])
	print "2. %s (using %d MP)" % (P_skill[1],P_energy[1])
	print "3. %s (using %d MP)" % (P_skill[2],P_energy[2])
	print "-" * 10
	val = raw_input("If you want to choose other charactor, please press q botton : ")
	if val == "q" or val == "Q":
		print "-" * 10
		Select()
	else:
		print "-" * 10
		print "Ok, you choose %s as player!!" % P_name





