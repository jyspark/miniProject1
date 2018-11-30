# miniProject1 & miniProject3

This project was created for class EC601 at Boston University in F18.
The project takes a twitter handle from the user, downloads the images, converts the images to a video, and analyzes the video.
The project contains:
  1. getandread.py - Takes a twitter handle from the user
  2. mediaURLs.py - gets tweets from getandread.py and extracts imageURLs from the tweets
  3. getimage.py - creates a folder and takes the list of the images to download
  4. FFmpeg.py - converts the images to a video using FFmpeg
  5. description.py - analyzes the video using Google Vision API

##The project can be run by running getandread.py file:
##python getandread.py 


Additionally, miniProject3 has been added using mini3 branch.
The goal of miniProject3 was to implement databases of mySQL and MongoDB.
The project contains:
  1. mySQL_main.py - Runs the program and writes data on mySQL databases
  2. mongodb.py - Runs the program and write data on MongoDB databases
  
The project can be run by running either mySQL_main.py or mongodb.py
  
 Requirements:
  1. import tweepy
  2. import google videointelligence
  3. import mysql.connector
  4. import mongodb
