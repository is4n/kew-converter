#TODO main script that will be run by the user

import sys
import os
import conf
import gets_swf

if __name__ == "__main__":
	arguments = sys.argv[1:]
	
	# print usage if no input
	if (len(arguments) < 2):
		print ("usage: kew-converter <KEW_url> <output> [-z]")
		sys.exit(0)
	
	# checks validity of arguments
	
	# check that output path exists
	if (not os.path.exists(arguments[1])): 
		print ("Could not find path " + arguments[1])
		sys.exit(0)

	# set output_dir
	conf.set_prop("output_dir", arguments[1])

	kewUrl = arguments[0]
	
	print("STEP 1: Acquiring KEW slides from server")
	gets_swf.fetch_all(kewUrl, conf.get_prop("output_dir"))
	print("STEP 2: Fetching linked text")
	gets_swf.get_linked_text_all(conf.get_prop("output_dir"))
	print("STEP 3: Extracting audio")
	gets_swf.extract_audio_all(conf.get_prop("output_dir"))
	print("STEP 4: Extracting images")
	gets_swf.extract_images_all(conf.get_prop("output_dir"))

