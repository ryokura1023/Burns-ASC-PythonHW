#usr/bin/python

from sys import argv

script,filename,name,age,birthmonth  = argv


print "If you are okay to continue, please press Enter key."
print "If you want to quit, please press Ctrl+C"
raw_input("> ")

print "Open the file..."
file = open(filename, 'w')
print "Refreshing the text file....."
file.truncate()

print "Now, let's add some information of you"

print "What's your name?"
#name = raw_input("> ")
file.write(name)
file.write("\n")
print "How old are you?"
#age = raw_input("> ")
file.write(age)
file.write("\n")
print "When is your birthmonth?"
#birthmonth = raw_input("> ")
file.write(birthmonth)
file.write("\n")

file.close()

print "Youre name is %r, your age is %r, and your birthmonth is %r" % (name,age,birthmonth)


