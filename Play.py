#!usr/bin/python

import Player
import Opponent
import random
from sys import exit


Player.Select()
print "-" * 10
print "Now, it's time to choose opponent."
Opponent.Select()

print "This time is %s VS %s  " %(Player.P_name,Opponent.O_name)

HP1 = Player.P_HP
MP1 = Player.P_MP
HP2 = Opponent.O_HP
MP2 = Opponent.O_MP

def start():
	global HP1
	global HP2
	print "-" * 15
	print "%s has HP:%d, and %s has HP:%d " %(Player.P_name,HP1,Opponent.O_name,HP2)
	print "-" * 15
	while True:
		if HP1 >= 0 and HP2 >= 0:
			i = random.randint(1,2)
			if i == 1:
				print "It's %s's turn!" % Player.P_name
				P_turn()
			else:
				print "It's %s's turn!" % Opponent.O_name
				O_turn()

		elif HP1 <= 0:
			print "%s is beaten by %s....." % (Player.P_name,Opponent.O_name)
			print "You loose....."
			exit(0)

		elif HP2 <= 0:
			print "%s beat %s" % (Player.P_name,Opponent.O_name)
			print "You're win!!"
			exit(0)


def P_turn():
	global HP1
	print "-" * 10
	print "What %s will do ?" % Player.P_name
	print "1. Attack"
	print "2. Recover"
	print "3. Check status"

	next = int(raw_input("> "))

	if next == 1:
		attack()
	elif next == 2:
		recover()
	elif next == 3:
		print "The current HP of %s is %d, and MP : %d." % (Player.P_name,HP1,MP1)
		P_turn()
	else:
		P_turn()

def attack():
	global HP2
	global MP1
	print "1. %s" % Player.P_skill[0]
	print "2. %s" % Player.P_skill[1]
	print "3. %s" % Player.P_skill[2]
	print "4. Go back to previous choice"

	next = int(raw_input("> "))

	if next == 1:
		dm = Player.P_damage[0]
		print "%s damaged %d to %s" %(Player.P_name,dm,Opponent.O_name)
		HP2 = HP2 - dm
	elif next == 2:
		if MP1 <= 0:
			print "You can't %s, use ether." % Player.P_skill[1]
			attack()
		else:
			dm = Player.P_damage[1]
                	print "%s damaged %d to %s" %(Player.P_name,dm,Opponent.O_name)
			HP2 = HP2 - dm
			MP1 = MP1 - Player.P_energy[1]
	elif next == 3:
		if MP1 <= 0:
			print "You can7t use %s, use ether." % Player.P_skill[2]
			attack()
		else:
			dm = Player.P_damage[2]
                	print "%s damaged %d to %s" %(Player.P_name,dm,Opponent.O_name)
			HP2 = HP2 - dm
			MP1 = MP1 - Player.P_energy[2]

	elif next == 4:
		return P_turn

	else:
		print "Invalid choice, please try again."
		return start()

	return start()

def recover():
	global HP1
	global MP1
	print "1. Portion"
	print "2. Ether"
	print "3. Go back to previous choice"

	next = int(raw_input("> "))

	if next == 1:
		HP1 = HP1 + 100
		print "Now, %s's HP is %d" %(Player.P_name,HP1)

	elif next == 2:
		MP1 = MP1 + 10
		print "Now, %s's MP is %d" %(Player.P_name,MP1)

	elif next == 3:
		return P_turn()

	return start()


def O_turn():
	print "-" * 15
	n = random.randint(1,3)
	global HP1

	if n == 1:
		dm = Opponent.O_damage[0]
		print "%s use %s!" %(Opponent.O_name,Opponent.O_skill[0])
		print "It damaged %d to %s!" %(dm, Player.P_name)
		HP1 = HP1 - dm

	elif n == 2:
		dm = Opponent.O_damage[1]
		print "%s use %s!" %(Opponent.O_name,Opponent.O_skill[1])
		print "It damaged %d to %s!" %(dm, Player.P_name)
		HP1 = HP1 - dm

	elif n == 3:
		dm = Opponent.O_damage[2]
		print "%s use %s!" %(Opponent.O_name,Opponent.O_skill[2])
		print "It damaged %d to %s!" %(dm, Player.P_name)
		HP1 = HP1 - dm

	return start()


start()
