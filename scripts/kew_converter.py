#TODO main script that will be run by the user

import sys

if __name__ == "__main__":
	arguments = sys.argv

	if (len(arguments) = 0):
		print ("usage: kew-converter <KEW_url>"
	
	else if (len(arguments) = 1):
		kewPath = arguments[0]

		gets_swf.fetch_all(kewPath, conf.get_prop("slide_dump_dir"))
		gets_swf.extract_audio_all(conf.get_prop("slide_dump_dir"))
