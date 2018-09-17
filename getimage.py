import os
import sys
import wget

def getimage(mediaList):
	PATH = '.'
	NewPath = PATH + '/Images'
	
	##Check/Create Folder named "Images"	
	if os.path.exists(NewPath):
		print("The folder is existed")
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')

	elif os.path.exists(NewPath) == 0:
		print("The folder's created")
		os.mkdir(NewPath)
		for i in range(len(mediaList)):
			wget.download(mediaList[i], NewPath+'/'+'image'+str(i)+'.jpg')
	elif OSError:
		print("Disk Full/File NOT Found")


	

