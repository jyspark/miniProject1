import sys

def getmediaURLs(initTweet): 
	from getimage import getimage   
    
    ##initialize a list to hold all mediaURLs
	initMedia = []

	##Get media_urls from initTweet
	for i in initTweet:
		media = i.entities.get('media',[])
		if len(media) != 0:
			url_media = media[0]['media_url']
			file_type = url_media.split('.')[-1]
			if file_type == 'jpg':
				initMedia.append(media[0]['media_url'])

	#print(initMedia) 
	 
	getimage(initMedia)

    
  