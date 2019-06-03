# fetches the slideX.swf files and removes the desired contents into a specified folder

import subprocess
import os
import io
import time
import conf
import converts_pdf

def fetch_all(url, out_dir):
	#TODO: add non-linux OS support
	# runs script that gets "index of" page
	os.system("chmod +x ./get_lsn_index.sh")
	os.system("./get_lsn_index.sh \"" + out_dir + "\" " + url) 
	
	# gets URLs to the page*.swf files and downloads them
	lsnIndex = io.open(out_dir + "/.cache/lsn_index.html")
	htmlLines = lsnIndex.read().split("\n")
	swfFilesCount = 0
	swfFiles = []
	
	# iterates through every line in index page
	for line in htmlLines:
		# if this is an .swf slide, download it
		if (line.find("page") != -1): 
			print("fetching page " + str(swfFilesCount + 1)) 

			if os.path.exists(out_dir + "/page" + str(swfFilesCount + 1) + ".swf"):
				print ("file aready exists -- skipping this page")
			else:
				os.system("wget " + url + "/page" + str(swfFilesCount + 1) + ".swf" + \
					" -O \"" + out_dir + "/page" + str(swfFilesCount + 1) + ".swf\"")
				time.sleep(1.5) # be nice to the servers

			# create folders for dumping SWF contents into
			os.system("mkdir " + out_dir + "/page" + str(swfFilesCount + 1) + "/") 
			swfFilesCount = swfFilesCount + 1

		# if this is the PDF notes for the lesson download them too
		if (line.find("pdf") != -1):
			print("fetching PDF text")

			# Identify lesson number
			#TODO: This solution is hacky - if the lesson is hosted anywhere else
			# without a URL format exactly the way it is now, this will break
			lesson = ""
			if (url[len(url) - 1] == "/"): lesson = url[url.find("lesson") + 6:-1]
			else: lesson = url[url.find("lesson") + 6]

			os.system("wget \"" + url + "/Lesson " + lesson + " Notes.pdf\"" + \
				" -O \"" + out_dir + "/text.pdf\"")


	print ("downloaded " + str(swfFilesCount) + " files")

	# cleans up
	os.system("rm -r " + out_dir + "/.cache")

def get_swf_list(swf_dir):
	swfList = []

	# iterates through swf_dir and gets every .swf file
	for swf in os.listdir(swf_dir):
		if (swf.find(".swf") is not -1): swfList.append(swf)

	return swfList

def extract_audio(swf_path, out_path):
	os.system(conf.get_prop("swftools_path") + "swfextract -m -o " + out_path + " " + swf_path)

def extract_audio_all(swf_dir):
	# gets list of SWFs
	swfList = get_swf_list(swf_dir)
	swfIndex = 1

	for swf in swfList:
		# extract_audio 
		print ("input file: " + swf_dir + swf)
		print ("output file: " + swf_dir + swf[:-4] + "/audio.mp3")
		
		extract_audio(swf_dir + swf, swf_dir + swf[:-4] + "/audio.mp3")
		swfIndex = swfIndex + 1

def extract_images(swf_path, out_dir):
	# gets ids for images in SWF
	imageIds = get_image_ids(swf_path)
	
	# use swfextract to extract images based off id
	for imageId in imageIds:
		os.system(conf.get_prop("swftools_path") + "swfextract -j " + str(imageId) +\
			" -o " + out_dir + "/" + str(imageId) + ".jpg " + swf_path)

def extract_images_all(swf_dir): 
	swfList = get_swf_list(swf_dir)
	
	for swf in swfList:
		extract_images(swf_dir + swf, swf_dir + swf[:-4])

def get_image_ids(swf_path):
	# gets the output of swftools
	swfextractOut = str(subprocess.check_output([conf.get_prop("swftools_path") +\
		"swfextract", swf_path]))

	# finds the string with the JPEG ids
	beginpoint = swfextractOut.find("JPEG")
	
	if (beginpoint is not -1):
		ids = []
		# finds start/end of the juicy bits 
		startpoint = swfextractOut.find(")", beginpoint) + 2
		endpoint = swfextractOut.find('\\n', beginpoint)
		idsStr = swfextractOut[startpoint:endpoint]

		# prints debug info
		print("starting point: " + str(startpoint))
		print("ending point: " + str(endpoint))
		print(swfextractOut[startpoint:endpoint])

		if (idsStr.find(",") == -1): return [int(idsStr)]
		else:
			for idStr in idsStr.split(","):
				ids.append(int(idStr))
			return ids

	return []
		
def get_linked_text(page_num, text_path):
	# reads notes file
	ltRead = open(text_path, 'r')

	# Cleans up PDF text - The space characters in replace(" ", " ") are actually different!
	lessonText = ltRead.read().replace("", "-").replace(" ", " ")
	ltRead.close()
	
	# find the start/end points of the wanted text
	beginpoint = lessonText.find("Page " + str(page_num).strip())
	startpoint = lessonText.find(":", beginpoint) + 1
	endpoint = lessonText.find("Page " + str(int(page_num) + 1), startpoint)
	
	# prints debug info
	print("page number: " + str(page_num))
	print("find tex1: " + "Page " + str(page_num).strip())
	print("begin point: " + str(beginpoint))
	print("starting point: " + str(startpoint))
	print("ending point: " + str(endpoint))
	
	return lessonText[startpoint:endpoint].strip()

def get_linked_text_all(swf_dir):
	# converts PDF to plaintext if it hasn't been done already
	if (not os.path.exists(swf_dir + "text.txt")):
		convert_pdf(swf_dir + "text.pdf", swf_dir + "text.txt")

	swfList = get_swf_list(swf_dir)

	for swf in swfList:
		textWriter = open(swf_dir + swf[:-4] + "/text.txt", 'w')
		textWriter.write(get_linked_text(int(swf[4:-4]), swf_dir + "text.txt"))
		textWriter.close()

def convert_pdf(in_path, out_path):
	converts_pdf.pdf_to_text(in_path, out_path)

def clean_up_all(swf_dir):
	os.system("rm " + swf_dir + "*.swf " + swf_dir + "*.pdf")

