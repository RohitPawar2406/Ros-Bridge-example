#!/usr/bin/env python3

import rospy
from my_robot_msgs.msg import HardwareStatus, CustomMessage

if __name__ == '__main__':
	rospy.init_node("hardware_status_publisher")

	pub = rospy.Publisher("/my_robot/hardware_status", CustomMessage, queue_size=10)

	rate = rospy.Rate(5)

	while not rospy.is_shutdown():
		msg = CustomMessage()
		msg.value = 1.0
		print(msg.value)
		pub.publish(msg)
		rate.sleep()
