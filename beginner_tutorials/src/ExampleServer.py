#!/usr/bin/env python
from beginner_tutorials.srv import *
import rospy
from std_msgs.msg import String 

class ExampleServer:
	def __init__(self):
		self.poi = None


	def handle_example(self, request):
		retlist = []
	
 		nextString = String()
		nextString.data = "strings"
		retlist.append(nextString)

		return exampleResponse(retlist)
			


	def spin(self):
		rospy.init_node('example_server')
		s = rospy.Service('example_server', example, self.handle_example)
		print "Ready to print example."
		rospy.spin()

if __name__ == "__main__":
	example_server = ExampleServer()
	example_server.spin()
