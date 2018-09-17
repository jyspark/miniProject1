import os 

os.popen('ffmpeg -start_number 0 -framerate 1/2 -i /media/sf_Assginment1/EC601/miniProject1/Images/image%d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -r 30 -pix_fmt yuv420p video.mp4')
