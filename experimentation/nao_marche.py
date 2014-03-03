import sys

from naoqi import ALProxy

def main():
    IP = "192.168.1.3"
    PORT = 9559

    motion = ALProxy("ALMotion", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)

    motion.wakeUp()

    posture.goToPosture("StandInit",1)

    motion.moveTo(0.5,0,0)

    motion.moveTo(-0.5,0,0)

    motion.rest()

main()
