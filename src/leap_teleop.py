#!/usr/bin/env python

import rospy
from leap_motion.msg import leap
from leap_motion.msg import leapros
from geometry_msgs.msg import Twist


teleop_topic = '/cmd_vel'


reverse_speed = -0.5
stop_speed = 0
forward_speed = 0.5

right_turn = -0.5
stop_turn = 0
left_turn = 0.5

pitch_positive_threshold = 20
pitch_negative_threshold = -20

roll_negative_threshold = -60
roll_positive_threshold = 60


# Callback of the ROS subscriber, just print the received data.
def callback_ros(data):
    global pub

    msg = leapros()
    msg = data
    
    roll = msg.ypr.x
    pitch = msg.ypr.y
    yaw = msg.ypr.z

    twist = Twist()

    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0

#Just sending Twist message
   
    if(pitch > pitch_positive_threshold and pitch < pitch_positive_threshold + 90):
	    twist.linear.x = reverse_speed; twist.linear.y = 0; twist.linear.z = 0
	    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
            rospy.loginfo("Pitch positive. Moving Backwards")
    
    elif(pitch < pitch_negative_threshold and pitch > pitch_negative_threshold - 90):
	    twist.linear.x = forward_speed; twist.linear.y = 0; twist.linear.z = 0
	    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
            rospy.loginfo("Pitch negative. Moving Forward")

    
    elif(roll > roll_positive_threshold and roll < roll_positive_threshold + 90):
	    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = left_turn
            rospy.loginfo("Roll positive. Moving Left")

    
    elif(roll < roll_negative_threshold and roll > roll_negative_threshold - 90):
	    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = right_turn
            rospy.loginfo("Roll negative. Moving Right")
    

    pub.publish(twist)

    rospy.loginfo(rospy.get_name() + ": Roll %s" % msg.ypr.x)
    rospy.loginfo("\n")
    rospy.loginfo(rospy.get_name() + ": Pitch %s" % msg.ypr.y)
    #rospy.loginfo("\n")
    #rospy.loginfo(rospy.get_name() + ": Yaw %s" % msg.ypr.z)
    #rospy.loginfo("\n")




# Yes, a listener aka subscriber ;) obviously. Listens to: leapmotion/data
def listener():
    global pub
    rospy.init_node('leap_sub', anonymous=True)
    rospy.Subscriber("leapmotion/data", leapros, callback_ros)
    pub = rospy.Publisher(teleop_topic, Twist, queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    listener()
