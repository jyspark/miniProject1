##2018 Julie Park
from google.cloud import videointelligence
import io
import sys
import mysql.connector

def description(ID,imgNum):
	video_client = videointelligence.VideoIntelligenceServiceClient()
	features = [videointelligence.enums.Feature.LABEL_DETECTION]

	##Read the video with Google Vision API
	with io.open('C:/Users/Julie Park/Desktop/BU/F18_EC602/Week1/Assginment1/EC601/miniProject1/movie.mp4', 'rb') as video:
	#with io.open('/media/sf_Assginment1/EC601/miniProject1/movie.mp4', 'rb') as video:
		print("Opening Video")
		input_content = video.read()

		##API result
		try:
			operation = video_client.annotate_video(features=features, input_content=input_content)
			print('\nProcessing Video for label Annotations')
			result = operation.result(timeout=90)
			print('\nFinished processing.')

		except Exception as e:
			print("Error")
			print(e)
			exit()

	print("description almost DONEEEEE")
	##Display analysis
	label = ""
	num = 0
	segment_labels = result.annotation_results[0].segment_label_annotations

	for i, segment_label in enumerate(segment_labels):
		print('Video Label Description: {}'.format(segment_label.entity.description))
		label = label + segment_label.entity.description+","
		num = num + 1
		for category_entity in segment_label.category_entities:
			print('\tLabel Category Description: {}'.format(category_entity.description))


	#insert to mysql db
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="",auth_plugin='mysql_native_password')
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS miniProject3")
	mycursor.execute("use miniProject3")
	#sql = "INSERT INTO user_data (ID, ImgNum, Label, Label_Num) VALUES (%s, %s,%s,%s)"
	sql = "INSERT INTO user_data (ID, ImgNum, Label) VALUES (%s, %s,%s)"
	label = label[:-1]
	val = (ID, imgNnum, label)
	mycursor.execute(sql, val)

	mydb.commit()

	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["mydatabase"]
	mycol = mydb["users"]
	mydict = { "ID": ID, "ImgNum": imgNum,"Label":label,"Label_Num":num }
	x = mycol.insert_one(mydict)
