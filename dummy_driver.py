#!/usr/bin/env python
#-- coding:utf-8 --

import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('dummy_driver', anonymous=True)

pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)

motor = Int32MultiArray()

while not rospy.is_shutdown():
    motor.data = [-10, 50]
    pub.publish(motor)

