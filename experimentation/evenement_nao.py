import sys
import time

from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker

from optparse import OptionParser

NAO_IP = "192.168.1.3"

HumanGreeter = None
memory = None

class HumanGreeterModule(ALModule):
    """ Tentative de reconnaissance faciale

    """
    def __init__(self,name):
        ALModule.__init__(self,name)
        
        self.tts = ALProxy("ALTextToSpeech") # Pour faire parler le robot
        self.posture = ALProxy("ALRobotPosture") # Pour changer la posture du robot
        
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")

    def onFaceDetected(self, *_args):
        """Appele a chaque fois qu'un visage est detecte 
        (Bug, il detecte des visages alors qu'il n'y en a pas....)

        """

        #On retire la gestion de l'evenement pendant la duree ou on le traite
        memory.unsubscribeToEvent("FaceDetected", "HumanGreeter")

        self.tts.say("Salut ! Comment ca va ?")
        self.tts.say("J'ai trop la forme !")
        #On remet la gestion de l'evenement une fois termine
        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")


def main():
    """ Main entry point (cette partie du code (ALBroker, OptionParser, a ete reprise d'ici :
    https://community.aldebaran-robotics.com/doc/1-14/dev/python/reacting_to_events.html
    )
    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    motion = ALProxy("ALMotion", pip, pport)
    posture = ALProxy("ALRobotPosture", pip, pport)
    tts = ALProxy("ALTextToSpeech", pip, pport)

    motion.wakeUp()

    posture.goToPosture("StandInit", 0.5)

    try:
        while True:
            time.sleep(1)
            tts.say("Rien")
    except KeyboardInterrupt: #Quand on fait un ctrl+c
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        posture.goToPosture("LyingBack", 0.5) #on se couche sur le dos avant de couper les moteurs
        motion.rest()
        sys.exit(0)
    

main()
