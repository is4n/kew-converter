# Debug/test script for KEW converter

import sys
import conf
import gets_swf

if __name__ == "__main__":
	if (len(sys.argv) == 1):
		print("0 = gets_swf.fetch_all")
		print("1 = gets_swf.extract_audio")
		print("2 = gets_swf.extract_audio_all")
		print("3 = gets_swf.convert_pdf")
		print("4 = conf.set_prop")
		print("5 = conf.get_prop")
		print("6 = conf.check_prop_exists")
		print("7 = gets_swf.gets_image_IDs")

	else:
		if (sys.argv[1] == "0"): gets_swf.fetch_all(sys.argv[2], sys.argv[3])
		if (sys.argv[1] == "1"): gets_swf.extract_audio(sys.argv[2], sys.argv[3])
		if (sys.argv[1] == "2"): gets_swf.extract_audio_all(sys.argv[2])
		if (sys.argv[1] == "3"): gets_swf.convert_pdf(sys.argv[2], sys.argv[3])	
		if (sys.argv[1] == "4"): conf.set_prop(sys.argv[2], sys.argv[3])
		if (sys.argv[1] == "5"): print(conf.get_prop(sys.argv[2]))
		if (sys.argv[1] == "6"): print(conf.check_prop_exist(sys.argv[2]))
		if (sys.argv[1] == "7"): print(gets_swf.get_image_ids(sys.argv[2]))

