#!/usr/bin/env python
from beginner_tutorials.srv import *
import sys
import rospy

def example_client():
	rospy.wait_for_service('example_server')
	try:
		example_server = rospy.ServiceProxy('example_server', example)
		resp1 = example_server()
		return resp1
		print resp1
	except rospy.ServiceException, e:
         	print "Service call failed!: %s"%e

def usage():
	return "usage"

if __name__ == "__main__":
	print usage()
	
	print "Reached main of client"
	print "%s" %(example_client())
	sys.exit(1)
