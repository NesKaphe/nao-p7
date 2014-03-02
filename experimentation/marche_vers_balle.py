import sys
import time

from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker

from optparse import OptionParser

NAO_IP = "192.168.1.3"
MarcheBalle = None
memory = None
track = None
#i = 0

class MarcheBalleModule(ALModule):
	""" Module pour marcher vers une balle

    	"""

	def __init__(self,name):
        	ALModule.__init__(self,name)
		self.motion = ALProxy("ALMotion")
		global memory
		memory = ALProxy("ALMemory")
        	memory.subscribeToEvent("redBallDetected", "MarcheBalle", "detection")

	def detection(self, *_args):
		"""global i
		print "UNE BALLE!!!!!", i
		i += 1"""
		try:
			memory.unsubscribeToEvent("redBallDetected", "MarcheBalle")
			global track
			#print track.getPosition()
			position = track.getPosition()
			dist = position[2]
			#print dist
			angle = self.motion.getAngles("HeadYaw",True)

			#print "Yaw : ", yaw, " ; Pitch: ", pitch
			if dist>0.3:
				print "je marche !"
				self.motion.moveTo(0.2,0,0)
			else:
				print "je ne bouge pas"

			memory.subscribeToEvent("redBallDetected", "MarcheBalle", "detection")
		#except ALMemory::unsubscribeToEvent,e:
		#	print "toto

		except Exception,e:
                	print "L'exception est : ", e


def main():
#	IP = "192.168.1.3"
#	PORT = 9559

	parser = OptionParser()
	parser.add_option("--pip", help="Parent broker port. The IP address or your robot", dest="pip")
	parser.add_option("--pport", help="Parent broker port. The port NAOqi is listening to", dest="pport", type="int")
	parser.set_defaults(pip=NAO_IP, pport=9559)

	(opts, args_) = parser.parse_args()
	pip   = opts.pip
	pport = opts.pport

	# We need this broker to be able to construct
	# NAOqi modules and subscribe to other modules
	# The broker must stay alive until the program exists
	myBroker = ALBroker("myBroker", "0.0.0.0", 0, pip, pport)
	
	global track
	track = ALProxy("ALRedBallTracker", pip, pport)
	motion = ALProxy("ALMotion", pip, pport)
	posture = ALProxy("ALRobotPosture", pip, pport)

	motion.setStiffnesses("Head", 1.0)
	posture.goToPosture("StandInit",0.5)

	global MarcheBalle
	MarcheBalle = MarcheBalleModule("MarcheBalle")
	#time.sleep(15)
	track.startTracker()
	try:
		while True:
			pass
		    
    	except KeyboardInterrupt: #Quand on fait un ctrl+c
		print
		print "Interrupted by user, shutting down"
		myBroker.shutdown()
		#posture.goToPosture("LyingBack", 0.5) #on se couche sur le dos avant de couper les moteurs
		motion.rest()
		sys.exit(0)

main()
		
		
