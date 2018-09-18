import os 


file = './video.mp4'
if os.path.exists(file):
	os.remove('movie.mp4')
	
os.popen('ffmpeg -start_number 0 -framerate 1/2 -i /media/sf_Assginment1/EC601/miniProject1/Images/image%d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4')
print('\n Analysing the video')

os.system('python description.py')

	