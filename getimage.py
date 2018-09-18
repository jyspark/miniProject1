import os
import sys
import wget
import shutil

def getimage(mediaList):
		
	PATH = '.'
	NewPath = PATH + '/Images'
	
	##Check/Create Folder named "Images"	
	if os.path.exists(NewPath):
		print("Creating a new folder")
		shutil.rmtree(NewPath)
		os.mkdir(NewPath)
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')
	elif os.path.exists(NewPath) == False:
		print("The folder's created")
		os.mkdir(NewPath)
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')
	elif OSError:
		print("Disk Full/File NOT Found")

	os.system('python FFmpeg.py')
	


