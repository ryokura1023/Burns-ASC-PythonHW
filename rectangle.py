#usr/bin/python

from sys import exit

print "-" * 10
print "Programer : Ryota Kurazono"
print "Date : October 9, 2017"
print "Purpose : Input the width and length of rectangle,"
print "          and display Area or Perimeter of the rectangle."
print "-" * 10

print "Pleaes input the length of the Rectangle: "
length = int(raw_input("> "))
print "Please input the width of the Rectangle: "
width = int(raw_input("> "))

print "-" * 10
print "Now, let's calcurate Area or Perimeter of the Rectangle!"
print "1. It shows Area "
print "2. It shows Perimeter"


while True:

	choice = int(raw_input("> "))

	if choice == 1:
		Area = length * width
		print "The Area of the rectangle is %d" % Area
		exit(0)

	elif choice == 2:
		Perimeter = (length * 2) + (width * 2)
		print "The Perimeter of the rectangle if %d" % Perimeter
		exit(0)

	else:
		print "There is no choice, try again."


