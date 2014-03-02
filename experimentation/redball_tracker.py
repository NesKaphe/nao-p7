"""
This example shows how to use ALRedBallTracker.
It is launched for a little while, then stopped.
"""

import sys
import time
from naoqi import ALProxy

if (len(sys.argv) < 2):
    print "Usage: 'python %s IP [PORT]'" % (__file__)
    sys.exit(1)

IP = sys.argv[1]
PORT = 9559
if (len(sys.argv) > 2):
    PORT = sys.argv[2]


print "Connecting to", IP, "with port", PORT
motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP , PORT)
#video = ALProxy("ALVideoRecorder", IP, PORT)
redBallTracker = ALProxy("ALRedBallTracker", IP, PORT)

# First, set Head Stiffness to ON.
motion.setStiffnesses("Head", 1.0)
posture.goToPosture("StandInit",0.5)
# Then, start tracker.
redBallTracker.startTracker()

print "ALRedBallTracker successfully started, now show your face to Nao!"
print "ALRedBallTracker will be stopped in 60 s."

#Tentative d'enregistrement de la camera
#video.startRecording("/home/neskaphe/Master/Semestre2/ProjetLong/projet-nao-dias-charasson/experimentation/", "VideoTest")

compteur = 20
while compteur>0:
	print redBallTracker.getPosition() #on regarde la position de la balle pour le nao
	compteur -= 1
	time.sleep(1)


#video.stopRecording()


# Stop tracker and remove head stiffness.
redBallTracker.stopTracker()
motion.setStiffnesses("Head", 0.0)
motion.rest()

print "ALRedBallTracker stopped."
