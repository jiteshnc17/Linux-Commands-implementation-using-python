import sys
import fileinput

if(len(sys.argv)==2):
	fname=sys.argv[1]
	try:
		with open(fname, 'r') as file:
			data=file.read()
		print data
	except OSError, e:
		print e
else :
	print "Enter proper argument"
