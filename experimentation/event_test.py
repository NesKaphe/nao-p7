import sys
import almath
import time

from naoqi import ALProxy

def main():
	IP = "192.168.1.3"
	PORT = 9559
	try:
		memory =  ALProxy("ALMemory", IP , PORT)
		motion = ALProxy("ALMotion", IP , PORT)
		posture = ALProxy("ALRobotPosture", IP , PORT)
		#print "list envents" , memory.getEventList()#donne la list des evenements
		motion.wakeUp()
		posture.goToPosture("StandInit",0.5)
		
		
		print "historique des evenements", posture.getEventHistory('robotPoseChanged')

	except Exception,e:
		print "\n!!!!probleme!!!!"
		#speech.say("Oulala je vihun de beuguer!")

	motion.rest()
main()
