from google.cloud import videointelligence
import io
import sys


video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]

with io.open('/media/sf_Assginment1/EC601/miniProject1/video.mp4', 'rb') as video:
	print("Opening Video")
	input_content = video.read()
try: 
	operation = video_client.annotate_video(features=features, input_content=input_content)
	print('\nProcessing Video for label Annotations')
	result = operation.result(timeout=90)
	print('\nFinished processing.')
except Exception as e:
	print("Error")
	print(e)
	exit()

segment_labels = result.annotation_results[0].segment_label_annotations

for i, segment_label in enumerate(segment_labels):
	print('Video Label Description: {}'.format(segment_label.entity.description))
	for category_entity in segment_label.category_entities:
		print('\tLabel Category Description: {}'.format(category_entity.description))