from naoqi import ALProxy

#destine a mettre au repos les moteurs du robot


IP = "192.168.1.3"
PORT = 9559

motion = ALProxy("ALMotion", IP , PORT)
motion.rest()


