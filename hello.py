import sys

i = 0

for arg in sys.argv: 
	if i > 0:
		print ("Hello, " + arg + "!")
	i += 1

print("Hello, World!")
