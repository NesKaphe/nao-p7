import sys
import almath
import time

from naoqi import ALProxy

def main():
        #IP = "192.168.1.3"
		IP = "169.254.28.144"
        PORT = 9559

        try:
                motion = ALProxy("ALMotion", IP , PORT)
                posture = ALProxy("ALRobotPosture", IP , PORT)
                speech = ALProxy("ALTextToSpeech", IP , PORT)

                motion.wakeUp()

                posture.goToPosture("StandInit",0.5)


                motion.closeHand('RHand')

                #names  = "HeadYaw"
                names   = "LShoulderPitch"
                angles  = -30.0*almath.TO_RAD
                frac    = 0.1 #10% de le vitesse max

                angle_courrant = motion.getAngles("LShoulderPitch" , True)
                print "l'angle vaut :", angle_courrant


                motion.setAngles(names,angles,frac)
                time.sleep(2)
                #motion.setAngles(names,angle_courrant,frac)


                motion.setStiffnesses("LArm",0.05)
                posture.goToPosture("Sit",0.5)

        except Exception,e:
                print "probleme"
                speech.say("Oulala je vihun de beuguer!")

        motion.rest()
        speech.say("Au revoir !")


main()
