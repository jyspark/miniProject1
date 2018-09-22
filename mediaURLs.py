##2018 Julie Park
import sys

def getmediaURLs(initTweet): 
	from getimage import getimage   
	from getandread import gettweets
    
    ##initialize a list to hold all mediaURLs
	initMedia = []

	##Get media_urls from initTweet
	for i in initTweet:
		media = i.entities.get('media',[])
		if len(media) != 0:
			url_media = media[0]['media_url']
			file_type = url_media.split('.')[-1]
			##Change to other extension if needed
			if file_type == 'jpg':		
				initMedia.append(media[0]['media_url'])

	##No images to download
	if len(initMedia) == 0:
		print("NO Images found.\n")
		gettweets(input("Enter Username: @"))
		
	#print(initMedia) 
	
	##pass the list of image URLs 
	getimage(initMedia)
	

    
  