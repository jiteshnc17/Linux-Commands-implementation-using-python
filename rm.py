import os 
import sys
import commands
import shutil

if(len(sys.argv)==2):
	name=sys.argv[1]
	
	if (name[0]!="/"):
		print "in current dir"
		pat=os.getcwd()
		print "current dir is "+pat
		name=pat+"/"+name
		print "Name is "+name	
#		os.remove(name)
		shutil.rmtree(name)
		print "removed successfully"
	
	elif (name[0]=="/"):
		print "absolute path"
	
		shutil.rmtree(name)
		os.listdir()
		print "removed successfully"
else:
	print error
