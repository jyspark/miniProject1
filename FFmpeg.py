##2018 Julie Park
import os 

##Remove the mp4 file if it exits 
file = './video.mp4'
if os.path.exists(file):
	os.remove('movie.mp4')

print("Creating a video...")

try:
	##Convert the image to video with the framerate of 1/2	
	os.popen('ffmpeg -start_number 0 -framerate 1/2 -i /media/sf_Assginment1/EC601/miniProject1/Images/image%d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4')
	print('\n Analysing the video')
except Exception as err:
	print("Error" + err)
	exit()


##Run the analysis
os.system('python description.py')

	