#!/usr/bin/env python
from beginner_tutorials.srv import *
import rospy


def handle_example(req):
	locations = []
	print "Returning list: "
	#print locations 
	return locations


def example_server():
	rospy.init_node('example_server')
	s = rospy.Service('example_server', example, handle_example)
	print "Ready to print example."
	rospy.spin()

if __name__ == "__main__":
	example_server()
