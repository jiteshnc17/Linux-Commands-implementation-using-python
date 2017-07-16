
import os
import sys
c=[]

if(len(sys.argv)==2):
	loc=sys.argv[1]
	c= os.listdir(loc)
	print c

if(len(sys.argv)==1):
	loc=os.getcwd()
	c=os.listdir(loc)
	print '  '.join(c)
#	for x in c:
#		print x
