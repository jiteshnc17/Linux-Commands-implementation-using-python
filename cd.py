import os
#import commands
import sys



if(len(sys.argv)==2):
	loc=sys.argv[1]

	os.chdir(loc)

	print "The present working dir is changed to "

	print os.getcwd()

else:
	#os.chdir(os.path.expanduser('~'))
	os.chdir(os.getenv("HOME"))
	print os.getcwd()
	
