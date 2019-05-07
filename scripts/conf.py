# Need some way to get configuration data around

import io
import os

def get_prop(prop):
	try: 
		confFile = open("../conf/" + prop, 'r')
		val = confFile.read().replace("\n", "")
		confFile.close()
		return(val)
	except:
		return(0)
		
def set_prop(prop, val):
	confFile = build_config_file(prop)
	confFile.write(val + "\n")
	confFile.close()

def check_prop_exist(prop):
	try:
		if (os.file.exists("../conf/" + prop)):
			return True
		else: return False
	except:
		return False

def build_config_file(name):
	if (not os.path.exists("../conf")): os.system("mkdir ../conf")
	os.system("touch ../conf/" + name)
	return open("../conf/" + name, 'w')

