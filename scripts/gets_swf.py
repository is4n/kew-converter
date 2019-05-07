# his file will have methods to fetch the slideX.swf files and (possibly)
# remove the desired contents into a specified folder

import os
import io
import time
import conf
import converts_pdf

def fetch_all(url, out_dir):
	#TODO: add non-linux OS support
	# runs script that gets "index of" pag
	os.system("chmod +x ./get_lsn_index.sh")
	os.system("./get_lsn_index.sh \"" + out_dir + "\" " + url) 
	
	# gets URLs to the page*.swf files and downloads them
	lsnIndex = io.open(out_dir + "/.cache/lsn_index.html")
	htmlLines = lsnIndex.read().split("\n")
	swfFilesCount = 0
	swfFiles = []
	for line in htmlLines:
		if (line.find("page") != -1): 
			print("fetching page " + str(swfFilesCount + 1)) 
			if os.file.exists(out_dir + "/page" + str(swfFilesCount + 1) + ".swf"):
				print ("file aready exists -- skipping this page")
			else: os.system("wget " + url + "/page" + str(swfFilesCount + 1) + ".swf" + \
				" -O \"" + out_dir + "/page" + str(swfFilesCount + 1) + ".swf\"")
			# create folders for dumping SWF contents into
			os.system("mkdir " + out_dir + "/page" + str(swfFilesCount + 1) + "/") 
			time.sleep(1.5) # be nice to the servers
			swfFilesCount = swfFilesCount + 1
	print ("downloaded " + str(swfFilesCount) + " files")
	
	# cleans up
	os.system("rm -r " + out_dir + "/.cache")

def extract_audio(swf_path, out_path):
	os.system(conf.get_prop("swftools_path") + "swfextract -m -o " + out_path + " " + swf_path)

def extract_audio_all(swf_dir):
	swfList = []
	for swf in os.listdir(swf_dir):
		if (swf.find(".swf") is not -1): swfList.add(swf)
	
	swfIndex = 1
	for swf in swflist:
		# extract_audio 
		extract_audio(swf, swf[:-4] + "/audio.mp3")
		swfIndex = swfIndex + 1

def get_linked_text(swf_name):
	# if (os.file.exists(conf.get_prop("swftools_path") + "
	pass

def convert_pdf(in_path, out_path):
	pdf_to_text(in_path, out_path)

#TODO: get_images, etc...

