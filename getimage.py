##2018 Julie Park
import os
import sys
import wget
import shutil
import subprocess

def getimage(mediaList):

	#Path to the Images Folder
	PATH = '.'
	NewPath = PATH + '/Images'

	imgNum = 0

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

			imgNum += 1

	elif OSError:
		print("Disk Full/File NOT Found")

	print(imgNum)
	print("\ngetimage DONEEEEEE")

	file = './movie.mp4'
	if os.path.exists(file):
		os.remove('movie.mp4')

	print("Creating a video...")

	try:
		##Convert the image to video with the framerate of 1/2
		#os.popen('ffmpeg -start_number 0 -framerate 1/2 -i /media/sf_Assginment1/EC601/miniProject1/Images/image%d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4')
		#subprocess.call('ffmpeg -loglevel panic -framerate 1/5 -f image2 -i C:/Users/Julie Park/Desktop/BU/F18_EC602/Week1/Assginment1/EC601/miniProject1/Images/image%d.jpg -vf scale=640:360 -r 30 movie.mp4')
		os.popen('ffmpeg -start_number 0 -framerate 1/2 -i C:/Users/Julie Park/Desktop/BU/F18_EC602/Week1/Assginment1/EC601/miniProject1/Images/image%d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4')
		print('\n Analyzing the video')
	except Exception as err:
		print("Error" + err)
		exit()

	print("FFmpeg.py DONEEEEEE1")

	return imgNum
