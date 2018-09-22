##2018 Julie Park
import os
import sys
import wget
import shutil

def getimage(mediaList):
	
	#Path to the Images Folder	
	PATH = '.'
	NewPath = PATH + '/Images'
	
	##Check/Create Folder named "Images"	
	if os.path.exists(NewPath):
		##If the folder already exists, remove,create and downloads the images in .jpg
		print("Creating a new folder")
		shutil.rmtree(NewPath)
		os.mkdir(NewPath)
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')
	elif os.path.exists(NewPath) == False:
		#Creates the folder and downloads the images in .jpg
		print("The folder's created")
		os.mkdir(NewPath)
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')
	elif OSError:
		#Displays error if there is
		print("Disk Full/File NOT Found")

	#runs the next file which converts the images to a video
	os.system('python FFmpeg.py')
	


