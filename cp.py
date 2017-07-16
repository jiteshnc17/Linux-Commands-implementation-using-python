import fileinput
import sys


if (len(sys.argv)==3):
	f1=sys.argv[1]
	f2=sys.argv[2]
	
	with open(f1,'r') as file:
		readdata=file.read()

	with open(f2,'w') as file:
		file.write(readdata)
else:
	print "Enter the correct no of arguments"
