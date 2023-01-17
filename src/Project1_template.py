#!/usr/bin/env python3

######## Project 1 for HRSE ########
######## Uploading data to ThingSpeak Platform while manual driving the TB3 ########

# Import necessary packages needed to send data
from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import thingspeak
from time import sleep
from math import isnan

# Import necessary packages for TB3
import rospy
from nav_msgs.msg import Odometry

# defining field variables (to send to ThingSpeak)
px = 0
py = 0
pz = 0
ox = 0
oy = 0
oz = 0
ow = 0

#####  ThingSpeak Channel Settings #####

# The ThingSpeak Channel ID
# Replace this with your Channel ID
channelID = "XXXXXX"

# The Write API Key for the channel
# Replace this with your Write API key
apiKey = "XXXXXXXXXXXXXXXXXXXXX"

channel = thingspeak.Channel(id=channelID, api_key=apiKey)

#####   End of user configuration   #####


###### Start of functions ######

def callback(msg):				#define a function called 'callback' that receives a parameter named 'msg'
	print (msg.pose.pose)

	global px, py, pz, ox, oy, oz, ow
	px = msg.pose.pose.position.x
	py = msg.pose.pose.position.
	pz = msg.pose.pose.position.

	ox = msg.pose.pose.orientation.x
	oy = msg.pose.pose.orientation.
	oz = msg.pose.pose.orientation.
	ow = msg.pose.pose.orientation.

rospy.init_node('pose_data_collection')			# Initiate a Node called 'pose_data_collection'

while not rospy.is_shutdown():
	
	odom_sub = rospy.Subscriber("/topicname", Odometry, callback)

	##### Send pose data to ThingSpeak #####

	# build the payload string
	channel.update({'field1': str(XXX), 'field2': str(XXX), 'field3': str(XXX), 'field4': str(XXX), 'field5': str(XXX), 'field6': str(XXX), 'field7': str(XXX)})

	###################################

rospy.spin()


