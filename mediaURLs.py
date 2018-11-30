##2018 Julie Park
import sys

def getmediaURLs(initTweet):
	initMedia = []

	for i in initTweet:
		media = i.entities.get('media',[])
		if len(media) != 0:
			url_media = media[0]['media_url']
			file_type = url_media.split('.')[-1]

			if file_type == 'jpg':
				initMedia.append(media[0]['media_url'])

	if len(initMedia) == 0:
		print("NO Images found.\n")

	#print(initMedia)

	print("getmediaURLs DONEEEEEEE")

	return initMedia
