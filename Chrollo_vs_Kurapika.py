#!usr/bin/python

import random
from sys import exit
from sys import argv

script, filename = argv

print "If you want to continue, please press enterkey"
print "Ohterwise, press ctrl+C"
trace = open(filename, 'w')

print "Truncating the file"
trace.truncate()



HP1 = 1000
HP2 = 1000
MP1 = 50
MP2 = 50

print "-" * 15
print "This battle is between Chrollo and Krapika in HunterXHunter"
print "Both of them has HP 1000 and MP 50, if the HP of one of"
print "them is 0, the game is over."


def start():
	print "-" * 15
	global HP1
	global HP2
	print "Kurapika's HP is %d, and Chrollo's HP is %d " % (HP1,HP2)
	print "-" * 15
	while True:
		if HP1 >= 0 and HP2 >= 0:
			i = random.randint(1,2)
			if i == 1:
				str1 =  "It's Krapika's turn!\n"
				print str1
				trace.write(str1)
				kurapika_turn()
			elif i == 2:
				str2 = "It's Chrollo's trun!\n"
				print str2
				trace.write(str2)
				chrollo_turn()
		elif HP1 <= 0:
			str1 =  "Kurapika is killed by Chrollo, the winner is Chrolllo.\n"
			print str1
			trace.write(str1)
			trace.close()
			exit(0)
		elif HP2 <= 0:
			str1 = "Chrollo is killed by Kurapika, the winner is Kurapika.\n"
			str2 =  "He also killed the lest of menbers of the Phantom Troupe!!\n"
			print str1
			print str2
			trace.write(str1)
			trace.write(str2)
			trace.close()
			exit(0)

def kurapika_turn():
	global HP1
	global MP1
	print "-" * 15
	print "What Kurapika will do ?"
	print "1. Attack Chrollo"
	print "2. Recover himself"
	print "3. Run away"
	print "4. Check his status"

	next = int(raw_input("> "))

	if next == 1:
		attack()
	elif next == 2:
		recover()
	elif next == 3:
		run_away()
	elif next == 4:
		print "the current HP of Hisoka is %d, and his MP is %d" % (HP1, MP1)
		kurapika_turn()
	else:
		print "Kurapika suiside somewhat, the winner is Chrollo."
		trace.close()
		exit(0)


def chrollo_turn():
	print "-" * 15
	n = random.randint(1,3)
	global HP1

	if n == 1:
		dm = random.randint(10,50)
		str1 =  "Chrollo use Ben's Knife\n"
		str2 = "Then he caused damege to Kurapika %d \n" % dm
		print str1
		print str2
		trace.write(str1)
		trace.write(str2)
		HP1 = HP1 - dm
	elif n == 2:
		dm = random.randint(100,150)
		str1 = "Chrollo steal Kurapika's ability\n"
		str2 = "Then he use Chain jail, it caused damege %d!\n" % dm
		print str1
		print str2
		trace.write(str1)
		trace.write(str2)
		HP1 = HP1 - dm
	elif n == 3:
		dm = random.randint(150,200)
		str1 =  "Chrollo use 'Sun and Moon', which is the strongest\n"
		str2 = "Then he caused damege to Kurapika %d\n" % dm
		print str1
		print str2
		trace.write(str1)
		trace.write(str2)
		HP1 = HP1 - dm

	trace.write("----------------\n")
	return start()


def attack():
	print "1. Punch"
	print "2. Chain jail"
	print "3. Emperor time"
	print "4. Go back to previous choice"

	next = int(raw_input("> "))
	global HP2
	global MP1
	if next == 1:
		dm = random.randint(10,50)
		HP2 = HP2 - dm
		trace.write("He punched, and Chrollo was dameged %d\n" % dm)
	elif next == 2:
		if MP1 <= 0:
			print "He can't use this ability, use ethel!"
			attack()
		else:
			dm = random.randint(50,150)
			HP2 = HP2 - dm
			trace.write("He used Chain jail, and Chrollo was dameged %d\n" % dm)
			MP1 = MP1 -10
	elif next == 3:
		if MP1 <= 0:
			print "He can't use this ability, use ethel!"
			attack()
		else:
			dm = random.randint(150,300)
			HP2 = HP2 - dm
			trace.write("He used Emperor time, and Chrollo was dameged %d\n" % dm)
			MP1 = MP1 -25

	elif next == 4:
		return kurapika_turn()
	else:
		print "Invalid choice, please try again."
		return attack()

	trace.write("------------------\n")
	return start()


def recover():
	print "1. Holy chain"
	print "2. ether"
	print "3. Go back to previous choice"

	next = int(raw_input("> "))
	global HP1
	global MP1

	if next == 1:
		HP1 = HP1 + 100
		MP1 = MP1 - 5
		print "Now, Krapika's HP is %d" % HP1
	elif next == 2:
		MP1 = MP1 + 10
		print "Now, Krapika's MP is %d" % MP1

	return start()

def run_away():
	print "Kurapika tries to run away, but the other menbers of Phantom Troupe captured him!"
	print "He was killed by them."
	exit(0)


start()

